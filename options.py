class Operation:

    # It's will chacking the option, so user don't try anything incorrect.
    def check():

        try:

            # Here the console going send a mensage to user
            operation = int(input('Enter a number: '))
            print('1: to add')
            print('2: to subtract')
            print('3: to multiply')
            print('4: to shared')

        except ValueError:
            while ValueError:
                operation = int(input('Error... Please enter an number: '))
        
        else:
            return operation
        
        return -1
    

    # It's function will calculate the result
    def operation(value1, value2):
        option = int(check())
        # it match going calcule the value
        match option:
            case 1:
                return value1 + value2
        return 0


    def __init__(self, value1, value2):
        operation(value1, value2)
