import random
import time

#Creamos diccionario con los valores para ser mostrados en consola
values = {
    1: 'Piedra',
    2: 'Papel',
    3: 'Tijera'
}

#Creamos la funcion con la dinamica del juego.
def game_ppt():
    print('******************************************************')
    print('Bienvenido a Piedra, Papel o Tijera!\nDemuestra que puedes vencer a Python en un duelo a 3 puntos.')
#Definimos las variables con los puntos
    cpu_score = 0
    human_score = 0
    
    while cpu_score < 3 and human_score < 3: #Creamos condiciones de puntos + eleccion de opciones.
        cpu_choice = random.randint(1,3)
        time.sleep(2)
        print('\nEliga entre una de las opciones(Indique entre 1, 2 y 3): ')
        print('\n 1) Piedra\n 2) Papel\n 3) Tijera')
        human_choice = int(input('Opcion: '))
        
        while human_choice < 4 and human_choice > 0:
            if (human_choice == 1 and cpu_choice == 3) or (human_choice == 2 and cpu_choice == 1) or (human_choice == 3 and cpu_choice == 2):
                print(f'===========> Has elejido {values[human_choice]}.')
                print(f'===========> Python elije {values[cpu_choice]}.')
                human_score += 1
                time.sleep(1)
                print('*** ¡Ganaste! ***')
                time.sleep(1)
                print(f'\nResultado Parcial: Tú = {human_score} / Python = {cpu_score}')
                break
            elif human_choice == cpu_choice:
                print(f'===========> Has elejido {values[human_choice]}.')
                print(f'===========> Python elije {values[cpu_choice]}.')
                time.sleep(1)
                print('---- Empate ----')
                time.sleep(1)
                print(f'\nResultado Parcial: Tú = {human_score} / Python = {cpu_score}')
                break
            else:
                print(f'===========> Has elejido {values[human_choice]}.')
                print(f'===========> Python elije {values[cpu_choice]}.')
                cpu_score +=1
                time.sleep(1)
                print('¡¡¡ Perdiste !!!')
                time.sleep(1)
                print(f'\nResultado Parcial: Tú = {human_score} / Python = {cpu_score}')
                break
        
        else: 
            print('Opcion incorrecta, elija entre las opciones indicadas.')
    else: 
        if human_score == 3:
            print('\nHas ganado!!!')
            time.sleep(1)
            print(f'Resultado final:\nTú = {human_score} / Python = {cpu_score}')
        elif cpu_score == 3:
            print('\nHas Perdido!!!')
            time.sleep(1)
            print(f'Resultado final:\nTú = {human_score} / Python = {cpu_score}')
            time.sleep(4)
            
game_ppt()