import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

my_dataset = pd.read_csv("weather_tokyo_data.csv")

my_dataset["temperature"] = my_dataset["temperature"].replace(
    to_replace=r"[^\d.-]+", value="", regex=True
)
my_dataset["temperature"] = my_dataset["temperature"].astype(float)

my_dataset["date"] = pd.to_datetime(my_dataset["year"].astype(str) + "-" + my_dataset["day"])

my_dataset["month"] = my_dataset["date"].dt.to_period("M")

avg_temp = my_dataset["temperature"].mean()
print("Average Temperature:", round(avg_temp, 2), "°C")

max_temp_day = my_dataset.loc[my_dataset["temperature"].idxmax()]
min_temp_day = my_dataset.loc[my_dataset["temperature"].idxmin()]

print("Hottest Day:", max_temp_day["date"].date(), "-", max_temp_day["temperature"], "°C")
print("Coldest Day:", min_temp_day["date"].date(), "-", min_temp_day["temperature"], "°C")

monthly_avg = my_dataset.groupby("month")["temperature"].mean().reset_index()
monthly_avg["month"] = monthly_avg["month"].astype(str)

print("\nMonthly Average Temperatures:")
for _, row in monthly_avg.iterrows():
    print(f"{row['month']}: {round(row['temperature'], 2)} °C")

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_avg, x="month", y="temperature", marker="o", color="blue")
plt.title("Average Monthly Temperature in Tokyo")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

fig = px.line(monthly_avg, x="month", y="temperature",
              title="Average Monthly Temperature in Tokyo",
              markers=True,
              labels={"month": "Month", "temperature": "Temperature (°C)"})
fig.update_layout(xaxis_tickangle=-45)
fig.show()