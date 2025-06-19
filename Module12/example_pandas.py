import pandas as pd

produktet = ["Apples", "Bananas", "Oranges", "Grapes", "Pineapples"]
sales=[150,220,154,325,60]

sales_per_product=pd.Series(sales,index=produktet)
print(sales_per_product)

#sales - grapes
print(sales_per_product["Grapes"])

bestSeller = sales_per_product.idxmax()
print(bestSeller)