import os
import sys

print("Checking for correct file types ... ", end="")
for filename in os.listdir("./designer"):
    try:
        assert filename[-3:] == ".ui"
    except:
        print("Error: All Files in the designer folder must have .ui extension -> {}".format(filename))
        sys.exit(1)
print("passed")
    
print("Compiling all UI files ... ")
for filename in os.listdir("./designer"):
    pyname = filename[:-3] + ".py"
    
    #compile the temporary file
    os.system("pyuic5 ./designer/{} -o ./compiled/{}.tmp".format(filename, pyname))
    
    #open temporary file for reading and final python file for writing
    tempFile = open("./compiled/{}.tmp".format(pyname),"r")
    pyFile = open("./compiled/{}".format(pyname),"w")
    
    #copy lines and make necessary changes
    for line in tempFile:
        if "from PyQt5 import QtCore, QtGui, QtWidgets" in line:
            pyFile.write("from PySide2 import QtCore, QtGui, QtWidgets\n")
        else:
            pyFile.write(line)
    #close files and delete temp file
    pyFile.close()
    tempFile.close()
    os.system("rm ./compiled/{}.tmp".format(pyname))
    print("{:>20} -> {:<20}".format(filename, pyname))
