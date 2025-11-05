# -*- coding: utf-8 -*-

MATRIX_STYLE = """
/* Matrix Theme - Green Digital Rain */
QWidget {
    background-color: #000000;
    color: #00ff00;
    font-family: 'Courier New', 'Consolas', monospace;
    font-size: 11px;
}

QMainWindow {
    background-color: #000000;
    border: 2px solid #00ff00;
}

QPushButton {
    background-color: #001100;
    color: #00ff00;
    border: 2px solid #00ff00;
    padding: 10px 22px;
    font-weight: bold;
    font-size: 12px;
    min-height: 32px;
}

QPushButton:hover {
    background-color: #00ff00;
    color: #000000;
    border: 2px solid #00cc00;
    box-shadow: 0 0 15px #00ff00, inset 0 0 10px #00ff00;
}

QPushButton:pressed {
    background-color: #00cc00;
    color: #000000;
    border: 2px solid #009900;
}

QPushButton:disabled {
    background-color: #000000;
    color: #003300;
    border: 2px solid #003300;
}

QLabel {
    color: #00ff00;
    background-color: transparent;
    font-size: 12px;
    padding: 5px;
}

QLabel#title {
    font-size: 28px;
    font-weight: bold;
    color: #00ff00;
    text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00;
}

QLabel#subtitle {
    font-size: 14px;
    color: #00cc00;
}

QListWidget {
    background-color: #000000;
    color: #00ff00;
    border: 2px solid #00ff00;
    padding: 6px;
    selection-background-color: #00ff00;
    selection-color: #000000;
}

QListWidget::item {
    padding: 8px;
    border-bottom: 1px solid #001100;
}

QListWidget::item:hover {
    background-color: #001100;
    border-left: 3px solid #00ff00;
}

QListWidget::item:selected {
    background-color: #00ff00;
    color: #000000;
    border-left: 3px solid #00cc00;
    font-weight: bold;
}

QCheckBox {
    color: #00ff00;
    spacing: 6px;
    font-size: 11px;
}

QCheckBox::indicator {
    width: 20px;
    height: 20px;
    border: 2px solid #00ff00;
    background-color: #000000;
}

QCheckBox::indicator:checked {
    background-color: #00ff00;
    border: 2px solid #00cc00;
}

QCheckBox::indicator:hover {
    background-color: #001100;
    border: 2px solid #00ff00;
    box-shadow: 0 0 8px #00ff00;
}

QDialog {
    background-color: #000000;
    border: 3px solid #00ff00;
}

QDialog QLabel {
    color: #00ff00;
}

QDialogButtonBox QPushButton {
    min-width: 115px;
}

QMessageBox {
    background-color: #000000;
}

QMessageBox QLabel {
    color: #00ff00;
}

QProgressBar {
    border: 2px solid #00ff00;
    border-radius: 0px;
    text-align: center;
    background-color: #000000;
    color: #00ff00;
    font-weight: bold;
}

QProgressBar::chunk {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #001100,
        stop: 0.3 #00ff00,
        stop: 0.7 #00ff00,
        stop: 1 #001100
    );
}

QComboBox {
    background-color: #001100;
    color: #00ff00;
    border: 2px solid #00ff00;
    padding: 6px;
    min-width: 150px;
}

QComboBox:hover {
    border: 2px solid #00cc00;
    box-shadow: 0 0 8px #00ff00;
}

QComboBox::drop-down {
    border: none;
    width: 28px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 8px solid #00ff00;
    margin-right: 6px;
}

QComboBox QAbstractItemView {
    background-color: #000000;
    color: #00ff00;
    border: 2px solid #00ff00;
    selection-background-color: #00ff00;
    selection-color: #000000;
}

QMenuBar {
    background-color: #000000;
    color: #00ff00;
    border-bottom: 2px solid #00ff00;
}

QMenuBar::item {
    background-color: transparent;
    padding: 5px 10px;
}

QMenuBar::item:selected {
    background-color: #00ff00;
    color: #000000;
}

QMenu {
    background-color: #000000;
    color: #00ff00;
    border: 2px solid #00ff00;
}

QMenu::item:selected {
    background-color: #00ff00;
    color: #000000;
}

QScrollBar:vertical {
    background-color: #000000;
    width: 14px;
    border: 1px solid #00ff00;
}

QScrollBar::handle:vertical {
    background-color: #00ff00;
    min-height: 22px;
}

QScrollBar::handle:vertical:hover {
    background-color: #00cc00;
    box-shadow: 0 0 8px #00ff00;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background-color: #001100;
    height: 14px;
}

QScrollBar:horizontal {
    background-color: #000000;
    height: 14px;
    border: 1px solid #00ff00;
}

QScrollBar::handle:horizontal {
    background-color: #00ff00;
    min-width: 22px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #00cc00;
    box-shadow: 0 0 8px #00ff00;
}
"""

def get_matrix_style():
    return MATRIX_STYLE
