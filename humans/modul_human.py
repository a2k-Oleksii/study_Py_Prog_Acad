class Human:
    
    def __init__(self, name, surname, birthday):
        self.name = name
        self.surname = surname
        self.birthday = birthday

    def __str__(self):
        return "name: {}, surname: {}, birthday: {}".format(self.name, self.surname, self.birthday)
