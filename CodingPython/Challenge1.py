#1. First name prompt
firstName = input("Enter your first name: ")

#2. Surname Prompt
surName = input("Enter your Surname: ")
print("Welcome ", surName, firstName,"!!")

#3. The Joke
print("What do you call a bear with no teeth?\nA gummy bear")

#4. Sum
num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter a 2nd Number: "))
print("The sum is ", num1 + num2)

#5. Multiplication
num3 = int(input("Enter a 3rd Number: "))
print("The multiple of 1st num + 2nd num * 3rd num is", (num1 + num2) * num3)

#6. Pizza
sliceSt = int(input("How many slices of pizza did you start with: "))
sliceSe = int(input("How many slices have you eaten: "))
print("You had", sliceSt, "slices,\nYou have eaten", sliceSe,"slices,\nYou have", sliceSt - sliceSe,"slices left.")

#7. Next Birthday
age = int(input("How old are you? "))
print(firstName, ", you will be",(age + 1),"on your next birthday")

#8. 