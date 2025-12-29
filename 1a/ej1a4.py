'''
Enunciado:
Crea una función llamada "count_vowels(text_chain)" que reciba como parámetro
una cadena de texto de tipo string llamada 'text_chain' y retorne el número
de vocales, ya sean mayúsculas o minúsculas, sin tilde que se encuentren en dicha 
cadena de texto.

Parámetros:
- text_chain: Este parámetro admite únicamente strings.

Ejemplo: 
    Entrada:
    count_vowels('Hello world, this is an example.')

    Salida:
    9

'''

def count_vowels(text_chain:str):
    
    if not isinstance(text_chain, str):
        raise TypeError("El valor debe ser una cadena de texto")

    return sum(1 for letra in text_chain.lower() if letra in 'aeiou')

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
try:
    print(count_vowels("Hello world, thIs is an example."))
except TypeError as e:
    print(f'ERROR {e}')