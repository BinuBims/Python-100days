from question_model import Question
from data import question_data
import quiz_brain


question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = quiz_brain.QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("you have completed the quiz")
print(f"your final score was{quiz.score}")