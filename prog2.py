name = "sipra DaadI"
name2 = ''
for i in name.lower():
    c=0
    if i not in name2:

        for j in name.lower():
            if i==j:
                c= c+1
        name2 = name2+i
    if c>1:
        
        print(f"{i} : {c}")







    

    