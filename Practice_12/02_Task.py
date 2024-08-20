# Write a program to print third, fifth and seventh element from a list using enumerate function.

myList = ["Apple", "Mango", "Peach", "Pineapple", "Graphes",
          "Guava", "Oranges", "Watermelon", "Muskmelon"]


for index, item in enumerate(myList):
    if (index in (2, 4, 6)):
        print(f"{index+1} -> {item} ")
