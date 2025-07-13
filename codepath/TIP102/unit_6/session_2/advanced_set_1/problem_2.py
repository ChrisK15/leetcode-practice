"""
You are given the head of two linked lists, playlist1 and playlist2 with lengths n and m respectively. Remove playlist1's nodes from the ath to the bth node and put playlist2 in its place. Assume the lists are 0-indexed.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
    currentA = playlist1
    currentB = playlist2
    count = 1
    while currentA:
        if count in range(a, b + 1):
            currentA.value = currentB.value
            currentB = currentB.next
        if count == b:
             break
        currentA = currentA.next
        count += 1
    return playlist1

playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))
