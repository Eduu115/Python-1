fichero = open("ficheros/fichero.txt", "w")

fichero.write("Hola mundo")

fichero.close()

print("Final")

with open("fichero2.txt", "w") as fic:
    fic.write("pollica pelua")