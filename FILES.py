#SUBMODULE:FILES

#ACTIONS

def load(filename):
    # print("LOAD FROM FILENAME")
    # print(filename)
    with open(filename, 'r') as file:
	return file.readlines()

def save(filename,data):
    # print("SAVE TO FILENAME")
    # print(filename)
    with open(filename, 'w') as file:
	file.writelines(data)

def loadline(filename,index):
    data = load(filename)
    return data[index]

def saveline(filename,index,text):
    data = load(filename)
    # print("SAVELINE TO FILENAME")
    # print(filename)
    # print("DATA =")
    # print(data)
    data[index] = text + "\n"
    save(filename,data)