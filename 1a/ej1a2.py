'''
Enunciado:
Crea una función 'sum_odd_numbers(list_numbers)' que reciba como 
parámetro una lista de números positivos enteros llamada 'list_numbers'
y devuelva la suma de los números impares encontrados en la lista.
Considerar que 'list_numbers' debe contener valores numéricos enteros mayores
o iguales a '0', en caso contrario se debe mostrar un error tipo 'ValueError'.

El error lo puedes mostrar con la siguiente instrucción:    
raise ValueError("MENSAJE DE ERROR")

Parámetros:
- list_numbers: Lista de números enteros positivos.

Ejemplo:
	Entrada:
	sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

	Salida:
	30

'''

def is_odd(number) -> bool:
	return number % 2 != 0


def sum_odd_numbers(list_numbers):
	
	total_odd_sum = 0

	for number in list_numbers:

		if not all(isinstance(n, int) for n in list_numbers):
			raise ValueError("Todos los valores deben ser enteros")
	
		if not all(n >= 0 for n in list_numbers):
			raise ValueError("Todos los valores deben ser >= 0")
		
		elif is_odd(number):
			total_odd_sum += number
	
	return total_odd_sum


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100]))
