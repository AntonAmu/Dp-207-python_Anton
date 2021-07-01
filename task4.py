from pathlib import Path
import argparse
import sys
import logging

logging.basicConfig(filename='task4.log', filemode='a', level=logging.INFO)

class FileParser():
    """
    Class FileParser tekes 3 arguments
    file: path to file,
    string_to_find: string
    string_to_replace: string
    """
    def __init__(self, file, string_to_find, string_to_replace = None):
        self.file = file
        self.string_to_find = string_to_find
        self.string_to_replace = string_to_replace
    
    def find_str(self):
        """
        Return count of string in file
        """
        count = 0
        with open(self.file, encoding = "UTF-8") as f:
            for line in f:
                count += line.count(self.string_to_find)
        return f"Find {count} strings"
    
    
    def replace_str(self):
        """
        Replace one string another in file
        and return the number of replacement
        """
        text = []
        count = 0
        with open(self.file, encoding = "UTF-8") as f:
            for line in f.readlines():
                count += line.count(self.string_to_find)
                new_line = line.replace(self.string_to_find, self.string_to_replace)
                text.append(new_line)
        if text:
            with open(self.file, 'w+', encoding = "UTF-8") as f:
                for line in text:
                    f.write(line)
            return f"Replaced {count} strings"
    
    @staticmethod
    def check_file_exists(path):
        """
        Check if path exists and if path is file
        """
        path = Path(r"" + path)
        if not path.exists():
            raise FileExistsError()
        elif not path.is_file():
            raise FileExistsError()
        return path



def parse_arg(args):
        parser = argparse.ArgumentParser()
        parser.add_argument('file', type = FileParser.check_file_exists)
        parser.add_argument('string_to_find')
        parser.add_argument('-r', '--string_to_replace')
        return parser.parse_args(args)    

def main():
    args = parse_arg(sys.argv[1:])
    try:
        if args.string_to_replace:
            logging.info(FileParser(**args.__dict__).replace_str())
        else:
            logging.info(FileParser(**args.__dict__).find_str())
    except FileExistsError as e:
        logging.error("Such file doesn't exists")
        print("Such file doesn't exists")
        


if __name__ == "__main__":
    main()
        
