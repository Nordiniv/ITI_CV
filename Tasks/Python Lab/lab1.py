# Author: Nordin Shafiq
# Date: 2024-09-12
# Question No. 4 was implemented on the same implementation of the previous questions

class Person:
    """Question 1"""
    def __init__(self, name, age, gender):
        self.name = name # public attribute
        self._age = age # protected attribute
        self.__gender = gender # private attribute

    def _get_age(self): # protected method
        return self._age
    
    def __get_gender(self): # private method
        return self.__gender
    
    def _protect_gender(self): # protected method that calls private method
        return self.__get_gender()
    
    def display_info(self): # public method
        print(f'Name: {self.name}', f'Age: {self._get_age()}', f'Gender: {self.__get_gender()}', sep='\n')



class Student(Person):
    """Question 2"""
    def __init__(self, name, age, gender, student_id, major, GPA, studied_courses):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.major = major
        self.GPA = GPA
        self.studied_courses = studied_courses

    def _get_id(self): # protected method
        return self.student_id
    
    def display_info(self): # public method
        print(f'Name: {self.name}', f'Age: {self._get_age()}', f'Gender: {self._protect_gender()}',
              f'Student ID: {self._get_id()}', f'Major: {self.major}', f'GPA: {self.GPA}',
              f'Studied Courses: {", ".join(self.studied_courses)}', sep='\n')


 
def print_info(person):
    """Question 3"""
    person.display_info()

if __name__ == '__main__':
    p1 = Person('Sohaila', 22, 'F') # polimorphism

    s1 = Student('Nordin', 22, 'M', '1000206564', 'CCSED',
                 3.5, ['Math', 'Physics', 'Computer Vision']) # polimorphism
    
    print_info(p1)
    print("------------")
    print_info(s1)