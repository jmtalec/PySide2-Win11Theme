
from win11theme import *



if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication, QVBoxLayout
    import sys

    layout1 = QVBoxLayout()
    layout2 = QVBoxLayout()
    layout3 = QVBoxLayout()
        

    app = QApplication(sys.argv)
    
    w1 = Win11FXWindow()
    w2 = Win11FXWindow()
    w3 = Win11FXWindow()

    w1['fx'] = FX_AERO
    w2['fx'] = FX_MICA
    w3['fx'] = FX_ACRYLIC

    w1.titleBar.raise_()
    w2.titleBar.raise_()
    w3.titleBar.raise_()
    
    w1.setWindowTitle('FX_AERO')
    w2.setWindowTitle('FX_MICA')
    w3.setWindowTitle('FX_ACRYLIC')


    layout1.addWidget(Calendar(w1))
    layout2.addWidget(Calendar(w2))
    layout3.addWidget(Calendar(w3))

    layout1.setContentsMargins(0, 32, 0, 0)
    layout2.setContentsMargins(0, 32, 0, 0)
    layout3.setContentsMargins(0, 32, 0, 0)
    
    w1.setLayout(layout1)
    w2.setLayout(layout2)
    w3.setLayout(layout3)
    

    w1.show()
    w2.show()
    w3.show()
        

    app.exec_()

