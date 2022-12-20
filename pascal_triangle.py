"""Вывод треугольника Паскаля с n - строк"""

num = int(input())
pascal_triangle = list()
for i in range(num):
    pascal_triangle.append(list())
    for j in range(i + 1):
        if j == 0 or j == i:
            pascal_triangle[i].append(1)
        else:
            pascal_triangle[i].append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
print(*pascal_triangle, sep='\n')