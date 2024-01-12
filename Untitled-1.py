#importing modules and widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QLabel, QLineEdit,QListWidget,QMessageBox
import json
from secwindow import SeccondWindow
#declaring constants
win_width, win_height = 200, 300
win_x, win_y = 200, 200
txt_title = "Sending text"
txt_line = "Entry field"
 
class MainWindow(QWidget):
    value = 0
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        # creating and customizing the graphical elements:
        self.initUI()
        #connects the elements
        self.connects()
        self.dict=dict()
        self.load_data()
        #determines how the window will look (text, size, location)
        self.set_appear()
 
        # start:
        self.show()
    def load_data(self):
        try:
            with open("save.json", "r")as inputfile: 
                self.dict=json.load(inputfile)
                self.addlist()
        except:
            print('no data to read')
    
                
    def initUI(self):
        ''' creates graphical elements '''
        intrebare=QLabel('intrebare',self)
        corect=QLabel('raspuns corect',self)
        r1=QLabel('raspuns gresit 1',self)
        r2=QLabel('raspuns gresit 2',self)
        r3=QLabel('raspuns gresit 3',self)
        self.corectedit=QLineEdit()
        self.intrebareedit=QLineEdit()
        self.r1edit=QLineEdit()
        self.r2edit=QLineEdit()
        self.r3edit=QLineEdit()
        self.edit=QListWidget()
        self.edit.setMinimumWidth(120) 
        self.edit.setMinimumHeight(120)
        self.intrnou=QPushButton('intrebare noua',self)
        self.sterintr = QPushButton("sterge intrebarea", self)
        self.exers=QPushButton('incepe sa exersezi',self)
        self.layout_line = QVBoxLayout()
 
        
 
        L=QVBoxLayout()
        l1 = QHBoxLayout()
        l1.addWidget(self.edit)
        
        l2=QVBoxLayout()
        l2.addWidget(intrebare)
        l2.addWidget(corect)
        l2.addWidget(r1)
        l2.addWidget(r2)
        l2.addWidget(r3)
        l3=QVBoxLayout()
        l3.addWidget(self.intrebareedit)
        l3.addWidget(self.corectedit)
        l3.addWidget(self.r1edit)
        l3.addWidget(self.r2edit)
        l3.addWidget(self.r3edit)
        l1.addLayout(l2)
        l1.addLayout(l3)
        l5=QHBoxLayout()
        l5.addWidget(self.intrnou)
        l5.addWidget(self.sterintr)
        l6=QHBoxLayout()
        l6.addWidget(self.exers)
        L.addLayout(l1)
        L.addLayout(l5)
        L.addLayout(l6)
        
        
        
        self.layout_line.addLayout(L)
        self.setLayout(self.layout_line)
    def addNewQuestion(self):
        question=self.intrebareedit.text()
        ct=self.corectedit.text()
        r1t=self.r1edit.text()
        r2t=self.r2edit.text()
        r3t=self.r3edit.text()
        msg = QMessageBox()
        msg.setWindowTitle("raspuns lipseste")
        if r1t=='':
            msg.setText("lipseste raspunsul gresit 1")
            msg.exec_() 
        elif r2t=='':
            msg.setText("lipseste raspunsul gresit 2")
            msg.exec_() 
        elif r3t=='':
            msg.setText("lipseste raspunsul gresit 3")
            msg.exec_() 
        elif ct=='':
            msg.setText("lipseste raspunsul corect ")
            msg.exec_() 
        elif question=='':
            msg.setText("lipseste intrebarea ")
            msg.exec_() 
        else:
            self.dict[question]={'cq':ct,'r1':r1t ,'r2':r2t,'r3':r3t}
            print(self.dict)
            self.addlist()
            with open("save.json", "w") as outfile: 
                jsonsave=json.dumps(self.dict)
                outfile.write(jsonsave)
    def learn(self):
        self.secondW = SeccondWindow()
        self.secondW.set_questions(self.dict)
        self.secondW.show()
    def deleteb(self):
        items = self.edit.selectedItems()
        for item in items:
            question = item.text()
            print(f'Removing {question}')
            del self.dict[question]
            self.addlist()

        # listItems=list(self.edit.selectedItems())
        # print(listItems)
        # if listItems: 
        #     for item in listItems:
        #         print(item)
        #         del self.dict[item] 

        #         self.addlist() 
        #         with open("save.json", "w") as outfile: 
        #             jsonsave=json.dumps(self.dict)
        #             outfile.write(jsonsave)
             
    def addlist(self):
        self.edit.clear()
        items=self.dict.keys()
        self.edit.addItems(items)


    def connects(self):
        self.intrnou.clicked.connect(self.addNewQuestion)
        self.sterintr.clicked.connect(self.deleteb)
        self.exers.clicked.connect(self.learn)
        # Nu need for the buttons to do something in this exercise/nothing to add here 
        pass
        
    ''' determines how the window will look (text, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
 
 
def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()
 
main()
