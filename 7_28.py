##
# A function that returns a number specifying the number of dice rolled
# the most times in a row
#

def f(dice):
    if not dice:  # return none if input is empty
        return None

    max_count = 1  # maximum streak count
    max_number = dice[0]  # number corresponding ti the maximum streak
    current_count = 1  # current streak count

    for i in range(1, len(dice)):
        if dice[i] == dice[i-1]:  # check if the current number matches the previous one
            current_count += 1  # increase the streak
        else:
            if current_count > max_count:
                max_number = dice[i - 1]
        current_count = 1  # reset streak

    # final check at the end of the string
    if current_count > max_count:
        max_count = current_count
        max_number = dice[-1]

    return max_number


print(f("5233165554211"))
print(f('2133'))