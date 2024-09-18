grade = int(input("Type your percent: "))
if 0 <= grade <= 50:
    print("You got a F")
elif 51 <= grade <=60:
    print("You got a D")
elif 61 <= grade <=75:
    print("You got a C")
elif 76 <= grade <=88:
    print("You got a B")
elif 89 <= grade <= 100:
    print("You got an A")