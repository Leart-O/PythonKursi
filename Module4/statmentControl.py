#break keyword
from Module4.WhileLoop import count

numrat=[1,2,3,4,5,6]
target=3
for num in numrat:
    print(num)
    if num==target:
        print("Target found")
        break
# continue
scores=[68,42,57,78,35,62,50,92]
total=0
count=0
for score in scores:
    if score<50:
        continue
    total=total+score
    count+=1
mes=total/count #mesatarja per vlerat mbi 50
print("Mesatarja= ",mes)