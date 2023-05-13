
# 5
# 12 9 61 5 14 
#############################################################################chịu
def palindromic(n):
    nlist = list(str(n))
    return str.join('', nlist) == str.join('', reversed(nlist))

input()
numbers = list(map(int, input().split()))

is_palindromic = [palindromic(x) for x in numbers]
is_positive = [x >= 0 for x in numbers]

print(all(is_positive) and any(is_palindromic))

# n = int (input("Nhập vào đi: "))
# numbers = []
# for i in range(n):
#     print ("nhập nhẹ: ")
#     x = input().split()
#     # x = int(input("Nhập số thứ {0}: ".format(i+1)))
#     numbers.append(x)
# print (numbers)
# kq = False
# for i in range (len(numbers)):
#     if numbers[i] > 0:
#         print (numbers[i])
#         kq = True
#     else: 
#         kq = False
#         break

# print (kq)


# n = int (input())
# numbers = []
# for i in range(n):
#     x = int(input())
#     numbers.append(x)
# kq = False
# for i in range (len(numbers)):
#     if numbers[i] > 0:
#         print (numbers[i])
#         kq = True
#     else: 
#         kq = False
#         break
# print (kq)
