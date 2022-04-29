import sys
def mycipher(number):
  text=input()
  encoded=""
  res=""
  upper=text.upper()
  for char in upper:
    if char.isalpha()==False:
      continue
    ascii=((ord(char) + number)-65) % 26 + 65
    encoded += chr(ascii) 
  groups_of_5=[]
  for i in range(0,len(encoded),5):
    groups_of_5.append(encoded[i:i+5])
  counter=1
  for word in groups_of_5:
    if counter%10==0:
      res+=word+"\n"
    else:
      res+= word + " "
    counter+=1
  return res
n=int(sys.argv[1])
print(mycipher(n))

