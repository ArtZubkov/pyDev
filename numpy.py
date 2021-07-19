''' 
    Исследование функций. Уточнение корней с заданной степенью точности. 
    Вывод графиков.

'''


import matplotlib.pyplot as plt
import numpy as np

# Заданная функция.
def f(x):
    f = (x-1)*(x+2)
    return f

# Производная.
def f2(x):
    f2 = 2*x+1
    return f2

# 2 производная.
def f3(x):
    f3 = 2
    return f3


# Функция ввода.
def read():
    global a,b,h,e1,e2,maxiter,choice
    a = float(input('Введите a: '))
    b = float(input('Введите b: '))
    h = float(input('Введите шаг: '))
    choice = input('Выберите параметр точности x/y/x&y: ')
    if choice == 'x':
        e1 = float(input('Введите точность по x: '))
        e2 = abs(f(e1)-f(0))
    if choice == 'y':
        e1 = 5
        e2 = float(input('Введите точность по y: '))
    if choice == 'x&y':
        e1 = float(input('Введите точность по x: '))
        e2 = float(input('Введите точность по y: '))
    maxiter = float(input('Введите максимальное число итераций: '))


# Функция проверки корней на интервале a и b.
def check(a,b,f):
    t = 0
    h = 0.001
    i = a
    while i < b:
        if (f(i) * f(i+h)< 0.0) or abs(f(i))<e2 or f(i)==0 or f(i+h)==0:
            t = 1
            break
        i += h
    return t

# Функция уточнения корней методом половинного деления.
def poldel(a,b,f,f2,f3):
 global iters
 iters=0
 while b-a>=e1 or b-a>=e2:
      c=(a+b)/2      
      if f(a)*f(c)<=0:
         b=c
      else:
         a=c
      iters+=1
 return c

#Функция нахождения точек перегиба на отрезке.
def peregibi(a,b,h,f2,f3):
    a1 = a
    while f3(a1)*f3(a)>0:
        if f3(b)==0:
            a1 = b
            break
        if a1>b:
            a1=b
            break
        if f2(a)*f2(a1)<0:
            a = a1
        a1+=h
    return a,a1

#Функция проверки на точки перегиба.
def check_peregibi(a,b,h,f3):
    t = 1
    a1 = a
    if f3(a)==f3(b)==f3(a/0.5):
        return 0
    while f3(a1)*f3(a)>0:
        if f3(b)==0:
            break
        if a1>=b:
            t = 0
        a1+=h
    return t

# Функция нахождения экстремумов на отрезке.
def extr(a,b,h,f2):
    a1 = a
    while f2(a1)*f2(a)>0:
        if f2(b)==0:
            a1 = b
            break
        if a1>b:
            a1=b
            break
        a1+=h
    return a1

# Функция проверки на экстремумы.
def check_extr(a,b,h,f2):
    t = 1
    a1 = a
    while f2(a1)*f2(a)>0:
        if f2(b)==0:
            break
        if a1>b:
            t = 0
            break
        a1+=h
    return t

# Функция нахождения минимума и максимума.
def min_and_max(a,b,f):
    xmin,xmax = a,a
    min, max = f(a), f(a) 
    i = a+0.01
    while i<=b:
        if f(i)>max:
            max = f(i)
            xmax = i
        if f(i)<min:
            min = f(i)
            xmin = i
        i+=0.01
    return min,max,xmin,xmax

# Метод 3/8.
def tri_vos(func, a, b):
    n = 100000
    h = (b-a)/n
    e = 1
    sum1,sum2 = 0,0
    while e < n:
        if e % 3 == 0:            
            sum2 += func(a+h*e)
        else:
            sum1 += func(a+h*e)
        e += 1    
    sum = 3/8*h*(func(a)+func(b)+ 3*sum1 + 2*sum2)
    return sum
    
read()
while not check(a,b,f):
    print('На интервале [',a,';',b,'] для функции'
          +' f(x) = sin(x) корней не найдено.\n')
    read()
    
# Вывод корней.    
num = 1
print('\n                   '
      +'Корни функции f(x) = sin(x) найденные методом половинного деления.\n'+
      '                               (красные точки на графике)')
print('-'*108)
print('|  №  |             a |             b |        Корень |'
      +'             f(x) | Кол-во итераций |  Код ошибки*  |') 
print('-'*108)
korni = set()
i = a
while i < b:
    b1=i+h
    if i+h>b: b1=b
    if check(i,b1,f) and not(f(b1)== 0 and a<b1<b):
       if f3(i)*f3(b1)>=0 and not(check_peregibi(i,b1,0.01,f3)):
           k = poldel(i,b1,f,f2,f3)
       else:
           p = peregibi(i,b1,0.01,f2,f3)
           if check(i,p[1],f):
               k = poldel(p[0],p[1],f,f2,f3)
           elif check(p[1],i+h,f):
               k = poldel(p[1],b1,f,f2,f3)
           else:
               print('error pass')

           
       if iters > maxiter and a<=k<=b and k not in korni:
           kod = 1
           print('| ',num,' |','{:13.4f}'.format(i),'|',end=' ')
           print('{:13.4f}'.format(b1),'|',' '*12+'-',end=' ')
           print('|',' '*15+'-','|','{:15}'.format(iters),end=' ')
           print('|','{:13}'.format(kod),'|')
           num+=1

           
       elif iters <= maxiter and a<=k<=b:
           kod = 0
           korni.add(k)    
           print('| ',num,' |','{:13.4f}'.format(i),'|',end=' ')
           print('{:13.4f}'.format(b1),'|','{:13.7f}'.format(k),end=' ')
           print('|','{:16.1g}'.format(f(k)),'|','{:15}'.format(iters),end=' ')
           print('|','{:13}'.format(kod),'|')
           num+=1
       else:
           if not(a<=k<=b):
               kod = 2
               print('| ',num,' |','{:13.4f}'.format(i),'|',end=' ')
               print('{:13.4f}'.format(b1),'|',' '*12+'-',end=' ')
               print('|',' '*15+'-','|','{:15}'.format(iters),end=' ')
               print('|','{:13}'.format(kod),'|')
               num+=1
               
    i+=h

print('-'*108)
print('Код ошибки* : "0" - нет ошибки')
print('              "1" - превышение макс.кол-ва итераций')
print('              "2" - корень не в границах интервала\n\n')

# Вывод точек перегиба.
peregibs = set()
if check_peregibi(a,b,0.01,f3):
    print('Точки перегиба. \n(синие точки на графике)')
    print('-'*20)
    print('|  №  |      Точка |')
    print('-'*20)
    num = 1
    i = a
    while i <= b:
        if check_peregibi(i,i+h,0.001,f3):
            p=peregibi(i,i+h,0.0001,f2,f3)
            if a<=p[1]<=b and p[1] not in peregibs:
                peregibs.add(p[1])
                print('| ',num,'|{:12.6} |'.format(p[1]))
                num+=1
        i+=h
    print('-'*20,'\n\n')

else:
    peregibs.add('!')
    print('Точек перегиба не обнаружено.\n\n')

# Вывод экстремумов.
extremum = set()
if check_extr(a,b,0.01,f):
    print('Экстремумы функции. \n(голубые точки на графике)')
    print('-'*20)
    print('|  №  |  Экстремум |')
    print('-'*20)
    num = 1
    i = a
    while i <= b:
        if check_extr(i,i+h,0.001,f2):
            p=extr(i,i+h,0.00001,f2)
            if a<=p<=b and p not in extremum:
                extremum.add(p)
                print('| ',num,'|{:12.6} |'.format(p))
                num+=1
        i+=h
    print('-'*20,'\n\n')

else:
    extremum.add('!')
    print('Точек экстремумов не обнаружено.\n\n')

s = min_and_max(a,b,f)
print('Минимальное значение функции в точке ({:7.5f},{:7.5f} )'.format(s[2],s[0]))
print('Максимальное значение функции в точке ({:6.5f},{:7.5f} )'.format(s[3],s[1]))

# Рисуем график.
x = np.linspace(a,b,int(b-a)*100)
y = f(x)
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.axis([a*1.3, 2*b,-10,15])
plt.plot(x,y,label='$sin(x)$')
t=0
for i in korni:
    if t == 0:
        plt.scatter(i,0,edgecolors='red',label='$roots$')
        t+=1
        continue
    plt.scatter(i,0,edgecolors='red')
    
if '!' not in peregibs:
    for i in peregibs:
        if t ==1:
            plt.scatter(i,f(i),label='$peregib$')
            t+=1
            continue
        plt.scatter(i,f(i))
if '!' not in extremum:
    for i in extremum:
        if t == 2:
            plt.scatter(i,f(i),edgecolors='cyan',label='$extremum$')
            t+=1
            continue
        plt.scatter(i,f(i),edgecolors='cyan')
plt.scatter(s[2],s[0],edgecolors='magenta',label='$min$')
plt.scatter(s[3],s[1],edgecolors='magenta',label='$max$')
plt.legend(loc='upper right')
plt.show()






# Вычисляем точки пересечения двух функций.

#Функция два.
def g(x):
    return 1.5*np.cos(x)

def dva(x):
    return f(x) - g(x)

def dva_revers(x):
    return g(x)-f(x)
    
def dva2(x):
    return f2(x) + 1.5*np.sin(x)

def dva3(x):
    return f3(x) + 1.5*np.cos(x)




korni2 = []
print('\n                   '
      +'Точки пересечения функций f(x) = sin(x) и g(x) = 1.5*cos(x) .\n'+
      '                               (красные точки на графике)')
print('-'*108)
print('|  №  |             a |             b |        Корень |'
      +'        f(x)-g(x) | Кол-во итераций |  Код ошибки*  |') 
print('-'*108)


i = a
num = 0
h = 0.5
while i < b:
    if check(i,i+h,dva) and not(dva(i+h)== 0 and a<i+h<b):
       if dva3(i)*dva3(i+h)>=0 and not(check_peregibi(i,i+h,0.01,dva3)):
           k = poldel(i,i+h,dva,dva2,dva3)
       else:
           p = peregibi(i,i+h,0.01,dva2,dva3)
           if check(i,p[1],dva):
               k = poldel(p[0],p[1],dva,dva2,dva3)
           elif check(p[1],i+h,dva):
               k = poldel(p[1],i+h,dva,dva2,dva3)
           else:
               print('error pass')

           
       if iters > maxiter and a<=k<=b and k not in korni2:
           kod = 1
           print('| ',num,' |','{:13.4f}'.format(i),'|',end=' ')
           print('{:13.4f}'.format(i+h),'|',' '*12+'-',end=' ')
           print('|',' '*15+'-','|','{:15}'.format(iters),end=' ')
           print('|','{:13}'.format(kod),'|')
           num+=1

           
       elif iters <= maxiter and a<=k<=b:
           kod = 0
           korni2.append(k)    
           print('| ',num,' |','{:13.4f}'.format(i),'|',end=' ')
           print('{:13.4f}'.format(i+h),'|','{:13.7f}'.format(k),end=' ')
           print('|','{:16.1g}'.format(dva(k)),'|','{:15}'.format(iters),end=' ')
           print('|','{:13}'.format(kod),'|')
           num+=1
       else:
           if not(a<=k<=b):
               kod = 2
               print('| ',num,' |','{:13.4f}'.format(i),'|',end=' ')
               print('{:13.4f}'.format(i+h),'|',' '*12+'-',end=' ')
               print('|',' '*15+'-','|','{:15}'.format(iters),end=' ')
               print('|','{:13}'.format(kod),'|')
               num+=1
               
    i+=h
print('-'*108)
print('Код ошибки* : "0" - нет ошибки')
print('              "1" - превышение макс.кол-ва итераций')
print('              "2" - корень не в границах интервала\n\n')



#Функция для проверки какой график выше.
def higher(a,b,f,g):
    r = (a+b)/2
    if f(r)>g(r):
        return 1
    else:
        return 0
    



if len(korni2)==0:
    print('Графики не пересекаются.')
else :
    summa = 0
    for i in range(len(korni2)):
        if len(korni2)==1:
            
            if higher(a,korni2[0],f,g):
                summa += tri_vos(dva,a,korni2[0])
            else:
                summa += tri_vos(dva_revers,a,korni2[0])
                
            if higher(korni2[0],b,f,g):
                summa += tri_vos(dva,korni2[0],b)
            else:
                summa += tri_vos(dva_revers,korni2[0],b)            
            break
        
        if i == 0:
            if higher(a,korni2[i],f,g):
                summa += tri_vos(dva,a,korni2[i])
            else:
                summa += tri_vos(dva_revers,a,korni2[i])
            
        if i == len(korni2)-1:
            if higher(korni2[i],b,f,g):
                summa += tri_vos(dva,korni2[i],b)
            else:
                summa += tri_vos(dva_revers,korni2[i],b)            
            break
        
        if higher(korni2[i],korni2[i+1],f,g):
            summa += tri_vos(dva,korni2[i],korni2[i+1])
        else:
            summa += tri_vos(dva_revers,korni2[i],korni2[i+1])            


    print('Площадь фигуры, ограниченной графиками функций \n'+
          'f(x) = sin(x) и g(x) = 1.5*cos(x) равна: {:9.7}'.format(summa))
                    


#Рисуем графики функций.
x1 = np.linspace(a,b,int(b-a)*100)
y1 = f(x1)
y2 = g(x1)
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.axis([a*1.3, b*2,-10,10])
plt.plot(x1,y1,label='$sin(x)$')
plt.plot(x1,y2,label='$1.5*cos(x)$')
plt.scatter(korni2[0],g(korni2[0]),edgecolor='red',label='$roots$')
if len(korni2)>1:
    for i in range(1,len(korni2)):
        plt.scatter(korni2[i],g(korni2[i]),edgecolor='red')

plt.legend(loc='upper right')
plt.show()
