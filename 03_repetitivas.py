for i in range(0,10):
    print(i)

print("OPCION")

opcion = 1
while opcion <= 10:
    print(opcion)
    opcion += 1

nombre = "Edu"
for letra in nombre:
    print(letra)

frase = "En un lugar de la mancha cuyo lugar no quiero acordarme"
i = 0
for word in frase.split(" "):
    print(word)
    for letra in frase.split(" ")[i]:
        print(letra)
    i += 1

print("SOLO LETRAS")  
for letter in frase:
    print(letter)

# frase.split(" ") = [En, un, lugar]
# frase = [e,n, ,u,n, ,l,u,]
# frase[0] = "e"
# frase.split(" ")[1] = "un"

cucu = frase.split(" ")
cucu.insert(1, "cucudrulu")

# "convierte" la lista en una especie de diccionario con los valores y la posicion (i)
print("ENUMERATE")
for i, valor in enumerate(cucu):
    print(f'{i} => {valor}')

opcion = 1
print ("has dicho {}".format(opcion))
print("has dicho {opcion}")
print(f"has dicho {opcion} {cucu}")