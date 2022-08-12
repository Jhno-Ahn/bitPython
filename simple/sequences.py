# sequences.py
# 열거형 나열형

# 문자열
name = "홍길동"
age = 20
print( "name : " + name + " age : " + str(age) )
print( "=" * 10 )
print( "name : %s age : %d" %(name, age) )
print( "name : {0} age : {1}".format( name, age ) )
print( "name : {name} age : {age}".format( name="홍길동", age= 30 ) )

a = "Hello"
print( "{0:10}".format( a ) )
print( "{0:<10}".format( a ) )
print( "{0:>10}".format( a ) )
print( "{0:^10}".format( a ) )
print( "{0:=^10}".format( a ) )
print( "{0:-^10}".format( a ) )
print( "{0:x^10}".format( a ) )

# 문자열 관련 함수
a = "Hello Python"
print( a.lower() )
print( a.upper() )
print( a.title() )
print( a.swapcase() )
print( a.islower() )
print( a.isupper() )
print( a.count( "o" ) )
print( a.find( "a" ) )
# print( a.index( "a" ) )
print( ",".join( a ) )
b = "    b    b   b    "
print( b.lstrip( " " ) )
print( b.rstrip( " " ) )
print( b.strip() )
print( a.replace( "o", "a" ) )
print( a.split() )
print( a.split( "o" ) )

c = " ABC123"
print( c.isalnum() )    # 알파벳 + 숫자
print( c.isalpha() )    # 알파벳
print( c.isidentifier() )
print( c.isdigit() )    # 숫자

print()
print( "0abc".isidentifier() )
print( " abc".isidentifier() )
print( "_abc".isidentifier() )
print( "a+bc".isidentifier() )
print( "a$b".isidentifier() )
print( "가나다".isidentifier() )

# 인덱싱
#   0   1   2   3   4   5   6   7   8   9  10  11  12
# | H | e | l | l | o |   | P | y | t | h | o | n | \0 |        # 배열 리스트
print( a[0] )
print( a[11] )

# 슬라이싱
print( a[:] )
print( a[3:] )
print( a[:10] )     # end index -1
print( a[2:10] )
print( a[:-1] )
print( a[:-2] )


# 리스트
print()
fruits = ["banana", "apple", "orange", "pear", "grape"]
print( "banana" in fruits )
print( "melon" in fruits )

print( fruits[3] )
fruits[3] = "melon"
print( fruits )

print( fruits[:] )
print( fruits[2:] )
print( fruits[:3] )     # end index -1
print( fruits[:-2] )
print( fruits[4][1] )

print( len( fruits ) )
print( max( fruits ) )
print( min( fruits ) )
print( fruits )
fruits.append( "pear" )
print( fruits )
fruits.insert( 2, "watermelon" )
print( fruits )
# fruits.extend( "apple" )
# print( fruits )
print( fruits.count( "apple" ) )
print( fruits.index( "apple" ) )
print( fruits.pop() )
fruits.remove( "apple" )
print( fruits )
fruits.sort( reverse=True )
print( fruits )

shop = ["라면", "햇반", "김치"]
shoplist = [fruits, shop]
print( shoplist )

print( shoplist[1][1] )
print( shoplist[1][1][1] )
print( shoplist[1][:2] )
shoplist[1].append( "달걀" )
print( shoplist )

print( shoplist[:2][:2] )
print( shoplist[0][: len( shoplist[0] )] )


# 튜플
print()
a, b = ( 10, 20 )
print( a, b )

zoo = ( "dog", "cat", "monkey", "snake" )
a, b, c, d = zoo
print( a )

print( zoo[0] )
print( zoo[0:2] )
print( len( zoo ) )

# list <-> tuple
z = list( zoo )
z.sort()
z.append( "tiger" )
print( z )
print( type( z ) )

t = tuple( z )
print( max( t ) )
print( t.index( "tiger" ) )
print( t )
print( type( t ) )

def calc( a, b ) :
    return ( a+b, a-b, a*b, a/b )
values = calc( 5, 2 )
print( values[0] )


# Set
country = set( ["korea", "japan", "china", "russia", "taiwan"] )
print( type( country ) )
country.add( "korea" )
print( country )
nation = country.copy()
nation.add( "USA" )
nation.add( "UK" )
print( nation )
print( nation - country )
print( nation | country )
print( nation & country )
print()
print( nation.difference( country ) )
print( nation.union( country ) )
print( nation.intersection( country ) )

nation.remove( "UK" )
print( nation )
nation.pop()
print( nation )

print( nation.symmetric_difference( country ) )     # 교집합이 아닌 값 

print( "korea" in nation )
print( "korea" not in nation )











