import subprocess
import os
import time



def runTest(folder,fileName):
    outputFolder = folder.replace("instancias","resultados")
    testPath = folder + "/" + fileName

    logPath = outputFolder + "/" + fileName.replace(".stp",".log")
    print(outputFolder,testPath,logPath)

    output = subprocess.check_output("python3 main.py "+testPath, shell=True)
    file = open(logPath,"w")
    file.write(output.decode())

    solPath = outputFolder + "/" + fileName.replace(".stp",".sol")
    time.sleep(0.5)
    os.rename('solution', solPath)
    time.sleep(0.5)

if __name__ == "__main__":
    subfolders = ["B10"]
    for sFolder in subfolders:
        currentFolder = "instancias/" + sFolder
        files = os.listdir(currentFolder)
        for fileName in files:
            if fileName[-4:] == ".stp":
                print(currentFolder,fileName)
                runTest(currentFolder,fileName)