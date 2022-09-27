num = 1
cube = num ** 3
while cube <= 1000:
    print(str(num) + ' cubed is ' + str(cube))
    num += 1
    cube = num ** 3



num = 2
while num < 100:
    for i in range(2,num):
        if num % i == 0:
            break
        elif i == (num - 1):
            print(num)
    num += 1



age = input('What is your age? ')
if int(age) < 18:
    print(f'At the age of {str(age)} are a kid.')
elif int(age) <= 65:
    print(f'At the age of {str(age)} are an adult.')
else:
    print(f'At the age of {str(age)} are a senior.')