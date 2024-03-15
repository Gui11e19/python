#while

""" while condicion:
        codigo
    else 
        codigo

Cuidado con las condiciones de paro

Palabras clave break continue pass

monedas = 5

while monedas:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:print("Ya no te quedan monedas F")


respuesta = 's'

while respuesta == 's':
    respuesta = input("quieres seguir? (s/n)")
else:
    print("Gracias")

"""

numero = 50

while numero >= 0:
    if numero%5 == 0:
        print(numero)
    numero -= 1

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero>0:
        print(numero)
    else:
        break

