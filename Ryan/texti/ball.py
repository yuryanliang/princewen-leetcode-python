def balls_re(balls):
    balls.sort()
    max_nums_stay = 0
    slow_pt = 0
    for fast_pt in range(len(balls)):
        while balls[fast_pt] - len(balls) - balls[slow_pt] >= 0:  # while slow pt ball  within the range of ball fast pt ball
            slow_pt += 1

        cur_num_stay = fast_pt - slow_pt + 1
        # num_stay
        max_nums_stay = max(max_nums_stay, cur_num_stay)
    moves=len(balls)-max_nums_stay
    return moves


balls = [6, 4, 1, 7, 10]
print(balls_re(balls))
