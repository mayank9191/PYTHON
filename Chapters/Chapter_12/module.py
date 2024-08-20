def myFunc():
    print("Hello World!")


myFunc()
print(__name__)  # it returns the name from which it runs like if we run in main.py it return module and if we run from module only returns __main__

if (__name__ == "__main__"):
  # If this code is directly executed by running the file its present in
    print("We are directly running this code")
