# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 20:57:32 2018

@author: Hassan
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
    QInputDialog, QApplication) 	
def cir1(func = 1,trig = 'sin',curve_type = "Polar Curve",a=0, b=0, n=1):
    cstr = "Equation : (r = " + str(a) +" * " + 'θ' + ")"
    graph(2,curve_type = cstr,n = a)
    return 
def cir2(func = 1,trig = 'sin',curve_type = "Polar Curve",a=0, b=0, n=1):
    #print("Equation is of the form : " + "(r = a * (cos " + 'θ' + "))")
    trig_func = trig
    #trig_func = input("Enter Trig Function (sin , cos) : ")
    cstr = "Equation : (r = " + str(a) +" * (" + trig_func + " " + 'θ' + "))"
    graph(1,trig_func,curve_type = cstr,b=a)
    return
def  rose(func = 1,trig = 'sin',curve_type = "Polar Curve",a=0, b=0, n=1):
    #print("Equation is of the form : " + "(r = a * (cos (n * " + 'θ' + ")))")
    #trig_func = input("Enter Trig Function (sin , cos) : ")
    trig_func = trig
    cstr = "Equation : (r = " + str(a) +" * (" + trig_func + " ( " + str(n) + " * "+ 'θ' + ")))"
    graph(1,trig_func,curve_type = cstr ,b=a,n=n)
    return
def lemniscate(func = 1,trig = 'sin',curve_type = "Polar Curve",a=0, b=0, n=1):
    #print("Equation is of the form : " + "(r = a * sqrt(cos (n * " + 'θ' + ")))")
    #trig_func = input("Enter Trig Function (sin , cos) : ")
    trig_func = trig
    cstr = "Equation : (r = " + str(a) +" * sqrt(" + trig_func + " ( " + str(n) + " * "+ 'θ' + ")))"
    graph(3,trig_func,curve_type = cstr,b=a,n=n)
    return
def cardl(func = 1,trig = 'sin',curve_type = "Polar Curve",a=0, b=0, n=1):
    #print("Equation is of the form : " + "(r = a +  b * (cos " + 'θ' + "))")
    #trig_func = input("Enter Trig Function (sin , cos) : ")
    trig_func = trig
    cstr = "Equation : (r = "+ str(a) +" + " + str(b) +" * (" + trig_func + " " + 'θ' + "))"
    graph(1,trig_func,curve_type = cstr,a = a,b = b)
    return 
def graph(func = 1,trig = 'sin',curve_type = "Polar Curve",a=0, b=0, n=1):
    
    theta = np.arange(0, 2 * np.pi, 0.01)
    
    tf = [np.sin,np.cos]
    tf_int = 0
    if(trig == 'sin'):
        tf_int = 0
    elif(trig == 'cos'):
        tf_int = 1
    else:
        print("INVALID INPUT ")
        return 
    
    if(func == 1):
        r = a + (b * (tf[tf_int](n * theta)))
        rad = np.arange(0, (a + b) + 1 , 2)
    elif(func == 2):
        
        r = (theta >= 0) * n
        rad = np.arange(0, n + n, 2)
    elif(func == 3):
        r = theta
        r = r * 0
        l = len(theta)
        for i in range(0,l):
            if((tf[tf_int](n * theta[i])) > 0):
                r[i] = b * np.sqrt((tf[tf_int](n * theta[i])))
            else:
                r[i] = 0
        rad = np.arange(0, a + b +1 , 2)
        
    else:
        print("INVALID INPUT ")
        return 
    
    
    
        
    ax = plt.subplot(111, projection='polar')
    ax.plot(theta, r)
    ax.set_rmax(a + b + 2)
    ax.set_rticks(rad)  # Less radial ticks
    ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)
    ax.set_title(curve_type, va='bottom')
    plt.show()
    

    return a + b



qtCreatorFile = "base1.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

globalobj = 0
def graph_widget(tfunc_val = 0,val_a = 0, val_b = 0,val_n = 1, val_trig_func = 'sin'):
        func = [cir1,cir2,rose,lemniscate,cardl]
        func[tfunc_val](a = val_a,b = val_b ,n = val_n,trig =  val_trig_func)
        

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    
        
    def func_cir1(self):
        tval_a, ok = QInputDialog.getText(self, 'Input a ', 
            'Enter value of a :')
        
        if ok:
            tval_a = int(tval_a)
            graph_widget(tfunc_val = 0,val_a = tval_a)
       
    def func_cir2(self):  
        tval_a, ok = QInputDialog.getText(self, 'Input a ', 
            'Enter value of a :')
        tval_trig_func, ok = QInputDialog.getText(self, 'Input trignometric function ', 
            'Enter trig func (sin or cos) :')
        
        if ok:
            tval_a = int(tval_a)
        
        graph_widget(tfunc_val = 1,val_a = tval_a,val_trig_func = tval_trig_func)

    def func_rose(self):  
        tval_a, ok = QInputDialog.getText(self, 'Input a ', 
            'Enter value of a :')
        tval_trig_func, ok = QInputDialog.getText(self, 'Input trignometric function ', 
            'Enter trig func (sin or cos) :')
        tval_n, ok = QInputDialog.getText(self, 'Input n ', 
            'Enter value of n :')
        
        if ok:
            tval_a = int(tval_a)
            tval_n = int(tval_n)
        graph_widget(tfunc_val = 2,val_a = tval_a,val_n = tval_n,val_trig_func = tval_trig_func)    
    
    def func_lemniscate(self):  
        tval_a, ok = QInputDialog.getText(self, 'Input a ', 
            'Enter value of a :')
        tval_trig_func, ok = QInputDialog.getText(self, 'Input trignometric function ', 
            'Enter trig func (sin or cos) :')
        tval_n, ok = QInputDialog.getText(self, 'Input n ', 
            'Enter value of n :')
        
        if ok:
            tval_a = int(tval_a)
            tval_n = int(tval_n)
        graph_widget(tfunc_val = 3,val_a = tval_a,val_n = tval_n,val_trig_func = tval_trig_func)    
    
    def func_carl(self):  
        tval_a, ok = QInputDialog.getText(self, 'Input a ', 
            'Enter value of a :')
        tval_b, ok = QInputDialog.getText(self, 'Input b ', 
            'Enter value of b :')
        tval_trig_func, ok = QInputDialog.getText(self, 'Input trignometric function ', 
            'Enter trig func (sin or cos) :')
        
        
        if ok:
            tval_a = int(tval_a)
            tval_b = int(tval_b)
        graph_widget(tfunc_val = 4,val_a = tval_a,val_b = tval_b,val_trig_func = tval_trig_func)    
        
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_cir1.clicked.connect(self.func_cir1)
        self.pushButton_cir2.clicked.connect(self.func_cir2)
        self.pushButton_rose.clicked.connect(self.func_rose)
        self.pushButton_lemniscate.clicked.connect(self.func_lemniscate)
        self.pushButton_carl.clicked.connect(self.func_carl)
        
if __name__ == "__main__":
   
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    