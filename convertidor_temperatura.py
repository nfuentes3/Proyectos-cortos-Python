"""Definimos un script que tome del usuario una temperatura y que sea 
convertida segun las opciones disponibles."""
#Inicializando las variables con su type.
celsius : float = 0
fahrenheit : float = 0

#Definimos las funciones que convierten las temperaturas.
def to_celsius(fahrenheit):
    result = (fahrenheit - 32) / 1.8
    result = round(result, 2)
    print(f'La temperatura {fahrenheit}° Fahrenheit es igual a {result}° Celsius.')

def to_fahrenheit(celsius):
    result = (celsius * 1.8) + 32
    result = round(result, 2)
    print(f'La temperatura {celsius}° Celsius es igual a {result}° Fahrenheit.')

#Definimos funcion segun los argumentos pasados.
def temp_converter(unit, value):
    while True:
        if unit == 'c' or unit == 'C':
            to_fahrenheit(value)
            break
        if unit == 'f' or unit == 'F':
            to_celsius(value)
            break
        else:
            print('Datos incorrectos.')
            break

#invocamos la funcion con distintas pruebas.
temp_converter('c', 30)
temp_converter('F', 75.7)
temp_converter('q', 23)
temp_converter('f', 56)
temp_converter('B', 12)
