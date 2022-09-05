import numpy as np
a = [[1, 2, 3, 4], [5, 6, 7, 8]]
print( a )

a = np.arange( 15 ).reshape( 3, 5 )
print( a )
print( a.shape )
print( a.ndim )
print( a.dtype )
print( a.itemsize )
print( a.size )

t = ( 10, 20, 30, 40, 50 )
print( type( t ) )
tt = np.array( t )
print( type( tt ) )

s = {10, 20, 30, 40, 50}
print( type( s ) )
ss = np.array( s )
print( type( ss ) )

m = [10, 20, 30, 40, 50]
# print( m.shape )
mm = np.array( m )
print( mm.shape )

w = [ -5, 9, 8, 7, 5, -6, -7, 3, -5, 2]
print( np.shape( w ) )
print( np.abs( w ) )
print( np.square( w ) )
print( np.sqrt( np.abs( w ) ) )

# print( help( np.shape ) )
print( np.isnan( w ) )
print( np.sum( w ) )
print( np.mean( w ) )
print( np.max( w ) )
print( np.min( w ) )
print( np.argmax( w ) )
print( np.cumsum( w ) )
# w = sorted( w )
# print( w )
# w.sort()
# print( w )

print( np.sort( w ) )
print( np.sort( w )[::-1] )

w = [[1, 3, 5], [2, 4, 6]]
print( w )
w = np.array( w )
print( w )
w = [1, 2, 3, 4, 5, 6]
w = np.array( w ).reshape( 2, 3 )
# w = np.array( w ).reshape( 3, 3 )            error
w = w.reshape( 3, 2 )
print( w )

print( np.sum( w ) )
print( np.sum( w, axis=0 ) )
print( np.sum( w, axis=1 ) )
print( np.mean( w ) )
print( np.mean( w, axis=0 ) )
print( np.mean( w, axis=1 ) )
print( np.median( w ) )
print( np.median( w, axis=0 ) )

print( np.var( w ) )            # 분산        거리 ** 2 값의 평균
print( np.std( w ) )            # 표준편차     분산의 제곱근
print( np.std( w, axis=0 ) )   

m = [10, 20, 30, 40, 50]
# print( m + 2 )                # error
m = np.array( m )
print( m + 2 )                  # element wise

w = [1, 2, 3, 4, 5]
print( m + w )

print( np.sin( m ) * 10 )
print( m > 20 )

a = np.array( [[1, 1], [1, 1]] )
b = np.array( [[1, 2], [3, 4]] )
print( np.add( a, b ) )
print( a + b )
print( np.subtract( a, b ) )
print( a - b )
print( np.multiply( a, b ) )
print( a * b )
print( np.divide( a, b ) )
print( a // b )

print( a @ b )
print( a.dot( b ) )

print( np.zeros( 10 ) )
print( np.zeros( (3, 3) ) )
print( np.ones( (3, 3,) ) )

x = np.random.randn( 10 )
print( x )
y = np.random.randn( 10 )
print( np.maximum( x, y ) )
print( np.minimum( x, y ) )

# 인덱싱 / 슬라이싱
s = "ABCDEFG"
print( s[1] )
print( s[1:4] )

a = [ i for i in range( 10, 20 ) ]      # list
print( a[0] )
print( a[0:5] )
print( a[0:-1] )
print( a[:6] )
print( a[6:] )

b = np.arange( 10, 20 )                 # ndarray
print( b[0] )
print( b[0:5] )
print( b[:-1] )
print( b[:6] )
print( b[6:] )

a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
# print( a )
print( a[2][2] )
print( a[:][:] )
print( a[:] )
print( a[2][:] )
print( a[0:2][0:2] )
print( a[0:2][1] )
# print( a[0:2, 0:2] )            에러

b = np.arange( 1, 16 ).reshape( 3, 5 )
print( b )
print( b[2][2] )
print( b[:][:] )
print( b[:] )
print( b[2][:] )
print( b[0:2][0:2] )
print( b[0:2][1] )

print( b[0:2, 0:2] )
print( b[:-1, :-1] )
print( b[1:2, :] )
print( b[2, 2] )

a = list( np.empty( ( 8, 4 ) ) )
for i in range( 8 ) :
    for j in range( 4 ) :
        a[i][j] = i
print( type( a ) )
print( a )
# print( a[[5, 7, 2]] )                에러

b = np.arange( 32 ).reshape( 8, 4 )
print( type( b ) )
print( b )
print( b[[5, 7, 2]] )
print( b[[5, 7, 2], [1, 2, 3]])

print( b )
print( b.T )

a = np.floor( np.random.rand( 2, 2 ) * 10 )
print( a )
b = np.floor( np.random.rand( 2, 2 ) * 10 )
print( b )
print( np.hstack( ( a, b ) ) )
print( np.vstack( ( a, b ) ) ) 

c = np.floor( np.random.rand( 2, 12 ) * 10 )
print( c )
print( np.hsplit( c, 3 ) )
print( np.hsplit( c, ( 3, 5 ) ) )       # 0~2 3~4 5~11

d = np.floor( np.random.rand( 12, 2 ) * 10 )
print( d )
print( np.vsplit( d, 3 ) )
print( np.vsplit( d, ( 3, 5 ) ) )
















