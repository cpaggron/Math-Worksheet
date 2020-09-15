import random
m = open('../desktop/mathworksheet.txt', 'w')
typster = str(input('Do you want multiplication, addition, subtraction, division, or exponent?\n'))
# Addition
if typster == 'addition':
    choice = int(input('Do you want to 1. answer questions digitally or 2. Make a worksheet? (Type your choice as a number\n'))
    if choice == 1:
        correct = 0
        q = int(input('How many questions do you want?\n'))
        qo = q
        while q != 0:
            num1 = random.randint(0, 500)
            num2 = random.randint(0, 500)
            answer1 = num1 + num2
            answer = int(input(f'{num1}+{num2}='))
            if answer1 == answer:
                print('Correct!')
                correct = correct + 1
            else:
                print('Incorrect.')
                print(answer1)
            q = q - 1
        print(f'You got {correct}/{qo}')
    elif choice == 2:
        q = int(input('How many questions do you want?\n'))
        while q != 0:
            num1 = random.randint(1, 500)
            num2 = random.randint(0, 9)
            m.write(f'{num1}+{num2}=\n')
            q = q - 1
        m = open('../desktop/mathworksheet.txt')
        content = m.read()
        m.close()
# Division
elif typster == 'division':
    choice = int(input('Do you want to 1. answer questions digitally or 2. Make a worksheet? (Type your choice as a number\n'))
    if choice == 1:
        correct = 0
        q = int(input('How many questions do you want?\n'))
        qo = q
        while q != 0:
            num1 = random.randint(1, 500)
            num2 = random.randint(0, 9)
            answer1 = num1 * num2
            answer = str(input(f'{num1}/{num2}='))
            if answer1 == answer:
                print('Correct!')
                correct = correct + 1
            else:
                print('Incorrect.')
                print(answer1)
            q = q - 1
        print(f'You got {correct}/{qo}')
    elif choice == 2:
        q = int(input('How many questions do you want?\n'))
        while q != 0:
            num1 = random.randint(1, 500)
            num2 = random.randint(0, 9)
            m.write(f'{num1}/{num2}=\n')
            q = q - 1
        m = open('../desktop/mathworksheet.txt')
        content = m.read()
        m.close()
# Subtraction
elif typster == 'subtraction':
    choice = int(input('Do you want to 1. answer questions digitally or 2. Make a worksheet? (Type your choice as a number\n'))
    if choice == 1:
        correct = 0
        q = int(input('How many questions do you want?\n'))
        qo = q
        while q != 0:
            num1 = random.randint(0, 500)
            num2 = random.randint(0, 500)
            answer1 = num1 - num2
            answer = int(input(f'{num1}-{num2}='))
            if answer1 == answer:
                print('Correct!')
                correct = correct + 1
            else:
                print('Incorrect.')
                print(answer1)
            q = q - 1
        print(f'You got {correct}/{qo}')
    elif choice == 2:
        q = int(input('How many questions do you want?\n'))
        while q != 0:
            num1 = random.randint(0, 500)
            num2 = random.randint(0, 500)
            m.write(f'{num1}-{num2}=\n')
            q = q - 1
        m = open('../desktop/mathworksheet.txt')
        content = m.read()
        m.close()
# Power
elif typster == 'exponent':
    choice = int(input('Do you want to 1. answer questions digitally or 2. Make a worksheet? (Type your choice as a number\n'))
    if choice == 1:
        correct = 0
        q = int(input('How many questions do you want?\n'))
        qo = q
        while q != 0:
            num1 = random.randint(1, 500)
            num = [0, 1, 2, 3, 5, 10, 100, 1000]
            num2 = random.choice(num)
            answer1 = num1 ** num2
            answer = int(input(f'{num1}^{num2}='))
            if answer1 == answer:
                print('Correct!')
                correct = correct + 1
            else:
                print('Incorrect.')
                print(answer1)
            q = q - 1
        print(f'You got {correct}/{qo}')
    elif choice == 2:
        q = int(input('How many questions do you want?\n'))
        while q != 0:
            num1 = random.randint(1, 500)
            num = [0, 1, 2, 3, 5, 10, 100, 1000]
            num2 = random.choice(num)
            m.write(f'{num1}^{num2}=\n')
            q = q - 1
        m = open('../desktop/mathworksheet.txt')
        content = m.read()
        m.close()
else:
    choice = int(input('Do you want to 1. answer questions digitally or 2. Make a worksheet? (Type your choice as a number\n'))
    if choice == 1:
        correct = 0
        q = int(input('How many questions do you want?\n'))
        qo = q
        while q != 0:
            num1 = random.randint(1, 500)
            num2 = random.randint(0, 9)
            answer1 = num1 * num2
            answer = str(input(f'{num1}*{num2}='))
            if answer1 == answer:
                print('Correct!')
                correct = correct + 1
            else:
                print('Incorrect.')
                print(answer1)
            q = q - 1
        print(f'You got {correct}/{qo}')
    elif choice == 2:
        q = int(input('How many questions do you want?\n'))
        while q != 0:
            num1 = random.randint(1, 500)
            num2 = random.randint(0, 9)
            m.write(f'{num1}*{num2}=\n')
            q = q - 1
        m = open('../desktop/mathworksheet.txt')
        content = m.read()
        m.close()
    
