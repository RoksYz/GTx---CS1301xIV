class Person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

one = Person("Mr. Burdell",53)
two = Person("Mrs. Burdell",53)
three = Person("George P. Burdell",25,one,two)
george_p = three

print(george_p.name)
print(george_p.mother.name)
print(george_p.father.name)
