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
("Who is known as The Boy Who Lived?","Harry Potter","Ron Weasley","Draco Malfoy","Neville Longbottom","A"),
("What is the name of Harry's owl?","Crookshanks","Hedwig","Scabbers","Errol","B"),
("Which house does Harry belong to?","Gryffindor","Slytherin","Ravenclaw","Hufflepuff","A"),
("Who is the Headmaster of Hogwarts?","Severus Snape","Rubeus Hagrid","Albus Dumbledore","Sirius Black","C"),
("Who is Harry's best friend?","Draco Malfoy","Ron Weasley","Cedric Diggory","Neville Longbottom","B"),
("What sport is played on broomsticks?","Football","Quidditch","Cricket","Hockey","B"),
("What is the name of Harry's school?","Beauxbatons","Durmstrang","Hogwarts","Ilvermorny","C"),
("What platform does the Hogwarts Express leave from?","Platform 8","Platform 9","Platform 9¾","Platform 10","C"),
("Who is Harry's female best friend?","Ginny Weasley","Luna Lovegood","Hermione Granger","Cho Chang","C"),
("Who is the main villain in the Harry Potter series?","Lucius Malfoy","Bellatrix Lestrange","Lord Voldemort","Peter Pettigrew","C")
]

def start_quiz():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    score = 0
    wrong = []

    print("\nWelcome,", name)
    print("Roll Number:", roll)
    print("Quiz Started")

    for i in range(len(questions)):
        q = questions[i]

        print("\nQuestion", i + 1)
        print(q[0])
        print("A.", q[1])
        print("B.", q[2])
        print("C.", q[3])
        print("D.", q[4])

        while True:
            ans = input("Enter Answer (A/B/C/D): ").upper()
            if ans in ["A","B","C","D"]:
                break
            else:
                print("Invalid Choice.")

        if ans == q[5]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct Answer:", q[5])
            wrong.append((q[0], ans, q[5]))

    percent = (score / len(questions)) * 100

    print("\n===== RESULT =====")
    print("Student Name:", name)
    print("Roll Number:", roll)
    print("Score:", score, "/", len(questions))
    print("Percentage: {:.2f}%".format(percent))
    print("Grade:", grade(percent))

    if len(wrong) > 0:
        print("\nReview of Incorrect Answers")
        for i in wrong:
            print("\nQuestion:", i[0])
            print("Your Answer:", i[1])
            print("Correct Answer:", i[2])
    else:
        print("\nExcellent! All Answers are Correct.")

while True:
    print("\nQuiz and Examination System")
    print("1. Start Quiz")
    print("2. Exit")

    try:
        ch = int(input("Enter Choice: "))
    except ValueError:
        print("Invalid Input.")
        continue

    if ch == 1:
        start_quiz()
    elif ch == 2:
        print("Thank You!")
        break
    else:
        print("Invalid Choice.")