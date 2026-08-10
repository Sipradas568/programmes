inp = [10,7,9,1, 2, 0, 11, 1, 3,2,1,10,1,11]
inp2 = []
for i in inp:
    if i not in inp2:
        ctr = 0
        for j in inp:
            if i ==j:
                ctr = ctr+1
        if ctr >=2:
            inp2.append(i)
print(inp2)

    
