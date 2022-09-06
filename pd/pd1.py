import numpy as np
# where
x = np.array( [1, 2, 3, 4, 5] )
y = np.array( [6, 7, 8, 9, 10] )
z = np.array( [True, False, False, True, False] )

print( [ a if c else b for a, b, c in zip( x, y, z)] )
print( np.where( z, x, y ) )

a = np.random.randn( 4, 4 )
# print( a )
print( np.where( a > 0, 1, 0 ) )
print( np.where( a < 0, 0, a ) )

# 파일 입출력
a = np.arange( 10 )
np.save( "np1.npy", a )
arr = np.load( "np1.npy" )
print( arr )

b = np.arange( 10, 20 )
np.savez( "np2.npz", arr1=a, arr2=b )
c = np.load( "np2.npz" )
print( c["arr1"] )
print( c["arr2"] )

### Pandas ###
import pandas as pd
# Series        1차원
s = pd.Series( [1, 0, 8, -3, -6, 9, 3, -2, 6, -7] )
print( type( s ) )
# print( s )
print( s.index )
print( s.values )
print( type( s.values ) )
print( s.dtype )

s.index = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print( s )
print( s.index )

print( s["a"] )
print( s.a )
print( s[0] )
print( s[0:5] )
print( s["a":"e"] )

d = { "A":65, "B":66, "C":67, "D":68 }
print( type( d ) ) 
print( d["A"] )
# print( d.A )
# print( d[0:3] )
# print( d["A":"C"] )
for key, value in d.items() :
    print( key, value )

s = pd.Series( d )
print( s.index )
print( s.values )
print( s[0:3] )
print( s["A":"C"] )

# DataFrame
d = {
    "name" : ["kim", "park", "hong", "lee"],
    "age" : [20, 30, 40, 25],
    "tel" : ["1111-2222", "2222-1111", "2222-3333", "3333-1111"]
}
df = pd.DataFrame( d )
print( df )
print( df.index )
print( df.columns )
print( df.values )

df.index.name = "Num"
df.columns.name = "User"
print( df )
print( df.index )
print( df.columns )

n = np.array(
    [["kim", 20, "1111-2222"],
     ["lee", 30, "2222-1111"],
     ["hong", 40, "3333-2222"]]    
)
df = pd.DataFrame( n )
print( df )
print( df.index )
print( df.columns )

df.index = ["a", "b", "c"]
df.columns = ["name", "age", "tel"]
print( df )

df1 = pd.DataFrame( n, index=["a", "b", "c"], columns=["name", "age", "tel"] )
print( df1 )

print( df.info )
print( df.describe() )
result = df.describe()
print( result.index )
print( result.columns )

print()
print( df )
print( df["name"] )
print( df["name"]["a"] )
print( df["name"].a )
print( df["name"][:2] )
print( df["name"]["b":"c"] )

print()
print( df )
print( df[["name", "age"]] )
print( df.name, df.age )
print( df[:][:] )
print( df[:2] )
print( df[:2][:2] )
# print( df[:2, :2] )               에러
print( df.values[:2, :2] )          # Numpy

df["address"] = ["서울", "수원", "인천"]
df["adult"] = df["age"] >= "30"
df["age"][0] = 40
df["adult"][0] = True
del( df["adult"] )

df.index = ["A", "B", "C"]
index = ["I", "II", "III"]
df.reindex( index )
df.reset_index()

print( df )

# 정렬
print()
s = pd.Series( range( 4 ), index=["b", "d", "c", "a"] )
s = s.sort_index( ascending=False )
s = s.sort_values( ascending=False )
print( s )

df = pd.DataFrame( np.arange( 12 ).reshape( 3, 4 ), 
                   index=["b", "c", "a"], columns=["B", "A", "D", "C"] )
df = df.sort_index()
print( df )
df = df.sort_index( axis=1 )
print( df )

df = df.sort_values( by="A", ascending=False )
print( df )
df = df.sort_values( axis=1, by="a" )
print( df )
df = df.sort_values( axis=1, by=["a", "b"] )
print( df )

# loc iloc
print()
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print( m )
print( m[1][2] )
print( m[0:2][0:2] )
# print( m[0:2, 0:2] )            에러

n = np.array( m )
print( n )
print( n[1][2] )
print( n[0:2][0:2] )
print( n[0:2, 0:2] )

w = pd.DataFrame( m, index=["a", "b", "c"], columns=["A", "B", "C"] )
print( w )
# print( w[1][2] )        # 에러
print( w["A"][2] )        # [컬럼][인덱스]
print( w[0:2][0:2] )
# print( w[0:2, 0:2] )    # 에러
    
print()
df = pd.DataFrame( np.arange( 10, 26 ).reshape( 4, 4 ), columns=["A", "B", "C", "D"] )
print( df )
# print( df[0][0] )        # 에러
print( df["A"][0] )        # [컬럼][인덱스]
# print( df[["A":"C"]] )   # 에러
print( df[["A", "D"]] )
print( df[["A", "D"]][0:2] )    # [컬럼][인덱스]
# print( df[["A", 0:2]] )  # 에러
 
print()
# print( df[1, 1] )        # 에러
# print( df.loc[1, 1] )    # 에러
print( df.iloc[1, 2] )     # 행 열
# print( df.iloc[1, "A"] ) # 에러
# print( df.iloc["A", 1] ) # 에러   

print( df.iloc[:2, :2] ) 
print( df.iloc[:2, :-1])
print( df.iloc[:-1, :-1] )

# loc
print()
print( df )
print( df[0:2][0:2] )
print( df[["A","C"]] )
print( df.iloc[1, 1] )
print( df.iloc[2:, 2:] )
# print( df.iloc["A", 1] )        # 에러

print( df.loc[1][1] )
# print( df.loc[1, 1] )           # 에러
# print( df.loc["A", 1] )         # 에러
# print( df.loc["A"][1] )         # 에러
print( df.loc[1]["A"] )           # [인텍스][컬럼]  
print( df["A"][1] )               # [컬럼][인덱스]
print( df.iloc[2][1] )            # [인덱스][컬럼]
# print( df[1]["A"] )             # 에러

print()
print( df.loc[:2, :"B"] )
print( df.loc["A":"C"] )
print( df.loc[:, "A":"C"] )
# print( df.loc[:2]["A":"C"] )    # 에러
print( df.loc[:2][["A","B"]] )

print()
df["E"] = [30, 31, 32, 33]
df.loc[:, "F"] = [40, 41, 42, 44]
df.loc[0, "A"] = 99
df.loc[3, ["A", "C", "E"]] = [50, 51, 52]

# df[:][4] = [60, 61, 62, 63, 64, 65]    # 에러
df.loc[4] = [60, 61, 62, 63, 64, 65]

del( df["F"] )
# df.drop( "E", axis=0 )            # 에러
df = df.drop( "E", axis=1 )
# df.drop( 1, axis=1 )              # 에러
df = df.drop( 1, axis=0 )

print( df )

print( df.loc[::-1, ::-1] )
print( sorted( [4, 6, 8, 2, 4] )[::-1] )

df = pd.DataFrame(
    [["kim", 20, "1111-2222"],
     ["lee", 30, "2222-1111"],
     ["park", 40, "1111-3333"],
     ["hong", 35, "2222-3333"]], columns=["name", "age", "tel"]
    )

# boolean indexing
print()
print( df )
print( df.iloc[:, 0:2] )
print( df.loc[:, "name":"age"] )
# print( df.loc[:, 0:2] )                # 에러
# print( df.iloc[:, "name":"age"] )      # 에러
  
print( )
print( df.loc[ df["age"] >= 30, ["name", "age"] ] )  
print( df.loc[ df["name"] == "kim", ["name", "tel"] ] )
print( df.loc[ df["tel"] == "1111-2222", "name":"tel"] )
print( df.loc[ (df["age"] >=30) & (df["age"] <=40), ["name", "age"] ] )

# 결측값
print()
df["address"] = ""
df.loc[ df["address"] == "", ["address"] ] = "서울"

df.loc[ ::2, ["address"]] = None
# df.loc[ df["address"] == None, ["address"] ] = "수원"
df.loc[ df["address"].isnull(), ["address"] ] = "수원"

df.loc[:, "income"] = [np.NaN, 5000, np.NaN, 6000]
df.loc[5, :] = [np.NaN, np.NaN, np.NaN, np.NaN, np.NaN]
# df = df.dropna( how="any" )
# df = df.dropna( how="all" )
df.dropna( how="all", inplace=True )

# df["income"].fillna( value=0, inplace=True )
# df["income"].fillna( value = np.mean( df["income"] ), inplace=True )

print( df.isnull()["income"] )
print( df.drop( df[ df.isnull()["income"] ].index , axis=0 ) )
print( df.drop( ["income"], axis=1 ) )
print( df.drop( ["tel", "income"], axis=1 ) )


# 전치
print( df )
# print( df.T )
print( df.transpose() )























