from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


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
#        database = 'secondhand_bookweb', 
        database = 'bookweb_0411',  # 資料庫名稱
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
    A_StuID = request.form.get("A_StuID")
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