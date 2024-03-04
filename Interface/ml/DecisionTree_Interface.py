import time

from PySide6 import QtCore, QtGui, QtWidgets

class Ui_decision_tree(object):
    def setupUi(self, decision_tree):
        decision_tree.setObjectName("decision_tree")
        decision_tree.setEnabled(True)
        decision_tree.resize(873, 889)
        decision_tree.setMinimumSize(QtCore.QSize(500, 400))
        decision_tree.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.decision_tree_Frame = QtWidgets.QFrame(decision_tree)
        self.decision_tree_Frame.setGeometry(QtCore.QRect(10, 40, 700, 600))
        self.decision_tree_Frame.setMinimumSize(QtCore.QSize(500, 400))
        self.decision_tree_Frame.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.decision_tree_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision_tree_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision_tree_Frame.setObjectName("decision_tree_Frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.decision_tree_Frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.decision_tree_title_frame = QtWidgets.QFrame(self.decision_tree_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.decision_tree_title_frame.sizePolicy().hasHeightForWidth())
        self.decision_tree_title_frame.setSizePolicy(sizePolicy)
        self.decision_tree_title_frame.setStyleSheet("")
        self.decision_tree_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision_tree_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision_tree_title_frame.setObjectName("decision_tree_title_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.decision_tree_title_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.decision_tree_option_frame = QtWidgets.QFrame(self.decision_tree_title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.decision_tree_option_frame.sizePolicy().hasHeightForWidth())
        self.decision_tree_option_frame.setSizePolicy(sizePolicy)
        self.decision_tree_option_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.decision_tree_option_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision_tree_option_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision_tree_option_frame.setObjectName("decision_tree_option_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.decision_tree_option_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.decision_tree_name = QtWidgets.QLabel(self.decision_tree_option_frame)
        self.decision_tree_name.setStyleSheet("font: 75 9pt \"Fixedsys\";")
        self.decision_tree_name.setObjectName("decision_tree_name")
        self.horizontalLayout_2.addWidget(self.decision_tree_name, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.decision_tree_option_frame)
        self.verticalLayout.addWidget(self.decision_tree_title_frame)
        self.decision_tree_show_frame = QtWidgets.QFrame(self.decision_tree_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.decision_tree_show_frame.sizePolicy().hasHeightForWidth())
        self.decision_tree_show_frame.setSizePolicy(sizePolicy)
        self.decision_tree_show_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(74, 188, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.decision_tree_show_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision_tree_show_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision_tree_show_frame.setObjectName("decision_tree_show_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.decision_tree_show_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.decision_tree_info_frame = QtWidgets.QFrame(self.decision_tree_show_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.decision_tree_info_frame.sizePolicy().hasHeightForWidth())
        self.decision_tree_info_frame.setSizePolicy(sizePolicy)
        self.decision_tree_info_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.decision_tree_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision_tree_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision_tree_info_frame.setObjectName("decision_tree_info_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.decision_tree_info_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.decision_tree_introduction = PlainTextEdit(self.decision_tree_info_frame)
        self.decision_tree_introduction.setEnabled(True)
        self.decision_tree_introduction.setStyleSheet("LineEdit, TextEdit, PlainTextEdit {\n"
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
        self.decision_tree_introduction.setReadOnly(True)
        self.decision_tree_introduction.setObjectName("decision_tree_introduction")
        self.verticalLayout_5.addWidget(self.decision_tree_introduction, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.decision_tree_info_frame)
        self.decision_tree_button_img_frame = QtWidgets.QFrame(self.decision_tree_show_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.decision_tree_button_img_frame.sizePolicy().hasHeightForWidth())
        self.decision_tree_button_img_frame.setSizePolicy(sizePolicy)
        self.decision_tree_button_img_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.decision_tree_button_img_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision_tree_button_img_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision_tree_button_img_frame.setObjectName("decision_tree_button_img_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.decision_tree_button_img_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.decision_tree_Button_Frame = QtWidgets.QFrame(self.decision_tree_button_img_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decision_tree_Button_Frame.sizePolicy().hasHeightForWidth())
        self.decision_tree_Button_Frame.setSizePolicy(sizePolicy)
        self.decision_tree_Button_Frame.setStyleSheet("")
        self.decision_tree_Button_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision_tree_Button_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision_tree_Button_Frame.setObjectName("decision_tree_Button_Frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.decision_tree_Button_Frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.decision_tree_button = QtWidgets.QFrame(self.decision_tree_Button_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.decision_tree_button.sizePolicy().hasHeightForWidth())
        self.decision_tree_button.setSizePolicy(sizePolicy)
        self.decision_tree_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.decision_tree_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision_tree_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision_tree_button.setObjectName("decision_tree_button")
        self.gridLayout = QtWidgets.QGridLayout(self.decision_tree_button)
        self.gridLayout.setObjectName("gridLayout")
        self.decision_tree_dataset_label = QtWidgets.QLabel(self.decision_tree_button)
        self.decision_tree_dataset_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.decision_tree_dataset_label.setObjectName("decision_tree_dataset_label")
        self.gridLayout.addWidget(self.decision_tree_dataset_label, 0, 0, 1, 1)
        self.decision_tree_dataset_combobox = ComboBox(self.decision_tree_button)
        self.decision_tree_dataset_combobox.setObjectName("decision_tree_dataset_combobox")
        self.decision_tree_dataset_combobox.addItem("")
        self.decision_tree_dataset_combobox.addItem("")
        self.gridLayout.addWidget(self.decision_tree_dataset_combobox, 0, 1, 1, 1)
        self.decision_tree_MaxDepth_label = QtWidgets.QLabel(self.decision_tree_button)
        self.decision_tree_MaxDepth_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.decision_tree_MaxDepth_label.setObjectName("decision_tree_MaxDepth_label")
        self.gridLayout.addWidget(self.decision_tree_MaxDepth_label, 1, 0, 1, 1)
        self.decision_tree_MaxDepth_combobox = ComboBox(self.decision_tree_button)
        self.decision_tree_MaxDepth_combobox.setObjectName("decision_tree_MaxDepth_combobox")
        self.decision_tree_MaxDepth_combobox.addItem("")
        self.decision_tree_MaxDepth_combobox.addItem("")
        self.gridLayout.addWidget(self.decision_tree_MaxDepth_combobox, 1, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.decision_tree_button)
        self.decision_tree_progress = QtWidgets.QFrame(self.decision_tree_Button_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.decision_tree_progress.sizePolicy().hasHeightForWidth())
        self.decision_tree_progress.setSizePolicy(sizePolicy)
        self.decision_tree_progress.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.decision_tree_progress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision_tree_progress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision_tree_progress.setObjectName("decision_tree_progress")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.decision_tree_progress)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.decision_tree_progress_ring_frame = QtWidgets.QFrame(self.decision_tree_progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decision_tree_progress_ring_frame.sizePolicy().hasHeightForWidth())
        self.decision_tree_progress_ring_frame.setSizePolicy(sizePolicy)
        self.decision_tree_progress_ring_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision_tree_progress_ring_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision_tree_progress_ring_frame.setObjectName("decision_tree_progress_ring_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.decision_tree_progress_ring_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.decision_tree_Progress_Ring = ProgressRing(self.decision_tree_progress_ring_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.decision_tree_Progress_Ring.sizePolicy().hasHeightForWidth())
        self.decision_tree_Progress_Ring.setSizePolicy(sizePolicy)
        self.decision_tree_Progress_Ring.setMinimumSize(QtCore.QSize(10, 10))
        self.decision_tree_Progress_Ring.setTextVisible(True)
        self.decision_tree_Progress_Ring.setObjectName("decision_tree_Progress_Ring")
        self.verticalLayout_8.addWidget(self.decision_tree_Progress_Ring)
        self.horizontalLayout_5.addWidget(self.decision_tree_progress_ring_frame)
        self.decision_tree_progress_label_frame = QtWidgets.QFrame(self.decision_tree_progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decision_tree_progress_label_frame.sizePolicy().hasHeightForWidth())
        self.decision_tree_progress_label_frame.setSizePolicy(sizePolicy)
        self.decision_tree_progress_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision_tree_progress_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision_tree_progress_label_frame.setObjectName("decision_tree_progress_label_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.decision_tree_progress_label_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.decision_tree_train_button = PushButton(self.decision_tree_progress_label_frame)
        self.decision_tree_train_button.setObjectName("decision_tree_train_button")
        self.verticalLayout_9.addWidget(self.decision_tree_train_button)
        self.decision_tree_img_button = PushButton(self.decision_tree_progress_label_frame)
        self.decision_tree_img_button.setObjectName("decision_tree_img_button")
        self.verticalLayout_9.addWidget(self.decision_tree_img_button)
        self.decision_tree_reset_button = PushButton(self.decision_tree_progress_label_frame)
        self.decision_tree_reset_button.setObjectName("decision_tree_reset_button")
        self.verticalLayout_9.addWidget(self.decision_tree_reset_button)
        self.horizontalLayout_5.addWidget(self.decision_tree_progress_label_frame)
        self.verticalLayout_6.addWidget(self.decision_tree_progress)
        self.horizontalLayout_4.addWidget(self.decision_tree_Button_Frame)
        self.decision_tree_img_Frame = QtWidgets.QFrame(self.decision_tree_button_img_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decision_tree_img_Frame.sizePolicy().hasHeightForWidth())
        self.decision_tree_img_Frame.setSizePolicy(sizePolicy)
        self.decision_tree_img_Frame.setStyleSheet("")
        self.decision_tree_img_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision_tree_img_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision_tree_img_Frame.setObjectName("decision_tree_img_Frame")
        self.decision_tree_img_widget = QWidget(self.decision_tree_img_Frame)
        self.decision_tree_img_widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                          "stop:0 rgba(225, 225, 225, 225), stop:1 rgba(65, 105, 225, 255));")
        self.decision_tree_img_widget.setGeometry(14, 14, 330, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.decision_tree_img_widget.setSizePolicy(sizePolicy)
        self.decision_tree_img_widget.setContentsMargins(0, 0, 0, 0)
        self.decision_tree_imageLabel = QtWidgets.QLabel(self.decision_tree_img_widget)

        self.horizontalLayout_4.addWidget(self.decision_tree_img_Frame)
        self.verticalLayout_2.addWidget(self.decision_tree_button_img_frame)
        self.verticalLayout.addWidget(self.decision_tree_show_frame)
        self.retranslateUi(decision_tree)
        QtCore.QMetaObject.connectSlotsByName(decision_tree)

    def retranslateUi(self, decision_tree):
        _translate = QtCore.QCoreApplication.translate
        decision_tree.setWindowTitle(_translate("decision_tree", "Form"))
        self.decision_tree_name.setText(_translate("decision_tree", "决策树"))
        self.decision_tree_introduction.setPlainText(_translate("decision_tree", "决策树（Decision Tree）希望从训练数据中学习得"
                                                                                 "出一个树状结构的模型。决策树是一种判别模型，通过"
                                                                                 "做出一系列决策（选择）来对数据进行划分，这类似于"
                                                                                 "针对一系列问题进行选择。决策树的决策过程就是从根"
                                                                                 "节点开始，测试待分类项中对应的特征属性，并按照其"
                                                                                 "值选择输出分支，直到叶子节点，将叶子节点的存放的"
                                                                                 "类别作为决策结果。比较常见的决策树有ID3、C4.5、CART等。\n"
                                                                                 "ID3的大致步骤为：\n"
                                                                                 "（1）初始化特征集合和数据集合；\n"
                                                                                 "（2）计算数据集合信息熵和所有特征的条件熵，选择信"
                                                                                 "息增益最大的特征作为当前决策节点；\n"
                                                                                 "（3）更新数据集合和特征集合（删除上一步使用的特征，并按照特征值来"
                                                                                 "划分不同分支的数据集合）；\n"
                                                                                 "（4）重复 2，3 两步，若子集值包含单一特征，则为分支叶子节点。\n"
                                                                                 "C4.5用信息增益率筛选属性；在决策树构造过程中进行"
                                                                                 "剪枝，对非离散数据也能处理，能够对不完整数据进行处理。\n"
                                                                                 "CART分类树算法使用基尼系数选择特征，基尼系数代表了模型的"
                                                                                 "不纯度，基尼系数越小，不纯度越低，特征越好。"))
        self.decision_tree_dataset_label.setText(_translate("decision_tree", "数据集"))
        self.decision_tree_dataset_combobox.setItemText(0, _translate("decision_tree", "Iris"))
        self.decision_tree_dataset_combobox.setItemText(1, _translate("decision_tree", "Wine"))
        self.decision_tree_MaxDepth_label.setText(_translate("decision_tree", "最大深度"))
        self.decision_tree_MaxDepth_combobox.setItemText(0, _translate("decision_tree", "3"))
        self.decision_tree_MaxDepth_combobox.setItemText(1, _translate("decision_tree", "5"))
        self.decision_tree_train_button.setText(_translate("decision_tree", "开始训练"))
        self.decision_tree_img_button.setText(_translate("decision_tree", "显示结果"))
        self.decision_tree_reset_button.setText(_translate("decision_tree", "重置进度条"))

from qfluentwidgets import PlainTextEdit, ProgressRing, PushButton, ComboBox, InfoBarPosition, InfoBar

from PySide6.QtWidgets import QWidget

from sklearn.datasets import load_wine
from sklearn.datasets import load_iris

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

import math
import matplotlib.pyplot as plt

class DecisionTreeInterface(QWidget, Ui_decision_tree):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.decision_tree_img_widget.close()

        self.decision_tree_train_button.clicked.connect(self._start_train)

        self.decision_tree_img_button.clicked.connect(self._show_result)

        self.decision_tree_reset_button.clicked.connect(self._reset_progress_ring)


    def _start_train(self):
        # 加载数据集
        if self.decision_tree_dataset_combobox.currentText() == 'Iris':
             dataset = load_iris()
        else:
             dataset = load_wine()

        X = dataset['data']
        Y = dataset['target']

        for i in range(len(Y)):
            self.decision_tree_Progress_Ring.setValue(math.ceil((i + 1) / len(Y) * 100))

        # 训练阶段
        tree_clf = DecisionTreeClassifier(max_depth=int(self.decision_tree_MaxDepth_combobox.currentText()))
        tree_clf.fit(X, Y)

        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), dpi=300)
        tree.plot_tree(tree_clf, filled=True)

        fig.savefig('Resource/results/decision_tree_result.png', transparent=True)

        self.has_train = True

    def _show_result(self):
        if self.has_train:
                imgpath = 'Resource/results/decision_tree_result.png'

                pixmap = QtGui.QPixmap(imgpath)
                self.decision_tree_imageLabel.setPixmap(pixmap)
                self.decision_tree_imageLabel.setScaledContents(True)
                self.decision_tree_imageLabel.setGeometry(0, 20, 320, 240)
                self.decision_tree_imageLabel.setContentsMargins(0, 0, 0, 0)

                self.decision_tree_img_widget.update()
                self.decision_tree_img_widget.show()
        else:
            InfoBar.warning(
                title='注意',
                content="请先训练模型再查看结果",
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM_RIGHT,
                duration=-1,
                parent=self
            )

    def _reset_progress_ring(self):
        self.decision_tree_Progress_Ring.setValue(0)

