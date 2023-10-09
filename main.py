# Jacob Richmond
# INF 601
# MiniProject 2


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import prettyprint
from pathlib import Path

'''

10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt.txt
file which contains all the packages that need installed. You can create this file with the output of pip freeze at the
 terminal prompt.
(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the
 pip requirements.txt, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the
explanations.
'''

# create our directory for the files to be saved in, only if it does not already exist.
try:
    Path("Charts").mkdir()
except FileExistsError:
    pass
    # create empty list for the closing prices of all stocks

data = pd.read_csv('all_mtg_cards.csv', index_col='name')
# potential data: Most popular color, creature type, and word in flavor text
columns = data.columns
# print(columns)
mycolors = list(data['colors'])
colors = {}


def colorConcentration():
    # sets colors as the number of occurences of each card
    for color in mycolors:
        # kill all the nans
        if type(color) != float:

            # ignore these characters
            ignoreList = ['[', ']', "'", ',', ' ']
            # convert string to list
            charlist = list(color)

            # check each character
            for char in charlist:
                # make sure character is not in ignorelist and is upper case
                if not char in ignoreList and char.isupper():
                    # if this color is not in the dictionary, add it
                    if not char in colors:
                        colors[char] = 1
                    else:
                        colors[char] += 1
        '''
        else:
            if color not in colors:
                colors[str(color)] = 1
            else:
                colors[str(color)] += 1
        '''
    print(colors)

    # conversion to pandas frame
    mydata = pd.DataFrame(colors.values(), colors.keys())
    y = colors.values()
    x = colors.keys()

    fig, ax = plt.subplots()
    bar_colors = [(1, 1, 1), 'tab:blue', (0, 0, 0), 'tab:red', 'tab:green']
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7, color=bar_colors)
    ax.set(xlim=(0, 5), xticks=np.arange(0, 5),
           ylim=(13600, 14600), yticks=np.arange(13600, 14600, 100))
    plt.title("Magic: THe gathering Card Colors")
    plt.xlabel('Color')
    plt.ylabel('Count')
    # saves the plot
    savefile = "Charts/MTGColors.png"
    plt.savefig(savefile)
    plt.show()


myTypes = list(data['type'])
basicTypes = dict({})
legendaryTypes = dict({})


def typeConcentration():
    # print(myTypes)
    typeList = ["Enchantment", "Artifact", "Land", "Creature", "Sorcery", "Instant", "Planeswalker"]
    for card in myTypes:
        card = card.split('â€”')[0].strip()
        # if the card is Legendary
        if 'Legendary' not in card:
            for basicType in typeList:
                # if this card falls under a categorey Ive defined
                if basicType in card:
                    # add it to the correct Category
                    if basicType not in basicTypes:
                        basicTypes[basicType] = 1
                    else:
                        basicTypes[basicType] += 1


        else:
            for basicType in typeList:
                if basicType in card:
                    if basicType not in legendaryTypes:
                        legendaryTypes[basicType] = 1
                    else:
                        legendaryTypes[basicType] += 1

    # this shows teh graph for the non-legendary types
    # conversion to pandas frame
    mydata = pd.DataFrame(basicTypes.keys(), basicTypes.values())
    y = basicTypes.values()
    x = basicTypes.keys()

    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(0, len(typeList)), xticks=np.arange(0, len(typeList)),
           ylim=(7000, 31000), yticks=np.arange(7000, 31000, 1000))
    plt.title("Magic: The gathering Non-Legendary Type Distribution")
    plt.xlabel('Creature Type')
    plt.ylabel('Count')
    # saves the plot
    savefile = "Charts/MTGNonLegDist.png"
    plt.savefig(savefile)
    plt.show()

    # this then shows the graph for the legendary types
    mydata = pd.DataFrame(legendaryTypes.keys(), legendaryTypes.values())
    y = legendaryTypes.values()
    x = legendaryTypes.keys()
    bar_colors = ['tab:red', 'tab:blue', 'tab:purple', 'tab:orange', 'tab:green']
    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7, align='center', color=bar_colors)
    # The -1 after the len(typeList) is because there are no legendary instants
    ax.set(xlim=(0, len(typeList) - 1), xticks=np.arange(0, len(typeList) - 1),
           ylim=(0, 6000), yticks=np.arange(0, 6000, 500))

    plt.title("Magic: THe gathering Legendary Type Distribution")
    plt.xlabel('Creature Type')
    plt.ylabel('Count')
    # saves the plot
    savefile = "Charts/MTGLegDist.png"
    plt.savefig(savefile)
    plt.show()


colorConcentration()
typeConcentration()
