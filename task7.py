
class Main():
    def __init__(self, number):
        self.number = number
        
    def get_range_of_natural_numbers(self):
        return str(list((n for n in range(1, self.number) if n < self.number**0.5)))[1:-1]
    
if __name__ == '__main__':
    cl= Main(100)
    print(cl.get_range_of_natural_numbers())