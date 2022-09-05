import numpy as np
import pandas as pd
df = pd.DataFrame(
    [["kim", 89,71,78],
     ["lee",46,np.NaN,65],
     ["part",79,85,np.NaN],
     ["honh",np.NaN,95,98],
     ["kjan",np.NaN,np.NaN,np.NaN]], columns=["name","kor","eng","mat"]
    )

print(df.info())
print(df.describe())
print(df.count())
print(df.count(axis=1))
print(df[["kor","eng","mat"]].sum(axis=1))
print(df)
