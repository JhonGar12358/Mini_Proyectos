# Crea un programa que permita a los usuarios agregar, editar y eliminar tareas en una lista.
# Pueden expandir el proyecto agregando funciones como la fecha de vencimiento y la prioridad de las tareas.

print("BIENVENIDO AL SISTEMA")

DiccWorks = {
        1: {
            "priority": "important",
            "date": "21/08/2024"
        },
        2: {
            "priority": "important",
            "date": "21/08/2024"
        },
        3: {
            "priority": "important",
            "date": "21/08/2024"
        }
    }

def add(word, priority, date):
    # if word != int:
    #     DiccWorks.append(word)
    # else:
    #     prit("No ingresaste una tarea valida")
    contador = DiccWorks + 1
    DiccWorks.update( {
        contador:{
            "priority": priority,
            "date": date
        }
    } )
    print(DiccWorks)


def delate(word):
    del DiccWorks[word]
    # arrayWorks.remove(word)
    print(DiccWorks)

def edit(word):
    for i in DiccWorks:
        if i == word:
            consulta = input("Qué valor desea editar? ")
            if consulta == "nombre":
                nombre = input("Ingrese el nuevo nombre: ")
                DiccWorks[word]= nombre
            # DiccWorks.remove(i)
            # temporal= i
            # editar = input("edita nuevamente la tarea: ")
            # temporal = editar
            # DiccWorks.insert(0,temporal)
            
            break
        else:
            print("la tarea que deseas editar no se escuentra!")
    print(DiccWorks)    

desire = int(input("Que deseas hacer con el programa de tareas?: \n1) AGREGAR\n2) EDITAR\n3) ELIMINAR\n"))

if desire == 1:
    var = input("Ingresa la tarea a agregar: ")
    priority = input("Ingrese el nivel de prioridad: ")
    date = input("Ingrese fecha limite: ")
    add(var, priority, date)
elif desire == 2:
    var = input("Ingresa la tarea a editar: ")
    edit(var)
elif desire == 3:
    var = input("Ingresa la tarea a eliminar: ")
    delate(var)
else:
    print("respuesta incorrecta")


