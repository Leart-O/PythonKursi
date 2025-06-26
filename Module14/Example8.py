import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

from Module14.Example4 import color

my_dataset=pd.read_csv("avgIQpercountry.csv")
my_dataset["Population - 2023"]=my_dataset["Population - 2023"].str.replace(",","").astype(float)

fig=px.choropleth(my_dataset,locations="Country",locationmode="country names",
                    color="Continent",projection="natural earth",
                   hover_data=["Literacy Rate","Nobel Prices"],color_continuous_scale="agsunset",
                   title="Average IQ by Country")
fig.show()