list1  = [2,4,6,10,12]
l2=[]
diff = 0
for i in range(0,len(list1)):
    if (i+1)<len(list1):
        diff =abs(list1[i]-list1[i+1])
        l2.append(diff)
    
print(l2)
for i in range(0,len(list1)):
    if (i+1)<len(l2):
        if l2[i]!=l2[i+1]:
            list1.insert(i+2,list1[i+1]+diff)
            break
    

print(list1)