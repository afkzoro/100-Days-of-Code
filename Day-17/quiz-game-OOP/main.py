from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
#enter = input("What do you want: ")

for i in question_data:
    item1 = i['text']
    item2 = i['answer']
    question_n = Question(item1, item2)
    question_bank.append(question_n)

quiz = QuizBrain(question_bank) 
(quiz.next_question())