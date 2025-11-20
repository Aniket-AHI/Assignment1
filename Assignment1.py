# Name: Aniket Ahirwar
# Enrollment: 0103CS231054
# Batch: 6
# Batch Time: 12:10 PM - 1:50 PM



# IF - ELSE PROBLEMS 

# 1
num = int(input("enter a number : "))
if num > 0 :
    print(f"{num} is positive")
elif num < 0 :
    print(f"{num} is negative")
else:
    print(f"{num} is Zero")


# 2.
num2 = int(input("Enter a number :"))
if num2 % 2 == 0:
    print(f"{num2} is Even")
else:
    print(f"{num2} is odd")


# 3.
y = int(input("Enter year : "))
if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    print("leap Year")
else:
    print("not leap Year")


# 4.
x = int(input("Enter a number :"))
y = int(input("Enter second number :"))
if x>y:
    print(f"{x} is greater")
else:
    print(f"{y} is greater")


# 5.
age = int(input("Enter age: "))
if age >= 18:
    print("can Vote")
else:
    print("can not vote")

# 6.
vowels = ['a', 'e', 'i', 'o', 'u']
ch = input('enter a character :').lower()
if ch in vowels:
    print(f'{ch} is vowel')
else:
    print(f'{ch} is consonant')

# 7.
num7 = int(input("Enter a number: "))
if num7 % 5 == 0:
    print(f"{num7} is Divisible by 5")
else:
    print(f"{num7} is not divisible by 5")


# 8.
num8 = abs(int(input("Enter a number: ")))

if num8 < 10:
    print(f"{num8} single digit")
elif num8 < 100:
    print(f"{num8} two digit")
else:
    print("More than two digits")

# 9.
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# 10.
num10 = int(input("Enter a number: "))
if num10 % 3 == 0 and num10 % 7 == 0:
    print(f"{num10} is multiple of 3 and 7")
else:
    print(f"{num10} is not multiple of 3 and 7")



# LADDER IF - ELSE PROBLEMS

# 1.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest =", a)
elif b >= a and b >= c:
    print("Greatest =", b)
else:
    print("Greatest =", c)

# 2.
age2 = int(input("Enter age: "))

if age2 < 13:
    print("Child")
elif age2>=13 and age2 <= 19:
    print("Teenager")
elif age2>=20 and age2 <= 59:
    print("Adult")
else:
    print("Senior citizen")

# 3.
marks2 = int(input("Enter marks: "))

if marks2 >= 90 and marks2 <= 100:
    print("Grade A")
elif marks2 >=89 and  marks >= 75:
    print("Grade B")
elif marks >=74 and marks >= 50:
    print("Grade C")
elif marks2 >=49 and marks >= 35:
    print("Grade D")
else:
    print("Fail")

# 4.
s1 = int(input("Enter side 1: "))
s2 = int(input("Enter side 2: "))
s3 = int(input("Enter side 3: "))

if s1+s2 > s3 and s1+s3 > s2 and s2+s3 > s1:
    if s1 == s2 and s2 == s3:
        print("Equilateral Triangle")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")



# 5.
char = input("Enter a character: ")

if char.isupper():
    print("Uppercase Letter")
elif char.islower():
    print("Lowercase Letter")
elif char.isdigit():
    print("Digit")
else:
    print("Special Symbol")

# 6.
units = int(input("Enter units : "))
bill = 0
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100*5 + (units-100)*7
else:
    bill = 100*5 + 100*7 + (units-200)*10

print("Bill =", bill)

# 7.
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))
if n1 > n2:
    if n1 > n3:
        if n1 > n4:
            largest = n1
        else:
            largest = n4
    else:
        if n3 > n4:
            largest = n3
        else:
            largest = n4
else:
    if n2 > n3:
        if n2 > n4:
            largest = n2
        else:
            largest = n4
    else:
        if n3 > n4:
            largest = n3
        else:
            largest = n4

print("The largest number is:", largest)

# 8.
year2 = int(input("Enter year: "))

if year2 % 100 == 0:
    print("Century Year")
else:
    print("Not Century Year")

if (year2 % 400 == 0) or (year2 % 4 == 0 and year2 % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 9.
bmi = float(input("Enter BMI value: "))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# 10.
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))
if number1 < number2:
    if number1 < number3:
        print("Smallest number is:", number1)
    else:
        print("Smallest number is:", number3)
else:
    if number3 < number2:
        print("Smallest number is:", number2)
    else:
        print("Smallest number is:", number2)


# FOR LOOP PROBLEMS

# 1.
for n in range(100, 1000):
    s = 0
    temp = n
    while temp > 0:
        d = temp % 10
        s += d**3
        temp //= 10
    if s == n:
        print(n)

# 2.
n = int(input("Enter how many primes: "))
count = 0
num = 2

while count < n:
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
        count += 1
    num += 1

# 3.
for n in range(1, 501):
    if n % 3 == 0:
        s = 0
        for d in str(n):
            s += int(d)
        if s <= 10:
            print(n, end=" ")

# 4.
n = int(input("Enter height: "))
for i in range(1, n+1):
    spaces = " " * (n-i)
    stars = "*" * (2*i - 1)
    print(spaces + stars)


# 5.
s = input("Enter a string: ").lower()
letters = set()

for ch in s:
    if 'a' <= ch <= 'z':
        letters.add(ch)

if len(letters) == 26:
    print("Pangram")
else:
    print("Not Pangram")

# 6.
for p in range(2, 100):
    prime1 = True
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            prime1 = False
            break
    if prime1:
        q = p + 2
        if q < 100:
            prime2 = True
            for j in range(2, int(q**0.5) + 1):
                if q % j == 0:
                    prime2 = False
                    break
            if prime2:
                print(p, q)

# 7.
n = int(input("Enter number: "))
s = 0
for d in str(abs(n)):
    s += int(d)

if n % s == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")


# 8
n = int(input("Enter rows: "))
row = [1]

for i in range(n):
    print(" ".join(map(str, row)))
    new_row = [1]
    for j in range(len(row)-1):
        new_row.append(row[j] + row[j+1])
    new_row.append(1)
    row = new_row

# 9.
n = int(input("Enter n: "))
s = 0
for i in range(1, n+1):
    s += i**2
print("Sum =", s)

# 10.
n = int(input("Enter number: "))
s = 0
for d in str(n):
    digit = int(d)
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    s += fact
if s == n:
    print("Strong Number")
else:
    print("Not Strong Number")

# WHILE LOOP PROBLEMS

# 1.
n = int(input("Enter number: "))
temp = n
rev = 0
while temp > 0:
    rev = rev*10 + temp % 10
    temp //= 10
print("Reversed =", rev)
i = 2
prime = True
if rev < 2:
    prime = False
else:
    while i*i <= rev:
        if rev % i == 0:
            prime = False
            break
        i += 1
if prime:
    print("Reversed is Prime")
else:
    print("Reversed is Not Prime")

# 2.
total = 0
while total <= 100:
    n = int(input("Enter number: "))
    s = 0
    temp = abs(n)
    while temp > 0:
        s += temp % 10
        temp //= 10
    total += s
print("Final Sum of digits =", total)


# 3.
n = input("Enter number: ")
i = 0
found_zero = False
while i < len(n):
    if n[i] == '0':
        found_zero = True
    i += 1
if n[0] != '0' and found_zero:
    print("Duck Number")
else:
    print("Not Duck Number")

# 4.
n = int(input("Enter number: "))
seen = []
while n != 1 and n not in seen:
    seen.append(n)
    s = 0
    temp = n
    while temp > 0:
        d = temp % 10
        s += d*d
        temp //= 10
    n = s
if n == 1:
    print("Happy Number")
else:
    print("Not Happy Number")

# 5.
n = int(input("Enter number: "))
n = abs(n)
i = 2
largest = None
while i*i <= n:
    while n % i == 0:
        largest = i
        n //= i
    i += 1
if n > 1:
    largest = n
print("Largest Prime Factor =", largest)

# 6.
while True:
    s = input("Enter string: ")
    i = 0
    j = len(s) - 1
    palindrome = True
    while i < j:
        if s[i] != s[j]:
            palindrome = False
            break
        i += 1
        j -= 1
    if palindrome:
        print("Palindrome Entered:", s)
        break

# 7.
n = int(input("Enter number: "))
while n >= 10:
    s = 0
    temp = n
    while temp > 0:
        s += temp % 10
        temp //= 10
    n = s
print("Digital Root =", n)

# 8.
n = int(input("Enter number: "))
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3*n + 1
print(1)


# 9.
n = int(input("Enter number: "))
sq = n*n
sq_str = str(sq)
found = False
i = 1
while i < len(sq_str):
    left = int(sq_str[:i]) if sq_str[:i] else 0
    right = int(sq_str[i:]) if sq_str[i:] else 0
    if left + right == n:
        found = True
        break
    i += 1
if found or n == 1:
    print("Kaprekar Number")
else:
    print("Not Kaprekar Number")

# 10.
balance = 0
while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Balance =", balance)
    elif choice == 2:
        amt = int(input("Enter deposit amount: "))
        balance += amt
    elif choice == 3:
        amt = int(input("Enter withdraw amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient Balance")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
