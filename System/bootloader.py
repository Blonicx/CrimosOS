from kernel import _start_
import handler.init as init

print("Checking for Setup...")

if(init.checkForSetup()):
    pass
else:
    init.setupSystem()

print("Booting up...")

_start_()