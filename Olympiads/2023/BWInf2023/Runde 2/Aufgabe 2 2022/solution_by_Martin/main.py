from random import choices
from random import randrange


def equation(num):
    operator_arr = []
    for x in range(num):
        operator_arr.append(choices(['+', '-', '*', '/']))

    operand_arr = []
    for x in range(num + 1):
        operand_arr.append(randrange(1, 10))

    task_full = []
    for x in range(num + 1):
        task_full.append(operand_arr[x])
        if x != num: task_full.append(str(operator_arr[x])[2:-2])

    task_full = ''.join(map(str, task_full))
    print(task_full)
    return task_full


if __name__ == "__main__":

    while True:
        num = int(input("Number of operators: "))

        task_full = equation(num)

        while True:
            if float(eval(task_full)).is_integer() and eval(task_full) >= 0:
                res = eval(task_full)
                print(f"{task_full} = {res:.0f}")

                str_to_replace = {'+': ' o ',
                                  '-': ' o ',
                                  '*': ' o ',
                                  '/': ' o '}

                print(f"{task_full.translate(str.maketrans(str_to_replace))} = {res:.0f}")
                break
            else:
                task_full = equation(num)
