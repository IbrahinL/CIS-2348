# a-f are the inputs for the equation
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
solution_found = False
# the ranges of X and Y
for x in range(-10, 11):
    for y in range(-10, 11):
        # the equations
        if a * x + b * y == c and d * x + e * y == f:
            solution_found = True
            x_solution = x
            y_solution = y
            # if statement is found true then the solution found will print
            if solution_found:
                print(x_solution, y_solution)
                break
# if the two equations don't equal then it will print
if not solution_found:
    print('No solution')