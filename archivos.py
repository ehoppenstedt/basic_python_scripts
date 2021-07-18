def read():
    numbers = []
    with open("./python_intermedio/archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.apprend(int(line))
    print(numbers)

def write():
    pass

def run():
    read()


if __name__=='__main__':
    run()