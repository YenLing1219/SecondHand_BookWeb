import pymysql
mysql_conn = pymysql.connect(
    host= '127.0.0.1', 
    port= 3306, 
    user= 'root', 
    password= '', 
    db= 'SecondHand_BookWeb'
    )

## 新增
# sql = "INSERT INTO account_manage (A_Account, A_Password, A_StuID, A_RealNameVerify, A_BirthDate, A_Major) VALUES ('{0}','{1}', '{2}', '{3}','{4}', '{5}')" .format('ABC123@gmail.com','123456','410402408','1','','10')
# try:
#     with mysql_conn.cursor() as cursor:
#         cursor.execute(sql)
#     mysql_conn.commit()
# except Exception as e:
#     mysql_conn.rollback()

## 新增資料裡包含特殊字元，可以用escape解決 
# A_Account = "ABC''123@gmail.com"
# A_Account = mysql_conn.escape(A_Account)
# sql = "INSERT INTO account_manage (A_Account, A_Password, A_StuID, A_RealNameVerify, A_BirthDate, A_Major) VALUES ('{0}','{1}', '{2}', '{3}','{4}', '{5}')" .format(A_Account,'123456','410402408','1','','10')
# try:
#     with mysql_conn.cursor() as cursor:
#         cursor.execute(sql)
#     mysql_conn.commit()
# except Exception as e:
#     mysql_conn.rollback()

## 刪除 account_manage 裡面 A_StuID 為 410402408 的資料
# sql = "DELETE FROM account_manage WHERE A_StuID = '{0}'".format('410402408')
# try:
#     with mysql_conn.cursor() as cursor:
#         cursor.execute(sql)
#     mysql_conn.commit()
# except Exception as e:
#         print(e)
#         mysql_conn.rollback()

## 更新 account_manage 裡面 的 A_Account 欄位 用 A_Major 為 10 當條件，
## 符合條件的欄位 A_Account 更新為 rqrqr@gmail.com 
# sql = "UPDATE account_manage SET A_Account  = '{0}' WHERE A_Major = '{1}'".format('rqrqr@gmail.com', '10')
# try:
#     with mysql_conn.cursor() as cursor:
#         cursor.execute(sql)
#     mysql_conn.commit()
# except Exception as e:
#     print(e)
#     mysql_conn.rollback()
    
# 查找 account_manage 資料表裡面的 全部資料 用 A_StuID 當條件 要是符合 A_StuID=410402408 
# 就 print 出來 這裡使用一個叫fetchone()的函數來做結果的篩選，只篩一個。     
# sql = "SELECT * FROM account_manage WHERE A_StuID = '{0}'".format(410402408)
# try:
#     with mysql_conn.cursor() as cursor:
#         cursor.execute(sql)
#         select_result = cursor.fetchone()
#         print(select_result)
# except Exception as e:
#     print(e)

## 查找 account_manage 資料表裡面的 全部資料 用 A_StuID 當條件 要是符合 A_StuID=410402408 
# 就 print 出來，跟上面不同的是會把全部符合的資料都print出，是為 fetchall() 
# 下面還用了迴圈去遍歷，可以看出fetchall是把所有資料整合成array。  
# sql = "SELECT * FROM account_manage WHERE A_StuID = '{0}'".format(410402408)
# try:
#     with mysql_conn.cursor() as cursor:
#         cursor.execute(sql)
#         select_result = cursor.fetchall()
#         for result_one in select_result:
#             print(result_one) 
# except Exception as e:
#     print(e)