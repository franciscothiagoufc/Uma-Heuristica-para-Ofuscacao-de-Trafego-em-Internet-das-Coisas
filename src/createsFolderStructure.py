"""
Creates the folder structure where the files generated by padding strategies are stored. 
"""
import os

rootFolder = "../Data"

def createGroundTruthFolder():
    os.makedirs(os.path.join(rootFolder, "Processed", "groundTruthFeatures"))

def createExistingPaddingFolder():
    for folder in ["Exponential", "Linear", "Mouse_elephant", "MTU", "Random", "Random255"]:
        os.makedirs(os.path.join(rootFolder, "Processed", "PaddingData", "Existing", folder))
        os.makedirs(os.path.join(rootFolder, "Processed", "paddingFeatures", folder))

def createProposalPaddingFolder():
    for folder in ["100", "500", "700", "900"]:
        os.makedirs(os.path.join(rootFolder, "Processed", "PaddingData", "Proposal", folder))
        os.makedirs(os.path.join(rootFolder, "Processed", "paddingFeatures", folder))

if __name__ == "__main__":
    createGroundTruthFolder()
    createExistingPaddingFolder()
    createProposalPaddingFolder()