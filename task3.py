
class TryAddExistTriangleException(Exception):
    pass
class TriangleNotExistException(Exception):
    pass
class ValidationException(Exception):
    pass


class Triangle():

    list_of_triangles = {}

    def __init__(self, name, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.name = name
        Triangle.validate_data(self)
        Triangle.is_exist(self)
        Triangle.add_instance(self)
    @property
    def area(self):
        p = (self.side_1 + self.side_2 + self.side_3)*.5
        area = (p*(p - self.side_1)*(p - self.side_2)*(p - self.side_3))**.5
        return area
    
    @classmethod
    def add_instance(cls, instance):
        if cls.list_of_triangles.get(instance.name):
            raise TryAddExistTriangleException()    
        else:
            cls.list_of_triangles[instance.name] = instance.area
    
    @classmethod
    def reset(cls):
        cls.list_of_triangles = {}
    
    @classmethod
    def ordered_list(cls):
        ordered_list_of_triangles = sorted(list(cls.list_of_triangles.items()), key = lambda item: item[1])
        return ordered_list_of_triangles
    
    @classmethod
    def is_exist(cls, instance):
        if not isinstance(instance.area, complex):
            if instance.side_1 <=0 or instance.side_2 <= 0 or instance.side_3 <= 0 or instance.area <= 0:
                raise TriangleNotExistException()
        else:
            raise TriangleNotExistException()

    @classmethod
    def validate_data(cls, instance):
        v =  Validator()
        for attr in instance.__dict__:
            if attr == 'name':
                instance.__dict__[attr] = v.validate_to_string(instance.__dict__[attr])
            else:
                instance.__dict__[attr] = v.validate_to_number(instance.__dict__[attr])


class Validator():

    def validate_to_number(self, value):
        value = value.strip()
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                raise ValidationException()
            else:
                return value
        else:
            return value

    def validate_to_string(self, value):
        value = value.strip()
        return value
        



if __name__ == "__main__":
    while True:
        name = input("Enter the name of triangle:")
        side_1 = input("Enter the first side of triangle:")
        side_2 = input("Enter the second side of triangle:")
        side_3 = input("Enter the third side of triangle:")
        while True:
            try:
                Triangle(name, side_1, side_2, side_3)
            except TryAddExistTriangleException:
                print("You are trying to add triangle with existed name!")
                answer = input("Do you want to change name? [y/n][Yes/No]").lower()
                if answer == 'y' or answer == 'yes':
                    name = input("Enter the name of triangle:")
                else:
                    break
            except TriangleNotExistException:
                print("Such triangle doesn't exists")
                break
            except ValidationException:
                print("Not valid data in entering sides")
                break
            else:
                break
        answer = input("Do you want to add triangle? [y/n][Yes/No]").lower()
        if answer == 'n' or answer == 'no':
            output = '===== Triangles list:======\n'
            for  index, triangle in enumerate(Triangle.ordered_list()):
                output += f"{index}. [Triangle {triangle[0]}]: {round(triangle[1], 2)} cm\n"
            print(output)
            print("By my friend!")
            break
   





"""
    Triangle.reset()
    while True:
        while True:
            try:
                name = Validator.validate_to_string(input("Enter the name of triangle:"))
                side_1 =  Validator.validate_to_number(input("Enter the first side of triangle:"))
                side_2 =  Validator.validate_to_number(input("Enter the second side of triangle:"))
                side_3 =  Validator.validate_to_number(input("Enter the third side of triangle:"))
            except ValidationExcepton:
                print("Not valid data in entering sides")
                break
            else:
                while True:
                    try:
                        Triangle(name, side_1, side_2, side_3)
                    except TryAddExistTriangleExcepton:
                        print("You are trying to add triangle with existed name!")
                        answer = input("Do you want to change name? [y/n][Yes/No]").lower()
                        if answer == 'y' or answer == 'yes':
                            name = input("Enter the name of triangle:")
                        else:
                            break
                    except TriangleNotExistExcepton:
                        print("Such triangle doesn't exists")
                        break
                    else:
                        break
            finally:
                break
        answer = input("Do you want to add triangle? [y/n][Yes/No]").lower()
        if answer == 'n' or answer == 'no':
            output = '===== Triangles list:======\n'
            for  index, triangle in enumerate(Triangle.ordered_list()):
                output += f"{index}. [Triangle {triangle[0]}]: {triangle[1]} cm\n"
            print(output)
            print("By my friend!")
            break
""" 