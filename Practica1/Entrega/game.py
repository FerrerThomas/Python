import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_attempts = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []

def levelDifficulty(secret_word,level):
    newWord = []
    match level:
        case 1:  #si el nivel elegido es facil
                vocales = "aeiou"
                for letter in secret_word:
                    if letter in vocales:   #muestro las vocales
                        newWord.append(letter)
                    else:
                        newWord.append("_")
        case 2:  #muestro la primera y ultima letra si la dificultad es 2
                primera = 0
                ultima = len(secret_word) -1
                actual = 0
                for letter in secret_word:
                    if (actual == primera) or (actual == ultima):
                        newWord.append(letter)
                    else:
                        newWord.append("_")
                    actual+=1
        case 3:
                newWord = ["_"] * len(secret_word)  #si el 3 por lo tanto no muestro ninguna letra
    return newWord


print("¡Bienvenido al juego de adivinanzas!")
print("""Elige un nivel de dificulta: |1| Facil
                             |2| Medio
                             |3| Dificil""")
level = int(input("Nivel: ")) #lee la dificultad
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Cargo la palabra segun la dificultad (con o sin letras ya debloqueadas)
letters = levelDifficulty(secret_word,level)

word_displayed = "".join(letters)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

#Cuento los fallos hasta llegar a mi maximo de fallos que seria "max_attempts"
fallos = 0

while (fallos < max_attempts):
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verifico que lo ingresado no sea vacio
    print() #solo para que quede mas bonito con una separacion :p
    if(not letter.isalpha()):
        print("EROR: Debe ingresar una letra")
        fallos+= 1  #Si el usuriario no ingresa nada, lo tomo como fallo  a mi criterio
    
    # Verificar si la letra ya ha sido adivinada  
    elif letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         fallos+= 1     #Si ingresa una letra que ya habia ingresado, lo tomo como fallo
         continue       #ya que inconcientemente uso un intento por decirlo de una manera
    
    # Verificar si la letra está en la palabra secreta
    elif letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        fallos+= 1 #Si la letra o esta, es un claro fallo

    # Agregar la letra a la lista de letras adivinadas        
    guessed_letters.append(letter)

    # Mostrar la palabra parcialmente adivinada
    i = 0
    for letter in secret_word:
        if letter in guessed_letters:
            letters[i] = letter
        i+= 1

    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")
