list_of_env = ["dev","stg","prd","tst","qa","qa","dev"]
key = "testing"
is_found = False
for env in list_of_env:
    if env == key:
        is_found = True
if is_found:
    print("Found")
else:
    print("Not found")