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
    sum = 0
    spare_flag = False
    strike_flag_ctr=[0,0]
    FINAL_ROUND_NR=(17,)
    row_num=0
    if len(rolls) > 22:
        rolls = rolls[:22]
    for shot in rolls:
        if row_num>FINAL_ROUND_NR[0]:
            for i,x in enumerate(strike_flag_ctr):
                if x>0:
                    sum+=shot
                    strike_flag_ctr[i]-=1
            if spare_flag:
                sum += shot
                spare_flag=False
            sum+=shot
            continue
        if row_num % 2 == 0:
            first_shot = shot
            sum+=first_shot
            if spare_flag:
                sum += first_shot
                spare_flag = False
            for i,x in enumerate(strike_flag_ctr):
                if x>0:
                    sum+=first_shot
                    strike_flag_ctr[i]-=1
            if first_shot==10:
                strike_flag_ctr[1]=strike_flag_ctr[0]
                strike_flag_ctr[0]=2
                row_num+=1
        else:
            second_shot = shot
            sum+=second_shot
            for i,x in enumerate(strike_flag_ctr):
                if x>0:
                    sum+=second_shot
                    strike_flag_ctr[i]-=1
            if first_shot+second_shot== 10:
                spare_flag = True
        row_num+=1
    return sum


def test_sum_of_20_shots():
    assert bowling_score(
        [2,1, 3,4, 5,4, 3,3, 2,2, 1,3, 4,5, 3,1, 2,3, 1,7]) == 59

def test_spare():
    assert bowling_score([2, 8, 3, 7, 2, 4]) == 31

def test_strike():
    assert bowling_score([10, 8, 1, 7, 2]) == 37

def test_final_round_spare():
    assert bowling_score([2, 1, 3, 4, 5, 4, 3, 3, 2, 2, 1, 3, 4, 5, 3, 1, 2, 3, 1, 9, 6]) == 67

def test_final_round_strike():
    assert bowling_score([2, 1, 3, 4, 5, 4, 3, 3, 2, 2, 1, 3, 4, 5, 3, 1, 2, 3, 10, 9, 1]) == 71

def test_all_spares():
    assert bowling_score([9,1] * 10 + [9]) == 190

def test_perfect_score():
    assert bowling_score([10]*12 )==300
