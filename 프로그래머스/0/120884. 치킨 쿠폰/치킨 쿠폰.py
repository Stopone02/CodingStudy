def solution(chicken):
    service = 0
    coupon = 0
    while True:
        service += chicken//10
        coupon += chicken%10
        if coupon > 10 or coupon == 10:
            service += 1
            coupon -= 9
        chicken //= 10
        print(service, coupon)
        if chicken == 0:
            break
    return service