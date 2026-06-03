stack = []

# push = toevoegen
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# pop = verwijderen van bovenkant

x = stack.pop()

print(x) # 30
print(stack) # [10, 20]

# De belangrijkste functies van een stack zijn.


# stack.append(waarde) # push
# stack.pop()          # pop (delete the one on the stack)
# stack[-1]            # peek/top 

#print(stack[-1])