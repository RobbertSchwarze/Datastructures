# Een lege queue

queue = []

# Enqueue (toevoegen)

queue.append(10)
queue.append(20)
queue.append(30)

print(queue) # [10, 20, 30]

# Dequeue (verwijderen van vooraan)

first = queue.pop(0)

print(first) # 10
print(queue) # [20, 30]

# Front bekijken, dus de nieuwste in de rij.
print(queue[0]) # 20