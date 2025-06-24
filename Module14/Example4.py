import pandas as pd
import matplotlib.pyplot as plt


#getting data from file
df=pd.read_csv("avgIQpercountry.csv")

nobelPrizes=df.groupby("Continent")["Nobel Prices"].sum()
noOfContinents=nobelPrizes.count()

color=["gold","lightcoral","yellow","thistle","red","orange","aquamarine","burlywood"]
plt.figure(figsize=(10,10))

nobelPrizes.plot(kind="pie", colors=color, autopct="%1.1f%%")

plt.title("Distribution of Nobel Prizes by Continent")
plt.axis("equal")
plt.ylabel("")
plt.tight_layout()
plt.show()