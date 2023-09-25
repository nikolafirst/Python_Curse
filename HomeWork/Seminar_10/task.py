import random
import pandas as pd

lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})
data.head()

df = pd.DataFrame({"column": ["robot", "human"]})
unique_values = df["column"].unique()
one_hot_df = pd.DataFrame(0, index=df.index, columns=unique_values)
for value in unique_values:
    one_hot_df.loc[df["column"] == value, value] = 1
print(one_hot_df)


