temperature_f = int(input("Please type in a temperature (F): "))
 
temperature_c = (temperature_f - 32) * 5/9
 
print(f"{temperature_f} degrees Fahrenheit equals {temperature_c} degrees Celsius")
 
if temperature_c < 0:
    print("Brr! It's cold in here!")
    
# Please type in a temperature (F): 101
# 101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius
#
# Please type in a temperature (F): 21
# 21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
# Brr! It's cold in here!