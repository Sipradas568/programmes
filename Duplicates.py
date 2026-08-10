inp = "Sipra DasR"
inp2 = inp.lower()
inp3 =[]
for i in inp2:
    ctr = 0
    if i not in inp3:
         for j in inp2:
            if i ==j:
                ctr= ctr + 1

         if ctr>= 2:
            inp3.append(i)
print("Duplicate occurrence", inp3)

    
   

