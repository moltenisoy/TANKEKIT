# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bloatware_remover import *
from theme_cyberpunk import get_cyberpunk_style
from i18n import i18n

class CyberpunkUninstallerApp(UninstallerApp):
    def initUI(self):
        super().initUI()
        self.setStyleSheet(get_cyberpunk_style())
        self.setWindowTitle(i18n.get("app_title") + " - CYBERPUNK 2077 EDITION")
        
        lang_layout = QHBoxLayout()
        lang_label = QLabel(i18n.get("language") + ":")
        self.lang_combo = QComboBox()
        self.lang_combo.addItems([i18n.get("spanish"), i18n.get("english")])
        self.lang_combo.currentIndexChanged.connect(self.change_language)
        lang_layout.addWidget(lang_label)
        lang_layout.addWidget(self.lang_combo)
        lang_layout.addStretch()
        
        self.layout().insertLayout(0, lang_layout)
    
    def change_language(self, index):
        lang = "es" if index == 0 else "en"
        i18n.set_language(lang)
        self.info_label.setText(i18n.get("welcome_msg"))
        self.detect_button.setText(i18n.get("detect_button"))
        self.remove_button.setText(i18n.get("remove_button"))
        self.select_all_checkbox.setText(i18n.get("select_all"))
        self.setWindowTitle(i18n.get("app_title") + " - CYBERPUNK 2077 EDITION")

if __name__ == '__main__':
    if not is_admin():
        if request_admin_privileges():
            logging.info("Elevación solicitada. Saliendo del proceso no elevado.")
            sys.exit(0)
        else:
            logging.error("No se obtuvieron privilegios de administrador. Saliendo.")
            print("ERROR: " + i18n.get("admin_required"))
            try:
                app_temp = QApplication.instance() or QApplication(sys.argv)
                QMessageBox.critical(None, i18n.get("permission_error"), i18n.get("admin_required"))
            except:
                input("Press Enter to exit...")
            sys.exit(1)

    logging.info("Ejecutando con privilegios de administrador.")
    app = QApplication(sys.argv)
    ex = CyberpunkUninstallerApp()
    ex.show()
    sys.exit(app.exec())
