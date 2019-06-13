numm=int(input())
for i in range(2,numm):
  s=numm%i
  if(s==0):
    print('no')
    break
  else:
    print('yes')
