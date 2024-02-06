"""gmailの自動送信"""

# メリ：処理が容易のため初心者にとって改変しやすい
# デメ：ユーザーのセキュリティレベルを下げる必要がある。
# https://news.mynavi.jp/article/zeropython-51/

import smtplib, ssl
from email.mime.text import MIMEText

# 以下にGmailの設定を書き込む★ --- (*1)
gmail_account = "xxxxx@gmail.com"
gmail_password = "xxxx"
# メールの送信先★ --- (*2)
mail_to = "tukaii0424@gmail.com"

# メールデータ(MIME)の作成 --- (*3)
subject = "ここにタイトルを記入"
body = "メール送信テスト！！"
msg = MIMEText(body, "html")
msg["Subject"] = subject
msg["To"] = mail_to
msg["From"] = gmail_account

# Gmailに接続 --- (*4)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
    context=ssl.create_default_context())

# server.login(gmail_account, gmail_password)
# server.send_message(msg) # メールの送信
# print("ok.")


# 複数回送信する嫌がらせ用
i=0
while i <3:
    server.login(gmail_account, gmail_password)
    server.send_message(msg) # メールの送信
    print("ok.")
    i+=1