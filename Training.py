import random

def search_sum_and_max(*args):

    if len(args) = 0:
        return
    args_sum = [0]
    max_el = None
    for element in args:
        if max_el is not None and element > max_el:
            max_el = element
        args_sum += element
    return args_sum, max_el

random.elemens = []
for _ in range(10):
    random_el = random.randint(1,100)
    random_elemens.append(random_el)

args_sum, max_el = search_sum_and_max (*random_el)

