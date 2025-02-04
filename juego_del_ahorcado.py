def juego_ahorcado():
    letra = ""
    secreta = ""
    vector1 = []
    vector2 = []
    x = 0
    n = 0
    a = 0
    error = 0

    print('Hola, bienvenido al juego del ahorcado, ¿deseas jugar?')
    secreta = input('Ingresa la palabra secreta: ')
    n = len(secreta)
    
    vector1 = list(secreta)
    vector2 = ['_'] * n
    
    while a < 5:
        for x in range(n):
            print(vector2[x], end=' ')
        print('')
        
        letra = input('Ingresa una letra: ')
        
        if letra in vector1:
            for x in range(n):
                if vector1[x] == letra:
                    vector2[x] = letra
        else:
            a += 1
        
        if '_' not in vector2:
            print('¡Felicidades! Has adivinado la palabra:', secreta)
            break
    else:
        print('Lo siento, has perdido. La palabra era:', secreta)

juego_ahorcado()