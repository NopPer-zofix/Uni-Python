import math

def cone_surface_area(r,h):
    return math.pi * r** 2 + math.pi * r * math.sqrt(r**2 + h**2)

def cone_volume(r,h):
    
    return (1/3) * math.pi * r**2 * h


def is_nneg_float(s):
    if not 'e' in s.lower() and s[-1] == '.' or s[0] == '.' or s.count('.') == 0:
        return True
    else:        
        return False

def get_nneg_float(): 
    while(True):
        p = input("input a non-negative float: ")
        if float(p) >= 0 and is_nneg_float(p) is True:
            break
        else:           
            print("Invalid input. Please enter a non-negative float.")
    p = float(p)
    return p

r = get_nneg_float()
h = get_nneg_float()


print(f"Surface Area: {cone_surface_area(r, h):.2f}")
print(f"Volume: {cone_volume(r, h):.2f}")