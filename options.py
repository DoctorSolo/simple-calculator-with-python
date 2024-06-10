class Calculator:

    # Variables
    historic = {}


    def __init__(self, value1:float, value2:float):
        self.value1 = value1
        self.value2 = value2
    

    # The historic
    def historic_met(self, result: float):
        historic_temp = {
            'Value1': self.value1,
            'Value2': self.value2,
            'Result': result
        }
        self.historic.update(historic_temp)
        print (self.historic)

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
            # Case the user enter a error type, the console send a mensage
            except ValueError:
                print('Error... Please enter a number: ')
    

    # It's function will calculate the result
    def calculate(self):

        # Variables
        value1 = self.value1
        value2 = self.value2

        # Option receive a number for the operation
        option = self.check()

        # it match going calcule the value
        match option:
            case 1:
                result = value1 + value2
            case 2:
                result = value1 - value2
            case 3:
                result = value1 * value2
            case 4:
                result = value1 / value2
            case _:
                result = 0
        
        # after calculate do historic and return
        self.historic(result)
        return result
