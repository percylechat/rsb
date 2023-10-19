import sys


def powerset_gen(s):
    if not s:
        return [
            []
        ]  # The power set of an empty set is a set containing only the empty set.

    element = s.pop()  # Choose an element from the set.
    subsets = powerset_gen(
        s
    )  # Recursively find the power set of the remaining elements.

    # For each subset in the current power set, add a new subset that includes the chosen element.
    new_subsets = [subset + [element] for subset in subsets]

    # Combine the current power set with the new subsets.
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
        powerset(str_)
