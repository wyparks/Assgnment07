while True:
    try:
        print('trying to open new file')
        new_file = open('new_file.txt','r')

    except FileNotFoundError:
        print("Tried to read a file that did not exist")
        new_file = open('new_file.txt','w')
        print('opened a new file in write mode, that can now be read from')
        new_file.close()
        continue
    else:
        print('this will only print if there are no exceptions')
    finally:
        print('this will print regardless of exceptions')

    break
    #Raising a custom exception
x = 10
if x > 5:
    raise Exception(f'A custom exception was raised. x should not exceed 5. The value of x was {x}')





