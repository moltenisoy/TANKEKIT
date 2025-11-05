# -*- coding: utf-8 -*-

XBOX360_STYLE = """
/* Xbox 360 Theme - Green/Gray Blades */
QWidget {
    background-color: #2d2d2d;
    color: #ffffff;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 11px;
}

QMainWindow {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 1,
        stop: 0 #1a1a1a,
        stop: 0.5 #2d2d2d,
        stop: 1 #1a1a1a
    );
    border: 2px solid #9bca3b;
}

QPushButton {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #9bca3b,
        stop: 1 #7ba82f
    );
    color: #ffffff;
    border: 2px solid #5f8624;
    border-radius: 6px;
    padding: 10px 24px;
    font-weight: bold;
    font-size: 12px;
    min-height: 32px;
}

QPushButton:hover {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #b5e045,
        stop: 1 #9bca3b
    );
    border: 2px solid #9bca3b;
}

QPushButton:pressed {
    background-color: #5f8624;
    border: 2px solid #4a6a1c;
}

QPushButton:disabled {
    background-color: #3d3d3d;
    color: #777777;
    border: 2px solid #2d2d2d;
}

QLabel {
    color: #ffffff;
    background-color: transparent;
    font-size: 12px;
    padding: 5px;
}

QLabel#title {
    font-size: 28px;
    font-weight: bold;
    color: #9bca3b;
}

QLabel#subtitle {
    font-size: 14px;
    color: #cccccc;
}

QListWidget {
    background-color: #1a1a1a;
    color: #ffffff;
    border: 2px solid #3d3d3d;
    border-radius: 4px;
    padding: 8px;
    selection-background-color: #9bca3b;
    selection-color: #000000;
}

QListWidget::item {
    padding: 10px;
    border-bottom: 1px solid #2d2d2d;
    border-radius: 2px;
}

QListWidget::item:hover {
    background-color: #3d3d3d;
    border-left: 4px solid #9bca3b;
}

QListWidget::item:selected {
    background-color: #9bca3b;
    color: #000000;
    border-left: 4px solid #b5e045;
    font-weight: bold;
}

QCheckBox {
    color: #ffffff;
    spacing: 6px;
    font-size: 11px;
}

QCheckBox::indicator {
    width: 20px;
    height: 20px;
    border: 2px solid #9bca3b;
    background-color: #1a1a1a;
    border-radius: 3px;
}

QCheckBox::indicator:checked {
    background-color: #9bca3b;
    border: 2px solid #b5e045;
}

QCheckBox::indicator:hover {
    background-color: #2d2d2d;
    border: 2px solid #b5e045;
}

QDialog {
    background-color: #2d2d2d;
    border: 3px solid #9bca3b;
    border-radius: 8px;
}

QDialog QLabel {
    color: #ffffff;
}

QDialogButtonBox QPushButton {
    min-width: 110px;
}

QMessageBox {
    background-color: #2d2d2d;
}

QMessageBox QLabel {
    color: #ffffff;
}

QProgressBar {
    border: 2px solid #3d3d3d;
    border-radius: 6px;
    text-align: center;
    background-color: #1a1a1a;
    color: #ffffff;
    font-weight: bold;
    height: 20px;
}

QProgressBar::chunk {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #9bca3b,
        stop: 0.5 #7ba82f,
        stop: 1 #9bca3b
    );
    border-radius: 4px;
}

QComboBox {
    background-color: #1a1a1a;
    color: #ffffff;
    border: 2px solid #3d3d3d;
    border-radius: 6px;
    padding: 6px;
    min-width: 150px;
}

QComboBox:hover {
    border: 2px solid #9bca3b;
}

QComboBox::drop-down {
    border: none;
    width: 28px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 8px solid #9bca3b;
    margin-right: 6px;
}

QComboBox QAbstractItemView {
    background-color: #1a1a1a;
    color: #ffffff;
    border: 2px solid #9bca3b;
    selection-background-color: #9bca3b;
    selection-color: #000000;
}

QScrollBar:vertical {
    background-color: #1a1a1a;
    width: 14px;
    border: 1px solid #3d3d3d;
    border-radius: 7px;
}

QScrollBar::handle:vertical {
    background-color: #9bca3b;
    border-radius: 6px;
    min-height: 25px;
}

QScrollBar::handle:vertical:hover {
    background-color: #b5e045;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background-color: #2d2d2d;
    height: 14px;
}

QScrollBar:horizontal {
    background-color: #1a1a1a;
    height: 14px;
    border: 1px solid #3d3d3d;
    border-radius: 7px;
}

QScrollBar::handle:horizontal {
    background-color: #9bca3b;
    border-radius: 6px;
    min-width: 25px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #b5e045;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    background-color: #2d2d2d;
    width: 14px;
}
"""

def get_xbox360_style():
    return XBOX360_STYLE
