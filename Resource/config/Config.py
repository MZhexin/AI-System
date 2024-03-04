'''
    应用设置的配置文件
'''

from enum import Enum
from PySide6.QtCore import QLocale
from qfluentwidgets import (qconfig, QConfig, ConfigItem, OptionsConfigItem, BoolValidator,
                            ColorConfigItem, OptionsValidator, ConfigSerializer, Theme)

class Language(Enum):
    CHINESE_SIMPLIFIED = QLocale(QLocale.Chinese, QLocale.China)

class LanguageSerializer(ConfigSerializer):
    def serialize(self, language):
        return language.value.name() if language != Language.CHINESE_SIMPLIFIED else "zh_CN"
    def deserialize(self, value: str):
        return Language(QLocale(value)) if value != "zh_CN" else Language.CHINESE_SIMPLIFIED


# 系统配置
class Config(QConfig):
    language = OptionsConfigItem(
        "MainWindow", "Language", 'zh_CN', OptionsValidator(Language), LanguageSerializer(), restart=True)
    checkUpdateAtStartUp = ConfigItem("Update", "CheckUpdateAtStartUp", True, BoolValidator())

# 版本信息
YEAR = 2024
AUTHOR = "鼠鼠爱猫猫团队"
VERSION = "1.0"

# 保存配置文件
cfg = Config()
cfg.themeMode.value = Theme.AUTO
qconfig.load('config.json', cfg)