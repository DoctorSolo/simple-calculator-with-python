class Calculator:

    # Variables
    historic    = {}
    result      = 0.0

    # The builder
    def __init__(self, value1:float, operator: bytes, value2:float):
        self.operador = operator
        self.value1 = value1
        self.value2 = value2
        self.result = self.calculate()
    

    # It's function will calculate the result
    def calculate(self):

        # Variables
        value1 = self.value1
        value2 = self.value2

        # Option receive a number for the operation
        # option = self.check()

        # it match going calcule the value
        match self.operador:
            case 1:
                self.result = (value1 + value2)
            case 2:
                self.result = (value1 - value2)
            case 3:
                self.result = (value1 * value2)
            case 4:
                self.result = (value1 / value2)
            case _:
                self.result = 0
        
        # after calculate do historic
        self.historic_met(self.result, self.operador)

        # Next operation
        # self.next_operation(self.result)
        
        #return
        return self.result


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
        # print(self.historic)
        return self.historic


    # This method will loop with an operation
    def next_operation(self, result):

        # Ask a question
        contin = input('Would you like continue [1]yes [any]no ? ')
        if contin == '1':

            # Second result
            second = float(input('Enter the second result: '))
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


    # This method convert a number in operation
    def convert_in_operation(self, option: int):
        match option:
            case 1:
                return '+'
            
            case 2:
                return '-'
            
            case 3:
                return '*'
            
            case _:
                return '-'
            