def myFunction( *paramètres ):
    myList = []

    for param in paramètres:
        if isinstance(param,(int)):
            myList.append(param)
            myList.sort()
    print(myList)

myFunction(2,84,33,45,5,21,12)