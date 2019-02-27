import pprint
import json
import re
import os.path
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

#searching and checking for target file_path
def findFile():
    text = input("Which file to use? ")
    print("Searching for " + text + "...")
    if os.path.exists(text):
        print("Successful.")
    else:
        print("Unsuccessful. Please try again.")
        findFile()
    return text

#search for the target team id given a player
def findTeam(file):
    print(file)
    gamedata = open(file)
    # print("Preview: ")
    # print(gamedata.read(50))

    df = pd.read_json(file)
    print(df)
    #df.to_csv()

    name = input("Whose team are you looking for? ")
    print("Looking for " + name + "...")

    #TODO: uncomment when method complete
    #process(df)

#processing the individual data sets, until target team found
def process(file):
    print("process individual data here")

#re-running through the individual data sets and accumulating sets of gmscrs
def gamescore():
    print("get gamescores here")

#run the code here in main
def main():
    gamedata = findFile()
    findTeam(gamedata)

main()
