def convert_upper(func):
    def wrapper(*args,**kwargs):  # when u write only word it will take only 1 time. but *args used for multiple args
        return func(*args,**kwargs).upper()  # **kwargs is dictionary of parameter we passed
    return wrapper
@convert_upper  # now we used this decorator using @
def show_word(word):
    return word
print(show_word("nir oza"))

def remove_punc(func):
    def wrapper():
        return func().replace(",","")
    return wrapper
@remove_punc
def take_sentence():
    sentence = input("Enter a sentence: ")
    return sentence
print(take_sentence())