import sys
import pickle
from PyQt4 import QtGui, QtCore
from msilib.schema import ComboBox

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(0, 28, 250, 600)
        self.setWindowTitle("Build Storage")
        self.setWindowIcon(QtGui.QIcon(r'C:\Users\lwree\Downloads\turtle_logo.ico'))

        newBuild = QtGui.QAction("&New", self)
        newBuild.setShortcut("Ctrl+N")
        newBuild.setStatusTip('Create new build')
        newBuild.triggered.connect(self.new_build)

        self.statusBar()

        
        self.build_buttons()
        self.home()
        self.quit_button()

    def home(self):
        

        newBuild = QtGui.QAction('New', self)
        newBuild.triggered.connect(self.new_build)
        
        exitTool = QtGui.QAction('Exit', self)
        exitTool.triggered.connect(self.close_app)
        
        clearTool = QtGui.QAction('Clear', self)
        clearTool.triggered.connect(self.clear_builds)
        
        self.toolBar = self.addToolBar("Tools")
        self.toolBar.addAction(newBuild)
        self.toolBar.addAction(clearTool)
        self.toolBar.addAction(exitTool)

        
        
        
        self.show()
        
    def build_buttons(self):
        build_dict = pickle.load(open("build_dicts.p", "rb"))
        i = 0
        for buildBut in build_dict.keys():
            buildBtn = QtGui.QPushButton(buildBut, self)
            buildBtn.resize(250, 50)
            buildBtn.move(0 , 20 + i)
            
            buildBtn.show()
            
            deleteBtn = QtGui.QPushButton("X", self)
            deleteBtn.clicked.connect(lambda:build_dict.pop(buildBut))
            deleteBtn.clicked.connect(lambda:pickle.dump(build_dict, open("build_dicts.p", "wb")))
            deleteBtn.clicked.connect(self.build_buttons)
            deleteBtn.resize(30, 30)
            deleteBtn.move(200, 30 + i)
            deleteBtn.show()
            
            i += 50
        
        
        pickle.dump(build_dict, open("build_dicts.p", "wb"))
        
        self.build_buttons
    def new_build(self):
        build_dict = pickle.load(open("build_dicts.p", "rb"))
        build_dict["test1"] = "test1"
        pickle.dump(build_dict, open("build_dicts.p", "wb"))
        self.build_buttons()
        
    def clear_builds(self):
        build_dict = pickle.load(open("build_dicts.p", "rb"))
        build_dict.clear()
        pickle.dump(build_dict, open("build_dicts.p", "wb"))
        self.build_buttons()
        
    def quit_button(self):
        exit_app = QtGui.QPushButton("Quit", self)
        exit_app.clicked.connect(self.close)
        exit_app.resize(exit_app.minimumSizeHint())
        exit_app.resize(250, 50)
        exit_app.move(0, 550)
        exit_app.show()
        
        
    def close_app(self):
        sys.exit()
        
            

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
