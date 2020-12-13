import os


def showContent(content, count=0):
    #pass directory path. Its content will be listed
    dirContent = os.listdir(content)
    i = count
    tabString = ""
    while i !=0:
        tabString += "\t"
        i=i-1    
    for item in dirContent:
        print(tabString + item)
        if os.path.isdir(content + "//" + item):
            showContent(content + "//" + item,count+1)


if __name__ == "__main__":
    dirPath = os.path.dirname(os.path.realpath(__file__)) #directory with this python file
    showContent(dirPath)
