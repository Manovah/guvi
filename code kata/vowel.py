x=input()
z=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
y=['a','e','i','o','u']
if (x in z):
  if(x in y):
    print('Vowel')
  else:
    print('Consonant')
else:
  print('invalid')
