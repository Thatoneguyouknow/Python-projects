'''
Task:Design and create a class that models people. Each person should be
represented by their basic information (???) and an attribute that defines
whether their information is publically available to others. Create a
person that represents you or someone your know. (Note: Start by drawing
the UML diagram.)
'''

class Person:
    ''' To create a person object you must supply a name,
          date of birth, and gender. By default new people have
          public information.
    '''
    # No class member variables needed for this example
    
    # constructor - automatically called when an object is created
    def __init__(self, name, dob, gender):
        # intialize a person's (instance variables) to parameter values passed in
        self._name = name
        self._dob = dob
        self.__gender = gender # class private attribute (cannot be overwritten in subclass)
        # by default information is public
        self._is_public = True 
        # create an empty email field, could be filled out later (add getter and setter for it)
        self._email = ""
    
    def getName(self):
        return self._name
    
    def setName(self, new_name):
        self._name = new_name
            
    def getIsPublic(self):
        return self._is_public 
    
    
    def setIsPublic(self, is_public):
        # is_public attribute can only be updated to a boolen value
        if type(is_public)==bool:
            self._is_public = is_public
        else:
            print("'is_public' must be True or False")
            
    def getDob(self):
        return self._dob
    
    def setDob(self, dob_str):
        self._dob = dob_str
        
    def getGender(self):
        return self.__gender
    
    def setGender(self, gender):
        self.__gender = gender
        
    # defines how a person object should be printed
    def __str__(self):
        if self._is_public:
            return "Name: " + self._name + " DOB: " + self._dob +                     " Gender: " + self.__gender
        else: 
            return "No results returned."
        
    # defines what it means for two person object to be equal    
    def __eq__(self,other): #p1 == p2
        if self._name == other._name:
            return True
        else:
            return False
    

def main():
    print("Creating people...") 
    # syntax --> variable = ClassName(p1, p2, p3)
    joe = Person("Joe", "12-4-2001", "male")
    print(joe)
    joe.setIsPublic(False)
    #joe._is_public = 'false'
    print(joe)

    jane = Person("Jane", "03-06-1999", "female")
    print(jane)
    #jane.setIsPublic('false')
    print(jane.getName()) # doesn't check is_public attribute.
    #jane._is_public = 'false'
    print(jane)

    print("Creating another person named Joe...")
    joe2 = Person("Joe", "12-4-2001", "male")
    print(joe2)

    # this automatically invokes the __eq__ method in the Person class
    if joe == joe2:
        print("objects are equivlant")
    else:
        print ("objects are not equal")

if __name__ == "__main__":
    main()
