import time

from PySide6 import QtCore, QtGui, QtWidgets

class Ui_KNN(object):
    def setupUi(self, KNN):
        KNN.setObjectName("KNN")
        KNN.setEnabled(True)
        KNN.resize(873, 889)
        KNN.setMinimumSize(QtCore.QSize(500, 400))
        KNN.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.KNN_Frame = QtWidgets.QFrame(KNN)
        self.KNN_Frame.setGeometry(QtCore.QRect(10, 40, 700, 600))
        self.KNN_Frame.setMinimumSize(QtCore.QSize(500, 400))
        self.KNN_Frame.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.KNN_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.KNN_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.KNN_Frame.setObjectName("KNN_Frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.KNN_Frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.KNN_title_frame = QtWidgets.QFrame(self.KNN_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.KNN_title_frame.sizePolicy().hasHeightForWidth())
        self.KNN_title_frame.setSizePolicy(sizePolicy)
        self.KNN_title_frame.setStyleSheet("")
        self.KNN_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.KNN_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.KNN_title_frame.setObjectName("KNN_title_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.KNN_title_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.KNN_option_frame = QtWidgets.QFrame(self.KNN_title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.KNN_option_frame.sizePolicy().hasHeightForWidth())
        self.KNN_option_frame.setSizePolicy(sizePolicy)
        self.KNN_option_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.KNN_option_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.KNN_option_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.KNN_option_frame.setObjectName("KNN_option_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.KNN_option_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.knn_name = QtWidgets.QLabel(self.KNN_option_frame)
        self.knn_name.setStyleSheet("font: 75 9pt \"Fixedsys\";")
        self.knn_name.setObjectName("knn_name")
        self.horizontalLayout_2.addWidget(self.knn_name, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.KNN_option_frame)
        self.verticalLayout.addWidget(self.KNN_title_frame)
        self.KNN_show_frame = QtWidgets.QFrame(self.KNN_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.KNN_show_frame.sizePolicy().hasHeightForWidth())
        self.KNN_show_frame.setSizePolicy(sizePolicy)
        self.KNN_show_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(74, 188, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.KNN_show_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.KNN_show_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.KNN_show_frame.setObjectName("KNN_show_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.KNN_show_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.KNN_info_frame = QtWidgets.QFrame(self.KNN_show_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.KNN_info_frame.sizePolicy().hasHeightForWidth())
        self.KNN_info_frame.setSizePolicy(sizePolicy)
        self.KNN_info_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.KNN_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.KNN_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.KNN_info_frame.setObjectName("KNN_info_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.KNN_info_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.KNN_introduction = PlainTextEdit(self.KNN_info_frame)
        self.KNN_introduction.setEnabled(True)
        self.KNN_introduction.setStyleSheet("LineEdit, TextEdit, PlainTextEdit {\n"
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
        self.KNN_introduction.setReadOnly(True)
        self.KNN_introduction.setObjectName("KNN_introduction")
        self.verticalLayout_5.addWidget(self.KNN_introduction, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.KNN_info_frame)
        self.KNN_button_img_frame = QtWidgets.QFrame(self.KNN_show_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.KNN_button_img_frame.sizePolicy().hasHeightForWidth())
        self.KNN_button_img_frame.setSizePolicy(sizePolicy)
        self.KNN_button_img_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.KNN_button_img_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.KNN_button_img_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.KNN_button_img_frame.setObjectName("KNN_button_img_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.KNN_button_img_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.KNN_Button_Frame = QtWidgets.QFrame(self.KNN_button_img_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KNN_Button_Frame.sizePolicy().hasHeightForWidth())
        self.KNN_Button_Frame.setSizePolicy(sizePolicy)
        self.KNN_Button_Frame.setStyleSheet("")
        self.KNN_Button_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.KNN_Button_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.KNN_Button_Frame.setObjectName("KNN_Button_Frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.KNN_Button_Frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.knn_button = QtWidgets.QFrame(self.KNN_Button_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.knn_button.sizePolicy().hasHeightForWidth())
        self.knn_button.setSizePolicy(sizePolicy)
        self.knn_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.knn_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.knn_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.knn_button.setObjectName("knn_button")
        self.gridLayout = QtWidgets.QGridLayout(self.knn_button)
        self.gridLayout.setObjectName("gridLayout")
        self.knn_dataset_label = QtWidgets.QLabel(self.knn_button)
        self.knn_dataset_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.knn_dataset_label.setObjectName("knn_dataset_label")
        self.gridLayout.addWidget(self.knn_dataset_label, 0, 0, 1, 1)
        self.knn_dataset_combobox = ComboBox(self.knn_button)
        self.knn_dataset_combobox.setObjectName("knn_dataset_combobox")
        self.knn_dataset_combobox.addItem("")
        self.knn_dataset_combobox.addItem("")
        self.gridLayout.addWidget(self.knn_dataset_combobox, 0, 1, 1, 1)
        self.knn_Kvalue_label = QtWidgets.QLabel(self.knn_button)
        self.knn_Kvalue_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.knn_Kvalue_label.setObjectName("knn_Kvalue_label")
        self.gridLayout.addWidget(self.knn_Kvalue_label, 1, 0, 1, 1)
        self.knn_Kvalue_combobox = ComboBox(self.knn_button)
        self.knn_Kvalue_combobox.setObjectName("knn_Kvalue_combobox")
        self.knn_Kvalue_combobox.addItem("")
        self.knn_Kvalue_combobox.addItem("")
        self.gridLayout.addWidget(self.knn_Kvalue_combobox, 1, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.knn_button)
        self.knn_progress = QtWidgets.QFrame(self.KNN_Button_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.knn_progress.sizePolicy().hasHeightForWidth())
        self.knn_progress.setSizePolicy(sizePolicy)
        self.knn_progress.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.knn_progress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.knn_progress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.knn_progress.setObjectName("knn_progress")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.knn_progress)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.knn_progress_ring_frame = QtWidgets.QFrame(self.knn_progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.knn_progress_ring_frame.sizePolicy().hasHeightForWidth())
        self.knn_progress_ring_frame.setSizePolicy(sizePolicy)
        self.knn_progress_ring_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.knn_progress_ring_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.knn_progress_ring_frame.setObjectName("knn_progress_ring_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.knn_progress_ring_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.KNN_Progress_Ring = ProgressRing(self.knn_progress_ring_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.KNN_Progress_Ring.sizePolicy().hasHeightForWidth())
        self.KNN_Progress_Ring.setSizePolicy(sizePolicy)
        self.KNN_Progress_Ring.setMinimumSize(QtCore.QSize(10, 10))
        self.KNN_Progress_Ring.setTextVisible(True)
        self.KNN_Progress_Ring.setObjectName("KNN_Progress_Ring")
        self.verticalLayout_8.addWidget(self.KNN_Progress_Ring)
        self.horizontalLayout_5.addWidget(self.knn_progress_ring_frame)
        self.knn_progress_label_frame = QtWidgets.QFrame(self.knn_progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.knn_progress_label_frame.sizePolicy().hasHeightForWidth())
        self.knn_progress_label_frame.setSizePolicy(sizePolicy)
        self.knn_progress_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.knn_progress_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.knn_progress_label_frame.setObjectName("knn_progress_label_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.knn_progress_label_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.knn_train_button = PushButton(self.knn_progress_label_frame)
        self.knn_train_button.setObjectName("knn_train_button")
        self.verticalLayout_9.addWidget(self.knn_train_button)
        self.knn_test_button = PushButton(self.knn_progress_label_frame)
        self.knn_test_button.setObjectName("knn_test_button")
        self.verticalLayout_9.addWidget(self.knn_test_button)
        self.knn_img_button = PushButton(self.knn_progress_label_frame)
        self.knn_img_button.setObjectName("knn_img_button")
        self.verticalLayout_9.addWidget(self.knn_img_button)
        self.knn_reset_button = PushButton(self.knn_progress_label_frame)
        self.knn_reset_button.setObjectName("knn_reset_button")
        self.verticalLayout_9.addWidget(self.knn_reset_button)
        self.horizontalLayout_5.addWidget(self.knn_progress_label_frame)
        self.verticalLayout_6.addWidget(self.knn_progress)
        self.horizontalLayout_4.addWidget(self.KNN_Button_Frame)
        self.KNN_img_Frame = QtWidgets.QFrame(self.KNN_button_img_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KNN_img_Frame.sizePolicy().hasHeightForWidth())
        self.KNN_img_Frame.setSizePolicy(sizePolicy)
        self.KNN_img_Frame.setStyleSheet("")
        self.KNN_img_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.KNN_img_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.KNN_img_Frame.setObjectName("KNN_img_Frame")
        self.knn_img_widget = QWidget(self.KNN_img_Frame)
        self.knn_img_widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                          "stop:0 rgba(225, 225, 225, 225), stop:1 rgba(65, 105, 225, 255));")
        self.knn_img_widget.setGeometry(14, 14, 330, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.knn_img_widget.setSizePolicy(sizePolicy)
        self.knn_img_widget.setContentsMargins(0, 0, 0, 0)
        self.KNN_imageLabel = QtWidgets.QLabel(self.knn_img_widget)

        self.horizontalLayout_4.addWidget(self.KNN_img_Frame)
        self.verticalLayout_2.addWidget(self.KNN_button_img_frame)
        self.verticalLayout.addWidget(self.KNN_show_frame)
        self.retranslateUi(KNN)
        QtCore.QMetaObject.connectSlotsByName(KNN)

    def retranslateUi(self, KNN):
        _translate = QtCore.QCoreApplication.translate
        KNN.setWindowTitle(_translate("KNN", "Form"))
        self.knn_name.setText(_translate("KNN", "K-近邻算法"))
        self.KNN_introduction.setPlainText(_translate("KNN", "K-近邻算法（K-Nearest Neighbors）是一种基于实例的学习方法，或者说是一种基于邻近度的算法。它被广泛应用于分类和回归问题。KNN算法的核心思想非常直观,即一个样本的类别由其最接近的K个邻居的类别决定。\n"
"算法步骤如下：\n"
"1. 确定K值：K是一个正整数，表示邻居的数量。K的选择对算法的结果有很大影响。太小的K使模型对噪声敏感，而太大的K会使模型过于简化；\n"
"2. 计算距离：计算待分类点与其他所有点之间的距离。距离的计算方法多样，常见的有欧氏距离、曼哈顿距离等；\n"
"3. 找到最近的K个邻居：根据距离远近，选择距离最小的K个点作为最近的邻居；\n"
"4. 进行决策：在K个最近邻居中，数一数哪个类别最多，那个类别就是待分类点的类别。"))
        self.knn_dataset_label.setText(_translate("KNN", "数据集"))
        self.knn_dataset_combobox.setItemText(0, _translate("KNN", "Iris"))
        self.knn_dataset_combobox.setItemText(1, _translate("KNN", "Wine"))
        self.knn_Kvalue_label.setText(_translate("KNN", "K值"))
        self.knn_Kvalue_combobox.setItemText(0, _translate("KNN", "3"))
        self.knn_Kvalue_combobox.setItemText(1, _translate("KNN", "5"))
        self.knn_train_button.setText(_translate("KNN", "开始训练"))
        self.knn_test_button.setText(_translate("KNN", "开始测试"))
        self.knn_img_button.setText(_translate("KNN", "显示结果"))
        self.knn_reset_button.setText(_translate("KNN", "重置进度条"))

from qfluentwidgets import PlainTextEdit, ProgressRing, PushButton, ComboBox, InfoBarPosition, InfoBar

from PySide6.QtWidgets import QWidget

from sklearn.datasets import load_wine
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import matplotlib.pyplot as plt

import math
from tqdm import tqdm

class KNNInterface(QWidget, Ui_KNN):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.knn_img_widget.close()

        self.knn_train_button.clicked.connect(self._start_train)

        self.knn_test_button.clicked.connect(self._start_test)

        self.knn_img_button.clicked.connect(self._show_result)

        self.knn_reset_button.clicked.connect(self._reset_progress_ring)


    def _start_train(self):
        # 加载数据集
        if self.knn_dataset_combobox.currentText() == 'Iris':
             dataset = load_iris()
        else:
             dataset = load_wine()

        X = dataset['data']
        Y = dataset['target']

        # 数据划分
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

        for i in tqdm(range(len(Y_train))):
            self.KNN_Progress_Ring.setValue(math.ceil((i + 1) / len(Y_train) * 100))

        # 训练阶段
        self.model = KNeighborsClassifier(n_neighbors=int(self.knn_Kvalue_combobox.currentText()))
        self.model.fit(X_train, Y_train)

        self.has_test = False

    def _start_test(self):
        if hasattr(self, "model"):
            if self.knn_dataset_combobox.currentText() == 'Iris':
                    dataset = load_iris()
            else:
                    dataset = load_wine()

            X = dataset['data']
            Y = dataset['target']

            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

            Y_pred = self.model.predict(X_test)

            # 可视化
            plt.clf()
            plt.scatter(X_train[:, 0], X_train[:, 1], c=Y_train, alpha=0.3)

            correct_num = 0

            for i in tqdm(range(len(X_test))):
                self.KNN_Progress_Ring.setValue(math.ceil((i + 1) / len(Y_test) * 100))
                if Y_pred[i] == Y_test[i]:
                        correct_num += 1
                        plt.scatter(X_test[i][0], X_test[i][1], color="green")
                else:
                        plt.scatter(X_test[i][0], X_test[i][1], color="red")

            plt.savefig('Resource/results/knn_result.png', transparent=True)

            # 准确率
            accuracy = (correct_num / len(Y_test)) * 100

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
                imgpath = 'Resource/results/knn_result.png'

                pixmap = QtGui.QPixmap(imgpath)
                self.KNN_imageLabel.setPixmap(pixmap)
                self.KNN_imageLabel.setScaledContents(True)
                self.KNN_imageLabel.setGeometry(0, 20, 320, 240)
                self.KNN_imageLabel.setContentsMargins(0, 0, 0, 0)

                self.knn_img_widget.update()
                self.knn_img_widget.show()
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
        self.KNN_Progress_Ring.setValue(0)

