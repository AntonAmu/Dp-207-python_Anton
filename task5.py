import logging

logging.basicConfig(filename='task5.log', filemode='a', level=logging.INFO)

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

class TooManyHope(CustomException):
    pass

class NotValiData(CustomException):
    pass

class RepresentNumber():

    list_of_functionality = {}

    def __init__(self):
        for sub_cls in RepresentNumber.__subclasses__():
            sub_cls.add_list_of_functionality()
 
    @classmethod
    def add_language_repr(cls):
        RepresentNumber.list_of_functionality[cls._language] = {}
    
    @classmethod
    def add_list_of_functionality(cls):
        cls.add_language_repr()
        for sub_cls in cls.__subclasses__():
            sub_cls.update_list_of_functionality()
        return RepresentNumber.list_of_functionality[cls._language]
    

class RepresentNumberRu(RepresentNumber):

    _language = 'Rus'

    list_num_str_repr = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одинадцать', 'двенадцать',
        'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'сорок', 'девяносто']
    list_num = list(range(1, 21)) + [40, 90]
    
    list_num_str_repr += ['сто', 'двести', 'триста', 'четыриста']
    list_num += [100, 200, 300, 400]
    
    list_num_str_repr += ['одна', 'две', 'три', 'четыре']
    list_num += [1000, 2000, 3000, 4000]
     
    _numbers = dict(zip(list_num, list_num_str_repr))


class RepresentNumberEng(RepresentNumber):
    _language = 'Eng'
    

class Selector():
    
    def __init__(self, language = "Rus", basic_class_of_repr = RepresentNumber):
        
        self.language = language
        self.basic_class_of_repr = RepresentNumber


    @property
    def list_of_functionality(self):
        if self.basic_class_of_repr.list_of_functionality.get(self.language):
            return self.basic_class_of_repr.list_of_functionality.get(self.language)
        else:
            raise TooManyHope(f"I can't process language such {self.language}")
    
    def within_range(self, number):

        try:
            key = list(filter((lambda key: number in key), self.list_of_functionality))[0]
            return key
        except IndexError:
            raise TooManyHope(f"I can process only numbers from 1 to {max([key.stop for key in self.list_of_functionality])-1}")
    
    def get_proper_str(self, number):
        return self.list_of_functionality.get(self.within_range(number))

class Number():
    
    selector = Selector()

    def __init__(self, input):
        self.number = Number.validate_number(Number.parse_data(input)[1])
        self.sign = Number.parse_data(input)[0]

    @staticmethod
    def validate_number(parse_data):
        try:
            number = int(parse_data)
            return f"{number}"
        except ValueError():
            raise NotValiData("Not valid type")
    
    @staticmethod
    def parse_data(input):
        if input[0] == '-' or input[0] == '+':
            parse_data = input[1:]
            sign = input[0]
        else:
            sign = '+'
            parse_data = input
        return sign, parse_data
    
    @property
    def string_repr_of_abs_value(self):

        abs_value = int(self.number)
        return self.selector.get_proper_str(abs_value)(self.number)


    def __str__(self):
        if self.sign == '-':
            return 'минус ' + self.string_repr_of_abs_value
        else:
            return self.string_repr_of_abs_value


class RepresentNumberFrom_1_To_99(RepresentNumberRu):

    range_ = range(1, 100)    
    
    @classmethod
    def str(cls, number):

        dict_ = cls._numbers

        if len(number) <= 2 and dict_.get(int(number)):
            string= dict_.get(int(number))
        elif int(number) < 40:
            string = f'{dict_.get(int(number[0]))}дцать {dict_.get(int(number[1]))}'
        elif len(number) == 2 and int(number[0]) == 4:
            string = f'{dict_.get(40)} {dict_.get(int(number[1]))}'
        elif len(number) == 2 and int(number) > 49 and  int(number) < 89:
            string = f'{dict_.get(int(number[0]))}десят {dict_.get(int(number[1]))}'
        elif len(number) == 2 and int(number[0]) == 9:
            string = f'{dict_.get(90)} {dict_.get(int(number[1]))}'
        return string
    
    @classmethod
    def update_list_of_functionality(cls):
        RepresentNumber.list_of_functionality[cls._language][cls.range_] = cls.str
        for sub_cls in cls.__subclasses__():
            sub_cls.update_list_of_functionality()


class RepresentNumberFrom_100_To_999(RepresentNumberFrom_1_To_99):
    
    range_ = range(100, 1000)
    
    @classmethod
    def str(cls, number):
        dict_ = cls._numbers 


        if int(number) in dict_:
            string = f'{dict_.get(int(number))}'
        elif int(number) in range(100, 501):
            string = f"{RepresentNumberFrom_100_To_999.str(int(number) - int(number[1:]))} {RepresentNumberFrom_1_To_99.str(number[1:])}"
        elif int(number[:1]) == 0:
            string = f'{RepresentNumberFrom_1_To_99.str(number[2])}'
        else:
            string = f'{RepresentNumberFrom_1_To_99.str(number[0])}сот { RepresentNumberFrom_1_To_99.str(number[1:])}'
        return string

class RepresentNumberFrom_1000_To_9_999(RepresentNumberFrom_100_To_999):
    
    range_ = range(1000, 10_000)

    @classmethod
    def str(cls, number):

        dict_ = cls._numbers 
        if int(number) == 1000:
            string = f'{dict_.get(int(number))} тысяча'
        elif int(number) - int(number[1:]) == 1000:
            string = f"{RepresentNumberFrom_1000_To_9_999.str(int(number) - int(number[1:]))} {RepresentNumberFrom_100_To_999.str(number[1:])}"
        elif int(number) - int(number[1:]) in dict_:    
            string = f"{RepresentNumberFrom_1000_To_9_999.str(int(number) - int(number[1:]))} тысячи {RepresentNumberFrom_100_To_999.str(number[1:])}"
        else:
            string= f"{RepresentNumberFrom_1_To_99.str(number[1])} тысячь " + RepresentNumberFrom_100_To_999.str(number[1:])
        return string

class RepresentNumberFrom_10_000_To_99_999(RepresentNumberFrom_1000_To_9_999):

    range_ = range(10_000, 100_000)
    
    @classmethod
    def str(cls, number):

        string = f"{RepresentNumberFrom_1_To_99.str(number[:-3]).split()[0]} {RepresentNumberFrom_1000_To_9_999.str(number[-4:])} " 

        return string
    
class RepresentNumberFrom_100_000_To_999_999(RepresentNumberFrom_10_000_To_99_999):
    
    range_ = range(100_000, 1_000_000)

    @classmethod
    def str(cls, number):

        string = f"{RepresentNumberFrom_100_To_999.str(number[:-3]).split()[0]} {RepresentNumberFrom_10_000_To_99_999.str(number[1:])} " 

        return string
        
def main():

    RepresentNumber()
    edit_lang = ["Eng", "Fr", "Rus"]
    for lang in edit_lang:
        Number.selector = Selector(lang)
        try:
            print(Number('-22'))
            print(Number('2'))
            print(Number('33'))
            print(Number('44'))
            print(Number('66'))
            print(Number('106'))
            print(Number('222'))
            print(Number('242'))
            print(Number('401'))
            print(Number('99101'))
            print(Number('441101'))
            print(Number('9999999'))
        except (TooManyHope, NotValiData) as e:
            logging.error(e.msg)

if __name__ == "__main__":
    main()