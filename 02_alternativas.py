edad = int(input("Dime tu edad"))

if edad >= 18:
    print("eres mayor de edad")
else:
    print ("eres menor de edad")

opcion = input("introduzca opcion (insert, update, delete): ")

if opcion == "insert":
    print("añadiendo")
elif opcion == "update":
    print("actualizando")
elif opcion == "delete":
    print("eliminando")
else:
    print("opcion errónea")

print("CON MATCH")

match opcion:
    case 'insert':
        print('insertando')
    case 'update':
        print('modif.')
    case 'delete':
        print('eliminando')
    case _:
        print('opcion eronea')