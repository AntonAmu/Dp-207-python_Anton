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
    """
    Class RepresentNumber which collects all available languages and representation's numbers's ranges 
    """
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
    
    list_num_str_repr += ['сто', 'двести', 'триста', 'четыреста']
    list_num += [100, 200, 300, 400]
    
    list_num_str_repr += ['одна', 'две', 'три', 'четыре']
    list_num += [1000, 2000, 3000, 4000]
     
    _numbers = dict(zip(list_num, list_num_str_repr))


class RepresentNumberEng(RepresentNumber):
    _language = 'Eng'
    

class Selector():
    """
    Class Selector whitch takes takes two arguments: language (by default 'Rus') and
    basic class of representation (by default RepresentNumber)
    """    
    def __init__(self, language = "Rus", basic_class_of_repr = RepresentNumber):
        
        self.language = language
        self.basic_class_of_repr = RepresentNumber


    @property
    def list_of_functionality(self):
        """
        Choses all available functionality for appropriate language
        """   
        if self.basic_class_of_repr.list_of_functionality.get(self.language):
            return self.basic_class_of_repr.list_of_functionality.get(self.language)
        else:
            raise TooManyHope(f"I can't process language such {self.language}")
    
    def within_range(self, number):
        """
        Checks if appropriate functionality exists for the given number
        """   
        try:
            key = list(filter((lambda key: number in key), self.list_of_functionality))[0]
            return key
        except IndexError:
            raise TooManyHope(f"I can process only numbers from 1 to {max([key.stop for key in self.list_of_functionality])-1}")
    
    def get_proper_str(self, number):
        """
        Rerurns function for number's representation 
        """
        return self.list_of_functionality.get(self.within_range(number))

class Number():
    """
    Class Number 
    """  
    selector = Selector()

    def __init__(self, number):
        self.abs_number = Number.validate_number(Number.parse_data(number)[1])
        self.sign = Number.parse_data(number)[0]

    @staticmethod
    def validate_number(parse_data):
        """
        Checks if the value is integers else raises NotValiData exception
        """
        try:
            number = int(parse_data)
            return f"{number}"
        except ValueError:
            raise NotValiData("Not valid type")
    
    @staticmethod
    def parse_data(number):
        """
        Parses number from the calling the class constructor
        """
        if number[0] == '-' or number[0] == '+':
            parse_data = number[1:]
            sign = number[0]
        else:
            sign = '+'
            parse_data = number
        return sign, parse_data
    
    @property
    def string_repr_of_abs_value(self):
        """
        Returns appropriate string representation of number's absolute value
        """
        int_abs_value = int(self.abs_number)
        return self.selector.get_proper_str(int_abs_value)(self.abs_number).strip()


    def __str__(self):
        """
        Returns appropriate string representation of number
        """
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
        elif number == '00':
            string = ''
        elif int(number) < 40 and number[1] == '0':
            string = f'{dict_.get(int(number[0]))}дцать'
        elif int(number) < 40 and number[1] != '0':
            string = f'{dict_.get(int(number[0]))}дцать {dict_.get(int(number[1]))}'
        elif len(number) == 2 and int(number[0]) == 4:
            string = f'{dict_.get(40)} {dict_.get(int(number[1]))}'
        elif int(number) > 49 and  int(number) < 89 and int(number[1]) == 0:
            string = f'{dict_.get(int(number[0]))}десят'
        elif len(number) == 2 and int(number[0]) == 9:
            string = f'{dict_.get(90)} {dict_.get(int(number[1]))}'
        elif int(number) == 90:
            string = f'{dict_.get(90)}'
        else:
            string = f'{dict_.get(int(number[0]))}десят {dict_.get(int(number[1]))}'
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
        elif len(number) == 3 and int(number) == 0:
            string = ''
        elif int(number) in range(100, 500):
            string = f"{RepresentNumberFrom_100_To_999.str(str(int(number) - int(number[1:])))} {RepresentNumberFrom_1_To_99.str(number[1:])}"
        elif int(number[:1]) == 0:
            string = f'{RepresentNumberFrom_1_To_99.str(number[1:])}'
        else:
            string = f'{RepresentNumberFrom_1_To_99.str(number[0])}сот {RepresentNumberFrom_1_To_99.str(number[1:])}'
        return string

class RepresentNumberFrom_1000_To_9_999(RepresentNumberFrom_100_To_999):
    
    range_ = range(1000, 10_000)

    @classmethod
    def str(cls, number):

        dict_ = cls._numbers
        if  number[0] == '0':
            string= f"тысячь {RepresentNumberFrom_100_To_999.str(number[1:])}"
        elif int(number) == 1000:
            string = f'{dict_.get(int(number))} тысяча'
        elif int(number) - int(number[1:]) == 1000:
            string = f"{RepresentNumberFrom_1000_To_9_999.str(str(int(number) - int(number[1:])))} {RepresentNumberFrom_100_To_999.str(number[1:])}"
        elif int(number) - int(number[1:]) in dict_:    
            string = f"{dict_.get(int(number) - int(number[1:]))} тысячи {RepresentNumberFrom_100_To_999.str(number[1:])}"
        else:
            string= f"{RepresentNumberFrom_1_To_99.str(number[:1])} тысячь {RepresentNumberFrom_100_To_999.str(number[1:])}" 
        return string

class RepresentNumberFrom_10_000_To_99_999(RepresentNumberFrom_1000_To_9_999):

    range_ = range(10_000, 100_000)
    
    @classmethod
    def str(cls, number):
        if number[0] == '0':
            string = f"{RepresentNumberFrom_1000_To_9_999.str(number[1:])}"
        elif int(number[:2]) in range(11,20) or number[1] == '0':
            string = f"{RepresentNumberFrom_1_To_99.str(number[:-3]).split()[0]} тысячь {RepresentNumberFrom_100_To_999.str(number[-3:])}"
        else:
            string = f"{RepresentNumberFrom_1_To_99.str(number[:-3]).split()[0]} {RepresentNumberFrom_1000_To_9_999.str(number[-4:])}" 
     
        return string
    
class RepresentNumberFrom_100_000_To_999_999(RepresentNumberFrom_10_000_To_99_999):
    
    range_ = range(100_000, 1_000_000)

    @classmethod
    def str(cls, number):
        string = f"{RepresentNumberFrom_100_To_999.str(number[:-3]).split()[0]} {RepresentNumberFrom_10_000_To_99_999.str(number[1:])}" 
        return string
        
def main():

    RepresentNumber()
    print(RepresentNumber.list_of_functionality)
    edit_lang = ["Eng", "Fr", "Rus"]
    for lang in edit_lang:
        Number.selector = Selector(lang)
        try:
            # print(Number('-22'))
            # print(Number('2'))
            # print(Number('33'))
            # print(Number('44'))
            # print(Number('66'))
            # print(Number('106'))
            # print(Number('222'))
            # print(Number('242'))
            # print(Number('401'))
            print(Number('333333'))
            print(Number('551001'))
            print(Number('45310'))
        except (CustomException) as e:
            logging.error(e.msg)

if __name__ == "__main__":
    main()