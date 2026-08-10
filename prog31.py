inp = 'sipra das'
st = ''
for i in inp:
    if i not in st and i != ' ':

        c= 0
        for j in inp:
            if i ==j:
                c= c+1
                st = st+i
        print("no of "+i+" "+str(c))

