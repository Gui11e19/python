texto = input("Ingresa un texto: ").lower()
letras = []
i = 0
while i <3:
    letras.append(input("Ingresa una letra: ").lower())
    i += 1

j = 0
letra1 = 0
letra2 = 0
letra3 = 0
contador_letras = 0

for letra in texto:
    contador_letras += 1
    if letra == letras[0] in texto:
        letra1 += 1
        #print(letra1)
    elif letra == letras[1] in texto:
        letra2 += 1
        #print(letra2)
    elif letra == letras[2] in texto:
        letra3 += 1
        #print(letra3)
    j+=1
palabras = texto.split()

validador = " "
if "Python" in texto:
    validador = "Si"
else:
    validador = "No"

print(f"Tengo {letra1} letra '{letras[0]}' ")
print(f"Tengo {letra2} letra '{letras[1]}' ")
print(f"Tengo {letra3} letra '{letras[2]}' ")
print(f"El total de letras es {contador_letras}")
print(f"El total de palabras es {len(palabras)}")
print(f"El texto al reves es\n '{texto[::-1]}'")
print(f"La palabra Python se encuentra en el texto {validador}")
