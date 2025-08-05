class Dog():
    def sound(self):
        return "멍멍"

class Cat():
    def sound(self):
        return "야옹"

class Pet(Dog, Cat):
    def __str__(self):
        print (f"애완동물은 {self.sound()} 소리를 냅니다.")
