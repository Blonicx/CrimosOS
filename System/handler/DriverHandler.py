import subprocess

def StartDriver(Name):
    subprocess.call(f"python Driver/{Name}.cos")