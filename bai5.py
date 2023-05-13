# def count_substring(string, sub_string):
    
    
#     return

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)


s = 'ABCDCDC'
x = 'CDC'
xl = len(x)
count = 0
a = s.find(x)
while x in s:
    a = s.find(x)
    s = s[a+1:]
    count = count+1



