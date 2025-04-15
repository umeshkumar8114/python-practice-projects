# Umesh Kumar U95237454 (Navigator)
# Ebin Abraham U52630521 (Driver)
# ASSIGNMENT 8
# Participation % = 50/50
# Exercise (Trivia Questions)

from ClassTrivia import Trivia

# below are the 10 questions that were given in the sample output.


def get_questions():
    questions = []   # an empty list is created here to later use for storing questions.
    questions.append(Trivia('How many days are in a lunar year?',
                            '354',
                            '365',
                            '243',
                            '379',
                            1))
    questions.append(Trivia('What is the largest planet?',
                            'Mars',
                            'Jupiter',
                            'Earth',
                            'Pluto',
                            2))
    questions.append(Trivia('What is the largest kind of whale?',
                            'Orca whale',
                            'Humpback whale',
                            'Beluga whale',
                            'Blue whale',
                            4))
    questions.append(Trivia('Which dinosaur could fly?',
                            'Triceratops',
                            'Tyrannosaurus Rex',
                            'Pterandon',
                            'Diplodocus',
                            3))
    questions.append(Trivia('Which of these Winnie the Pooh characters is a donkey?',
                            'Pooh',
                            'Eeyore',
                            'Piglet',
                            'Kanga',
                            2))
    questions.append(Trivia('What is the hottest planet?',
                            'Mars',
                            'Jupiter',
                            'Earth',
                            'Pluto',
                            4))
    questions.append(Trivia('Which dinosaur had the largest brain compared to body size?',
                            'Troodon',
                            'Stegosaurus',
                            'Ichthysaurus',
                            'Giganoraptor',
                            1))
    questions.append(Trivia('What is the largest type of penguin?',
                            'Chinstrap penguins',
                            'Macaroni penguins',
                            'Emperor penguins',
                            'White-flippered penguins',
                            3))
    questions.append(Trivia('Which children\'s story character is a monkey?',
                            'Winnie the Pooh',
                            'Curious George',
                            'Horton',
                            'Goofy',
                            2))
    questions.append(Trivia('How long is a year on Mars?',
                            '550 Earth days',
                            '498 Earth days',
                            '126 Earth days',
                            '687 Earth days',
                            4))

    return questions  # this returns a list of 10 questions inside the list "questions"
