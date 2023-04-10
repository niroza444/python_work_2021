import re
msg = "my number is 905-345-7654 and my office number is 305-546-5789"
my_reg_ex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Find all pattern of the string and return a list objects
print(my_reg_ex.findall(msg))
