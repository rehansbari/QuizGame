class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list

    def next_question(self):
        print(f"Q.{self.question_number} {self.questions_list[0].text}" )
        for question in self.questions_list:
