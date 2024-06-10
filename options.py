class Calculator:

    # Variables
    historic = {}

    # The builder
    def __init__(self, value1:float, value2:float):
        self.value1 = value1
        self.value2 = value2
        self.calculate()
    

    # This method convert a number in operation
    def convert_in_operation(option: int):
        match option:
            case 1:
                return '+'
            
            case 2:
                return '-'
            
            case 2:
                return '*'
            
            case _:
                return '-'


    # The historic
    def historic_met(self, result: float, option: int):

        # this variable create a temporary libraly
        historic_temp = {
            'Value1'    : self.value1,
            'Operation' : self.convert_in_operation(option),
            'Value2'    : self.value2,
            'Result'    : result
        }
        # So this makes an update
        self.historic.update(historic_temp)
        print (self.historic)

        return self.historic


    # This method will loop with an operation
    def next_operation(self, result):

        # Ask a question
        contin = input('Would you like continue [1]yes [any]no ? ')
        if contin == '1':

            # Second result
            second = float(int('Enter the second result: '))
            Calculator(result,second)
        pass


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
                result = (value1 + value2)
            case 2:
                result = (value1 - value2)
            case 3:
                result = (value1 * value2)
            case 4:
                result = (value1 / value2)
            case _:
                result = 0
        
        # after calculate do historic and return
        self.historic(result, option)

        # Next operation
        self.next_operation(result)

        return result
