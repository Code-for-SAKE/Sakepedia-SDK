# Sakepedia
SakepediaのAPIをプログラムから利用しやすくするためのPythonSDK

Sakepediaはみんなでつくる日本酒オープンデータです。
Nuxt.js版が以下で稼働しています。

https://sakepedia.code4sake.org/

このサイトのAPIにPythonからアクセスするパッケージです。

## 機能
- 酒蔵データの取得
- 銘柄データの取得
- 日本酒データの取得、更新、登録

*更新および登録には、Sakepediaへのユーザー登録とJWTの発行が必要です。
JWTの有効期限にご注意ください。*

## 使用方法

### 日本酒データの登録、既にあれば更新

```
JWT = "JWT issued with your own Sakepedia account"
api = sakepedia.SakepediaAPI(JWT)

sake = sakepedia.SakeData()
sake.brewery = "test brewery"
sake.brand =  "test brand"
sake.url = "https://testbrewery.co.jp/testbrand/sake"
sake.name = "test sake bottle"
sake.description = "test description"

res = api.saveSakeData(sake)
```


## パッケージのビルドとアップロード

```
# pip install twine
# pip install wheel
```

```
# rm -rf dist/*
# python setup.py sdist
# python setup.py bdist_wheel
```

```
# twine upload --repository testpypi dist/*
# twine upload --repository pypi dist/*
```
