import random
print('**********************************************************')
print('Bienvenido al juego donde tienes que adivinar el numero!')
print('Python piensa en un numero, puedes adivinar que numero es?')
print('Recuerda que solo tienes 5 intentos!\n')

attemps : int = 0
number : int = random.randint(1,50)
total_attemps : int = 5

while attemps < 5:
        my_number : int = int(input('Indica el numero a adivinar ====>  '))
        if my_number < number:
            attemps += 1
            attemps_left = total_attemps - attemps
            print('Incorrecto, debe ser un numero mas alto.')
            print(f'\nTe quedan {attemps_left} intentos.')
        elif my_number > number:
            attemps += 1
            attemps_left = total_attemps - attemps
            print('Incorrecto, debe ser un numero mas bajo.')
            print(f'\nTe quedan {attemps_left} intentos.')
        else:
            print(f'Ganaste! El numero elegido por Python es el {number}.')
            break
else:
    print('\n************************************')
    print('Perdiste, te quedaste sin intentos!')
    print('Fin del juego!')
    print('************************************')
