from humans.modul_human import Human
    
    
class Student(Human):
    def __init__(self, name, surname, birthday, faculty):
        super().__init__(name, surname, birthday)
        self.faculty = faculty

    def __str__(self):
        return super().__str__() + ", faculty: {}".format(self.faculty)
