# Write a program to find whether a given number is prime or not.

num = int(input("Enter number: "))

count = 0

if (num > 1):
    for i in range(1, num+1):
        if (num % i == 0):
            count += 1

    if (count == 2):
        print(f"{num} is prime  number.")

    else:
        print(f"{num} is not prime number.")

elif (num == 1):
    print("0 is neither prime nor composite number")

else:
    print(f"{num} is not positive number")
