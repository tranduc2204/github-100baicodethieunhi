N = int(input())

li = []
li.insert(0,5)
li.insert(1,10)
li.insert(0,6)
print (li)
for i in range (len(li)):
    if li[i] % 2 == 0:
        li.remove(li[i])
        break
    
print (li)




