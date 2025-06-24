import pandas as pd
from pandas.compat.numpy.function import SORT_DEFAULTS

df = pd.read_csv("avgIQpercountry.csv")
print(df.info()) #we see the columns of this dataset
print(df.head()) #we see the first 5 rows

countryData = df["Country"]
print(countryData)

subset=df[["Country", "Average IQ"]]
filtered_DF=subset[subset["Average IQ"]>100]
print(filtered_DF)

#null_mask finding null rows
null_mask = df.isnull()
null_count = null_mask.sum()
print(null_count)

#removing duplicates
df.drop_duplicates(keep="first",inplace=True)
df["Population - 2023"]=df["Population - 2023"].apply(lambda x: float(x.replace(",","")))

#find the avg of a continent
avg_iq_per_continent=df.groupby('Continent')["Average IQ"].mean()

avg_iq_per_continent=avg_iq_per_continent.sort_values(ascending=False)
print(avg_iq_per_continent)

#calculate nobel prizes by country. And show countries only with more than 1 nobel
# you have to use Group By, Sum and sort values

nobel_per_country=df.groupby('Country')["Nobel Prices"].sum()
sorted_nobel_per_country=nobel_per_country.sort_values(ascending=False)
sorted_nobel_per_country=sorted_nobel_per_country[sorted_nobel_per_country!=0]
print(sorted_nobel_per_country)

