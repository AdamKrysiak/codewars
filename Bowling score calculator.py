# Rules of bowling in a nutshell:
#
# A game consists of 10 frames. In each frame the player rolls 1 or 2 balls, except for the 10th frame, where the player rolls 2 or 3 balls.
# The total score is the sum of your scores for the 10 frames
# If you knock down fewer than 10 pins with 2 balls, your frame score is the number of pins knocked down
# If you knock down all 10 pins with 2 balls (spare), you score the amount of pins knocked down plus a bonus - amount of pins knocked down with the next ball
# If you knock down all 10 pins with 1 ball (strike), you score the amount of pins knocked down plus a bonus - amount of pins knocked down with the next 2 balls
# Rules for 10th frame
#
# As the 10th frame is the last one, in case of spare or strike there will be no next balls for the bonus. To account for that:
#
# if the last frame is a spare, player rolls 1 bonus ball.
# if the last frame is a strike, player rolls 2 bonus balls.
# These bonus balls on 10th frame are only counted as a bonus to the respective spare or strike.

def bowling_score(rolls):
    return sum(rolls)


def test_sum_of_20_shots():
    assert bowling_score([2, 1, 3, 4, 5, 6, 3, 3, 2, 2, 1, 3, 4, 5, 3, 1, 2, 3, 1 ,7]) == 61
