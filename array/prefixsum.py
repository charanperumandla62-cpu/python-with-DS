def prefixsum(a):
  ar=[0 for _ in range(len(a))]
  sum=0
  for i in range(len(a)):
    sum=sum+a[1]
    ar[i]=sum

  return ar

a=(3,1,4,1,5,9,2,6)
print(prefixsum(a))