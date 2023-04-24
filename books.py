from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


#最初的模板
@app.route('/')
def hello_world():
    return 'Hello World! 上架: http://localhost:5000/book_create'


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

# [上架] 顯示上架書籍的網站
@app.route('/book_create')
def show_register():
    return render_template("book_create.html")

# [上架] 接收表單提交的數據
@app.route('/do_book_create', methods=['POST'])
def do_register():
    print(request.form)
    B_BookID = request.form.get("B_BookID") #有用A_I的話可以刪掉
    B_BookName = request.form.get("B_BookName")
    B_ISBN = request.form.get("B_ISBN")
    B_Author = request.form.get("B_Author")
    B_BookVersion = request.form.get("B_BookVersion")
    B_BookMajor = request.form.get("B_BookMajor")
    B_LessonName = request.form.get("B_LessonName")
    B_BookPic = request.form.get("B_BookPic") # 上傳圖片的功能還沒出來
    B_BookStatus = request.form.get("B_BookStatus")
    B_UsedStatus = request.form.get("B_UsedStatus")
    B_UsedByTeacher = request.form.get("B_UsedByTeacher")
    B_Extra_Info = request.form.get("B_Extra_Info")
    B_Price = request.form.get("B_Price")
    sql = f'''
    insert into book_information(B_BookID, B_BookName, B_ISBN, B_Author, B_BookVersion, B_BookMajor, B_LessonName, B_BookPic, B_BookStatus, B_UsedStatus, B_UsedByTeacher, B_Extra_Info, B_Price)
    values({B_BookID},  '{B_BookName}', '{B_ISBN}', '{B_Author}', '{B_BookVersion}', '{B_BookMajor}', '{B_LessonName}', '{B_BookPic}', {B_BookStatus}, '{B_UsedStatus}', '{B_UsedByTeacher}', '{B_Extra_Info}', {B_Price})
    '''
    print(sql)
    insert_or_update_data(sql)
    return "Book added successfully!"

# 執行
if __name__ == '__main__': # 如果以主程式執行
    app.run() 