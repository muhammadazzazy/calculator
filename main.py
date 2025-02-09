import os
from sys import exit


def main() -> None:
    greeting = """Welcome to the 🖩 App!

The following operations are supported:
\t[] ()\t parentheses
\t** ^ \t exponentiation
\t* × \t multiplication
\t/ ÷\t floating-point division
\t//\t floor division
\t%\t modulus percentage
\t+\t addition
\t-\t subtraction
"""
    print(greeting)
    while True:
        try:
            user_input = input('Enter a mathematical expression: ')
            if user_input == 'exit':
                print('Thanks for trying my program!')
                exit()

            user_input = user_input.replace('^', '**')
            user_input = user_input.replace('×', '*')
            user_input = user_input.replace('÷', '/')
            user_input = user_input.replace('[', '(')
            user_input = user_input.replace(']', ')')
            if user_input[-1] == '%':
                user_input = user_input.replace('%', '/100')

            if user_input == 'C':
                os.system('clear')

            if user_input[-1] == '=':
                output = eval(user_input[:-1])
            else:
                output = eval(user_input)
            print(output)

        except NameError:
            print('Mathematical expression contains letters...')
            continue
        except SyntaxError:
            print('Mathematical expression contains invalid symbols...')
            continue
        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()
