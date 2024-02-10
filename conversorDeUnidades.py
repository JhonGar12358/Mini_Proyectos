# Crea un programa que convierte entre diferentes unidades de medida, como longitud, masa o temperatura.
# Los estudiantes pueden implementar funciones para convertir de una unidad a otra y luego crear una interfaz de usuario simple.

print("CONVERSOR DE UNIDADES")

unidad = int(input("Que unidad desea convertir?\n*1) Masa\n*2) Longitud\n*3) Temperatura\n"))
resultado = 0

if unidad == 1:
    entrada_1 = int(input("Ingrese la opcion de conversion: \n1 - Libras a Kilos\n2 - Kilos a Libras\n3 - Kilos a Toneladas\n4 - Toneladas a Kilos"))
    
    if entrada_1 == 1:
        print("Libras a Kilos")
        entrada_1 = float(input("Ingresa la cantidad en Libras: "))
        resultado = round(entrada_1/2)
    elif entrada_1 == 2:
        print("Kilos a Libras")
        entrada_1 = float(input("Ingresa la cantidad en Kilogramos: "))
        resultado = round(entrada_1*2)
    elif entrada_1 == 3:
        print("Kilos a Toneladas")
        entrada_1 = float(input("Ingresa la cantidad en Kilogramos: "))
        resultado = round(entrada_1/1000)
    elif entrada_1 == 4:
        print("Toneladas a Kilos")
        entrada_1 = float(input("Ingresa la cantidad en Toneladas: "))
        resultado = round(entrada_1*1000)
    print("El resultado de la conversión es: {} ".format(resultado))

elif unidad == 2:
    entrada_2 = int(input("Ingrese la opcion de conversion: \n1 - Milimetros a Centimetros\n2 - Centimetros a Milimetros\n3 - Centimetros a Metros\n4 - Metros a Centimetros\n5 - Metros a Kilometros\n6 - Kilosmetros a Metros\n"))

    if entrada_2 == 1:
        print("Milimetros a Centimetros")
        entrada_2 = float(input("Ingresa la cantidad en Milimetros: "))
        resultado = round(entrada_2/10)
    elif entrada_2 == 2:
        print("Centimetros a Milimetros")
        entrada_2 = float(input("Ingresa la cantidad en Centimetros: "))
        resultado = round(entrada_2*10)
    elif entrada_2 == 3:
        print("Centimetros a Metros")
        entrada_2 = float(input("Ingresa la cantidad en Centimetros: "))
        resultado = round(entrada_2/100)
    elif entrada_2 == 4:
        print("Metros a Centimetros")
        entrada_2 = float(input("Ingresa la cantidad en Metros: "))
        resultado = round(entrada_2*100)
    elif entrada_2 == 5:
        print("Metros a Kilometros")
        entrada_2 = float(input("Ingresa la cantidad en Metros: "))
        resultado = round(entrada_2/1000)
    elif entrada_2 == 6:
        print("Kilometros a Metros")
        entrada_2 = float(input("Ingresa la cantidad en Kilometros: "))
        resultado = round(entrada_2*1000)
    print("El resultado de la conversión es: {} ".format(resultado))

elif unidad == 3:
    entrada_3 = int(input("Ingrese la opcion de conversion:\n1 - Celcius a Fahrenheit\n2 - Fahrenheit a Celcius\n3 - Fahrenheit a Kelvin\n4 - Kelvin a Fahrenheit\n"))

    if entrada_3 == 1:
        print("Celcius a Fahrenheit")
        entrada_3 = float(input("Ingresa la cantidad en Celcius: "))
        resultado = (entrada_3 * 9/5) + 32
    elif entrada_3 == 2:
        print("Fahrenheit a Celcius")
        entrada_3 = float(input("Ingresa la cantidad en Fahrenheit: "))
        resultado = (entrada_3 - 32) * (5/9)
    elif entrada_3 == 3:
        print("Fahrenheit a Kelvin")
        entrada_3 = float(input("Ingresa la cantidad en Fahrenheit: "))
        resultado = (entrada_3 - 32) * 5/9 + 273.15
    elif entrada_3 == 4:
        print("Kelvin a Fahrenheit")
        entrada_3 = float(input("Ingresa la cantidad en Kelvin: "))
        resultado = (entrada_3 - 273.15) * 9/5 + 32
    print("El resultado de la conversión es: {} ".format(resultado))
