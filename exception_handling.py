import builtins
cloud_envs = ["aws","azure","gcp"]
#theory 1
try:
    print(cloud_envs[4])
    raise Exception("This is a new exception added by developer")
except: #theory 2
    print("exception handled")
finally: #theory 3
    print("I will excecute this anyways")

#theory 4
print("this code should run")
#theory 5
try:
    print(cloud_envs[200])
    a = 10
    b = 0
    c = a/b
except ZeroDivisionError as e:
    print("1",e)
except IndexError as e:
    print("2",e)
#theory 6
print(dir(builtins))