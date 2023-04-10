list_of_cloud_serv = list(["aws","azure","gcp"])
list_of_envs = ["dev","stg","prod","test","qa"]
list_of_envs.append("client")
for i in list_of_envs:
    print("deploying to", i)
    
a = 2
list_of_envs.insert(1,"testing")
print(list_of_envs)

print(a.denominator.__doc__)