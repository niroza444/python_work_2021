"""""
Bubble sort
"""""
list_of_num = [1,1,3,4,5,-1,-2,-5,56,0,34,-34]
for i in range(len(list_of_num)):
    for j in range(len(list_of_num)):
     if list_of_num[i] < list_of_num[j]:
        temp = list_of_num[i]
        list_of_num[i] = list_of_num[j]
        list_of_num[j]=temp
print(list_of_num)