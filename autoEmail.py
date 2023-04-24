# email套件(Package)下的mime(Multipurpose Internet Mail Extensions)子套件，為網際網路媒體類型
# 定義了在網路上傳輸電子郵件的格式標準，在其底下的multipart子套件中
# MIMEMultipart類別能夠讓電子郵件的格式包含純文字或HTML的內容。
import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from time import sleep

from flask import Flask, request, render_template
from flask_mysql_connector import MySQL
import pymysql
from flask_login import LoginManager, UserMixin, confirm_login, login_user, logout_user, login_required, current_user

app = Flask(__name__)
mysql = MySQL(app)
app.secret_key = configparser.get('flask', '123456')

# 連接mysql
def get_conn():
    return pymysql.connect(
        host = '127.0.0.1', 
        user = 'root', 
        password = '12345678', 
        database = 'secondhand_bookweb', # 資料庫名稱(我改回這個名稱了，我用日期標記之後自己感覺不太好= =)
        charset = 'utf8'
    )
    
# 接收訂單成立的數據
@app.route('/purchase', methods=['POST'])
def purchase():
    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "輔大二手書網站交易成功"  #郵件標題
    content["from"] = "wsx2244667@gmail.com"  #寄件者(我們網站方)
    content["to"] = "request.values['A_SalerID']" #收件者(需要接值)
    content.attach(MIMEText("請將您的書籍放入1號櫃"))  #郵件內容


    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("wsx2244667@gmail.com", "gpitruqqyaubmocl")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)
    
    sleep(5)
    
    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "輔大二手書網站交易成功"  #郵件標題
    content["from"] = "wsx2244667@gmail.com"  #寄件者(我們網站方)
    content["to"] = "request.values['A_BuyerID']" #收件者(需要接值)
    content.attach(MIMEText("請前往1號櫃領取您的書籍"))  #郵件內容


    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("wsx2244667@gmail.com", "gpitruqqyaubmocl")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)
    
    