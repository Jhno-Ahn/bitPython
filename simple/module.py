# 추상화    abstract
from abc import abstractmethod, ABCMeta
class Animal( metaclass=ABCMeta ) :     # 추상클래스    
    def __init__(self, name="", age=0) :
        self.name = name
        self.age = age
    @abstractmethod
    def disp(self) :       # 추상메서드     구현할 필요가 없다.
        pass               # 호출되지 않기때문에 구현할 필요가 없다.
class Dog (Animal) :
    # def __init__(self, name, age ) :
    #     Animal.__init__( self, name, age )
    def disp(self) :       # 추상메서드는 반드시 구현해야 한다.     
        print( self.name, self.age )
class Cat(Animal) :
    def disp(self) :
        print( self.name, self.age )   
    
# animal = Animal()        # 추상클래스는 객체를 생성할 수 없다.
dog = Dog( "멍멍이", 5 ) 
dog.disp()
cat = Cat( "나비", 10 )
cat.disp()

# 예외처리
# C        경고    에러    예외(정의해야 한다)
# Java     에러    에러    예외(정의되어 있다)
# Python   에러    에러    에러

# syntax error        문법이 틀린경우
# semantic error      예외. 실행 중 문제가 생기는 경우

import traceback
try :
    # a = 4 / 0
    # a = 4 / "2"
    a = 4 / 2
except ZeroDivisionError :
    print( "0으로 나누면 안됩니다" )   
except TypeError :
    print( "정수로만 나누세요" ) 
except Exception :
    traceback.print_exc()
else :
    print( "값 : ", a )    
finally :
    print( "프로그램 끝" )
    
# 사용자 정의 예외    

# class NumberException( Exception ) :
#     pass
# class InputException( Exception ) :
#     pass
#
# try :
#     a = input( "단 : " )
#     # print( a )
#     if not a.isdigit() :
#         raise NumberException()
#     if int(a) < 2 or int(a) > 9 :
#         raise InputException()
# except NumberException :
#     print( "숫자만 입력하세요" )
# except InputException :
#     print( "2~9사이만 입력하세요" )
# else :
#     for i in range( 1, 10 ) :
#         print( a, "*", i, "=", int(a)*i )
# finally :
#     print( "프로그램 끝" )                    
     

# 모듈         파일 
# 패키지        폴더
# Java        부품의 단위 - 클래스
# Python      부품의 단위 - 모듈

import simple.module.mymodule
simple.module.mymodule.hello() 
simple.module.mymodule.bye()
user = simple.module.mymodule.User( "홍길동", 30 )
print( user.getName() )
print( user.getAge() )

import simple.module.mymodule as my
my.hello()
my.bye()
user = my.User( "이순신", 20 )
print( user.getName() )
print( user.getAge() )

from simple.module import mymodule
mymodule.hello()
mymodule.bye()
user = mymodule.User( "김유신", 30 )
print( user.getName() )
print( user.getAge() )

from simple.module.mymodule import hello, bye, User
hello()
bye()
user = User( "강감찬", 40 )
print( user.getName() )
print( user.getAge() )

from simple.module.mymodule import User as U
user = U( "대조영", 35 )
print( user.getName() )
print( user.getAge() )

# 자주 사용하는 모듈
import os
# print( os.__doc__ )
# print( help( os ) )
# print( help( os.mkdir ) )
# python -m pydoc -p 3333

path = "c:/"
for file in os.listdir( path ) :
    if os.path.isdir( path + file ) :
        print( "폴더 :", file )
    else :
        print( "화일 :", file )
    print( os.path.split( path + file ) )
    print( os.path.join( path + file ) )
print( os.path.abspath( "." ) )
if not os.path.exists( "test" ) :
    os.mkdir( "test" )
if os.path.exists( "test" ) :
    os.rmdir( "test" )    

import sys
print( sys.exc_info() )
# sys.exit( 0 )
print( sys.modules )
print( sys.path )
print( sys.version )
print( sys.version_info )

import logging, platform
print( platform.platform() )
if platform.platform().startswith( "Window" ) :
    # 윈도우인 경우
    logfile = os.path.join( os.getenv( "HOMEDRIVE" ), os.getenv( "HOMEPATH"), "test.log" )
else :
    # 윈도우가 아닌 경우
    logfile = os.path.join( os.getenv( "HOME" ), "test.log" )
print( logfile )        
logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s : %(levelname)s : %(message)s",
        filename=logfile,
        filemode="w"
    )
logging.debug( "디버그" )
logging.info( "정보" )
logging.warning( "경고" )
logging.error( "에러" )
logging.critical( "크리티컬" )

from datetime import date, time, datetime, timedelta
now = date.today()
print( now )
print( now.year, "년", now.month, "월", now.day, "일" )

now = datetime.today()
print( now )
print( now.year, "년", now.month, "월", now.day, "일",
       now.hour, ":", now.minute, ":", now.second, " ", now.microsecond )

import time
print( time.time() )
print( time.gmtime( time.time() ) )
t = time.gmtime( time.time() )
print( t.tm_hour + 9, "시" )

# print( now + 30 )
print( now + timedelta( 30 ) )

print( now.strftime( "%y년 %m월 %d일 %H : %M : %S" ) )     # 날짜 문자열로
s = "2022-8-18 13:05:30"
print( datetime.strptime( s, "%Y-%m-%d %H:%M:%S" ) )
t = datetime.strptime( s, "%Y-%m-%d %H:%M:%S" )
print( type( t ) )

import random
# random.seed( 0 )
# for i in range( 6 ) :
#     print( int( random.random() * 45 ) + 1 )       # 1 ~ 45
lotto = random.sample( range(1, 46), 6 )
# print( lotto.sort() ) 
print( sorted( lotto ) )   
random.shuffle( lotto )
print( lotto )
for i in range( 6 ) :
    # print( random.randint( 1, 45 ) )
    print( random.uniform( 1, 45 ) )

# 파일 입출력
f = open( "a.txt", "a", encoding="utf-8" )
for i in range( 1, 11 ) :
    f.write( str( i ) + " " )
f.write( "\r\n" )
print( "파일 생성 완료" )
f.close()

# f = open( "a.txt", "r", encoding="utf-8" )
# while True :
#     data = f.read()
#     if data == "" :
#         break
#     print( data, end=" " )    
# f.close()

# f = open( "a.txt", "r", encoding="utf-8" )
# while True :
#     line = f.readline()
#     if line == "" :
#         break
#     print( line )
# f.close()

# f = open( "a.txt", "r", encoding="utf-8" )
# for line in f :
#     print( line )
# f.close()

# with open( "a.txt", "r", encoding="utf-8" ) as f :
#     lines = f.readlines()
#     for line in lines :
#         print( line )

# CSV
with open( "lotto.csv", "w" ) as f :
    for i in range( 10 ) :
        m = random.sample( range( 1, 46 ), 6 )
        m.sort()
        for i, a in enumerate( m ) :
            f.write( str(a) )
            if( i < len(m) -1 ) :
                f.write( "," )
        f.write( "\n" )

with open( "lotto.csv", "r" ) as f :
    for line in f :
        for a in line.split( "," ) :
            print( a, end="\t" )
        print()         

# pickling     객체 단위 입출력
class User :
    def __init__(self, name, age, tel ) :
        self.name = name
        self.age = age
        self.tel = tel
    def getName(self) :
        return self.name
    def getAge(self) :
        return self.age
    def getTel(self) :
        return self.tel
    
import pickle    
hong = User( "홍길동", 20, "1111-2222" )
with open( "user.txt", "wb" ) as f :
    pickle.dump( hong, f )
with open( "user.txt", "rb" ) as f :
    user = pickle.load( f )
    print( user.getName(), user.getAge(), user.getTel() )    

users = [
        User( "김유신", 20, "1111-2222" ),
        User( "이순신", 30, "2222-1111" ),
        User( "홍길동", 25, "1111-3333" )        
    ]
with open( "users.txt", "wb" ) as f :
    pickle.dump( users, f )
with open( "users.txt", "rb" ) as f :
    us = pickle.load( f )
    print( type( us ) )
    for u in us :
        print( u.getName(), u.getAge(), u.getTel() )
        
print()        
# 정규표현식    Regular Expression
import re
p = re.compile( "[a-z]+" )
print( p.match( "" ) )
print( p.match( " " ) )
print( p.match( "a " ) )
print( p.match( "python!!" ) )
print( p.match( "Python!!" ) )
print( p.match( "pyThon!!" ) )
print( p.match( " python!!" ) )

print( p.search( "" ) )
print( p.search( " " ) )
print( p.search( "a " ) )
print( p.search( "python!!" ) )
print( p.search( "Python!!" ) )
print( p.search( "pyThon!!" ) )
print( p.search( " python!!" ) )
word = p.search( " python!!" )
print( word.start() )
print( word.end() )
print( word.span() )
print( word.group() )

s = "Life is too Short"
print( p.match( s ) )     
print( p.search( s ) )
print( p.findall( s ) )   
print( p.finditer( s ) )
for word in p.finditer( s ) :
    print( word.group() )

p = re.compile( "a.b" )
print( p.search( "ab" ) )
print( p.search( "ac" ) )
print( p.search( "acb" ) )
print( p.search( "a0b" ) )
print( p.search( "a&b" ) )
print( p.search( "a\tb" ) )
print( p.search( "a\nb" ) )
print( p.search( "accb" ) )

s = """
    abc acb accb a
    cb a\nb a0b a\tb
"""
print( p.findall( s ) )
p = re.compile( "a.b", re.DOTALL )          # re.S    \n 도 가능
print( p.findall( s ) )

p = re.compile( "[A-Z]+")
print( p.findall( s ) )
p = re.compile( "[A-Z]+", re.IGNORECASE )   # re.I    대소문자 상관없이
print( p.findall( s ) )

s = """python one
pythontwo
python
study python
python 1
life is too short"""
p = re.compile( "^python\s\w+" )
print( p.findall( s ) )
p = re.compile( "^python\s\w+", re.MULTILINE )  # re.M
print( p.findall( s ) )













