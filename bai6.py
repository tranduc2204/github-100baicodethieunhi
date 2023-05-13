s = input()
isalnum= isalpha=isdigit=islower=isupper = False
for ch in s:
    if ch.isalnum() == True:
        isalnum = True
    if ch.isalpha() == True:
        isalpha = True
    if ch.isdigit() == True:
        isdigit = True
    if ch.islower() == True:
        islower = True
    if ch.isupper() == True:
        isupper = True
        
print(isalnum, isalpha, isdigit, islower, isupper, sep = '\n' )