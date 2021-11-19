def is_summary(all_num):
    num_summ = 0
    for i in range(0, len(all_num)):
        num_summ += int(all_num[i])
    return f"Сумма чисел равна {num_summ}"


file = open("task1.txt", "r")
line = file.read().split()
file.close()
print(is_summary(line))
