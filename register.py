from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysql_connector import MySQL
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import pymysql


app = Flask(__name__)
app.secret_key = '123456' #flask做login功能用途的key，可以隨便定義
mysql = MySQL(app) #mysql引入的參數



#最初的模板
@app.route('/')
def hello_world():
    return 'Hello World! 註冊: http://localhost:5000/show_register'


# 連接mysql
def get_conn():
    return pymysql.connect(
        host = '127.0.0.1', 
        user = 'root', 
        password = '12345678', 
        database = 'secondhand_bookweb', # 資料庫名稱(我改回這個名稱了，我用日期標記之後自己感覺不太好= =)  
        # database = 'bookweb_0411',  
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

# 顯示表單提交的網站
@app.route('/show_register') # route:路由，字串是網址路徑
def show_register():
    return render_template("show_register.html") # 模板渲染

# 接收表單提交的數據
@app.route('/do_register', methods=['POST'])
def do_register():
    print(request.form)
#做了檢驗學號是否重複的小功能，但我不確定先print form之後不管它跳回register那邊會不會出事
#我電腦不知道為什麼跑不出來檔案，幫測...Orz
    A_StuID = request.form.get("A_StuID")

    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM your_table_name WHERE A_StuID=%s", (A_StuID,))
    result = cursor.fetchone()
    
    if result[0] > 0:
        flash('學號已存在，請重新輸入。', 'error')
        return redirect(url_for('show_register.html'))
    
    A_Account = request.form.get("A_Account")
    A_Password = request.form.get("A_Password")
    A_RealNameVerify = request.form.get("A_RealNameVerify")
    A_BirthDate = request.form.get("A_BirthDate")
    A_Major = request.form.get("A_Major")
    sql = f'''
    insert into account_manage(A_StuID, A_Account, A_Password, A_RealNameVerify, A_BirthDate, A_Major)
    values('{A_StuID}',  '{A_Account}', '{A_Password}', {A_RealNameVerify}, '{A_BirthDate}', '{A_Major}')
    '''
    print(sql)
    insert_or_update_data(sql)
    return "Account added successfully!"




# 執行
if __name__ == '__main__': # 如果以主程式執行
    app.run() 