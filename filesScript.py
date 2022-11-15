import plistlib

def creatKeysList(filename, keyName):
    fileKeys = list()

    with open(filename, 'rb') as fp:
        pl = plistlib.load(fp)
    
    for key in pl[keyName]:
        fileKeys.append(key)

    return fileKeys

def createLangCodesList(filename, fileKeys):
    listOfLists = list()

    with open(filename, 'rb') as fp:
        pl = plistlib.load(fp)

    for key in fileKeys:
        for langCode in pl["localisations"][key]:
            listOfLists.append({key: langCode})
    
    return listOfLists

def keysAdded(fileKeysA, fileKeysB):
    for key in fileKeysB:
        if(key not in fileKeysA):
            print(key)

def keysRemoved(fileKeysA, fileKeysB):
    for key in fileKeysA:
        if(key not in fileKeysB):
            print(key)
    

def main():
    fileKeysA = creatKeysList("localisations_1_2_0.plist", "localisations")
    fileKeysB = creatKeysList("localisations_1_2_1.plist", "localisations")

    print("++++++++++++++++++++++++++++++++++++++++++")
    print("B1.1")
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("keys added: ")
    keysAdded(fileKeysA, fileKeysB)
    print("++++++++++++++++++++++++++++++++++++++++++")

    print("B1.2")
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("keys removed: ")
    keysRemoved(fileKeysA, fileKeysB)
    print("++++++++++++++++++++++++++++++++++++++++++")

    listOfListsA = createLangCodesList("localisations_1_2_0.plist", fileKeysA)
    listOfListsB = createLangCodesList("localisations_1_2_1.plist", fileKeysB)

    print("B1.3")
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("language codes added: ")
    keysAdded(listOfListsA, listOfListsB)
    print("++++++++++++++++++++++++++++++++++++++++++")

    print("B1.4")
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("language codes removed: ")
    keysRemoved(listOfListsA, listOfListsB)
    print("++++++++++++++++++++++++++++++++++++++++++")

    print("B1.5")
    print("++++++++++++++++++++++++++++++++++++++++++")


if __name__ == '__main__':
   main()