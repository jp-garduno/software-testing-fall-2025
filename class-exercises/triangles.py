def is_triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return "Yes, it is a triangle!"
    
    return "No, it is not a triangle."

print(is_triangle(3,4,5) == "Yes, it is a triangle!")
print(is_triangle(1,1,3) == "No, it is not a triangle.")
print(is_triangle(-3,-4,-5) == "No, it is not a triangle.")
print(is_triangle(3.2,4.6,5.9) == "Yes, it is a triangle!")
print(is_triangle("a","b","c") == "No, it is not a triangle.")