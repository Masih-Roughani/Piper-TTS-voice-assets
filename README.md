# Piper Page Reader voice assets

This repository serves optional Piper ONNX voice weights through immutable GitHub Release assets. The browser extension source and bundled runtime live in a separate repository. Large ONNX files are release attachments, not Git history.

## Multilingual catalog

[voices-v3.json](voices-v3.json) lists 49 languages, 51 production voices, immutable upstream sources, file sizes and SHA-256 digests. [Release v3](https://github.com/Masih-Roughani/Piper-TTS-voice-assets/releases/tag/v3) carries the new weights, original configurations and attribution cards; existing weights remain in v1/v2.

Mana (Persian) and Ryan High (English) ship inside the extension. Every other voice downloads only when selected for reading or preview, then stays cached locally. The source repository never serves optional models. The interface can use any of the same 49 languages.

Japanese, Hebrew, Lithuanian and Thai require dedicated phonemizers and are excluded from this eSpeak build. The 46 new optional languages passed actual eSpeak WASM + ONNX Runtime Web WASM synthesis. Audio quality has not been subjectively certified across all languages.

The **Publish verified voices** workflow downloads pinned official weights, verifies their hashes, uploads configs/cards and checks every release asset before publishing. A failed run keeps v3 as a draft. Published assets cannot be changed by rerunning the script. This maintainer tooling is independent of the extension runtime.

## v1 assets

| File | Bytes | SHA-256 | Upstream |
| --- | ---: | --- | --- |
| `gooya-rizehpizeh-v2.onnx` | 63,516,051 | `3f85f450fc21415e1eddaa0aa894c667e76d14aa9a342c4e77f1f9009b96f170` | [Reza2kn/Gooya-RizehPizeh-v2](https://huggingface.co/Reza2kn/Gooya-RizehPizeh-v2) |
| `en_US-ryan-high.onnx` | 120,786,792 | `b3990d7606e183ec8dbfba70a4607074f162de1a0c412e0180d1ff60bb154eca` | [rhasspy/piper-voices Ryan High](https://huggingface.co/rhasspy/piper-voices/tree/main/en/en_US/ryan/high) |

The extension verifies size and SHA-256 before caching and using a downloaded model. Do not replace assets under the existing `v1` tag; publish a new version and update the extension's pinned URLs and checksums.

## Attribution and terms

Gooya's repository declares MIT. Ryan High's [model card](https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_US/ryan/high/MODEL_CARD) identifies its training dataset as **CC BY-NC-SA 4.0**. This repository preserves that attribution and does not assert broader rights to either voice. Check the source terms before commercial distribution.

Mana and Ganji are hosted in v3; only Mana is bundled in the current extension. Lessac High is excluded from the production catalog. Each other voice retains the terms in its original MODEL_CARD attachment. Hosting a model here does not relicense it or its training dataset.
