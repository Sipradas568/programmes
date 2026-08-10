inp = [-3,-27888888,100,9,-2,10,1000,20000,1,2,0,-10]
max = 0
min = 0


for i in inp:
    if i >max:
        max = i
    if i< min:
        min = i
print(max,min)

for i in range(len(inp)-1):
    for j in range(len(inp)-1):

       if inp[j]>inp[j+1]:
           inp[j],inp[j+1]= inp[j+1],inp[j]
    

print(inp)
