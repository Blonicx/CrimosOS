## Imports ##
import os
import sys
import time

## Custom ##
from kernel import _start_
import handler.init as init

print("Checking for Setup...")

if(init.Setup.checkForSetup()):
    pass
else:
    init.Setup.setupSystem()
    
    time.sleep(1)
    os.execv(sys.executable, ['python'] + [__file__])

print("Booting up...")

_start_()