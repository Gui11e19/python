#loop for 

"""nombres = ['Juan','Ana','Carlos','Belen','Fran']
x = input("ingrese una letra: ").upper()
print(x)
for nombre in nombres:
    numero = nombres.index(nombre) + 1
    print(f"El {numero}! nombre es {nombre}")
    if nombre.startswith(x):
        print(f"El nombre {nombre} empieza con {x}")"""

""""numeros = [1,2,3,4,5,6,7,8]
x = 0

for numero in numeros:
    x = x + 1

print(f"El total es: {x}")"""

#se puede hacer un for a una palabra

for letra in 'palabra':
    print(f"La palabra deletreada es: {letra}")

# iterar una lista anidada
    
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

#iterar en un diccionario

dic = {'c1':'a','c2':'b','c3':'c'}

#si quiero los elementos dentro de dic for item in dic.items():
#si quiero los valores dentro de dic for item in dic.values(): o
# for a,b in dic.items():

for item in dic:
    print(item) 


#Ejercicios practicos

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
    
print(f"La suma es {suma_numeros}")

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0 
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
    
print(f"La suma de los impares es {suma_impares}\n La suma de los pares es {suma_pares}")
