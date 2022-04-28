import time
import bubble_sort
import counting_sort
import merge_sort
import heap_sort
import quick_sort
import input_data
import statistics
import matplotlib.pyplot as plt
import datetime
import save_to_file as file

number_of_lists = 5
first_col_width = 25
col_width = 10


def timepassed(func):
    def inside_f(len_list):
        start = time.perf_counter()
        func(len_list)
        stop = time.perf_counter()
        return 1000000*(stop - start)
    return inside_f

@timepassed
def speed_test_merge(len_list):
    for x in range(number_of_lists):
        merge_sort.merge_sort(input_data.auto_random(len_list))

@timepassed
def speed_test_heap(len_list):
    for x in range(number_of_lists):
        heap_sort.heap_sort(input_data.auto_random(len_list))


@timepassed
def speed_test_bubble(len_list):
    for x in range(number_of_lists):
        bubble_sort.bubble_sort(input_data.auto_random(len_list))


@timepassed
def speed_test_counting(len_list):
    for x in range(number_of_lists):
        counting_sort.counting_sort(input_data.auto_random(len_list))


@timepassed
def speed_test_quick(len_list):
    for x in range(number_of_lists):
        quick_sort.quick_sort(input_data.auto_random(len_list),0,len_list-1)


def row_result(name, input):
    row = ('|'+name.center(first_col_width))
    for element in input:
        row = row+('|'+str(round(element,1)).center(col_width))
    row += '|'
    return row


def make_raport(legend, results, lists_tests_len, number_of_lists):
    raport = f"""This program compared calculation time for 5 sorting algorithm:
    - merge sorting 
    - heap sorting
    - bubble sorting
    - counting sorting
    - quick list sorting
    
In this case was sorted {len(lists_tests_len)} sequence with length {str(lists_tests_len)} of natural numbers.
For each sequence length, the test was performed {number_of_lists} times. The results of the comparison are
 presented in the table below\n\n"""
    avr_report = ""
    raport += (((first_col_width+2)+(col_width+1)*len(lists_tests_len))*'_')+'\n'
    raport += row_result("Length list",lists_tests_len)+'\n'
    raport += (((first_col_width+2) + (col_width+1) * len(lists_tests_len)) * '-')+'\n'
    i = 0
    for time_result in results:
        raport += row_result(legend[i], time_result)+'\n'
        avr_report = avr_report + f'Average time for {legend[i].lower()} is {round(statistics.mean(time_result),2)}us\n'
        i = i+1
    raport +=(((first_col_width+2) +(col_width+1) * len(lists_tests_len)) * '-')+'\n\n'
    raport += avr_report
    return raport

def main():

    lists_tests_len = [10,20,30,40,50]#,100,200,500]
    results_merge = []
    results_heap = []
    results_bubble = []
    results_counting = []
    results_quick = []

    for tests_len in lists_tests_len:
        results_merge.append(speed_test_merge(tests_len)/number_of_lists)
        results_heap.append(speed_test_heap(tests_len)/number_of_lists)
        results_bubble.append(speed_test_bubble(tests_len)/number_of_lists)
        results_counting.append(speed_test_counting(tests_len)/number_of_lists)
        results_quick.append(speed_test_quick(tests_len) / number_of_lists)

    results = [results_merge, results_heap, results_bubble, results_counting, results_quick]
    legend = ["Merge sorting", "Heap sorting", "Bubble sorting", "Counting sorting", "Quick list sorting"]
    content = make_raport(legend, results, lists_tests_len, number_of_lists)

    #Print report on console
    print(content)

    #Save raport to file
    file.save('Test result from '+datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")+'.txt', content)

    # Plot graph
    for result in results:
        plt.plot(lists_tests_len, result)
    plt.xlabel('Number of sorted elements')
    plt.ylabel('Time[us]')
    plt.title('Compare sorting algorithms')
    plt.legend(legend)
    plt.show()


if __name__ == '__main__':
    main()
