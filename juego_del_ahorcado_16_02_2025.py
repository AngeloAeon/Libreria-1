def juego_ahorcado():
    letra = ''
    secreta = ''
    vector1 = []
    vector2 = []
    x = n = a = error = c = 0

    print('Hola, bienvenido al juego del ahorcado, ¿deseas jugar?')
    secreta = input('Ingresa la palabra secreta: ')
    n = len(secreta)
    vector1 = list(secreta)
    vector2 = ['_'] * n

    a = 0
    while a < 5:
        for x in range(n):
            print(vector2[x], end='')
        print('')
        a += 1
        letra = input("Ingrese una letra: ")
        error = 1
        for x in range(n):
            if letra == vector1[x]:
                if vector2[x] == "_":
                    vector2[x] = letra
                    c += 1
                    error = 0
        if c == n:
            print("¡Felicidades, has ganado el juego!")
            a = 6
        else:
            if error == 1:
                a += 1
            if a == 1:
                print(".")
                print(".")
                print(".")
                print(".")
                print("Te quedan 4 intentos")

juego_ahorcado()