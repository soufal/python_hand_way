import math

r = float(input("please input the r:"))
def Compute_circle(r):
    peri = 2 * math.pi * r
    area = math.pi * r**2
    print("The peri is: {}".format(peri))
    print("The area is: {}".format(area))

Compute_circle(r)
