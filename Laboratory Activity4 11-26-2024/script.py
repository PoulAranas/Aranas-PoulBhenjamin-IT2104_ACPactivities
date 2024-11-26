from Capybara import Capybara

def run_case():
  
  test_case = int(input("Enter the test case number: "))

  if (test_case == 1):
    c1 = Capybara("Wonwoo", "M", 3)
    print(f"Test Case {test_case}: Name: {c1.name}, Gender: {c1.gender}, Age: {c1.age}")
  elif (test_case == 2):
    c2 = Capybara("Seungcheol", "M", 4)
    print(f"Test Case {test_case}: Name: {c2.name}, Gender: {c2.gender}, Age: {c2.age}")
  elif (test_case == 3):
    c3 = Capybara("Mingyu", "M", 5)
    print(f"Test Case {test_case}: Name: {c3.name}, Gender: {c3.gender}, Age: {c3.age}")
  elif (test_case == 4):
    c4 = Capybara("Vernon", "M", 6)
    print(f"Test Case {test_case}: Name: {c4.name}, Gender: {c4.gender}, Age: {c4.age}")
  else:
    print("Invalid entered number")

run_case()