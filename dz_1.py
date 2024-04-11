class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.courses_in_progress = []  # текущие курсы
      self.finished_courses = []  # завершенные_курсы
      self.grades = {}  # оценки
  
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
      return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.grades}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенный курсы: {self.finished_courses}"
    
  def __gt__(self):
      if self.aver_grade() > self.aver_grade():
          return f"Средняя оценка студента {self.name} {self.surname} больше чем у студента {self.name} {self.surname}"
      else:
          return f"Средняя оценка студента {self.name} {self.surname} меньше чем у студента {self.name} {self.surname}"
      

class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []  # Прилагаемые курсы


class Reviewer(Mentor):  # Reviewer - эксперт (выставляет студентам оценки за домашние задания).

  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'
        
  def __str__(self):
      return f" Имя: {self.name}\n Фамилия: {self.surname}"

class Lecturer(Mentor):  # Lecturer - лектор (получает от студентов оценки за лекции).
  def __init__(self, name, surname):
      super().__init__(name, surname)
      self.courses_attached = []
      self.grades = {}  # оценки

  def _average_rating(self): #средняя оценка
    grade = {}
    for course in self.grades.items():
      for grade in course:
        grade.append(course)
    return sum(grade) / len(grade)
      
      
  def __str__(self):
      return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.grades}"
    
  def __gt__(self):
      if self.average_rating() > self.average_rating():
          return f"Средняя оценка лектора {self.name} {self.surname} больше чем у лектора {self.name} {self.surname}"
      else:
          return f"Средняя оценка лектора {self.name} {self.surname}"

cool_reviewer_1 = Reviewer('Олег', 'Булыгин')
cool_reviewer_1.courses_attached += ['Python']
print(cool_reviewer_1)

cool_reviewer_2 = Reviewer('Алена', 'Батицкая')
cool_reviewer_2.courses_attached += ['Git']
print(cool_reviewer_2)

cool_lecturer_1 = Lecturer('Александр', 'Сидоров')
cool_lecturer_1.courses_attached += ['Python']
cool_lecturer_1.grades = {'Python': [10, 10, 10, 10, 10]}
print(cool_lecturer_1)

cool_lecturer_2 = Lecturer('Евгений', 'Петров')
cool_lecturer_2.courses_attached += ['Git']
cool_lecturer_2.grades = {'Git': [10, 10]}
print(cool_lecturer_2)

best_student_1 = Student('Ирик', 'Мурясов', 'муж')
best_student_1.courses_in_progress += ['Python', 'Git']
best_student_1.grades = {'Python': [10, 10, 10, 10, 10], 'Git': [10, 10]}
best_student_1.finished_courses += ['Введение в программирование']
print(best_student_1)

best_student_2 = Student('Сергей', 'Иванов', 'муж')
best_student_2.courses_in_progress += ['Python', 'Git']
best_student_2.grades = {'Python': [10, 10, 10, 10, 10], 'Git': [10, 10]}
best_student_2.finished_courses += ['Введение в программирование']
print(best_student_2)