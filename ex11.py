import sys


def reverse_map(nbr):
    # check que int16 bits
    if nbr < 0 or nbr > 1:
        print("error, invalid number")
        sys.exit(1)
    if nbr == 0:
        return 0, 1
    nbr1 = nbr * 1000000
    return nbr1 / 2, (nbr1 / 2) + 1


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
        reverse_map(nbr1)
