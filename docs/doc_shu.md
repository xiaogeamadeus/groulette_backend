# Backend 作業記録

担当: Wang, Shu
[toc]

## 大まかな流れ

- レストランデータベース

  1. Nearby Search で百万遍交差点を中心に 1km 範囲内のレストランを取得する  
     → 返り値: json ファイル
     - 詳細：結局ジャンル別 keyword で検索した 4/26
     - これから：ジャンル別検索結果をマージして、重複するものを削除する
  2. Details Search で 1 で検索したレストラン(place_id 使えば OK)の営業時間などより詳細な情報を取得する  
     → 　返り値: json ファイルにまとめる
  3. json ファイルを csv ファイルへ変換  
     → 返り値: csv ファイル
  4. csv ファイルを sqlite3 へ落として、データベースを作る
     → 返り値: 関係データベース

- API
  - 予定: Django を使う

## Google Places API

### Nearby Search

#### Response

responses に全部で以下の 4 つの key が含まれている。
html_attributions, next_page_token, results, status

店舗の名前が入ってるのは**results**  
results の中に各レストランの情報が入ってる
各レストランには **17 コの key**を持ってる

- key

  ```
  [u'rating', u'user_ratings_total', u'name', u'icon', u'price_level', u'geometry', u'opening_hours', u'place_id', u'plus_code', u'vicinity', u'photos', u'types', u'scope', u'icon_background_color', u'business_status', u'reference', u'icon_mask_base_uri']
  ```

- 必要な key

  - rating
  - user_ratings_total
  - name
  - place_id
  - vicinity
  - geometry-location

- 必要になるかもの key

  - photos-html_attributions
  - price_level
  - icon

- いらない key
  - types
  - plus_code
  - icon_background_color
  - icon_mask_base_uri
  - opening hours
    (true か false しかない、営業時間は Details で取得すること)
  - scope
  - business_status
  - reference

### レストランジャンル

0. Asian/Chinese1,2/Korean
1. Yakiniku
2. Ramen
3. Fast/Pizza/Humberger
4. (Wasyoku)Gyudon/Tempura/Udon/Teishoky/Suchi/Syokudo
5. (Yosyoku)Pasta/French/Italian
6. Izakaya/Yakitori
7. (そのほか)Family/Health/Vegan/cafe
   削除: noodles

## 環境構築

sqx の環境構築:
仮想環境: **groulette** (conda)

## git

- `git checkout {branch 名}`: branch へいく
- branch で作業して、push する
- github で `creat pull request`ボタンを押す
- merge request
- ターミナルで`git checkout origin/main`で main ブランチへ戻る
- `git pull` で更新されたリモートレポジトリをローカルに同期する
- `git checkout {branch 名}`で自分の作業ブランチに戻って作業を続ける
- `git branch`: 今いる branch を調べる (ローカル)
- `git branch -r`: リモート branch を調べる
- `git pull orgin {remote branch名}:{local branch名}`:　リモートブランチの更新をローカルブランチへ持ってくる

## Framework

- Django tutorial
- Database sqlite3

## データベース関係

### API

- 候補レストランを返す
  - 1. mode,genre,userid を受け取って、db から対応するデータを選ぶ
  - 2. mode 変数に基づき、レストラン順位を決めるアルゴリズムで 1 で得られたデータをソートする
  - 3. 上位 20 位を返す(name, genre, ID)

**ソース**

- create database: <https://www.sqlitetutorial.net/sqlite-python/creating-database/>
- view database/takbe: <https://www.youtube.com/watch?v=VKg1Dnz7GN0>
- general:
  - <https://www.geeksforgeeks.org/python-sqlite-insert-data/?ref=lbp>
  - <https://www.tutorialspoint.com/python_data_access/python_sqlite_delete_data.htm>
- add new column to the existing model
  - <https://www.dev2qa.com/how-to-add-new-model-field-to-exist-django-model/>
- modify existing data object
  - <https://www.geeksforgeeks.org/django-orm-inserting-updating-deleting-data/>
