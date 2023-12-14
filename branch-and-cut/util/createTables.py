import subprocess
import os
import time
import networkx as nx
import re


import numpy as np
import matplotlib.pyplot as plt
from steiner import stpToGraph

def testToInfo(stpPath,logPath,solPath):
    
    stpFile = open(stpPath,"r")
    logFile = open(logPath,"r")
    solFile = open(solPath,"r")

    info = []

    graph = stpToGraph(stpFile)
    info += [len(graph.nodes),len(graph.edges),len(graph._sSet)]

    info.append(solFile.readline()[:-1])


    text = logFile.read()

    reExpr = re.compile(r'in ([+-]?([0-9]*[.])?[0-9]+) seconds ')
    result = reExpr.search(text)
    info.append(result.group(1))
    
    reExpr = re.compile(r'Optimal solution found ')
    if reExpr.search(text):
        info.append('yes')
    else:
        info.append('no')
    return info


def getTestsInfo(insFolder,resFolder):
    info = []


    files = os.listdir(insFolder)
    files.sort()
    for fileName in files:
        if fileName[-4:] == ".stp":
            stpPath = insFolder + "/" + fileName
            logPath = resFolder + "/" + fileName.replace(".stp",".log")
            solPath = logPath.replace(".log",".sol")

            cInfo = [fileName[:-4]]
            cInfo += testToInfo(stpPath,logPath,solPath)
            info.append(cInfo)

    print(info)
    return info


if __name__ == "__main__":

    fig_background_color = 'white'
    fig_border = 'skyblue'

    column_headers = ["|V|","|E|","|T|","Sol","Time","isOpt"]


    folders = ["instancias","resultados"]
    subfolders = ["B10"]

    for sFolder in subfolders:
        title_text = 'resultados testset ' + sFolder

        insFolder = folders[0] +"/"+ sFolder
        resFolder = folders[1] +"/"+ sFolder
        data = getTestsInfo(insFolder,resFolder)

        row_headers = [test.pop(0) for test in data]
        print(row_headers)

        cell_text = data

        print(len(cell_text[0]),len(column_headers))


        rcolors = plt.cm.BuPu(np.full(len(row_headers), 0.1))
        ccolors = plt.cm.BuPu(np.full(len(column_headers), 0.1))

        #Creating the figure. Setting a small pad on the tight layout

        plt.figure(linewidth=2,
                edgecolor=fig_border,
                facecolor=fig_background_color,
                tight_layout={'pad':1})

        #Adding a table at the bottom of the axes

        the_table = plt.table(cellText=cell_text,
                            rowLabels=row_headers,
                            rowColours=rcolors,
                            rowLoc='right',
                            colColours=ccolors,
                            colLabels=column_headers,
                            loc='center')

        # Scaling influences the top and bottom cell padding.
        the_table.scale(1, 1.5)

        # Hiding axes
        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Hiding axes border
        plt.box(on=None)

        plt.suptitle(title_text)

        # Without plt.draw() here, the title will center on the axes and not the figure.
        plt.draw()
        # Creating the image. plt.savefig ignores the edge and face colors, so we need to map them.
        fig = plt.gcf()
        plt.savefig(sFolder + '.png',
                    #bbox='tight',
                    edgecolor=fig.get_edgecolor(),
                    facecolor=fig.get_facecolor(),
                    dpi=150
                    )