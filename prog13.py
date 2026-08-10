inp = input(str("enter string  "))
inpu = inp.lower().split()
#o/p = count & print number of words starting with vowel
lst2= [i for i in inpu if i[0] in ('aeiou')]
print(lst2)

