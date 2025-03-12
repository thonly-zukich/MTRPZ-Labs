import math

def solvequad_supercool(a, b, c):
    if a == 0:
        raise ValueError("'a' cannot be zero.")

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        return ()

if __name__ == "__main__":
    print("This is solver module.")
