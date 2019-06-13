numm=int(input())
for i in range(2,numm):
  if(numm%i==0):
    print('no')
    break
else:
  print('yes')
