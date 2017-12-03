# Program make a simple calculator
# that can add, subtract, multiply, divide
# and use exponent, integer division and modulus functions

add <- function(x, y) {
  return(x + y)
}

subtract <- function(x, y) {
  return(x - y)
}

multiply <- function(x, y) {
  return(x * y)
}

divide <- function(x, y) {
  return(x / y)
}

exponent <- function(x, y) {
  return(x ** y)
}

Integer_division <- function(x, y) {
  return(x %/% y)
}

modulus <- function(x, y) {
  return(x %% y)
}

square_root <- function(x) {
  return(sqrt(x))
}

squared <- function(x) {
  return(x*x)
}

cubed <- function(x) {
  return(x*x*x)
}

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Integer_division")
print("7.modulus")
print("8.square_root")
print("9.squared")
print("10.cubed")

choice = as.integer(readline(prompt="Enter choice[1/2/3/4/5/6/7/8/9/10]: "))

if(choice < 8){

  num1 = as.integer(readline(prompt="Enter first number: "))
  num2 = as.integer(readline(prompt="Enter second number: "))

  operator <- switch(choice,"+","-","*","/","**","%/%","%%")
  result <- switch(choice, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2), exponent(num1, num2), Integer_division(num1, num2), modulus(num1, num2))

  print(paste(num1, operator, num2, "=", result))
} else if(choice == 8) {
  num3 = as.integer(readline(prompt="Enter a number: "))
  print(paste("Square root of",(num3), "=", sqrt(num3)))
} else if(choice == 9) {
  num4 = as.integer(readline(prompt="Enter a number: "))
  print(paste((num4), "squared", "=", (num4*num4)))
} else if(choice == 10) {
  num5 = as.integer(readline(prompt="Enter a number: "))
  print(paste((num5), "cubed", "=", (num5*num5*num5)))
} else {
  print("Invalid Choice")
}
