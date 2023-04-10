list_of_cloud = ["aws","azure","gcp","oracle"]
list_of_env = ["dev","test","prod"]


#list iteration
for cloud in list_of_cloud:
    if cloud == "aws":
        print("aws is the best")
#dictionary
dict_of_cloud = {
    "aws":"Amazon web services",
    "azure":"Microsoft Azure",
    "gcp":"Google Cloud Platform",
}
print(dict_of_cloud.get("aws","not found"))
dict_of_cloud.update({"linode":"linode cloude"})

print(dict_of_cloud)