import random


def is_matrix(column, width):
    count = 0
    matrix = []

    while count != column:
        for i in range(width):
            matrix.append(str(random.randint(-100, 100)))
            matrix.append(" ")
        matrix.append('\n')
        count += 1

    file = open("task2.txt", "w")
    file.writelines(matrix)
    file.close()


a = int(input("Введите количество столбцов: "))
b = int(input("Введите ширину: "))

is_matrix(a, b)
