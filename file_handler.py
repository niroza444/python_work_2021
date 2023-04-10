file_obj = open('myfile.txt','a') #open
print(file_obj.write('')) #process (use read or readlines(5) readline etc)
file_obj.close() #close    better to save RAM else it will be keep running if it is heavy programm then gonna use too much ram


#try:
file_obj = open('my_new_file.txt','w') #this is not exist so we add it to try and except
#except:
print(file_obj.write('xyz')) #process (use read or readlines(5) readline etc)
#finally:
file_obj.close()

# r will give error if file not present but w will create a new file and start writing it
