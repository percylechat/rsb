import sys

# https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset

def count_different_letters(input):
    unique_letters = set()
    for char in reversed(input):
        if char.isalpha():
            unique_letters.add(char)
    return unique_letters


def powerset_gen(s):
    if not s:
        return [
            []
        ] 
    element = s.pop()
    subsets = powerset_gen(
        s
    ) 
    new_subsets = [subset + [element] for subset in subsets]
    return subsets + new_subsets


def powerset(str_):
    set_ = powerset_gen(list(str_))
    print(set_)
    res = set()
    for elem in set_:
        # temp = frozenset()
        # for el in elem:
        #     temp.add(el)
        res.add(frozenset(elem))
    print(res)
    return res


    
def eval_set(str_, set_):
    variables = count_different_letters(str_)
    variables = list(variables)
    proper_letters = [*set(variables)]
    if len(proper_letters) != len(set_):
        print("fail")
        sys.exit(1)
    megaset = powerset(set_)
    stack = []
    for elem in str_:
        if elem.isalpha():
            stack.append(elem)
        elif elem == "!":
            op1 = stack.pop()
            op2 = megaset - op1
            stack.append(op2)
        elif elem == ">":
            op2 = stack.pop()
            op1 = stack.pop()
            op3 = megaset - op1
            stack.append(op3 | op2)
        elif elem == "=":
            op2 = stack.pop()
            op1 = stack.pop()
            op3 = megaset - op1
            op4 = megaset - op2
            stack.append((op3 | op2) & (op1 | op4) )
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if elem == "|":
                stack.append(op1 | op2)
            else:
                stack.append(op1 & op2)
    return stack[0]


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Please enter 1 string and 'debug' option")
        sys.exit(0)
    # TODO check
    str_ = sys.argv[1]
    set_ = sys.argv[2]
    if len(sys.argv) == 3:
        if sys.argv[2] == "debug":
            conjunctive_normal_form_debug(str_)
    else:
        eval_set(str_, list(set_)
