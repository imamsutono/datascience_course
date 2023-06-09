class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I'm {self.age} years old.")

# Membuat objek baru dari kelas Person
person1 = Person("John", 25)
person2 = Person("Jane", 30)

# Memanggil metode introduce() pada setiap objek
person1.introduce()
person2.introduce()