import clipboard

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
iconTypes = {
    "cc": "'clinicalConcept'",
    "cn": "'compNote'",
    "dn": "'dosingNote'",
    "en": "'efficacyNote'",
    "kp": "'keyPoint'",
    "sn": "'safetyNote'",
    "faq": "'fq'",
    "qf": "'quickFact'",
    "se": "'secondaryEndpoint'",
    "nn": "'note'",
    "oh": "'objectionHandler'",
    "pn": "'penNote'",
    "fn":"'fieldNote",
    "rn":"'resultsNote'",
    "xn":"'xyremNote'"
}

iconList = []
_moduleNumber=0
_sectionNumber=0
_pageNumber=0

def continueDraw(continue_answer):
    global _pageNumber
    
    continue_answer = continue_answer.lower()

    if continue_answer =="n":
        iconList.clear()
        _pageNumber += 1
        setIconValues(_moduleNumber,_sectionNumber,_pageNumber)
    else:
        setGlossaryTerms()

def setIconValues(m,s,p):
    iconNumber = input("How many icons are on the page? ")

    # Loop through equal to number of icons
    x = 0
    if int(p) < 10:
            p = "0"+str(p)
    while x < int(iconNumber):

        # Ask for X value
        xValue = input("What is the X value? ")

        # Ask for Y value
        yValue = input("What is the Y value? ")

        # Ask for W value
        wValue = input("What is the W value? ")

        # Ask for H value
        hValue = input("What is the H value? ")

        # Ask what kind of icon
        iconAbbrev = input("What is the icon abbreviation? ")

        
            

        iconInfo = str(xValue) + "," + str(yValue) + "," + \
            str(wValue) + "," + str(hValue)
        pageInfo = "'{m0" + str(_moduleNumber) + "_s0" + str(_sectionNumber) + \
            "_t" + str(p) + "_" + str(x+1)

        iconComplete = iconInfo + ",showPop(" + pageInfo + ":title}'" + "," + \
            pageInfo + ":text}'," + \
            iconTypes[iconAbbrev] + ")," + iconAbbrev + "|"
        iconList.append(iconComplete)

        x += 1

    print(*iconList, sep="\n")
    _iconList = '\n'.join(iconList);
    
    clipboard.copy(_iconList);
    userContinue = input("Would you like to add glossary terms? ")
    continueDraw(userContinue)    

def setGlossaryTerms():
    iconNumber = input("How many terms are on the page? ")

    # Loop through equal to number of icons
    x = 0
    while x < int(iconNumber):

        # Ask for X value
        xValue = input("What is the X value? ")

        # Ask for Y value
        yValue = input("What is the Y value? ")

        # Ask for W value
        wValue = input("What is the W value? ")

        # Ask for H value
        hValue = input("What is the H value? ")

        # Ask what kind of icon
        iconAbbrev = input("What is the glossary abbreviation? ")

            

        iconInfo = str(xValue) + "," + str(yValue) + "," + \
            str(wValue) + "," + str(hValue)       

        iconComplete = iconInfo + ",showPop('{" + iconAbbrev + ":title}'" + ",'{" + \
            iconAbbrev + ":text}')," + "glossary|"
        iconList.append(iconComplete)

        x += 1

    print(*iconList, sep="\n")
    _iconList = '\n'.join(iconList);
    clipboard.copy(_iconList);
    continueDraw("n")
    

def setPageValues():
    global _pageNumber,_moduleNumber,_sectionNumber
    # Ask what module you are on
    moduleNumber = input("What module number is this? ")
    _moduleNumber = int(moduleNumber)

    # Ask what section you are in
    sectionNumber = input("What section is this? ")
    _sectionNumber = int(sectionNumber)

    # Ask what number you are on
    pageNumber = input("What page number is this? ")   
    _pageNumber = int(pageNumber)

    setIconValues(_moduleNumber,_sectionNumber,pageNumber)
   

setPageValues()