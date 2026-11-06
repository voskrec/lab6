numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]

# Через словарь с подсчётом
from collections import Counter
counts = Counter(numbers)
#сортируем что принт выведет только те числа чьё колл больше 1
duplicates = [num for num, count in counts.items() if count > 1]
print (duplicates)