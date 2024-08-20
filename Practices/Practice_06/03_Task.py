# A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"


comment = input("Enter your comment here : ")

if ((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("Don't write any spam comment here 😒")

else:
    print("You are good to go!")
