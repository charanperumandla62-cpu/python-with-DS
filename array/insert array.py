def insertElement(ar,el,ind):
    ar2=[0 for i in range(len(ar)+1)]
    for i in range(ind):
        ar2[i]=ar[i]
    ar2[ind]=el
    for i in range(ind,len(ar)):
        ar2[i+1]=ar[i]
    return ar2