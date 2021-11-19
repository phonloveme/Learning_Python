def is_sort(col_num):

    # считывание всех строк
    file = open("task3.txt", "r")
    lst = file.read().split()
    file.close()

    # сортировка нужного столбца
    file = open("task3.txt", "r")
    num_list = []
    count = 0
    while count != 4:
        all_num = file.readline().split()
        num_list.append(all_num[col_num-1])
        count += 1
    num_list = [int(i) for i in num_list]
    num_list.sort()
    num_list = [str(i) for i in num_list]
    file.close()

    # замена элементов столбца
    count = 0
    if col_num == 1:
        num_elem = 0
        nm = 0
        while count != 4:
            lst[num_elem] = num_list[nm]
            num_elem += 6
            nm += 1
            count += 1
    else:
        num_elem = 0 + (col_num - 1)
        nm = 0
        while count != 4:
            lst[num_elem] = num_list[nm]
            num_elem += 6
            nm += 1
            count += 1

    # вывод в файл
    sorted_file = open("task3_sorted.txt", "w")
    width_count = 0
    st = 0
    en = 6

    while width_count != 4:
        for i in range(st, en):
            sorted_file.write(lst[i])
            sorted_file.write(" ")
        sorted_file.write("\n")
        st += 6
        en += 6
        width_count += 1
    sorted_file.close()


column = int(input("Введите номер столбца: "))
is_sort(column)
