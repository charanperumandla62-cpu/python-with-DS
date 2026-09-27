def prefixsum(a):
  ar=[0 for _ in range(len(a))]
  sum=0
  for i in range(len(a)):
    sum=sum+a[i]
    ar[i]=sum

  return ar
def rangesum(a,st,en):
  if st==0:
    return a[en]
  return a[en]-a[st-1]

def maxsubarray(a,k,target):
    s=0
    for i in range(k):
      s+=a[i]
    if s==target:
        return a[:k]
    for i in range(k,len(a)):
        s=s+a[i]-a[i-k]
        if s==target:
            return a[i-k+1:i+1]
    return [-1, -1]
            

a=[3,1,4,1,5,9,2,6]
res=prefixsum(a)
print(rangesum(res,0,5))
print(maxsubarray(a,5,10))