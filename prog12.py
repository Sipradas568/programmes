inp = [23,2,2,7,5,3,5,7,6,8,17,9,9,19,3,3,5,9,11,13,12,15,16,17,17,16,16]

#o/p= [3,5,7,9,11,13,15,17]

lst = []
[lst.append(i) for i in inp if i not in lst]

    
       
print(lst)
for i in range(len(lst)-1):
      for j in range(len(lst)-1):
           
        if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]


            

print(lst)
    
        
    


          
        


            



           
        

