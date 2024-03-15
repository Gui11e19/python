#set se pueden crear ([]) o { }
#solo admiten elementos unicos
#no estan ordenados ni se pueden ordenar
#son inmutables mno se pueden incluir listas y diccionarios


#set([1,2,3,4,5,6])

# otra manera de declarar
#s1 = {1,2,3}


# se puede incluir tuples s = set([1,2,3,4,5,(1,2,3)])

#s = set([1,2,3,4,5,6])
#print(len(s))

#print(2 in s) 

#union de sets
s1 = {1,2,3}
#s2 = {4,5,6}
#s3 = s1.union(s2) #unir

#agregar
s1.add(4)

#eliminar
s1.remove(4)
print(s1)

#no crashe sino haya el parametro
s1.discard()

#elimina uno de los elementos aleatoriamente y llenarlo en una variable
s1.pop()

#vacia el set
s1.clear()