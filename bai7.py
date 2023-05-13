


# number = (5, 10, 15, 20)
# # strr = "lambda "+
# # print (strr)

# result = list(map(lambda x: x, number))

# print(result)

# x, k = map(int, input().split())
# string = input()
# if eval(string) ==k:
#     print(True)
# else:
#     print (False)

inputs = input().split()
print (inputs)
x = int(inputs[0])
k = int(inputs[1])
statement = input()
statement = statement.replace("x", str(x))
print(eval(statement) == k)