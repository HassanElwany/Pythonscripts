class Person:
  def __init__(self, name):
      self.name = name 
  def talk(self):
    print(f"Hi!, {self.name}")

hassan = Person("Hassan Elwany")
print(hassan.name)
hassan.talk()