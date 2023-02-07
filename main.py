n=int(input())
k=int(input())
factors=[]
for i in range (n):
    if(n%(i+1)==0):
        factors.append(i+1)
        print(i)
#print(k)
#print(i)
if k>len(factors):
    print(i)
else:
    print(factors[-k])
