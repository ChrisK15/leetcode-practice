# Problem 3
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