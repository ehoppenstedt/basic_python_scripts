def run():
    my_dict = {}
    #usando for loop
    for i in range(1, 101):
        if i%3 !=0:
            my_dict[i] = i**3
    #usando dictionanry comprehension:
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    #ambas devuelven el mismo resultado,
    print(my_dict)

if __name__=='__main__':
    run()