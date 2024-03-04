# 系统设置
from Resource.config.Config import cfg, YEAR, AUTHOR, VERSION
from qfluentwidgets import (SettingCardGroup, SwitchSettingCard, PrimaryPushSettingCard, ScrollArea, ComboBoxSettingCard,
                            ExpandLayout, InfoBar)
from qfluentwidgets import FluentIcon as FIF
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QFont

# 系统设置
class Ui_Settings(ScrollArea):
    # 检查更新
    checkUpdateSig = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)

        # 标题
        self.settingLabel = QLabel(self.tr("设置"), self)
        self.settingLabel.setFont(QFont('SimHei', 20))

        '''
            个性化设置
        '''
        self.personalGroup = SettingCardGroup(self.tr("个性化"), self.scrollWidget)
        self.languageCard = ComboBoxSettingCard(cfg.language,
                                                FIF.LANGUAGE,
                                                self.tr('语言设置'),
                                                self.tr('选择系统语言'),
                                                texts=['简体中文'],
                                                parent=self.personalGroup)

        '''
            应用更新
        '''
        self.updateSoftwareGroup = SettingCardGroup(self.tr("应用更新"), self.scrollWidget)
        self.updateOnStartUpCard = SwitchSettingCard(FIF.UPDATE,
                                                    self.tr('自动更新'),
                                                    self.tr('应用启动时自动检查更新'),
                                                    configItem = cfg.checkUpdateAtStartUp,
                                                    parent = self.updateSoftwareGroup)

        '''
            关于应用
        '''
        self.aboutGroup = SettingCardGroup(self.tr('关于应用'), self.scrollWidget)
        self.aboutCard = PrimaryPushSettingCard(self.tr('检查更新'),
                                                FIF.INFO,
                                                self.tr('关于应用'),
                                                '© ' + self.tr('版权所有：') + f" {YEAR}, {AUTHOR}； " +
                                                self.tr('当前版本：') + f" {VERSION}",
                                                self.aboutGroup)

        self.__initWidget()

    def __initWidget(self):
        self.resize(873, 889)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 120, 0, 20)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

        self.__initLayout()
        self.__connectSignalToSlot()


    def __initLayout(self):
        self.settingLabel.move(60, 63)

        self.personalGroup.addSettingCard(self.languageCard)

        self.updateSoftwareGroup.addSettingCard(self.updateOnStartUpCard)

        self.aboutGroup.addSettingCard(self.aboutCard)

        self.expandLayout.setSpacing(25)
        self.expandLayout.setContentsMargins(60, 10, 60, 0)
        self.expandLayout.addWidget(self.personalGroup)
        self.expandLayout.addWidget(self.updateSoftwareGroup)
        self.expandLayout.addWidget(self.aboutGroup)

    # 重启提示
    def __showRestartTooltip(self):
        InfoBar.warning(
            '',
            self.tr('重启后适应新配置'),
            parent=self.window()
        )

    # 连接信号槽
    def __connectSignalToSlot(self):
        cfg.appRestartSig.connect(self.__showRestartTooltip)

        # 关于
        self.aboutCard.clicked.connect(self.checkUpdateSig)


from PySide6 import QtCore
from PySide6.QtWidgets import QHBoxLayout

class SettingInterface(Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName('Settings')
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)

        self.resize(873, 889)
        self.setMinimumSize(QtCore.QSize(500, 400))
        self.setGeometry(QtCore.QRect(0, 40, 700, 600))