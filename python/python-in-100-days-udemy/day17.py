questionData = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.",
        "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


class Question:
    def __init__(self, q, a):
        self.text = q
        self.answer = a


class QuizMachine:
    def __init__(self, questionBank):
        self.score = 0
        self.qNum = 0
        self.questions = questionBank

    def next_question(self):
        now_question = self.questions[self.qNum]
        self.qNum += 1
        while True:
            user_answer = input(f"Q.{self.qNum}: {now_question.text} (True/False):\n").strip()
            if user_answer.lower() not in ["true", "false"]:
                print("Invalid input. Please enter 'True' or 'False'.")
                continue
            self.check_answer(user_answer, now_question.answer)
            break

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("right!")
            self.score += 1
        else:
            print("wrong!")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.qNum}")

    def stil_quiz(self):
        if self.qNum < len(self.questions):
            return True
        else:
            return False


questionBank = []
for question in questionData:
    newq = Question(question["text"], question["answer"])
    questionBank.append(newq)
quiz = QuizMachine(questionBank)
while quiz.stil_quiz():
    quiz.next_question()