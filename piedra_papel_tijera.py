import random

# Diccionario de valores (No se usan como diccionario per se, pero se podria utilizar.)
values = {
    1: 'Piedra',
    2: 'Papel',
    3: 'Tijera'
}
# Definimos la funcion que evalua el juego.


def game():
    # Inicializamos los puntos.
    cpu_score : int = 0
    human_score : int = 0
    print('******************************************************')
    print('Bienvenido a Piedra, Papel o Tijera!\nDemuestra que puedes vencer a Python en un duelo a 3 puntos.')
    # Definimos los bucles para la partida con los la suma de los contadores
    while cpu_score < 3 and human_score < 3:
        cpu_choice : int = random.randint(1, 3)  # Eleccion del CPU
        print('\nEliga entre una de las opciones(Indique entre 1, 2 y 3): ')
        print('\n 1) Piedra\n 2) Papel\n 3) Tijera')
        human_choice : int = int(input('Eleccion: '))  # Eleccion del humano

        # Creamos las condiciones de los puntos
        if (human_choice == 1 and cpu_choice == 3) or (human_choice == 2 and cpu_choice == 1) or (human_choice == 3 and cpu_choice == 2):
            human_score += 1
            print('Has ganado la ronda!')
            print('Resultado parcial:')
            print(f'\n Humano: {human_score}\n Python: {cpu_score}')
            print('******************************************************')
        elif human_choice == cpu_choice:
            print('Es un empate!')
            print('******************************************************')
        else:
            cpu_score += 1
            print('Ha ganado Python!')
            print('Resultado parcial:')
            print(f'\n Humano: {human_score}\n Python: {cpu_score}')
            print('******************************************************')
    else:
        print('Fin de la partida.')

    if human_score == 3:
        print('\nHas ganado!')
        print(
            f'Resultado final: \n Humano: {human_score}\n Python: {cpu_score}')
    else:
        print('\nHas Perdido!')
        print(
            f'Resultado final: \n Humano: {human_score}\n Python: {cpu_score}')


game()
