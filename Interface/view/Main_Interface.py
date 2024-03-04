'''
    主页面子界面
'''
from PySide6 import QtCore, QtGui, QtWidgets

# .ui文件转换得到
class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(873, 889)
        Main.setMinimumSize(QtCore.QSize(500, 400))
        self.Main_Frame = QtWidgets.QFrame(Main)
        self.Main_Frame.setGeometry(QtCore.QRect(0, 40, 700, 600))
        self.Main_Frame.setMinimumSize(QtCore.QSize(500, 400))
        self.Main_Frame.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Main_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_Frame.setObjectName("Main_Frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Main_Frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Main_title_frame = QtWidgets.QFrame(self.Main_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.Main_title_frame.sizePolicy().hasHeightForWidth())
        self.Main_title_frame.setSizePolicy(sizePolicy)
        self.Main_title_frame.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.Main_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_title_frame.setObjectName("Main_title_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Main_title_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Main_system_frame = QtWidgets.QFrame(self.Main_title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Main_system_frame.sizePolicy().hasHeightForWidth())
        self.Main_system_frame.setSizePolicy(sizePolicy)
        self.Main_system_frame.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.Main_system_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_system_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_system_frame.setObjectName("Main_system_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Main_system_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Main_icon = QtWidgets.QFrame(self.Main_system_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_icon.sizePolicy().hasHeightForWidth())
        self.Main_icon.setSizePolicy(sizePolicy)
        self.Main_icon.setMinimumSize(QtCore.QSize(85, 85))
        self.Main_icon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_icon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_icon.setObjectName("Main_icon")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Main_icon)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Main_Icon = QtWidgets.QLabel(self.Main_icon)
        self.Main_Icon.setMinimumSize(QtCore.QSize(85, 85))
        self.Main_Icon.setStyleSheet("")
        self.Main_Icon.setText("")
        self.Main_Icon.setPixmap(QtGui.QPixmap("Resource/img/logo.png"))
        self.Main_Icon.setScaledContents(True)
        self.Main_Icon.setObjectName("Main_Icon")
        self.verticalLayout_4.addWidget(self.Main_Icon, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.Main_icon, 0, QtCore.Qt.AlignTop)
        self.Main_title = QtWidgets.QFrame(self.Main_system_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_title.sizePolicy().hasHeightForWidth())
        self.Main_title.setSizePolicy(sizePolicy)
        self.Main_title.setMinimumSize(QtCore.QSize(130, 50))
        self.Main_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_title.setObjectName("Main_title")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Main_title)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Main_Title = QtWidgets.QLabel(self.Main_title)
        self.Main_Title.setMinimumSize(QtCore.QSize(256, 46))
        self.Main_Title.setStyleSheet("")
        self.Main_Title.setText("")
        self.Main_Title.setPixmap(QtGui.QPixmap("Resource/img/title.jpg"))
        self.Main_Title.setScaledContents(True)
        self.Main_Title.setObjectName("Main_Title")
        self.horizontalLayout_3.addWidget(self.Main_Title)
        self.horizontalLayout.addWidget(self.Main_title)
        self.verticalLayout_3.addWidget(self.Main_system_frame, 0, QtCore.Qt.AlignVCenter)
        self.Main_option_frame = QtWidgets.QFrame(self.Main_title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Main_option_frame.sizePolicy().hasHeightForWidth())
        self.Main_option_frame.setSizePolicy(sizePolicy)
        self.Main_option_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_option_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_option_frame.setObjectName("Main_option_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Main_option_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main = QtWidgets.QLabel(self.Main_option_frame)
        self.main.setStyleSheet("font: 75 9pt \"Fixedsys\";")
        self.main.setObjectName("main")
        self.horizontalLayout_2.addWidget(self.main, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.Main_option_frame)
        self.verticalLayout.addWidget(self.Main_title_frame)
        self.Main_Welcome_frame = QtWidgets.QFrame(self.Main_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.Main_Welcome_frame.sizePolicy().hasHeightForWidth())
        self.Main_Welcome_frame.setSizePolicy(sizePolicy)
        self.Main_Welcome_frame.setStyleSheet("")
        self.Main_Welcome_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_Welcome_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_Welcome_frame.setObjectName("Main_Welcome_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Main_Welcome_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.welcome = QtWidgets.QLabel(self.Main_Welcome_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome.sizePolicy().hasHeightForWidth())
        self.welcome.setSizePolicy(sizePolicy)
        self.welcome.setMinimumSize(QtCore.QSize(256, 256))
        self.welcome.setText("")
        self.welcome.setPixmap(QtGui.QPixmap("Resource/img/welcome.png"))
        self.welcome.setScaledContents(True)
        self.welcome.setObjectName("welcome")
        self.verticalLayout_2.addWidget(self.welcome, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.Main_Welcome_frame)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.main.setText(_translate("Main", "欢迎使用人工智能算法教学演示系统！"))

from PySide6.QtWidgets import QWidget

class MainInterface(QWidget, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)