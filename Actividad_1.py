# 1. Leemos por consola dos números enteros y calculamos y mostramos por la consola:
# a. La suma
# b. La resta
# c. El producto
# d. La división
# e. La división entera
# f. El resto de su división

def ejercicio1():
    n1 = int(input("Introduce un numero \n"))
    n2 = int(input("Introduce otro numero \n"))
    print(f"""
    la suma es : {n1 + n2} \n
    la resta es: {n1 - n2} \n
    la multiplicacion es: {n1 * n2} \n 
    la division es: {n1 / n2} \n
    la division entera es {int(n1 / n2)} \n
    el resto es: {n1 % n2}
    """)

# 2. Leer consecutivamente dos números cada vez, hasta que los dos sean -1. Comparar
# los dos números leídos e informar cada vez si son iguales, mayor o menor (el primero
# respecto al segundo). Al final del proceso informar cuantas veces los números eran
# iguales, cuantas veces el primero era mayor del segundo y cuantas veces el primero
# era menor del segundo número leído.


def ejercicio2():
    while True:
        n1 = int(input("Introduce un numero \n"))
        n2 = int(input("Introduce otro numero \n"))
        contador_iguales = 0
        contador_n1_mas_que_n2 = 0
        contador_n2_mas_que_n1 = 0
        # logica
        if n1 == -1 and n2 == -1:
            break
        elif n1 > n2:
            numeros = 1
            contador_n1_mas_que_n2 += 1
        elif n2 > n1:
            numeros = 2
            contador_n2_mas_que_n1 += 1
        else:
            numeros = 3
            contador_iguales += 1

        # resultados
        match numeros:
            case 1:
                print("El numero 1 es mayor a el numero 2")
            case 2:
                print("El numero 2 es mayor a el numero 1")
            case 3:
                print("Los numeros son iguales")
    # Resultados
    print(f"Los numeros han sido iguales {contador_iguales} veces")
    print(f"El numero 1 ha sido mayor a el numero 2 {contador_n1_mas_que_n2} veces")
    print(f"El numero 2 ha sido mayor a el numero 1 {contador_n2_mas_que_n1} veces")

# 3. Escribir los números múltiplos de 3 y de 7, que hay entre el 1 y el 250. Y además
# escribir al final, cuántos de los 250 son:
# a. Múltiplos de 3 y de 7.
# b. Cuantos hay múltiplos de 3
# c. Cuantos hay múltiplos de 7.
# d. Cuantos no son múltiplos de ni de 3 ni de 7.
# Ojo la suma de todos NO da 250. Tened en cuenta que por ejemplo el número 21, es
# múltiplo de 3 y 7 , por tanto lo es de 3 y lo es de 7.
# Recordar que un número es múltiplo de otro cuando al dividirlos su resto es cero.

def ejercicio3():

    # Múltiplos de 3 recorremos los 250 números para compararlos con el 3
    def comporbar_multiplos(numero):
        print(f"Vamos a comprobar los múltiplos de {numero}")
        contador_multiplos = 0
        for i in range(1,250):
            if i % numero == 0:
                contador_multiplos += 1
        return contador_multiplos
    print(f"Hay {comporbar_multiplos(3)} multiplos de 3")
    print(f"Hay {comporbar_multiplos(7)} multiplos de 7")
    print(f"Hay {comporbar_multiplos(7) + comporbar_multiplos(3)} multiplos de los dos, en total,"
          f" en los primeros 250 numeros ")
    print(f"{250 - (comporbar_multiplos(7) + comporbar_multiplos(3))} numeros del 1 al 250 no son muliplos de niunguno")

# 4. Para que un triángulo sea válido se tiene que cumplir que la suma de dos cualquiera
# de sus lados siempre tiene que ser mayor que el tercero(en todas sus
# combinaciones).
# a. Crear una función que reciba los tres lados y devuelva True si el triángulo es
# válido, y False si el triángulo no es válido
# b. Tras llamar a esta función si no es válido informar y si es válido, determinar si
# es equilatero(los tres lados iguales, isósceles(2 lados iguales y uno desigual, o
# escaleno, los tres lados distintos.

def ejercicio4():
    triangulo = [
        int(input("Introduce el primer lado \n")),
        int(input("Introduce el segundo lado \n")),
        int(input("Introduce el tercer lado \n")),
    ]

    def triangulo_valido(lados):
        a, b, c = lados
        if (a + b > c) and (a + c > b) and (b + c > a):
            return True
        else: return False

    if not triangulo_valido(triangulo):
        print("El triángulo NO es válido.")
    else:
        a, b, c = triangulo
        if a == b == c:
            tipo = "equilátero"
        elif a == b or a == c or b == c:
            tipo = "isósceles"
        else:
            tipo = "escaleno"
        print("El triángulo ES VALIDO. \n")
        print(f"El triangulo es de tipo {tipo}")

# 5. Pedir por consola el nombre, el apellido y el salario y el sexo(“H” o “M”) de una
# persona
# a. Escribir toda la información de lo tecleado de la siguiente forma:
# b. Nombre completo en mayúsculas + el literal de sexo: Hombre para H, Mujer
# para M + el literal del salario: Bajo si el salario es menor de 30.000; Medio
# entre 30.000 y 50.000; Alto si es mayor de 50.000.
# c. El nombre completo, el literal del sexo y el salario hacerlo en sendas
# funciones previas al algoritmo.

def ejercicio5():

    nombreInp = input("Introduce el nombre de la persona \n")
    apellidoInp = input("Introduce el apellido de la persona \n")
    salarioInp = int(input("Introduce el salario de la persona \n"))
    sexoInp = input("Introduce el sexo de la persona (h/m) \n")

    def literal_nombre(nombre, apellido):
        return str(nombre).upper() + " " + str(apellido).upper()

    def literal_sexo(sexo):

        match str(sexo).upper():
            case "H":
                sexo = "MASCULINO"
            case "M":
                sexo = "FEMENINO"
        return sexo

    def literal_salario(salario):
        if salario < 30000: salario = "Bajo"
        elif salario < 50000: salario = "Medio"
        else: salario = "Alto"
        return salario

    print(f" Su nombre es: {literal_nombre(nombreInp, apellidoInp)}, sexo: {str(literal_sexo(sexoInp))}, "
          f"salario: {str(literal_salario(salarioInp))}")

def flujo():
    print("Ejercicio 1 \n \n")
    #ejercicio1()
    print("Ejercicio 2 \n \n")
    #ejercicio2()
    print("Ejercicio 3 \n \n")
    #ejercicio3()
    print("Ejercicio 4 \n \n")
    #ejercicio4()
    print("Ejercicio 5 \n \n")
    ejercicio5()
if __name__ == "__main__":
    flujo()