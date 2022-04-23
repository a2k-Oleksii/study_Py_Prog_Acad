class GroupIterator:

    def __init__(self, group_list):
        self.group_list = group_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.group_list):
            raise StopIteration
        temp_student = self.group_list[self.index]
        self.index += 1
        return temp_student
