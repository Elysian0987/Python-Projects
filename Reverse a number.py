# Write a python program to reverse a number

def revers_number(number):
    revers_number = 0
    while number > 0:
        digit = number % 10
        revers_number =revers_number * 10 + digit
        number = number // 10
    return revers_number
number = int(input("Enter desired number: "))
revers_number = revers_number(number)
print("Original number : ",number)
print("Reversed number : ",revers_number)

# Simplified version 

'''num = int(input("Enter desired number: "))
reversed_num = 0
while num != 0:
    digit = num % 10 
    reversed_num = reversed_num*10 + digit
    num//=10
print("Reversed Number: "+str(reversed_num))'''