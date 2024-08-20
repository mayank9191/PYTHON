def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

# It ensures execution of a piece of code in spite of the exception or return of any statement inside a function.
    finally:
        print("I am inside finally")


main()
