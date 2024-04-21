


def calculadora():

    print(''' BEM VINDO A CALCULADORA SIMPLES!''')

    operation = input('''
    Por favor escolha qual o tipo de operação será feita
    + para adição
    - para subtração
    * para multiplicação
    / para divisão
 ''')


    numero_1 = int(input('Coloque um número:'))
    numero_2 = int(input('Coloque outro número:'))


    if operation == '+':
        print('{} + {} ='.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operation == '-':
        print('{} - {} ='.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    elif operation == '*':
        print('{} * {}='.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operation == '/':
        print('{} / {}='.format(numero_1, numero_2))
        print(numero_1 / numero_2)

    else :
        print('Operrador não definido, reinicie o programa')
    again()

def again():
    again_input = input(''' 
    Se você deseja usar novamente a calculadora simples, digite "Y", se não, "N".
    ''')
    
    if again_input.upper() == 'Y':
        calculadora()

    elif again_input.upper() == 'N':
        print('Adeus')

    else:
        again()

calculadora()

