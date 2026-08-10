inp = "Sipra is good"
str1 = ""
for i in inp.lower():
    ctr=0
    for j in inp.lower():
        if i==j:
            ctr=ctr+1
    if ctr==1:
        str1 = str1+i
print(str1)


