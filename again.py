inp = "Sipra DasI"

lst = []
for i in inp.lower():
    ctr= 0
    if i not in lst:
        for j in inp.lower():
            if i ==j:
                ctr= ctr+1
        if ctr >=2:
            lst.append(i)
            print(f"{i} is {ctr}")

        

        