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

## アクセストークン取得手順
①下記にアクセス
https://notify-bot.line.me/ja/

②ログイン→マイページ
![IMG_4285.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/453711/5e6237ca-fc38-e300-14d8-4948b401b623.png)

![IMG_4286.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/453711/79928e12-6732-6958-3864-0ed3e65a980c.png)

③トークンを発行を押下します。
![IMG_4287.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/453711/cf0868f1-534f-2009-461d-d7acc080088f.png)

④トークンを発行する、にてトークン名と通知を送信するトークルームを選択、発行するを押下します。
　ex: トークン名→明日の予定 通知を送信するトークルームを選択
![IMG_4289.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/453711/50aa5678-9b37-4b43-5f1a-e2621a9d43d6.png)

⑤トークンが発行されるため、必ずコピーをします。
![IMG_4290.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/453711/9e291332-d3b2-2efc-1a82-8d08da95b898.png)