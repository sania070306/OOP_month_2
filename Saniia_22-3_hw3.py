class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def set_cpu(self, value):
        self.__cpu = value

    def get_cpu(self):
        return self.__cpu

    def set_memory(self, value):
        self.__memory = value

    def get_memory(self):
        return self.__memory

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f'Cpu: {self.__cpu}, Memory: {self.__memory}'

    def __gt__(self, other):
        return self.__memory > other.__memory
    def __eq__(self, other):
        return self.__memory == other.__memory
    def __ge__(self, other):
        return self.__memory >= other.__memory
    def __lt__(self, other):
        return self.__memory < other.__memory
    def __le__(self, other):
        return self.__memory <= other.__memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def set_sim_cards_list(self, value):
        self.__sim_cards_list = value

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def call(self, sim_card_number, call_to_number):
        self.sim_card_number = sim_card_number
        self.call_to_number = call_to_number
        print(f'Идет звонок на номер {self.sim_card_number}, с сим-карты {self.call_to_number}')

    def __str__(self):
        return f'Sim cards list: {self.__sim_cards_list}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
    def use_gps(self, location):
        self.location = location
        print(f'Осталось {self.location} метров')

    def __str__(self):
        return f'{Computer.__str__(self)} {Phone.__str__(self)}'

computer = Computer(16, 321)
phone = Phone(2)
smart_phone1 = SmartPhone(6, 124, 3)
smart_phone2 = SmartPhone(4, 64, 2)
print(computer)
print(phone)
print(smart_phone1)
print(smart_phone2)

print(computer.make_computations())
print(computer > smart_phone1)
print(computer >= smart_phone1)
print(computer < smart_phone1)
print(computer <= smart_phone1)
print(computer == smart_phone1)
print(computer > smart_phone2)
print(computer >= smart_phone2)
print(computer < smart_phone2)
print(computer <= smart_phone2)
print(computer == smart_phone2)
print(phone.call(9966622451, 2))
print(smart_phone1.use_gps(20))
print(smart_phone2.use_gps(500))