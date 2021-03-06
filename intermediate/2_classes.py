"""Python supports classes and inheritance."""


class Student:
    """Student class."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return Student(self.name, self.age + other.age)

    def __str__(self):
        return "name: %s age: %d" % (self.name, self.age)

    def print_age(self):
        print("Student", self.name, "is", self.age)

    def print_location(self):
        pass


class CollegeStudent(Student):                      # supports subclassing
    """College student class."""

    def __init__(self, college, name, age):
        # call __init__ on the base class
        Student.__init__(self, name, age)
        self.college = college


class UniversityStudent(Student):
    """University student class."""

    def __init__(self, university, name, age):
        print("in university init:", super())
        super().__init__(name, age)                 # alternative way to call base class
        self.university = university

    def print_location(self):                       # overriding the base class method
        print("Location:", self.university)


print("\ncreate a student object called 'bob' from Student class...")
bob = Student('bob', 19)
bob.print_age()

print("\ncreate a college student object called 'susan' from CollegeStudent subclass...")
susan = CollegeStudent('edinburgh', 'susan', 21)
susan.print_age()               # will use base Student class method

print("\nwe can use getattr() on user defined objects...")
print("does bob have an attribute called age:", hasattr(bob, 'age'))
print("getattr(bob, 'age'):", getattr(bob, 'age'))
print("bob.age =", bob.age)       # or directly

print("\nclasses have multiple attributes...")
print(dir(UniversityStudent))
print("UniversityStudent.__class__ = ", UniversityStudent.__class__)
print("UniversityStudent.__doc__ = ", UniversityStudent.__doc__)
print("UniversityStudent.__dict__ = ", UniversityStudent.__dict__)

print("\ncreate a university student object called 'dave' from UniversityStudent subclass...")
dave = UniversityStudent('edinburgh', 'dave', 20)
dave.print_age()

# instance with subclassing
print("is dave an instance of Student:", isinstance(dave, Student))
print("is dave an instance of UniversityStudent:",
      isinstance(dave, UniversityStudent))
print("is dave an instance of CollegeStudent:",
      isinstance(dave, CollegeStudent))

print("is dave of type Student:", type(dave) is Student)
# type is exactly of UniversityStudent
print("is dave of type UniversityStudent:", type(dave) is UniversityStudent)
print("is dave an type CollegeStudent:", type(dave) is CollegeStudent)

print("is UniversityStudent a subclass of Student:",
      issubclass(UniversityStudent, Student))
print("is Student a subclass of UniversityStudent:",
      issubclass(Student, UniversityStudent))

print("\nyou can override methods in the subclass...")
dave.print_location()

print("\nyou can add two classes in your own fashion by implementing __add__() method...")
twin_a = Student('bob', 21)
twin_b = Student('tom', 21)
print(twin_a)                       # uses __str__ method
print(twin_b)                       # uses __str__ method

both_twins = twin_a + twin_b        # uses __add__ method
print(both_twins)

print("\ninstance methods are callable...but so are class methods and classes...")
print("callable(dave.print_location) =", callable(dave.print_location))
print("callable(UniversityStudent.print_location) =",
      callable(UniversityStudent.print_location))
print("callable(UniversityStudent) =", callable(UniversityStudent))

print("\nvars() built in function returns the __dict__ attribute of an object...")
# this is a list of the changeable attributes of dave
print(vars(dave))
print("when I do dave.name Python does a look-up in dave.__dict__")
print(dave.__dict__)
