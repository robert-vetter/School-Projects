import random, itertools as it, time

ops = ["+", "-", "*", "/"]
target = 4792
chosen_nums = [4, 3, 2, 6, 3, 9, 7, 8, 2, 9, 4, 4, 6, 4, 4, 5]
infix = []
sta = []

start_time = time.time()


def ToInfix(postfix, infix, list):
    for i in range(0, len(list)):
        infix.append(postfix[i])
        if len(infix) == len((list) * 2) - 1:
            return infix
        else:
            infix.append(postfix[i + len(list)])


def ListToString(list):
    string = " "
    return (string.join([str(val) for val in list]))


def Worker(ListOfPermutations, op_perms, sta, solutions=0):
    for i in range(0, len(ListOfPermutations)):
        for j in range(0, len(op_perms)):
            postfix = ListOfPermutations[i] + op_perms[j]
            infix_string = ListToString(ToInfix(postfix, infix, ListOfPermutations[i]))
            if (target + 0.0) == (eval(infix_string)):
                if sta != eval(infix_string):
                    print(f'{infix_string} = {eval(infix_string)}')
                    solutions += 1
                    sta = eval(infix_string)

            infix.clear()
    return solutions


'''high_num_amount = int(input("How many high numbers : "))

for i in range(high_num_amount):
    val = high_nums[random.randint(0, len(high_nums) - 1)]
    chosen_nums.append(val)
    high_nums.remove(val)

for i in range(6 - high_num_amount):
    val = low_nums[random.randint(0, len(low_nums) - 1)]
    chosen_nums.append(val)
    low_nums.remove(val)'''

print(f'Target: {target}')
print(f'Using: {chosen_nums}')

for i in range(2, 7):
    list_permutations = it.permutations(chosen_nums, i)
    num_perms = list(list_permutations)

    all_operator_permutations = it.combinations_with_replacement(ops, i - 1)
    op_perms = list(all_operator_permutations)
    print(op_perms)

    solutions = Worker(num_perms, op_perms, sta)

print(f'Solutions found: {str(solutions)}')
print(f'Time Elapsed: {time.strftime("%S", time.gmtime(time.time() - start_time))} seconds')
