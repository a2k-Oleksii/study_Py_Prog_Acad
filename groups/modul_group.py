from exceptions.my_exceptions import ElevenStudentAddGroupException


class Group:
    
    def __init__(self, name_group):
        self.name_group = name_group
        self.list_group = []

    def __str__(self):
        result = "Group '{}':".format(self.name_group)
        for student in self.list_group:
            result += "\n" + student.__str__()
        return result

    def add_student(self, student):
        if student in self.list_group:
            print("This student is alredy in this group!")
        else:
            try:
                if len(self.list_group) == 10:
                    raise ElevenStudentAddGroupException()
                self.list_group.append(student)
                print("Student is add in this group!")
            except ElevenStudentAddGroupException as err:
                print(err)

    def delete_student(self, student):
        if len(self.list_group) == 0:
            self.list_group.append(student)
            print("The group does not contain any students!")
        else:
            if student in self.list_group:
                self.list_group.remove(student)
                print("This student is delete in this group!")               
            else:
                print("The group does not contain such a students!")

    def find_student(self, surname):
        if len(self.list_group) == 0:
            print("This group no have student!")
            return None
        else:
            count = 0
            for element in self.list_group:
                count += 1
                if element.surname == surname:
                    return element
                elif count == len(self.list_group):
                    return None
