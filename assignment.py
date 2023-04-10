numbs = 4  #add how many numbs u want to enter
smallest = 2**32  
second_smallest = 2**32


for x in range(numbs):
    list = input('Enter #' + str(x + 1) + ': ')   # list will run till numbs variable value we entered
    if int(list) < smallest:  # then simple math logic
        smallest = int(list)
    elif int(list) >= smallest and int(list) < second_smallest:
        second_smallest = int(list)

print('\n smallest number is ' + str(smallest))
print('\nSecond smallest number is ' + str(second_smallest))  # \n for escape
