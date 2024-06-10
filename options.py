class Calculator:

    def __init__(self, value1:float, value2:float):
        self.value1 = value1
        self.value2 = value2
        return self.calculate()

    # It's will chacking the option, so user don't try anything incorrect.
    def check(self):

        while True:
            try:
                # Here the console going send a mensage to user
                print('1: to add')
                print('2: to subtract')
                print('3: to multiply')
                print('4: to shared')
                operation = int(input('Enter a number: '))
                return operation
            
            except ValueError:
                print('Error... Please enter an number: ')
    

    # It's function will calculate the result
    def calculate(self):
        value1 = self.value1
        value2 = self.value2

        option = self.check()
        # it match going calcule the value
        match option:
            case 1:
                return value1 + value2
            case 2:
                return value1 - value2
            case 3:
                return value1 * value2
            case 4:
                return value1 / value2
            case _:
                return 0
