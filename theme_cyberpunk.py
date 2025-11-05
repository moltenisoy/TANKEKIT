# -*- coding: utf-8 -*-

CYBERPUNK_STYLE = """
/* Cyberpunk 2077 Theme - Neon Yellow/Black */
QWidget {
    background-color: #0a0a0a;
    color: #fcee09;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 11px;
}

QMainWindow {
    background-color: #0a0a0a;
    border: 2px solid #fcee09;
}

QPushButton {
    background-color: #1a1a1a;
    color: #fcee09;
    border: 2px solid #fcee09;
    padding: 10px 20px;
    font-weight: bold;
    font-size: 12px;
    text-transform: uppercase;
    min-height: 30px;
}

QPushButton:hover {
    background-color: #fcee09;
    color: #0a0a0a;
    border: 2px solid #ff00ff;
    box-shadow: 0 0 20px #fcee09;
}

QPushButton:pressed {
    background-color: #ff00ff;
    color: #0a0a0a;
    border: 2px solid #00ffff;
}

QPushButton:disabled {
    background-color: #0f0f0f;
    color: #555555;
    border: 2px solid #333333;
}

QLabel {
    color: #fcee09;
    background-color: transparent;
    font-size: 12px;
    padding: 5px;
}

QLabel#title {
    font-size: 24px;
    font-weight: bold;
    color: #ff00ff;
    text-shadow: 0 0 10px #ff00ff;
}

QLabel#subtitle {
    font-size: 14px;
    color: #00ffff;
}

QListWidget {
    background-color: #111111;
    color: #fcee09;
    border: 2px solid #fcee09;
    padding: 5px;
    selection-background-color: #fcee09;
    selection-color: #0a0a0a;
}

QListWidget::item {
    padding: 8px;
    border-bottom: 1px solid #333333;
}

QListWidget::item:hover {
    background-color: #1a1a1a;
    border-left: 3px solid #ff00ff;
}

QListWidget::item:selected {
    background-color: #fcee09;
    color: #0a0a0a;
    border-left: 3px solid #ff00ff;
}

QCheckBox {
    color: #fcee09;
    spacing: 5px;
    font-size: 11px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border: 2px solid #fcee09;
    background-color: #111111;
}

QCheckBox::indicator:checked {
    background-color: #fcee09;
    border: 2px solid #ff00ff;
    image: url(none);
}

QCheckBox::indicator:checked:after {
    content: "✓";
    color: #0a0a0a;
    font-weight: bold;
}

QCheckBox::indicator:hover {
    border: 2px solid #ff00ff;
    box-shadow: 0 0 10px #ff00ff;
}

QDialog {
    background-color: #0a0a0a;
    border: 3px solid #fcee09;
}

QDialog QLabel {
    color: #fcee09;
}

QDialogButtonBox QPushButton {
    min-width: 100px;
}

QMessageBox {
    background-color: #0a0a0a;
}

QMessageBox QLabel {
    color: #fcee09;
}

QProgressBar {
    border: 2px solid #fcee09;
    border-radius: 0px;
    text-align: center;
    background-color: #111111;
    color: #fcee09;
    font-weight: bold;
}

QProgressBar::chunk {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #fcee09,
        stop: 0.5 #ff00ff,
        stop: 1 #00ffff
    );
}

QComboBox {
    background-color: #1a1a1a;
    color: #fcee09;
    border: 2px solid #fcee09;
    padding: 5px;
    min-width: 150px;
}

QComboBox:hover {
    border: 2px solid #ff00ff;
}

QComboBox::drop-down {
    border: none;
    width: 30px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 8px solid #fcee09;
    margin-right: 5px;
}

QComboBox QAbstractItemView {
    background-color: #111111;
    color: #fcee09;
    border: 2px solid #fcee09;
    selection-background-color: #fcee09;
    selection-color: #0a0a0a;
}

QMenuBar {
    background-color: #0a0a0a;
    color: #fcee09;
    border-bottom: 2px solid #fcee09;
}

QMenuBar::item {
    background-color: transparent;
    padding: 5px 10px;
}

QMenuBar::item:selected {
    background-color: #fcee09;
    color: #0a0a0a;
}

QMenu {
    background-color: #111111;
    color: #fcee09;
    border: 2px solid #fcee09;
}

QMenu::item:selected {
    background-color: #fcee09;
    color: #0a0a0a;
}

QScrollBar:vertical {
    background-color: #111111;
    width: 15px;
    border: 1px solid #fcee09;
}

QScrollBar::handle:vertical {
    background-color: #fcee09;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #ff00ff;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background-color: #1a1a1a;
    height: 15px;
}

QScrollBar:horizontal {
    background-color: #111111;
    height: 15px;
    border: 1px solid #fcee09;
}

QScrollBar::handle:horizontal {
    background-color: #fcee09;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #ff00ff;
}

/* Glowing effect for important elements */
.glow {
    text-shadow: 0 0 10px #fcee09, 0 0 20px #fcee09;
}

.glow-pink {
    text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff;
}

.glow-cyan {
    text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
}

/* Animated border effect */
@keyframes border-pulse {
    0%, 100% { border-color: #fcee09; }
    50% { border-color: #ff00ff; }
}
"""

def get_cyberpunk_style():
    return CYBERPUNK_STYLE
