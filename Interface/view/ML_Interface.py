'''
    机器学习子界面
'''
from PySide6 import QtCore, QtGui, QtWidgets

# .ui文件转换得到
class Ui_MachineLearning(object):
    def setupUi(self, MachineLearning):
        MachineLearning.setObjectName("MachineLearning")
        MachineLearning.resize(873, 889)
        MachineLearning.setMinimumSize(QtCore.QSize(500, 400))
        self.MachineLearning_Frame = QtWidgets.QFrame(MachineLearning)
        self.MachineLearning_Frame.setGeometry(QtCore.QRect(0, 40, 700, 600))
        self.MachineLearning_Frame.setMinimumSize(QtCore.QSize(500, 400))
        self.MachineLearning_Frame.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.MachineLearning_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MachineLearning_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MachineLearning_Frame.setObjectName("MachineLearning_Frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MachineLearning_Frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MachineLearning_title_frame = QtWidgets.QFrame(self.MachineLearning_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.MachineLearning_title_frame.sizePolicy().hasHeightForWidth())
        self.MachineLearning_title_frame.setSizePolicy(sizePolicy)
        self.MachineLearning_title_frame.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.MachineLearning_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MachineLearning_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MachineLearning_title_frame.setObjectName("MachineLearning_title_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.MachineLearning_title_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.MachineLearning_system_frame = QtWidgets.QFrame(self.MachineLearning_title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MachineLearning_system_frame.sizePolicy().hasHeightForWidth())
        self.MachineLearning_system_frame.setSizePolicy(sizePolicy)
        self.MachineLearning_system_frame.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.MachineLearning_system_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MachineLearning_system_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MachineLearning_system_frame.setObjectName("MachineLearning_system_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MachineLearning_system_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MachineLearning_icon = QtWidgets.QFrame(self.MachineLearning_system_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MachineLearning_icon.sizePolicy().hasHeightForWidth())
        self.MachineLearning_icon.setSizePolicy(sizePolicy)
        self.MachineLearning_icon.setMinimumSize(QtCore.QSize(85, 85))
        self.MachineLearning_icon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MachineLearning_icon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MachineLearning_icon.setObjectName("MachineLearning_icon")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.MachineLearning_icon)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Machinelearning_Icon = QtWidgets.QLabel(self.MachineLearning_icon)
        self.Machinelearning_Icon.setMinimumSize(QtCore.QSize(85, 85))
        self.Machinelearning_Icon.setStyleSheet("")
        self.Machinelearning_Icon.setText("")
        self.Machinelearning_Icon.setPixmap(QtGui.QPixmap("Resource/img/logo.png"))
        self.Machinelearning_Icon.setScaledContents(True)
        self.Machinelearning_Icon.setObjectName("Machinelearning_Icon")
        self.verticalLayout_4.addWidget(self.Machinelearning_Icon, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.MachineLearning_icon, 0, QtCore.Qt.AlignTop)
        self.MachineLearning_title = QtWidgets.QFrame(self.MachineLearning_system_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MachineLearning_title.sizePolicy().hasHeightForWidth())
        self.MachineLearning_title.setSizePolicy(sizePolicy)
        self.MachineLearning_title.setMinimumSize(QtCore.QSize(130, 50))
        self.MachineLearning_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MachineLearning_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MachineLearning_title.setObjectName("MachineLearning_title")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.MachineLearning_title)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Machinelearning_Title = QtWidgets.QLabel(self.MachineLearning_title)
        self.Machinelearning_Title.setMinimumSize(QtCore.QSize(256, 46))
        self.Machinelearning_Title.setStyleSheet("")
        self.Machinelearning_Title.setText("")
        self.Machinelearning_Title.setPixmap(QtGui.QPixmap("Resource/img/title.jpg"))
        self.Machinelearning_Title.setScaledContents(True)
        self.Machinelearning_Title.setObjectName("Machinelearning_Title")
        self.horizontalLayout_3.addWidget(self.Machinelearning_Title)
        self.horizontalLayout.addWidget(self.MachineLearning_title)
        self.verticalLayout_3.addWidget(self.MachineLearning_system_frame, 0, QtCore.Qt.AlignVCenter)
        self.MachineLearning_option_frame = QtWidgets.QFrame(self.MachineLearning_title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MachineLearning_option_frame.sizePolicy().hasHeightForWidth())
        self.MachineLearning_option_frame.setSizePolicy(sizePolicy)
        self.MachineLearning_option_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MachineLearning_option_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MachineLearning_option_frame.setObjectName("MachineLearning_option_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.MachineLearning_option_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.machine_learning = QtWidgets.QLabel(self.MachineLearning_option_frame)
        self.machine_learning.setStyleSheet("font: 75 9pt \"Fixedsys\";")
        self.machine_learning.setObjectName("machine_learning")
        self.horizontalLayout_2.addWidget(self.machine_learning, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.MachineLearning_option_frame)
        self.verticalLayout.addWidget(self.MachineLearning_title_frame)
        self.MachineLearning_button_frame = QtWidgets.QFrame(self.MachineLearning_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.MachineLearning_button_frame.sizePolicy().hasHeightForWidth())
        self.MachineLearning_button_frame.setSizePolicy(sizePolicy)
        self.MachineLearning_button_frame.setStyleSheet("")
        self.MachineLearning_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MachineLearning_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MachineLearning_button_frame.setObjectName("MachineLearning_button_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MachineLearning_button_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MachineLearning_gridLayout = QtWidgets.QGridLayout()
        self.MachineLearning_gridLayout.setObjectName("MachineLearning_gridLayout")
        self.linear_regression = PushButton(self.MachineLearning_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linear_regression.sizePolicy().hasHeightForWidth())
        self.linear_regression.setSizePolicy(sizePolicy)
        self.linear_regression.setMinimumSize(QtCore.QSize(150, 80))
        self.linear_regression.setObjectName("linear_regression")
        self.MachineLearning_gridLayout.addWidget(self.linear_regression, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.KNN = PushButton(self.MachineLearning_button_frame)
        self.KNN.setMinimumSize(QtCore.QSize(150, 80))
        self.KNN.setObjectName("KNN")
        self.MachineLearning_gridLayout.addWidget(self.KNN, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.SVM = PushButton(self.MachineLearning_button_frame)
        self.SVM.setMinimumSize(QtCore.QSize(150, 80))
        self.SVM.setObjectName("SVM")
        self.MachineLearning_gridLayout.addWidget(self.SVM, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.PCA = PushButton(self.MachineLearning_button_frame)
        self.PCA.setMinimumSize(QtCore.QSize(150, 80))
        self.PCA.setObjectName("PCA")
        self.MachineLearning_gridLayout.addWidget(self.PCA, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.decision_tree = PushButton(self.MachineLearning_button_frame)
        self.decision_tree.setMinimumSize(QtCore.QSize(150, 80))
        self.decision_tree.setObjectName("PCA")
        self.MachineLearning_gridLayout.addWidget(self.decision_tree, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.MachineLearning_Others = PushButton(self.MachineLearning_button_frame)
        self.MachineLearning_Others.setMinimumSize(QtCore.QSize(150, 80))
        self.MachineLearning_Others.setObjectName("MachineLearning_Others")
        self.MachineLearning_gridLayout.addWidget(self.MachineLearning_Others, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.MachineLearning_gridLayout)
        self.verticalLayout.addWidget(self.MachineLearning_button_frame)

        self.retranslateUi(MachineLearning)
        QtCore.QMetaObject.connectSlotsByName(MachineLearning)

    def retranslateUi(self, MachineLearning):
        _translate = QtCore.QCoreApplication.translate
        MachineLearning.setWindowTitle(_translate("MachineLearning", "Form"))
        self.machine_learning.setText(_translate("MachineLearning", "机器学习算法教学演示"))
        self.linear_regression.setText(_translate("MachineLearning", "线性回归"))
        self.KNN.setText(_translate("MachineLearning", "K-近邻"))
        self.SVM.setText(_translate("MachineLearning", "支持向量机"))
        self.PCA.setText(_translate("MachineLearning", "主成分分析"))
        self.decision_tree.setText(_translate("MachineLearning", "决策树"))
        self.MachineLearning_Others.setText(_translate("MachineLearning", "敬请期待"))
from qfluentwidgets import PushButton

from PySide6.QtWidgets import QWidget

class MachineLearningInterface(QWidget, Ui_MachineLearning):
    def __init__(self):
        super().__init__()
        self.setupUi(self)