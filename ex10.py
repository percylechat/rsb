import sys


def map_(nbr1, nbr2):
    # check que int16 bits
    if nbr1 > 65535 or nbr1 < 0 or nbr2 > 65535 or nbr2 < 0:
        print("error, invalid number")
        sys.exit(1)
    nbr3 = (nbr1 + nbr2) + 1
    nbr4 = nbr3 / 1000000
    return nbr4


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
        map_(int(nbr1), int(nbr2))
