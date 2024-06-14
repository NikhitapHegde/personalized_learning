N=int(input("enter the number of planets"))
L=[int(i) for i in input().split()]
K=int(input("enter the position in unsorted list"))
d={}
for i in range (N):
    d[i+1]=L[i]
L.sort()
p=int(d[K]) 
for i in range (N):
    if(L[i]==p):
        print(i+1)
        break;
    

    
    