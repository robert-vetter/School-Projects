import sys
import operator
from itertools import permutations
import functools


OPERATIONS = {
    "add": operator.add,
    "mul": operator.mul,
    "sub": operator.sub,
    "div": operator.truediv,
}

SYMBOLS = {
    "add": "+",
    "mul": "*",
    "sub": "-",
    "div": "/",
}


def _get_groupings(nums):
    if len(nums) == 1:
        yield nums[0]
    elif len(nums) == 2:
        yield nums
    else:
        yield from (
            (xx, yy)
            for i in range(1, len(nums))
            for xx in _get_groupings(nums[:i])
            for yy in _get_groupings(nums[i:])
        )


def get_groupings(perms):
    for nums in perms:
        yield from _get_groupings(nums)


def _generate_candidates(nums):
    x, y = nums[0], nums[1]
    if not isinstance(x, tuple) and not isinstance(y, tuple):
        for name in OPERATIONS:
            yield name, x, y
    else:
        x_gens = [x] if not isinstance(x, tuple) else _generate_candidates(x)
        y_gens = [y] if not isinstance(y, tuple) else _generate_candidates(y)
        yield from (
            (name, a, b) for a in x_gens for b in y_gens for name in OPERATIONS
        )


def generate_candidates(numbers):
    all_permutations = (
        x for x in permutations(numbers, len(numbers))
    )

    for g in get_groupings(all_permutations):
        yield from _generate_candidates(g)


@functools.lru_cache()
def compute(candidate):
    name, x, y = candidate
    child_x, child_y = x, y
    child_x = compute(x)[1] if isinstance(x, tuple) else x
    child_y = compute(y)[1] if isinstance(y, tuple) else y
    return candidate, OPERATIONS[name](child_x, child_y)


def get_best_candidates(candidates, final_result):
    counter = 0
    best_candidate, best_result, exact_found = None, 0, False
    for candidate in candidates:
        try:
            n, r = compute(candidate)
        except (ValueError, ZeroDivisionError, TypeError, OverflowError, ArithmeticError):
            continue
        if abs(r - final_result) < abs(best_result - final_result):
            best_candidate, best_result = n, r
        if r == final_result:
            exact_found = True
            counter = counter + 1
            if counter > 1:
                break
            yield r, n
    if not exact_found:
        yield best_result, best_candidate


def parse(candidate, bracket=False):
    name, x, y = candidate
    symbol = SYMBOLS[name]
    child_x = parse(x) if isinstance(x, tuple) else str(x)
    child_y = parse(y) if isinstance(y, tuple) else str(y)
    result = f"{symbol}".join([child_x, child_y])
    if bracket:
        return f"({result})"
    return result

def generate_riddles(input_numbers, target):
    for (x, y) in get_best_candidates(generate_candidates(input_numbers), target):
        print(x, y)
        expr = parse(y, False)
        # print(f"{expr} = {x}")

def evaluate(equation):
    import string
    if not set(equation).intersection(string.ascii_letters + '{}[]_;\n'):
        return eval(equation)
    else:
        return None

if __name__ == "__main__":
    input_numbers = (4, 3, 2, 6, 3, 9, 7, 8, 2, 9, 4, 4, 6, 4, 4, 5)
    target = 4792
    generate_riddles(input_numbers, target)
