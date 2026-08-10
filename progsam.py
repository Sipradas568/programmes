str2 = ''
str3 = ''
dictn = {}
str1 = 'I am Sipra Das'
for i in str1.lower():
        ctr = 0
        if i not in str2 and i != ' ':

            for j in str1.lower():
                if i ==j:
                    ctr = ctr+1
                    str2 = str2+i
            dictn[i]=ctr
print(dictn)
