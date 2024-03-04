import random  # Импортирование модуля random

def find_target(array: list, target: int):  # Определение функции для поиска числа в списке
    for item in range(len(array)):  # Цикл перебора элементов списка
        if array[item] == target:  # Сравнение текущего элемента со введенным числом
            return f"Число {target} найдено на позиции {item + 1} за {item + 1} шагов"  # Возврат результата, если число найдено
        else:  # Если число не найдено в текущей итерации цикла
            return f"Число {target} не найдено в списке"  # Возврат сообщения о том, что число не найдено

random_array = [random.randint(1, 100) for _ in range(10 + 1)]  # Создание списка из 10 случайных чисел от 1 до 100
print(random_array)  # Вывод созданного списка
user_num = int(input("Введите число, которое нужно найти в списке -> "))  # Ввод числа для поиска

print(find_target(random_array, user_num))  # Вывод результата поиска