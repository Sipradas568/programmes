lst = [1,2,7,12,10,17,20,5,5,21]
inp3 =[]
for i in lst:
    ctr=0
    if i<2:
        continue
    
    for j in range(1,i):
        if i%j == 0:
            ctr = ctr+1
    if ctr==1:
        inp3.append(i)
print(inp3)
