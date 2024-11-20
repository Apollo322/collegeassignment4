def is_triangle(a,b,c) :
    if a + b > c and a + c > b and b + c > a :
        return "能构成三角形"
    else :
        return"不能构成三角形"
print(is_triangle(3,4,5))

        