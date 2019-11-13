from functools import reduce

# сумма чисел от 1 до 2^25
print(sum(range(1, 2**25+1)))

# факториал 100
print(str(reduce(lambda x, y: x*y, [i for i in range(1, 1001)])))

# Найти элементы списка, отсутствующие в другом
print(list(set(['one', 'two', 'three', 'four', 'five', 'six', 'seven']) - set(['two', 'four', 'six', 'eight'])))

# Удвоить все нечётные числа в списке
print([i*2 if i % 2 == 1 else i for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]])

# Считать чтрочку с клавиатуры и развернуть
print(input("Your string : ")[::-1])