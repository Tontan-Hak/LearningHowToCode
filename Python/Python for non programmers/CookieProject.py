# Picking random numbers
import random
print(random.randint(1,10))
print(random.random())

# Make your own version of a magic 8 ball that print yes, no or maybe each time you ask it
answer = random.randint(1,3)
if answer == 1:
    print("Yes")
if answer == 2:
    print("No")
if answer == 3:
    print("Maybe")

