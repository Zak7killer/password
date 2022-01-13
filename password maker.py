import random

ALPHABET = [chr(i) for i in range(65, 91)]
alphabet = [i.lower() for i in ALPHABET]
num = [str(i) for i in range(0, 10)]
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '/', '-', ';', ']', '[', '.', ',']

print('hello today we will help you to make a strong ass password :)\n')
n = input('how long your password should be : ')

while True:
    try:
        n = int(n)

        if n < 6:
            print('\nyour password need to be at least 6 characters long')
            n = int(input('please try again : '))
        else:
            break
    except:
        print('you need to insert numbers only')
        n = input('please try again : ')

code = []
for i in range(round(n * (30 / 100))):
    code.append(random.choice(alphabet))
    code.append(random.choice(ALPHABET))
for j in range(round(n * (20 / 100))):
    code.append(random.choice(num))
    code.append(random.choice(symbol))
print(code)
print(len(code))

print('\nhere is your strong ass password is :', ''.join([i for i in code]))