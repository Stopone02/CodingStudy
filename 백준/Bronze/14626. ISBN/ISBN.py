isbn = list(input())

isbn_sum = 0
for i in range(0, len(isbn)-1):
    if isbn[i] != '*':
        if (i+1)%2 == 1:
            num = int(isbn[i])
        else:
            num = int(isbn[i])*3
        isbn_sum += num
    else:
        if (i+1)%2 == 1:
            weight = 1
        else:
            weight = 3

m = int(isbn[-1])

for i in range(0, 10):
    if (isbn_sum + weight*i + m)%10 == 0:
        print(i)