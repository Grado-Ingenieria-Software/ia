import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(512, 304)
        self.centralwidget = QWidget()
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.page1 = elegirProblema()
        self.wgtMainWindow = QPushButton(self.page1)
        self.wgtMainWindow.setGeometry(QRect(120, 120, 50, 18))
        self.wgtMainWindow.setObjectName("wgtMainWindow")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = elegirAlgoritmo()
        self.wgtbtnB = QPushButton(self.page2)
        self.wgtbtnB.setGeometry(QRect(120, 120, 50, 18))
        self.wgtbtnB.setObjectName("wgtbtnB")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = elegirModoSimulacion()
        self.wgtbtnC = QPushButton(self.page3)
        self.wgtbtnC.setGeometry(QRect(120, 120, 50, 18))
        self.wgtbtnC.setObjectName("wgtbtnC")
        self.stackedWidget.addWidget(self.page3)
        MainWindow.setCentralWidget(self.centralwidget)
		
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)
        

class menuPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super(menuPrincipal, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.setWindowTitle("TRABAJO IA")
        self.ui.setupUi(self)
        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("Menu")
		
        save = QAction("Inicio",self)
        save.setShortcut("Ctrl+I")
        file.addAction(save)
		
        edit = file.addMenu("Problemas")
        edit.addAction("Tigre")
        edit.addAction("TAG")
        edit.addAction("Anuncios")
        edit.addAction("InidianaJones")
		
        salir = QAction("Salir",self) 
        salir.setShortcut("Ctrl+Q")
        file.addAction(salir)
        file.triggered[QAction].connect(self.triggerMenu)
        self.setLayout(layout)
        self.setWindowTitle("TRABAJO IA")

        self.ui.wgtbtnC.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.wgtbtnB.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.wgtMainWindow.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
		
    def triggerMenu(self,q):
        if q.text()=="Tigre":
            problema = "Tigre"
            print("Problema tigre")
            self.ui.stackedWidget.setCurrentIndex(1)
        if q.text()=="TAG":
            problema = "TAG"
            print("Problema TAG")
            self.ui.stackedWidget.setCurrentIndex(1)
        if q.text()=="Anuncios":
            problema = "Anuncios"
            print("Problema Anuncios")
            self.ui.stackedWidget.setCurrentIndex(1)
        if q.text()=="IndianaJones":
            problema = "IndianaJones"
            print("Problema InidianaJones")
            self.ui.stackedWidget.setCurrentIndex(1)
        if q.text()=="Inicio":
            print("Inicio")
            self.ui.stackedWidget.setCurrentIndex(0)
        if q.text()=="Salir":
            exit()

        

class elegirProblema(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        plantilla = QGridLayout()
        self.setLayout(plantilla)

        plantilla.addWidget(QLabel("Elija el problema a resolver:"))  

        radiobutton = QRadioButton("Tigre")
        radiobutton.problema = "Tigre"
        radiobutton.toggled.connect(self.problemaElegido)
        plantilla.addWidget(radiobutton)

        radiobutton = QRadioButton("TAG")
        radiobutton.problema = "TAG"
        radiobutton.toggled.connect(self.problemaElegido)
        plantilla.addWidget(radiobutton)

        radiobutton = QRadioButton("Anuncios")
        radiobutton.problema = "Anuncios"
        radiobutton.toggled.connect(self.problemaElegido)
        plantilla.addWidget(radiobutton)

        radiobutton = QRadioButton("IndianaJones")
        radiobutton.problema = "IndianaJones"
        radiobutton.toggled.connect(self.problemaElegido)
        plantilla.addWidget(radiobutton)

    def problemaElegido(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            problema = radioButton.problema
            print("Has elegido el problema: %s" % (radioButton.problema))
      


class elegirAlgoritmo(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        plantilla = QGridLayout()
        self.setLayout(plantilla)

        plantilla.addWidget(QLabel("Elija el algoritmo:"))  

        radiobutton = QRadioButton("POMDP")
        radiobutton.algoritmo = "POMDP"
        radiobutton.toggled.connect(self.algoritmoElegido)
        plantilla.addWidget(radiobutton)

        radiobutton = QRadioButton("PBVI")
        radiobutton.algoritmo = "PBVI"
        radiobutton.toggled.connect(self.algoritmoElegido)
        plantilla.addWidget(radiobutton)

    def algoritmoElegido(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            algoritmo = radioButton.algoritmo
            print("Has elegido el algoritmo: %s" % (radioButton.algoritmo))


class elegirModoSimulacion(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        plantilla = QGridLayout()
        self.setLayout(plantilla)

        plantilla.addWidget(QLabel("Elija el modo de simulacion:"))  

        radiobutton = QRadioButton("Iterativa")
        radiobutton.modo = "Iterativa"
        radiobutton.toggled.connect(self.modoElegido)
        plantilla.addWidget(radiobutton)

        radiobutton = QRadioButton("Silenciosa")
        radiobutton.modo = "Silenciosa"
        radiobutton.toggled.connect(self.modoElegido)
        plantilla.addWidget(radiobutton)

        
        radiobutton = QRadioButton("Benchmark")
        radiobutton.modo = "Benchmark"
        radiobutton.toggled.connect(self.modoElegido)
        plantilla.addWidget(radiobutton)

    def modoElegido(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            algoritmo = radioButton.modo
            print("Has elegido el modo de simulacion: %s" % (radioButton.modo))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mySW = menuPrincipal()
    mySW.show()
    sys.exit(app.exec_())