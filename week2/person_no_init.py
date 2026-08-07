class Person:
  name = ""
  height = 0.0
  weight = 0

  def set_name(self, name: str):
    self.name = name
    print("New name: ", name)

  def set_name(self, height: float):
    self.height = height
    print("New height: ", height)

  def set_name(self, weight: int):
    self.weight = weight
    print("New weight: ", weight)

  def get_name(self):
    print("New name: ", self.name)

  def get_name(self):
    print("New height: ", self.height)

  def get_name(self):
    print("New weight: ", self.weight)

  def bmi(self):
    result = self.weight / (self.height ** 2)
    print(round(result))

def main():
  person = Person()
  person.name = "Giovani"
  person.height = 1.82
  person.weight = 90

  person.bmi()


if __name__ == "__main__":
  main()
