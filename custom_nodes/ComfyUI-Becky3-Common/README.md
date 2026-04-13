# ComfyUI-Becky3-Common

ComfyUI 用の汎用ユーティリティノード集です。

外部ライブラリ不要。Python 標準ライブラリのみで動作します。

## インストール

`ComfyUI-Becky3-Common` フォルダを `ComfyUI/custom_nodes/` にコピーして、ComfyUI を再起動するだけです。

## ノード一覧

### Show Text

受け取った文字列をノード上に表示するデバッグ用ノードです。入力をそのまま出力としてパススルーします。

| パラメータ | 説明 |
|---|---|
| `text` | 表示する文字列（外部接続） |

**出力:** `text` (STRING) — 入力をそのまま返す
