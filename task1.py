import argparse
import sys

class ChessDesk():
    """Create chessdesk appropriate height and width.
    Height and width must be greater or equal null"""
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def __str__(self):
        """"Return chessdesk representation"""
        even_row = '* '*self.width
        odd_row = ' *'*self.width
        view = '\n'.join([odd_row if i%2!=0 else even_row.strip() for i in range(self.height)]) 
        return view

   
def validation(value):
    """Validate and return only possitive integers.
    In case of negative integers raises argparse.ArgumentTypeError"""
    ivalue = int(value)
    if ivalue < 0 :
        raise ValueError(f"Invalid negative int {ivalue}")
    return ivalue

def parse_arg(args):
        parser = argparse.ArgumentParser()
        parser.add_argument('width', type=validation)
        parser.add_argument('height', type=validation)
        return parser.parse_args(args)

def main():
    args = parse_arg(sys.argv[1:])
    print(ChessDesk(**args.__dict__))


if __name__ == "__main__":
    main()
