# -*- coding: utf-8 -*-

GTA6_STYLE = """
/* GTA 6 Theme - Vice City Neon Purple/Pink/Blue */
QWidget {
    background-color: #120322;
    color: #ff00ff;
    font-family: 'Arial', sans-serif;
    font-size: 11px;
}

QMainWindow {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 1,
        stop: 0 #120322,
        stop: 0.3 #1a0533,
        stop: 0.7 #0f1a33,
        stop: 1 #120322
    );
    border: 3px solid #ff00ff;
}

QPushButton {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 0.5 #8338ec,
        stop: 1 #3a86ff
    );
    color: #ffffff;
    border: 2px solid #ff00ff;
    border-radius: 8px;
    padding: 12px 28px;
    font-weight: bold;
    font-size: 13px;
    text-transform: uppercase;
    min-height: 34px;
}

QPushButton:hover {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff1a8c,
        stop: 0.5 #9b5bff,
        stop: 1 #5ba3ff
    );
    border: 2px solid #00ffff;
    box-shadow: 0 0 15px #ff00ff;
}

QPushButton:pressed {
    background-color: #1a0533;
    border: 2px solid #00ffff;
}

QPushButton:disabled {
    background-color: #1a0533;
    color: #555555;
    border: 2px solid #2d2d2d;
}

QLabel {
    color: #ff00ff;
    background-color: transparent;
    font-size: 12px;
    padding: 5px;
}

QLabel#title {
    font-size: 36px;
    font-weight: bold;
    color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff00ff,
        stop: 0.5 #00ffff,
        stop: 1 #ff00ff
    );
    text-shadow: 0 0 20px #ff00ff;
}

QLabel#subtitle {
    font-size: 16px;
    color: #00ffff;
    font-style: italic;
}

QListWidget {
    background-color: #0a0115;
    color: #ff00ff;
    border: 2px solid #8338ec;
    border-radius: 6px;
    padding: 8px;
    selection-background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 1 #3a86ff
    );
    selection-color: #ffffff;
}

QListWidget::item {
    padding: 10px;
    border-bottom: 1px solid #1a0533;
    border-radius: 4px;
}

QListWidget::item:hover {
    background-color: #1a0533;
    border-left: 4px solid #ff00ff;
    box-shadow: 0 0 10px #ff00ff;
}

QListWidget::item:selected {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 1 #3a86ff
    );
    color: #ffffff;
    border-left: 4px solid #00ffff;
    font-weight: bold;
}

QCheckBox {
    color: #ff00ff;
    spacing: 7px;
    font-size: 11px;
}

QCheckBox::indicator {
    width: 22px;
    height: 22px;
    border: 2px solid #ff00ff;
    background-color: #0a0115;
    border-radius: 4px;
}

QCheckBox::indicator:checked {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 1,
        stop: 0 #ff006e,
        stop: 1 #8338ec
    );
    border: 2px solid #00ffff;
}

QCheckBox::indicator:hover {
    background-color: #1a0533;
    border: 2px solid #00ffff;
    box-shadow: 0 0 8px #ff00ff;
}

QDialog {
    background-color: #120322;
    border: 3px solid qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 0.5 #8338ec,
        stop: 1 #3a86ff
    );
    border-radius: 10px;
}

QDialog QLabel {
    color: #ff00ff;
}

QDialogButtonBox QPushButton {
    min-width: 130px;
}

QMessageBox {
    background-color: #120322;
}

QMessageBox QLabel {
    color: #ff00ff;
}

QProgressBar {
    border: 2px solid #8338ec;
    border-radius: 10px;
    text-align: center;
    background-color: #0a0115;
    color: #ffffff;
    font-weight: bold;
    height: 22px;
}

QProgressBar::chunk {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 0.25 #8338ec,
        stop: 0.5 #3a86ff,
        stop: 0.75 #00ffff,
        stop: 1 #ff00ff
    );
    border-radius: 8px;
}

QComboBox {
    background-color: #0a0115;
    color: #ff00ff;
    border: 2px solid #8338ec;
    border-radius: 8px;
    padding: 8px;
    min-width: 160px;
}

QComboBox:hover {
    border: 2px solid #ff00ff;
    box-shadow: 0 0 10px #ff00ff;
}

QComboBox::drop-down {
    border: none;
    width: 32px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 10px solid #ff00ff;
    margin-right: 8px;
}

QComboBox QAbstractItemView {
    background-color: #0a0115;
    color: #ff00ff;
    border: 2px solid #8338ec;
    border-radius: 6px;
    selection-background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 1 #3a86ff
    );
    selection-color: #ffffff;
}

QScrollBar:vertical {
    background-color: #0a0115;
    width: 16px;
    border: 1px solid #8338ec;
    border-radius: 8px;
}

QScrollBar::handle:vertical {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #ff006e,
        stop: 1 #8338ec
    );
    border-radius: 7px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #ff1a8c,
        stop: 1 #9b5bff
    );
    box-shadow: 0 0 10px #ff00ff;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background-color: #1a0533;
    height: 16px;
    border-radius: 8px;
}

QScrollBar:horizontal {
    background-color: #0a0115;
    height: 16px;
    border: 1px solid #8338ec;
    border-radius: 8px;
}

QScrollBar::handle:horizontal {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 1 #3a86ff
    );
    border-radius: 7px;
    min-width: 30px;
}

QScrollBar::handle:horizontal:hover {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff1a8c,
        stop: 1 #5ba3ff
    );
    box-shadow: 0 0 10px #00ffff;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    background-color: #1a0533;
    width: 16px;
    border-radius: 8px;
}
"""

def get_gta6_style():
    return GTA6_STYLE
