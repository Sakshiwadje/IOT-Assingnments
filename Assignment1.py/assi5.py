

num1 = float(input("Enter marks of student in Maths :"))
num2 = float(input("Enter marks of student in Bio :"))
num3 = float(input("Enter marks of student in Chem :"))

avr = (num1 + num2 + num3)/3
print(f"avr = {avr}")

if (avr > 90) & (avr < 100):
    print("Grade A")
elif (avr > 80)  & (avr < 89):
    print("Grade B")
elif (avr > 70) & (avr < 79):
    print("Grade C")
elif (avr > 60) & (avr < 69):
    print("Grade D")
else:
    print("F")                