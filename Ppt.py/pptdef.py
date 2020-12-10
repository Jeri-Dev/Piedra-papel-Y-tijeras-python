import time
from random import randint

opciones = ['1. piedra', '2. papel', '3. Tijeras']


def juego():
    for i in opciones:
        print('opcion  ', i)
        time.sleep(1)

    opcion = int(input('Que vas a usar usar?: '))
    time.sleep(1)

    if opcion == 1:
        print('Haz elgido piedra')
        time.sleep(1)
       
        print('tu oponente esta eligiendo...')
        time.sleep(1)
       
        poto = randint(1, 3)
        
        if poto == 1:
            print('La decision del oponente fue Piedra')
            time.sleep(1)
        elif poto == 2:
             print('La decision del oponente fue Papel')
             time.sleep(1)
        elif poto == 3:
            print('La decision del oponente fue Tijeras')
            time.sleep(1)

        if poto == 1:
            print('Los dos jugadores han elegido piedra')
            time.sleep(1)

            volver = input('quieres volver a jugar?(si o no): ')
            if volver == 'si':
                juego()

            juego()
        elif poto == 2:
            print('Tu oponente a ganado ya que Papel mata a piedra!')
            time.sleep(1)

            volver = input('quieres volver a jugar?(si o no): ')
            if volver == 'si':
                juego()
            
        elif poto == 3:
            print('Haz ganado ya que piedra vence a tijeras tijeras')
            time.sleep(1)

            volver = input('quieres volver a jugar?(si o no): ')
            if volver == 'si':
                juego()
        

    elif opcion == 2:
        print('Haz elgido papel')
        time.sleep(1)

        print('tu oponente esta eligiendo...')
        time.sleep(1)
       
        poto = randint(1, 3)
        
        if poto == 1:
            print('La decision del oponente fue Piedra')
            time.sleep(1)
        elif poto == 2:
             print('La decision del oponente fue Papel')
             time.sleep(1)
        elif poto == 3:
            print('La decision del oponente fue Tijeras')
            time.sleep(1)

        if poto == 1:
            print('Haz ganado ya que Papel vence a Piedra!')
            time.sleep(1)

            volver = input('quieres volver a jugar?(si o no): ')
            if volver == 'si':
                juego()

            juego()
        elif poto == 2:
            print('Los dos jugadores han elegido Papel')
            time.sleep(1)

            volver = input('quieres volver a jugar?(si o no): ')
            if volver == 'si':
                juego()
            
        elif poto == 3:
            print('Tu oponente a ganado ya que Tijeras vence a Papel')
            time.sleep(1)
            
            volver = input('quieres volver a jugar?(si o no): ')
            if volver == 'si':
                juego()        
       
        print('tu oponente esta eligiendo...')
        time.sleep(1)
    elif opcion == 3:
        print('Haz elgido tijeras')
        time.sleep(1)

        print('tu oponente esta eligiendo...')
        time.sleep(1)
       
        poto = randint(1, 3)
        
        if poto == 1:
            print('La decision del oponente fue Piedra')
            time.sleep(1)
        elif poto == 2:
             print('La decision del oponente fue Papel')
             time.sleep(1)
        elif poto == 3:
            print('La decision del oponente fue Tijeras')
            time.sleep(1)

        if poto == 1:
            print('Tu oponente a ganado ya que Piedra mata a Tijeras')
            time.sleep(1)

            volver = input('quieres volver a jugar?(si o no): ')
            if volver == 'si':
                juego()

        elif poto == 2:
            print('Haz ganado ya que Tijeras vence a Papel')
            time.sleep(1)

            volver = input('quieres volver a jugar?(si o no): ')
            if volver == 'si':
                juego()
            
        elif poto == 3:
            print('Los dos jugadores han elegido Tijeras')
            time.sleep(1)
            
            volver = input('quieres volver a jugar?(si o no): ')
            if volver == 'si':
                juego()

        print('tu oponente esta eligiendo...')
        time.sleep(1)
    else:
        print('Esta opcion no se encuentra...')
        time.sleep(1)

        juego()

#juego()
#poto = randint(1, 3)      
#print(poto)    