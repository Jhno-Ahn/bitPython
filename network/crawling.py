# crawling.py

# 스레드 Thread
# import time
# def doing() :
#     time.sleep( 1 )
#     print( "실행중" )
#
# start = time.time()
# for i in range( 10 ) :
#     doing()
# end = time.time()
# print( "실행시간 :", (end-start) )        

import time
import threading
# def doing() :
#     time.sleep( 1 )
#     print( "스레드 실행중" )
# if __name__ == "__main__" :
#     start = time.time()
#     threads = []
#     for i in range( 10 ) :
#         t = threading.Thread( target=doing )
#         t.start()       # 실행대기 상태
#         threads.append( t )
#     for thread in threads :
#         thread.join()
#     end = time.time()
#     print( "실행시간 :", (end-start) )

from concurrent import futures              # start() join()을 자동으로 처리
# def doing() :
#     time.sleep( 1 )
#     return "스레드 실행중"
# if __name__ == "__main__" :
#     start = time.time()
#     results = []
#     with futures.ThreadPoolExecutor() as excutor :
#         for i in range( 10 ) :
#             result = excutor.submit( doing )
#             results.append( result )
#     for f in futures.as_completed( results ) :
#         print( f.result() )
#     end = time.time()
#     print( "실행시간 :", (end-start) )

# def calc_sum( list ) :
#     sum = 0
#     for i in range( list[0], list[1]+1 ) :
#         sum += i
#     return sum
# if __name__ == "__main__" :
#     start = time.perf_counter()
#     result = calc_sum( [1, 100000000] )
#     print( result )
#     end = time.perf_counter()
#     print( "실행시간 :", (end-start) )

# def calc_sum( list ) :
#     sum = 0
#     for i in range( list[0], list[1]+1 ) :
#         sum += i
#     return sum
# if __name__ == "__main__" :
#     start = time.time()
#     with futures.ThreadPoolExecutor() as excutor :
#         sub = [ [1, 100000000//2], [100000000//2 +1, 100000000] ]
#         results = excutor.map( calc_sum, sub )
#     print( sum( results ) )
#     end = time.time()
#     print( "실행시간 :", (end-start) )
        
# 멀티 프로세스
from multiprocessing import Pool, Semaphore
# def calc_sum( list ) :
#     sum = 0
#     for i in range( list[0], list[1]+1 ) :
#         sum += i
#     print( sum )
# if __name__ == "__main__" :
#     start = time.time()
#     sub = [ [1, 100000000//2], [100000000//2 +1, 100000000] ]
#     pool = Pool( processes=2 )
#     pool.map( calc_sum, sub )
#     pool.close()
#     pool.join()
#     end = time.time()
#     print( "실행시간 :", (end-start) )
    
# 스레드 동기화
# number = 0
# lock = threading.Lock()
# def thread1( num ) :    
#     global number
#     lock.acquire()              # 다른 스레드 접근 금지
#     for i in range( num) :
#         number += 1
#     lock.release()
# def thread2( num ) :
#     global number
#     lock.acquire()
#     for i in range( num ) :
#         number += 1
#     lock.release()
# if __name__ == "__main__" :
#     threads = []
#     start = time.time()
#     t1 = threading.Thread( target=thread1, args=(50000000,) )
#     t1.start()
#     threads.append( t1 )
#     t2 = threading.Thread( target=thread2, args=(50000000,) )
#     t2.start()
#     threads.append( t2 )
#     for thread in threads :
#         thread.join()
#     print( number )
#     end = time.time()
#     print( "실행시간 :", (end-start) )
        
# 멀티 프로세스 동기화
from multiprocessing import shared_memory, Semaphore, Process
import numpy as np
# def calc_sum( id, number, shm, arr, sem ) :
#     # id 스레드번호, number 최대값, shm 공유메모리, arr numpy.array, sem 세마포어
#     sum = 0
#     for i in range( number ) :
#         sum += 1
#     sem.acquire()       # 세마포어 획득
#     new_shm = shared_memory.SharedMemory( name=shm )
#     tmp_arr = np.ndarray( arr.shape, dtype=arr.dtype, buffer=new_shm.buf )
#     tmp_arr[0] += sum
#     sem.release()       # 세마포어 해제
# if __name__ == "__main__" :
#     start = time.time()
#     arr = np.array( [0] )
#     shm = shared_memory.SharedMemory( create=True, size=arr.nbytes )
#     np_shm = np.ndarray( arr.shape, dtype=arr.dtype, buffer=shm.buf )
#     sem = Semaphore()
#     p1 = Process( target=calc_sum, args=(1, 50000000, shm.name, np_shm, sem ) )
#     p2 = Process( target=calc_sum, args=(2, 50000000, shm.name, np_shm, sem ) )
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time.time()
#     print( np_shm[0] )
#     print( "실행시간 :", (end-start) )
#     shm.close()
#     shm.unlink()
    
# 네트워크
import urllib.request as req
from urllib.error import URLError 
# f = req.urlopen( "http://www.daum.net" )
# print( f.read( 100 ).decode( "utf-8" ) )    

# re = req.Request( "http://www.daum.net1" )
# try :
#     req.urlopen( re )
# except URLError as e :
#     print( e.reason )

response = req.urlopen( "http://www.daum.net" )
# print( response )
print( "url : ", response.geturl() )
headers = response.info()
print( "date : ", headers["date"] )
print( headers )
data = response.read()
print( len( data ) )

    
# 크롤링
import urllib.request
# url = "https://img1.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/202208/19/sportskhan/20220819133522707nahy.jpg"
# savename = "blackpink.jpg"
# urllib.request.urlretrieve( url, savename )
# print( "저장했습니다" ) 
#
# url = "http://www.google.com/robots.txt"
# txt = urllib.request.urlopen( url )
# data = txt.read().decode( "utf-8" )
# # print( data )
# with open( "robots.txt", "w", encoding="utf-8" ) as f :
#     f.write( data )
# print( "저장했습니다" )            





# BeautifulSoup 
from bs4 import BeautifulSoup as bs
html = """
    <html>
        <head>
            <meta charset="utf-8">
            <title>HTML Test</title>
        </head>
        <body>
            <h2> HTML 연습 </h2>
            <p id="first">짜장면</p>
            <p class="strong">짬뽕</p>
            <p class="point strong">탕수육</p>
            <p id="second">울면</p>            
        </body>
    </html>
"""
soup = bs( html, "html.parser" )
print( "<<" + soup.find( "h2" ).string + ">>")
print( "<<" + soup.html.body.h2.string + ">>")

h2 = soup.find( "h2" )
body = h2.parent
# print( body )
html = body.parent
# print( html )
p1 = h2.next_sibling.next_sibling
print( p1.string )
nodes = body.children
# for node in nodes :
#     print( node.string )

ps = soup.find_all( "p" )
for p in ps :
    print( p.string )

h2 = body.findChild()
print( h2.string )
print()

p1 = soup.find( id="first" )
print( p1.string )
p4 = soup.find( id="second" )
print( p4.string )

pp = soup.find_all( class_="strong" )
for p in pp :
    print( p.string )

# select()
# select_one()
html = """
    <html>
        <head>
            <meta charset="utf-8">
            <title> HTML 연습 </title>
        </head>
        <body>
            <h2 class="title"> 웹 스크랩핑 </h2>
            <p id="name"> HTML </p>
            <p class="subject"><a> XML </a></p>
            <p class="subject"><b><a> JSON </a></b></p>
            <a> CDATA </a>
        </body>
    </html>
"""
soup = bs( html, "html.parser" )
h2 = soup.select_one( "body h2" )
print( "<<" + h2.string + ">>" )

ps = soup.select( ".subject" )
for p in ps :
    print( p.string )

pp = soup.select( "body p" )
for p in pp :
    print( p.string )

ps = soup.select( "p a" )       # 자손선택자
for p in ps :
    print( p.string )

pp = soup.select( "p > a" )      # 자식선택자
for p in pp :
    print( p.string ) 

p = soup.select_one( "p#name" )
print( p.string )

p = soup.select_one( "p.subject" )
print( p.string )


# RSS 
import urllib.request as req
import urllib.parse as pa
# url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stdId=109"
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    "stnId" : 109
    }
params = pa.urlencode( values )
url = url + "?" + params
# print( url )
data = req.urlopen( url ).read().decode( "utf-8" )
# print( data )

with open( "whether.txt", "w", encoding="utf-8" ) as f :
    f.write( data )
    
soup = bs( data, "html.parser" )
title = soup.find( "title" )
print( "<<" + title.string + ">>" )

cities = soup.find_all( "city" )
# for city in cities :
#     print( city.string )

datas = soup.find_all( "data" )
for data in datas :
    print( data.parent.city.string, end="\t" )    
    print( data.tmef.string, "\t", data.wf.string, 
           "\t", data.tmn.string, "\t", data.tmx.string ) 
print()






















