import pandas as pd

data={"Name":["Alice", "Bob", "Tom"],
      "Age":[25,35,21],
      "City":["NY", "LA", "Paris"],
      }

df=pd.DataFrame(data)
print(df)
