# 2.escribe una función que verifique si la palabra dada es palíndrome (una palabra que se lee igual
#  en ambos sentidos).
def isPalindrome(palabra):
    for i in range(0, len(palabra), 1):

        if palabra[i] == palabra[len(palabra)-1-i]:
            continue
        else:
            return False
    return True

    # print(palabra[i])
    # print(palabra[len(palabra)-1-i])


b = isPalindrome("")
print(b)

##################################################################################

# # 3. monedas : escribe una función que determine cuántas monedas de 25 centavos, de 10
# centavos, de 5 centavos y de 1 centavo le dará a un cliente para un cambio en el que minimice la cantidad de monedas que entrega.
# Ejemplo: dado 87 centavos, el resultado debe ser 3 cuartos, 1 centavo, 0 níquel y 2 centavos


def monedas(numero):
    monedas = [25, 10, 5, 1]
    cantidad = []
    for moneda in monedas:
        cantidad.append(int(numero/moneda))
        numero -= ((int(numero/moneda))*moneda)
    return cantidad


b = monedas(87)
print(b)

# 4.BONUS - factorial - Escribe una función recursiva que devuelve el factorial de un
#  número dado. Recuerde que el factorial de un número es el producto de todos los
#  números entre 1 y el número dado (por ejemplo, 4! = 4 * 3 * 2 * 1).


def factorial(num):
    fac = 1
    for i in range(num, 1, -1):
        fac *= i
    return fac


print(factorial(6))


def factorial(n):
    """ Precondición: n entero >=0
        Devuelve: n! """
    if n == 0:
        return 1

    return n * factorial(n-1)

# 5. Escribe una función recursiva que acepta un número, n, y devuelve el enésimo número de
# Fibonacci de la secuencia. Los primeros dos números de Fibonacci son 0 y 1. Cada número
# posterior se calcula sumando los 2 números anteriores de la secuencia.
#  (es decir, 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)
# Ejemplo: fibonacci (5) debería devolver 3 (el quinto número en la secuencia es 3).


def fib(num):
    if (num == 1):
        return 0
    else:
        lista = []
        if (num == 2):
            return 1
        else:

            return (fib(num-2)+fib(num-1))


b = fib(9)
print(b)
b = fib(3)
print(b)
b = fib(4)
print(b)
b = fib(9)
print(b)
