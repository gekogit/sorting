import input_data


def counting_sort(data_list):
    min_in_data_list = min(data_list)
    histogram_base = list(range(min_in_data_list, max(data_list)+1))
    len_histogram = len(histogram_base)
    histogram = [0] * len_histogram

    for el in data_list:
        histogram[el-min_in_data_list] +=1

    data_sorted = []
    for x in range(0, len_histogram):
        if histogram[len_histogram - x-1] > 0:
            for repeat in range(0, histogram[len_histogram - x-1]):
                data_sorted.append(histogram_base[len_histogram - x-1])
    return data_sorted


def main():
    print(counting_sort(input_data.auto_random(20)))
    print(counting_sort([2, 3, 8, -5, 4, -2, 6, 7, 9, 3, 4, 6]))


if __name__ == '__main__':
    main()