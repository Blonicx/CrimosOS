import os
import subprocess

addonsFolder = "./Addons"

def checkForInstalation(AddonName):
    if os.path.exists(os.path.join(addonsFolder, AddonName + ".py")) == True:
        return True
    else: print("not existing"); return False
    
def StartAddon(AddonName):
    if checkForInstalation(AddonName) == True:
        subprocess.call("python " + os.path.join(addonsFolder, AddonName + ".py"))
    else: print(AddonName + "not existing.")