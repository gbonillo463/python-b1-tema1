"""
Enunciado:
Implementar la función 'obtain_max(list_numbers)' que recibe 
como parámetro una lista no vacía de números enteros y devuelve
el número mayor de la lista.

Recuerda que en Python existe la función llamada 'max'

Parámetros:
- list_numbers: Lista de números enteros

Ejemplo:
    Entrada:
    obtain_max([1, 45, 87, 21, 0, 23, 28])

    Salida:
    87

"""

def obtain_max(list_numbers):
    
    if not all(isinstance(n, int) for n in list_numbers):	
        raise ValueError("Todos los valores deben ser enteros")	
    
    if not all(n >= 0 for n in list_numbers):
        raise ValueError("Todos los valores deben ser números enteros")
    
    return max(list_numbers)
    

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
try:
    print(obtain_max([1, 45, 87, 21, 0, 23, -28]))
except ValueError as e:
    print(f'ERROR {e}')