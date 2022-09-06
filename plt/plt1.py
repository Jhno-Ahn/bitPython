import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits
from mpl_toolkits.mplot3d.axes3d import Axes3D

# plt.plot( [1, 2, 3, 4] )
# plt.plot( [1, 2, 3, 4], [1, 4, 9, 16] )
# plt.plot( [1, 2, 3, 4], [1, 4, 9, 16], "ro-" )

# t = np.arange( 0, 5, 0.2 )
# plt.plot( t, t, "r--", t, t**2, "bs", t, t**3, "g^" )

# data_dict = {"data_x" : [1, 2, 3, 4, 5], "data_y" : [2, 4, 6, 8, 10] }
# plt.plot( "data_x", "data_y", data=data_dict, label="Price" )
#
# font1 = {
#     "family" : "serif",
#     "color" : "b",
#     "weight" : "bold",
#     "size" : 14
#     }
# font2 = {
#     "family" : "fantasy",
#     "color" : "deeppink",
#     "weight" : "normal",
#     "size" : "xx-large"
#     }
# plt.xlabel( "data_x", labelpad=15, fontdict=font1, loc="right" )
# plt.ylabel( "data_y", labelpad=20, fontdict=font2, loc="top" )
#
# plt.plot( [1, 2, 3, 4, 5], [-1, -2, -3, -4, -5], "r", label="Count" )
# # plt.legend( loc=(0.5, 0.5) )
# # plt.legend( loc="best" )
# # plt.legend( loc="upper right" )
# # plt.legend( ncol=1 )
# # plt.legend( ncol=2 )
# # plt.legend( fontsize=14, frameon=False )
# plt.legend( shadow=True )
#
# # plt.xlim( [0, 10] )
# # plt.ylim( [-10, 20] )
# # plt.axis( [0, 10, -10, 20] )
# # plt.axis( "auto" )
# # plt.axis( "equal" )
# # plt.axis( "square" )
# # plt.axis( "scaled" )
# plt.axis( "tight" )


# plt.plot( [1, 2, 3], [4, 4, 4], linestyle="solid", label="solid" )
# plt.plot( [1, 2, 3], [3, 3, 3], linestyle="dashed", label="dashed" )
# plt.plot( [1, 2, 3], [2, 2, 2], linestyle="dotted", label="dotted" )
# plt.plot( [1, 2, 3], [1, 1, 1], linestyle="dashdot", label="dashdot" )

# plt.plot( [1, 2, 3], [4, 4, 4], "-", label="solid" )
# plt.plot( [1, 2, 3], [3, 3, 3], "--", label="dashed" )
# plt.plot( [1, 2, 3], [2, 2, 2], ":", label="dotted" )
# plt.plot( [1, 2, 3], [1, 1, 1], "-.", label="dashdot" )

# plt.plot( [1, 2, 3], [4, 4, 4], linestyle=(0,(1,1)), label="(0, (1,1))" )
# plt.plot( [1, 2, 3], [3, 3, 3], linestyle=(0,(1,5)), label="(0, (1,5))" )
# plt.plot( [1, 2, 3], [2, 2, 2], linestyle=(0,(5,1)), label="(0, (5,1))" )
# plt.plot( [1, 2, 3], [1, 1, 1], linestyle=(0,(3, 5, 1, 5)), label="(0, (3, 5, 1, 5))" )

# plt.plot( [1, 2, 3], [4, 4, 4], "-", linewidth=10, solid_capstyle="butt" )
# plt.plot( [1, 2, 3], [3, 3, 3], "-", linewidth=10, solid_capstyle="round" )
# plt.plot( [1, 2, 3], [2, 2, 2], "--", linewidth=10, dash_capstyle="butt" )
# plt.plot( [1, 2, 3], [1, 1, 1],  "--", linewidth=10, dash_capstyle="round" )

# plt.plot( [1, 2, 3], [4, 4, 4], "-", marker="o" )
# plt.plot( [1, 2, 3], [3, 3, 3], "-", marker="^" )
# plt.plot( [1, 2, 3], [2, 2, 2], "--", marker="v" )
# plt.plot( [1, 2, 3], [1, 1, 1],  "--", marker="<" )

# plt.plot( [1, 2, 3], [4, 4, 4], "bo-" )
# plt.plot( [1, 2, 3], [3, 3, 3], "g^-" )
# plt.plot( [1, 2, 3], [2, 2, 2], "rv--" )
# plt.plot( [1, 2, 3], [1, 1, 1], "y<--" )

# plt.plot( [1, 2, 3], [4, 4, 4], marker="H", color="limegreen" )
# plt.plot( [1, 2, 3], [3, 3, 3], marker="d", color="violet" )
# plt.plot( [1, 2, 3], [2, 2, 2], marker="x", color="dodgerblue" )
# # plt.plot( [1, 2, 3], [1, 1, 1], marker=11 )
# plt.plot( [1, 2, 3], [1, 1, 1], marker="$Z$", color="#ff0000" )


# x = [1, 2, 3, 4, 5]
# y = [2, 4, 7, 9, 11]
# plt.plot( x, y )
# # plt.fill_between( x[1:4], y[1:4], alpha=0.5 )
# # plt.fill_betweenx( y[1:4], x[1:4], alpha=0.5 )
# z = [4, 5, 8, 11, 14]
# plt.plot( x, z )
# # plt.fill_between( x[1:4], y[1:4], z[1:4], alpha=0.5, color="lightgray" )
# plt.fill( [1.9, 1.9, 3.1, 3.1], [1.0, 4.0, 6.0, 3.0], color="magenta", alpha=0.5 )

# x = np.linspace( -10, 10, 100 )
# y = x**3
# plt.plot( x, y )
# plt.xscale( "symlog" )
# plt.yscale( "log" )
#
# plt.grid( True, axis="y", color="red", alpha=0.5, linestyle="--" )


# x = np.arange( 0, 2, 0.2 )
# plt.plot( x, x, "bo" )
# plt.plot( x, x**2, "r*" )
#
# # plt.xticks( [0, 1, 2, 3] )
# # plt.yticks( np.arange(0, 5) )
#
# plt.xticks( np.arange( 0, 2, 0.5 ), labels=["Jan", "Feb", "Mar", "Apr"] )
# plt.yticks( np.arange( 0, 5 ), ("0GB", "1GB", "2GB", "3GB", "4GB") )
# plt.tick_params( axis="x", direction="inout", length=10, pad=6, labelsize=12, labelcolor="green",
#                  top=True )
# plt.tick_params( axis="y", direction="in", length=10, pad=10, labelsize=12, labelcolor="green",
#                  right=True )
#
# plt.axhline( 2, 0.1, 0.9, color="red", linestyle="--", linewidth=2 )
# plt.vlines( 0.5, 1, 3, color="red", linestyle=":", linewidth=2 )

# plt.legend()

## 막대 그래프 ##
x = np.arange( 3 )
y = [100, 300, 700]
years = ["2020", "2021", "2022"]

# # plt.bar( x, y )
# # plt.xticks( np.arange( 3 ), years )
# # plt.bar( x, y, color="y" )
# colors = ["y", "b", "g"]
# # plt.bar( x, y, color=colors, width=0.8 )
# plt.bar( x, y, align="edge", edgecolor="r", linewidth=5, tick_label=years )

# plt.barh( x, y )
# plt.yticks( np.arange( 3 ), years )
# plt.barh( x, y, align="edge", edgecolor="#eee", linewidth=5, tick_label=years )

## 산점도 ##
np.random.seed( 0 )
n = 100
x = np.random.rand( n )
y = np.random.rand( n )
# plt.scatter( x, y, alpha=0.5 )
# area = ( 30 * np.random.rand( n ) ) ** 2
# plt.scatter( x, y, s=area, alpha=0.5 )

# plt.plot( [1], [1], 'o', markersize=20, c="r" )
# plt.scatter( [2], [1], s=400, c="b" )
# plt.text( 1.0, 1.01, "Plot", fontdict={"size":14} )
# plt.text( 2.0, 1.01, "Scatter", fontdict={"size":14} )
# plt.axis( [0.5, 2.5, 0, 2] )

# colors = np.random.rand( n )
# plt.scatter( x, y, c=colors, alpha=0.5 )
# plt.colorbar()


# from mpl_toolkits.mplot3d import Axes3D
# n = 100
# xmin, xmax, ymin, ymax, zmin, zmax = 0, 20, 0, 20, 0, 50
# cmin, cmax = 0, 2
# x = np.array( [ (xmax-xmin) * np.random.random_sample() + xmin for _ in range( n ) ] )
# y = np.array( [ (ymax-ymin) * np.random.random_sample() + ymin for _ in range( n ) ] )
# z = np.array( [ (zmax-zmin) * np.random.random_sample() + zmin for _ in range( n ) ] )
# color = np.array( [ (cmax-cmin) * np.random.random_sample() + cmin for _ in range( n ) ] )
# fig = plt.figure( figsize=(6, 6) )
# ax = fig.add_subplot( 111, projection="3d" )
# # ax.scatter( x, y, z, c=color, marker="o", s=15 )
# # ax.plot( x, y, z )
# ax.bar( x, y, z )


## 히스토그램 ##
weights = np.array( [ (150-40) * np.random.random_sample() + 40 for _ in range( n ) ] )
# plt.hist( weights )
# plt.hist( weights, bins=20 )
# plt.hist( weights, bins=20, cumulative=True )

weights1 = np.array( [ (150-40) * np.random.random_sample() + 40 for _ in range( n*10 ) ] )
# plt.hist( (weights, weights1), label=("weights", "weights1") )
# plt.hist( (weights, weights1), label=("weights", "weights1"), histtype="bar" )
# plt.hist( (weights, weights1), label=("weights", "weights1"), histtype="barstacked" )
# plt.hist( (weights, weights1), label=("weights", "weights1"), histtype="step" )
# plt.hist( (weights, weights1), label=("weights", "weights1"), histtype="stepfilled", alpha=0.5 )

plt.hist( (weights, weights1), label=("weights", "weights1"), histtype="step", density=True )

plt.legend()

plt.tight_layout()
plt.show()


















