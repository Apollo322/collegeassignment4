def fb_num(n):
    if n<=0:
        return 0
    elif n==1 :
        return 1
    else:
        return fb_num(n-1)+fb_num(n-2)
print(fb_num(10))    