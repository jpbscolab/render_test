# FastAPI test

## 動作させるには

サーバー環境とローカルテスト用サーバーがある

1. サーバー環境

render(https://dashboard.render.com/)にホストしている。
Github(https://github.com/jpbscolab/render_test/)のリポジトリと連携させているので、Githubにコミットすると自動的にデプロイされる。
Githubリポジトリにファイルを反映させるには、リポジトリのホーム画面の Add file > Update Files を選択して、ファイルを更新する。 

1.1. renderの設定(Pythonのバージョン)

Environmentから
PYTHON_VERSION  3.12.0
を設定


2. ローカルテスト用サーバー

環境が構築されていない場合は、環境構築から行う

2.1. 環境構築

- Python 3.12.xをインストール
- このフォルダに入り `py -m venv .venv` で仮想環境を作成
- `.\.venv\Scripts\Activate.ps1` で仮想環境をアクティブ化する
- `pip install -r requirements.txt`

2.2. 起動

このフォルダに移動して、`py .\main.py` を実行

2.3. テスト

http://127.0.0.1:8000
http://127.0.0.1:8000/docs



9. 参考資料

https://qiita.com/NasuPanda/items/2e4d0e6d4d3824e52754

https://www.shibutan-bloomers.com/python-libraly-pptx/988/#google_vignette

https://python-pptx.readthedocs.io/en/latest/
