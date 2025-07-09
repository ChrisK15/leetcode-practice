# Problem 7
def count_less_than(race_times, threshold):
    count = 0
    for x in race_times:
        if x < threshold:
            count += 1
    return count