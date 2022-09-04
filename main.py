osoby = []

char_num = int(input("Podaj liczbę postaci: "))

for i in range(0, char_num):
    postac = (input("Bohater " + str(i+1) + ": "))
    postac = postac.upper()+'\n'
    osoby.append(postac)

import os
filetrack = os.path.abspath(input("Podaj nazwę pliku: "))
f = open(filetrack, 'r', encoding='utf-8')

print(repr(f.readline()))
s = f.readline()
a = f.readline()

while a not in osoby:
    p = (s)
    f1 = open(p, 'a+', encoding='utf-8')
    f1.write(a)
    a = f.readline()
    if a in osoby:
       s = a
       a = f.readline()
    elif len(a) == 0:
        break