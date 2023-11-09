#Challenge 3: Implement the Complete Student Class

class Student:

    def __init__(self):
        # Initializing private properties
        self._name = None
        self._rollNumber = None

    def setName(self, name):
        # Setter for name
        self._name = name

    def getName(self):
        # Getter for name
        return self._name

    def setRollNumber(self, rollNumber):
        # Setter for rollNumber
        self._rollNumber = rollNumber

    def getRollNumber(self):
        # Getter for rollNumber
        return self._rollNumber

# Example
student_instance = Student()

# Set name and rollNumber using setters
student_instance.setName("Akshay Mawle")
student_instance.setRollNumber(12)

# Get name and rollNumber using getters
print(student_instance.getName())        
print(student_instance.getRollNumber())   
