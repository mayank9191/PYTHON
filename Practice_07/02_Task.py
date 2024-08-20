# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = []
num = int(input("Enter number of list item: "))

for i in range(num):
    name = input(f"Enter list item NO.{i+1}: ").lower()
    l.append(name)


letter = input("Enter first name letter to great in name: ").lower()

# By for loop

for name in l:
    if (name.startswith(letter)):
        print(f"Hello {name.capitalize()} sir, have a nice day!")


# By while loop

# i = 0
# while (i < num)):
#     if (l[i][0] == letter):
#         print(f"Hello {l[i]} sir, have a nice day!")
#     i += 1
