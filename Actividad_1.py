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
    while (True):
        n1 = int(input("Introduce un numero \n"))
        n2 = int(input("Introduce otro numero \n"))
        contador_iguales = 0
        contador_n1_mas_que_n2 = 0
        contador_n2_mas_que_n1 = 0
        # logica
        if n1 == -1 and n2 == -1:
            break
        elif (n1 > n2):
            numeros = 1
            contador_n1_mas_que_n2 += 1
        elif (n2 > n1):
            numeros = 2
            contador_n2_mas_que_n1 += 1
        else:
            numeros = 3
            contador_iguales += 1

        # resultados
        match (numeros):
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

    # Multiplos de 3 recorremos los 250 numeros para compararlos con el 3
    def comporbar_multiplos(numero):
        print(f"Vamos a comprobar los multiplos de {numero}")
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

#


def flujo():
    print("Ejercicio 1 \n \n")
    ejercicio1()
    print("Ejercicio 2 \n \n")
    ejercicio2()
    print("Ejercicio 3 \n \n")
    ejercicio3()

if __name__ == "__main__":
    flujo()