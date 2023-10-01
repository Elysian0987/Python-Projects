import secrets
import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation
allChars = lower + upper + digits + special
password = ""

pwLen = int(input("Password Length : "))
minLower = int(input("Lower Case : "))
minUpper = int(input("Upper Case : "))
minDigits = int(input("Digits : "))
minSpec = int(input("Special Characters : "))

for i in range(minLower):
    password += "".join(random.choice(secrets.choice(lower)))

for i in range(minUpper):
    password += "".join(random.choice(secrets.choice(upper)))

for i in range(minDigits):
    password += "".join(random.choice(secrets.choice(digits)))

for i in range(minSpec):
    password += "".join(random.choice(secrets.choice(special)))

remaining = pwLen - minLower - minUpper - minDigits - minSpec

for i in range(remaining):
    password += "".join(random.choice(secrets.choice(allChars)))

password = list(password)
random.shuffle(password)
print("".join(password)) 