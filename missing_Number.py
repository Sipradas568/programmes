inp = [1,2,4,5,7,100]
#op = 3 is missing
lst = []
inp2=  range(1,max(inp))
for i in inp2:
    if i not in inp:
        lst.append(i)
print(lst)

        
    
        

