import os
import fnmatch
import pyperclip

def getScormList():
    # get directory path for scormcontent
    path = "./SCORM/scormcontent"
    x=[]
    
    #search directory for files of .htm or .html
    for file_name in os.listdir(path):
        if fnmatch.fnmatch(file_name, '*.htm*'):
        #output list with directory structure in front of it
            x.append("<file href=\"scormcontent/" + file_name + "\" />")
    x = "\n".join(x)
    pyperclip.copy(x)
    print("new manifest values copied to clipboard")
            

getScormList()
