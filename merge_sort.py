

def merge_sort(input):
    length_input = len(input)
    if length_input == 1:
        return input
    split_point = length_input // 2

    left_side = merge_sort(input[:split_point])
    right_side = merge_sort(input[split_point:])

    return merge(left_side, right_side)

def merge(left, right):

    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output

if __name__ == '__main__':
    values = [5,9,6,0,1,3]
    print(values)
    sorted_list = merge_sort(values)
    print(sorted_list)

