"""
Regular Expression for extracting email_ids"""
#pypi we can install import packages additionally
# print(dir(re)) we can check all class of re
#print(re.findall.__doc__) we can check how to use that particular class
import re
Text = """
This alert service notifies Niravoza444@gmail.com and mahadev1218@gmail.com also to oza.aro@gmail.com"""
#dataquest.io gives you cheat sheets of python regular expression
list_of_emails = re.findall("[A-Za-z0-9\.\-+_]+@+[a-z0-9\.\-+_]+.+[a-z0-9\.\-+_]",Text)
print(list_of_emails)