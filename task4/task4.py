def read_array_in_file(file):
    result = []
    f1 = open(file)
    for i in f1:
        temp = int(i)
        result.append(temp)
    f1.close()
    return result


def get_median(array):
    sorted_array = sorted(array)
    if len(sorted_array) % 2 == 0:
        index = len(sorted_array) // 2
        median = (sorted_array[index] + sorted_array[index - 1]) / 2
    else:
        median = sorted_array[len(sorted_array) // 2]
    return int(median)


array_file = 'file1.txt'
lst = read_array_in_file(array_file)

median = get_median(lst)

summa = 0
for v in lst:
    x = abs(v-median)
    summa += x

print(summa)
