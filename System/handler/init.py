import os
import requests

class Setup:
    def checkForSetup():
        if os.path.exists("./Files") == True:
            print("Alredy Setup.")
            return True
        else:
            print("Needing Setup.")
            return False
            
    def setupSystem():
        os.mkdir("./Files")
        pass
    
    def downloadDrivers():
        pass