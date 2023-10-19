python3 ex05.py "AB&!"
echo "expected A!B!|"

# python3 ex05.py "AB|!"
# echo "expected A!B!&"

# python3 ex05.py "AB>"
# echo "expected A!B|"

# python3 ex05.py "AB="
# echo "expected AB&A!B!&|"

# python3 ex05.py "AB|C&!"
# echo "expected A!B!&C!|"


# // println!("{}", negation_normal_form(" AB& ! "));
# // A!B!|
# println!("{}", negation_normal_form("AB|!"));
# // A!B!&
# println!("{}", negation_normal_form("AB>"));
# // A!B|
# println!("{}", negation_normal_form("AB="));
# // AB&A!B!&|
# println!("{}", negation_normal_form("AB|C&!"));
# // A!B!&C!|