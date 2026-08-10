
inp = "sipra 12sipra 123sipra muni2 si8p7r s s,ss"
lst = inp.split()
lst2 = []
for i in lst:
    valid = False
    for j in i:
        if j>='0' and j<='9':
            valid= True
            break
       
    if valid == False:
        lst2.append(i)
print(lst2)




