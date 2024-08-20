# Write a program to find whether a given number is prime or not.

num = int(input("Enter number: "))

if (num > 1):
    for i in range(2, num):
        if ((num % i) == 0):
            f"{num} is not prime  number."
            break

    else:
        print(f"{num} is prime  number.")

elif (num == 0):
    print(f"{num} is not prime  number.")

else:
    print(f"{num} is not positive number.")
