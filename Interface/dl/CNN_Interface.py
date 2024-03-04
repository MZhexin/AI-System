import time

from PySide6 import QtCore, QtGui, QtWidgets

class Ui_CNN(object):
    def setupUi(self, CNN):
        CNN.setObjectName("CNN")
        CNN.setEnabled(True)
        CNN.resize(873, 889)
        CNN.setMinimumSize(QtCore.QSize(500, 400))
        CNN.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.CNN_Frame = QtWidgets.QFrame(CNN)
        self.CNN_Frame.setGeometry(QtCore.QRect(10, 40, 700, 600))
        self.CNN_Frame.setMinimumSize(QtCore.QSize(500, 400))
        self.CNN_Frame.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.CNN_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CNN_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CNN_Frame.setObjectName("CNN_Frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CNN_Frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CNN_title_frame = QtWidgets.QFrame(self.CNN_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.CNN_title_frame.sizePolicy().hasHeightForWidth())
        self.CNN_title_frame.setSizePolicy(sizePolicy)
        self.CNN_title_frame.setStyleSheet("")
        self.CNN_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CNN_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CNN_title_frame.setObjectName("CNN_title_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.CNN_title_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.CNN_option_frame = QtWidgets.QFrame(self.CNN_title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.CNN_option_frame.sizePolicy().hasHeightForWidth())
        self.CNN_option_frame.setSizePolicy(sizePolicy)
        self.CNN_option_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CNN_option_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CNN_option_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CNN_option_frame.setObjectName("CNN_option_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.CNN_option_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.CNN_name = QtWidgets.QLabel(self.CNN_option_frame)
        self.CNN_name.setStyleSheet("font: 75 9pt \"Fixedsys\";")
        self.CNN_name.setObjectName("CNN_name")
        self.horizontalLayout_2.addWidget(self.CNN_name, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.CNN_option_frame)
        self.verticalLayout.addWidget(self.CNN_title_frame)
        self.CNN_show_frame = QtWidgets.QFrame(self.CNN_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.CNN_show_frame.sizePolicy().hasHeightForWidth())
        self.CNN_show_frame.setSizePolicy(sizePolicy)
        self.CNN_show_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(74, 188, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.CNN_show_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CNN_show_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CNN_show_frame.setObjectName("CNN_show_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.CNN_show_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CNN_info_frame = QtWidgets.QFrame(self.CNN_show_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.CNN_info_frame.sizePolicy().hasHeightForWidth())
        self.CNN_info_frame.setSizePolicy(sizePolicy)
        self.CNN_info_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.CNN_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CNN_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CNN_info_frame.setObjectName("CNN_info_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.CNN_info_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.CNN_introduction = PlainTextEdit(self.CNN_info_frame)
        self.CNN_introduction.setEnabled(True)
        self.CNN_introduction.setStyleSheet("LineEdit, TextEdit, PlainTextEdit {\n"
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
        self.CNN_introduction.setReadOnly(True)
        self.CNN_introduction.setObjectName("CNN_introduction")
        self.verticalLayout_5.addWidget(self.CNN_introduction, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.CNN_info_frame)
        self.CNN_button_img_frame = QtWidgets.QFrame(self.CNN_show_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.CNN_button_img_frame.sizePolicy().hasHeightForWidth())
        self.CNN_button_img_frame.setSizePolicy(sizePolicy)
        self.CNN_button_img_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.CNN_button_img_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CNN_button_img_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CNN_button_img_frame.setObjectName("CNN_button_img_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.CNN_button_img_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.CNN_Button_Frame = QtWidgets.QFrame(self.CNN_button_img_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CNN_Button_Frame.sizePolicy().hasHeightForWidth())
        self.CNN_Button_Frame.setSizePolicy(sizePolicy)
        self.CNN_Button_Frame.setStyleSheet("")
        self.CNN_Button_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CNN_Button_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CNN_Button_Frame.setObjectName("CNN_Button_Frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.CNN_Button_Frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.CNN_buttons_area = QtWidgets.QFrame(self.CNN_Button_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.CNN_buttons_area.sizePolicy().hasHeightForWidth())
        self.CNN_buttons_area.setSizePolicy(sizePolicy)
        self.CNN_buttons_area.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.CNN_buttons_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CNN_buttons_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CNN_buttons_area.setObjectName("CNN_buttons_area")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.CNN_buttons_area)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cnn_confusion_matrix = PushButton(self.CNN_buttons_area)
        self.cnn_confusion_matrix.setObjectName("cnn_confusion_matrix")
        self.gridLayout_2.addWidget(self.cnn_confusion_matrix, 1, 1, 1, 1)
        self.cnn_loss_func = PushButton(self.CNN_buttons_area)
        self.cnn_loss_func.setObjectName("cnn_loss_func")
        self.gridLayout_2.addWidget(self.cnn_loss_func, 1, 2, 1, 1)
        self.cnn_cifar10 = PushButton(self.CNN_buttons_area)
        self.cnn_cifar10.setObjectName("cnn_cifar10")
        self.gridLayout_2.addWidget(self.cnn_cifar10, 0, 2, 1, 1)
        self.cnn_mnist = PushButton(self.CNN_buttons_area)
        self.cnn_mnist.setObjectName("cnn_mnist")
        self.gridLayout_2.addWidget(self.cnn_mnist, 0, 1, 1, 1)
        self.cnn_dataset_label = QtWidgets.QLabel(self.CNN_buttons_area)
        self.cnn_dataset_label.setObjectName("cnn_dataset_label")
        self.gridLayout_2.addWidget(self.cnn_dataset_label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.cnn_visual_label = QtWidgets.QLabel(self.CNN_buttons_area)
        self.cnn_visual_label.setObjectName("cnn_visual_label")
        self.gridLayout_2.addWidget(self.cnn_visual_label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.cnn_show_result = PushButton(self.CNN_buttons_area)
        self.cnn_show_result.setObjectName("cnn_show_result")
        self.gridLayout_2.addWidget(self.cnn_show_result, 2, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_2)
        self.verticalLayout_6.addWidget(self.CNN_buttons_area)
        self.horizontalLayout_4.addWidget(self.CNN_Button_Frame)
        self.CNN_img_Frame = QtWidgets.QFrame(self.CNN_button_img_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CNN_img_Frame.sizePolicy().hasHeightForWidth())
        self.CNN_img_Frame.setSizePolicy(sizePolicy)
        self.CNN_img_Frame.setStyleSheet("")
        self.CNN_img_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CNN_img_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CNN_img_Frame.setObjectName("CNN_img_Frame")
        self.CNN_img_widget = QWidget(self.CNN_img_Frame)
        self.CNN_img_widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                          "stop:0 rgba(225, 225, 225, 225), stop:1 rgba(65, 105, 225, 255));")
        self.CNN_img_widget.setGeometry(14, 14, 330, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.CNN_img_widget.setSizePolicy(sizePolicy)
        self.CNN_img_widget.setContentsMargins(0, 0, 0, 0)
        self.CNN_imageLabel = QtWidgets.QLabel(self.CNN_img_widget)
        self.horizontalLayout_4.addWidget(self.CNN_img_Frame)
        self.horizontalLayout_4.addWidget(self.CNN_img_Frame)
        self.verticalLayout_2.addWidget(self.CNN_button_img_frame)
        self.verticalLayout.addWidget(self.CNN_show_frame)
        self.CNN_buttons_area_label_frame = QtWidgets.QFrame(CNN)
        self.CNN_buttons_area_label_frame.setGeometry(QtCore.QRect(150, 760, 287, 155))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CNN_buttons_area_label_frame.sizePolicy().hasHeightForWidth())
        self.CNN_buttons_area_label_frame.setSizePolicy(sizePolicy)
        self.CNN_buttons_area_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CNN_buttons_area_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CNN_buttons_area_label_frame.setObjectName("CNN_buttons_area_label_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.CNN_buttons_area_label_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.retranslateUi(CNN)
        QtCore.QMetaObject.connectSlotsByName(CNN)

    def retranslateUi(self, CNN):
        _translate = QtCore.QCoreApplication.translate
        CNN.setWindowTitle(_translate("CNN", "Form"))
        self.CNN_name.setText(_translate("CNN", "卷积神经网络"))
        self.CNN_introduction.setPlainText(_translate("CNN", "卷积神经网络（Convolutional Neural Networks, CNN）是一种深度学习模型或类似于人工神经网络的多层感知器，常用来分析视觉图像。\n"
"一个卷积神经网络主要由以下5层组成：数据输入层、卷积计算层、ReLU激励层、池化层和全连接层。\n"
"数据输入层要做的处理主要是对原始图像数据进行预处理。卷积计算层主要通过滤波器，对图像信息进行平滑操作。"
"ReLU激励层把卷积层输出结果做非线性映射。池化层夹在连续的卷积层中间，用于压缩数据和参数的量，减小过拟合"
"。两层之间所有神经元都有权重连接，通常全连接层在卷积神经网络尾部。"))
        self.cnn_confusion_matrix.setText(_translate("CNN", "混淆矩阵"))
        self.cnn_loss_func.setText(_translate("CNN", "损失函数"))
        self.cnn_cifar10.setText(_translate("CNN", "CIFAR-10"))
        self.cnn_mnist.setText(_translate("CNN", "MNIST"))
        self.cnn_dataset_label.setText(_translate("CNN", "数据集"))
        self.cnn_visual_label.setText(_translate("CNN", "可视化"))
        self.cnn_show_result.setText(_translate("CNN", "显示结果"))

from qfluentwidgets import PlainTextEdit, PushButton, InfoBar, InfoBarPosition

from PySide6.QtWidgets import QWidget

class CNNInterface(QWidget, Ui_CNN):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.CNN_img_widget.close()

        InfoBar.info(
            title='注意',
            content="由于深度学习算法的训练时间较长，我们仅提供已训练好的结果供用户学习",
            orient=QtCore.Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=-1,
            parent=self
        )

        InfoBar.info(
            title='参数配置',
            content="Epoch为20  学习率为0.001  优化器为Adam",
            orient=QtCore.Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=-1,
            parent=self
        )

        # 选择数据集
        self.cnn_mnist.clicked.connect(self._dataset_mnist)
        self.cnn_cifar10.clicked.connect(self._dataset_cifar10)

        # 选择可视化结果
        self.cnn_confusion_matrix.clicked.connect(self._visual_confu)
        self.cnn_loss_func.clicked.connect(self._visual_loss)
        
        # 显示结果
        self.cnn_show_result.clicked.connect(self._show_result)

    def _dataset_mnist(self):
        self.dataset = 'mnist'

    def _dataset_cifar10(self):
        self.dataset = 'cifar10'

    def _visual_confu(self):
        self.visual = 'confu'

    def _visual_loss(self):
        self.visual = 'loss'

    def _show_result(self):
        if hasattr(self, "dataset") and hasattr(self, "visual"):
            imgpath = 'Resource/results/CNN_{0}_{1}.png'.format(self.dataset, self.visual)

            pixmap = QtGui.QPixmap(imgpath)
            self.CNN_imageLabel.setPixmap(pixmap)
            self.CNN_imageLabel.setScaledContents(True)
            self.CNN_imageLabel.setGeometry(0, 20, 320, 240)
            self.CNN_imageLabel.setContentsMargins(0, 0, 0, 0)

            self.CNN_img_widget.update()
            self.CNN_img_widget.show()
        else:
            InfoBar.warning(
                title='注意',
                content="请先选择数据集和可视化内容",
                orient=QtCore.Qt.Vertical,
                isClosable=True,
                position=InfoBarPosition.BOTTOM_RIGHT,
                duration=-1,
                parent=self
            )