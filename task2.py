from pathlib import Path
import sys
APP_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(APP_ROOT))

from task3 import validate_to_number, ValidationException
from enum import Enum

EXIT = 'Do you want to exit?'
REPEAT = 'Do you want to repeat?'
TRY = 'Try again?'
INFO = "We couldn't understand you"
CAN =  "You can put in each other"
CANNOT = "You can not put in each other"

class Envelope():
    """Create the envelope with two sides.
    The side must be possitive integer or float value"""
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2
        Envelope.validate_data(self)
    
    
    def put_in_envelope(self, envelope):
        """Cheks if two envelopes can be puted into eachother"""
        if self.side_1 < envelope.side_1 and self.side_2 < envelope.side_2\
        or self.side_2 < envelope.side_1 and self.side_1 < envelope.side_2\
        or envelope.side_1 < self.side_1 and envelope.side_2 < self.side_2\
        or envelope.side_2 < self.side_1 and envelope.side_1 < self.side_2:
            return CAN
        else:
            return CANNOT
    
    @staticmethod
    def validate_data(instance):
        for attr in instance.__dict__:
            instance.__dict__[attr] = validate_to_number(instance.__dict__[attr])
            if instance.__dict__[attr] <= 0:
                raise ValidationException('The side should be possitive number')

class Choises(Enum):
    first = "first"
    second = "second"

def answer_choise(question):
    answer = input(f"{question} [y/n][Yes/No]").lower()
    if answer == 'n' or answer == 'no':
        return False
    elif answer == 'y' or answer == 'yes':
        return True
    else:
        print(INFO)
        return answer_choise(question)

def create_envelop_from_input(name):
    try:
        side_1 = input(f"Enter the first side of the {name} envelope:")
        side_2 = input(f"Enter the second side of the {name}  envelope:")
        return Envelope(side_1, side_2)
    except ValidationException as e:
        print(e.msg)
        if answer_choise(TRY):
            return create_envelop_from_input(name)
        else:
            return False

def create_envelopes():
    for name in Choises._member_names_:
        yield create_envelop_from_input(name)

def main():
    envelope_1, envelope_2 =  create_envelopes()
    if False in (envelope_1, envelope_2):
        if answer_choise(EXIT):
            return None
        else:
            if answer_choise(REPEAT):
                return main()
            else:
                return None
    else:
        print(envelope_1.put_in_envelope(envelope_2))
        if answer_choise(REPEAT):
            return main()
        else:
            return None


if __name__ == "__main__":
    main()