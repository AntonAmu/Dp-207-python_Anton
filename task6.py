from functools import reduce
import json
from pathlib import Path

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

class CanNotFindApproachException(CustomException):
    pass

class NotValidTicket(CustomException):
    pass

def factorial (num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*factorial(num-1)

def some_math(num_1, num_2):
    f = factorial
    return f(num_1)/(f(num_2)*f(num_1 - num_2))


class Approach():
    
    @classmethod
    @property
    def list_of_approach(cls):
        return dict(zip([sub_class.title for sub_class in cls.__subclasses__()],[sub_class for sub_class in cls.__subclasses__()]))

    @staticmethod
    def sum_(str):
        sum_ = reduce((lambda total, char: total + int(char)), list(str), 0)
        return sum_

    @classmethod
    def is_lucky_number(cls, str):     
        
        str_1, str_2 = cls.creat_parts_of_comparison(str)

        if cls.sum_(str_1) == cls.sum_(str_2):

            return True
        else:
            return False
    
    @staticmethod
    def creat_parts_of_comparison(str):
        pass


class MoskowApproach(Approach):

    title = 'Moskow'
    
    @staticmethod
    def creat_parts_of_comparison(str):         
        str_1 = str[:3]
        str_2 = str[3:]
        return str_1, str_2

class PiterApproach(Approach):

    title = 'Piter'

    @staticmethod
    def creat_parts_of_comparison(str):

        str_1 = ''.join(char for index, char in enumerate(str) if index%2 == 0)
        str_2 = ''.join(char for index, char in enumerate(str) if index%2 != 0)
        return str_1, str_2

class SerieOfTickets():

    tickets = {}
    id = 1
    approach = None
    num_len = None
    
    @classmethod
    def set_approach(cls, name, class_approach = Approach):
        if name in  class_approach.list_of_approach:
            cls.approach = class_approach.list_of_approach[name]

    @classmethod
    def set_approach_from_file(cls, file):
        check_file_exists(file)
        with open(file) as f:
            for line in f:
                if line.find('Moskow') != -1:
                    cls.set_approach('Moskow')
                elif line.find('Piter') != -1:
                    cls.set_approach('Piter')
                else:
                    raise CanNotFindApproachException("We can't find approach witch we know")
    
    @classmethod
    def reset(cls):
        cls.tickets = {}
        cls.id = 1  
        cls.approach = None
        num_len = None  
    
    @classmethod
    def create_tickets_from_file(cls, file):
        cls.reset()
        with open(file) as f:
            data = json.load(f)
        for ticket in data:
            cls.add_to_tickets(ticket)
    
    @classmethod
    def add_to_tickets(cls, dict_):
        if len(dict_.get("number")) == cls.num_len:
            cls.tickets[dict_.get("id")] = dict_.get("number")
        else:
            raise NotValidTicket(f"Trying to add ticket(id = {dict_.get('id')}) with unproper number")

    @classmethod
    def increment_id(cls):
        cls.id +=1
    
    @classmethod
    def set_num_len(cls, num):
        cls.reset()  
        cls.num_len = num

    @classmethod
    @property
    def total_amount_of_lucky_tickets(cls, m = 10):
        if cls.num_len%2 == 0 and cls.num_len >= 2:
            smth = some_math
            sum_ = 0.5*cls.num_len*range(m-1).stop
            k = min(cls.num_len, round(sum_/m))
            number_of_tickets = 0
            for k in range(k):
                num_1 = cls.num_len + sum_ - k*m - 1
                num_2 = cls.num_len - 1
                number_of_tickets += ((-1)**k)*smth(num_1, num_2)*smth(cls.num_len, k)
            return round(number_of_tickets)
        return 0
    
    @classmethod
    def count_lucky_tickets(cls):
        count = 0
        for ticket in cls.tickets:
            #str_ = f"{num:06}"
            if cls.approach.is_lucky_number(cls.tickets.get(ticket)):
                count += 1
        return count


    def __init__(self, number):
        self.id = self.__class__.id
        self.number = number
        self.__class__.add_to_tickets(self.to_dict())
        self.__class__.increment_id()
    
    def to_dict(self):
        return {"id": self.id, "number": self.number}
    

def main():
    try:
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('file', type=check_file_exists)
        args =  parser.parse_args()
        SerieOfTickets.set_num_len(6)
        SerieOfTickets.set_approach_from_file(args.file)
        print(SerieOfTickets.total_amount_of_lucky_tickets)
    except FileExistsError:
        print("Such file doesn't exists")


def check_file_exists(path):
    """
    Check if path exists and if path is file
    """
    path = Path(r"" + path)
    if not path.exists():
        raise FileExistsError("Such file doesn't exists")
    elif not path.is_file():
        raise FileExistsError("Such file doesn't exists")
    return path

if __name__ == "__main__":
    try:
        main()
        # SerieOfTickets.set_num_len(6)
        # ticket1 = SerieOfTickets('026466')
        # ticket2 = SerieOfTickets('888888')
        # ticket3 = SerieOfTickets('456789')
        # SerieOfTickets.set_approach_from_file('approach.txt')
        # print(SerieOfTickets.count_lucky_tickets())
        # print('*'*90)
        # print(ticket1.id)
        # print(SerieOfTickets.id)
        # print(SerieOfTickets.tickets)
        # print(SerieOfTickets.total_amount_of_lucky_tickets)
        # print(ticket2.id)
        # print(ticket1.approach)
        # SerieOfTickets.create_tickets_from_file('tickets.json')
        # SerieOfTickets.set_approach_from_file('approach.txt')
        # print('*'*90)
        # print(SerieOfTickets.tickets)
        # print(SerieOfTickets.count_lucky_tickets())
        # print(SerieOfTickets.approach.is_lucky_number('234162'))
        # print(Approach.list_of_approach)
        # SerieOfTickets.set_approach('Moskow')
        # print('*'*90)
        # print(SerieOfTickets.approach)
        # print(SerieOfTickets.tickets)
        # print(SerieOfTickets.count_lucky_tickets())
    except (CustomException, FileExistsError) as e:
        if getattr(e, 'msg', None):
            print(e.msg)
        else:
            print("Such file doesn't exists")