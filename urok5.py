numbers = [i for i in range(1, 11)]
chotnie = [num for num in numbers if num % 2 ==0]
nechotnie = [num for num in numbers if num %2 !=0]
print(chotnie, nechotnie)

my_list = [i for i in range (1, 11, 2)]
print(my_list)
print('/')

names = ['pavel', 'sasha', 'jordan', 'pasha']
answer = [name[0] for name in names]
print(answer)
print('/')

nums=[1, 2, 3]
my_lis= [i for i in range(1, 11)if i in nums]
print(my_lis)