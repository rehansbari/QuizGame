# class User:
#     # Initializing the object that is created. Left is the actual attribute name of the class you can access or modify later
#     def __init__(self, username):
#         self.username = username
#         self.followers = 0
#         #To create a default value that every object has, don't include it in the parameters when initializing the class
#
#     def gain_followers(self):
#         self.followers = 100
#
# user_1 = User("Rehan")
# print(user_1.username)
#
# user_1.gain_followers()
# print(user_1.followers)

import data
from quiz_brain import QuizBrain
from quiz_model import Question

data = data.question_data
question_bank = []
for i in range(len(data) -1):
    question = Question(q_text = data[i]['text'], q_answer= data[i]['answer'])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()
