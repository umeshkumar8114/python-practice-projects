# Umesh Kumar U95237454 (Driver)
# Ebin Abraham U52630521 (Navigator)
# ASSIGNMENT 8
# Participation % = 50/50
# Exercise (Trivia Questions)

from questions import get_questions

scores = [0, 0]  # scores of both players stored in a list

turn = 0  # first player's turn

questions = get_questions()


def game_runs():  # defining a function that runs the game
    global turn
    for ques in questions:
        if turn == 0:  # game starts with the first player's turn
            print('Question for the first player')
        else:
            print('Question for the second player')

        print(str(ques))  # prints the question

        choice = int(input('Enter your solution (a number between 1 and 4): '))

        if choice == ques.correct:  # check to see whether the answer is correct
            print('That is the correct answer.\n')
            scores[turn] += 1
        else:
            print(f'That is incorrect. The correct answer is {ques.correct}.\n')

        if turn == 1:  # this if-else structure here changes the turn from first player to second
            turn = 0
        else:
            turn = 1

    print('The first player earned {} points.'.format(scores[0]))
    print('The second player earned {} points.'.format(scores[1]))

    if scores[0] > scores[1]:  # using if-elif to determine which player won the game
        print('The first player wins the game.')
    elif scores[0] < scores[1]:
        print('The second player wins the game.')
    else:  # when both players get equal points
        print('The game is tied.')

# calling of the function that runs the game
game_runs()
