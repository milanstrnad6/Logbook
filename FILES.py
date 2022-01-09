#SUBMODULE:FILES

#ACTIONS

def resetWithData(filename,data):
    with open(filename, 'w') as file:
        file.writelines(data)

def reset(filename):
    data = ""
    with open(filename, 'w') as file:
        file.writelines(data)

def load(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def save(filename,data):
    with open(filename, 'w') as file:
        file.writelines(data)

def append(filename,data):
    currentData = load(filename)
    newData = currentData + data
    save(filename,newData)

def loadline(filename,index):
    data = load(filename)
    return data[index]

def saveline(filename,index,text):
    data = load(filename)
    data[index] = text + "\n"
    save(filename,data)