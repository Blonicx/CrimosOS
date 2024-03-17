import Ui

def CreateFunc(username, password):
    userInfoFile = open('./OperatingSystem/User/userInfo.json', 'a')
    
    userInfoFile.write(f"""
    {{
        "username" : "{username}",
        "password" : {password}
    }}
    """
    )
    
    Ui.LoginUI()

def LoginFunc(username, password):
    if username and password in "./User/userInfo.json":
        Ui.MainUI()
    else:
        return "UserError"