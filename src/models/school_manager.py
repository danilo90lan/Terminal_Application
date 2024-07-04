from models import Student, Teacher
from tools_management import write_json, studentObject_to_Dict, teacherObject_to_Dict

class School: 
    """ The School class works as a container for instances of Student and Teacher objects, 
    providing methods to interact and manipulate these objects efficiently.
    """
    def __init__(self, students, teachers):
        """ The constructor initializes the class with two arguments: students and teachers, 
        which are lists containing student and teacher instances.
    """
        self.students = students
        self.teachers = teachers

    def display_all_students(self):
        """
        Sorts the student objects in alphabetical order.
        It uses the sorted function (which sorts the elemnts of students based on criteria 
        provided by the key parameter) and the lamba function that defines how each element should be 
        sorted. After the list of objects is sorted the method print_info is called which returns the 
        instance attributes values
        return: the number of the students instances
        """
        if self.students != []: 
            print(f"""
                            ***** List of all students *****\n""")
            # sort alphabetically
            sorted_students = sorted(self.students, key=lambda student: (student.name, student.last_name))
            for i in sorted_students:
                print(Student.print_info(i))
            return f"There are {len(sorted_students)} students registered in this school"
        else:
            return  "\nThere is no students records"

    def display_all_teachers(self):
        """
        Sorts the teacher objects in alphabetical order.
        It uses the sorted function (which sorts the elemnts of students based on criteria 
        provided by the key parameter) and the lamba function that defines how each element should be 
        sorted. After the list of objects is sorted the method print_info is called which returns the 
        instance attributes values
        return: the number of the teacher instances otherwise return another message
        """
        if self.teachers != []: 
            print(f"""
                            ***** List of all teachers *****\n""")
            # sort alphabetically
            sorted_teachers = sorted(self.teachers, key=lambda teacher: (teacher.name, teacher.last_name))
            for i in sorted_teachers:
                print(Teacher.print_info(i))
            return f"There are {len(sorted_teachers)} teachers registered in this school"
        else:
            return "\nThere is no teachers records"

    def find_student_by_id(self, student_id):
        """
        Finds a student by their ID number.
        parameter: student_id: an ID number to use for the search
        returns a boolean value True if the record is found, otherwise returns False.
        """
        record_found =False
        for i in self.students:
            if Student.get_id(i) == student_id:
                student = i
                record_found = True
                break
        if record_found:
            print(Student.print_info(student))
        else:
            print("\nStudent record NOT in the system")
        return record_found
    
    def find_student_by_name(self, student_name):
        student_record = False
        student_found = []

        for i in self.students:
            if i.name.lower() == student_name.lower():
                print(Student.print_info(i))
                student_found.append(Student.get_id(i))
                student_record = True
        if not student_record:
            print("\nStudent recond NOT in the system")
        return student_record, student_found

    def find_teacher_by_id(self, teacher_id):
        """
        Finds a student by their ID number.
        parameter: student_id: an ID number to use for the search
        returns a boolean value True if the record is found, otherwise returns False.
        """
        record_found = False
        for i in self.teachers:
            if Teacher.get_id(i) == teacher_id:
                teacher = i
                record_found = True
                break
        if record_found:
            print(Teacher.print_info(teacher))
        else:
            print("\nTeacher record NOT in the system")
        return record_found
    
    def find_teacher_by_name(self, teacher_name):
        # return a boolean True if the Teacher record has benn found
        # and also the ID or list of IDs of the found instances 

        teacher_record = False
        teacher_found_id = []

        for i in self.teachers:
            if i.name.lower() == teacher_name.lower():
                print(Teacher.print_info(i))
                teacher_found_id.append(Teacher.get_id(i))
                teacher_record = True
        if not teacher_record:
            print("\nTeacher recond NOT in the system")
        return teacher_record, teacher_found_id

    def student_update(self, id):
        for i in self.students:
            if Student.get_id(i) == id:
                Student.update_student(i)
        json_data = studentObject_to_Dict(self.students) + teacherObject_to_Dict(self.teachers)
        write_json(json_data, f"\nThe student info with ID: {id} has beeen succesfully updated!")

    def teacher_update(self, id):
        for i in self.teachers:
            if Teacher.get_id(i) == id:
                Teacher.update_teacher(i)  
        json_data = studentObject_to_Dict(self.students) + teacherObject_to_Dict(self.teachers) 
        write_json(json_data,f"\nThe teacher info with ID: {id} has been succesfully updated!")

    def delete_teacher(self, id):
        for i in self.teachers:
            if Teacher.get_id(i) == id:
                self.teachers.remove(i)
        json_data = studentObject_to_Dict(self.students) + teacherObject_to_Dict(self.teachers)
        write_json(json_data, f"\nThe teacher record wih ID: {id} has been succesfully deleted!")

    def delete_student(self, id):
        for i in self.students:
            if Student.get_id(i) == id:
                self.students.remove(i)
        json_data = studentObject_to_Dict(self.students) + teacherObject_to_Dict(self.teachers)
        write_json(json_data, f"\n The student with ID: {id} has been succesfully deleted!")

    def filter_students_by_course(self, course):
        record = False
        list = []
        for i in self.students:
            if i.course.lower() == course.lower():
                list.append(i)
                print(Student.print_info(i))
                record = True
        if not record:
            print(f"\nThe course {course} has NOT been found in the system")
        return list
    
    def filter_teachers_by_subject(self, subject):
        record = False
        list = []
        for i in self.teachers:
            if i.subject_area.lower() == subject.lower():
                list.append(i)
                print(Teacher.print_info(i))
                record = True
        if not record:
            print(f"\nThe subject {subject} has NOT been found in the system")
        return list
    
    def print_list_all_courses(self):
        # defining a set variable to store the list of courses with no duplicate
        list_courses = set()
        # defining a boolean variable that returns False if the list is empty
        course = True

        for i in self.students:
            if i.course == "":
                continue
            list_courses.add(i.course)
        if list_courses:
            print(f"""
                    ***** List of all courses in the school *****\n""")
            for i in list_courses:
                print(i,"\n")
        else:
            print("There is NO courses in the system")
            course = False
        return course

    def print_list_all_subjects(self):
        # defining a set variable to store the list of all subjects with no duplicate
        list_subjects = set()
        # defining a boolean variable that returns False if the list is empty
        subject = True
        
        for i in self.teachers:
            if i.subject_area == "":
                continue
            list_subjects.add(i.subject_area)
        if list_subjects:
            print(f"""
                    ***** List of all subjects taught in the school *****\n""")
            for i in list_subjects:
                print(i,"\n")
        else:
            print("There is NO subjects in the system")
            subject = False
        return subject