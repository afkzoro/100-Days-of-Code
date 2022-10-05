class QuizBrain:
    def __init__(self, q_list):
        self.number = 0
        self.question_list = q_list
        
    
    def next_question(self):
        new_question = self.question_list[self.number]
        self.number += 1
        user = input(f"Q.{self.number + 1}: {new_question.text} (True/False): ")