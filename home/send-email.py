# 教學: https://www.youtube.com/watch?v=YQboCnlOb6Y
# 1. 寄送email的程式
# 2. 準備訊息物件設定
import email.message
msg = email.message.EmailMessage()
msg["From"] = "georgiawang5332@gmail.com"  # 寄件人
# msg["To"] = "nunumary5798@gmail.com"  # 有效收件人
msg["To"] = "wleejan982@hotmail.com"  # 有效收件人
msg["Subject"] = "你好，玥玥"
# 3. 寄送純文字內容
# msg.set_content("TEST 試試看")
# 4. 寄送必較多樣式的內容(html)
msg.add_alternative("<h3>優惠券</h3>滿五百送一百，限時優惠要買要快!", subtype="html")
# 5. 連線到SMTP Server, 驗證寄件人的身分並發送郵件
import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465) # 到網路上搜尋 gmail(yahoo hotmail) smtp server，會有各自server or port:465(端口) 號碼是多少
# 就可以建立跟gmail郵件伺服器連線
server.login("georgiawang5332@gmail.com", "uusnymglbxkyyqfy")
# ("帳號", "應用程式產生的密碼") 安全性=>登入google=>應用程式密碼=>輸入信箱密碼=>選取應用程式(其他)=>選取裝置(其他-自訂名稱)=>產生=>拍照，因為備用密碼只會出現一次
server.send_message(msg)#送出郵件
server.close()#關閉連線

# 登入: C:\Users\wleej\PycharmProjects\meatFoodManager\home>python send-email.py

