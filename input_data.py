"""
Dane wejściowe: N-elementowy ciąg liczb naturalnych wczytywany z klawiatury (n<=10) oraz generowany przez generator
danych będący częścią/modułem programu.

Wygeneruj n-elementowe ciągi liczb naturalnych podanych w postaci losowej, rosnącej, malejącej,
za każdym razem przetestuj dla 5 różnych wartości n z przedziału <10,50>

"""
import random


def manual_generator():
    array_len_ok = False
    array_ints = False

    while not (array_ints and array_len_ok):
        num = []
        array_ints = True
        num_str = input('Type numbers, comma separated and list length n<=10:')
        num_str = num_str.split(',')
        for el in num_str:
            try:
                num.append(int(el))
            except (ValueError, TypeError):
                print(f'Mistake in typing "{el}".')
                array_ints = False
                num = []
        if len(num) in range(1, 11):
            array_len_ok = True
        else:
            array_len_ok = False
            print("List is not in range. ")

    return num


def auto_random(len_list):
    num = []
    for x in range(len_list):
        num.append(random.randrange(1000))
    return num


def auto_up(len_list):
    num = auto_random(len_list)
    num.sort()
    return num


def auto_down(len_list):
    num = auto_up(len_list)
    num.reverse()
    return num


def main():
    data_manual = manual_generator()
    print("User list: ", data_manual)
    data_auto_random = auto_random(20)
    print("Auto random list: ", data_auto_random)
    data_auto_up = auto_up(20)
    print("Auto up list: ", data_auto_up)
    data_auto_down = auto_down(20)
    print("Auto down list: ", data_auto_down)


if __name__ == '__main__':
    main()
