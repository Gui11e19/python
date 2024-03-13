"""Tú trabajas en una empresa donde los vendedores reciben comisiones
del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores 
a calcular sus comisiones creando un programa que les pregunte su nombre y 
cuánto han vendido en este mes. Tu programa le va a responder con una frase 
que incluya su nombre y el monto que le corresponde por las comisiones."""

nombres = (input("Ingresa tus nombres: "))
apellidos = (input("Ingresa tus apellidos: "))
ventas = float(input("Ingresa total de ventas: "))
comision = round(ventas*0.13,2)

print(f"El vendedor {nombres} {apellidos}, \nVendio una cantidad total de: ${ventas} \nSu total de comisiones es ${comision}")