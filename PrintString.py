def PrintString(original, binarystring):
  i = 0
  spacecount = 0
  original.strip()
  while i < len(original):
    if original[i] == " ":
      spacecount += 1
    i += 1
  print(spacecount)
  i = 0
  j = 0
  iterations = len(binarystring) + spacecount
  while i < (iterations):
    if original[i] == " ":
      print("SPACE")
      i += 1
    else:
      print(str(original[i]) + "=>" + str(binarystring[j]))
      i += 1
      j +=1
