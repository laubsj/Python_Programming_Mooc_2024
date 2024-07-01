# Let's take the square root of math-module in use
from math import sqrt
 
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))
 
discriminant = b**2 - (4 * a * c)
 
root1 = (-b + sqrt(discriminant)) / (2 * a)
root2 = (-b - sqrt(discriminant)) / (2 * a)
 
print(f"The roots are {root1} and {root2}")
# Let's take the square root of math-module in use
 
# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5