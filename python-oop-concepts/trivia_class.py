# Umesh Kumar U95237454 (Driver)
# Ebin Abraham U52630521 (Navigator)
# ASSIGNMENT 8
# Participation % = 50/50
# Exercise (Trivia Questions)

class Trivia:
    def __init__(self, question, ans1, ans2, ans3, ans4, correct):
        self.question = question
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.correct = correct

    def __str__(self):
        strr = ''
        strr += self.question + '\n'
        strr += '1. ' + self.ans1 + '\n'
        strr += '2. ' + self.ans2 + '\n'
        strr += '3. ' + self.ans3 + '\n'
        strr += '4. ' + self.ans4
        return strr


