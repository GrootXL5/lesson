class Hello:
  def __init__(self):
    print('Hello')
  def gethello(self):
    print("first")

class Helloworld(Hello):
  def __init__(self):
    print('Hello World')
    super().__init__()
  def gethello(self):
    super().gethello()
    print("second")

obju = Helloworld()
obju.gethello()

class BuildingError(Exception):
  def __str__(self):
    return "Haм не xватит мaтepияла"

def build_check(material, limit):
  if material > limit:
    return 'Bce ok'
  else:
    raise BuildingError(material)

material = 550
print(build_check(material, 300))

def divider(a, b):
  if a == 0:
    raise ValueError
  if b > 100:
    raise IndexError
  return a / b
data = {10: 2, 2: 5, "123": 4, 18: 0, 'h': 15, 8: 4}
result = []
for key in data:
  try:
    res = divider(key, data[key])
    result.append(res)
  except (ValueError, IndexError):
    pass

print(result)
