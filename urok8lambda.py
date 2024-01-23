x= lambda e: e
print(x(9))

a = lambda a: a**2
print(a(4))

x= [1, 2, 3, '4']
a= map(lambda d:d*2,x)
print(list(a))

x= [1, 2, 3, '4']
a= filter(lambda d:d*2==4,x)
print(list(a))

i= [1, 2, 3, 4, 5, 6]
a = list(filter(lambda x: x%2==0,i))
print(a)

i = ['jordan', 'pavel', 'jacky']
a=list(filter(lambda x:'j' in x, i))
print(a)

x = [1, 2, -4, -4, -8, -7, 4, 15]
y = list(filter(lambda x: x>0, x))
print(y)

a = 3.613331213
print(round(a, 3))


alpha = lambda x, y: x + y
chislo1 = int(input('1-Введите первое число: '))
chislo2 = int(input('2-Введите второе число: '))
beta = alpha(chislo1, chislo2)
print(beta)
