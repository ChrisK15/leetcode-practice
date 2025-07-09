"""
Problem 7: Performances with Maximum Audience II

If you used a dictionary as part of your solution to max_audience_performances() in the previous problem, try reimplementing the function without using a dictionary. If you implemented max_audience_performances() without using a dictionary, try solving the problem with a dictionary.

Once you've come up with your second solution, compare the two. Is one solution better than the other? Why or why not?

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
    d = {}
    for audience in audiences:
        if audience in d:
            d[audience] += 1
        else:
            d[audience] = 1
    
    max = float('-inf')
    multVal = 0
    for entry, value in d.items():
        if entry > max:
            max = entry
            multVal = value
    return max * multVal


audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
