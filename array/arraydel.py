def delete(ar,ind):
  ar2=[0 for _ in range(len(ar)-1)]
  print(ar)
  for i in range(0,ind):
    ar2[i]=ar[i]
  for i in range(ind+1,len(ar)):
    ar2[i-1]=ar[i]
  print(ar2)

a=[1,2,3,4,5]
delete(a,2)