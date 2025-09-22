class Person:
    total= 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.total += 1
    def introduce(self):
        print(f"Hi, I am {self.name}, {self.age} years old.")
    @classmethod
    def total_obj(cls):
        print(f"Total object: {cls.total}")



class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age)
        self.student_id = student_id
        self.course_list = []
        self.__cgpa = 0.0

    def enroll_course(self,course):
        self.course_list.append(course) 
    def show_courses(self):
        if self.course_list:
            courses =""
            for i in range (len(self.course_list)):
                if i != len(self.course_list)-1:
                    courses += self.course_list[i] + ", "
                else:
                    courses += self.course_list[i]
            print(f" {self.name}'s Enrolled courses are {courses}")
        else:
            print(f"{self.name} has not enrolled in any courses yet.")    

    @property
    def cgpa(self):
        return self.__cgpa
    @cgpa.setter
    def cgpa(self,value):
        if 0.0 <= value <= 4.0:
            self.__cgpa = value
        else:
            print("Invalid CGPA. It must be between 0.0 and 4.0")

    @staticmethod
    def is_valid_id(student_id):
        return student_id.startswith("S-")
    
class Teacher(Person):
    def __init__(self,name,age,employee_id,subject):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.subject = subject
            

    def introduce(self):
        print(f"I am Professor {self.name}, teaching {self.subject}.")

class GraduateStudent(Student):
    def __init__(self,name,age,student_id,thesis_title):
        super().__init__(name,age,student_id)
        self.thesis_title = thesis_title

    def introduce(self):
        print(f"Hi, I am {self.name}, a graduate student researching on {self.thesis_title}.")
        
    def show_thesis(self):
        print(f"{self.name}'s thesis title is '{self.thesis_title}'")

    def display(self,Person):
        if isinstance(Person,Student):
            Person.introduce()
        elif isinstance(Person,Teacher):
            Person.introduce()

        else:
            print("Unknown person type")


if __name__ == "__main__":
    p1 = Person("ABC",24)
    

    s1 = Student("Anamika",22,"S-001")
    s1.enroll_course("Python")
    s1.enroll_course("Java")
    s1.cgpa = 3.8

    t1 = Teacher("Xayed",45,"E-1001","OOP")

    g1 = GraduateStudent("Rahim",28,"S-002","Computer Vision")

    print(p1.introduce())
    print(s1.introduce())
    print(t1.introduce())
    print(g1.introduce())
    print(s1.show_courses())    
    print(s1.cgpa)
    print(Student.is_valid_id("S-123"))
    print(Student.is_valid_id("A-123"))
    print(g1.show_thesis())    
    Person.total_obj()
    print(Student.total)
    g1.display(s1)

