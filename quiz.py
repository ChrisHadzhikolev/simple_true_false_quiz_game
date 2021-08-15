class Quiz:
    def __init__(self, questions):
        self.question_num = 0
        self.questions = questions
        self.score = 0

    def next_question(self):
        current_question = self.questions[self.question_num]
        self.question_num += 1
        return f'Q{self.question_num}: {current_question.text} True or False? '

    def still_has_questions(self):
        return len(self.questions) - self.question_num > 0

    def check_answer(self, answer):
        if answer.lower().strip() == self.questions[self.question_num - 1].answer.lower().strip():
            self.score += 1
            return True
        return False
