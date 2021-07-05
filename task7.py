import math

class Main():
    """
    Class Main
    """
    def __init__(self, number):
        self.number = number
        
    def get_range_of_natural_numbers(self):
        """
        Return range of natural digits that is less than appropriate number squares 
        """
        return str(list((n for n in range(1, math.ceil(self.number**0.5)))))[1:-1]
    
if __name__ == '__main__':
    cl= Main(10)
    print(cl.get_range_of_natural_numbers())