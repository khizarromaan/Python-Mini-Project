def grade(p):
    if p >= 90:
        return "O"
    elif p >= 80:
        return "A+"
    elif p >= 70:
        return "A"
    elif p >= 60:
        return "B+"
    elif p >= 50:
        return "B"
    else:
        return "F"

questions = [
("Who developed Python?","James Gosling","Guido van Rossum","Dennis Ritchie","Bjarne Stroustrup","B"),
("Which symbol is used for comments?","//","#","/*","--","B"),
("Which data type is immutable?","List","Dictionary","Tuple","Set","C"),
("Which keyword is used to define a function?","function","def","fun","define","B"),
("Which function is used to take input?","scan()","cin","input()","read()","C"),
("Which collection stores key-value pairs?","List","Dictionary","Tuple","Set","B"),
("Which operator is used for exponent?","^","*","**","%","C"),
("Which loop executes while condition is true?","for","while","loop","repeat","B"),
("Which keyword skips an iteration?","break","pass","continue","exit","C"),
("Which keyword exits a loop?","continue","exit","break","stop","C")
]

def quiz():
    score = 0
    wrong = []

    for q in questions:
        print("\n" + q[0])
        print("A.", q[1])
        print("B.", q[2])
        print("C.", q[3])
        print("D.", q[4])

        while True:
            ans = input("Answer (A/B/C/D): ").upper()
            if ans in ["A","B","C","D"]:
                break
            print("Invalid choice.")

        if ans == q[5]:
            score += 1
        else:
            wrong.append((q[0], ans, q[5]))

    per = score * 100 / len(questions)

    print("\nScore:", score, "/", len(questions))
    print("Percentage: {:.2f}%".format(per))
    print("Grade:", grade(per))

    if len(wrong) > 0:
        print("\nWrong Answers")
        for i in wrong:
            print("\nQuestion:", i[0])
            print("Your Answer:", i[1])
            print("Correct Answer:", i[2])
    else:
        print("\nAll answers are correct.")

while True:
    print("\n1.Start Quiz")
    print("2.Exit")

    try:
        ch = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input.")
        continue

    if ch == 1:
        quiz()
    elif ch == 2:
        break
    else:
        print("Invalid choice.")
        