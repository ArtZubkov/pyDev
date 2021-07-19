'''  
       Программа ищет совпадения в файле с данными по определенным критериям 
       и выдает результат, который также записывается в другой файл.
'''

print('Критерии поиска: \n1. Вид спорта \n2. Страна возникновения \n3. Год возникновения')
n1 = input('\nВведите номера критериев для поиска (в строку): ').split()
s = [0,0,0]  
k = 0
p = False
m=[]

if n1.count('1') != 0:
    s[0]=input('1. Введите вид спорта: ')
else:
    if n1.count('2') != 0:
      s[1]=input('2. Введите страну возникновения: ')
    else:
      if n1.count('3') != 0:
         s[2]=input('3. Введите год возникновения: ')



print('\nРезультаты поиска: ')
for stroka in open('sport.txt'):
    mas = stroka.split()
    for i in range(3):
        if s[i] == mas[i] or s[i] == 0:
             k += 1
    if k == 3:
        p = True
        m.append(stroka.split())
        print(stroka, end='')
    k=0

file = open('result.txt', 'w')

for i in range(len(m)):
    for j in range(3):
        file.write(m[i][j])
        file.write(' ')
    file.write('\n')
file.close()

        
if p != True:
    print('Нет совпадений.')

