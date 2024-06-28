from typing import List
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average_grade(self):
        """Calculates average grade across all courses."""
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0
    def __str__(self):
        """Returns a string representation of the student."""
        average_grade = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
    def __lt__(self, other):
        """Compares students based on average grade."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()
    def __le__(self, other):
        """Compares students based on average grade."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()
    def __eq__(self, other):
        """Compares students based on average grade."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()
    def __ne__(self, other):
        """Compares students based on average grade."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() != other.average_grade()
    def __gt__(self, other):
        """Compares students based on average grade."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()
    def __ge__(self, other):
        """Compares students based on average grade."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() >= other.average_grade()
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self):
        """Returns a string representation of the mentor."""
        return f"Имя: {self.name}\nФамилия: {self.surname}"
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Dictionary to store grades from students
    def average_grade(self):
        """Calculates average grade across all courses."""
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0
    def __str__(self):
        """Returns a string representation of the lecturer."""
        average_grade = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}"
    def __lt__(self, other):
        """Compares lecturers based on average grade."""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()
    def __le__(self, other):
        """Compares lecturers based on average grade."""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() <= other.average_grade()
    def __eq__(self, other):
        """Compares lecturers based on average grade."""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()
    def __ne__(self, other):
        """Compares lecturers based on average grade."""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() != other.average_grade()
    def __gt__(self, other):
        """Compares lecturers based on average grade."""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()
    def __ge__(self, other):
        """Compares lecturers based on average grade."""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() >= other.average_grade()
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        """Returns a string representation of the reviewer."""
        return f"Имя: {self.name}\nФамилия: {self.surname}"
def average_grade_for_students(students: List[Student], course: str) -> float:
    """Calculates average grade for students in a given course."""
    grades = []
    for student in students:
        if course in student.grades:
            grades.extend(student.grades[course])
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0
def average_grade_for_lecturers(lecturers: List[Lecturer], course: str) -> float:
    """Calculates average grade for lecturers in a given course."""
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades.extend(lecturer.grades[course])
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0
# Create instances
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
another_student = Student('Jane', 'Doe', 'your_gender')
another_student.courses_in_progress += ['Python', 'Git']
another_student.finished_courses += ['Введение в программирование']
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
another_lecturer = Lecturer('John', 'Smith')
another_lecturer.courses_attached += ['Git']
# Rate homework and lectures
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(another_student, 'Python', 9)
cool_mentor.rate_hw(another_student, 'Python', 8)
cool_mentor.rate_hw(another_student, 'Python', 7)
cool_mentor.rate_hw(another_student, 'Git', 10)
cool_mentor.rate_hw(another_student, 'Git', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
another_student.rate_lecturer(cool_lecturer, 'Python', 7)
another_student.rate_lecturer(cool_lecturer, 'Python', 8)
another_student.rate_lecturer(another_lecturer, 'Git', 10)
another_student.rate_lecturer(another_lecturer, 'Git', 9)
# Print information
print(f"Best Student:\n{best_student}")
print(f"Another Student:\n{another_student}")
print(f"Cool Mentor:\n{cool_mentor}")
print(f"Cool Lecturer:\n{cool_lecturer}")
print(f"Another Lecturer:\n{another_lecturer}")
# Comparison
print(f"Is best_student better than another_student: {best_student > another_student}")
print(f"Is cool_lecturer better than another_lecturer: {cool_lecturer > another_lecturer}")
# Average grades
print(f"Average grade for Python in students: {average_grade_for_students([best_student, another_student], 'Python')}")
print(f"Average grade for Git in students: {average_grade_for_students([another_student], 'Git')}")
print(f"Average grade for Python in lecturers: {average_grade_for_lecturers([cool_lecturer], 'Python')}")
print(f"Average grade for Git in lecturers: {average_grade_for_lecturers([another_lecturer], 'Git')}")
