
# li1 = []
# li2 = []
# li3 = []
# print ("Nhập vào li1: ")
# for i in range (2):
#     li1.append(int(input ("Nhập số thứ: "+ str(i) + " : ")))
# print ("\nNhập vào li2: ")
# for i in range (2):
#     li2.append(int(input ("Nhập số thứ: "+ str(i) + " : ")))   

# for i in range (len(li1)):
#     for j in range (len(li2)):
#         li3.append(li1[i] * li2[j])
    
    
# for i in range (len(li3)):
#     print (li3[i], end =" ")

from itertools import product
A = input().split()
A = list(map(int, A))
B = input().split()
B = list(map(int, B))
for i in product(A, B):
    print (i, end = " ")