def run():
    my_list = [1, "Hello", True, 4.5] #lista
    my_dict = {"firstname": "Eduardo", "lastname": "Hoppenstedt"} #lista

    #listas dentro de diccionarios y viceversa:
    super_list = [
       {"firstname": "Eduardo", "lastname": "Hoppenstedt"},
       {"firstname": "Susana", "lastname": "Horia"},
       {"firstname": "Aquiles", "lastname": "Brinco"},
       {"firstname": "Deborah", "lastname": "Mesta"},
    ]

    super_dict = {
        "natural_nums":[1,2,3,4,5,6],
        "integer_nums":[-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 2.1, 3.1, 4.5]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for key, value in super_list.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()
