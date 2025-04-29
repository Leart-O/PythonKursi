name_of_list=["item1","item2","item3","item4","item5"]
shopping_list=["banane",3.5,3]

name_of_list.append("item6") #shton element te ri ne fund te listes
#name_of_list.clear() # fshin te gjithe element e listes
#name_of_list.count() #outputs the numer of elements
lista2=name_of_list.copy() #copy from one list to the other
lista3=lista2
lista2[0]="alma"

print("lista 3",lista3)
print("lista 2", lista2)

lista2.insert(1,"item10") # add the element to the specific place
print("lista 2", lista2)
lista2.pop(1) # this remove the element from the specific place
lista2.remove("item4") #remove element based on value
lista2.reverse() # revereses the elements
print(lista2[-1])
