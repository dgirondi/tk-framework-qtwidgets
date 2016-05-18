# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'version_details_widget.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_VersionDetailsWidget(object):
    def setupUi(self, VersionDetailsWidget):
        VersionDetailsWidget.setObjectName("VersionDetailsWidget")
        VersionDetailsWidget.resize(390, 737)
        self.verticalLayout_17 = QtGui.QVBoxLayout(VersionDetailsWidget)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.details_title_bar = QtGui.QFrame(VersionDetailsWidget)
        self.details_title_bar.setMaximumSize(QtCore.QSize(16777215, 13))
        self.details_title_bar.setStyleSheet("background: rgb(37,38,41)")
        self.details_title_bar.setFrameShape(QtGui.QFrame.NoFrame)
        self.details_title_bar.setFrameShadow(QtGui.QFrame.Plain)
        self.details_title_bar.setLineWidth(0)
        self.details_title_bar.setObjectName("details_title_bar")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.details_title_bar)
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setContentsMargins(0, 5, 5, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtGui.QSpacerItem(350, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.float_button = QtGui.QToolButton(self.details_title_bar)
        self.float_button.setMaximumSize(QtCore.QSize(8, 8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/version_details/dock.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/version_details/undock_hover.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/version_details/undock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/version_details/undock_hover.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/version_details/undock_hover.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/version_details/dock_hover.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.float_button.setIcon(icon)
        self.float_button.setCheckable(True)
        self.float_button.setAutoRaise(True)
        self.float_button.setObjectName("float_button")
        self.horizontalLayout_9.addWidget(self.float_button)
        self.close_button = QtGui.QToolButton(self.details_title_bar)
        self.close_button.setMaximumSize(QtCore.QSize(8, 8))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/version_details/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/version_details/close_hover.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/version_details/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/version_details/close_hover.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/version_details/close_hover.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/version_details/close_hover.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.close_button.setIcon(icon1)
        self.close_button.setAutoRaise(True)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_9.addWidget(self.close_button)
        self.verticalLayout_17.addWidget(self.details_title_bar)
        self.pages = QtGui.QStackedWidget(VersionDetailsWidget)
        self.pages.setObjectName("pages")
        self.main_page = QtGui.QWidget()
        self.main_page.setObjectName("main_page")
        self.verticalLayout = QtGui.QVBoxLayout(self.main_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.entity_tab_widget = QtGui.QTabWidget(self.main_page)
        self.entity_tab_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_tab_widget.setObjectName("entity_tab_widget")
        self.entity_note_tab = QtGui.QWidget()
        self.entity_note_tab.setObjectName("entity_note_tab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.entity_note_tab)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.info_layout = QtGui.QHBoxLayout()
        self.info_layout.setSpacing(0)
        self.info_layout.setContentsMargins(0, 0, -1, 0)
        self.info_layout.setObjectName("info_layout")
        self.widget = QtGui.QWidget(self.entity_note_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.current_version_card = ShotgunEntityCardWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_version_card.sizePolicy().hasHeightForWidth())
        self.current_version_card.setSizePolicy(sizePolicy)
        self.current_version_card.setObjectName("current_version_card")
        self.horizontalLayout_2.addWidget(self.current_version_card)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setContentsMargins(-1, 0, 2, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.shotgun_nav_button = QtGui.QToolButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shotgun_nav_button.sizePolicy().hasHeightForWidth())
        self.shotgun_nav_button.setSizePolicy(sizePolicy)
        self.shotgun_nav_button.setMaximumSize(QtCore.QSize(15, 15))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/version_details/navigate_out_hover.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap(":/version_details/navigate_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap(":/version_details/navigate_out_hover.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.shotgun_nav_button.setIcon(icon2)
        self.shotgun_nav_button.setAutoRaise(True)
        self.shotgun_nav_button.setObjectName("shotgun_nav_button")
        self.horizontalLayout.addWidget(self.shotgun_nav_button)
        self.pin_button = QtGui.QToolButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pin_button.sizePolicy().hasHeightForWidth())
        self.pin_button.setSizePolicy(sizePolicy)
        self.pin_button.setMaximumSize(QtCore.QSize(15, 15))
        self.pin_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/version_details/tack_hover.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":/version_details/tack_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":/version_details/tack_hover.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pin_button.setIcon(icon3)
        self.pin_button.setCheckable(True)
        self.pin_button.setAutoRaise(True)
        self.pin_button.setObjectName("pin_button")
        self.horizontalLayout.addWidget(self.pin_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.info_layout.addWidget(self.widget)
        self.verticalLayout_3.addLayout(self.info_layout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtGui.QSpacerItem(40, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.more_info_button = QtGui.QToolButton(self.entity_note_tab)
        self.more_info_button.setCheckable(True)
        self.more_info_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.more_info_button.setArrowType(QtCore.Qt.NoArrow)
        self.more_info_button.setObjectName("more_info_button")
        self.horizontalLayout_4.addWidget(self.more_info_button)
        self.more_fields_button = QtGui.QToolButton(self.entity_note_tab)
        self.more_fields_button.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.more_fields_button.setObjectName("more_fields_button")
        self.horizontalLayout_4.addWidget(self.more_fields_button)
        spacerItem3 = QtGui.QSpacerItem(40, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.notes_tab_line = QtGui.QFrame(self.entity_note_tab)
        self.notes_tab_line.setFrameShape(QtGui.QFrame.HLine)
        self.notes_tab_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.notes_tab_line.setObjectName("notes_tab_line")
        self.verticalLayout_3.addWidget(self.notes_tab_line)
        self.note_stream_widget = ActivityStreamWidget(self.entity_note_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.note_stream_widget.sizePolicy().hasHeightForWidth())
        self.note_stream_widget.setSizePolicy(sizePolicy)
        self.note_stream_widget.setObjectName("note_stream_widget")
        self.verticalLayout_3.addWidget(self.note_stream_widget)
        self.entity_tab_widget.addTab(self.entity_note_tab, "")
        self.entity_version_tab = QtGui.QWidget()
        self.entity_version_tab.setObjectName("entity_version_tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.entity_version_tab)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.version_top_layout = QtGui.QWidget(self.entity_version_tab)
        self.version_top_layout.setObjectName("version_top_layout")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.version_top_layout)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.version_fields_button = QtGui.QToolButton(self.version_top_layout)
        self.version_fields_button.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.version_fields_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.version_fields_button.setObjectName("version_fields_button")
        self.horizontalLayout_6.addWidget(self.version_fields_button)
        self.label = QtGui.QLabel(self.version_top_layout)
        self.label.setMaximumSize(QtCore.QSize(8, 8))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/version_details/arrow.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.version_sort_button = QtGui.QToolButton(self.version_top_layout)
        self.version_sort_button.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.version_sort_button.setObjectName("version_sort_button")
        self.horizontalLayout_7.addWidget(self.version_sort_button)
        self.label_2 = QtGui.QLabel(self.version_top_layout)
        self.label_2.setMaximumSize(QtCore.QSize(8, 8))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/version_details/arrow.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.version_search = SearchWidget(self.version_top_layout)
        self.version_search.setObjectName("version_search")
        self.horizontalLayout_5.addWidget(self.version_search)
        self.verticalLayout_2.addWidget(self.version_top_layout)
        self.line = QtGui.QFrame(self.entity_version_tab)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.entity_version_view = QtGui.QListView(self.entity_version_tab)
        self.entity_version_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.entity_version_view.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.entity_version_view.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.entity_version_view.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.entity_version_view.setObjectName("entity_version_view")
        self.verticalLayout_2.addWidget(self.entity_version_view)
        self.entity_tab_widget.addTab(self.entity_version_tab, "")
        self.verticalLayout.addWidget(self.entity_tab_widget)
        self.pages.addWidget(self.main_page)
        self.empty_page = QtGui.QWidget()
        self.empty_page.setObjectName("empty_page")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.empty_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.empty_label = QtGui.QLabel(self.empty_page)
        self.empty_label.setText("")
        self.empty_label.setPixmap(QtGui.QPixmap(":/version_details/panel_empty_background.png"))
        self.empty_label.setAlignment(QtCore.Qt.AlignCenter)
        self.empty_label.setObjectName("empty_label")
        self.verticalLayout_5.addWidget(self.empty_label)
        self.pages.addWidget(self.empty_page)
        self.verticalLayout_17.addWidget(self.pages)

        self.retranslateUi(VersionDetailsWidget)
        self.pages.setCurrentIndex(0)
        self.entity_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VersionDetailsWidget)

    def retranslateUi(self, VersionDetailsWidget):
        VersionDetailsWidget.setWindowTitle(QtGui.QApplication.translate("VersionDetailsWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.float_button.setText(QtGui.QApplication.translate("VersionDetailsWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.close_button.setText(QtGui.QApplication.translate("VersionDetailsWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_nav_button.setText(QtGui.QApplication.translate("VersionDetailsWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.more_info_button.setText(QtGui.QApplication.translate("VersionDetailsWidget", "More info", None, QtGui.QApplication.UnicodeUTF8))
        self.more_fields_button.setText(QtGui.QApplication.translate("VersionDetailsWidget", "Fields...", None, QtGui.QApplication.UnicodeUTF8))
        self.entity_tab_widget.setTabText(self.entity_tab_widget.indexOf(self.entity_note_tab), QtGui.QApplication.translate("VersionDetailsWidget", "NOTES", None, QtGui.QApplication.UnicodeUTF8))
        self.version_fields_button.setText(QtGui.QApplication.translate("VersionDetailsWidget", "Fields", None, QtGui.QApplication.UnicodeUTF8))
        self.version_sort_button.setText(QtGui.QApplication.translate("VersionDetailsWidget", "Sort", None, QtGui.QApplication.UnicodeUTF8))
        self.entity_tab_widget.setTabText(self.entity_tab_widget.indexOf(self.entity_version_tab), QtGui.QApplication.translate("VersionDetailsWidget", "VERSIONS", None, QtGui.QApplication.UnicodeUTF8))

from ..qtwidgets import ActivityStreamWidget, SearchWidget, ShotgunEntityCardWidget
from . import resources_rc
