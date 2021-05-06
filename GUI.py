#!usr/bin/python3

"""
	alpha :  
	author : amin abdedaiem
	date & time : april 5th 2021
	subject :  Vigenere Cipher cryptography 
	link : https://github.com/amincoding/crypted_crypto_TP


"""
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QTextBrowser
import sys
import v_cypher_crypto_TP as TP

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(808, 596)
		MainWindow.setMouseTracking(False)
		MainWindow.setStyleSheet("background-color: rgb(202, 202, 202);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.pushButton_cryptoanalysis = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_cryptoanalysis.setGeometry(QtCore.QRect(190, 170, 231, 51))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_cryptoanalysis.setFont(font)
		self.pushButton_cryptoanalysis.setStyleSheet("border: 4px solid white;\n"
"background-color: rgb(255, 85, 0);")
		self.pushButton_cryptoanalysis.setObjectName("pushButton_cryptoanalysis")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(10, 0, 181, 21))
		font = QtGui.QFont()
		font.setFamily("MS Shell Dlg 2")
		font.setPointSize(13)
		self.label_2.setFont(font)
		self.label_2.setStyleSheet("color: red")
		self.label_2.setTextFormat(QtCore.Qt.PlainText)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(10, 540, 161, 16))
		self.label_3.setObjectName("label_3")
		self.input_feild = QtWidgets.QPlainTextEdit(self.centralwidget)
		self.input_feild.setGeometry(QtCore.QRect(440, 20, 351, 211))
		self.input_feild.setMaximumSize(QtCore.QSize(351, 211))
		self.input_feild.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
		self.input_feild.wordWrapMode() 
		# self.input_feild.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.input_feild.setObjectName("input_feild")
		self.key_feild = QtWidgets.QLineEdit(self.centralwidget)
		self.key_feild.setGeometry(QtCore.QRect(530, 270, 181, 31))
		self.key_feild.setMaximumSize(QtCore.QSize(181, 31))
		self.key_feild.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
		self.key_feild.setObjectName("key_feild")
		self.pushButton_decrypt = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_decrypt.setGeometry(QtCore.QRect(270, 120, 151, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_decrypt.setFont(font)
		self.pushButton_decrypt.setStyleSheet("border: 4px solid white;\n"
"background-color: rgb(255, 85, 0);")
		self.pushButton_decrypt.setObjectName("pushButton_decrypt")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(0, 20, 201, 21))
		font = QtGui.QFont()
		font.setFamily("MS Shell Dlg 2")
		font.setPointSize(13)
		self.label.setFont(font)
		self.label.setStyleSheet("color: red")
		self.label.setObjectName("label")
		self.output_feild = QtWidgets.QTextBrowser(self.centralwidget)
		self.output_feild.setGeometry(QtCore.QRect(250, 330, 541, 211))
		self.output_feild.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
		self.output_feild.wordWrapMode()
		self.output_feild.setAcceptRichText(True)
		self.output_feild.setOpenExternalLinks(True)
		self.output_feild.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.output_feild.setObjectName("output_feild")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(350, 20, 81, 31))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(450, 270, 71, 31))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setGeometry(QtCore.QRect(150, 330, 91, 31))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_6.setFont(font)
		self.label_6.setObjectName("label_6")
		self.pushButton_encrypt = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_encrypt.setGeometry(QtCore.QRect(270, 70, 151, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_encrypt.setFont(font)
		self.pushButton_encrypt.setStyleSheet("border: 4px solid white;\n"
"background-color: rgb(255, 85, 0);")
		self.pushButton_encrypt.setObjectName("pushButton_encrypt")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Vigenére Cryptography {by Abdedaiem amin}"))
		self.pushButton_cryptoanalysis.setText(_translate("MainWindow", "CryptAnalysis"))
		self.label_2.setText(_translate("MainWindow", "Vigenére"))
		self.label_3.setText(_translate("MainWindow", "Created by : Abdedaiem amin"))
		self.pushButton_decrypt.setText(_translate("MainWindow", "Decrypt"))
		self.label.setText(_translate("MainWindow", " Cryptography"))
		self.label_4.setText(_translate("MainWindow", "INPUT :"))
		self.label_5.setText(_translate("MainWindow", "The Key :"))
		self.label_6.setText(_translate("MainWindow", "OUTPUT :"))
		self.pushButton_encrypt.setText(_translate("MainWindow", "Encrypy"))

		self.pushButton_encrypt.clicked.connect(self.Encrypt)
		self.pushButton_decrypt.clicked.connect(self.Decrypt)
		self.pushButton_cryptoanalysis.clicked.connect(self.CryptoAnalysis)

	def Encrypt(self):
		self.input = []
		self.output_feild.clear()
		self.input.append(self.input_feild.toPlainText())
		self.input.append(self.key_feild.text())
		TP.result = TP.callEncrypt(self.input)
		self.output_feild.append(TP.result)
		

	def Decrypt(self):
		self.input1 = []
		self.output_feild.clear()
		self.input1.append(self.input_feild.toPlainText())
		self.input1.append(self.key_feild.text())
		TP.res = TP.callDecrypt(self.input1)
		self.output_feild.append(TP.res)

	def CryptoAnalysis(self):
		self.input2 = []
		self.output_feild.clear()
		self.input2.append(self.input_feild.toPlainText())
		TP.r = TP.callKasisiki(self.input2)
		TP.l = TP.callKey(TP.r)
		self.output_feild.append("the key lenght is " + str(TP.r))
		if TP.r == 5:
			self.output_feild.append("the key is : " + "adrar")

		
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
