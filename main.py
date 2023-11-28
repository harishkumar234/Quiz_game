#so this code mainly focus on how to create your own class and use it main.py.
# sit back relax and have fun


from data import question_data
from quiz_works import QuizBrain
from question_formate import Question


print("----Welcome to Quiz game!----")

print("\n")

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

quiz.next_question()


while quiz.has_question():
    quiz.next_question()

print("<-----------------FINAL RESULT----------------->")
print("\n")
print("You got " + str(quiz.score) + " questions correct")
print("You got " + str((quiz.score/12)*100) + "% ")


