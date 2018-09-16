class Person:
    def __init__(self, name, age, GTID):
        self.set_name(name)
        self.set_age(age)
        self.set_GTID(GTID)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_GTID(self, GTID):
        self.GTID = GTID

    def get_name(self):
        return self.name

    def get_age(self):
       return self.age

    def get_GTID(self):
        return self.GTID

def same_person(person1,person2):
    if person1.GTID == person2.GTID:
        return True
    else:
        return False
#print: True, then False.
person1 = Person("David Joyner", 30, 901234567)
person2 = Person("D. Joyner", 29, 901234567)
person3 = Person("David Joyner", 30, 903987654)
print(same_person(person1, person2))
print(same_person(person1, person3))

