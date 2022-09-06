import numpy as np
import pandas as pd
df = pd.DataFrame(
        [["kim", 89, 79, 78],
         ["lee", 46, np.NaN, 65],
         ["park", 79, 85, np.NaN],
         ["hong", np.NaN, 95, 98],
         ["kang", np.NaN, np.NaN, np.NaN]], columns=["name", "kor", "eng", "mat"]
    )
print( df.info() )
print( df.describe() )
print( df.count() )
print( df.count( axis=1 ) )
print( df.sum() )
print( df[["kor", "eng", "mat"]].sum( axis=1 ) )
print( df )

print( df.min() )
print( df.min( axis=1 ) )
print( df.max() )
print( df.max( axis=1 ) )

print( df.mean() )
print( df.mean( axis=1 ) )

df["tot"] = df[["kor", "eng", "mat"]].sum( axis=1 )
df["avg"] = df.loc[:, "kor":"mat"].mean( axis=1 )

print( df.median() )
print( df.median( axis=1 ) )

print( df.mad() )               # 편차
print( df.var() )               # 분산
print( df.var( axis=1 ) )
print( df.std() )               # 표준편차

print( df.cumsum() )
print( df.loc[:, "kor":"mat"].cumprod() )

print( df.loc[:, "kor":"mat"].idxmax() )
print( df.loc[:, "kor":"mat"].idxmin() )

print( df["kor"].corr( df["eng"] ) ) 
print( df["kor"].corr( df["avg"] ) )
print( df["mat"].corr( df["avg"] ) )
print( df["eng"].corr( df["avg"] ) )

print( df["kor"].cov( df["avg"] ) )
print( df["mat"].cov( df["avg"] ) )
print( df["eng"].cov( df["avg"] ) )

print( df.sort_index( ascending=False ) )
print( df.sort_index( axis=1 ) )
print( df.sort_values( by="kor" ) )
# print( df.sort_values( by="kor", axis=1 ) )        # 에러

print( df["kor"].unique() )
print( df["kor"].value_counts() )
print( df["kor"].isin( [46, 50, 60, 70] ) )
print( df.loc[ df["kor"].isin( [46, 56, 66, 76] ), "kor":"mat" ] )

print( df )

print()
df = pd.DataFrame( np.random.randn( 4, 3 ), columns=["A", "B", "C"], 
                   index=["kim", "lee", "hong", "park"] )
print( df )

def func( x ) :
    return x.max() - x.min()
print( df.apply( func ) ) 
print( df.apply( func, axis=1 ) )  
print( df.apply( lambda x : x.max()-x.min(), axis=1 ) ) 

### Pandas Plot ###
np.random.seed( 0 )
df = pd.DataFrame( np.random.rand( 100, 3 ), index=pd.date_range( "9/1/2022", periods=100),
                   columns=["A", "B", "C"] ).cumsum()
print( df.tail() )                   

import matplotlib.pyplot as plt

# df.plot()
# plt.xlabel( "Time" )
# plt.ylabel( "Value" )
# plt.title( "PLOT" )
# plt.show()

import seaborn as sns
iris = sns.load_dataset( "iris" )
titanic = sns.load_dataset( "titanic" )

# print( iris )
# iris["sepal_length"][:20].plot( kind="bar", rot=0 )
# plt.show()

# iris[:5].plot( kind="bar" )
# iris[:5].plot.bar( rot=0 )
# plt.show()

# iris[:5].plot( kind="barh" )
# plt.show()

# df = titanic.pclass.value_counts()
# # print( df )
# df.plot.pie( autopct="%.2f%%" )
# plt.show()

# iris.plot.hist()
# plt.show()

# iris.plot.kde()
# plt.show()

# iris.plot.box()
# plt.show()

iris.boxplot( by="species" )
plt.show()




















