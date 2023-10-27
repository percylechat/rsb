import sys


def negation_normal_form(str_: str) -> str:
    stn = standard_notation(str_)
    print('check sn', stn)
    check = "".join(stn)
    print('check join', check)
    temp = infix_to_nnf(check)
    # nnf = neg_form(check)
    return temp

def apply_demorgans(node: list):
    if node[0] == "&":
        return [
            "|",
            apply_demorgans(["!", node[1]]),
            apply_demorgans(["!", node[2]]),
        ]
    elif node[0] == "|":
        return [
            "&",
            apply_demorgans(["!", node[1]]),
            apply_demorgans(["!", node[2]]),
        ]
    elif node[0] == "!":
        if node[1][0] == "&":
            return [
                "|",
                apply_demorgans(["!", node[1][1]]),
                apply_demorgans(["!", node[1][2]]),
            ]
        elif node[1][0] == "|":
            return [
                "&",
                apply_demorgans(["!", node[1][1]]),
                apply_demorgans(["!", node[1][2]]),
            ]
        else:
            return node
    else:
        return node

def infix_to_nnf(tokens):
    # Applique De Morgan's Laws (doubleneg and stuff)
    stack = []
    for token in tokens:
        if token != ")":  # Tant que avant ou dans parenthese
            stack.append(token)
        else:
            sub_expression = []
            while stack and stack[-1] != "(":
                sub_expression.append(stack.pop())
            stack.pop()  # enleve '('
            sub_expression.reverse()
            if len(sub_expression) == 1:  # gere variable unique ou neg
                stack.append(sub_expression[0])
            else:
                print('check1', sub_expression)
                #operator = sub_expression.pop(1)
                print('check2', sub_expression)
                if sub_expression[0] == "!":
                    stack.append(apply_demorgans(["!", sub_expression[1]]))
                else:
                    operator = sub_expression.pop(1)
                    print(operator, sub_expression[0], sub_expression[1])
                    stack.append(
                        apply_demorgans(
                            [operator, sub_expression[0], sub_expression[1]]
                        )
                    )

    nnf_expression = "".join(map(str, stack))
    print(nnf_expression)
    return nnf_expression


def standard_notation(str_):
    #converts RPN into standard notation ie simplify and 
    #puts parenthesis and ! before formula
    stack = []
    for elem in str_:
        if elem.isalpha():
            stack.append(elem)
        elif elem == "!":
            op1 = stack.pop()
            stack.append("(!" + op1 + ")")
        elif elem == "^":
            # XOR(a, b) = (a AND NOT b) OR (NOT a AND b)
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(
                "("
                + str(op1)
                + "&(!"
                + str(op2)
                + "))|((!"
                + str(op1)
                + ")&"
                + str(op2)
                + ")"
            )
        elif elem == ">":
            # (A ⇒ B) ⇔ (¬A ∨ B)
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append("((!" + str(op1) + ")|" + str(op2) + ")")
        elif elem == "=":
            # (A ⇔ B) ⇔ ((A ⇒ B) ∧ (B ⇒ A))
            # ((A ⇒ B) ∧ (B ⇒ A)) = ((¬A ∨ B) ∧ (¬B ∨ A))
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(
                "((!"
                + str(op1)
                + ")|"
                + str(op2)
                + ")&((!"
                + str(op2)
                + ")|"
                + str(op1)
                + ")"
            )
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append("(" + str(op1) + elem + str(op2) + ")")
    # print(stack)
    return stack


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please enter 1 string. beware with exclamation point")
        sys.exit(0)
    str_ = sys.argv[1]
    negation_normal_form(str_)
