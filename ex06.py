import sys


def get_list_values(data_structure, temp=[]):
    for item in data_structure:
        if type(item) == list:
            temp = get_list_values(item, temp)

        else:
            temp.append(item)

    return temp


def applyNegation(str_):
    stack = []
    temp = ""

    for c in str_:
        print(c, str_)
        if c.isalpha():
            if len(stack):
                stack.append(stack.pop() + c + "!")
            else:
                stack.append(c + "!")
        elif c == "!":
            temp = stack.pop()
            stack.append(temp[:-1])
            print(stack)
        elif c == "&":
            temp = stack.pop()
            stack.append(temp + "|")
        elif c == "|":
            temp = stack.pop()
            stack.append(temp + "&")
        else:
            break
    return stack[0]


def rewriteFormula(str_):
    stack = []
    for elem in str_:
        if elem.isalpha():
            stack.append(elem)
        elif elem == "!":
            op1 = stack.pop()
            stack.append(op1 + "!")
        elif elem == "^":
            # XOR(a, b) = (a AND NOT b) OR (NOT a AND b)
            # AB|A!B!|& ((A OR B) OR NOT A) AND NOT B
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 + op2 + "|" + op1 + "!" + op2 + "!|&")
        elif elem == ">":
            # (A ⇒ B) ⇔ (¬A ∨ B)
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 + "!" + op2 + "|")
        elif elem == "=":
            # (A ⇔ B) ⇔ ((A ⇒ B) ∧ (B ⇒ A))
            # ((A ⇒ B) ∧ (B ⇒ A)) = ((¬A ∨ B) ∧ (¬B ∨ A))
            # B!A|BA!|& (NOT B OR A) OR B)AND NOT A)
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 + "!" + op2 + "|" + op1 + op2 + "!|&")
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 + op2 + elem)
    return stack[0]


def conjunctive_normal_form(nstr_):
    stack = []

    str_ = rewriteFormula(nstr_)
    # str_ = get_list_values(str__)
    print(str_)
    toadd = 0
    for c in str_:
        if c.isalpha():
            stack.append(c)
        elif c == "!":
            temp = stack.pop()
            stack.append(applyNegation(temp, toadd))
        # elif c == "&" or c == "|":
        elif c == "|":
            temp = stack.pop()
            temp2 = stack.pop()
            stack.append(temp2 + temp + c)
        elif c == "&":
            temp = stack.pop()
            temp2 = stack.pop()
            stack.append(temp2 + temp)
            toadd += 1
        else:
            print("error")
    print("end:", stack[0])
    str_ = stack[0] + "&" * toadd
    print(str_)


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Please enter 1 string and 'debug' option")
        sys.exit(0)
    # TODO check
    str_ = sys.argv[1]
    if len(sys.argv) == 3:
        if sys.argv[2] == "debug":
            conjunctive_normal_form_debug(str_)
    else:
        conjunctive_normal_form(str_)
