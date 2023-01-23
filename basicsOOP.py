class Person:
    def __init__(self, name, age,):
        self.name = name
        self.age = age

    def setschool(self, school):
        self.school = school

    def getSchool(self):
        return self.school

    def random(self):
        print("Hi! My name is ", self.name)
        print("And my age is ", self.age)


demo_person = Person("Beidy", 25)
demo_person.setschool("Wilmington")
# print(demo_person.name)
# print(demo_person.age)
demo_person.random()
print(demo_person.getSchool())
