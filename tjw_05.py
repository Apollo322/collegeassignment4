def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)
a,b=map(int,input("请输入两个数：").split())
print("最小公倍数是：",lcm(a,b))