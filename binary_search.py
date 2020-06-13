'''Алгоритм бинарного поиска'''

'''Бинарный поиск - это поиск позиции элемента в массиве данных в середине списка с последующим делением на два.'''

'''Например:'''
'''128 = 64 = 32 = 16 = 8 = 4 = 2 = 1 # стандартное число шагов поиска - 7'''
'''256 = 128 = 64 = 32 = 16 = 8 = 4 = 2 = 1 # если увеличить массив на два, шагов будет 8''''

'''Код бинарного поиска в реализации Python:'''

def binary_search(list, item):

  low = 0
  high = len(list)-1

  while low <= high:
    mid = (low + high)
    guess = list[mid]
    
    if guess == item:
      return mid
    elif guess > item:
      high = mid - 1
    else:
      low = mid + 1

  return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 7)) # ответ - 3
print(binary_search(my_list, 2)) # ответ - Null (позиция отсутствует
