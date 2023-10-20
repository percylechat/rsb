import sys


def negation_normal_form(str_: str) -> str:
    stn = standard_notation(str_)
    # print(stn)
    check = "".join(stn)
    temp = infix_to_nnf(check)
    # nnf = neg_form(check)
    return temp


def infix_to_nnf(tokens):
    # Helper function to apply De Morgan's Laws
    def apply_demorgans(node):
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
    # Tokenize the expression
    # tokens = expression.split()
    stack = []
    print(tokens)
    for token in tokens:
        if token != ")":  # Tant que avant ou dans parenthese
            stack.append(token)
        else:
            sub_expression = []
            while stack and stack[-1] != "(":
                sub_expression.append(stack.pop())
            stack.pop()  # Pop the '('
            sub_expression.reverse()
            if len(sub_expression) == 1:  # Handle single variable or NOT
                stack.append(sub_expression[0])
            else:
                print(sub_expression)
                operator = sub_expression.pop(1)
                if operator == "!":
                    stack.append(apply_demorgans(["!", sub_expression[0]]))
                else:
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
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Please enter 1 string and 'debug' option")
        sys.exit(0)
    str_ = sys.argv[1]
    if len(sys.argv) == 3:
        if sys.argv[2] == "debug":
            negation_normal_form_debug(str_)
    else:
        negation_normal_form(str_)
