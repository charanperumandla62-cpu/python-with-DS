def rightshift(ar,key):
    ar3=[0 for _ in range(len(ar))]
    ind=2
    for i in range(key,len(ar)):
        ar3[ind]=ar[i]
        ind-=1
    for i in range(key):
        ar3[ind]=ar[i]
        ind-=1
    print(ar3)

a=[1,2,3,4,5]
rightshift(a,3)