"""
Problem 5: Best Set

As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes that maps attendees id numbers to the artist they voted for, return the artist that had the most number of votes. If there is a tie, return any artist with the top number of votes.

def best_set(votes):
    pass

Example Usage:

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))

Example Output:

SZA
Ethel Cain
Note: SZA and Ethel Cain would both be acceptable answers for the second example
"""

def best_set(votes):
    freq_map = {}
    for id in votes:
        if votes[id] in freq_map:
            freq_map[votes[id]] += 1
        else:
            freq_map[votes[id]] = 1
    max = float('-inf')
    retval = ""
    for artist in freq_map:
        if freq_map[artist] > max:
            max = freq_map[artist]
            retval = artist
    return retval

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))