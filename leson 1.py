class Granparent:
  height = 168
  satiety =  100
  age = 68
class Parent(Granparent):
  age = 45
class Child(Parent):
  height = 95
  def __init__(self):
    print(self.height)
    print(self.satiety)
    print(self.age)
kid = Child()
class Hello_world():
  hello = "Hello"
  _hello = '_hello'
  __hello = '__hello'
  def __init__(self):
    self.world = 'World'
    self._world = '_world'
    self.__world = '__world'
    def printer(self):
      print(self.hello)
      print(self._hello)
      print(self.__hello)
      print(self.world)
      print(self._world)
      print(self.__world)
class Hi(Hello_world):
  def printer_hi(self):
    print(self.hello)
    print(self._hello)
    print(self.world)
    print(self._world)
obj = Hi()
obj.printer_hi()