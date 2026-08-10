#remove duplicates
s = "automationa"
lst2= []
for i in s:
    ctr =0
    if i not in lst2:

        for j in s:
            if i == j:
                ctr=ctr+1
    if ctr==1:
        lst2.append(i)
print(''.join(lst2))

