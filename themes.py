# -*- coding: utf-8 -*-
"""
Unified Themes Module for TANKEKIT
Contains all theme definitions and metadata in a single file
"""

# Theme metadata - describes each available theme
THEME_METADATA = {
    "cyberpunk": {
        "name": "CYBERPUNK 2077",
        "description": "Futurista neón amarillo/magenta",
        "icon": "🟨",
        "colors": ["#fcee09", "#ff00ff", "#00ffff"],
        "version": "1.0",
        "display_order": 1
    },
    "ps5": {
        "name": "PS5",
        "description": "Minimalista blanco/azul limpio",
        "icon": "🔵",
        "colors": ["#0070cc", "#ffffff", "#f2f2f2"],
        "version": "1.0",
        "display_order": 2
    },
    "xbox360": {
        "name": "XBOX 360",
        "description": "Verde clásico gaming",
        "icon": "🟢",
        "colors": ["#9bca3b", "#2d2d2d", "#ffffff"],
        "version": "1.0",
        "display_order": 3
    },
    "gta6": {
        "name": "GTA 6",
        "description": "Vice City neon multi-color",
        "icon": "💜",
        "colors": ["#ff00ff", "#8338ec", "#3a86ff"],
        "version": "1.0",
        "display_order": 4
    },
    "matrix": {
        "name": "MATRIX",
        "description": "Terminal hacker verde",
        "icon": "💚",
        "colors": ["#00ff00", "#000000"],
        "version": "1.0",
        "display_order": 5
    }
}

# Cyberpunk 2077 Theme
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
    color: #0a0a0a;
    font-weight: bold;
}

QCheckBox::indicator:hover {
    border: 2px solid #ff00ff;
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

# PS5 Theme
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
    font-weight: 400;
    color: #555555;
}

QListWidget {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #dddddd;
    border-radius: 8px;
    padding: 8px;
    selection-background-color: #0070cc;
    selection-color: #ffffff;
}

QListWidget::item {
    padding: 12px;
    border-bottom: 1px solid #eeeeee;
    border-radius: 4px;
}

QListWidget::item:hover {
    background-color: #f0f0f0;
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
    width: 20px;
    height: 20px;
    border: 2px solid #cccccc;
    border-radius: 4px;
    background-color: #ffffff;
}

QCheckBox::indicator:checked {
    background-color: #0070cc;
    border: 2px solid #0070cc;
}

QCheckBox::indicator:hover {
    border: 2px solid #0070cc;
}

QDialog {
    background-color: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 12px;
}

QDialog QLabel {
    color: #000000;
}

QDialogButtonBox QPushButton {
    min-width: 100px;
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
    background-color: #e0e0e0;
    color: #000000;
    font-weight: 600;
    height: 8px;
}

QProgressBar::chunk {
    background-color: #0070cc;
    border-radius: 8px;
}

QComboBox {
    background-color: #ffffff;
    color: #000000;
    border: 2px solid #dddddd;
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
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 8px solid #0070cc;
    margin-right: 5px;
}

QComboBox QAbstractItemView {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #dddddd;
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
    background-color: #0070cc;
    min-height: 20px;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover {
    background-color: #0052a3;
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
    background-color: #0070cc;
    min-width: 20px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #0052a3;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}
"""

# Xbox 360 Theme
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
    border: 2px solid #555555;
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
    border: 2px solid #9bca3b;
    padding: 5px;
    selection-background-color: #9bca3b;
    selection-color: #000000;
}

QListWidget::item {
    padding: 10px;
    border-bottom: 1px solid #3d3d3d;
}

QListWidget::item:hover {
    background-color: #2d2d2d;
    border-left: 3px solid #9bca3b;
}

QListWidget::item:selected {
    background-color: #9bca3b;
    color: #000000;
    border-left: 3px solid #7ba82f;
}

QCheckBox {
    color: #ffffff;
    spacing: 5px;
    font-size: 11px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border: 2px solid #9bca3b;
    background-color: #1a1a1a;
}

QCheckBox::indicator:checked {
    background-color: #9bca3b;
    border: 2px solid #7ba82f;
}

QCheckBox::indicator:hover {
    border: 2px solid #b5e045;
}

QDialog {
    background-color: #2d2d2d;
    border: 3px solid #9bca3b;
}

QDialog QLabel {
    color: #ffffff;
}

QDialogButtonBox QPushButton {
    min-width: 100px;
}

QMessageBox {
    background-color: #2d2d2d;
}

QMessageBox QLabel {
    color: #ffffff;
}

QProgressBar {
    border: 2px solid #9bca3b;
    border-radius: 4px;
    text-align: center;
    background-color: #1a1a1a;
    color: #ffffff;
    font-weight: bold;
}

QProgressBar::chunk {
    background-color: #9bca3b;
    border-radius: 2px;
}

QComboBox {
    background-color: #1a1a1a;
    color: #ffffff;
    border: 2px solid #9bca3b;
    padding: 5px;
    min-width: 150px;
}

QComboBox:hover {
    border: 2px solid #b5e045;
}

QComboBox::drop-down {
    border: none;
    width: 30px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 8px solid #9bca3b;
    margin-right: 5px;
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
    border: 1px solid #9bca3b;
}

QScrollBar::handle:vertical {
    background-color: #9bca3b;
    min-height: 20px;
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
    border: 1px solid #9bca3b;
}

QScrollBar::handle:horizontal {
    background-color: #9bca3b;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #b5e045;
}
"""

# GTA 6 Theme
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
}

QPushButton:pressed {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #cc0058,
        stop: 0.5 #6b2bcc,
        stop: 1 #2d6acc
    );
    border: 2px solid #ff1a8c;
}

QPushButton:disabled {
    background-color: #1a1a2e;
    color: #555555;
    border: 2px solid #333344;
}

QLabel {
    color: #ff00ff;
    background-color: transparent;
    font-size: 12px;
    padding: 5px;
}

QLabel#title {
    font-size: 32px;
    font-weight: bold;
    color: #ff00ff;
    text-shadow: 0 0 20px #ff00ff, 0 0 40px #8338ec;
}

QLabel#subtitle {
    font-size: 16px;
    color: #3a86ff;
    text-shadow: 0 0 10px #3a86ff;
}

QListWidget {
    background-color: #0a0514;
    color: #ff00ff;
    border: 2px solid #ff00ff;
    padding: 5px;
    selection-background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 1 #8338ec
    );
    selection-color: #ffffff;
}

QListWidget::item {
    padding: 10px;
    border-bottom: 1px solid #2a1544;
}

QListWidget::item:hover {
    background-color: #1a0533;
    border-left: 4px solid #ff00ff;
}

QListWidget::item:selected {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 1 #8338ec
    );
    color: #ffffff;
    border-left: 4px solid #00ffff;
}

QCheckBox {
    color: #ff00ff;
    spacing: 5px;
    font-size: 11px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border: 2px solid #ff00ff;
    background-color: #0a0514;
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
    border: 2px solid #00ffff;
}

QDialog {
    background-color: #120322;
    border: 3px solid #ff00ff;
}

QDialog QLabel {
    color: #ff00ff;
}

QDialogButtonBox QPushButton {
    min-width: 100px;
}

QMessageBox {
    background-color: #120322;
}

QMessageBox QLabel {
    color: #ff00ff;
}

QProgressBar {
    border: 2px solid #ff00ff;
    border-radius: 8px;
    text-align: center;
    background-color: #0a0514;
    color: #ffffff;
    font-weight: bold;
}

QProgressBar::chunk {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 0.33 #8338ec,
        stop: 0.66 #3a86ff,
        stop: 1 #00ffff
    );
    border-radius: 6px;
}

QComboBox {
    background-color: #1a0533;
    color: #ff00ff;
    border: 2px solid #ff00ff;
    padding: 5px;
    min-width: 150px;
}

QComboBox:hover {
    border: 2px solid #00ffff;
}

QComboBox::drop-down {
    border: none;
    width: 30px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 8px solid #ff00ff;
    margin-right: 5px;
}

QComboBox QAbstractItemView {
    background-color: #0a0514;
    color: #ff00ff;
    border: 2px solid #ff00ff;
    selection-background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 1 #8338ec
    );
    selection-color: #ffffff;
}

QScrollBar:vertical {
    background-color: #0a0514;
    width: 14px;
    border: 1px solid #ff00ff;
}

QScrollBar::handle:vertical {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 1 #8338ec
    );
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff1a8c,
        stop: 1 #9b5bff
    );
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background-color: #1a0533;
    height: 14px;
}

QScrollBar:horizontal {
    background-color: #0a0514;
    height: 14px;
    border: 1px solid #ff00ff;
}

QScrollBar::handle:horizontal {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff006e,
        stop: 1 #8338ec
    );
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #ff1a8c,
        stop: 1 #9b5bff
    );
}
"""

# Matrix Theme
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
    font-size: 26px;
    font-weight: bold;
    color: #00ff00;
    text-shadow: 0 0 15px #00ff00;
}

QLabel#subtitle {
    font-size: 14px;
    color: #00cc00;
}

QListWidget {
    background-color: #000000;
    color: #00ff00;
    border: 2px solid #00ff00;
    padding: 5px;
    selection-background-color: #00ff00;
    selection-color: #000000;
}

QListWidget::item {
    padding: 8px;
    border-bottom: 1px solid #003300;
}

QListWidget::item:hover {
    background-color: #001100;
    border-left: 3px solid #00ff00;
}

QListWidget::item:selected {
    background-color: #00ff00;
    color: #000000;
    border-left: 3px solid #00cc00;
}

QCheckBox {
    color: #00ff00;
    spacing: 5px;
    font-size: 11px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border: 2px solid #00ff00;
    background-color: #000000;
}

QCheckBox::indicator:checked {
    background-color: #00ff00;
    border: 2px solid #00cc00;
}

QCheckBox::indicator:hover {
    border: 2px solid #00ff00;
}

QDialog {
    background-color: #000000;
    border: 3px solid #00ff00;
}

QDialog QLabel {
    color: #00ff00;
}

QDialogButtonBox QPushButton {
    min-width: 100px;
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
    background-color: #00ff00;
}

QComboBox {
    background-color: #001100;
    color: #00ff00;
    border: 2px solid #00ff00;
    padding: 5px;
    min-width: 150px;
}

QComboBox:hover {
    border: 2px solid #00cc00;
}

QComboBox::drop-down {
    border: none;
    width: 30px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 8px solid #00ff00;
    margin-right: 5px;
}

QComboBox QAbstractItemView {
    background-color: #000000;
    color: #00ff00;
    border: 2px solid #00ff00;
    selection-background-color: #00ff00;
    selection-color: #000000;
}

QScrollBar:vertical {
    background-color: #000000;
    width: 14px;
    border: 1px solid #00ff00;
}

QScrollBar::handle:vertical {
    background-color: #00ff00;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #00cc00;
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
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #00cc00;
}
"""

# Theme registry - maps theme keys to their style strings
THEMES = {
    "cyberpunk": CYBERPUNK_STYLE,
    "ps5": PS5_STYLE,
    "xbox360": XBOX360_STYLE,
    "gta6": GTA6_STYLE,
    "matrix": MATRIX_STYLE
}

# Getter functions for backward compatibility
def get_cyberpunk_style():
    """Returns Cyberpunk 2077 theme stylesheet"""
    return CYBERPUNK_STYLE

def get_ps5_style():
    """Returns PS5 theme stylesheet"""
    return PS5_STYLE

def get_xbox360_style():
    """Returns Xbox 360 theme stylesheet"""
    return XBOX360_STYLE

def get_gta6_style():
    """Returns GTA 6 theme stylesheet"""
    return GTA6_STYLE

def get_matrix_style():
    """Returns Matrix theme stylesheet"""
    return MATRIX_STYLE

def get_theme(theme_key):
    """
    Get a theme by its key
    
    Args:
        theme_key: One of 'cyberpunk', 'ps5', 'xbox360', 'gta6', 'matrix'
    
    Returns:
        Theme stylesheet string
    
    Raises:
        ValueError: If theme_key is not valid
    """
    if theme_key not in THEMES:
        raise ValueError(f"Invalid theme key: '{theme_key}'. Available themes: {list(THEMES.keys())}")
    return THEMES[theme_key]

def get_all_themes():
    """Returns dictionary of all available themes"""
    return THEMES.copy()

def get_theme_metadata(theme_key=None):
    """
    Get theme metadata
    
    Args:
        theme_key: Optional theme key. If None, returns all metadata
    
    Returns:
        Theme metadata dict or all metadata if theme_key is None
    """
    if theme_key:
        return THEME_METADATA.get(theme_key)
    return THEME_METADATA.copy()

def get_theme_list(sorted_by_display_order=True):
    """
    Returns list of available theme keys
    
    Args:
        sorted_by_display_order: If True, returns themes sorted by display_order
    
    Returns:
        List of theme keys
    """
    if sorted_by_display_order:
        # Sort by display_order from metadata
        return sorted(THEMES.keys(), key=lambda k: THEME_METADATA[k].get('display_order', 999))
    return list(THEMES.keys())
