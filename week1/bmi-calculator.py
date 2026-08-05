def bmi(weight, height):
  result = weight / (height ** 2)

  print(result)

if __name__ == "__main__":
  bmi(float(input("Please enter your weight: ")), float(input("Please enter your height: ")))
