from pathlib import Path
import sys
APP_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(APP_ROOT))

from task3 import Validator, ValidationException
from enum import Enum

class MoreThanTwoException(Exception):
    pass
class EnvelopeNotExistException(Exception):
    pass



class Envelope():
    count = -1
    list_of_envelopes = {}

    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2
        Envelope.validate_data(self)
        Envelope.is_exist(self)
        Envelope.add_instance(self)
    
    @classmethod
    def add_instance(cls, instance):
        if len(cls.list_of_envelopes) > 2:
            raise MoreThanTwoExcepton()    
        else:
            cls.count +=1
            cls.list_of_envelopes[cls.count] = instance.__dict__
    
    @classmethod
    def reset(cls):
        cls.list_of_envelopes = {}
        cls.count = -1
    
    @classmethod
    def put_in_envelopes(cls, envelope_1, envelope_2):
        if envelope_1['side_1'] < envelope_2['side_1'] and envelope_1['side_2'] < envelope_2['side_2']\
        or envelope_1['side_2'] < envelope_2['side_1'] and envelope_1['side_1'] < envelope_2['side_2']\
        or envelope_2['side_1'] < envelope_1['side_1'] and envelope_2['side_2'] < envelope_1['side_2']\
        or envelope_2['side_2'] < envelope_1['side_1'] and envelope_2['side_1'] < envelope_1['side_2']:
            return "You can put in each other"
        else:
            return "You can not put in each other"
    
    @classmethod
    def is_exist(cls, instance):
        if instance.side_1 <=0 or instance.side_2 <= 0:
            raise EnvelopeNotExistException()
    
    @classmethod
    def validate_data(cls, instance):
        v =  Validator()
        for attr in instance.__dict__:
            instance.__dict__[attr] = v.validate_to_number(instance.__dict__[attr])

class Choises(Enum):
    first = "first"
    second = "second"




if __name__ == "__main__":
    while True:
        while True:
            try:
                for name in Choises._member_names_:
                    side_1 = input(f"Enter the first side of the {name} envelope:")
                    side_2 = input(f"Enter the second side of the {name}  envelope:")
                    Envelope(side_1, side_2)
                envelope_1, envelope_2 =  (Envelope.list_of_envelopes[key] for key in Envelope.list_of_envelopes)
                print(envelope_1, envelope_2 )
                print(Envelope.put_in_envelopes(envelope_1, envelope_2))
                #else:
                #    for envelope_1 in Envelope.list_of_envelopes:
                #        for envelope_2 in Envelope.list_of_envelopes:
                #            if envelope_1 != envelope_2:
                #                print(Envelope.put_in_envelopes(Envelope.list_of_envelopes[envelope_1], Envelope.list_of_envelopes[envelope_2]))
                #        else:
                #            break
                #    else:
                #        break           
            except MoreThanTwoException:
                print("You have already had two envelope!")
                answer = input("Do you want to reset list? [y/n][Yes/No]").lower()
                if answer == 'y' or answer == 'yes':
                    Envelope.reset()
                else:
                    break
            except EnvelopeNotExistException:
                print("Such envelope doesn't exists")
                break
            except ValidationException:
                print("Not valid data in entering sides")
                break
            break
        answer = input("Do you want to repeat? [y/n][Yes/No]").lower()
        if answer == 'n' or answer == 'no':
            print("By my friend!")
            break
        elif answer == 'y' or answer == 'yes':
            Envelope.reset()
        else:
            print("We couldn't understand you")
            print("By my friend!")
            break
   




