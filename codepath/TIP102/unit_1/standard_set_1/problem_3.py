"""
Problem 3: Catchphrase

Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below.
Character               Catchphrase
"Pooh"                  "Oh bother!"
"Tigger" 	            "TTFN: Ta-ta for now!"
"Eeyore" 	            "Thanks for noticing me."
"Christopher Robin"     "Silly old bear."

If the given character does not match one of the characters included above, print "Sorry! I don't know <character>'s catchphrase!"

def print_catchphrase(character):
	pass

Example Usage

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)

Example Output:

"Oh bother!"
"Sorry! I don't know Piglet's catchphrase!"

"""
def print_catchphrase(character):
    match character:
        case "Pooh":
            print("Oh brother!")
        case "Tigger":
            print("TTFN: Ta-ta for now!")
        case "Eeyore":
            print("Thanks for noticing me.")
        case "Tigger":
            print("Silly old bear.")
        case _:
            print("Sorry! I don't know " + character + "'s catchphrase!")

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)