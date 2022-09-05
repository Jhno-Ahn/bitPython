import cx_Oracle
import os
location = "C:\oraclexe\instantclient_21_6"
os.environ["PATH"] = location + ";" + os.environ["PATH"]

dsn = cx_Oracle.makedsn( "localhost", "1521", "xe" )
con = cx_Oracle.connect( "bit", "bit", dsn )
cursor = con.cursor()

# insert
# sql = "insert into dbtest values( :1, :2, :3, :4, sysdate )"
# user = ( "iii", "111", "홍길동", "1111-2222" )
# result = cursor.execute( sql, user )
# if result == 0 :
#     print( "가입실패" )
# else :
#     print( "가입성공" )    

# select
sql = "select * from dbtest"
cursor.execute( sql )
# for row in cursor :
#     # print( row )
#     for column in row :
#         print( column, end="\t" )
#     print()

rows = cursor.fetchall()
print( rows[0] )
print( rows[0][0] )
for row in rows :
    for column in row :
        print( column, end="\t" )
    print()

sql = "select count(*) from dbtest"
cursor.execute( sql )
count = cursor.fetchone()[0]        # ( 10 )
print( "회원수 :", count )
print()

sql = "select * from dbtest where id=:idx"
cursor.execute( sql, idx="aaa" )
user = cursor.fetchone()
print( user )

# delete
id = "iii"
passwd = "111"
sql = "select * from dbtest where id=:idx"
cursor.execute( sql, idx=id )
user = cursor.fetchone()
if user == None :
    print( "아이디가 없습니다" )
else :
    if passwd == user[1] :
        sql = "delete from dbtest where id=:idx"
        result = cursor.execute( sql, idx=id )
        if result == 0 :
            print( "탈퇴 실패" )
        else :
            print( "탈퇴 성공 :", id, "를 삭제했습니다" )        
    else :
        print( "비밀번호가 다릅니다" ) 


con.commit()
con.close()

















