import ast

fromMorse = {".-": "A",
             "-...": "B",
             "-.-.": "C",
             "-..": "D",
             ".": "E",
             "..-.": "F",
             "--.": "G",
             "....": "H",
             "..": "I",
             ".---": "J",
             "-.-": "K",
             ".-..": "L",
             "--": "M",
             "-.": "N",
             "---": "O",
             ".--.": "P",
             "--.-": "Q",
             ".-.": "R",
             "...": "S",
             "-": "T",
             "..-": "U",
             "...-": "V",
             ".--": "W",
             "-..-": "X",
             "-.--": "Y",
             "--..": "Z",
             ".----": "1",
             "..---": "2",
             "...--": "3",
             "....-": "4",
             ".....": "5",
             "-....": "6",
             "--...": "7",
             "---..": "8",
             "----.": "9",
             "-----": "0"}

toMorse = {" ": " ",
           ".": "  ",
           "A": ".- ",
           "B": "-... ",
           "C": "-.-. ",
           "D": "-.. ",
           "E": ". ",
           "F": "..-. ",
           "G": "--. ",
           "H": ".... ",
           "I": ".. ",
           "J": ".--- ",
           "K": "-.- ",
           "L": ".-.. ",
           "M": "-- ",
           "N": "-. ",
           "O": "--- ",
           "P": ".--. ",
           "Q": "--.- ",
           "R": ".-. ",
           "S": "... ",
           "T": "- ",
           "U": "..- ",
           "V": "...- ",
           "W": ".-- ",
           "X": "-..- ",
           "Y": "-.-- ",
           "Z": "--.. ",
           "1": ".---- ",
           "2": "..--- ",
           "3": "...-- ",
           "4": "....- ",
           "5": "..... ",
           "6": "-.... ",
           "7": "--... ",
           "8": "---.. ",
           "9": "----. ",
           "0": "----- "}

toBaudotL = {b'00011000': "A",
               b'00010011': "B",
               b'00001110': "C",
               b'00010010': "D",
               b'00010000': "E",
               b'00010110': "F",
               b'00001011': "G",
               b'00000101': "H",
               b'00001100': "I",
               b'00011010': "J",
               b'00011110': "K",
               b'00001001': "L",
               b'00000111': "M",
               b'00000110': "N",
               b'00000011': "O",
               b'00001101': "P",
               b'00011101': "Q",
               b'00001010': "R",
               b'00010100': "S",
               b'00000001': "T",
               b'00011100': "U",
               b'00001111': "V",
               b'00011001': "W",
               b'00010111': "X",
               b'00010101': "Y",
               b'00010001': "Z"}

toBaudotF = {b'00011000': "-",
               b'00010011': "?",
               b'00001110': ":",
               b'00010010': "WHO ARE YOU",
               b'00010000': "3",
               b'00010110': "%",
               b'00001011': "@",
               b'00000101': "$",
               b'00001100': "8",
               b'00011010': "BELL",
               b'00011110': "(",
               b'00001001': ")",
               b'00000111': ".",
               b'00000110': ",",
               b'00000011': "9",
               b'00001101': "0",
               b'00011101': "1",
               b'00001010': "4",
               b'00010100': "'",
               b'00000001': "5",
               b'00011100': "7",
               b'00001111': "=",
               b'00011001': "2",
               b'00010111': "/",
               b'00010101': "6",
               b'00010001': "+"}

fromBaudotL = {b'\x01': "T",
               b'\x03': "O",
               b'\x04': " ",
               b'\x05': "H",
               b'\x06': "N",
               b'\x07': "M",
               b'\x09': "L",
               b'\x0a': "R",
               b'\x0b': "G",
               b'\x0c': "I",
               b'\x0d': "P",
               b'\x0e': "C",
               b'\x0f': "V",
               b'\x10': "E",
               b'\x11': "Z",
               b'\x12': "D",
               b'\x13': "B",
               b'\x14': "S",
               b'\x15': "Y",
               b'\x16': "F",
               b'\x17': "X",
               b'\x18': "A",
               b'\x19': "W",
               b'\x1a': "J",
               b'\x1c': "U",
               b'\x1d': "Q",
               b'\x1e': "K"}

fromBaudotF = {b'\x01': "5",
               b'\x03': "9",
               b'\x04': " ",
               b'\x05': ",",
               b'\x06': "$",
               b'\x07': ".",
               b'\x09': ")",
               b'\x0a': "4",
               b'\x0b': "@",
               b'\x0c': "8",
               b'\x0d': "0",
               b'\x0e': ":",
               b'\x0f': "=",
               b'\x10': "3",
               b'\x11': "+",
               b'\x12': "WHO ARE YOU",
               b'\x13': "?",
               b'\x14': "'",
               b'\x15': "6",
               b'\x16': "%",
               b'\x17': "/",
               b'\x18': "-",
               b'\x19': "2",
               b'\x1a': "BELL",
               b'\x1c': "2",
               b'\x1d': "1",
               b'\x1e': "("}
           

def openUTF8(fileName):
    file1 = open(fileName, "r")
    fileData = file1.read()
    file1.close()
    return fileData

def writeUTF8(fileData):
    file2 = open("output.txt", "w")
    file2.writelines(fileData)
    file2.close()
    print("Contents saved to output.txt")
    return

def openMorse(fileName):
    
    file1 = open(fileName, "r")
    fileData = file1.read()
    file1.close()
    currentChar = ""
    newFileData = ""
    spaceCounter = 0
    for i in range(len(fileData)):
        if fileData[i] == " " and spaceCounter == 0:
            j = i
            while (j < len(fileData) and fileData[j] == " "):
                spaceCounter += 1
                j += 1
            if spaceCounter == 1:
                newFileData += fromMorse.get(currentChar)
                currentChar = ""
            elif spaceCounter == 2:
                newFileData += fromMorse.get(currentChar) + " "
                currentChar = ""
            elif spaceCounter == 3:
                newFileData += fromMorse.get(currentChar) + ". "
                currentChar = ""
        elif fileData[i] != " ":
            spaceCounter = 0
            currentChar += fileData[i]
    file1.close() 
    return newFileData

def writeMorse(fileData):
    file2 = open("output.txt", "w")
    newFileData = ""
    for i in range(len(fileData)):
        newFileData += toMorse.get(fileData[i].upper())
    file2.writelines(newFileData)
    file2.close()
    print("Contents saved to output.txt")
    return

def openBaudot(fileName):
    file1 = open(fileName, "rb")
    fileData = file1.read(1)
    newFileData = ""
    readLetters = True
    while fileData:
        if fileData == b'\x1f':
            readLetters = True
        elif fileData == b'\x1b':
            readLetters = False
        else:
            if readLetters == True:
                newFileData += fromBaudotL.get(fileData)
            else:
                newFileData += fromBaudotF.get(fileData)
        fileData = file1.read(1)
    file1.close()
    return newFileData

def writeBaudot(fileData):
    file2 = open("output.txt", "wb")
    writeLetters = True
    for i in fileData:
        if i == " ":
            file2.write(bytes([ast.literal_eval(b'0b00000100'.decode('utf8'))]))
        else:
            for code, char in toBaudotL.items():
                if char == i.upper():
                    if writeLetters == True:
                        file2.write(bytes([ast.literal_eval((b'0b' + code).decode('utf8'))]))
                    else:
                        file2.write(bytes([ast.literal_eval(b'0b00011111'.decode('utf8'))]))
                        file2.write(bytes([ast.literal_eval((b'0b' + code).decode('utf8'))]))
                        writeLetters = True
            for code, char in toBaudotF.items():
                if char == i.upper():
                    if writeLetters == False:
                        file2.write(bytes([ast.literal_eval((b'0b' + code).decode('utf8'))]))
                    else:
                        file2.write(bytes([ast.literal_eval(b'0b00011011'.decode('utf8'))]))
                        file2.write(bytes([ast.literal_eval((b'0b' + code).decode('utf8'))]))
                        writeLetters = False
    file2.close()
    print("Contents saved to output")
    return
    
def openUTF32(fileName):
    file1 = open(fileName, "rb")
    fileData = file1.read()
    newFileData = fileData.decode('utf32')
    file1.close()
    return newFileData

def writeUTF32(fileData):
    file2 = open("output.txt", "wb")
    newFileData = fileData.encode('utf32')
    file2.write(newFileData)
    file2.close()
    print("Contents saved to output.txt")
    return

print("Welcome, please type the number corrisponding to the input type.")
print("1 -> UTF-8")
print("2 -> Morse Code")
print("3 -> Baudot Code")
print("4 -> UTF-32")
inputType = int(input())
print("Thank you, please type the name of your input file including the file extension.\nIt must be contained in the same directory as the Python program.")
fileName = str(input())
print("Thank you, please type the number corrisponding to the output type.")
print("1 -> UTF-8")
print("2 -> Morse Code")
print("3 -> Baudot Code")
print("4 -> UTF-32")
outputType = int(input())

if inputType == 1:
    fileData = openUTF8(fileName)
elif inputType == 2:
    fileData = openMorse(fileName)
elif inputType == 3:
    fileData = openBaudot(fileName)
else:
    fileData = openUTF32(fileName)

print("Data read:")
print(fileData)

if outputType == 1:
    writeUTF8(fileData)
elif outputType == 2:
    writeMorse(fileData)
elif outputType == 3:
    writeBaudot(fileData)
else:
    writeUTF32(fileData)

print("Done.")
