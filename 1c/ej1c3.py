"""
Enunciado:

Implementa una función llamada find_max(lst) que encuentre el valor máximo en una
lista de números utilizando recursión. La función debe devolver el valor
máximo de la lista.

Parámetros:
    lst (List): lista de números enteros o flotantes

Ejemplo:
    Entrada:
    numbers_list = [1, 5, 2, 7, 3]
    find_max(numbers_list)

    Salida:
    7

"""

def find_max(lst):

    if len(lst) <= 1:
        return lst[0]

    return find_max(lst[:-1]) if lst[-1] < lst[0] else find_max(lst[1:])
    

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
numbers_list = [1, 5, 2, 7, 3]
print(find_max(numbers_list))
