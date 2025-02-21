def solution(a, b, n):
    a = int(a)
    b = int(b)
    n = int(n)
    Rest = n
    Get = 0
    
    while Rest >= a:
        sale, rest, total, get = 0, 0, 0, 0
        
        sale = (Rest // a) * a
        rest = Rest % a
        get = (sale // a) * b
        
        Rest = rest + get
        Get += get 
    return Get