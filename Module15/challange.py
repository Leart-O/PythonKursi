import seaborn as sns
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt


my_dataset = pd.read_csv("weather_tokyo_data.csv")
print(my_dataset.info())
my_dataset["temperature"] = my_dataset["temperature"].replace(
    to_replace=r"[^\d.-]+", value="", regex=True
)

my_dataset["temperature"] = my_dataset["temperature"].astype(float)

avg_temp = my_dataset["temperature"].mean()
print("Average Temperature:", avg_temp)

import seaborn as sns
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt


my_dataset = pd.read_csv("weather_tokyo_data.csv")
print(my_dataset.info())
my_dataset["temperature"] = my_dataset["temperature"].replace(
    to_replace=r"[^\d.-]+", value="", regex=True
)

my_dataset["temperature"] = my_dataset["temperature"].astype(float)

avg_temp = my_dataset["temperature"].mean()
print("Average Temperature:", avg_temp)

import seaborn as sns
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt


my_dataset = pd.read_csv("weather_tokyo_data.csv")
print(my_dataset.info())
my_dataset["temperature"] = my_dataset["temperature"].replace(
    to_replace=r"[^\d.-]+", value="", regex=True
)

my_dataset["temperature"] = my_dataset["temperature"].astype(float)

avg_temp = my_dataset["temperature"].mean()
print("Average Temperature:", avg_temp)

my_dataset = pd.DataFrame([x.split('/') for x in "day"])



