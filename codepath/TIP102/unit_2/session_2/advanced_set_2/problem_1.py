"""
Problem 1: Cook Off

In a reality TV show, contestants are challenged to do the best recreation of a meal cooked by an all-star judge using limited resources. The meal they must recreate is represented by the string target_meal. The contestants are given a collection of ingredients represented by the string ingredients.

Help the contestants by writing a function max_attempts() that returns the maximum number of copies of target_meal they can create using the given ingredients. You can take some letters from ingredients and rearrange them to form new strings.

def max_attempts(ingredients, target_meal):
    pass

Example Input:

ingredients1 = "aabbbcccc"
target_meal1 = "abc"

ingredients2 = "ppppqqqrrr"
target_meal2 = "pqr"

ingredients3 = "ingredientsforcooking"
target_meal3 = "cooking"

Example Output:

2
3
1
"""
from collections import Counter

def max_attempts(ingredients, target_meal):
    d = Counter(ingredients)
    l = []
    for x in target_meal:
        if x in d:
            l.append(d[x])
        else:
            return 0
    return min(l)


ingredients1 = "aabbbcccc"
target_meal1 = "abc"
print(max_attempts(ingredients1, target_meal1))

ingredients2 = "ppppqqqrrr"
target_meal2 = "pqr"
print(max_attempts(ingredients2, target_meal2))

ingredients3 = "ingredientsforcooking"
target_meal3 = "cooking"
print(max_attempts(ingredients3, target_meal3))