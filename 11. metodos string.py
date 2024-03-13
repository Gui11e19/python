""" 
upper() mayusculas txt[3].upper() posicion especifica
lower() minusculas 
split separar listas en partes txt.split("e") separador especifico
join() unir items con separador e = " ".join([a,b,c,d])
find() encontrar un substring res = txt.find("e") indices
replace() reemplazar unsubstring txt.replace("Guille","Andres")

a = "hola,"
b = "Guille"
c = "como"
d = "estas?"
e = " ".join([a,b,c,d])
print(e)

"""


txt = "Este es el texto de Guille"

res = txt.replace("Guille","Andres")

print(res)

