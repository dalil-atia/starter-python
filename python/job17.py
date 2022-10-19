def myFunction( *paramètres ):
    myList = []

    for param in paramètres:
        if isinstance(param,(int)):
            myList.append(param)

    for element in myList:
        if element % 2 == 0:
            print(element)

myFunction(2,10,33,22,98,45,6)