import sys 

class Adder:
    
    @staticmethod
    def start_message():
        print('Welcome to the command line adder.')
        print('Please enter a command similar to: python ishraqkhan-module.py arg1 arg2 ... argX')
        print('where arg1 is either \'int\' or \'float\' and all arguments after are ints or float that you want to add')
        print('The program will return the sum of your arguments.')
        print('')
        
    # data_type should be float or int only
    @staticmethod
    def add(data_type, args):
        running_sum = 0
        if data_type == 'int':
            data_type = int
        elif data_type == 'float':
            data_type = float
          
        # add all command line arguments to running sum as floats
        for i in args:
            running_sum += data_type(i)
        return running_sum    
    
if __name__ == '__main__':
    adder = Adder()
    adder.start_message()
    if len(sys.argv) > 1:
        adder_sum = adder.add(sys.argv[1], sys.argv[2:])
        print(f"The sum of {sys.argv[2:]} as {sys.argv[1]} is {adder_sum}")