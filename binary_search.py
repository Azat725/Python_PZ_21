# Импортирование модуля random
import random  

# Создание случайного списка из 10 чисел от 1 до 100
random_array = random.sample(range(1, 100 + 1), 10)  
# Сортировка списка в порядке возрастания
sorted_array = sorted(random_array)  
# Вывод отсортированного списка
print(sorted_array)  
# Ввод числа для поиска
user_num = int(input("Введите число, которое нужно найти в списке -> "))  


# Определение функции для поиска числа в списке
def find_target(array: list, target: int):  
    sorted_array = sorted(array)  
    low = 0
    heigh = len(sorted_array) - 1
    guess = array[mid]  
    count = 0
    # Цикл поиска
    while low <= heigh:  
        mid = (heigh - low) // 2
        count += 1
        guess = sorted_array[mid] 
        if target == guess:  
            return f"Число {target} найдено на позиции {guess} за {count} шагов"
        elif target < guess:
            heigh = mid - 1  
        elif target > guess:
            low = mid + 1
    return f"Число {target} не найдено в списке"

print(find_target(random_array, user_num))  