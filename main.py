import os, getpass, time

def calculator():
    global answer
    os.system('cls')
    print('Please Select The First Number')
    try:
        no1 = float(input('> '))
    except FloatingPointError:
        print('Please select a NUMBER')
    if isinstance(no1, float):
        no1 = int(no1)
        print('Please Select the function (* / + -)')
        function = input('> ')
        while function not in ['*', '/', '+', '-']:
            print('Please select a valid function.')
            print('Please Select the function (* / + -)')
            function = input('> ')
        print('Please select a final number.')
        no2 = float(input('> '))
        if type(no2) is float:
            no2 = int(no2)
            if function == '*':
                answer = no1 * no2
                print(f'Calculated Answer: {answer:,}')
                redo = input('Would you like to restart the program? [Y/N]')
                while redo not in ['y', 'n']:
                    print('Please select either yes or no')
                    redo = input('Would you like to restart the program? [Y/N]')
                if redo == 'y':
                    restart()
                if redo == 'n':
                    exit()
            if function == '/':
                try:
                    answer = no1 / no2
                    print(f'Calculated Answer: {answer:,}')
                    redo = input('Would you like to restart the program? [Y/N]')
                    while redo not in ['y', 'n']:
                        print('Please select either yes or no')
                        redo = input('Would you like to restart the program? [Y/N]')
                    if redo == 'y':
                        restart()
                    if redo == 'n':
                        exit()
                except ZeroDivisionError:
                    print('You cannot divide by zero')
                    getpass.getpass(prompt='Press enter to restart the program ')
                    restart()
            if function == '+':
                answer = no1 + no2
                print(f"Calculated Answer: {answer:,}")
                redo = input('Would you like to restart the program? [Y/N]')
                while redo not in ['y', 'n']:
                    print('Please select either yes or no')
                    redo = input('Would you like to restart the program? [Y/N]')
                if redo == 'y':
                    restart()
                if redo == 'n':
                    exit()
            if function == '-':
                answer = no1 - no2
                print(f'Calculated Answer: {answer:,}')
                redo = input('Would you like to restart the program? [Y/N]')
                while redo not in ['y', 'n']:
                    print('Please select either yes or no')
                    redo = input('Would you like to restart the program? [Y/N]')
                if redo == 'y':
                    restart()
                if redo == 'n':
                    exit()
        else:
            print('Please Ensure you select a number')
            getpass.getpass(prompt='Press enter to restart the program ')
            restart()
    else:
        print('Please Ensure you select a number')
        getpass.getpass(prompt='Press enter to restart the program ')
        restart()

def menu():
    os.system('cls')
    print('Calculator App')
    print('Simply Enter a number followed by the function.')
    print('Eg. "1" | "x" | "1"')
    secret = getpass.getpass(prompt='Press Enter to continue ')
    if secret == 'stats':
        print('96 Lines of code')
        print('23 Minustes coding time')
        print('7 Crashes')
        print('3 Moduel Imports')
        getpass.getpass(prompt='Enter to continue to the program ')
    calculator()

def restart():
    calculator()

if __name__ == "__main__":
    menu()