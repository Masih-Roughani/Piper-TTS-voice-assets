# Piper Page Reader voice assets

This repository serves optional Piper ONNX voice weights through immutable GitHub Release assets. The browser extension source and bundled runtime live in a separate repository. Large ONNX files are release attachments, not Git history.

## v1 assets

| File | Bytes | SHA-256 | Upstream |
| --- | ---: | --- | --- |
| `gooya-rizehpizeh-v2.onnx` | 63,516,051 | `3f85f450fc21415e1eddaa0aa894c667e76d14aa9a342c4e77f1f9009b96f170` | [Reza2kn/Gooya-RizehPizeh-v2](https://huggingface.co/Reza2kn/Gooya-RizehPizeh-v2) |
| `en_US-ryan-high.onnx` | 120,786,792 | `b3990d7606e183ec8dbfba70a4607074f162de1a0c412e0180d1ff60bb154eca` | [rhasspy/piper-voices Ryan High](https://huggingface.co/rhasspy/piper-voices/tree/main/en/en_US/ryan/high) |

The extension verifies size and SHA-256 before caching and using a downloaded model. Do not replace assets under the existing `v1` tag; publish a new version and update the extension's pinned URLs and checksums.

## Attribution and terms

Gooya's repository declares MIT. Ryan High's [model card](https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_US/ryan/high/MODEL_CARD) identifies its training dataset as **CC BY-NC-SA 4.0**. This repository preserves that attribution and does not assert broader rights to either voice. Check the source terms before commercial distribution.

The Mana and Ganji weights ship with the development extension build and are not hosted here. Lessac High is excluded from this release because its [model card](https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_US/lessac/high/MODEL_CARD) points to separate Blizzard 2013 dataset terms.
