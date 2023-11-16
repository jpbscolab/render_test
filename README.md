# FastAPI test

## 動作させるには

サーバー環境とローカルテスト用サーバーがある

1. サーバー環境

render(https://dashboard.render.com/)にホストしている。Github()のリポジトリと連携させているので、Githubにコミットすると自動的にデプロイされる。

1.1. renderの設定(Pythonのバージョン)

Environmentから
PYTHON_VERSION  3.12.0
を設定


2. ローカルテスト用サーバー

このフォルダに移動して、`py .\main.py` を実行

