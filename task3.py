class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

class TryAddExistTriangleException(CustomException):
    pass
class NotValidinstanceOfTriangleException(CustomException):
    pass
class ValidationException(CustomException):
    pass

class ListOfTriangles(list):
    """
    Creates list of triangles with unique names
    """    
    def __init__(self):
        self.list = []
    
    def append(self, instance):
        if instance.name not in (triangle.name for triangle in self.list):
            self.list.append(instance)
        else:
            raise TryAddExistTriangleException('You are trying to add triangle with existed name!')
    
    def __str__(self):
        output = '===== Triangles list:======\n'
        for  index, triangle in enumerate(sorted(self.list)):
            output += f"{index+1}. [Triangle {triangle.name}]: {round(triangle.area)} cm\n"
        return output
    
class Triangle():
    """
    Creates triangles with unique names. The sides of triangles
    must be possitive integer or float value. 
    """    
    def __init__(self, name, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.name = name
        self.validate_data()
        self.check_area()
    
    @property
    def area(self):
        """
        Calculate by Heron's formula and return area
        """
        p = (self.side_1 + self.side_2 + self.side_3)*.5
        area = (p*(p - self.side_1)*(p - self.side_2)*(p - self.side_3))**.5
        return area
    

    def check_area(self):
        """
        Check if the area is complex number or area less or equal to null. 
        """ 
        if not isinstance(self.area, complex):
            if self.area <= 0:
                raise NotValidinstanceOfTriangleException('Negative area of triangle')
        else:
            raise NotValidinstanceOfTriangleException('Negative area of triangle')

    def validate_data(self):
        """
        For attribute 'name' return string with the deleted whitespace at the begin and end of the string
        For sides attributes return integer or float and checks if the value greater than null
        """ 
        for attr in self.__dict__:
            if attr == 'name':
                self.__dict__[attr] = self.__dict__[attr].strip()
            else:
                self.__dict__[attr] = validate_to_number(self.__dict__[attr])
        if self.side_1 <=0 or self.side_2 <= 0 or self.side_3 <= 0:
            raise NotValidinstanceOfTriangleException('Negative side of triangle')

    def __lt__(self, other):
        if self.area < other.area:
            return True
        else:
            return False
        
    def __gt__(self, other):
        if self.area > other.area:
            return True
        else:
            return False

def validate_to_number(value):
    value = value.strip()
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            raise ValidationException("Not valid data in entering sides")
        else:
            return value
    else:
        return value

def answer_choise(question):
    answer = input(f"{question} [y/n][Yes/No]").lower()
    if answer == 'n' or answer == 'no':
        return False
    elif answer == 'y' or answer == 'yes':
        return True
    else:
        print("We couldn't understand you")
        return answer_choise(question)

def create_triangle_from_input():
    try:
        name = input("Enter the name of triangle:")
        side_1 = input("Enter the first side of triangle:")
        side_2 = input("Enter the second side of triangle:")
        side_3 = input("Enter the third side of triangle:")
        return Triangle(name, side_1, side_2, side_3)
    except CustomException as e:
        print(e.msg)
        if answer_choise('Try again?'):
            return create_triangle_from_input()
        return

def add_to_list(triangle, list_of_triangles):
    try:
        list_of_triangles.append(triangle)
    except CustomException as e:
        print(e.msg)
        if answer_choise('Do you want to change name?'):
            name = input("Enter the name of triangle:")
            triangle.name = name
            return add_to_list(triangle, list_of_triangles)

def create_and_add(list_of_triangles):
    tr = create_triangle_from_input()
    if tr: 
        add_to_list(tr, list_of_triangles)


def main():
    list_of_triangles = ListOfTriangles()
    want_to_add = True
    while want_to_add:
        create_and_add(list_of_triangles)
        want_to_add = answer_choise('Do you want to add triangle?')
    else:
        print(list_of_triangles)


if __name__ == "__main__":
    main()
   