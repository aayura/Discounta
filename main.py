import time # import time library to use the sleep() function to get a delay of 5 seconds after the end of code.
def my_func(func, arg1, arg2): # define the Shell function
  return func(arg1,arg2)
i = int(input("Type in the price\n")) # take in the Original Cost
m = int(input("Type in the discount percentage without the symbol\n")) # take in discount percentage
discount = lambda x,y: (y/100) * x # lambda function to calculate discount
n = my_func(discount, i, m) # call in the Shell function to create the lambda function and the input to arguments
n = i - n # subtract discount from original Cost
print(n) # print the discounted cost
print("Thanks for using my program. The program will shut itself in 5 seconds")
time.sleep(5) # calling in sleep() function and giving 5 as the argument