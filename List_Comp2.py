#even no
n = int(input())
lst = list(range(1,n+1))
lst2 = [i for i in lst if i%2==0]
print(lst2)