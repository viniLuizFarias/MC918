import subprocess
import os


def runTest(testPath):
    logPath = testPath.replace(".stp",".log")
    output = subprocess.check_output("python3 steiner.py "+testPath, shell=True)
    file = open(logPath,"w")
    file.write(output.decode())

if __name__ == "__main__":
    subfolders = ["C"]
    for sFolder in subfolders:
        currentFolder = "instancias/" + sFolder
        files = os.listdir(currentFolder)
        for fileName in files:
            if fileName[-4:] == ".stp":
                print(fileName)
                runTest(currentFolder+"/"+fileName)