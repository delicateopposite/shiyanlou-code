for i in range(101):
    if i%7==0:
        continue
    flag = False
    for c in str(i):
        if c=='7':
            flag = True
            break
    if flag == True:
        continue
    print(i)
