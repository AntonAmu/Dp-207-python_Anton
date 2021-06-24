import math

class NotExistException(Exception):
    def __init__(self, msg):
        self.msg = msg


class Range():

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
    
    def get_fibbonachi_range(self):
        return FibbonachiRange(self.begin, self.end).find_proper_fibbonachi_range()


class FibbonachiRange():

    def __init__(self, begin, end):
        self.range_begin = begin
        self.range_end = end
        self.range_ = (self.range_begin > 0, self.range_end > 0)
    
    @staticmethod
    def find_index_through_value(value): 
        
        index = math.log10(value*(5**0.5))/math.log10((1+5**0.5)/2)
        if index - round(index) > 0:
            return round(index) + 1 
        else:
            return round(index) 
        

    def find_proper_fibbonachi_range(self):
        for sub_class in self.__class__.__subclasses__():
            if sub_class.range_ == self.range_:
                return sub_class.generate_fibbonachi_range(self.range_begin, self.range_end)


class NegativeStartPositiveEndRange(FibbonachiRange):
    start = False
    end = True
    range_ = (start, end)
    
    @classmethod
    def generate_fibbonachi_range(cls, range_begin, range_end):
        index_begin = 0
        index_end = cls.find_index_through_value(range_end)
        return (round((((1+5**.5)/2)**i)/(5**0.5)) for i in range(index_begin, index_end))


class PositiveStartPositiveEndRange(FibbonachiRange):
    start = True
    end = True
    range_ = (start, end)
    
    @classmethod
    def generate_fibbonachi_range(cls, range_begin, range_end):
        index_begin = cls.find_index_through_value(range_begin)
        index_end = cls.find_index_through_value(range_end)
        return (round((((1+5**.5)/2)**i)/(5**0.5)) for i in range(index_begin, index_end))

class NegativeStartNegativeEndRange(FibbonachiRange):
    start = False
    end = False
    range_ = (start, end)
    
    @staticmethod
    def generate_fibbonachi_range(range_begin, range_end):
        raise NotExistException("There are no digits for such range")

def main():
    for r in Range(-100, 500), Range(0, 23), Range(142, 234), Range(-150, -100):
        print(list(r.get_fibbonachi_range()))



if __name__ == "__main__":
    try:
        main()
    except NotExistException as e:
        print(e.msg)