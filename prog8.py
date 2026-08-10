Input= "Sipra is a  girl"

lst2 = []

lst = Input.split()


for i in lst:
    if i[0] not in 'aeiou':
            
            lst2.append(i)
print(' '.join(lst2))







    
