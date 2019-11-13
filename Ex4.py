from scipy.fftpack import rfft, irfft, rfftfreq
import numpy as np
import math
import matplotlib.pyplot as plt
# время отображения
time = np.arange(0, 1, 0.001)
# частоты
f1 = 5
f2 = 9
f3 = 11
# Моделирование сигнала из трёх синусоид с некратными частотами
input = [3*math.sin(2*math.pi*t*f1)+5*math.sin(2*math.pi*t*f2)+7*math.sin(2*math.pi*t*f3) for t in time]
# Вывод исходного сигнала
plt.plot(time, input, color='blue')
plt.title('Исходный сигнал')
plt.xlabel('Время, сек')
plt.ylabel('Амплитуда, м')
plt.grid(True)
plt.show()
# Прибавление сгенерированного шума к исходному сигналу и его вывод
stray = np.random.uniform(-5, 5, np.size(time))
plt.plot(time, input + stray, color='red')
plt.title('Зашумленный сигнал')
plt.xlabel('Время, сек')
plt.ylabel('Амплитуда, м')
plt.grid(True)
plt.show()
# Вывод спектра зашумленного сигнала
spectr = rfft(input + stray)
plt.plot(rfftfreq(1000, 0.001), abs(spectr))
plt.title('Спектр зашумленного сигнала')
plt.xlabel('Частота, Hz')
plt.ylabel('Амплитуда, М')
plt.grid(True)
plt.show()
# Фильтрация шума по спектру и вывод спектра без шума
filtered_spectr = []
for i in range(0, len(spectr)):
    if abs(spectr[i]) > np.max(abs(spectr))/3:
        filtered_spectr.append(spectr[i])
    else:
        filtered_spectr.append(0)
plt.plot(rfftfreq(1000, 0.001), np.abs(filtered_spectr))
plt.title('Спектр без шума')
plt.xlabel('Частота, Hz')
plt.ylabel('Амплитуда, М')
plt.grid(True)
plt.show()
# Вывод отфильтрованного сигнала без шума
output = irfft(filtered_spectr)
plt.plot(time, output, color='green')
plt.title('Выходной сигнал без шума')
plt.xlabel('Время, сек')
plt.ylabel('Амплитуда, м')
plt.grid(True)
plt.show()
# Сравнение сигналов(исходного, зашумленого и отфильтрованного)
plt.plot(time, input, marker='x', markersize=4, color='Blue', label='Входной сигнал')
plt.plot(time, input + stray, linewidth=1, color='pink', label='Зашумленный сигнал')
plt.plot(time, output, linestyle='dashed', linewidth=2, color='green', label='Отфильтрованный сигнал')
plt.legend()
plt.grid(True)
plt.show()
print(np.max(abs(spectr)))