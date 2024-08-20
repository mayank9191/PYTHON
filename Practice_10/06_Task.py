# Can you change the self-parameter inside a class to something else (say “mayank”). Try changing self to “slf” or “mayank” and see the effects.

class Test:
    def greet(mayank):
        print(f"Hi {mayank.name} sir!")

    def your_score(slf):
        print(f"Your score is {slf.score}")


obj1 = Test()
obj1.name = "Mayank"
obj1.score = 97

obj1.greet()
obj1.your_score()

# Yes we can change the self-parameter inside a class to something else
