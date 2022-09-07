import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset( "iris" )
titanic = sns.load_dataset( "titanic" )
tips = sns.load_dataset( "tips" )
flights = sns.load_dataset( "flights" )

# print( iris.head() )
# x = iris.petal_length.values
# sns.rugplot( x )
# sns.rugplot( data=iris, x="petal_length" )
# sns.kdeplot( data=iris, x="petal_length" )

# x = iris["petal_length"].values
# sns.distplot( x, kde=True, rug=True )

# sns.countplot( data=titanic, x="class")
# sns.countplot( data=tips, x="day")
# plt.hist( tips["day"] )

# sns.jointplot( iris["petal_length"], iris["petal_width"], alpha=0.5 )
# plt.suptitle( "Jointplot" )
# sns.jointplot( data=iris, x="petal_length", y="petal_width", kind="scatter" )
# sns.jointplot( data=iris, x="petal_length", y="petal_width", kind="kde" )

# sns.pairplot( iris )
# sns.pairplot( iris, hue="species", markers=["o", "s", "D"] )

# print( titanic.head() )
# titanic_size = titanic.pivot_table( index="class", columns="sex", aggfunc="size" )
# # print( titanic_size )
# sns.heatmap( titanic_size, cmap=sns.light_palette( "gray", as_cmap=True ), 
#              annot=True, fmt="d" )

# sns.barplot( data=tips, x="day", y="total_bill", hue="sex" )

# sns.boxplot( data=tips, x="day", y="total_bill", hue="sex" )

# sns.violinplot( data=tips, x="day", y="total_bill", hue="sex", split=True )

# sns.stripplot( data=tips, x="day", y="total_bill", jitter=True, alpha=0.5, hue="sex", dodge=True )

# sns.swarmplot( data=tips, x="day", y="total_bill", size=3, hue="sex", dodge=True )
#
# data = titanic[ titanic.survived.notnull() ]
# sns.catplot( data=data, x="age", y="sex", hue="survived", kind="swarm", split=True, height=2, aspect=4 )

# sns.boxplot( data=tips, x="tip", y="day", whis=np.inf )
# sns.stripplot( data=tips, x="tip", y="day", color="0.4", alpha=0.5 )
# sns.violinplot( data=tips, x="tip", y="day", inner=None, alpha=0.5 )
# sns.swarmplot( data=tips, x="tip", y="day", color="0.9", alpha=0.5 )

sns.set_style( "ticks" )
sns.set_style( "darkgrid" )
sns.set_style( "whitegrid" )
def sinplot( flip=1 ) :
    x = np.linspace( 0, 14, 100 )
    for i in range( 1, 7 ) :
        plt.plot( x, np.sin( x+i*0.5) * (7-i) * flip )
sinplot()        


plt.show()





















