def fractionBinary(enteredFraction):
  whole = False
  while whole == False:
    fraction = enteredFraction
    fraction = fraction * (2**i)
    if fraction.is_integer() == True:
      whole = True
    i += 1
    
  print(fraction)

  
  
