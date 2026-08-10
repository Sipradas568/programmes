inp = "sipra is food sipra food good good sipra"
lst = inp.lower().split()
lst2 =[]

for i in lst:
    
    if i not in lst2:
        ctr=0
        for j in lst:
            if i ==j:
                ctr= ctr+1
        if ctr>=2:
            lst2.append(i)

print(lst2)

    

