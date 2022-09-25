import re


class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def __str__(self):
        return f'Full_name: {self.__full_name}, Email:{self.email}, File_name:{self.file_name}, Color:{self.color}'


with open('MOCK_DATA.txt', 'r', encoding='UTF-8') as file:
    people = file.readlines()

p = []
member = []
person = []
#
for i in range(1000):
    p = re.sub('\t', r' ', people[i])
    p1 = re.sub(r"\s+", " ", p)
    p = re.split(r' ', p1)
    member = p[0] + '_' + p[1]
    member = Data(p[0] + ' ' + p[1], p[2], p[3], p[4])
    person.append(member)

with open('Full_name.txt', 'w', encoding='UTF-8') as file:
    for i in range(1000):
        file.write(f'{i}. {person[i].full_name}\n')

with open('email.txt', 'w', encoding='UTF-8') as file:
    for i in range(1000):
        file.write(f'{i}. {person[i].email}\n')

with open('file_name.txt', 'w', encoding='UTF-8') as file:
    for i in range(1000):
        file.write(f'{i}. {person[i].file_name}\n')

with open('color.txt', 'w', encoding='UTF-8') as file:
    for i in range(1000):
        file.write(f'{i}. {person[i].color}\n')