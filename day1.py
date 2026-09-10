#a = int(input("Enter a number")) #typecasting
#print(type(a))

#print("This is a ", a)
#print(f"This is {a} ", end="\n") #fstring
#print("hello")

#''' b = 10 #not important to declare datatype(only in procedure oriented)
#c = a + b
#print(c) ''' #''' tripple quotes give multi line string and double quotes typically

#escape characters

#practice questions

#write a program to check if a number is odd or even
#example output = Number is odd : False

#x = int(input("Enter a number "))
#print("Number is odd : ", x%2 != 0)

#z = input("Enter a number: ")
#print("Number is odd : " + str(int (z) % 2 != 0))

# Write a program to print age in days
# OUTPUT: 3years = 1095 days

#age = int(input("Enter your age: "))
#print(age + "years", ((age)*365) "days")

#age = int(input("Enter your age: "))
#print(f"{age}years = {age * 365} days")

# Write a Program to convert minutes into hours and print it 
# example : 135 is 2 hours 15 minutes

#time = int(input("Enter time in minutes convert it into hours: "))
#print(f"{time} is {time//60} hours {time%60} minutes")

# Write a program to extract the last digit of a number
# OUTPUT = 1234 : last digit is 4

#number = int(input("Enter number: "))
#print(number, ": Last digit is ", number % 10)

#do it using string

#write a program to check if a person is eligible for discount the criteria if he must be a student and age must be below 21
#WITHOUT IF ELSE
#input values to take are role and age
#example : ELigible : True



#role = input("Enter role: ")
#age = int(input("Enter age: "))

#eligible = role == "student" and age < 21

#print("Eligible: ", eligible)

#write a program to swap two variables without using a third variable, using arithmetic operations
#example : before swap a = 10, b= 20
#after swap a = 20, b = 10

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Before swap: a =", a, ",b =", b)

a, b = b, a

print("After swap: a =", a, "b =", b)
