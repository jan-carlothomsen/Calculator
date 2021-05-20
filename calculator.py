firstnumber = ""
while firstnumber == "":
    try:
        firstnumber = int(input("First number?"))
    except ValueError:
        print("I need a number")
        firstnumber == ""
#First Number
operator=""
while (operator != '+') and (operator != '-') and (operator != '*') and (operator != '/'):
        operator = input("Math Operator?")
#Math operator
secondnumber = ""
while secondnumber == "":
    try:
        secondnumber = int(input("Second number?"))
    except ValueError:
        print("I need a number")
        secondnumber = ""
#Second number
result = 0
if operator == "+":
    result = firstnumber + secondnumber
elif operator == "-":
    result = firstnumber - secondnumber
elif operator == "*":
    result = firstnumber * secondnumber
elif operator == "/":
    if secondnumber != 0:
        result = firstnumber / secondnumber
else:
    result = "I don´t understand"
print(result)
#result


