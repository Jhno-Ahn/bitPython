# Map
# int m[] = { 10, 20, 30, 40, 50 }
# m = [10, 20, 30, 40, 50]

# Map<String, String> m = new HashMap<String, String>();
# m.put( "name", "김유신" )
# m.put( "name", "이순신" )

kim = { "name":"김유신", "age":30, "tel":"1111-2222"}
print( type( kim ) )
print( kim["name"] )
print( kim.get( "name" ) )

keys = kim.keys()
print( type( keys ) ) 
values = kim.values()
print( type( values ) )

if "id" not in kim.keys() :
    kim["id"] = "aaa"
kim["id"] = "bbb"
print( kim )  

for key, value in kim.items() :
    print( key, value )  

del kim["id"]
print( kim )

# print( kim[1] )
# print( kim["name":"age"] )

# a = input( "정수 : " )
# print( a )
# print( type( a ) )

# a = int( input( "정수 : " ) )
# b = int( input( "정수 : " ) )
# a = eval( input( "정수 : " ) )
# b = eval( input( "정수 : " ) )
# print( a + b )

# 조건문
# a = eval( input( "단 : " ) )
# if a >= 2 and a <= 9 :
#     # pass
#     for i in range( 1, 10 ) : # end value - 1
#         print( a, " * ", i, " = ", a*i )
# else :
#     print( "잘못입력" )

# age = eval( input( "나이 : " ) )
# if age <= 20 :
#     print( "어린이" )
# elif age <= 40 :
#     print( "청년" )
# elif age <= 60 :
#     print( "중년" )
# else :
#     print( "노년" )    

# 삼항연산 
# 조건 ? 참 : 거짓
a = 6
print( "짝수" if a%2==0 else "홀수" ) 

# 반복문
for i in range( 10 ) :
    print( i, end=" " )
print()
for i in range( 1, 11 ) :
    print( i, end=" " )
print()    
for i in range( 0, 10, 2 ) :
    print( i, end=" " )
print()
for i in range( 10, 0, -1 ) :
    print( i, end=" " )
print()    

# 나열형
m = [ 10, 20, 30, 40, 50]
print( type( m ) ) 
for a in m :
    print( a, end=" " )
print()    

m = ( 10, 20, 30, 40, 50 )
print( type( m ) )
for a in m :
    print( a, end=" " )
print()    

m = "ABCDEF"
print( type( m ) )
for a in m :
    print( a, end=" " )
print()    

m = set( [10, 20, 30, 40, 50, 50] )
print( type( m ) )
for a in m :
    print( a, end=" " )
print()  

m = {"kim":"김유신", "lee":"이순신", "hong":"홍길동"}
print( type( m ) )
for key, value in m.items() :
    print( key, value )
print()    

m = [(1, 2), (3, 4), (5, 6)]
print( type( m ) )
for a in m :
    print( a[0], a[1] )
print()
for a, b in m :
    print( a, b )
print()    

m = [ i for i in range( 1, 101 ) ]
m = [ i*2 for i in range( 1, 101) ]
m = [ "짝수" if i%2==0 else "홀수" for i in range( 1, 101) ]
print( m )


# 60점 이상이면 합격 아니면 불합격 출력
scores = { 'kim':89, 'lee':65, 'park':45, 'jung':96, 'choi':55,
          'cho':50, 'hong':44, 'hwang':60, 'ki':87, 'sung':35}
for key, value in scores.items() :
    if value >= 60 :
        print( key, "합격" )
    else :
        print( key, "불합격" )
        
i = 0
while( i<3 ) :
    print( i )
    i += 1
else :
    print( i )    
print()            

i = 0
while True :
    i += 1
    if i > 10 :
        break
    print( i, end=" " )
print()    
    
users = {"kim":"김유신", "lee":"이순신", "hong":"홍길동"}
for i, user in enumerate( users ) :
    # print( i, user, users[user] )
    print( i, user, users.get( user ) )    






















