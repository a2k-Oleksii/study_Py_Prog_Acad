from groups.modul_group import Group
from humans.students.modul_student import Student

if __name__ == "__main__":

    student_one = Student("Tim", "Zoom", "12.03.1988", "electronic")
    student_two = Student("Bil", "Din", "16.12.1989", "phisic")
    student_three = Student("Lia", "Mia", "29.09.1985", "marthematic")
    student_four = Student("Jhon", "Greeg", "03.11.1986", "filosophy")
    student_five = Student("Xena", "Mia", "29.09.1985", "marthematic")
    student_six = Student("Lena", "Mia", "29.09.1985", "marthematic")
    student_seven = Student("Lena", "Dona", "29.09.1985", "marthematic")
    student_eight= Student("Lena", "Anna", "29.09.1985", "marthematic")
    student_nine = Student("Lena", "Clara", "29.09.1985", "marthematic")
    student_ten = Student("Lena", "Eva", "29.09.1985", "marthematic")
    student_eleven = Student("Lena", "Guna", "29.09.1985", "marthematic")

    group_001 = Group("Smarts")

    group_001.add_student(student_one)
    group_001.add_student(student_two)
    group_001.add_student(student_three)
    group_001.add_student(student_one)
    group_001.add_student(student_four)
    group_001.add_student(student_five)
    group_001.add_student(student_six)
    group_001.add_student(student_seven)
    group_001.add_student(student_eight)
    group_001.add_student(student_nine)
    group_001.add_student(student_ten)
    group_001.add_student(student_eleven)

    print("X" * 30)
    print(group_001)
    print("X" * 30)
    print(group_001.find_student("Mia"))
    print("X" * 30)
    group_001.delete_student(student_six)
    group_001.delete_student(student_eleven)
    print("X" * 30)
    print(group_001)
