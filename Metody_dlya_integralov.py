#���������� ��������� ������� � �������� �������� ��������

'''  
       ���������, ������������� �������� ������� �� ��������� ��������� 
       ����� �������� (����� ���� � ����� ������ ���������������), � ���������        
       ���������� �������������� � ���� �������. ����� ������������,    
       ������� ����� ����� ��� �������������� ������� �������� ������   
       ������� � �������� ���������.
'''

#������� ��� ��������������
def func(x):
    y = x*x
    return y;

print('f(x)=x^2')

#���� ������
a = 0
b = 0
while a == b:
    a = float(input('������� ��������� �������� �������: '))
    b = float(input('������� �������� �������� �������: '))
if a > b:
    a, b = b, a
    
#������ � ������ ���������� �����
n1 = int(input('������� �������� n1: '))
n2 = int(input('������� �������� n2: '))


#������� ��������� �������

#����� 3/8
def m38(func,a,b,n):
  h=(b-a)/n
  s1=s2=0
  for i in range(1,n):
    if i%3!=0: s1=s1+func(a+i*h)
    else: s2=s2+func(a+i*h)
  res=3*h/8*(func(a)+func(b)+3*s1+2*s2)
  return res

#����� �������
def serp(func,a,b,n):
    h=(b-a)/n
    a=a+h*0.5
    s=0
    for i in range(1,n+1):
       s=s+func(a+h*i)
    s=s*h
    return s

#����� ������ ���������������
def rpr(func,a,b,n):
   h=(b-a)/n
   res=0
   for i in range(1,n+1):
    res=res+func(a+h*i)
   res=res*h
   return res

#����� ����� ���������������
def lpl(func,a,b,n):
   h=(b-a)/n
   res=0
   for i in range(n):
    res=res+func(a+h*i)
   res=res*h
   return res

#����� ����
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

#����� ������
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
    
#����� ��������
def trap(func,a,b,n):
     h=(b-a)/n
     s=0
     for i in range(1,n):
        s=s+func(a+h*i)
     res=h*((func(a)+func(b)/2+s))
     return res

#����� ��������
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


#����� ������� �����������
print('������� ��������:')
print('       �����      |  n1 ={0:6}'.format(n1),' |  n2 ={0:6}'.format(n2))
print('    ����� ����   |', end = '')
print(' {0:11.7}  |'.format(Boole(func,a,b,n1)),'{0:11.7}'.format(Boole(func,a,b,n2)))
print('  ������ ��������������  |', end = '')
print(' {0:11.7}  |'.format(rpr(func,a,b,n1)),'{0:11.7}'.format(rpr(func,a,b,n2)))

#�������������� ���� ��� �������� ������� ������
n = int(input('������� �������������� ���-�� ����� (n): '))
eps = float(input('������� �������� (Eps): '))
#���������� �����
while abs(rpr(func,a,b,n)) - abs(rpr(func,a,b,2*n)) > eps:
    n *= 2
#����� ����������
print('\n�������� ���������: {0:7}'.format(rpr(func,a,b,n)))
print('���������� �����, ��������������� ��� ���������� � ��������� ��',eps, '������� ������:',n)






















