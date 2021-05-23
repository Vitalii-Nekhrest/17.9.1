def input_val(): # Функция ввода целых чисел
    while type:
        numbers = input("Введите целые числа через пробел: ")
        try:
            base_list = list(map(int, numbers.split()))
            if len(base_list) == 0: # Защита от дурака (если введено не целое число)
                raise ValueError
        except ValueError:
            print("Данные числа не являются целыми")
        else:
            break
    while True: # Ввод числа
        digit = input("Введите целое число: ")
        try:
            number = int(digit)
        except ValueError: # Защита от дурака (если введено не целое число)
            print('"{0}" не является целым числом'.format(digit))
        else:
            break
    formatted_list = base_list + [number]
    print(search_binary(ranging(base_list),number,0,len(formatted_list))) # Вызов функций сортировки и поиска

def ranging(base_list): # Сортировка (Поскольку студет SkillFactory использовал "любимую" студенческую сортировку;) )
    for i in range(len(base_list)):
        for j in range(len(base_list) - i - 1):
            if base_list[j] > base_list[j + 1]:
                base_list[j], base_list[j + 1] = base_list[j + 1], base_list[j]
    return base_list

def search_binary(list, element, left, right): # Функция Дробного поиска согласно заданию
    if left > right:
        return f"Введенного числа нет в списке"

    middle = (right + left) // 2 # нахождение середини
    if list[middle] == element: # если элемент в середине
        if element == list[0]: # если число минимальное в списке
          return f"Индекс числа {middle} - это число найменшее в списке, Индекс следующего числа {middle+1}"
        else:
           return f"Индекс числа {middle}, Индекс предидущено числа {middle-1} ,Индекс следующего числа {middle+1}"
    elif element == list[-1]: # если число максимальное в списке
          return f"Индекс числа {middle} - это число найбольшее в списке, Индекс предедущего числа {middle - 1}"
    elif element < list[middle]: #если элемент меньше элемента в середине рекурсивно ищем в левой половине
        return search_binary(list, element, left, middle - 1)
    else: # иначе в правой
        return search_binary(list, element, middle + 1, right)
input_val()