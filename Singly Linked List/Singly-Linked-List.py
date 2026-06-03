# Singly Linked List

# Het heeft Nodes, en een reference die naar de volgende Node
# verwijst. De laatste Node is null.

# In een Singly Linked list, elke node heeft 2 stukjes.
# Data en een pointer die verwijst naar de volgende node.
# Deze structure zorgt ervoor dat nodes linked zijn
# Ze vormen een soortvan chain-like sequence.

# Definitie van een Node
class Node:
    def __init__(self, data):
        # Data part van de node.
        self.data = data
        self.next = None

# We gebruiken een integer voor data om informatie op te slaan.
# En een pointer om naar de volgende node te verwijzen.

# We maken een kleine Linked List of size 3 to Understand the working.

# First Node
# We maken memory voor de eerste node en we slaan hier data in op.
# We linken deze node aan de volgende node.

# Create Second Node
# We maken de second node, en slaan hier data in op.
# We linked de vorige nodig, met deze nieuwe node.

# Create the third node
# Allocate memory for the third node and store data in it.
# Link the second node's next to the node.
# Set it's next to NULL, want dit is de laatste die we linken.

# We maken de eerste Node (hoofd van de lijst.)
head = Node(10)

# We linken de volgende node
head.next = Node(20)

# We linken de derde node.

head.next.next = Node(30)

# We linked de vierde node.

head.next.next.next = Node(40)

# We verwijderen de derde node
head.next.next = head.next.next.next

# printing linked list
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next