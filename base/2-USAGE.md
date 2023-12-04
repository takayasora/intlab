# 使用法

1. 〇〇の設定を行います。
2. 以下のコマンドを実行して〇〇します。

```bash
$ command-to-run
```
# Lineに通知するには
Line Notifyというツールを使用してメッセージを配信します。

## LINE Notifyとは
APIにより連携することで、外部Webサービスやアプリケーションなどからの通知をLINEアカウントのメッセージを通じてユーザーに配信できるサービスです。

毎度取得手順を忘れるので備忘録として残します。
手順等に間違いがございましたら、ご教示よろしくお願いいたします🙇‍♀️

## 準備物
LINEアカウント

## Lineでの作業
①[こちらのページ](https://notify-bot.line.me/ja/)にアクセス！

②ログインする
![IMG_4285.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/453711/5e6237ca-fc38-e300-14d8-4948b401b623.png)

③マイページに入る
![IMG_4286.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/453711/79928e12-6732-6958-3864-0ed3e65a980c.png)

④トークンを発行を押下します。
![IMG_4287.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/453711/cf0868f1-534f-2009-461d-d7acc080088f.png)

⑤トークンを発行する、にてトークン名と通知を入力します（今回はIntlab）<br>
送信するトークルームを選択、発行するを押下します。
![IMG_4289.png](https://gyazo.com/291266f4cf3f75514a2dcc06190a3191.png)

⑥トークンが発行されるため、必ずコピーをします。
![IMG_4290.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/453711/9e291332-d3b2-2efc-1a82-8d08da95b898.png)

## エディターでの作業
setupmacroを開く。


## Webページをアップデート方法
### 1.インストーラーのダウンロード
下記サイトからインストーラーをダウンロードします。
http://nodejs.org/

Download > Windows Installer をクリックするとカレントバージョンの自身のPCに合わせたインストーラーがダウンロードされます。
明示的に、32bit版、64bit版、バイナリ版など指定したい場合は、それぞれの項目をクリックするとダウンロードが開始します。
![031.png](https://qiita-image-store.s3.amazonaws.com/0/81226/f4d3989f-b714-e58e-513f-0e8fbdfbcfe8.png)

### 2.インストール
実行します。
![image](https://qiita-image-store.s3.amazonaws.com/0/81226/d30d1e36-0b62-0aa5-70c7-f98ace44e332.png)

Nextをクリック。
![image](https://qiita-image-store.s3.amazonaws.com/0/81226/8e5b3a94-3614-a839-d9b8-ae18b91d2ad2.png)

ライセンス規約へ同意しNextをクリック。
![image](https://qiita-image-store.s3.amazonaws.com/0/81226/1687a4a7-dd8f-ea82-715b-d2eee263f7d0.png)

インストールフォルダを選択しNextをクリック。（インストール先は任意の場所でOKです）
![image](https://qiita-image-store.s3.amazonaws.com/0/81226/3f926063-c284-b628-062c-76f73eb3064f.png)

インストールするコンポーネントを選択しNextをクリック。基本デフォルトでOKです。
![image](https://qiita-image-store.s3.amazonaws.com/0/81226/3d6bccc4-19f4-8923-3db4-152005748de8.png)

Installをクリックでインストールが開始します。
![image](https://qiita-image-store.s3.amazonaws.com/0/81226/8dea0118-e75a-ded0-7291-a23b8c9d03be.png)

![image](https://qiita-image-store.s3.amazonaws.com/0/81226/79ae1d54-8d39-dd78-1641-340c9a634c2b.png)

特に問題がなければインストールが完了します。Finishをクリック。
![image](https://qiita-image-store.s3.amazonaws.com/0/81226/7dd648cf-972a-caa6-3405-9ebcedc3bf87.png)

コマンドプロンプトから下記のコマンドを実行します。
`node --version`

バージョンが表示されればインストールは成功です。
![image](https://qiita-image-store.s3.amazonaws.com/0/81226/df7603c8-078d-197e-17a8-d84c52c935c9.png)

もうひとつ、npmも同時にインストールされているはずなのでこちらもチェックします。
コマンドプロンプトから下記のコマンドを実行します。
`npm --version`

こちらも、バージョンが表示されればインストールは成功です。
![image](https://qiita-image-store.s3.amazonaws.com/0/81226/84d3dccc-f543-817e-2f9e-230f3100ad44.png)

### Visual Studio Codeで拡張機能をインストール
次に拡張機能をインストールしていきます。
![image](https://gyazo.com/d762038878d7570dfe58c5c47a5c74b6.png)

![image](https://gyazo.com/6d832687fe48c08695d237fbb7fec120.png)

![image](https://gyazo.com/1a9e60ebe0d8e2fcd93290ca35b33f9b.png)


```npm
npm -i
npm -run build
```
