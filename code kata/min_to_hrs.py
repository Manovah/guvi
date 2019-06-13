q=int(input())
if(q<59):
  print(0,q)
else:
  d=q//60
  b=q%60
  print(d,b)
