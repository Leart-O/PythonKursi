my_set={1,2,3,3,5,7,4,5,9,4}
print(my_set)
set_my=set([2,4,5,6,7,6])
print(set_my)


A={1,2,3}
B={3,4,5}

#find the union
unioni=A.union(B) #unioni A | B
print(unioni)

#prerja/intersection
prerja=A.intersection(B) #prerja=A & B
print(prerja)

#differenca
differenca=A.difference(B) #differenca=A-B
print(differenca)

#diferenca simetrike
d_simetrike=A.symmetric_difference(B) #d_simetrike A^B
print(d_simetrike)

#add element
A.add(6)
print(A)

#remove element
A.remove(6)

#discard -remove an element without error if not exists
A.discard(100)

#removes all elements
A.clear()



#find the number of elements of a set
print(len(A))

listas=[2,2,3,3,4,4]
C=set(listas)
print(C)

E={"apple", "bannana", "Kiwi"}
F={"Mango", "Cherry", "Kiwi"}
int=E&F
print(int)

a=set([1,2,3,4,5])
numri=1
#operatori in dhe not in
print(numri in a)#true ose false nese numri i perket bashkesise
print(numri not in a)