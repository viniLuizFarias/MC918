import subprocess
import os
import time

import numpy as np
import matplotlib.pyplot as plt


def solToInfo(filePath):
    logPath = filePath.replace(".sol",".log")


def getFolderTestsInfo(folder):

    files = os.listdir(folder)
    files.sort()
    info = []
    for fileName in files:
        if fileName[-4:] == ".sol":
            info.append(solToInfo(folder + "/" + fileName))

if __name__ == "__main__":

    title_text = 'Country vs Population over the years'
    fig_background_color = 'white'
    fig_border = 'skyblue'
    data =  [
                [         'India', 'China', 'Russia', 'USA', 'Australia'],
                [ '1980',  696828385,982372466,  138257420,  223140018,  14706322],
                ['1990',  870452165, 1153704252,  148005704,   248083732, 17048003],
                ['2000',  1059633675,  1264099069,  146844839,  282398554, 19017963],
                ['2010',  1240613620,  1348191368,  143242599,  311182845, 22019168],
                ['2020', 1396387127, 1424929781, 145617329,  335942003,  25670051],
            ]
    #the headers from the data array
    column_headers = ["Name","|V|","|E|","|T|","DC","Sol","Time","isOpt"]
    row_headers = [x.pop(0) for x in data]

    cell_text = []
    for sFolder in subfolders:
        currentFolder = "instancias/" + sFolder

    for row in data:
        cell_text.append([f'{x/1000:1.1f}' for x in row])

    assert len(cell_text[0] == len(column_headers))


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
    print("AA")
    # Creating the image. plt.savefig ignores the edge and face colors, so we need to map them.
    fig = plt.gcf()
    plt.savefig('pyplot-table-demo.png',
                #bbox='tight',
                edgecolor=fig.get_edgecolor(),
                facecolor=fig.get_facecolor(),
                dpi=150
                )