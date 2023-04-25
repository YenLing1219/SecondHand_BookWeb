from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)

# 設定 MySQL 連線資訊
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'secondhand_bookweb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# 全域變數，儲存使用者的信箱和學號
current_user = {'email': None, 'student_id': None}

@app.route('/', methods=['GET', 'POST'])
def login():
    global current_user
    if request.method == 'POST':
        student_id = request.form['A_StuID']
        password = request.form['A_Password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM account_manage WHERE A_StuID = %s", (student_id,))
        user = cur.fetchone()
        cur.close()

        if user:
            if password == user['A_Password']:
                # 登入成功
                flash(f"登入成功，歡迎 {user['A_Account']}!", 'success')
                # 更新全域變數，儲存當前使用者的信箱和學號
                current_user['email'] = user['A_Account']
                current_user['student_id'] = user['A_StuID']
                return redirect(url_for('welcome'))
            else:
                # 密碼錯誤
                flash('密碼錯誤，請重新輸入', 'danger')
        else:
            # 學號不存在
            flash('學號不存在，請重新輸入', 'danger')

    return render_template('loginpage.html')

@app.route('/welcome')
def welcome():
    return f"歡迎 {current_user['email']}!"

if __name__ == '__main__':
    app.secret_key = '123456'
    app.run(debug=True)