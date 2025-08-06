class Dog():
    def sound(self):
        return "멍멍"

class Cat():
    def sound(self):
        return "야옹"

class Pet(Cat, Dog):
    def __str__(self):
        return f"애완동물은 {self.sound()} 소리를 냅니다."

pet1 = Pet()
print (pet1)
print (pet1)