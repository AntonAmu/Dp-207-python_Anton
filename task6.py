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

class ValidationException(CustomException):
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
    def creat_parts_of_comparison(str_):         
        str_1 = str_[:3]
        str_2 = str_[3:]
        return str_1, str_2

    @staticmethod
    def total_amount_of_lucky_tickets(instance_serie, m = 10):
        if instance_serie.num_len%2 == 0 and instance_serie.num_len >= 2:
            smth = some_math
            sum_ = 0.5*instance_serie.num_len*range(m-1).stop
            k = min(instance_serie.num_len, round(sum_/m))
            number_of_tickets = 0
            for k in range(k):
                num_1 = instance_serie.num_len + sum_ - k*m - 1
                num_2 = instance_serie.num_len - 1
                number_of_tickets += ((-1)**k)*smth(num_1, num_2)*smth(instance_serie.num_len, k)
            return round(number_of_tickets)
        return 0

class PiterApproach(Approach):

    title = 'Piter'

    @staticmethod
    def creat_parts_of_comparison(str_):

        str_1 = ''.join(char for char in str_ if int(char)%2 == 0)
        str_2 = ''.join(char for char in str_ if int(char)%2 != 0)
        return str_1, str_2
    
    @staticmethod
    def total_amount_of_lucky_tickets(instance_serie, m = 10):
        if instance_serie.num_len >= 2:
            count = 0
            for ticket in range(10**(instance_serie.num_len)):
                if instance_serie.approach.is_lucky_number(str(ticket)):
                    count += 1
            return count
        return 0

class Ticket():
    
    id = 1

    def __init__(self, number, num_len=6, id = None):
        self.id = (self.__class__.id if not id else id)
        self.num_len = num_len
        self.number = self.validate_number(number)
        self.__class__.increment_id()
    
    
    @classmethod
    def increment_id(cls):
        cls.id +=1
    
    @classmethod
    def reset(cls):
        cls.id = 1

    def validate_number(self, number):
        try:
            value = int(number)
        except ValueError:
            raise ValidationException("Not valid data")
        else:
            return '0'*(self.num_len-len(str(value))) + str(value)


class SerieOfTickets():

    ticket = Ticket


    def __init__(self, approach = None, num_len = None):
        self.tickets = {}
        self.approach = approach
        self.num_len = num_len


    def set_approach(self, name, class_approach = Approach):
        if name in  class_approach.list_of_approach:
            self.approach = class_approach.list_of_approach[name]
        else:
            raise CanNotFindApproachException("We can't find approach witch we know")
    
    def set_approach_from_file(self, file):
        check_file_exists(file)
        with open(file) as f:
            for line in f:
                if line.find('Moskow') != -1:
                    self.set_approach('Moskow')
                elif line.find('Piter') != -1:
                    self.set_approach('Piter')
                else:
                    raise CanNotFindApproachException("We can't find approach witch we know")

    def create_serie_from_file(self, file):
        self.ticket.reset()
        self.tickets = {}
        with open(file) as f:
            data = json.load(f)
        for ticket in data:
            ticket['num_len'] = self.num_len
            self.add(self.ticket(**ticket))
        

    def add(self, ticket):
        if len(ticket.number) == self.num_len:
            self.tickets[ticket.id] = ticket.number
        else:
            raise NotValidTicket(f"Trying to add ticket(id = {ticket.id}) with unproper number")

    def count_lucky_tickets(self):
        count = 0
        for ticket in self.tickets:
            if self.approach.is_lucky_number(self.tickets.get(ticket)):
                count += 1
        return count

def parse_arg(args):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=check_file_exists)
    return parser.parse_args(args)

def main():
    try:
        import sys
        args = parse_arg(sys.argv[1:])
        serie = SerieOfTickets()
        serie.num_len = 6
        serie.set_approach_from_file(args.file)
        print(serie.approach.total_amount_of_lucky_tickets(serie))
    except FileExistsError:
        print("Such file doesn't exists")


def check_file_exists(path):
    """
    Check if path exists and if path is file
    """
    path = Path(r"" + str(path))
    if not path.exists():
        raise FileExistsError("Such file doesn't exists")
    elif not path.is_file():
        raise FileExistsError("Such file doesn't exists")
    return path

if __name__ == "__main__":
    try:
        #main()
        serie = SerieOfTickets()
        serie.num_len = 6
        ticket1 = Ticket('161103')
        ticket2 = SerieOfTickets.ticket('888888')
        ticket3 = Ticket('456789')
        ticket4 = Ticket(123)
        # serie.set_approach_from_file('approach.txt')
        serie.add(ticket1)
        serie.add(ticket2)
        serie.add(ticket3)
        serie.add(ticket4)
        # print(serie.count_lucky_tickets())
        # print(serie.tickets)
        print('*'*90)
        # print(serie.tickets)
        # print(serie.approach)
        print(serie.tickets)
        serie.create_serie_from_file('tickets.json')
        serie.set_approach_from_file('approach.txt')
        # print(serie.approach.total_amount_of_lucky_tickets(serie))
        print(serie.tickets, serie.ticket.id)
        print(Ticket.id)
        # print(serie.approach)
        # print('*'*90)
        serie.set_approach('Moskow')
        # print(serie.approach)
        # print(serie.tickets)
        # print(serie.count_lucky_tickets())
        # print(Approach.list_of_approach)
        # print(serie.tickets)
        # print(serie.approach.is_lucky_number('234162'))
        # print(serie.count_lucky_tickets())
        print(serie.approach.total_amount_of_lucky_tickets(serie))
    except (CustomException, FileExistsError) as e:
        if getattr(e, 'msg', None):
            print(e.msg)
        else:
            print("Such file doesn't exists")
