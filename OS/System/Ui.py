from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
import UserHandler

def MainUI():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("CrimosOS")
    window.show()
    app.exec()

def CreateUserUI():
    ## App ##
    app = QApplication([])
    
    ## Objects ##
    InfoText = QLabel("Create User")
    CreateButton = QPushButton("Create")
    UsernameInput = QLineEdit("Username")
    PasswordInput = QLineEdit("Password")
    
    ## Layout ##
    layout = QVBoxLayout()
    layout.addWidget(InfoText)
    layout.addWidget(UsernameInput)
    layout.addWidget(PasswordInput)
    layout.addWidget(CreateButton)
    
    ## Window ##
    window = QWidget()
    window.setWindowTitle("CrimosOS")
    window.show()
    
    ## Funcs ##
    CreateButton.clicked.connect(UserHandler.CreateFunc(UsernameInput.text, PasswordInput.text))
    
    ## Execute ##
    app.exec()

def LoginUI():
    ## App ##
    app = QApplication([])
    
    ## Objects ##
    InfoText = QLabel("Login")
    LoginButton = QPushButton("Login")
    UsernameInput = QLineEdit("Username")
    PasswordInput = QLineEdit("Password")
    
    ## Layout ##
    layout = QVBoxLayout()
    layout.addWidget(InfoText)
    layout.addWidget(UsernameInput)
    layout.addWidget(PasswordInput)
    layout.addWidget(LoginButton)
    
    ## Window ##
    window = QWidget()
    window.setWindowTitle("CrimosOS")
    window.setLayout(layout)
    
    ## Funcs ##
    LoginButton.clicked.connect(UserHandler.LoginFunc(UsernameInput.text, PasswordInput.text))
    
    ## Show ##
    window.show()
    InfoText.show()
    UsernameInput.show()
    PasswordInput.show()
    LoginButton.show()
    
    ## Execute ##
    app.exec()