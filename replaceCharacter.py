import xml.etree.ElementTree as ET
import re

"""
Goes through and replaces all of a user passed in value with a replacement
Proceeds to make changes then update the XMl file

**IMPORTANT**
Make sure this script is located in the root of your project. Not the course folder
This only applies if you are making iPrism courses. 
Explorers will just run as is
"""
def replaceValues(searchTerm=str(),replaceTerm=str()):
    course = ET.parse('./course.xml')
    root = course.getroot()
    

    for x in root.iter('text'):
        # y = x.text
        # fa = re.findall(r'®',str(y))
        if x.text !=None:
            x.text = re.sub(searchTerm,replaceTerm,x.text)
            course.write('course.xml')

userSearch = input("What is the character(s) you are searching for? ")
userReplace = input("What would you like to replace them with? ")

replaceValues(userSearch,userReplace)