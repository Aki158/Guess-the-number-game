# Guess-the-number-game

## 🌱概要
数字当てゲーム

## ✨デモ
![output](https://github.com/Aki158/Guess-the-number-game/assets/119317071/73332152-0568-4e4b-ba21-47ce115ed08e)

## 📝説明
このゲームは、数字当てゲームです。

ランダムに設定された数字を推測してゲームのクリアを目指します!

ユーザーは、最初に 最小値/最大値/入力回数の上限値 を設定する必要があります。

設定した情報をもとにゲームの難易度が変わります。

最初は、最小値と最大値の間隔を小さくして難易度をeasyにすることをオススメします!

基本的な機能としては、初期設定/入力された数字の判定/メッセージの表示ができます。

## 🧰前提条件
このゲームを実行するには、下記ソフトウェアを事前にインストールしておく必要があります。

インストールされていない場合は、[インストール](#インストール)/[使用方法](#使用方法)/[使用例](#使用例)で記載されているコマンドが実行できませんので

必ずインストールしてから進めてください。

### Git
Gitがインストールされていない場合は、下記手順でインストールしてください。

1. ターミナルを起動する。<br>使用するOSによりターミナルの名称が異なりますので注意してください。<br>(例. Windows:コマンドプロンプト,mac:ターミナル)

2. Gitがインストールされているか確認する。<br>`git version 2.34.1` のように表示された場合は、Gitがインストールされています。<br>以降の手順はスキップしてください。<br>**また、ターミナルは引き続き使用しますので開いたままにしてください!**
```
git --version
```

3. システムを更新する
```
sudo apt-get update
```

4. Gitをインストールする
```
sudo apt install git
```

5. Gitがインストールされたことを確認する。<br>`git version 2.34.1` のように表示されていれば、Gitのインストールは完了です!
```
git --version
```

### Python 3.x
[Python](https://www.python.org/downloads/)の公式サイトからあなたのPCのOSに合わせて、ダウンロードしてください。

ダウンロードしたファイルを使用してインストールできます。

Pythonがインストールされているかは、下記コマンドで確認することができます。

`Python 3.10.12`のように表示されていれば、Pythonはインストールされています。

```
python3 --version
```

## 🍴インストール
### クローン
このゲームをあなたのPCで実行するために、クローンします。

クローンとは、このゲームの実行に必要なファイル(リポジトリのコンテンツ)をあなたのPCのローカル環境へコピーすることです。

下記手順でクローンしてください。

1. リポジトリをクローンする
```
git clone https://github.com/Aki158/Guess-the-number-game.git
```

2. クローンしたリポジトリへ移動する
```
cd Guess-the-number-game
```

## 🚀使用方法
1. ゲームを起動する
2. ゲームの指示に従い、数字を入力する
3. ゲームを遊ぶ
4. ゲームを終了する

## 🙋使用例
一通りの手順のイメージは[デモ](#デモ)を参考にしてください。

1. ゲームを起動する
```
python3 main.py
```
2. ゲームの指示に従い、数字を入力する。<br>今回は、下記のように情報を設定しました。
    - Please enter a minimum value (n) : `2`
    - Please enter a maximum value (m) : `5`
    - Choose a difficulty level between 0 and 2<br>easy  (Input : 0)<br>medium(Input : 1)<br>hard  (Input : 2)<br>Input : `0`
3. ゲームを遊ぶ。<br>`Enter a number between 2 and 5 : `の後に正解の数字を推測しながら入力する。<br>入力回数は、手順2.で設定した難易度によって変わります。
4. ゲームを終了する。<br>ゲームのクリアに関わらず、最後まで遊ぶとゲームが自動的に終了します。<br>ゲームを途中でやめたくなった場合は、`Ctrl + c`を入力してください。

## 💾使用技術
<table>
<tr>
  <th>カテゴリ</th>
  <th>技術スタック</th>
</tr>
<tr>
  <td>開発言語</td>
  <td>Python</td>
</tr>
<tr>
  <td rowspan=2>インフラ</td>
  <td>Ubuntu</td>
</tr>
<tr>
  <td>VirtualBox</td>
</tr>
</table>

## 👀機能一覧
![image](https://github.com/Aki158/Guess-the-number-game/assets/119317071/a5c18166-7806-47be-b9a7-9322c9336db0)

| 機能 | 内容 |
| ------- | ------- |
| メッセージの表示 | ゲームを進行するために、必要な情報をターミナルに表示します。 |
| 初期設定 | 下記情報をもとに、ゲームの難易度を決めます。<br>・Please enter a minimum value (n) : <br>・Please enter a maximum value (m) : <br>・Choose a difficulty level between 0 and 2<br>　easy  (Input : 0)<br>　medium(Input : 1)<br>　hard  (Input : 2)<br>　Input : |
| 入力された数字の判定 | 入力された数字とランダムに設定された数字が一致しているか判定します。 |
| 入力回数の上限値設定 | 初期設定のdifficulty levelにより入力回数の上限が下記のように決められます。<br>・easy : 5<br>・medium : 10<br>・hard : 15 |
| 入力回数のカウント | 入力された数字を判定するたびに、+1カウントします。 |
| ゲームの終了 | 下記条件に該当する場合は、ゲームが終了されます。<br>・入力された数字とランダムに設定された数字が一致した<br>・入力回数の上限に到達した |

## 📜作成の経緯
⭐️後で記載する!!!

作成した理由を記載する。

## ⭐️こだわった点
⭐️後で記載する!!!

テキストや参考にした記事などを再度読み返して技術の理解を深めてから書く。

ここがエンジニアに一番読んでもらいたい箇所なのでできるだけ詳細に書く。

## 📮今後の実装したいもの
- [ ] ゲームのセーブ機能追加
- [ ] ユーザーの登録

## 📑参考文献
### 公式ドキュメント
- [Python](https://docs.python.org/ja/3/)

### 参考にしたサイト
- [Python_Download](https://www.python.org/downloads/)
