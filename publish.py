"""Publish pinned upstream weights, configs and original attribution cards.

The extension never runs this script. An incomplete or mismatched release
stays a draft. Published tags are immutable; reruns only verify their files.
"""
import concurrent.futures
import hashlib
import json
import os
import pathlib
import subprocess
import time
import urllib.request

REPO = os.environ.get('GH_REPO', 'Masih-Roughani/Piper-TTS-voice-assets')
TAG = 'v3'
DIRECTORY = pathlib.Path('downloads')
DIRECTORY.mkdir(exist_ok=True)
CATALOG = json.loads(pathlib.Path('voices-v3.json').read_text(encoding='utf-8'))

def gh(*args):
    return subprocess.check_output(['gh', *args], text=True)

def releases():
    pages = json.loads(gh('api', f'repos/{REPO}/releases', '--paginate', '--slurp'))
    return [release for page in pages for release in page]

release = next((item for item in releases() if item['tag_name'] == TAG), None)
if release is None:
    gh('release', 'create', TAG, '--repo', REPO, '--draft', '--title', 'Multilingual Piper voices', '--notes-file', 'RELEASE_NOTES.md')
    release = next(item for item in releases() if item['tag_name'] == TAG)
existing = {asset['name']: asset for asset in release['assets']}

def sha256(file):
    digest = hashlib.sha256()
    with file.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()

def download(url, file):
    for attempt in range(5):
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'Piper-voice-assets-publisher'})
            with urllib.request.urlopen(request, timeout=180) as response, file.open('wb') as target:
                for chunk in iter(lambda: response.read(1024 * 1024), b''):
                    target.write(chunk)
            return
        except Exception:
            if attempt == 4:
                raise
            time.sleep(2 ** attempt)

def upload(file):
    digest, size = sha256(file), file.stat().st_size
    old = existing.get(file.name)
    if old and old['size'] == size and old.get('digest') == 'sha256:' + digest:
        print('Verified existing', file.name, flush=True)
        return file.name, size, digest
    if not release['draft']:
        raise ValueError('Published asset differs: ' + file.name)
    for attempt in range(4):
        try:
            gh('release', 'upload', TAG, str(file), '--repo', REPO, '--clobber')
            print('Uploaded', file.name, flush=True)
            return file.name, size, digest
        except subprocess.CalledProcessError:
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)

def voice_assets(item):
    id, voice = item
    if f'/download/{TAG}/' not in voice['model']:
        return []
    name = voice['model'].rsplit('/', 1)[1]
    model = DIRECTORY / name
    # The first fallback is an immutable, official upstream URL.
    download(voice['modelFallbacks'][0], model)
    if model.stat().st_size != voice['bytes'] or sha256(model) != voice['sha256']:
        raise ValueError('Invalid model: ' + id)
    config = DIRECTORY / (name + '.json')
    download(voice['sourceConfig'], config)
    settings = json.loads(config.read_text())
    if settings.get('phoneme_type', 'espeak') != 'espeak' or not settings.get('espeak', {}).get('voice'):
        raise ValueError('Unsupported phonemizer: ' + id)
    card = DIRECTORY / name.replace('.onnx', '.MODEL_CARD')
    source_card = voice['sourceConfig'].rsplit('/', 1)[0] + '/MODEL_CARD'
    if id == 'mana':
        source_card = voice['modelCard']
    download(source_card, card)
    if not card.stat().st_size:
        raise ValueError('Empty model card: ' + id)
    return [upload(file) for file in (model, config, card)]

expected = []
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for assets in pool.map(voice_assets, CATALOG['voices'].items()):
        expected.extend(assets)
expected.append(upload(pathlib.Path('voices-v3.json')))
updated = next(item for item in releases() if item['tag_name'] == TAG)
assets = {asset['name']: asset for asset in updated['assets']}
for name, size, digest in expected:
    asset = assets.get(name, {})
    if asset.get('size') != size or asset.get('digest') != 'sha256:' + digest:
        raise ValueError('Release verification failed: ' + name)
if updated['draft']:
    gh('release', 'edit', TAG, '--repo', REPO, '--draft=false', '--notes-file', 'RELEASE_NOTES.md')
print(f'Published and verified {len(expected)} assets for {len(CATALOG["languages"])} languages', flush=True)
