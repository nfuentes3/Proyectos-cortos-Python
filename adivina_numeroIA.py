import random
import time
print('**********************************************************')
print('Bienvenido al juego donde tienes que adivinar el numero!')
print('Python piensa en un numero entre el 1 y el 50, puedes adivinar que numero es?')
print('Recuerda que solo tienes 5 intentos!\n')
time.sleep(1)

attemps : int = 0
number : int = random.randint(1,50)
total_attemps : int = 5

while attemps < 5:
        while True:
            my_number = input('Indica el numero a adivinar ====>  ')
            try:
                my_number = int(my_number)
                break
            except ValueError:
                print('La opcion ingresada es incorrecta, debe elegir un numero.')
                time.sleep(1)

            
        if my_number < number:
            attemps += 1
            attemps_left = total_attemps - attemps
            print('Incorrecto, debe ser un numero mas alto.')
            time.sleep(1)
            print(f'\nTe quedan {attemps_left} intentos.')
        elif my_number > number:
            attemps += 1
            attemps_left = total_attemps - attemps
            print('Incorrecto, debe ser un numero mas bajo.')
            time.sleep(1)
            print(f'\nTe quedan {attemps_left} intentos.')
        else:
            print(f'Ganaste! El numero elegido por Python es el {number}.')
            time.sleep(3)
            break
else:
    print('\n************************************')
    print('Perdiste, te quedaste sin intentos!')
    print('Fin del juego!')
    print('************************************')
    time.sleep(3)