set_1 = {1,1,1,2,2,2,6,6,6,34,34,56,56,78,68,34,2,1,1}
set_2 = {1,2,2,2,6,6,6,34,39,45,55,6,78,2,1,1}

print(set_1.intersection(set_2))
print(set_1.union(set_2))

list_of_envs = ["dev","stg","prd","tst","qa","qa","dev"]
print(list_of_envs)
list_of_envs = list(set(list_of_envs))
print(list_of_envs)