"""
Problem 2: Greeting

Write a function greeting() that accepts a single parameter, a string name, and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

def greeting(name):
	pass

Example Usage:

greetings("Michael")
greetings("Winnie the Pooh")

Example Output:

Welcome to The Hundred Acre Wood Michael! My name is Christopher Robin.
Welcome to The Hundred Acre Wood Winnie the Pooh! My name is Christopher Robin.
"""

def greetings(name):
    print("Welcome to The Hundred Acre Wood " + name + "! My name is Christopher Robin.")

greetings("Michael")
greetings("Winnie the Pooh")