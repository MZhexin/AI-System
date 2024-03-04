import time

from PySide6 import QtCore, QtGui, QtWidgets

class Ui_SVM(object):
    def setupUi(self, SVM):
        SVM.setObjectName("SVM")
        SVM.setEnabled(True)
        SVM.resize(873, 889)
        SVM.setMinimumSize(QtCore.QSize(500, 400))
        SVM.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SVM_Frame = QtWidgets.QFrame(SVM)
        self.SVM_Frame.setGeometry(QtCore.QRect(10, 40, 700, 600))
        self.SVM_Frame.setMinimumSize(QtCore.QSize(500, 400))
        self.SVM_Frame.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.SVM_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SVM_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SVM_Frame.setObjectName("SVM_Frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SVM_Frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SVM_title_frame = QtWidgets.QFrame(self.SVM_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.SVM_title_frame.sizePolicy().hasHeightForWidth())
        self.SVM_title_frame.setSizePolicy(sizePolicy)
        self.SVM_title_frame.setStyleSheet("")
        self.SVM_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SVM_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SVM_title_frame.setObjectName("SVM_title_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.SVM_title_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SVM_option_frame = QtWidgets.QFrame(self.SVM_title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.SVM_option_frame.sizePolicy().hasHeightForWidth())
        self.SVM_option_frame.setSizePolicy(sizePolicy)
        self.SVM_option_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SVM_option_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SVM_option_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SVM_option_frame.setObjectName("SVM_option_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.SVM_option_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SVM_name = QtWidgets.QLabel(self.SVM_option_frame)
        self.SVM_name.setStyleSheet("font: 75 9pt \"Fixedsys\";")
        self.SVM_name.setObjectName("SVM_name")
        self.horizontalLayout_2.addWidget(self.SVM_name, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.SVM_option_frame)
        self.verticalLayout.addWidget(self.SVM_title_frame)
        self.SVM_show_frame = QtWidgets.QFrame(self.SVM_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.SVM_show_frame.sizePolicy().hasHeightForWidth())
        self.SVM_show_frame.setSizePolicy(sizePolicy)
        self.SVM_show_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(74, 188, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.SVM_show_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SVM_show_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SVM_show_frame.setObjectName("SVM_show_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SVM_show_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SVM_info_frame = QtWidgets.QFrame(self.SVM_show_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.SVM_info_frame.sizePolicy().hasHeightForWidth())
        self.SVM_info_frame.setSizePolicy(sizePolicy)
        self.SVM_info_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.SVM_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SVM_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SVM_info_frame.setObjectName("SVM_info_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.SVM_info_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.SVM_introduction = PlainTextEdit(self.SVM_info_frame)
        self.SVM_introduction.setEnabled(True)
        self.SVM_introduction.setStyleSheet("LineEdit, TextEdit, PlainTextEdit {\n"
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
        self.SVM_introduction.setReadOnly(True)
        self.SVM_introduction.setObjectName("SVM_introduction")
        self.verticalLayout_5.addWidget(self.SVM_introduction, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.SVM_info_frame)
        self.SVM_button_img_frame = QtWidgets.QFrame(self.SVM_show_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.SVM_button_img_frame.sizePolicy().hasHeightForWidth())
        self.SVM_button_img_frame.setSizePolicy(sizePolicy)
        self.SVM_button_img_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.SVM_button_img_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SVM_button_img_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SVM_button_img_frame.setObjectName("SVM_button_img_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.SVM_button_img_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SVM_Button_Frame = QtWidgets.QFrame(self.SVM_button_img_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SVM_Button_Frame.sizePolicy().hasHeightForWidth())
        self.SVM_Button_Frame.setSizePolicy(sizePolicy)
        self.SVM_Button_Frame.setStyleSheet("")
        self.SVM_Button_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SVM_Button_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SVM_Button_Frame.setObjectName("SVM_Button_Frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.SVM_Button_Frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.SVM_button = QtWidgets.QFrame(self.SVM_Button_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.SVM_button.sizePolicy().hasHeightForWidth())
        self.SVM_button.setSizePolicy(sizePolicy)
        self.SVM_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.SVM_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SVM_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SVM_button.setObjectName("SVM_button")
        self.gridLayout = QtWidgets.QGridLayout(self.SVM_button)
        self.gridLayout.setObjectName("gridLayout")
        self.SVM_dataset_label = QtWidgets.QLabel(self.SVM_button)
        self.SVM_dataset_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.SVM_dataset_label.setObjectName("SVM_dataset_label")
        self.gridLayout.addWidget(self.SVM_dataset_label, 0, 0, 1, 1)
        self.SVM_dataset_combobox = ComboBox(self.SVM_button)
        self.SVM_dataset_combobox.setObjectName("SVM_dataset_combobox")
        self.SVM_dataset_combobox.addItem("")
        self.SVM_dataset_combobox.addItem("")
        self.gridLayout.addWidget(self.SVM_dataset_combobox, 0, 1, 1, 1)
        self.SVM_Kernel_label = QtWidgets.QLabel(self.SVM_button)
        self.SVM_Kernel_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.SVM_Kernel_label.setObjectName("SVM_Kernel_label")
        self.gridLayout.addWidget(self.SVM_Kernel_label, 1, 0, 1, 1)
        self.SVM_Kernel_combobox = ComboBox(self.SVM_button)
        self.SVM_Kernel_combobox.setObjectName("SVM_Kernel_combobox")
        self.SVM_Kernel_combobox.addItem("")
        self.SVM_Kernel_combobox.addItem("")
        self.SVM_Kernel_combobox.addItem("")
        self.gridLayout.addWidget(self.SVM_Kernel_combobox, 1, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.SVM_button)
        self.SVM_progress = QtWidgets.QFrame(self.SVM_Button_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.SVM_progress.sizePolicy().hasHeightForWidth())
        self.SVM_progress.setSizePolicy(sizePolicy)
        self.SVM_progress.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.SVM_progress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SVM_progress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SVM_progress.setObjectName("SVM_progress")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.SVM_progress)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.SVM_progress_ring_frame = QtWidgets.QFrame(self.SVM_progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SVM_progress_ring_frame.sizePolicy().hasHeightForWidth())
        self.SVM_progress_ring_frame.setSizePolicy(sizePolicy)
        self.SVM_progress_ring_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SVM_progress_ring_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SVM_progress_ring_frame.setObjectName("SVM_progress_ring_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.SVM_progress_ring_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.SVM_Progress_Ring = ProgressRing(self.SVM_progress_ring_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.SVM_Progress_Ring.sizePolicy().hasHeightForWidth())
        self.SVM_Progress_Ring.setSizePolicy(sizePolicy)
        self.SVM_Progress_Ring.setMinimumSize(QtCore.QSize(10, 10))
        self.SVM_Progress_Ring.setTextVisible(True)
        self.SVM_Progress_Ring.setObjectName("SVM_Progress_Ring")
        self.verticalLayout_8.addWidget(self.SVM_Progress_Ring)
        self.horizontalLayout_5.addWidget(self.SVM_progress_ring_frame)
        self.SVM_progress_label_frame = QtWidgets.QFrame(self.SVM_progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SVM_progress_label_frame.sizePolicy().hasHeightForWidth())
        self.SVM_progress_label_frame.setSizePolicy(sizePolicy)
        self.SVM_progress_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SVM_progress_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SVM_progress_label_frame.setObjectName("SVM_progress_label_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.SVM_progress_label_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.SVM_train_button = PushButton(self.SVM_progress_label_frame)
        self.SVM_train_button.setObjectName("SVM_train_button")
        self.verticalLayout_9.addWidget(self.SVM_train_button)
        self.SVM_test_button = PushButton(self.SVM_progress_label_frame)
        self.SVM_test_button.setObjectName("SVM_test_button")
        self.verticalLayout_9.addWidget(self.SVM_test_button)
        self.SVM_img_button = PushButton(self.SVM_progress_label_frame)
        self.SVM_img_button.setObjectName("SVM_img_button")
        self.verticalLayout_9.addWidget(self.SVM_img_button)
        self.SVM_reset_button = PushButton(self.SVM_progress_label_frame)
        self.SVM_reset_button.setObjectName("SVM_reset_button")
        self.verticalLayout_9.addWidget(self.SVM_reset_button)
        self.horizontalLayout_5.addWidget(self.SVM_progress_label_frame)
        self.verticalLayout_6.addWidget(self.SVM_progress)
        self.horizontalLayout_4.addWidget(self.SVM_Button_Frame)
        self.SVM_img_Frame = QtWidgets.QFrame(self.SVM_button_img_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SVM_img_Frame.sizePolicy().hasHeightForWidth())
        self.SVM_img_Frame.setSizePolicy(sizePolicy)
        self.SVM_img_Frame.setStyleSheet("")
        self.SVM_img_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SVM_img_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SVM_img_Frame.setObjectName("SVM_img_Frame")
        self.SVM_img_widget = QWidget(self.SVM_img_Frame)
        self.SVM_img_widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                          "stop:0 rgba(225, 225, 225, 225), stop:1 rgba(65, 105, 225, 255));")
        self.SVM_img_widget.setGeometry(14, 14, 330, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.SVM_img_widget.setSizePolicy(sizePolicy)
        self.SVM_img_widget.setContentsMargins(0, 0, 0, 0)
        self.SVM_imageLabel = QtWidgets.QLabel(self.SVM_img_widget)

        self.horizontalLayout_4.addWidget(self.SVM_img_Frame)
        self.verticalLayout_2.addWidget(self.SVM_button_img_frame)
        self.verticalLayout.addWidget(self.SVM_show_frame)
        self.retranslateUi(SVM)
        QtCore.QMetaObject.connectSlotsByName(SVM)

    def retranslateUi(self, SVM):
        _translate = QtCore.QCoreApplication.translate
        SVM.setWindowTitle(_translate("SVM", "Form"))
        self.SVM_name.setText(_translate("SVM", "支持向量机算法"))
        self.SVM_introduction.setPlainText(_translate("SVM", "支持向量机（Support Vector Machine, SVM）是一类按监督学习（supervised learning）方式对数据"
                                                             "进行二元分类的广义线性分类器（generalized linear classifier），其决策边界是对学习样本求解的最大"
                                                             "边距超平面（maximum-margin hyperplane） 。与逻辑回归和神经网络相比，支持向量机，在学习复杂的非线"
                                                             "性方程时提供了一种更为清晰，更加强大的方式。\n"
                                                             "假如数据是完全的线性可分的，那么学习到的模型可以称为硬间隔支持向量机。换个说法，硬间隔指的就是完全分类准"
                                                             "确，不能存在分类错误的情况。软间隔，就是允许一定量的样本分类错误。\n"
                                                             "SVM通常使用SMO（序列最小优化）算法来训练。SMO是一种将大优化问题分解为一系列最小问题的算法，这些小问题可"
                                                             "以更有效率地求解。\n"
                                                             "训练过程中，算法确定最优超平面的位置和方向，确保最大化类别之间的边际。支持向量是那些位于边际边缘或违反边际"
                                                             "的数据点，是模型决策的关键。模型参数如C（错误术语的惩罚系数）和核函数的选择对模型的性能和过拟合风险有显著"
                                                             "影响。\n在支持向量机中，一个很重要的概念是核函数。在低维空间计算获得高维空间的计算结果，满足高维，才能在"
                                                             "高维下线性可分。 我们需要引入一个新的概念：核函数。它可以将样本从原始空间映射到一个更高维的特质空间中，使"
                                                             "得样本在新的空间中线性可分。这样我们就可以使用原来的推导来进行计算，只是所有的推导是在新的空间，而不是在原"
                                                             "来的空间中进行，即用核函数来替换当中的内积。常用的核函数有线性核函数、多项式核函数和高斯核函数等，其中只有"
                                                             "高斯核函数需要调参。"))
        self.SVM_dataset_label.setText(_translate("SVM", "数据集"))
        self.SVM_dataset_combobox.setItemText(0, _translate("SVM", "Iris"))
        self.SVM_dataset_combobox.setItemText(1, _translate("SVM", "Wine"))
        self.SVM_Kernel_label.setText(_translate("SVM", "K值"))
        self.SVM_Kernel_combobox.setItemText(0, _translate("SVM", "线性核"))
        self.SVM_Kernel_combobox.setItemText(1, _translate("SVM", "高斯核"))
        self.SVM_Kernel_combobox.setItemText(2, _translate("SVM", "多项式核"))
        self.SVM_train_button.setText(_translate("SVM", "开始训练"))
        self.SVM_test_button.setText(_translate("SVM", "开始测试"))
        self.SVM_img_button.setText(_translate("SVM", "显示结果"))
        self.SVM_reset_button.setText(_translate("SVM", "重置进度条"))

from qfluentwidgets import PlainTextEdit, ProgressRing, PushButton, ComboBox, InfoBarPosition, InfoBar

from PySide6.QtWidgets import QWidget

from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.svm import SVC

import matplotlib.pyplot as plt

import math
import numpy as np
from tqdm import tqdm

class SVMInterface(QWidget, Ui_SVM):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.SVM_img_widget.close()

        self.SVM_train_button.clicked.connect(self._start_train)

        self.SVM_test_button.clicked.connect(self._start_test)

        self.SVM_img_button.clicked.connect(self._show_result)

        self.SVM_reset_button.clicked.connect(self._reset_progress_ring)

    def _start_train(self):
        # 加载数据集
        if self.SVM_dataset_combobox.currentText() == 'Iris':
            dataset = load_iris()
        else:
            dataset = load_wine()

        X = dataset['data']
        Y = dataset['target']

        X = X[:, :2]

        # 数据划分
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

        for i in tqdm(range(len(Y_train))):
            self.SVM_Progress_Ring.setValue(math.ceil((i + 1) / len(Y_train) * 100))

        # 判断用哪个核函数
        kernel_dic = {"线性核": "linear",
                      "高斯核": "rbf",
                      "多项式核": "poly"}

        # 训练阶段
        self.model = SVC(kernel=kernel_dic[self.SVM_Kernel_combobox.currentText()], random_state=42)
        self.model.fit(X_train, Y_train)

        self.has_test = False

    def _start_test(self):
        if hasattr(self, "model"):
            if self.SVM_dataset_combobox.currentText() == 'Iris':
                dataset = load_iris()
            else:
                dataset = load_wine()

            X = dataset['data']
            Y = dataset['target']

            X = X[:, :2]

            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

            for i in tqdm(range(len(Y_train))):
                self.SVM_Progress_Ring.setValue(math.ceil((i + 1) / len(Y_train) * 100))

            # 可视化
            h = .02  # 网格中的步长
            x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
            y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

            xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                                 np.arange(y_min, y_max, h))

            Z = self.model.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)

            plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

            plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.coolwarm, edgecolor='k', s=20)
            plt.xlim(xx.min(), xx.max())
            plt.ylim(yy.min(), yy.max())
            plt.xticks(())
            plt.yticks(())

            plt.savefig('Resource/results/SVM_result.png', transparent=True)

            # 准确率
            Y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(Y_test, Y_pred) * 100

            # 弹出提示框
            InfoBar.success(
                title='准确率',
                content="当前模型准确率为{:.2f}%".format(accuracy),
                orient=QtCore.Qt.Vertical,
                isClosable=True,
                position=InfoBarPosition.BOTTOM_RIGHT,
                duration=-1,
                parent=self
            )

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
        if hasattr(self, 'model'):
            if hasattr(self, 'has_test') and self.has_test:
                imgpath = 'Resource/results/SVM_result.png'

                pixmap = QtGui.QPixmap(imgpath)
                self.SVM_imageLabel.setPixmap(pixmap)
                self.SVM_imageLabel.setScaledContents(True)
                self.SVM_imageLabel.setGeometry(0, 20, 320, 240)
                self.SVM_imageLabel.setContentsMargins(0, 0, 0, 0)

                self.SVM_img_widget.update()
                self.SVM_img_widget.show()
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
        self.SVM_Progress_Ring.setValue(0)
