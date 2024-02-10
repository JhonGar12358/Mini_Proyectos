# Simulador de Banco de Datos:
# Desarrolla un programa que actúe como un pequeño banco de datos.
# Los usuarios pueden agregar, actualizar y eliminar registros. Pueden implementar funciones de búsqueda y visualización de datos.

print("BIENVENIDO AL BANCO DE DATOS")

banco = {
    # 1: {
    #     "nombre": "Miguel",
    #     "edad": 23,
    #     "estatura": 1.79,
    #     "profesion": "Ingeniero"
    # },
    # 2: {
    #     "nombre": "Sebastin",
    #     "edad": 21,
    #     "estatura": 1.78,
    #     "profesion": "Estudiante"
    # }
}



def añadir(nombre, edad, estatura, profesion):
    banco[1] = {
        "nombre": nombre,
        "edad": edad,
        "estatura": estatura,
        "profesion": profesion
    }
    print (banco)


# añadir("Miguel", 23, 1.79, "ingeniero")
# print(banco)

def actualizar(id):
    while True:
        banco[id]["nombre"] = input("Ingrese nuevo Nombre: ")
        banco[id]["edad"] = input("Ingrese nueva edad: ")
        opcion = input("numero")
        if opcion == "5":
            break




print(banco)

# def eliminar(id):
#     del banco[id]


desicion= input("Que deseas hacer?:\n1 - añadir usuario\n2 - actualizar ususario\n3 - Borrar Usuario\n")

if desicion == "1":
    print("añadiendo nuevo...")
    nombre= input("nombre del usuario: ")
    edad = int(input("edad del usurio: "))
    estatura = float(input("estatura del usuario: "))
    profesion = input("profesion del usuario: ")

    añadir(nombre, edad, estatura, profesion)

# elif desicion == 2:
#     print (banco)
#     id = input




# print("↓ La lista de abajo ya está eliminada ↓")

# eliminar(1)
# print(banco)


# print("la cantidad de usuarios almacenados actualmente es de: ", len(banco))

# def agregar(nombre, edad, estatura, profesion):
#     banco[{
#             nombre: nombre 
#         }
#         {
#             edad: edad
#         }
#         {
#             estatura: estatura
#         }
#         {
#             profesion: profesion
#         }]
    

# opcion = input("Que quieres hacer?\n1 - agregar registros\n2 - actualizar registros\n3 - eliminar registros\n\n")
# while opcion > 0 and opcion < 4:
#     if opcion == 1:
        
