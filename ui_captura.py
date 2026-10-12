# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'captura.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 420)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnCapturar = QPushButton(self.centralwidget)
        self.btnCapturar.setObjectName(u"btnCapturar")

        self.verticalLayout.addWidget(self.btnCapturar)

        self.txtDatos = QPlainTextEdit(self.centralwidget)
        self.txtDatos.setObjectName(u"txtDatos")
        self.txtDatos.setReadOnly(True)

        self.verticalLayout.addWidget(self.txtDatos)

        self.lblEstado = QLabel(self.centralwidget)
        self.lblEstado.setObjectName(u"lblEstado")
        self.lblEstado.setWordWrap(True)

        self.verticalLayout.addWidget(self.lblEstado)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Captura serial | Instrumentaci\u00f3n Biom\u00e9dica", None))
        self.btnCapturar.setText(QCoreApplication.translate("MainWindow", u"Capturar", None))
        self.txtDatos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Aqu\u00ed aparecer\u00e1n los datos de Arduino...", None))
        self.lblEstado.setText(QCoreApplication.translate("MainWindow", u"Listo para capturar", None))
    # retranslateUi

