import input_data


def replace_in_pair(x, y):
    return y, x


def bubble_sort(data_list):
    len_data_list = len(data_list)
    len_working_list = len_data_list
    while len_working_list > 1:
        for pair in range(0, len_data_list-1):
            if data_list[pair] < data_list[pair + 1]:
                data_list[pair+1], data_list[pair] = replace_in_pair(data_list[pair+1], data_list[pair])
        len_working_list -= 1
    return data_list


def main():
    print(bubble_sort(input_data.auto_random(20)))
    print(bubble_sort([2, 3, 8, -5, 4, -2, 6, 7, 9, 3, 4, 6]))


if __name__ == '__main__':
    main()