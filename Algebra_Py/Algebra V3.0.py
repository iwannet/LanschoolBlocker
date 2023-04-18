from math import sqrt
from fractions import Fraction

print("Welcome to my algebra solver\n")
print("! Made by iwannet !")

menu = "1: Quadratic solver\n2: Alpha and Beta solver\n3: Display formulas\n4: Credits\n\n"
answer = input(menu)

def quadratic_solver():
    print("AX² + BX + C = 0")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))

    # Calculate the discriminant
    D = (b * b) - (4 * a * c)

    if D < 0:
        print("The discriminant is negative. The solutions are complex numbers.")
        real_part = -b / (2 * a)
        imaginary_part = sqrt(-D) / (2 * a)
        solution1 = Fraction(real_part).limit_denominator() + Fraction(imaginary_part).limit_denominator() * 1j
        solution2 = Fraction(real_part).limit_denominator() - Fraction(imaginary_part).limit_denominator() * 1j
        print("\nx1 = " + str(solution1))
        print("x2 = " + str(solution2))
    elif D == 0:
        x = -b / (2 * a)
        print("\nx = " + str(x))
    else:
        square_root_D = sqrt(D)
        two_a = 2 * a
        x1 = (-b + square_root_D) / two_a
        x2 = (-b - square_root_D) / two_a

        print("\nx1 = " + str(Fraction(x1).limit_denominator()))
        print("x2 = " + str(Fraction(x2).limit_denominator()))

    

def alpha_beta_solver():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))

    alpha = (-1 * b) / (2 * a)
    beta = (4 * a * c) + (b * b) / (4 * a)

    print("alpha = " + str(alpha))
    print("beta = " + str(beta))
    print("top = " + str(alpha) + ";" + str(beta))
    print("function expression = " + str(a) + "*(x+" + str(alpha) + ")²+" + str(beta))

    print("\nAlpha and Beta Solver:")
    print("alpha = (-b) / (2a)")
    print("beta = (4ac + b^2) / (4a)")
    print("Function Expression: a * (x + alpha)² + beta")

def display_formulas():
    print("\n\nFormulas Alpha and Beta:")
    print("1. Quadratic Formula: ax² + bx + c = 0")
    print("2. Alpha and Beta Solver: alpha = (-b) / (2a), beta = (4ac + b²) / (4a)")
    print("\n\nFormulas Quadratic solver:")
    print("Quadratic Formula: ax² + bx + c = 0")
    print("Discriminant: D = b² - 4ac")
    print("x1 = (-b + sqrt(D)) / (2a)")
    print("x2 = (-b - sqrt(D)) / (2a)")
    

def credits():
    print("\nCredits:")
    print("Made by iwannet --> www.iwannet.cc")



if answer == "1" or answer == "2" or answer == "3" or answer == "4":
    if answer == "1": 
        quadratic_solver() 
        input("Press ENTER to exit") 
    if answer == "2":  
        alpha_beta_solver() 
        input("Press ENTER to exit")
    if answer == "3": 
        display_formulas() 
        input("Press ENTER to exit") 
    if answer == "4":  
        credits() 
        input("Press ENTER to exit")
    
else:
    print("Chose a correct option") 
    

