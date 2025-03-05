import random
import time
import sys


add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if a % b == 0 else 0 / 0

operations = [(add, '+'),
              (sub, '-'),
              (mul, '*'),
              (div, '/')]

operations_mul = [(mul, '*'),
                  (add, '+'),
                  (sub, '-'),
                  (div, '/')]

res = []


def ReprStack(stack):
    reps = [str(item) if type(item) is int else item[1] for item in stack]
    return ''.join(reps)


def Solve(target, numbers):
    counter = 0

    def Recurse(stack, nums):
        global res
        nonlocal counter
        valid = True
        end = False
        for n in range(len(nums)):
            stack.append(nums[n])
            remaining = nums[:n] + nums[n + 1:]
            pos = [position for position, char in enumerate(stack) if char == operations[3]]
            for j in pos:
                if stack[j - 1] % stack[j + 1] != 0:
                    valid = False

            if valid:
                if len(remaining) == 0:
                    # Überprüfung, ob Stack == target
                    solution_string = str(ReprStack(stack))
                    if eval(solution_string) == target:
                        if not check_float_division(solution_string)[0]:
                            counter += 1
                            res.append(solution_string)
                            if counter > 1:
                                res = []
                                values(number_ops)
                                target_new, numbers_list_new = values(number_ops)
                                Solve(target_new, numbers_list_new)
                else:
                    for op in operations_mul:
                        stack.append(op)
                        stack = Recurse(stack, remaining)
                        stack = stack[:-1]
            else:
                if len(pos) * 2 + 1 == len(stack):
                    end = True
                if counter == 1 and end:
                    print(print_solution(target))
                    sys.exit()
            stack = stack[:-1]
            return stack

    # am Anfang einmalig Methode "Recurse" aufrufen
    Recurse([], numbers)


def simplify_multiplication(solution_string):
    for i in range(len(solution_string)):
        pos_mul = [position for position, char in enumerate(solution_string) if char == '*']
        if solution_string[i] == '*' and len(pos_mul) > 0:
            ersatz = int(solution_string[i - 1]) * int(solution_string[i + 1])
            solution_string_new = solution_string[:i - 1] + solution_string[i + 1:]
            solution_string_new_list = list(solution_string_new)
            solution_string_new_list[i - 1] = str(ersatz)
            solution_string = ''.join(str(x) for x in solution_string_new_list)
        else:
            return solution_string

    return solution_string


def check_float_division(solution_string):
    pos_div = []
    solution_string = simplify_multiplication(solution_string)
    if len(solution_string) > 0:
        for i in range(len(solution_string)):
            pos_div = [position for position, char in enumerate(solution_string) if char == '/']
            if len(pos_div) == 0:
                return False, pos_div
            for j in pos_div:
                if int(solution_string[j - 1]) % int(solution_string[j + 1]) != 0:
                    # Float division
                    return True, pos_div
            else:
                # No float division
                return False, pos_div


def new_equation(number_ops):
    equation = []
    operators = ['+', '-', '*', '/']
    ops = ""
    if number_ops > 1:
        for i in range(number_ops):
            ops = ''.join(random.choices(operators, weights=(4, 4, 4, 4), k=1))
            const = random.randint(1, 9)
            equation.append(const)
            equation.append(ops)
        del equation[-1]
        pos = check_float_division(equation)[1]
        if check_float_division(equation):
            if len(pos) == 0:
                return equation
            for i in pos:
                equation[i] = ops
        else:
            '''for i in pos:
                if equation[i+1] < equation[i-1]:
                    while equation[i-1] % equation[i+1] != 0:
                        equation[i+1] += 1'''
            new_equation(number_ops)
    else:
        print("Keine Lösung mit nur einem Operand möglich")
        sys.exit()
    return equation


def values(number_ops):
    target = 0
    equation = ''
    while target < 1:
        equation = ''.join(str(e) for e in new_equation(number_ops))
        target = eval(equation)
    numbers_list = list(
        map(int, equation.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').split()))
    return target, numbers_list


def print_solution(target):
    equation_encrypted_sol = ''.join(res).replace('+', '○').replace('-', '○').replace('*', '○').replace('/', '○')
    print("Versuchen Sie, aus den Zahlen " + str(equation_encrypted_sol) + " die Zahl " + str(
        target) + " unter ausschließlicher Verwendung von +-*/ zu generieren")
    end_time = time.time()
    print("Dauer: ", end_time - start_time)
    input(
        "Drücken Sie eine beliebige Taste und betätigen sie anschließend 'Enter', um sich das Ergebnis anzeigen zu lassen: ")
    print(''.join(res))


if __name__ == '__main__':
    number_ops = int(input("Wie viele Operatoren sollen kreiert werden? "))
    # number_ops = 10
    target, numbers_list = values(number_ops)
    # target = 590
    # numbers_list = [9, 3, 5, 3, 5, 2, 6, 3, 4, 7]
    start_time = time.time()
    Solve(target, numbers_list)
