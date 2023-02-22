"""
Implements the packet padding proposal presented in the paper "Adaptive Packet Padding Approach for Smart Home Networks: A Tradeoff Between Privacy and Performance".
"""
from random import randint
import os
import glob
import codecs
import json

class invalidPaddingLevel(Exception):
    pass

class optimizedPadding:
    def __init__(self,frames,MTU):
        self.mtu = MTU
        self.paddingTable = dict()
        file = open("Optimization/padding"+str(frames)+".txt")
        lines = file.read().split('\n')
        for i in lines[0:-1]:
            field = i.split(" ")
            self.paddingTable[field[0]] = field[1]

    def padding(self, length):
        
        try:
            self.modification = length
            if length in self.paddingTable.keys():
                self.modification = self.paddingTable[length]
            return self.modification
        except ValueError as e:
            raise e

class Experiment:
    def __init__(self, csvFolder, outputFolder, packetLengthIndex):
        self.csvFolder = csvFolder
        self.outputFolder = outputFolder
        self.packetLengthIndex = packetLengthIndex

    def writeFile(self, line, outputFile):
        """
        Write the line with information for each packet in a text file. 
        """
        with codecs.open(outputFile, "a", "ISO-8859-1") as fileWriter:
            fileWriter.write(line)

    def readFiles(self, paddingExecutor):
        """
        Loads CSV files present in a specific folder. Reads all files present in this folder and applies the specified padding strategy. 
        Each line of a file contains attributes of a packet, such as IP and MAC addresses, transport layer port and length.   
        """
        for filepath in glob.glob(self.csvFolder+"*.csv"):
            filename = os.path.basename(filepath)
            self.inputFile = codecs.open(filepath, "r", "ISO-8859-1")
            self.outputFile = os.path.join(self.outputFolder, f"{filename}.csv")

            self.levelExecutor = paddingExecutor.padding

            for line in self.inputFile.readlines():
                try:
                    self.length = line.split(",")[self.packetLengthIndex].replace('"',"")
                    self.modifiedLength = self.levelExecutor(self.length)
                    line = line.replace(self.length, str(self.modifiedLength))
                    self.writeFile(line, self.outputFile)
                except ValueError:
                    self.writeFile(line, self.outputFile)

class ExperimentConfiration:
	def loadConfiguration(self, filepath):
		return json.load(open(filepath, mode="r"))

if __name__ == "__main__":
    configurationFile = os.path.join("..","Data","Configuration","experimentConfiguration.json")
    experimentConfiration = ExperimentConfiration()
    setup = experimentConfiration.loadConfiguration(configurationFile)

    frames = int(setup["frames"])
    MTU = int(setup["MTU"])
    padding = optimizedPadding(frames,MTU)
    experiment = Experiment("../Data/Raw/", f"../Data/Processed/PaddingData/OptimizedPadding/{frames}", 5)
    experiment.readFiles(padding)
