dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 2}

merge = dict1 | dict2
print(merge)


with (
    open("Chapter_12/text1.txt") as f1,
    open("Chapter_12/text2.txt") as f2
):
    content1 = f1.read()
    content2 = f2.read()
