# Problem 8
def print_todo_list(task):
    print("Pooh's To Dos:")
    for item in range(len(task)):
        num = item + 1
        print(str(num) + ". " + task[item])