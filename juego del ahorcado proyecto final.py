import random

def obtener_palabra_aleatoria():#definimos una variable
    palabras=["perro","gato","caja","sapo"]
    palabra_aleatoria=random.choice(palabras)#creamos otra variable con lafinalidad de introducir una palabra aleatoria de la lista de palbras con la funcion choice del modulo random.
    return palabra_aleatoria #por ultimo vamos a devolver nuestra palabra aleatoria

def mostrar_tablero(palabra_secreta, letra_adivinadas):#esta funcion se va a encargar de mostrar el estado actual del tablero del juego.
    tablero=""#creamos una variable inicializada como una cadena vacia
    for letra in palabra_secreta:#se crea este bucle para recorrer la palabra secreta
       if letra in palabra_secreta:
           tablero+=letra  #si se cumple la condicion vamos a agregar al tablero esa letra
       else:
           tablero+="_" #esto significa que la letra no ha sido adivinada 
    print(tablero)   #se imprime tablero


def jugar_ahorcado():#funcion principal del juego
    palabra_secreta=obtener_palabra_aleatoria()#se llama a la funcion palabra aleatoria, con la finalidad que me devuelva una palabra de la lista que se creo al inicio 

    letra_adivinadas=[]#se crea la lista de palabras adivinadas como una lista vacia porque al inicio no tiene nada 

    intentos_restantes=6 #se inicializa los intentos con un maximo de 6 
    while intentos_restantes>0: #se ejecutara mientras nos queden intentos 

        mostrar_tablero(palabra_secreta,letra_adivinadas)
        letra =input("introduce una letra").lower()#se le pide al usuario que ingrese una letra y se guardara en la variable letra y se convertira en minuscula de manera automatica
        if letra in letra_adivinadas:#se compara si la letra que introduce el usuario esta en la lista de letras adivinadas 
            print("ya has introducido esa letra") #se le envia un mensaje de aviso al usuario 
            continue     #se utiliza esta instruccion para saltarnos todos los pasos del bucle y regresar a la primera instruccion 
        if letra in palabra_secreta: #se comprueba si la letra que el usuario escribe esta dentro de la palabra secreta
            letra_adivinadas.append(letra)# se añade esta letra a la lista de palabras adivinidas mediante la funcion .append 
            if set(letra_adivinadas)==set(palabra_secreta): #se compara si letras adivinadas y la palabra secreta son iguales, mediante la funcion set que esta funcion se utiliza para crear conjuntos
                print ("felicidades, ganaste")
                break #se termina el bucle
        else:
            intentos_restantes-=1 #se le resta un intento al usuario 
            print(f"letra incorrecta, te quedan {intentos_restantes}") #dentro del mensaje se le envia la cantidad de intentos que le quedan al usuario
    if intentos_restantes==0:
        print(f"Perdiste, la palabra secreta es {palabra_secreta}")#un ultimo mensaje avisandole al usuario que perdio todos sus intentos
jugar_ahorcado()#se llama a la funcion para que se inicialice 


        
    
        
               
        
        
        

            
