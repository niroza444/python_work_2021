dict_of_item_1 = {
    "env":"dev",
    "server":"aws linux2",
    "ram": 1024,
    "cpu":4,
    "active":True
}
dict_of_item_2 = {
    "env":"prd",
    "server":"aws linux2",
    "ram":2048,
    "cpu":8,
    "active":False
}

env_details = [dict_of_item_1,dict_of_item_2]
for env in env_details:
    for key,value in env.items():
        if key == "active" and value:
            print(env.values())