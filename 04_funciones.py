# funcion que suma
def sumar(n1,n2):
    return n1 + n2

def literal_genero(genero):
    if str(genero).upper() == "H":
        return "HOMBRE"
    if genero == "m":
        return "MUJER"
    else:
        return "DESCONOCIDO"

n1 = int(input("Dime el primer numero para sumar"))
n2 = int(input("Dime el segundo numero para sumar"))
print(sumar(n1,n2))

gro = input("DIME tu GENERO (h/m)")
print(literal_genero(gro))