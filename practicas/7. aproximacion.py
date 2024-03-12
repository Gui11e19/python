#round
valor1 = float(input("Ingresa un divisor: "))
valor2 = float(input("Ingresa un dividendo: "))
decimal = int(input("Ingresa cantidad de decimales: "))
resultado = valor1/valor2

redondeo = round(resultado,decimal)

print(f"El resultado es {redondeo}, con la cantidad de decimales {decimal}")