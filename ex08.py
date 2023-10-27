import sys
#https://docs.python.org/3.10/library/stdtypes.html#set-types-set-frozenset

def powerset_gen(s: list) -> list:
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


def powerset(set_:set) -> set[frozenset]:
    set__ = powerset_gen(list(set_))
    res = set()
    for elem in set__:
        res.add(frozenset(elem))
    return res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please enter 1 string")
        sys.exit(0)
    str_ = sys.argv[1]
    print(powerset(set(str_)))
