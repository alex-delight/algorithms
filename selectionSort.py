'''Алгоритм сортировки выбором'''

'''Функция для поиска наименьшего элемента массива:'''

def find Smallest(a r r):
  smallest = arr[0] # для хранения наименьшего значения
  smallest_index = 0 # для хранения индекса наименьшего значения
  for i in range(l, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index
  
  '''Теперь на основе этой функции можно написать функцию сортировки выбором:'''
  
def selectionSort(arr): # сортирует массив
  newArr = []
  for i in range(len(arr)):
    smallest = indSmallest(arr) # находит наименьший эпемент в массиве и добавляет ero в новый массив
    newArr.append(arr.pop(smallest))
  return newArr
  
print(selectionSort([S, З, 6, 2, 10]))
