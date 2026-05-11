import math

def cone_surface_area(r,h):
    return math.pi * r** 2 + math.pi * r * math.sqrt(r**2 + h**2)

def cone_volume(r,h):
    
    return (1/3) * math.pi * r**2 * h


r = float(input("Enter the radius of the cone: ")   )
h = float(input("Enter the height of the cone: ")   )
print(f"Surface Area: {cone_surface_area(r, h):.2f}")
print(f"Volume: {cone_volume(r, h):.2f}")