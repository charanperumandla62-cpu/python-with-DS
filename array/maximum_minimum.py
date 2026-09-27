def maximum(a):
  max=a[0]
  for i in a:
    if i>max:
      max=i
  return max
def minimum(a):
  min=a[0]
  for i in a:
    if i<min:
      min=i
  return min

a=[20,2,3,2,4,100,3]
el=2
print(maximum(a))
print(minimum(a))