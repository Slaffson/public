try:
    array = list(map(int, input('Введите случайные числа, разделяя их пробелом: ').split()))
    element = int(input('Введите число:  '))
except ValueError as er:
    print('Вы ввели что-то не то, надо вводить цифры через пробел!')
    print('\n \n \n \n \n \n \n ------------------------------------------------------------------')
try:
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    print('Отсортированный список:  ', array) # удалить после проверки работоспособности

    def binary_search(array, element, left, right):
        if left > right:
            return False

        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)

    Zadanie_1 = binary_search(array, element, 0, len(array)) - 1

    if Zadanie_1 < 0:
        print('После сортировки, ваше число стоит на самом первом месте, честно, перед ним ничего нет! Левее просто некуда ;) ')
        quit()
    print('Номер позиции (индекс) элемента меньше заданного числа - ', Zadanie_1)
except IndexError as er:
    print('Кажется последнее введенное число не входит в список искомых... Как хош так и понимай =Р ')
    print('\n \n \n \n \n \n \n ------------------------------------------------------------------')