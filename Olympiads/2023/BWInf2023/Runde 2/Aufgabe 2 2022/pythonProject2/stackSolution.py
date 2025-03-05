add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if a % b == 0 else 0 / 0

operations = [(add, '+'),
              (sub, '-'),
              (mul, '*'),
              (div, '/')]


def sumOfStack(stack):
    try:
        total = 0
        lastOper = add
        for item in stack:
            if type(item) is int:
                total = lastOper(total, item)
            else:
                lastOper = item[0]

        return total
    except:
        return 0



def ReprStack(stack):
    reps = [str(item) if type(item) is int else item[1] for item in stack]
    return ''.join(reps)


def Solve(target, numbers):
    def Recurse(stack, nums):
        for n in range(len(nums)):
            stack.append(nums[n])

            remaining = nums[:n] + nums[n + 1:]

            # Überprüfung, ob Stack == target
            x = eval(str(ReprStack(stack)))
            if x == target:
                print(ReprStack(stack))

            if len(remaining) > 0:
                for op in operations:
                    stack.append(op)
                    stack = Recurse(stack, remaining)

                    # letzten Charakter wegnehmen
                    stack = stack[:-1]

            stack = stack[:-1]
            return stack

    Recurse([], numbers)


target = 87

numbers = [9, 1, 4, 7, 8, 4, 1, 3, 5, 5, 2, 8, 6, 8, 2, 6, 1, 1, 6]

print("Target: {0} using {1}".format(target, numbers))

Solve(target, numbers)


