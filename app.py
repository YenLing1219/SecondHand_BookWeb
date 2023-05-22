import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb
import pymysql
import bcrypt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from time import sleep

import os
import pathlib
from flask import Flask, url_for, redirect,  render_template, request

import logging

logging.basicConfig(filename='error.log', level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = "abc123"

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'secondhand_bookweb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


# 取得目前檔案所在的資料夾 
SRC_PATH =  pathlib.Path(__file__).parent.absolute()
# 結合目前的檔案路徑和static及uploads路徑，取得儲存書籍照片資料夾(uploads)的位置
UPLOAD_FOLDER = os.path.join(SRC_PATH,  'static', 'uploads')
print(UPLOAD_FOLDER)


#最初的模板
"""
@app.route('/')
def hello_world():
    return 'Hello World! 上架: /book_create    修改書籍資訊: /book_update/(+B_BookID)    書籍列表: /book_display    搜尋書籍: /book_search/(+search_str)'
"""


# 首頁
@app.route('/')
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        logging.exception("Error occurred during index")
        return "An error occurred during index. Please check the error log for more information.", 500
    
# 顯示[用戶資訊]頁面
@app.route('/user_information')
def show_user_information():
    return render_template("user_information.html")

# 顯示[賣家介面]
@app.route('/user_information_sellerpage')
def show_user_information_sellerpage():
    
    sql = "select B_BookID, B_BookName, B_BookPic from book_information"
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        datas = cursor.fetchall()
    except Exception as e:
        logging.exception("Error occurred during user_information_sellerpage")
        return "An error occurred during user_information_sellerpage. Please check the error log for more information.", 500
    finally:
        conn.close()
    print(sql)
    return render_template("user_information_sellerpage.html", datas = datas)

#註冊功能實現，需要pip install bcrypt
@app.route('/register', methods=["GET", "POST"]) 
def register():
    try: 
        if request.method == 'GET':
            return render_template("register.html")
        else:
            A_Email = request.form['A_Email']
            A_Password = request.form['A_Password']
            A_StuID = request.form['A_StuID']
            A_RealNameVerify = request.form['A_RealNameVerify']
            A_BirthDate = request.form['A_BirthDate']
            A_Major = request.form['A_Major']


            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO account_manage (A_Email, A_Password, A_StuID, A_RealNameVerify, A_BirthDate, A_Major) VALUES (%s,%s,%s,%s,%s,%s)",(A_Email,A_Password,A_StuID,A_RealNameVerify,A_BirthDate,A_Major))
            mysql.connection.commit()
            session['A_StuID'] = request.form['A_StuID']
            session['A_Email'] = request.form['A_Email']
            return redirect(url_for('index'))
    except Exception as e:
        logging.exception("Error occurred during registration")
        return "An error occurred during registration. Please check the error log for more information.", 500
    
#登入功能實現，加上MySQL和Mysqldb
@app.route('/login',methods=["GET","POST"])
def login():
    print("Entering login function")
    try:
        if request.method == "POST":
            print("Handling POST request")
            A_StuID = request.form['A_StuID']
            A_Password = request.form['A_Password']
            
            print(f"Login attempt: A_StuID={A_StuID}, A_Password={A_Password}")
 
            curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            curl.execute("SELECT * FROM account_manage WHERE A_StuID=%s",(A_StuID,))
            user = curl.fetchone()
            curl.close()
            
            print(f"User fetched from database: {user}")
 
            if len(user) > 0:
                if A_Password == user["A_Password"]:
                    session['A_StuID'] = user['A_StuID']
                    session['A_Email'] = user['A_Email']
                    return render_template("index.html")
                else:
                    return "Error password and email not match"
            else:
                return "Error user not found"
        else:
            print("Handling GET request")
            return render_template("login.html")
    except Exception as e:
        logging.exception("Error occurred during login")
        print(e)
        return "An error occurred during login. Please check the error log for more information.", 500


#將session清除，登出功能
@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html")
    
# 連接mysql
def get_conn():
    return pymysql.connect(
        host = '127.0.0.1', 
        user = 'root', 
        password = '12345678', 
        database = 'secondhand_bookweb', 
        charset = 'utf8'
    )

# 新增資料
def insert_or_update_data(sql):
        conn = get_conn()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        finally:
            conn.close()



# [上架] 顯示網站
@app.route('/book_create')
def show_book_create():
    return render_template("book_create.html")

# [上架] 接收表單提交的數據
@app.route('/do_book_create', methods=['POST'])
def book_create():

    # 儲存圖片
    file = request.files['B_BookPic']
    if file.filename != '':
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        print('--picture save successfully:' + file.filename)

    

    print(request.form)
    B_BookName = request.form.get("B_BookName")
    B_ISBN = request.form.get("B_ISBN")
    B_Author = request.form.get("B_Author")
    B_BookVersion = request.form.get("B_BookVersion")
    B_BookMajor = request.form.get("B_BookMajor")
    B_LessonName = request.form.get("B_LessonName")
    B_BookPic = file.filename
    B_BookStatus = request.form.get("B_BookStatus")
    B_UsedStatus = request.form.get("B_UsedStatus")
    B_UsedByTeacher = request.form.get("B_UsedByTeacher")
    B_Extra_Info = request.form.get("B_Extra_Info")
    B_Price = request.form.get("B_Price")
    B_SalerID = session['A_StuID']
    sql = f'''
    insert into book_information(B_BookName, B_ISBN, B_Author, B_BookVersion, B_BookMajor, B_LessonName, B_BookPic, B_BookStatus, B_UsedStatus, B_UsedByTeacher, B_Extra_Info, B_Price, B_SalerID)
    values('{B_BookName}', '{B_ISBN}', '{B_Author}', '{B_BookVersion}', '{B_BookMajor}', '{B_LessonName}', '{B_BookPic}', {B_BookStatus}, '{B_UsedStatus}', '{B_UsedByTeacher}', '{B_Extra_Info}', {B_Price},'{B_SalerID}')
    '''
    print(sql)
    insert_or_update_data(sql)
    return "Book added successfully!"
#    return redirect(url_for('home'))


# [修改書籍資訊] 顯示網站
@app.route('/book_update/<B_BookID>')
def show_book_update(B_BookID):
    sql = "select * from book_information where B_BookID=" + B_BookID
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        datas = cursor.fetchall()
        book = datas[0]
    finally:
        conn.close()
    print(sql)
    return render_template("book_update.html", book = book)

# [修改書籍資訊] 接收表單提交的數據
@app.route('/do_book_update', methods=['POST']) #修改接值方式 將尾截掉.edit
def book_update():
    # 儲存圖片
    file = request.files['B_BookPic']
    if file.filename != '':
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        print('--picture update successfully:' + file.filename)

    print(request.form)
    B_BookID = request.form.get("B_BookID") #擺在下方接值.edit
    B_BookName = request.form.get("B_BookName")
    B_ISBN = request.form.get("B_ISBN")
    B_Author = request.form.get("B_Author")
    B_BookVersion = request.form.get("B_BookVersion")
    B_BookMajor = request.form.get("B_BookMajor")
    B_LessonName = request.form.get("B_LessonName")
    B_BookPic = file.filename
    B_BookStatus = request.form.get("B_BookStatus")
    B_UsedStatus = request.form.get("B_UsedStatus")
    B_UsedByTeacher = request.form.get("B_UsedByTeacher")
    B_Extra_Info = request.form.get("B_Extra_Info")
    B_Price = request.form.get("B_Price")
    sql = f'''
    update book_information set B_BookName='{B_BookName}', B_ISBN='{B_ISBN}', B_Author='{B_Author}', B_BookVersion='{B_BookVersion}', 
    B_BookMajor='{B_BookMajor}', B_LessonName='{B_LessonName}', B_BookPic='{B_BookPic}', B_BookStatus={B_BookStatus}, 
    B_UsedStatus='{B_UsedStatus}', B_UsedByTeacher='{B_UsedByTeacher}', B_Extra_Info='{B_Extra_Info}', B_Price={B_Price}
    where B_BookID={B_BookID}
    '''
    print(sql)
    insert_or_update_data(sql)
    return "Information updated successfully!"

# [書籍列表] 顯示網站
@app.route('/book_display')
def show_book_display():
    sql = "select B_BookID, B_BookName, B_BookPic, B_Price from book_information"
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        datas = cursor.fetchall()
    finally:
        conn.close()
    print(sql)
    return render_template("book_display.html", datas = datas)

# [依"標籤"尋找書籍] 接收搜尋的數據
@app.route('/do_book_search', methods=['GET'])
def book_search():
    search_str = request.args.get('search_str')
    return show_book_search(search_str)

# [依"標籤"尋找書籍] 顯示網站
@app.route('/book_search/<search_str>')
def show_book_search(search_str):
    # 搜索欄位: 書名、作者、科系、課程、老師
    sql = f'''select B_BookID, B_BookName, B_BookPic, B_Price from book_information where 
    (B_BookName like '%{search_str}%') or (B_Author like '%{search_str}%') 
    or (B_BookMajor like '%{search_str}%') or (B_LessonName like '%{search_str}%') 
    or (B_UsedByTeacher like '%{search_str}%')'''
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        datas = cursor.fetchall()
        print(datas)
    finally:
        conn.close()
    print(sql)
    return render_template("book_search.html", datas = datas, search_str = search_str)


# [查看書籍詳細資訊] 顯示網站
@app.route('/book_detail/<B_BookID>')
def show_book_detail(B_BookID):
    sql = "select * from book_information where B_BookID=" + B_BookID
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        datas = cursor.fetchall()
        if datas:  # check if datas is not empty
            book = datas[0]
            session['B_SalerID'] = book['B_SalerID']  # store B_SalerID in the session
        else:
            book = None  # or handle this case appropriately
    finally:
        conn.close()
    print(sql)
    return render_template("book_detail.html", book = book)


def send_email_Buyer(to_email, A_BuyerID, book_name, locker_id):
    content = MIMEMultipart()
    content["subject"] = "您在輔大二手書網站的交易已成功!"
    content["from"] = "wsx2244667@gmail.com"
    content["to"] = to_email
    content.attach(MIMEText(f"Please proceed to locker {locker_id} to get your book {book_name}"))

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("wsx2244667@gmail.com", "gpitruqqyaubmocl")
            smtp.send_message(content)
            print("Email sent!")
        except Exception as e:
            print("Error message: ", e)

def send_email_Saler(to_email, A_SalerID, book_name, locker_id):
    content = MIMEMultipart()
    content["subject"] = "您在輔大二手書網站的交易已成功!"
    content["from"] = "wsx2244667@gmail.com"
    content["to"] = to_email
    content.attach(MIMEText(f"Please proceed to locker {locker_id} to put your book {book_name}"))

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("wsx2244667@gmail.com", "gpitruqqyaubmocl")
            smtp.send_message(content)
            print("Email sent!")
        except Exception as e:
            print("Error message: ", e)

#點擊後購買後產生訂單
@app.route('/order', methods=['POST'])
def order_book():
    B_BookID = request.form['B_BookID']
    A_BuyerID = session.get('A_StuID')
    O_OrderTime = datetime.datetime.now()
    O_LockerID = 1
    O_OrderStatus = 1
    
    # get saler_id from book_information table
    conn = get_conn()
    
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select B_SalerID FROM book_information WHERE B_BookID = %s", (B_BookID,))
    result = cursor.fetchone()
    if result is None:
        return 'Book not found'+ B_BookID, 404
    B_SalerID = result['B_SalerID'] # Here, use 'B_SalerID' instead of B_SalerID
    
    # insert order into order_information table
    cursor.execute(
    "INSERT INTO order_information (O_OrderTime, O_LockerID, B_BookID, B_SalerID, A_BuyerID, O_OrderStatus) VALUES (%s, %s, %s, %s, %s, %s)",
    (O_OrderTime, O_LockerID, B_BookID, B_SalerID, A_BuyerID, O_OrderStatus)
)

    conn.commit()
    
    # Fetch the necessary data for the email
    cursor.execute("SELECT A_Email FROM account_manage WHERE A_StuID = %s", (A_BuyerID,))
    result = cursor.fetchone()
    if result is not None:
        A_Email_Buyer = result['A_Email']
    cursor.execute("SELECT A_Email FROM account_manage WHERE A_StuID = %s", (B_SalerID,))
    result = cursor.fetchone()
    if result is not None:
        A_Email_Saler = result['A_Email']
    cursor.execute("SELECT B_BookName FROM book_information WHERE B_BookID = %s", (B_BookID,))
    result = cursor.fetchone()
    if result is not None:
        B_BookName = result['B_BookName']
    cursor.close()
    
    send_email_Buyer(A_Email_Buyer,A_BuyerID,B_BookName,O_LockerID)
    send_email_Saler(A_Email_Saler,B_SalerID,B_BookName,O_LockerID)
    return 'Order Placed Successfully'

# 執行
if __name__ == '__main__': # 如果以主程式執行
    app.run(debug=True) 