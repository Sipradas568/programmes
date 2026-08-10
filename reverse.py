inp = [2,1,1,1,1,2]
inp2 = []
for i in inp[::-1]:
    inp2.append(i)
print(inp2)
if inp == inp2:
    print("pallindrome")
else:
    print("not pallindrome")