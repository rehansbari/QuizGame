class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        user_answer = input((f"Q.{self.question_number + 1} {self.questions_list[self.question_number].text} (True/False): " )).lower()
        self.check_answer(user_answer)

    def still_has_question(self):
        if self.question_number < len(self.questions_list):
           return True
        else:
            print("You've completed the quiz!")
            print(f"You final score was {self.score}/{self.question_number + 1}")
            return False

    def check_answer(self, answer):
        correct_answer = self.questions_list[self.question_number].answer.lower()
        if answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print("\n")
        self.question_number += 1