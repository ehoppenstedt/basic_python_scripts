import os
import random



def welcome():
    os.system("clear")

def read():
    word = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            word.append(line.strip().upper())
    return(word)

# def select_word(data): #selecciona aleatoriamente una palabra de la lista y la convierte en un array de caracteres
    

def run():
    data = read()
    palabra = random.choice(data)
    palabra_array = [letter for letter in palabra]
    palabra_incognita = ["_"]*len(palabra_array) #string con _ equivalentes al número de letras de la palabra elegida aleatoriamente
    indice_letras = {}
    for idx, letter in enumerate(palabra):
        if not indice_letras.get(letter):
            indice_letras[letter] = []
        indice_letras[letter].append(idx)

    while True:
        welcome()
        print("Bienvenido al juego del ahorcado","\n","\n","Comienza a Jugar", "\n")
        print("¡Adivina la palabra!")
        for element in palabra_incognita:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in palabra_array:
            for idx in indice_letras[letter]:
                palabra_incognita[idx] = letter
        
        if "_" not in palabra_incognita:
            os.system("clear")
            print("\n"*3,"*"*10,"\n"*2)
            print("¡Ganaste! La palabra es:","\n", palabra, "\n"*2,"*"*10)
            break

if __name__=='__main__':
    run()