class Person:
    def __init__(self, name, age): #Конструктор класса Person
        self.__name = name #Атрибут name, приватный атрибут
        self.age = age #Атрибут age
        self.balance = 0

    def give_salary(self, salary = 1000):
        self.balance+=salary
        print(f"{self.__name} gets {salary} dollars of salary")  

    def get_name(self):  #функции-геттеры, метод, возвращающий значение приватного атрибута
        return self.__name

    def set_name(self, name): #функции-сеттеры, метод, изменяющий значение приватного атрибута
        if (str(name).isdigit()):
            print("Please input name, not number")
        else:   
            self.__name = name