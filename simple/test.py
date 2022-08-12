# a = 10
# print( a )

# import keyword
# print( keyword.kwlist )
# print( len( keyword.kwlist ) )

print( type( 10 ) )
print( type( 10.5 ) )
print( type( "ABC") )
print( type( 'ABC' ) )
print( type( 10 + 10j ) )
print( type( 1234567890123456789 ) )
print( type( 5/2 ) )            # 2.5

# a=10, b=20
a, b = 10, 20

# 교환
c = 0
c = a
a = b 
b = c
print( a, b )
a, b = b, a
print( a, b )
del a, b
# print( a, b )

print( "우리나라 \
대한민국" )

a = """
    우리나라
    대한민국
"""
print( a )

# 강제 형변환
print( type( int( 10.5 ) ) )
print( type( float( 10 ) ) )
# print( type( int( "ABC" ) ) )
print( type( int( "123" ) ) )
print( type( str( 123 ) ) )

# 진수변환
print( int( "1111", 2 ) )
print( int( "ff", 16 ) ) 

print( oct( 20 ) )
print( hex( 20 ) )
print( bin( 20 ) )

print( "ABC", "DEF" )
print( "ABC" + "DEF" )
print( "ABC" + str( 10 ) )
print( "{0}{1}".format( "ABC", "DEF" ) )
print( "{1}{0}".format( "ABC", "DEF" ) )
print( "{0:10s}{1:10s}".format( "ABC", "DEF" ) )
print( "{0:.2f}".format( 1234.5678 ) )

# 연산자 
a = 10
print( a ** 2 )
print( 5 / 2 )
print( 5.0 / 2 )
print( 5 // 2 )
print( 5.0 // 2 )

print( 0 and 0 )
print( 0 and 1 )
print( 1 and 0 )
print( 1 and 1 )

print( False or False )
print( False or True )
print( True or False )
print( True or True )

print()
print( "H" in "Hello" )
print( "H" not in "Hello" )

a = "Hello"
b = "Hello"
print( a is b )     # 주소
print( a == b )     # 내용
a += "Python!"
b += "Python!"
print( a is b )
print( a == b )

# 산술 대입연산자
a = 10
a += 10; print( a )
a -= 10; print( a )
a *= 10; print( a )
a /= 10; print( a )
a %= 10; print( a )

# 쉬프트 대입연산자
a = 20 
a <<= 2; print( a )
a >>= 2; print( a )

# 비트 논리 대입연산자
a = 10
a &= 10; print( a )
a |= 10; print( a )
a ^= 10; print( a )

















