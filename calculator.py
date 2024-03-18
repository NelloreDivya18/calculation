def calculate(num1, num2, operator):
  """
  Performs basic arithmetic operations based on the provided operator.

  Args:
      num1: First number (float).
      num2: Second number (float).
      operator: The arithmetic operation to perform (str).

  Returns:
      The result of the calculation (float).
  """
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero")
      return None
    else:
      return num1 / num2
  else:
    print("Invalid operator")
    return None

# Get user input
while True:
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    break
  except ValueError:
    print("Invalid input. Please enter numbers only.")

# Perform calculation and display result
result = calculate(num1, num2, operator)
if result is not None:
  print("The result is:", result)