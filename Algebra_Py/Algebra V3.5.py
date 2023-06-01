from math import sqrt

print("Welcome to my algebra solver\n")
print("! Made by iwannet !")

menu1 = "1: Quadratic solver\n2: Alpha and Beta solver\n3: Display formulas\n4: Credits\n\n"
answer1 = input(menu1)


def choose():
    menu3 = "\n1: Run Again\n2: Exit \n3: Credits\n\n"
    answer3 = input(menu3)
    if answer3 == "1" or answer3 == "2" or answer3 == "3":
        if answer3 == "1": 
            run()
        elif answer3 == "2":  
            exit()
        elif answer3 == "3":
            credits()
            choose()
    else:
        print("\nChose a correct option")
        run()
def quadratic_solver():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))

    # Calculate the discriminant
    D = (b * b) - (4 * a * c)

    if D < 0:
        print("The discriminant is negative. The solutions are complex numbers.")
        real_part = -b / (2 * a)
        imaginary_part = sqrt(-D) / (2 * a)
        print("\nx1 = {} + {}i".format(real_part, imaginary_part))
        print("x2 = {} - {}i".format(real_part, imaginary_part))
    elif D == 0:
        x = -b / (2 * a)
        print("\nx = {}".format(x))
    else:
        square_root_D = sqrt(D)
        two_a = 2 * a
        x1 = (-b + square_root_D) / two_a
        x2 = (-b - square_root_D) / two_a

        print("\nx1 = {}".format(x1))
        print("x2 = {}".format(x2))

    

def alpha_beta_solver():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))

    alpha = (-1 * b) / (2 * a)
    beta = (4 * a * c) + (b * b) / (4 * a)

    print("alpha = {}".format(alpha))
    print("beta = {}".format(beta))
    print("top = {};{}".format(alpha, beta))
    print("function expression = {}*(x+{})²+{}".format(a, alpha, beta))

    

def quadratic_solver_formule():
    print("\nQuadratic Formula: ax^2 + bx + c = 0")
    print("Discriminant: D = b^2 - 4ac")
    print("x1 = (-b + sqrt(D)) / (2a)")
    print("x2 = (-b - sqrt(D)) / (2a)")

def alpha_beta_solver_formule():
    print("\nAlpha and Beta Solver formules:")
    print("alpha = (-b) / (2a)")
    print("beta = (4ac + b^2) / (4a)")
    print("Function Expression: a * (x + alpha)^2 + beta")
    
def display_formulas():

    menu2 = "1: Quadratic solver Formule\n2: Alpha and Beta solver formule\n"
    answer2 = input(menu2)
    if answer2 == "1" or answer2 == "2":
        if answer2 == "1": 
            quadratic_solver_formule() 
            input("Press ENTER to exit")
            choose()
        if answer2 == "2":  
            alpha_beta_solver_formule() 
            input("Press ENTER to exit")
            choose()
        else:
            print("Chose a correct option")
            run()


    

def credits():
    try:
        print("\033[34m" + "\033[1m" + "Credits:\nMade by iwannet -> www.iwannet.cc \033[0m")
    except:
        print("Credits:\nMade by iwannet -> www.iwannet.cc")



def run():
    if answer1 == "1" or answer1 == "2" or answer1 == "3" or answer1 == "4":
        if answer1 == "1": 
            quadratic_solver() 
            input("\nPress ENTER to continue")
            choose()
        if answer1 == "2":  
            alpha_beta_solver() 
            input("\nPress ENTER to continue")
            choose()
        if answer1 == "3": 
            display_formulas() 
            input("\nPress ENTER to continue")
            choose()
        if answer1 == "4":  
            credits() 
            input("\nPress ENTER to continue")
            choose()
    
    else:
        print("\nChose a correct option")
        run()


run()
    

