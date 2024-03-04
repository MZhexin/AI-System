import time

from PySide6 import QtCore, QtGui, QtWidgets

class Ui_LinearRegression(object):
    def setupUi(self, LinearRegression):
        LinearRegression.setObjectName("LinearRegression")
        LinearRegression.setEnabled(True)
        LinearRegression.resize(873, 889)
        LinearRegression.setMinimumSize(QtCore.QSize(500, 400))
        LinearRegression.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.LinearRegression_Frame = QtWidgets.QFrame(LinearRegression)
        self.LinearRegression_Frame.setGeometry(QtCore.QRect(10, 40, 700, 600))
        self.LinearRegression_Frame.setMinimumSize(QtCore.QSize(500, 400))
        self.LinearRegression_Frame.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.LinearRegression_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinearRegression_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinearRegression_Frame.setObjectName("LinearRegression_Frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.LinearRegression_Frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LinearRegression_title_frame = QtWidgets.QFrame(self.LinearRegression_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.LinearRegression_title_frame.sizePolicy().hasHeightForWidth())
        self.LinearRegression_title_frame.setSizePolicy(sizePolicy)
        self.LinearRegression_title_frame.setStyleSheet("")
        self.LinearRegression_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinearRegression_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinearRegression_title_frame.setObjectName("LinearRegression_title_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.LinearRegression_title_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LinearRegression_option_frame = QtWidgets.QFrame(self.LinearRegression_title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.LinearRegression_option_frame.sizePolicy().hasHeightForWidth())
        self.LinearRegression_option_frame.setSizePolicy(sizePolicy)
        self.LinearRegression_option_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LinearRegression_option_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinearRegression_option_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinearRegression_option_frame.setObjectName("LinearRegression_option_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.LinearRegression_option_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LinearRegression_name = QtWidgets.QLabel(self.LinearRegression_option_frame)
        self.LinearRegression_name.setStyleSheet("font: 75 9pt \"Fixedsys\";")
        self.LinearRegression_name.setObjectName("LinearRegression_name")
        self.horizontalLayout_2.addWidget(self.LinearRegression_name, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.LinearRegression_option_frame)
        self.verticalLayout.addWidget(self.LinearRegression_title_frame)
        self.LinearRegression_show_frame = QtWidgets.QFrame(self.LinearRegression_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.LinearRegression_show_frame.sizePolicy().hasHeightForWidth())
        self.LinearRegression_show_frame.setSizePolicy(sizePolicy)
        self.LinearRegression_show_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(74, 188, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.LinearRegression_show_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinearRegression_show_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinearRegression_show_frame.setObjectName("LinearRegression_show_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LinearRegression_show_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LinearRegression_info_frame = QtWidgets.QFrame(self.LinearRegression_show_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.LinearRegression_info_frame.sizePolicy().hasHeightForWidth())
        self.LinearRegression_info_frame.setSizePolicy(sizePolicy)
        self.LinearRegression_info_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.LinearRegression_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinearRegression_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinearRegression_info_frame.setObjectName("LinearRegression_info_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.LinearRegression_info_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.LinearRegression_introduction = PlainTextEdit(self.LinearRegression_info_frame)
        self.LinearRegression_introduction.setEnabled(True)
        self.LinearRegression_introduction.setStyleSheet("LineEdit, TextEdit, PlainTextEdit {\n"
"    font: 10pt \"楷体\";\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"    border-radius: 5px;\n"
"    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
"    padding: 0px 10px;\n"
"    selection-background-color: #00a7b3;\n"
"}\n"
"\n"
"TextEdit,\n"
"PlainTextEdit {\n"
"    padding: 2px 3px 2px 8px;\n"
"}\n"
"\n"
"LineEdit:hover, TextEdit:hover, PlainTextEdit:hover {\n"
"    background-color: rgba(249, 249, 249, 0.5);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"LineEdit:focus {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"    background-color: white;\n"
"}\n"
"\n"
"TextEdit:focus,\n"
"PlainTextEdit:focus {\n"
"    border-bottom: 1px solid #009faa;\n"
"    background-color: white;\n"
"}\n"
"\n"
"LineEdit:disabled, TextEdit:disabled,\n"
"PlainTextEdit:disabled {\n"
"    color: rgba(0, 0, 0, 150);\n"
"    background-color: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"}\n"
"\n"
"#lineEditButton {\n"
"    background-color: transparent;\n"
"    border-radius: 4px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"#lineEditButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"}\n"
"\n"
"#lineEditButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"}\n"
"")
        self.LinearRegression_introduction.setReadOnly(True)
        self.LinearRegression_introduction.setObjectName("LinearRegression_introduction")
        self.verticalLayout_5.addWidget(self.LinearRegression_introduction, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.LinearRegression_info_frame)
        self.LinearRegression_button_img_frame = QtWidgets.QFrame(self.LinearRegression_show_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.LinearRegression_button_img_frame.sizePolicy().hasHeightForWidth())
        self.LinearRegression_button_img_frame.setSizePolicy(sizePolicy)
        self.LinearRegression_button_img_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.LinearRegression_button_img_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinearRegression_button_img_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinearRegression_button_img_frame.setObjectName("LinearRegression_button_img_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.LinearRegression_button_img_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LinearRegression_Button_Frame = QtWidgets.QFrame(self.LinearRegression_button_img_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LinearRegression_Button_Frame.sizePolicy().hasHeightForWidth())
        self.LinearRegression_Button_Frame.setSizePolicy(sizePolicy)
        self.LinearRegression_Button_Frame.setStyleSheet("")
        self.LinearRegression_Button_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinearRegression_Button_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinearRegression_Button_Frame.setObjectName("LinearRegression_Button_Frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.LinearRegression_Button_Frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.LinearRegression_button = QtWidgets.QFrame(self.LinearRegression_Button_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.LinearRegression_button.sizePolicy().hasHeightForWidth())
        self.LinearRegression_button.setSizePolicy(sizePolicy)
        self.LinearRegression_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.LinearRegression_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinearRegression_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinearRegression_button.setObjectName("LinearRegression_button")
        self.LinearRegression_para_Layout = QtWidgets.QVBoxLayout(self.LinearRegression_button)
        self.LinearRegression_para_Layout.setObjectName("LinearRegression_para_Layout")
        self.LinearRegression_para_Label = QtWidgets.QLabel(self.LinearRegression_button)
        self.LinearRegression_para_Label.setObjectName("LinearRegression_para_Label")
        self.LinearRegression_para_Layout.addWidget(self.LinearRegression_para_Label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.LinearRegression_parameter = RangeSlider(self.LinearRegression_button)
        self.LinearRegression_parameter.setOrientation(QtCore.Qt.Horizontal)
        self.LinearRegression_parameter.setObjectName("LinearRegression_parameter")
        self.LinearRegression_parameter.setGeometry(14, 36, 261, 18)
        self.LinearRegression_para_Layout.addWidget(self.LinearRegression_parameter)
        self.verticalLayout_6.addWidget(self.LinearRegression_button)
        self.LinearRegression_progress = QtWidgets.QFrame(self.LinearRegression_Button_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.LinearRegression_progress.sizePolicy().hasHeightForWidth())
        self.LinearRegression_progress.setSizePolicy(sizePolicy)
        self.LinearRegression_progress.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.LinearRegression_progress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinearRegression_progress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinearRegression_progress.setObjectName("LinearRegression_progress")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.LinearRegression_progress)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.LinearRegression_progress_ring_frame = QtWidgets.QFrame(self.LinearRegression_progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LinearRegression_progress_ring_frame.sizePolicy().hasHeightForWidth())
        self.LinearRegression_progress_ring_frame.setSizePolicy(sizePolicy)
        self.LinearRegression_progress_ring_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinearRegression_progress_ring_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinearRegression_progress_ring_frame.setObjectName("LinearRegression_progress_ring_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.LinearRegression_progress_ring_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.LinearRegression_Progress_Ring = ProgressRing(self.LinearRegression_progress_ring_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.LinearRegression_Progress_Ring.sizePolicy().hasHeightForWidth())
        self.LinearRegression_Progress_Ring.setSizePolicy(sizePolicy)
        self.LinearRegression_Progress_Ring.setMinimumSize(QtCore.QSize(10, 10))
        self.LinearRegression_Progress_Ring.setTextVisible(True)
        self.LinearRegression_Progress_Ring.setObjectName("LinearRegression_Progress_Ring")
        self.verticalLayout_8.addWidget(self.LinearRegression_Progress_Ring)
        self.horizontalLayout_5.addWidget(self.LinearRegression_progress_ring_frame)
        self.LinearRegression_progress_label_frame = QtWidgets.QFrame(self.LinearRegression_progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LinearRegression_progress_label_frame.sizePolicy().hasHeightForWidth())
        self.LinearRegression_progress_label_frame.setSizePolicy(sizePolicy)
        self.LinearRegression_progress_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinearRegression_progress_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinearRegression_progress_label_frame.setObjectName("LinearRegression_progress_label_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.LinearRegression_progress_label_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.LinearRegression_train_button = PushButton(self.LinearRegression_progress_label_frame)
        self.LinearRegression_train_button.setObjectName("LinearRegression_train_button")
        self.verticalLayout_9.addWidget(self.LinearRegression_train_button)
        self.LinearRegression_test_button = PushButton(self.LinearRegression_progress_label_frame)
        self.LinearRegression_test_button.setObjectName("LinearRegression_test_button")
        self.verticalLayout_9.addWidget(self.LinearRegression_test_button)
        self.LinearRegression_img_button = PushButton(self.LinearRegression_progress_label_frame)
        self.LinearRegression_img_button.setObjectName("LinearRegression_img_button")
        self.verticalLayout_9.addWidget(self.LinearRegression_img_button)
        self.LinearRegression_reset_button = PushButton(self.LinearRegression_progress_label_frame)
        self.LinearRegression_reset_button.setObjectName("LinearRegression_reset_button")
        self.verticalLayout_9.addWidget(self.LinearRegression_reset_button)
        self.horizontalLayout_5.addWidget(self.LinearRegression_progress_label_frame)
        self.verticalLayout_6.addWidget(self.LinearRegression_progress)
        self.horizontalLayout_4.addWidget(self.LinearRegression_Button_Frame)
        self.LinearRegression_img_Frame = QtWidgets.QFrame(self.LinearRegression_button_img_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LinearRegression_img_Frame.sizePolicy().hasHeightForWidth())
        self.LinearRegression_img_Frame.setSizePolicy(sizePolicy)
        self.LinearRegression_img_Frame.setStyleSheet("")
        self.LinearRegression_img_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LinearRegression_img_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LinearRegression_img_Frame.setObjectName("LinearRegression_img_Frame")
        self.LinearRegression_img_widget = QWidget(self.LinearRegression_img_Frame)
        self.LinearRegression_img_widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                          "stop:0 rgba(225, 225, 225, 225), stop:1 rgba(65, 105, 225, 255));")
        self.LinearRegression_img_widget.setGeometry(14, 14, 330, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.LinearRegression_img_widget.setSizePolicy(sizePolicy)
        self.LinearRegression_img_widget.setContentsMargins(0, 0, 0, 0)
        self.LinearRegression_imageLabel = QtWidgets.QLabel(self.LinearRegression_img_widget)

        self.horizontalLayout_4.addWidget(self.LinearRegression_img_Frame)
        self.verticalLayout_2.addWidget(self.LinearRegression_button_img_frame)
        self.verticalLayout.addWidget(self.LinearRegression_show_frame)
        self.retranslateUi(LinearRegression)
        QtCore.QMetaObject.connectSlotsByName(LinearRegression)

    def retranslateUi(self, LinearRegression):
        _translate = QtCore.QCoreApplication.translate
        LinearRegression.setWindowTitle(_translate("LinearRegression", "Form"))
        self.LinearRegression_name.setText(_translate("LinearRegression", "线性回归算法"))
        self.LinearRegression_introduction.setPlainText(_translate("LinearRegression", "线性回归（Linear Regression）是一种"
                                                                                       "统计学方法，用于建立一个或多个自变量（解"
                                                                                       "释变量）与因变量（目标变量）之间的线性关"
                                                                                       "系模型。这种方法在数据分析、经济学、生物"
                                                                                       "统计学等多个领域中有着广泛的应用。线性回"
                                                                                       "归模型旨在寻找最佳拟合直线（在简单线性回"
                                                                                       "归中）或超平面（在多元线性回归中），以便"
                                                                                       "最准确地预测因变量的值。"))
        self.LinearRegression_para_Label.setText(_translate("LinearRegression", "选择线性模型的参数"))
        self.LinearRegression_train_button.setText(_translate("LinearRegression", "开始训练"))
        self.LinearRegression_test_button.setText(_translate("LinearRegression", "开始测试"))
        self.LinearRegression_img_button.setText(_translate("LinearRegression", "显示结果"))
        self.LinearRegression_reset_button.setText(_translate("LinearRegression", "重置进度条"))

from qfluentwidgets import PlainTextEdit, ProgressRing, PushButton, InfoBarPosition, InfoBar
from qfluentwidgetspro import RangeSlider

from PySide6.QtWidgets import QWidget

import matplotlib.pyplot as plt

import numpy as np

class LinearRegressionInterface(QWidget, Ui_LinearRegression):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.has_train = False

        self.LinearRegression_img_widget.close()
        
        self.LinearRegression_train_button.clicked.connect(self._start_train)

        self.LinearRegression_test_button.clicked.connect(self._start_test)

        self.LinearRegression_img_button.clicked.connect(self._show_result)

        self.LinearRegression_reset_button.clicked.connect(self._reset_progress_ring)

    def _start_train(self):
        X = np.random.rand(100) * 10
        noise = np.random.normal(0, 1, 100)
        a = self.LinearRegression_parameter.getRangeStart()
        b = self.LinearRegression_parameter.getRangeEnd()
        Y = b + np.dot(a, X) + noise

        # 训练阶段
        one = np.ones(len(Y)) # 增广

        self.LinearRegression_Progress_Ring.setValue(25)    # 训练完成25%，反映到进度条上

        x_b = np.c_[one.T, X] # 拼接

        self.LinearRegression_Progress_Ring.setValue(50)  # 训练完成50%，反映到进度条上

        pinv = np.linalg.pinv(np.dot(x_b.T, x_b))   # 求伪逆

        self.LinearRegression_Progress_Ring.setValue(75)  # 训练完成75%，反映到进度条上

        self.w = np.dot(np.dot(pinv, x_b.T), Y)    # 求权重

        self.LinearRegression_Progress_Ring.setValue(100)  # 训练完成100%，反映到进度条上

        self.has_train = True
        self.has_test = False

    def _start_test(self):
        if self.has_train:
            X = np.random.rand(100) * 10
            noise = np.random.normal(0, 1, 100)
            a = self.LinearRegression_parameter.getRangeStart()
            b = self.LinearRegression_parameter.getRangeEnd()
            Y = b + np.dot(a, X) + noise

            # 测试
            one = np.ones(len(Y))  # 增广

            self.LinearRegression_Progress_Ring.setValue(25)  # 训练完成25%，反映到进度条上

            x_b = np.c_[one.T, X]  # 拼接

            self.LinearRegression_Progress_Ring.setValue(50)  # 训练完成50%，反映到进度条上

            y_predict = np.dot(self.w, x_b.T)

            self.LinearRegression_Progress_Ring.setValue(75)  # 训练完成75%，反映到进度条上

            # 可视化
            plt.clf()
            plt.scatter(X, Y, color='orange')
            plt.plot(X, y_predict)
            plt.tight_layout()

            plt.savefig('Resource/results/LinearRegression_result.png', transparent=True)

            self.LinearRegression_Progress_Ring.setValue(100)  # 训练完成100%，反映到进度条上

            self.has_test = True
        else:
            InfoBar.warning(
                title='注意',
                content="请先训练模型再进行测试",
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM_RIGHT,
                duration=-1,
                parent=self
            )

    def _show_result(self):
        if self.has_train:
            if hasattr(self, 'has_test') and self.has_test:
                imgpath = 'Resource/results/LinearRegression_result.png'

                pixmap = QtGui.QPixmap(imgpath)
                self.LinearRegression_imageLabel.setPixmap(pixmap)
                self.LinearRegression_imageLabel.setScaledContents(True)
                self.LinearRegression_imageLabel.setGeometry(0, 20, 320, 240)
                self.LinearRegression_imageLabel.setContentsMargins(0, 0, 0, 0)

                self.LinearRegression_img_widget.update()
                self.LinearRegression_img_widget.show()
            else:
                InfoBar.warning(
                    title='注意',
                    content="请先测试模型再查看结果",
                    orient=QtCore.Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM_RIGHT,
                    duration=-1,
                    parent=self
                )
        else:
            InfoBar.warning(
                title='注意',
                content="请先训练并测试模型再查看结果",
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM_RIGHT,
                duration=-1,
                parent=self
            )

    def _reset_progress_ring(self):
        self.LinearRegression_Progress_Ring.setValue(0)
