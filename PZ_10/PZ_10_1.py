# Средствами языка Python сформировать два текстовых файла (.txt),
# содержащих по одной последовательности из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Элементы первого файла, отсутствующие во втором:
# Элементы второго файла, отсутствующие в первом:
# Количество элементов:
# Индекс первого минимального элемента:
# Индекс последнего максимального элемента:

from random import *

spisok1 = []
spisok2 = []

for i in range(randint(1, 10)):
    spisok1.append(randint(-20, 20))

for i in range(randint(1, 10)):
    spisok2.append(randint(-20, 20))

file1 = open("file1.txt", "w+")
print(str(spisok1).strip("[]"), file=file1)
file1.close()

file2 = open("file2.txt", "w+")
print(str(spisok2).strip("[]"), file=file2)
file2.close()

oba = spisok1 + spisok2
v1 = []
v2 = []
chet = 0

for i in spisok1:
    for r in spisok2:
        if i != r:
            chet += 1
    if chet == len(spisok2):
        v1.append(i)
    chet = 0

for i in spisok2:
    for r in spisok1:
        if i != r:
            chet += 1
    if chet == len(spisok1):
        chet = 0
        v2.append(i)

file3 = open("file3.txt", "w+")
print("Содержимое первого и второго файла:", str(oba).strip("[]"), file=file3)
print("Элементы первого файла, отсутствующие во втором:", str(v1).strip("[]"), file=file3)
print("Элементы второго файла, отсутствующие во втором:", str(v2).strip("[]"), file=file3)
print("Количество элементов:", len(oba), file=file3)
print("Индекс первого минимального элемента:", oba.index(min(oba)), file=file3)
print("Индекс последнего максимального элемента:", oba.index(max(oba)), file=file3)
file3.close()
