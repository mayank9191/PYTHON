# Write a python function to remove a given word from a list ad strip it at the same time.

def remove(w, lists):
    lists.remove(w)
    for i in lists:
        if (w in i):
            lists[lists.index(i)] = i.strip(w)

            print(lists)


lists = []

n = int(input("Enter total number of list item: "))

for i in range(n):
    lists.append(input(f"Enter list item number {i+1}: "))

w = input("Enter word to remove: ")
remove(w, lists)
