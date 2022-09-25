class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(f'Fullname: {self.fullname} Age: {self.age} Is married: {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, **kwargs):
        Person.__init__(self, fullname, age, is_married)
        self.marks = kwargs

    def average_marks(self):
        c = 0
        for i in self.marks:
            c += 1
        v=self.marks.values()
        return sum(v)//c

    def introduce_myself(self):
        print(f'Fullname: {self.fullname} Age: {self.age} Is married: {self.is_married} Marks: {self.marks}')

Lia_student = Student('Lia', 20, 'no', maths =5, IT=1, ART=3)
print(Lia_student.introduce_myself())


class Teacher(Person):
    salary = 20
    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience

    def bonus(self):
        if self.experience > 3:
            return (self.experience - 3) * 5
        else:
            return 0

    def introduce_myself(self):
        total = (Teacher.salary / 100) * self.bonus()
        print(f'Fullname: {self.fullname} Age: {self.age} Is married: {self.is_married} Experience: {self.experience} Salary: {Teacher.salary + total}')


kira = Teacher('Kira', 54, 'married', 15)
print(kira.introduce_myself())

def create_students():
    Lily = Student('Lily', 16, 'no', maths = 2,IT = 5, ART = 4, chemistry = 2)
    Jake = Student ('Jake' , 19, 'no', maths = 5, IT= 5, ART = 4,chemistry = 4)
    Jessi = Student('Jessi', 18, 'no', maths = 3, IT = 2, ART = 4,chemistry = 3)
    students = [Lily, Jake, Jessi]
    return students

for student in create_students():
    print(f' {student.introduce_myself()} Average marks: {student.average_marks()}')

