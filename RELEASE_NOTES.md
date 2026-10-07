The catalog covers 49 language families. Mana and Ryan High are bundled with Piper Page Reader; other production voices download on demand and remain cached on the device.

This release adds 46 eSpeak-compatible languages, Ganji and Mana, together with their original configuration and attribution cards. Existing Gooya/Ryan assets remain pinned to v1 and Thorsten to v2. Model sizes and SHA-256 digests are listed in voices-v3.json and checked before inference.

All 46 newly added voices produced non-silent WAV samples using the same eSpeak WASM, ONNX Runtime Web WASM and synthesis functions used by the extension. This is a runtime compatibility check; listening quality varies by voice. Lada's legacy Ukrainian ID map skips an unsupported combining dental mark while preserving its base phones.

Japanese, Hebrew, Lithuanian and Thai require phonemizers unavailable in the bundled eSpeak frontend and are excluded. Original model/dataset license terms apply; this release does not relicense upstream voices.
