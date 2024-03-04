import time

from PySide6 import QtCore, QtGui, QtWidgets

class Ui_PCA(object):
    def setupUi(self, PCA):
        PCA.setObjectName("PCA")
        PCA.setEnabled(True)
        PCA.resize(873, 889)
        PCA.setMinimumSize(QtCore.QSize(500, 400))
        PCA.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.PCA_Frame = QtWidgets.QFrame(PCA)
        self.PCA_Frame.setGeometry(QtCore.QRect(10, 40, 700, 600))
        self.PCA_Frame.setMinimumSize(QtCore.QSize(500, 400))
        self.PCA_Frame.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.PCA_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCA_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCA_Frame.setObjectName("PCA_Frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PCA_Frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PCA_title_frame = QtWidgets.QFrame(self.PCA_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.PCA_title_frame.sizePolicy().hasHeightForWidth())
        self.PCA_title_frame.setSizePolicy(sizePolicy)
        self.PCA_title_frame.setStyleSheet("")
        self.PCA_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCA_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCA_title_frame.setObjectName("PCA_title_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.PCA_title_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.PCA_option_frame = QtWidgets.QFrame(self.PCA_title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.PCA_option_frame.sizePolicy().hasHeightForWidth())
        self.PCA_option_frame.setSizePolicy(sizePolicy)
        self.PCA_option_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PCA_option_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCA_option_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCA_option_frame.setObjectName("PCA_option_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.PCA_option_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PCA_name = QtWidgets.QLabel(self.PCA_option_frame)
        self.PCA_name.setStyleSheet("font: 75 9pt \"Fixedsys\";")
        self.PCA_name.setObjectName("PCA_name")
        self.horizontalLayout_2.addWidget(self.PCA_name, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.PCA_option_frame)
        self.verticalLayout.addWidget(self.PCA_title_frame)
        self.PCA_show_frame = QtWidgets.QFrame(self.PCA_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.PCA_show_frame.sizePolicy().hasHeightForWidth())
        self.PCA_show_frame.setSizePolicy(sizePolicy)
        self.PCA_show_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(74, 188, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PCA_show_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCA_show_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCA_show_frame.setObjectName("PCA_show_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.PCA_show_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PCA_info_frame = QtWidgets.QFrame(self.PCA_show_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.PCA_info_frame.sizePolicy().hasHeightForWidth())
        self.PCA_info_frame.setSizePolicy(sizePolicy)
        self.PCA_info_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.PCA_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCA_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCA_info_frame.setObjectName("PCA_info_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.PCA_info_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.PCA_introduction = PlainTextEdit(self.PCA_info_frame)
        self.PCA_introduction.setEnabled(True)
        self.PCA_introduction.setStyleSheet("LineEdit, TextEdit, PlainTextEdit {\n"
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
        self.PCA_introduction.setReadOnly(True)
        self.PCA_introduction.setObjectName("PCA_introduction")
        self.verticalLayout_5.addWidget(self.PCA_introduction, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.PCA_info_frame)
        self.PCA_button_img_frame = QtWidgets.QFrame(self.PCA_show_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.PCA_button_img_frame.sizePolicy().hasHeightForWidth())
        self.PCA_button_img_frame.setSizePolicy(sizePolicy)
        self.PCA_button_img_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.PCA_button_img_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCA_button_img_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCA_button_img_frame.setObjectName("PCA_button_img_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.PCA_button_img_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PCA_Button_Frame = QtWidgets.QFrame(self.PCA_button_img_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PCA_Button_Frame.sizePolicy().hasHeightForWidth())
        self.PCA_Button_Frame.setSizePolicy(sizePolicy)
        self.PCA_Button_Frame.setStyleSheet("")
        self.PCA_Button_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCA_Button_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCA_Button_Frame.setObjectName("PCA_Button_Frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.PCA_Button_Frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.PCA_button = QtWidgets.QFrame(self.PCA_Button_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.PCA_button.sizePolicy().hasHeightForWidth())
        self.PCA_button.setSizePolicy(sizePolicy)
        self.PCA_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.PCA_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCA_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCA_button.setObjectName("PCA_button")
        self.gridLayout = QtWidgets.QGridLayout(self.PCA_button)
        self.gridLayout.setObjectName("gridLayout")
        self.PCA_cluster_label = QtWidgets.QLabel(self.PCA_button)
        self.PCA_cluster_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.PCA_cluster_label.setObjectName("PCA_cluster_label")
        self.gridLayout.addWidget(self.PCA_cluster_label, 0, 0, 1, 1)
        self.PCA_cluster_combobox = ComboBox(self.PCA_button)
        self.PCA_cluster_combobox.setObjectName("PCA_cluster_combobox")
        self.PCA_cluster_combobox.addItem("")
        self.PCA_cluster_combobox.addItem("")
        self.PCA_cluster_combobox.addItem("")
        self.gridLayout.addWidget(self.PCA_cluster_combobox, 0, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.PCA_button)
        self.PCA_progress = QtWidgets.QFrame(self.PCA_Button_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.PCA_progress.sizePolicy().hasHeightForWidth())
        self.PCA_progress.setSizePolicy(sizePolicy)
        self.PCA_progress.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.PCA_progress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCA_progress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCA_progress.setObjectName("PCA_progress")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.PCA_progress)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.PCA_progress_ring_frame = QtWidgets.QFrame(self.PCA_progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PCA_progress_ring_frame.sizePolicy().hasHeightForWidth())
        self.PCA_progress_ring_frame.setSizePolicy(sizePolicy)
        self.PCA_progress_ring_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCA_progress_ring_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCA_progress_ring_frame.setObjectName("PCA_progress_ring_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.PCA_progress_ring_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.PCA_Progress_Ring = ProgressRing(self.PCA_progress_ring_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.PCA_Progress_Ring.sizePolicy().hasHeightForWidth())
        self.PCA_Progress_Ring.setSizePolicy(sizePolicy)
        self.PCA_Progress_Ring.setMinimumSize(QtCore.QSize(10, 10))
        self.PCA_Progress_Ring.setTextVisible(True)
        self.PCA_Progress_Ring.setObjectName("PCA_Progress_Ring")
        self.verticalLayout_8.addWidget(self.PCA_Progress_Ring)
        self.horizontalLayout_5.addWidget(self.PCA_progress_ring_frame)
        self.PCA_progress_label_frame = QtWidgets.QFrame(self.PCA_progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PCA_progress_label_frame.sizePolicy().hasHeightForWidth())
        self.PCA_progress_label_frame.setSizePolicy(sizePolicy)
        self.PCA_progress_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCA_progress_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCA_progress_label_frame.setObjectName("PCA_progress_label_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.PCA_progress_label_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.PCA_train_button = PushButton(self.PCA_progress_label_frame)
        self.PCA_train_button.setObjectName("PCA_train_button")
        self.verticalLayout_9.addWidget(self.PCA_train_button)
        self.PCA_img_button = PushButton(self.PCA_progress_label_frame)
        self.PCA_img_button.setObjectName("PCA_img_button")
        self.verticalLayout_9.addWidget(self.PCA_img_button)
        self.PCA_reset_button = PushButton(self.PCA_progress_label_frame)
        self.PCA_reset_button.setObjectName("PCA_reset_button")
        self.verticalLayout_9.addWidget(self.PCA_reset_button)
        self.horizontalLayout_5.addWidget(self.PCA_progress_label_frame)
        self.verticalLayout_6.addWidget(self.PCA_progress)
        self.horizontalLayout_4.addWidget(self.PCA_Button_Frame)
        self.PCA_img_Frame = QtWidgets.QFrame(self.PCA_button_img_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PCA_img_Frame.sizePolicy().hasHeightForWidth())
        self.PCA_img_Frame.setSizePolicy(sizePolicy)
        self.PCA_img_Frame.setStyleSheet("")
        self.PCA_img_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCA_img_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCA_img_Frame.setObjectName("PCA_img_Frame")
        self.PCA_img_widget = QWidget(self.PCA_img_Frame)
        self.PCA_img_widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                          "stop:0 rgba(225, 225, 225, 225), stop:1 rgba(65, 105, 225, 255));")
        self.PCA_img_widget.setGeometry(14, 14, 330, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.PCA_img_widget.setSizePolicy(sizePolicy)
        self.PCA_img_widget.setContentsMargins(0, 0, 0, 0)
        self.PCA_imageLabel = QtWidgets.QLabel(self.PCA_img_widget)

        self.horizontalLayout_4.addWidget(self.PCA_img_Frame)
        self.verticalLayout_2.addWidget(self.PCA_button_img_frame)
        self.verticalLayout.addWidget(self.PCA_show_frame)
        self.retranslateUi(PCA)
        QtCore.QMetaObject.connectSlotsByName(PCA)

    def retranslateUi(self, PCA):
        _translate = QtCore.QCoreApplication.translate
        PCA.setWindowTitle(_translate("PCA", "Form"))
        self.PCA_name.setText(_translate("PCA", "主成分分析"))
        self.PCA_introduction.setPlainText(_translate("PCA", "主成分分析（Principal Component Analysis, PCA）是一种降维方法，通"
                                                             "过将一个大的特征集转换成一个较小的特征集，这个特征集仍然包含了原始数据中的"
                                                             "大部分信息，从而降低了原始数据的维数。PCA的本质是特征选择。\n"
                                                             "。减少一个数据集的特征数量自然是以牺牲准确性为代价的，但降维的诀窍是用一点"
                                                             "准确性换取简单性。因为更小的数据集更容易探索和可视化，并且对于机器学习算法"
                                                             "来说，分析数据会更快、更容易，而不需要处理额外的特征。\n"
                                                             "PCA仅仅需要以方差衡量信息量,不受数据集以外的因素影响，且各主成分之间正交,"
                                                             "可消除原始数据成分间的相互影响的因素。同时，PCA算法计算方法简单,主要运算时"
                                                             "特征值分解,易于实现。最后，作为一种无监督学习,PCA完全没有参数限制。\n"
                                                             "但是需要注意到，主成分各个特征维度的含义具有一定的模糊性,不如原始样本特征"
                                                             "的解释性强，方差小的非主成分也可能含有对样本差异的重要信息,因降维丢弃可能"
                                                             "对后续数据处理有影响。\n"
                                                             "在演示过程中，我们主要使用维度-轮廓系数曲线来评估模型的性能。"))
        self.PCA_cluster_label.setText(_translate("PCA", "降维后的聚类方式"))
        self.PCA_cluster_combobox.setItemText(0, _translate("PCA", "KNN"))
        self.PCA_cluster_combobox.setItemText(1, _translate("PCA", "KMeans"))
        self.PCA_cluster_combobox.setItemText(2, _translate("PCA", "层次聚类"))
        self.PCA_train_button.setText(_translate("PCA", "开始训练"))
        self.PCA_img_button.setText(_translate("PCA", "显示结果"))
        self.PCA_reset_button.setText(_translate("PCA", "重置进度条"))

from qfluentwidgets import PlainTextEdit, ProgressRing, PushButton, ComboBox, InfoBarPosition, InfoBar

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QWidget

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import AgglomerativeClustering

import matplotlib.pyplot as plt

import math
from tqdm import tqdm

class PCAInterface(QWidget, Ui_PCA):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cluster = self.PCA_cluster_combobox.currentText()

        self.PCA_img_widget.close()

        self.PCA_train_button.clicked.connect(self._start_train)

        self.PCA_img_button.clicked.connect(self._show_result)

        self.PCA_reset_button.clicked.connect(self._reset_progress_ring)

    def _start_train(self):
        # 读取数据集
        data = pd.read_csv('Resource/dataset/pca/yaleB.csv')
        X = data.iloc[:, :-1]
        Y = data.iloc[:, -1]

        cluster = self.PCA_cluster_combobox.currentText()

        self.worker_thread = WorkerThread(X, Y, cluster)
        self.worker_thread.progress_updated.connect(self._update_progress_ring)
        self.worker_thread.start()

        self.has_train = True

    def _show_result(self):
        if self.has_train:
            imgpath = 'Resource/results/PCA_result.png'

            pixmap = QtGui.QPixmap(imgpath)
            self.PCA_imageLabel.setPixmap(pixmap)
            self.PCA_imageLabel.setScaledContents(True)
            self.PCA_imageLabel.setGeometry(0, 20, 320, 240)
            self.PCA_imageLabel.setContentsMargins(0, 0, 0, 0)

            self.PCA_img_widget.update()
            self.PCA_img_widget.show()
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
        self.PCA_Progress_Ring.setValue(0)

    def _update_progress_ring(self, value):
        self.PCA_Progress_Ring.setValue(value)

class WorkerThread(QThread):
    progress_updated = Signal(int)  # 用于更新进度的信号

    def __init__(self, X, Y, cluster):
        super().__init__()
        self.X = X
        self.Y = Y
        self.cluster = cluster

    def run(self):
        # 初始化维度和轮廓系数的列表
        dimensions = []
        silhouette_scores = []

        if self.cluster == 'KNN':
            for n_components in tqdm(range(1, self.X.shape[1] + 1, 20)):

                # 更新进度条
                progress = math.ceil(n_components * 100 / self.X.shape[1])
                self.progress_updated.emit(progress)

                # PCA+聚类
                X_pca = self._pca(self.X, n_components)
                knn = KNeighborsClassifier(n_neighbors=3)
                y_pred = knn.fit(X_pca, self.Y).predict(X_pca)
                silhouette_score = metrics.silhouette_score(X_pca, y_pred)
                dimensions.append(n_components)
                silhouette_scores.append(silhouette_score)

        elif self.cluster == 'KMeans':
            for n_components in tqdm(range(1, self.X.shape[1] + 1, 20)):

                # 更新进度条
                progress = math.ceil(n_components * 100 / self.X.shape[1])
                self.progress_updated.emit(progress)

                # PCA+聚类
                X_pca = self._pca(self.X, n_components)
                kmeans = KMeans(n_clusters=3, n_init=10)
                y_pred = kmeans.fit_predict(X_pca)
                silhouette_score = metrics.silhouette_score(X_pca, y_pred)
                dimensions.append(n_components)
                silhouette_scores.append(silhouette_score)

        elif self.cluster == '层次聚类':
            for n_components in tqdm(range(1, self.X.shape[1] + 1, 20)):

                # 更新进度条
                progress = math.ceil(n_components * 100 / self.X.shape[1])
                self.progress_updated.emit(progress)

                # PCA+聚类
                X_pca = self._pca(self.X, n_components)
                agg_clustering = AgglomerativeClustering(n_clusters=3)
                y_pred = agg_clustering.fit_predict(X_pca)
                silhouette_score = metrics.silhouette_score(X_pca, y_pred)
                dimensions.append(n_components)
                silhouette_scores.append(silhouette_score)

        # 绘制维度-轮廓系数曲线
        plt.clf()
        plt.plot(dimensions, silhouette_scores, marker='o')
        plt.xlabel('Number of Dimensions')
        plt.ylabel('Silhouette Score')

        plt.savefig('Resource/results/PCA_result.png', transparent=True, bbox_inches='tight', pad_inches=0.0)

        self.model = True

    def _pca(self, X, n_components):
        mean = np.mean(X, axis=0)
        X_centered = X - mean
        cov_matrix = np.cov(X_centered, rowvar=False)
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        top_eigenvectors = eigenvectors[:, -n_components:]
        X_pca = np.dot(X_centered, top_eigenvectors)
        return X_pca