#1.1
print("Shreya Sharma")
print("Shreya Sharma")
print("Shreya Sharma")

#2.1
a = 3
b = 7
c = 4
print(f'The sum of three number is: {a+b+c}')

#2.2
st1 = "This is "
st2 = "concatenation of "
st3 = "strings."
print(st1+st2+st3)

#4.1
print("Table of 5:")
for i in range(1, 11):
    print(f'5*{i}={5*i}')

print("Table of 7:")
for i in range(1, 11):
    print(f'7*{i}={7*i}')

#4.2
num1 = int(input("Enter the number:"))
print(f'Table of {num1}:')
for i in range(1, 11):
    print(f'{num1}*{i}={num1*i}')

#4.3
num2 = int(input("Enter number to sum till number from 1:"))
print(f'The sum of number from 1 to {num2} is:  {num2*(num2+1)/2}')

#5.1
print(f'Max of three numbers is: {max(int(input("Enter first number:")), int(input("Enter second number:")),
                                     int(input("Enter third number:")))}')

# #5.2
num3 = int(input("Enter number:"))
ans = 0
for i in range(1, num3+1):
    if i % 7 == 0 and i % 9 == 0:
        ans += i
print(f"Sum of numbers divisible by 7 and 9 is: {ans}")

#5.3
n = int(input("Enter a number: "))
prime_sum = 0

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += num

print("Sum of all prime numbers from 1 to", n, "is:", prime_sum)


#6.1
def sum_of_odds(n):
    odd_sum = 0
    for i in range(1, n + 1, 2):
        odd_sum += i
    return odd_sum


n1 = int(input("Enter a number: "))
result = sum_of_odds(n1)
print("Sum of all odd numbers from 1 to", n1, "is:", result)


#6.2
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def sum_of_primes(n):
    return sum(num for num in range(1, n + 1) if is_prime(num))


n2 = int(input("Enter a number: "))
print("Sum of all prime numbers from 1 to", n2, "is:", sum_of_primes(n2))
