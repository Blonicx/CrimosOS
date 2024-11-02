import handler.AdonsHandler as AH

def _start_():
    while True:
        cmd = input()
        
        if cmd.lower() == "Intsall Addons":
            return
        
        elif cmd.lower() == "Webbrowser":
            AH.StartAddon("Webbrowser")