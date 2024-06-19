alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetposition = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

def letLocation(string):
  array = []
  string = string.lower()
  i = 0
  while i < len(string):
    j = 0
    while j < len(alphabet):
      if string[i] == alphabet[j]:
        array.append(alphabetposition[j])
      j += 1
    i += 1
  return(array)
  return(spacecount)

