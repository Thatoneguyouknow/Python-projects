from person_file import Person
# this (Student) file should be saved in the same directory as the person_file.py file
class Student(Person):
    def __init__(self, name, gender, dob, idnumber):
        Person.__init__(self, name, gender, dob) # calls parent's constructor 
        self._idnumber = idnumber  # add specialization
        self.list_of_courses = []
        #gender attribute is not needed, but it's here to shows you canNOT
        #  inadvertantly overwrite _Person__gender attribute, try it
        self.__gender = "x"
        # Create a list for each student to hold courses in

    def __str__(self):
        if self._is_public:
            # return self.__getInfo() will return an error, try it
            return Person.__str__(self) + " Student ID #: " + str(self._idnumber)
        else:
            return self.getName()

    def add_course(self, course):
        for i in range(len(self.list_of_courses)):
            if course.Overlap(self.list_of_courses[i]) is False:
                return "Cannot add course, course overlaps"
            else:
                continue
        self.list_of_courses.append(course)
        return "Course successfully added!"
            
                
    # Add a method here that allows students to add course to their list of
    # courses. A student should only be able to add courses if they don't
    # overlap with their existing courses. 

# add a Course class here (DO THIS FIRST)
''' Courses should be intialized with (at least) a short name (e.g., CS126),
    a number of credits, a start time, and an end time. Include a method that
    will return True if two course times overlap, and False if they do not. '''
class Course():
    def __init__(self, s_name, creds, s_time, e_time):
        self._course_name = s_name
        self._credits = creds
        self._start_time = s_time
        self._end_time = e_time

    def Overlap(self, other):
        T = [self._start_time, self._end_time]
        T[0] = T[0].split(":")
        T[1] = T[1].split(":")
        SSHours = float(T[0][0]) + (float(T[0][1])/60)
        SEHours = float(T[1][0]) + (float(T[1][1])/60)
        T = [SSHours, SEHours]
        OT = [other._start_time, other._end_time]
        OT[0] = OT[0].split(":")
        OT[1] = OT[1].split(":")
        OSHours = float(OT[0][0]) + (float(OT[0][1])/60)
        OEHours = float(OT[1][0]) + (float(OT[1][1])/60)
        OT = [OSHours, OEHours]
        if SSHours <= OSHours and OSHours <= SEHours:
            return True
        elif SSHours <= OEHours and OEHours <= SEHours:
            return True
        else:
            return False

    def __str__(self):
        return self._course_name
        
# def main():
jane = Student("Jane", "female", "03-06-1999",1671)
print(jane)
# create students and courses and add courses to each student's list of courses
c1 = Course("CS126", 3, "08:00", "09:15")
c2 = Course("MAT136", 3, "09:30", "10:20")
c3 = Course("STA177", 2, "10:00", "10:50")
# c4 = Course("Garbage", 1, "07:20", "08:10")
print(c1.Overlap(c2))
print(c2.Overlap(c3))
print(c1.Overlap(c3))
print(jane.add_course(c1))
print(jane.add_course(c3))
print(jane.list_of_courses)

#if __name__=="__main__":
#    main()
