def bubble_sort(list):
    is_sorted = False
    k = 1
    while not is_sorted:
        is_sorted = True
        for i in range(len(list) - k):
            if list[i] > list[i + 1]:
                temp = list[i + 1]
                list[i + 1] = list[i]
                list[i] = temp
                is_sorted = False
        k += 1
    return list
