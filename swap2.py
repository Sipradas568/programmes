inp =[2,100,3,200]
n = len(inp)
#op = [200,100,3,2]
temp = inp[0]
inp[0]= inp[n-1]
inp[n-1]= temp
print(inp)