import math
#Формула Бине

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg


class NotExistException(CustomException):
    pass

class NotPositiveRange(CustomException):
    pass

class PositiveRange():

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.check_if_positiv()
    
    def get_fibbonachi_range(self):
        return FibbonachiRange(self.begin, self.end).find_proper_fibbonachi_range()

    def check_if_positiv(self):
        if self.end <= self.begin:
            raise NotPositiveRange("Not positive range")


class FibbonachiRange():

    def __init__(self, begin, end):
        self.range_begin = begin
        self.range_end = end
    
    @staticmethod
    def find_index_through_value(value):
        if value <= 0:
            return 0
        else: 
            index = math.log10(value*(5**0.5))/math.log10((1+5**0.5)/2)
            if index - round(index) > 0:
                return round(index) + 1 
            else:
                return round(index) 
        

    def find_proper_fibbonachi_range(self):
        index_begin = self.__class__.find_index_through_value(self.range_begin)
        index_end = self.__class__.find_index_through_value(self.range_end)
        if index_begin == 0 and index_end == 0:
            raise NotExistException("There are no digits for such range")
        else:
            return self.__class__.fibbonachi_range(index_begin, index_end)
    
    @staticmethod
    def fibbonachi_range(index_begin, index_end):
        return (round((((1+5**.5)/2)**i)/(5**0.5)) for i in range(index_begin, index_end))


def main():
    try:
        for r in PositiveRange(-100, 500), PositiveRange(22, 30), PositiveRange(1, 100), PositiveRange(-150, -100):
            try:
                print(list(r.get_fibbonachi_range()))
                #print(list(r.get_fibbonachi_range())[-1])
            except CustomException as e:
                print(e.msg)
                continue
    except CustomException as e:
            print(e.msg)
    except IndexError:
        pass


if __name__ == "__main__":

    main()

        