class BMIcalculator:
  weight = 0
  height = 0

  def getdata(self):
    """
    Get weight in kgs and height in cms.
    Height is entered in cetimetres and stored in metres
    """
    weight = float(input("Please enter your weight: "))
    height = float(input("Please enter your height: "))

    print(round(weight/(height*height),2))


def main():
  print("\n","="*42,"\n")
  print("Hello, let's calculate your BMI.");
  
  calc = BMIcalculator()
  print()
  calc.getdata()

if __name__ == "__main__":
    main()