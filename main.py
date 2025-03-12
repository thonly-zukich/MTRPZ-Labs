import math
import sys

def solve_funny_math(alpha, beta, gamma):
    if alpha == 0:
        raise ValueError("Oops! Alpha (a) cannot be zero.")

    discriminant = beta ** 2 - 4 * alpha * gamma  # Дискримінант

    if discriminant > 0:
        root1 = (-beta + math.sqrt(discriminant)) / (2 * alpha)
        root2 = (-beta - math.sqrt(discriminant)) / (2 * alpha)
        return (root1, root2)
    elif discriminant == 0:
        single_root = -beta / (2 * alpha)
        return (single_root,)
    else:
        return ()

def fun_interactive_mode():
    print("🎉 Super Fun Quadratic Equation Solver 🎉")
    print("Equation format: αx^2 + βx + γ = 0")

    while True:
        try:
            alpha = float(input("Enter α (a) = "))
            if alpha == 0:
                print("🚨 Oops! Alpha cannot be zero, try again!")
                continue

            beta = float(input("Enter β (b) = "))
            gamma = float(input("Enter γ (c) = "))

            roots = solve_funny_math(alpha, beta, gamma)

            print(f"Equation is: ({alpha}) x^2 + ({beta}) x + ({gamma}) = 0")

            if len(roots) == 2:
                print("🎉 There are 2 fantastic roots!")
                print(f"✨ Root 1: {roots[0]:.6g}")
                print(f"✨ Root 2: {roots[1]:.6g}")
            elif len(roots) == 1:
                print("⭐ Just 1 unique root!")
                print(f"🦄 Root: {roots[0]:.6g}")
            else:
                print("💨 No real roots this time, sorry!")

            break  # Виходимо після успішного розрахунку
        except ValueError:
            print("🚨 Whoops! That's not a valid number. Try again!")

def file_mode(filename):
    try:
        with open(filename, "r") as f:
            line = f.readline().strip()
            parts = line.split()
            if len(parts) != 3:
                raise ValueError("Invalid file format")
            alpha, beta, gamma = map(float, parts)

            roots = solve_funny_math(alpha, beta, gamma)

            print(f"Equation is: ({alpha}) x^2 + ({beta}) x + ({gamma}) = 0")

            if len(roots) == 2:
                print("🎉 There are 2 fantastic roots!")
                print(f"✨ Root 1: {roots[0]:.6g}")
                print(f"✨ Root 2: {roots[1]:.6g}")
            elif len(roots) == 1:
                print("⭐ Just 1 unique root!")
                print(f"🦄 Root: {roots[0]:.6g}")
            else:
                print("💨 No real roots this time, sorry!")

    except FileNotFoundError:
        print(f"🚨 Error: File '{filename}' not found.")
    except ValueError as e:
        print(f"🚨 Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_mode(sys.argv[1])
    else:
        fun_interactive_mode()
