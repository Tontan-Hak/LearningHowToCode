# Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1

# break statement
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

# continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) # Note that number 3 is missing in the result

# else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
