name = input("Entee Your Name: ")
age = input("Entee Your Age: ")

print("Hello " + name + "\nand your age is " + age)


# A small project to calculate the age in days and seconds
num1 = int(input("Please enter your age to calculate your age in days: "))
days = 366
seconds = 60
calc = num1 * days
calc_seconds = calc * seconds * 1000

a = ("Your age in days is {} and seconds is {}").format(calc, calc_seconds)
print(a)