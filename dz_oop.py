from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        avg_grade = get_average_grade(self)
        
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {avg_grade:.1f}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}'''

    def __eq__(self, other):
        if isinstance(other, Student):
            return get_average_grade(self) == get_average_grade(other)
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Student):
            return get_average_grade(self) > get_average_grade(other)
        return NotImplemented
    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}        
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'  
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
    
        


@total_ordering
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        print('Lecturer не могут ставить оценки студентам')
        return f'Ошибка'
    
    def __str__(self):
        return f'{super().__str__()}\nСредняя оценка за лекции: {get_average_grade(self):.1f}'
    
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return get_average_grade(self) == get_average_grade(other)
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return get_average_grade(self) > get_average_grade(other)
        return NotImplemented  


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


def average_grade_for_course(lst, course_name):
    total_grades = [grade for person in lst for grade in person.grades.get(course_name, [])]
    return sum(total_grades) / len(total_grades) if total_grades else 0       

def get_average_grade(person):
    if isinstance(person, Student) or isinstance(person, Mentor):
        all_grades = [grade for sublist in person.grades.values() for grade in sublist]
        return sum(all_grades) / len(all_grades) if all_grades else 0

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Петр', 'Петров')
student = Student('Алехина', 'Ольга', 'Ж')



some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.grades['Python'] = [10, 9, 10, 10, 10, 10, 10, 10, 10, 10]
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
some_student.grades['Python'] = [10, 10, 10, 9, 10, 10, 10, 10, 10, 10]


# 1

def dz_1():

    print(isinstance(lecturer, Mentor))
    print(isinstance(reviewer, Mentor))
    print(lecturer.courses_attached)
    print(reviewer.courses_attached)

# 2

def dz_2():
    student.courses_in_progress += ['Python', 'Java']
    lecturer.courses_attached += ['Python', 'C++']
    reviewer.courses_attached += ['Python', 'C++']
    print(student.rate_lecturer(lecturer, 'Python', 7))
    print(student.rate_lecturer(lecturer, 'Java', 8))
    print(student.rate_lecturer(lecturer, 'C++', 8))
    print(student.rate_lecturer(reviewer, 'Python', 6))

    print(lecturer.grades)

# 3

def dz_3():
    print(some_reviewer)
    print("-"*10)
    print(some_lecturer)
    print("-"*10)
    print(some_student)
    
def dz_4():
    s1 = Student('S1', 'S1', 'M')
    s2 = Student('S2', 'S2', 'M')
    s1.courses_in_progress += ['Python']
    s2.courses_in_progress += ['Python']
    s1.grades['Python'] = [8, 8]
    s2.grades['Python'] = [10, 10]
    s1.add_courses('Введение в программирование')
    s2.add_courses('Введение в программирование')
    
    
    lst1 = [s1, s2]
    
    l1 = Lecturer('L1', 'L1')
    l2 = Lecturer('L2', 'L2')
    l1.courses_attached += ['Python']
    l2.courses_attached += ['Python']
    l1.grades['Python'] = [10, 9]
    l2.grades['Python'] = [8, 9]
    s1.rate_lecturer(l1, 'Python', 9)
    s2.rate_lecturer(l2, 'Python', 10)
    
    l1.rate_hw(s1, 'Python', 9)
    l2.rate_hw(s2, 'Python', 10)
    print(s1)
    print("-"*10)
    print(s2)
    print("-"*10)
    print(f's1 < s2: {s1 < s2}')
    print(f's1 == s2: {s1 == s2}')
    print(f'Средняя оценка за курс Python у студентов: {average_grade_for_course(lst1, "Python"):.1f}')
    print("-"*10)
    print(l1)
    print("-"*10)
    print(l2)
    print("-"*10)
    print(f'l1 < l2: {l1 < l2}')
    print(f'l1 == l2: {l1 == l2}')
    lst2 = [l1, l2]
    print(f'Средняя оценка за курс Python у лекторов: {average_grade_for_course(lst2, "Python"):.1f}')



def main():
    dz_1()
    print(f'\n{"-"*20}\n')
    dz_2()
    print(f'\n{"-"*20}\n')
    dz_3()
    print(f'\n{"-"*20}\n')
    dz_4()
    
main()