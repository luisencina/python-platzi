def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = { "firstname": "Luis", "lastname": "Encina" }

    super_list = [
        { "firstname": "Luis", "lastname": "Encina" },
        { "firstname": "Felipe", "lastname": "Aceval" },
        { "firstname": "Carmen", "lastname": "Gavilan" },
        { "firstname": "María", "lastname": "Gómez" },
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, " - ", value)
    
    for i in super_list:
        print("----")
        # print(i["firstname"], " - ", i["lastname"]) or the next one
        for key, value in i.items():
            print(key, " - ", value)


if __name__ == "__main__":
    run()