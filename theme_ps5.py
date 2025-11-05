# -*- coding: utf-8 -*-

PS5_STYLE = """
/* PlayStation 5 Theme - Clean White/Blue */
QWidget {
    background-color: #f2f2f2;
    color: #000000;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 11px;
}

QMainWindow {
    background-color: #ffffff;
    border: none;
}

QPushButton {
    background-color: #0070cc;
    color: #ffffff;
    border: none;
    border-radius: 24px;
    padding: 12px 32px;
    font-weight: 600;
    font-size: 13px;
    min-height: 36px;
}

QPushButton:hover {
    background-color: #0052a3;
}

QPushButton:pressed {
    background-color: #003d7a;
}

QPushButton:disabled {
    background-color: #cccccc;
    color: #888888;
}

QLabel {
    color: #000000;
    background-color: transparent;
    font-size: 13px;
    padding: 5px;
}

QLabel#title {
    font-size: 32px;
    font-weight: 300;
    color: #0070cc;
}

QLabel#subtitle {
    font-size: 16px;
    color: #555555;
    font-weight: 300;
}

QListWidget {
    background-color: #ffffff;
    color: #000000;
    border: none;
    border-radius: 8px;
    padding: 10px;
    selection-background-color: #0070cc;
    selection-color: #ffffff;
}

QListWidget::item {
    padding: 12px;
    border-bottom: 1px solid #e8e8e8;
    border-radius: 4px;
}

QListWidget::item:hover {
    background-color: #f0f7ff;
}

QListWidget::item:selected {
    background-color: #0070cc;
    color: #ffffff;
}

QCheckBox {
    color: #000000;
    spacing: 8px;
    font-size: 12px;
}

QCheckBox::indicator {
    width: 22px;
    height: 22px;
    border: 2px solid #0070cc;
    background-color: #ffffff;
    border-radius: 4px;
}

QCheckBox::indicator:checked {
    background-color: #0070cc;
    border: 2px solid #0070cc;
}

QCheckBox::indicator:hover {
    background-color: #f0f7ff;
}

QDialog {
    background-color: #ffffff;
    border: none;
    border-radius: 12px;
}

QDialog QLabel {
    color: #000000;
}

QDialogButtonBox QPushButton {
    min-width: 120px;
}

QMessageBox {
    background-color: #ffffff;
}

QMessageBox QLabel {
    color: #000000;
}

QProgressBar {
    border: none;
    border-radius: 8px;
    text-align: center;
    background-color: #e8e8e8;
    color: #000000;
    font-weight: 600;
    height: 16px;
}

QProgressBar::chunk {
    background-color: #0070cc;
    border-radius: 8px;
}

QComboBox {
    background-color: #ffffff;
    color: #000000;
    border: 2px solid #e8e8e8;
    border-radius: 8px;
    padding: 8px;
    min-width: 150px;
}

QComboBox:hover {
    border: 2px solid #0070cc;
}

QComboBox::drop-down {
    border: none;
    width: 30px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 8px solid #0070cc;
    margin-right: 8px;
}

QComboBox QAbstractItemView {
    background-color: #ffffff;
    color: #000000;
    border: 2px solid #e8e8e8;
    border-radius: 8px;
    selection-background-color: #0070cc;
    selection-color: #ffffff;
}

QScrollBar:vertical {
    background-color: #f2f2f2;
    width: 12px;
    border: none;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #cccccc;
    border-radius: 6px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background-color: #0070cc;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background-color: #f2f2f2;
    height: 12px;
    border: none;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background-color: #cccccc;
    border-radius: 6px;
    min-width: 30px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #0070cc;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}
"""

def get_ps5_style():
    return PS5_STYLE
