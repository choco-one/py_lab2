
def uni_inter():
    list_1 = []
    list_2 = []

    list_1 = input('1st list: ').replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
    list_2 = input('2nd list: ').replace('[', ' ').replace(']', ' ').replace(',', ' ').split()

    list_1 = list(map(int, list_1))
    list_2 = list(map(int, list_2))

    set_1 = set(list_1)
    set_2 = set(list_2)

    print('=> union ', set_1 | set_2)
    print('=> intersection ', set_1 & set_2)
