"""
Script básico para un Algoritmo de la División y un Algoritmo que determine el Máximo Común Divisor de dos números.

MEL SEC04 20211
    
"""



def printMenu():
    print("\nBuenas\n")
    print("*" * 60)
    print("1- Algoritmo para dividir enteros")
    print("2- Máximo común divisor")
    print("*" * 60)


def algoritmoDivision(n: int, d: int):

    q = 0 # se inicializa en 1 porque cuando 'q' es cero 'r = n'
    r = n # r es el residuo
    
    if d > 0:
        
        while (r >= d):
            r = r - d
            q += 1

        print("{0} = ({1} * {2}) + {3}".format(n, q, d, r))

    else:
        print("'d' no puede ser igual a cero")



def maxComDivisor(n: int, d: int):
    if n > 1 and d > 1:

        primero = n

        segundo = d

        turno = True  # variable para ir cambiando la resta

        while primero != segundo:

            if turno:
                segundo = abs(primero - segundo)
                turno = False

            else:
                primero = abs(primero - segundo)
                turno = True

        print("mcd({0},{1}) = {2}".format(n, d, primero))

    else:
        print("'N' y 'D' deben ser mayores que 1.")
        



while __name__ == "__main__":
    printMenu()

    opcion = input("Ingrese la opción que desea:\n~ ")

    if opcion == '1':
        n = int(input("Elija un N mayor o igual a cero:\n~ "))
        d = int(input("Elija un D mayor que cero:\n~ "))

        algoritmoDivision(n, d)  # La función imprime el resultado
        
    elif opcion == '2':
        n = int(input("Elija un N mayor a uno:\n~ "))
        d = int(input("Elija un D mayor a uno:\n~ "))

        maxComDivisor(n, d)  # La función imprime el resultado

    else:
        exit()
    