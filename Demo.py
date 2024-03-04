'''
    人工智能算法教学演示系统
'''

import sys

# 导入PySide6
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon, QGuiApplication

# 导入QFluentWidget（使用前需购买该工具库的商业许可）
from qfluentwidgetspro import setLicense
from qfluentwidgets import (SplitFluentWindow, FluentIcon, NavigationItemPosition, FluentTranslator, Theme, setTheme)

# 导入导航栏的各个子界面
from Interface.view.Main_Interface import MainInterface
from Interface.view.ML_Interface import MachineLearningInterface
from Interface.view.DL_Interface import DeepLearningInterface
from Interface.view.Setting_Interface import SettingInterface
from Interface.view.Author_Interface import AuthorInterface

# 导入机器学习的各个子界面
from Interface.ml.KNN_Interface import KNNInterface
from Interface.ml.SVM_Interface import SVMInterface
from Interface.ml.LinearRegression_Interface import LinearRegressionInterface
from Interface.ml.PCA_Interface import PCAInterface
from Interface.ml.DecisionTree_Interface import DecisionTreeInterface

# 导入深度学习的各个子界面
from Interface.dl.CNN_Interface import CNNInterface

# 导入配置文件
from Resource.config.Config import cfg

class Window(SplitFluentWindow):
    def __init__(self):
        super().__init__()

        # 标题、logo以及页面大小的设置（固定窗口大小，不能拉伸）
        self.setWindowTitle('人工智能算法教学演示系统')
        self.setWindowIcon(QIcon('Resource/img/logo.png'))
        self.setFixedSize(765, 655)
        self.center()

        # 设置子界面
        self.maininterface = MainInterface()
        self.machinelearninginterface = MachineLearningInterface()
        self.deeplearninginterface = DeepLearningInterface()
        self.authorinterface = AuthorInterface()
        self.settinginterface = SettingInterface()

        # 机器学习模型子界面
        self.knninterface = KNNInterface()
        self.svminterface = SVMInterface()
        self.linearregressioninterface = LinearRegressionInterface()
        self.pcainterface = PCAInterface()
        self.decisiontreeinterface = DecisionTreeInterface()

        # 深度学习模型子界面
        self.cnninterface = CNNInterface()

        # 添加显示在导航栏的子界面
        self.addSubInterface(self.maininterface, FluentIcon.RINGER, '主界面')
        self.addSubInterface(self.machinelearninginterface, FluentIcon.BOOK_SHELF, '机器学习')
        self.addSubInterface(self.deeplearninginterface, FluentIcon.EDUCATION, '深度学习')
        self.addSubInterface(self.authorinterface, 'Resource/img/author.png', '项目制作组', NavigationItemPosition.BOTTOM, )
        self.addSubInterface(self.settinginterface, FluentIcon.SETTING, '设置', NavigationItemPosition.BOTTOM)

        # 添加机器学习的子界面
        self.stackedWidget.addWidget(self.knninterface)
        self.stackedWidget.addWidget(self.svminterface)
        self.stackedWidget.addWidget(self.linearregressioninterface)
        self.stackedWidget.addWidget(self.pcainterface)
        self.stackedWidget.addWidget(self.decisiontreeinterface)

        # 添加深度学习的子界面
        self.stackedWidget.addWidget(self.cnninterface)

        # 机器学习界面跳转
        self.machinelearninginterface.KNN.clicked.connect(lambda: self.switchTo(self.knninterface))
        self.machinelearninginterface.SVM.clicked.connect(lambda: self.switchTo(self.svminterface))
        self.machinelearninginterface.linear_regression.clicked.connect(lambda: self.switchTo(self.linearregressioninterface))
        self.machinelearninginterface.PCA.clicked.connect(lambda: self.switchTo(self.pcainterface))
        self.machinelearninginterface.decision_tree.clicked.connect(lambda: self.switchTo(self.decisiontreeinterface))

        # 深度学习界面跳转
        self.deeplearninginterface.CNN.clicked.connect(lambda: self.switchTo(self.cnninterface))

    # 保持窗口的初始化位置在屏幕正中间
    def center(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


if __name__ == '__main__':
    # 设置使用QFluentWidget的激活码（使用前需购买该工具库的商业许可以获得激活码）
    setLicense("mGR3+Zzt2pWCCCUVLKMgV2zNviEC95enQKeF7HsypddJ/Au7oFDjFxlO+gbE5JCFsx1jwHOHwNoj1w9abf86+jcagg4J/"
               "mCmwEOFVJnQ0uVlwzduTWLKQiztK4FmWmPjT2w6gQ0tkfXKi39Hc7BEbHMnWxr06CGgGbvs6Zu5yadgMzPUl8d5OTIler"
               "5dAL2WHltzyCk1/tQQfSz2WU2GESuYMRnmO7jXTZhw6y39vvzH5FgQ37massVJet9iGAoddLj8T9sspv1pMeT7h0ncnwy6"
               "wQfIDPMqPO2V+JkfGZ4=")

    # 实例化系统
    app = QApplication(sys.argv)

    # 配置语言项
    locale = cfg.get(cfg.language).value
    translator = FluentTranslator(locale)
    app.installTranslator(translator)

    # 配置主题
    setTheme(Theme.LIGHT)

    # 显示窗口
    w = Window()
    w.show()
    app.exec()