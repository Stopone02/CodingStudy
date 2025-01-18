str = input()
new_str = ''
for i in str:
    check = i.isupper()
    if check is True:
        new_str += i.lower()
    else:
        new_str += i.upper()
print(new_str)
