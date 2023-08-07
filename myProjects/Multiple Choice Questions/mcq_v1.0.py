from question import Question

question_prompt = [
    "\nWho is the child of Orland? \na) Fiona \nb) Jason \nc) Rebecca \n\n",
    "\nWho is the youngest of all the siblings? \na) Devaj \nb) Mesha \nc) Emmanuel \n\n",
    "\nWhat is Jason's middle name? \na) Jerome \nb) Abranches \nc) Albert \n\n"
]

answers = [
    "Rebecca",
    "Devaj",
    "Abranches"
]

questions = [
    Question(question_prompt[0], "c"),
    Question(question_prompt[1], "a"),
    Question(question_prompt[2], "b")
]


def run_test(questions):
    score = 0
    correct = True
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer and correct:
            score += 1
        else:
            i = 0
            print("\nIncorrect answer. The correct answer is " + answers[i])
            i += 1

    print("\nYou got " + str(score) + "/" + str(len(questions)) + " correct. \n")


run_test(questions)
