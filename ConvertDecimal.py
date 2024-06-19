from IntTranslator import integerTranslate

def fractionBinary(numerator, denominator):
  whole = False
  i = 1
  array = []
  while whole == False:
    fraction = int(numerator)/int(denominator)
    fraction = fraction * (2**i)
    if fraction.is_integer() == True:
      whole = True
      array.append(i)
      print(integerTranslate(array))
      print(int(integerTranslate(array))/i)
      
      # decimalBinary = nonDecimalBinary/i
      # print(decimalBinary)
    i += 1

  

  
  
