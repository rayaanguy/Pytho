print("Welcome to my first python program!")
a=input("Please enter your name: ")
print("hi", a, "are you ready to see my python program?")

score = 0

print("In this project \\ I am going to quiz you basic math questions.")
print("what is 15*3? \n a) 45 \n b) 50 \n c) 55")
a=input("Please enter your answer: ")
if a=="a":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer! The correct answer is a) 45")
print("what is 20*5? \n a) 120 \n b) 110 \n c) 100")
a=input("Please enter your answer: ")
if a=="c":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer! The correct answer is c) 100")
print("what is 10*10? \n a) 90 \n b) 100 \n c) 80")

a=input("Please enter your answer: ")
if a=="b":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer! The correct answer is b) 100")

print(f"Your total score is {score} out of 3")
