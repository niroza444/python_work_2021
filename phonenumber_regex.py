import re

def catch_numbers(txt):
    ph_regex = re.compile(r"(\+905)?\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})")
    grp = ph_regex.findall(txt)
    for gp in grp:
        print("".join(gp))

catch_numbers("so I need to match +905 123 123 123, also 123 123 123, also +905123123123 and also 123123123. Can you please...etc")