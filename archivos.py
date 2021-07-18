def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

#en este programa
def write():
    with open("./archivos/names.txt", "w", encoding="utf-8") as n: #si cambiamos "w" por "a", al correr el código se agregarán los nombres al final.
        name = []
        while name != "N":
            name = input("Agrega un nombre a la lista: ", "\n", "(Escribe N para detener el programa)")
            if name != "N":
                n.write(name)
                n.write("\n")

def run():
    write()


if __name__=='__main__':
    run()