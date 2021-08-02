class Student:

    def __init__(self, name, id, courses):
        self.name= name
        self.id= id
        for course in courses.values():
            if course[0]<=0:
                raise ValueError("Invalid Grade")
            elif course[1] not in range(0,101):
                if course[1]=="A" or course[1]=="B" or course[1]=="C" or course[1]=="D" or course[1]=="F":
                    continue
                raise ValueError("Invalid Grade")
        self.courses = courses

    def __repr__(self):
        sorted_courses = dict(sorted(self.courses.items(), key=lambda x: x[0].lower()))
        s= str(sorted_courses)
        punctuations = '''(){}:'",'''
        no_punct = ""
        for char in s:
            if char not in punctuations:
                no_punct = no_punct + char
        return "Name: "+ self.name+ "\nId: " + self.id +"\nCourses list: " + no_punct

    def get_average(self):
        sum_credits = 0
        sum_grades_credits = 0
        for course in self.courses.values():
            sum_credits+=course[0]
            sum_grades_credits+=course[1] * course[0]
        student_get_average = sum_grades_credits / sum_credits
        return student_get_average

class GradStudent(Student):

    def __init__(self, name, id, courses, degree):
        Student.__init__(self, name, id, courses)
        self.degree= degree

    def __repr__(self):
        to_print= Student.__repr__(self)
        to_print+="\nDegree: "+self.degree
        return to_print

    def get_average(self):
        if self.degree=="msc":
            if Student.get_average(self)*1.05>100:
                return 100.0
            else:
                return Student.get_average(self)*1.05
        elif Student.get_average(self)*1.15>100:
                return 100.0
        else:
            return Student.get_average(self)*1.15

class InternationalStudent(Student):

    def __init__(self, name, id, courses):
        Student.__init__(self, name, id, courses)

    def __repr__(self):
        return Student.__repr__(self)

    def get_average(self):
        dic_num_grades={}
        for dic_key in self.courses:
            if self.courses[dic_key][1] == "A":
                dic_num_grades[dic_key] = (self.courses[dic_key][0],100)
            elif self.courses[dic_key][1] == "B":
                dic_num_grades[dic_key] = (self.courses[dic_key][0], 90)
            elif self.courses[dic_key][1] == "C":
                dic_num_grades[dic_key] = (self.courses[dic_key][0], 80)
            elif self.courses[dic_key][1] == "D":
                dic_num_grades[dic_key] = (self.courses[dic_key][0], 70)
            elif self.courses[dic_key][1] == "F":
                dic_num_grades[dic_key] = (self.courses[dic_key][0], 60)
            else:
                raise ValueError ("Invaild American grade")
        sum_credits = 0
        sum_grades_credits = 0
        for course in dic_num_grades.values():
            sum_credits+=course[0]
            sum_grades_credits+=course[1] * course[0]
        student_get_average = sum_grades_credits / sum_credits
        return student_get_average

class Faculty:

    def __init__(self, name, students):
        self.name= name
        self.studetns= students

    def __repr__(self):
        course_taken_dic={}
        for stud in self.studetns:
            for course in stud.courses:
                count= course_taken_dic.get(course, 0)
                count+=1
                course_taken_dic[course]=count
        res=""
        headline="Faculty of " +self.name +"\n"
        for course in sorted(course_taken_dic.keys(), key=course_taken_dic.get, reverse=True):

            res+= course +" - " + str(course_taken_dic[course]) + " students\n"
        return headline+res

# # Use this code to test your implementation:
# A = Student('Or', '123456789', {'calculus': (7, 80), 'algebra': (7, 90), 'programming': (4, 100)})
# print(A)
# print(A.get_average())
#
# B = GradStudent('Guy', '987654321', {'calculus': (7, 84), 'quantummechanics': (4, 95), 'imageprocessing': (4, 90)},
#                 'msc')
# print(B)
# print(B.get_average())
#
# C = GradStudent('Dan', '192837465', {'phdseminar': (4, 95), 'programming': (4, 90)}, 'phd')
# print(C)
# print(C.get_average())
#
# D = InternationalStudent('Nadav', '220376541', {'calculus': (7, 'A'), 'babies 101': (2, 'C')})
# print(D)
# print(D.get_average())
#
# E = Faculty('engineering', [A, B, C, D])
# print(E)
