'''
Enunciado:
Implementa una función llamada "invert_text(text_chain)" que reciba como
parámetro una cadena de texto de tipo string llamada 'text_chain' y devuelva
el texto invertido.

Parámetros:
- text_chain: Este parámetro solo admite strings.

Ejemplo:
    Entrada:
    invert_text('Hello world!')

    Salida:
    !dlrow olleH

'''

def invert_text(text_chain:str):
    
    if type(text_chain) != str:
        raise TypeError('El valor debe ser una cadena de texto')

    string_inverted = text_chain[::-1]
    
    return string_inverted



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
try:
    print(invert_text('Hello World!'))
except TypeError as e:
    print(f'ERROR {e}')