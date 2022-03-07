
import unittest

# 1.escribe una función que invierta los valores en la lista (sin crear una matriz temporal).


def reverse_list(lista):
    for i in range(0, len(lista), 1):
        numero = lista.pop(i)
        lista.insert(0, numero)
    return lista


class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(reverse_list([1, 3, 5]), [5, 3, 1])

    def testThree(self):
        self.assertNotEqual(reverse_list([1, 3, 5, 7, 6]), [1, 3, 5, 7, 6])

    def testFour(self):
        self.assertEqual(reverse_list([5, 1, 8, 4, 9, 6]), [6, 9, 4, 8, 1, 5])

    def setUp(self):

        print("running setUp")

    def tearDown(self):

        print("running tearDown tasks")


# if __name__ == '__main__':
#     unittest.main()
##################################################################################################
# 2.escribe una función que verifique si la palabra dada es palíndrome (una palabra que se lee igual
#  en ambos sentidos).


def isPalindrome(palabra):
    for i in range(0, len(palabra), 1):
        if palabra[i] == palabra[len(palabra)-1-i]:
            continue
        else:
            return False
    return True


class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(isPalindrome("racecar"), True)

    def testThree(self):
        self.assertFalse(isPalindrome("paralelepipedo"))

    def testFour(self):
        self.assertEqual(isPalindrome("aba"), True)

    def testFive(self):
        self.assertEqual(isPalindrome("aerea"), True)

    def testSix(self):
        self.assertEqual(isPalindrome("paralelepipedo"), False)

    def testSeven(self):
        self.assertFalse(isPalindrome("rajr"))

    def testEight(self):
        self.assertFalse(isPalindrome("andale"))

    def setUp(self):

        print("running setUp")

    def tearDown(self):

        print("running tearDown tasks")


# if __name__ == '__main__':
#     unittest.main()
#####################################################################################

# 3. monedas : escribe una función que determine cuántas monedas de 25 centavos, de 10
# centavos, de 5 centavos y de 1 centavo le dará a un cliente para un cambio en el que minimice la cantidad de monedas que entrega.


def monedas(numero):
    monedas = [25, 10, 5, 1]
    cantidad = []
    for moneda in monedas:
        cantidad.append(int(numero/moneda))
        numero -= ((int(numero/moneda))*moneda)
    return cantidad


class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(monedas(87), [3, 1, 0, 2])

    def testThree(self):
        self.assertNotEqual(monedas(103), [7, 0, 5, 1])

    def testFour(self):
        self.assertEqual(monedas(106), [4, 0, 1, 1])

    def testFive(self):
        self.assertEqual(monedas(77), [3, 0, 0, 2])

    def testSix(self):
        self.assertEqual(monedas(93), [3, 1, 1, 3])

    def testSeven(self):
        self.assertNotEqual(monedas(17), [4, 5, 1, 1])

    def testEight(self):
        self.assertNotEqual(monedas(28), [9, 0, 1, 1])

    def setUp(self):

        print("running setUp")

    def tearDown(self):

        print("running tearDown tasks")


# if __name__ == '__main__':
#     unittest.main()

#######################################################################################
# 4.BONUS - factorial - Escribe una función recursiva que devuelve el factorial de un
#  número dado. Recuerde que el factorial de un número es el producto de todos los
#  números entre 1 y el número dado (por ejemplo, 4! = 4 * 3 * 2 * 1).


def factorial(num):
    fac = 1
    for i in range(num, 1, -1):
        fac *= i
    return fac


class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(factorial(5), 120)

    def testThree(self):
        self.assertNotEqual(factorial(5), 24)

    def testFour(self):
        self.assertEqual(factorial(6), 720)

    def testSeven(self):
        self.assertNotEqual(factorial(6), 78)

    def setUp(self):

        print("running setUp")

    def tearDown(self):

        print("running tearDown tasks")


# if __name__ == '__main__':
#     unittest.main()

############################################################################################
# 5. Escribe una función recursiva que acepta un número, n, y devuelve el enésimo número de
# Fibonacci de la secuencia. Los primeros dos números de Fibonacci son 0 y 1. Cada número
# posterior se calcula sumando los 2 números anteriores de la secuencia.
#  (es decir, 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)
# Ejemplo: fibonacci (5) debería devolver 3 (el quinto número en la secuencia es 3).


def fibonacci(num):
    if (num == 1):
        return 0
    else:
        lista = []
        if (num == 2):
            return 1
        else:
            return (fibonacci(num-2)+fibonacci(num-1))


class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(fibonacci(5), 3)

    def testThree(self):
        self.assertNotEqual(fibonacci(3), 9)

    def testFour(self):
        self.assertEqual(fibonacci(9), 21)

    def testSeven(self):
        self.assertNotEqual(fibonacci(8), 7)

    def setUp(self):

        print("running setUp")

    def tearDown(self):

        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()
