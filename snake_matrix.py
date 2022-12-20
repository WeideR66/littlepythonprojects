#Заполнение матрицы произвольной формы змейкой цифрами от 1 до ...

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(str(matrix[i][j]).ljust(3), end=" ")
        print()


params = [int(i) for i in input().split()]
matrix = [[0 for j in range(params[1])] for i in range(params[0])]
count = 1
start_i, start_j = 0, 0
stop_i, stop_j = params[0] - 1, params[1] - 1
stop_cycle = params[0] * params[1]
while True:
    for j in range(start_j, stop_j + 1):
        matrix[start_i][j] = count
        count += 1
    start_i += 1
    if count - 1 == stop_cycle:
        break
    for i in range(start_i, stop_i + 1):
        matrix[i][stop_j] = count
        count += 1
    stop_j -= 1
    if count - 1 == stop_cycle:
        break
    for j in range(stop_j, start_j - 1, -1):
        matrix[stop_i][j] = count
        count += 1
    stop_i -= 1
    if count - 1 == stop_cycle:
        break
    for i in range(stop_i, start_i - 1, -1):
        matrix[i][start_j] = count
        count += 1
    start_j += 1
    if count - 1 == stop_cycle:
        break

print_matrix(matrix)