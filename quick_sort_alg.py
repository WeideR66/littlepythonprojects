import random
import copy

# Чисто параметры для проверки алгоритма
seed_value = 60  # зерно рандомайзера
kolvo_prov = 10  # количество проверок
arr_legth = 20  # длинна проверяемых списков
random.seed(seed_value)  # установка зерна


# Сам алгоритм быстрой сортировки.
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        index = random.randrange(0, len(array))
        middle = array[index]
        del array[index]
        lower_arr = [i for i in array if i <= middle]
        upper_arr = [j for j in array if j > middle]
        return quick_sort(lower_arr) + [middle] + quick_sort(upper_arr)


# Цикл проверки алгоритма. Он создает два одинаковых списка с рандомными значениями и затем сортируется встроенным
# методом sort и алгоритмом быстрой сортировки. Если все норм, то он выведет истину, если где то ошибка то выведет не
# истину.
for _ in range(kolvo_prov):
    prov = True
    arr1 = [random.randrange(-100, 100) for _ in range(arr_legth)]
    arr2 = copy.deepcopy(arr1)
    print(f'\nМассив 1: {arr1}\nМассив 2: {arr2}')
    arr1.sort()
    arr2 = quick_sort(arr2)
    print(f"Разные ли объекты (списки):{arr1 is not arr2}")
    print(
        f'Массив отсортированный встроенной функцией (1 массив):\n{arr1}\n'
        f'Массив отсортированный быстрой сортировкой (2 массив):\n{arr2}')
    seed_value += 1
    for arr_index in range(arr_legth):
        if not arr1[arr_index] == arr2[arr_index]:
            prov = False
            break
    print(f"Одинаково ли отсортированы списки: {prov}")
