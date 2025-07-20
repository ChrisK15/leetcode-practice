"""
Problem 3: Shuffle Playlist

You are given the head of a singly linked list playlist. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Shuffle the playlist to have the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only the order of the nodes themselves may be changed. Return the head of the shuffled list.

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

def shuffle_playlist(playlist):
    current = playlist
    len = 0
    
    # Find length
    while current:
        len += 1
        current = current.next
    mid = len // 2
    current = playlist
    while mid != 0:
        current = current.next
        mid -= 1
    return playlist

playlist1 = Node(1, Node(2, Node(3, Node(4))))

playlist2 = Node(('Respect', 'Aretha Franklin'),
                Node(('Superstition', 'Stevie Wonder'),
                    Node(('Wonderwall', 'Oasis'),
                        Node(('Like a Prayer', 'Madonna'),
                            Node(('Bohemian Rhapsody', 'Queen'))))))

print_linked_list(shuffle_playlist(playlist1))
print_linked_list(shuffle_playlist(playlist2))

    