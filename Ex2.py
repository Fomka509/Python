import numpy as np
from scipy import stats

array = []
with open("array.txt") as f:
    for line in f:
        array.append([float(x) for x in line.split()])

min = min(array)
max = max(array)
mean = np.mean(array)
rms = np.std(array)
moment = stats.moment(array, moment=5)
print(array)
print(min)
print(max)
print(mean)
print(rms)
print(moment)

array1 = np.random.randint(-50, 51, 10)
print('рандомные целые числа', array1)

array5 = sorted(array1)
print('по возрастанию', array5)

array2 = np.random.randint(-50, 51, 10)
array3 = array1 + 1j * array2
print('рандомные комплексные числа', array3)

print('сортировка по модулю', sorted(array3, key=abs))

array6 = sorted(array3, reverse=True)
print('по убыванию действительной части', array6)

length_str = ['program', 'i', 'python', 'today', 'on']
print('сортировка списка строк по длине', sorted(length_str, key=len))

alf_str = ('program', 'i', 'python', 'today', 'on')
print('сортировка кортежа строк по алфавиту', sorted(alf_str))

alf_sp = ([3, 'bye', 10, 'a', ['hello']], ['one'], [100, -20, 'new', 'old', 3], ['a', 'b', 'c'],[1, 2, 3])
print('сортировка кортежа списков по длине', sorted(alf_sp, key=len))