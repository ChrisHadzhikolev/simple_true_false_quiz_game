from question import Question
from data import question_data
from quiz import Quiz

questions = []
for question in question_data:
    questions.append(Question(question["text"], question["answer"]))

quiz = Quiz(questions)
while quiz.still_has_questions():
    answer = input(quiz.next_question()).lower().strip()
    if quiz.check_answer(answer):
        print('Correct Answer')
    else:
        print('Wrong Answer')

print('That was the last question!')
print(f'Your final score is {quiz.score} out of {len(quiz.questions)}')

