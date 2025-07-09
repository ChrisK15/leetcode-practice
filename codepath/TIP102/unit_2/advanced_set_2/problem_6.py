"""
Problem 6: Performances with Maximum Audience

You are given an array audiences consisting of positive integers representing the audience size for different performances at a music festival.

Return the combined audience size of all performances in audiences with the maximum audience size.

The audience size of a performance is the number of people who attended that performance.

def max_audience_performances(audiences):
    pass

Example Usage:

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

Example Output:

250
440
"""

def max_audience_performances(audiences):
    maxNum = max(audiences)
    retval = 0
    for audience in audiences:
        if audience == maxNum:
            retval += audience
    return retval

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))