str1 = 'abbcabcbb'
max_len = 0
longest = ''
for i in range(len(str1)):
    str3 = ''
    for j in range(i,len(str1)):
        if str1[j] in str3:
            break
        else:
            str3 = str3+str1[j]
            if max_len< len(str3):

                max_len = len(str3)
                longest = str3
                index = i


print(max_len)
print(longest)
print(index)

