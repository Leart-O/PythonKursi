import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from unicodedata import numeric

my_dataset=pd.read_csv("avgIQpercountry.csv")

my_dataset["Population - 2023"]=my_dataset["Population - 2023"].str.replace(",","").astype(float)

numeric_iq_data_loc=my_dataset.select_dtypes(include=['number'])

sns.heatmap(numeric_iq_data_loc.corr(),annot=True,cmap="coolwarm",fmt=".2f")
plt.tight_layout()
plt.show()