# calling function from our file function definition
import function_definition
base = int(input("Please enter the base value: "))
expon = int(input("Please enter the exponential value: "))
function_definition.add(base,expon)
function_definition.exp(base,expon)
function_definition.printFib(25)
fibSeries = function_definition.calFib(25)
print(fibSeries)

