class UniversityStudent():
    """University student class."""

    def __init__(self, university, name, age):
        self.university = university
        self.name = name
        self.age = age

    def __repr__(self):
        """return representation"""      # use %r as we want UniversityStudent('edinburgh', 'dave', 20) *with* quotes
        return "UniversityStudent(%r, %r, %r)" % (self.university, self.name, self.age)

    def __str__(self):
        return "%s university student %s of age %d" % (self.university, self.name, self.age)


dave = UniversityStudent('edinburgh', 'dave', 20)

print("using user defined versions of __repr__ and __str__ in class...")
print("%r" % dave)      # uses __repr__
print("%s" % dave)      # uses __str__

# create an object based on what the object is
print("we can evaluate the representation to create the same object...")
print(repr(dave))
debug = eval(repr(dave))

unicode_university = UniversityStudent("\u018e", "sam", 22)
print(repr(unicode_university))
# get unicode as ASCII escape characters
print(ascii(unicode_university))
