#Вычисление интеграла функции с заданной степенью точности

'''  
       Программа, интегрирующая заданную функцию на указанном интервале 
       двумя методами (метод Буля и метод правых прямоугольников), и выводящая        
       результаты интегрирования в виде таблицы. Позже определяется,    
       сколько шагов нужно для интегрирования функции наименее точным   
       методом с заданной точностью.
'''

#Функция для интегрирования
def func(x):
    y = x*x
    return y;

print('f(x)=x^2')

#Ввод данных
a = 0
b = 0
while a == b:
    a = float(input('Введите начальное значение функции: '))
    b = float(input('Введите конечное значение функции: '))
if a > b:
    a, b = b, a
    
#Первое и второе количество шагов
n1 = int(input('Введите значение n1: '))
n2 = int(input('Введите значение n2: '))


#Функции различных методов

#Метод 3/8
def m38(func,a,b,n):
  h=(b-a)/n
  s1=s2=0
  for i in range(1,n):
    if i%3!=0: s1=s1+func(a+i*h)
    else: s2=s2+func(a+i*h)
  res=3*h/8*(func(a)+func(b)+3*s1+2*s2)
  return res

#Метод середин
def serp(func,a,b,n):
    h=(b-a)/n
    a=a+h*0.5
    s=0
    for i in range(1,n+1):
       s=s+func(a+h*i)
    s=s*h
    return s

#Метод правых прямоугольников
def rpr(func,a,b,n):
   h=(b-a)/n
   res=0
   for i in range(1,n+1):
    res=res+func(a+h*i)
   res=res*h
   return res

#Метод левых прямоугольников
def lpl(func,a,b,n):
   h=(b-a)/n
   res=0
   for i in range(n):
    res=res+func(a+h*i)
   res=res*h
   return res

#Метод Буля
def Boole(func,a,b,n):
   h=(b-a)/n
   s=7*(func(a)+func(b))
   s1=s2=s3=0
   for i in range(1,n):
    if i%2==1: s1=s1+func(a+h*i)
    else:
        if i%4==0: s3=s3+func(a+h*i)
        else:
            s2=s2+func(a+h*i)
   s=s+32*s1+12*s2+14*s3
   res=s*h*4/90
   return res

#Метод Уэддля
def Weddle(func,a,b,n):
    h=(b-a)/n
    s1=s2=s3=s4=0
    for i in range(1,n):
     if i%3==0:
       if i%6==0: s4=s4+func(a+h*i)
       else: s3=s3+func(a+h*i)
     else: 
      if i%2==0: s2=s2+func(a+h*i)
      else:
       s1=s1+func(a+h*i)
     res=h/140*(41*(func(a)+func(b))+216*s1+27*s2+272*s3+82*s4)
     return res
    
#Метод трапеций
def trap(func,a,b,n):
     h=(b-a)/n
     s=0
     for i in range(1,n):
        s=s+func(a+h*i)
     res=h*((func(a)+func(b)/2+s))
     return res

#Метод параболы
def parabola(a, b, n):
    h = (b-a)/n
    s1 = 0
    for i in range(1,n):
        if i % 2 == 0:
            s1 += 4*func(a+h*i)
        else:
            s1 += 2*func(a+h*i)
    res = h/3*(func(a) + s1 + func(b))
    return res


#Вывод таблицы результатов
print('Таблица значений:')
print('       Метод      |  n1 ={0:6}'.format(n1),' |  n2 ={0:6}'.format(n2))
print('    Метод Буля   |', end = '')
print(' {0:11.7}  |'.format(Boole(func,a,b,n1)),'{0:11.7}'.format(Boole(func,a,b,n2)))
print('  Правые прямоугольники  |', end = '')
print(' {0:11.7}  |'.format(rpr(func,a,b,n1)),'{0:11.7}'.format(rpr(func,a,b,n2)))

#Дополнительный ввод для наименее точного метода
n = int(input('Введите первоначальное кол-во шагов (n): '))
eps = float(input('Введите точность (Eps): '))
#Вычисление шагов
while abs(rpr(func,a,b,n)) - abs(rpr(func,a,b,2*n)) > eps:
    n *= 2
#Вывод результата
print('\nЗначение интеграла: {0:7}'.format(rpr(func,a,b,n)))
print('Количество шагов, потребовавшихся для вычисления с точностью до',eps, 'методом правых:',n)






















