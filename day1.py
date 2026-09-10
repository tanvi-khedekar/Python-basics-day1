a = int(input("Enter a number")) #typecasting
print(type(a))

print("This is a ", a)
print(f"This is {a} ", end="\n") #fstring
print("hello")

''' b = 10 #not important to declare datatype(only in procedure oriented)
#c = a + b
#print(c) ''' #''' tripple quotes give multi line string and double quotes typically

#escape characters

#practice questions

#write a program to check if a number is odd or even
#example output = Number is odd : False

x = int(input("Enter a number "))
print("Number is odd : ", x%2 != 0)

z = input("Enter a number: ")
print("Number is odd : " + str(int (z) % 2 != 0))

# Write a program to print age in days
# OUTPUT: 3years = 1095 days

#age = int(input("Enter your age: "))
#print(age + "years", ((age)*365) "days")

age = int(input("Enter your age: "))
print(f"{age}years = {age * 365} days")

#Write a Program to convert minutes into hours and print it 
#example : 135 is 2 hours 15 minutes

#time = 
        