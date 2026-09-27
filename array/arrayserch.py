def search(ar,el):
    for i in range(len(ar)):
        if ar[i]==el:
           print(f"Element {ar[i]} is found at index {i}")
           return
    print('Element not found')
  
a=[1,2,3,4,5]
search(a,4)