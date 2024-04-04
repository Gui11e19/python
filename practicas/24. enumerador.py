#enumerador

lista = ['a','b','c']

"""
indice = 0
    for item in lista:
        print(indice,item)
        indice += 1"""

"""for indice,item in enumerate(range(50,55)):
        print(indice,item)

tuples = list(enumerate(lista))
print(tuples[1][0])"""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
numero = list(enumerate(lista_nombres))

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


lista_indices = list(enumerate("Python")) 

for item in lista_indices:
        print(item)