# Program to calculate the area of a triangle using Heron's formula


def triangle_area(a, b, c):
    # Calculate the semiperimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
print('The area of the triangle with sides', a, b, c, 'is', triangle_area(a, b, c))


print('The area of a triangle with sides 3, 4, 5 is', triangle_area(3, 4, 5))
print('The area of a triangle with sides 5, 12, 13 is', triangle_area(5, 12, 13))
print('The area of a triangle with sides 7, 24, 25 is', triangle_area(7, 24, 25))