# creating classes for quiz , how actully going to work and perform tasks

class QuizBrain:
    def __init__(self,list):
        self.score = 0
        self.question_number = 0
        self.question_list = list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_guess = input(f"Q.{self.question_number}:{current_question.text}.(True/False):")
        self.check_answer(user_guess,current_question.answer)

    def has_question(self):
        return self.question_number < len(self.question_list)


    def check_answer(self,user_guess,current_answer):
        if user_guess.lower() == current_answer.lower():
            self.score += 1
            print("----CORRECT!----")
        else:
            print("----INCORRECT----")
        print(f"The right answer is {current_answer}")
        print(f"Your current score is : {self.score}/{self.question_number} ")
        print("\n")