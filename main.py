#Выполнила Слуцкая Екатерина ИВТ, 2 курс
import threading

matrixX = [[1, 2], [3, 4]]
matrixY = [[5, 6], [7, 8]]


def calculate_element(row, col):
    Z = 0

    for i, item in enumerate(row):
        Z += item * col[i]
    return Z


def calculate_row(rowX, matrixY):
    cols = [[row[i] for row in matrixY] for i in range(len(matrixY[0]))]
    Z = list(map(lambda a: calculate_element(rowX, a), cols))
    print(Z)
    return Z


for row in matrixX:
    threading.Thread(target=calculate_row, args=(row, matrixY)).start()
