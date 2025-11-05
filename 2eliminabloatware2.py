# -*- coding: utf-8 -*-

import sys
import os
import winreg
import subprocess
import ctypes
import logging
import shutil
import time
import re
from pathlib import Path

try:
    import psutil
except ImportError:
    print("El módulo 'psutil' no está instalado. Instalándolo...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    import psutil

try:
    import wmi
except ImportError:
    print("El módulo 'wmi' no está instalado. Instalándolo...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "WMI"])
    import wmi

try:
    from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                                   QListWidget, QListWidgetItem, QLabel, QMessageBox,
                                   QDialog, QDialogButtonBox, QProgressDialog, QCheckBox)
    from PySide6.QtCore import Qt, QThread, Signal
    from PySide6.QtGui import QIcon
except ImportError:
    print("El módulo 'PySide6' no está instalado. Instalándolo...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PySide6"])
    try:
        from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                                       QListWidget, QListWidgetItem, QLabel, QMessageBox,
                                       QDialog, QDialogButtonBox, QProgressDialog, QCheckBox)
        from PySide6.QtCore import Qt, QThread, Signal
        from PySide6.QtGui import QIcon
    except ImportError:
        print("Error: No se pudo instalar PySide6. Asegúrate de tener pip y Python configurados.")
        input("Presiona Enter para salir.")
        sys.exit(1)


log_file = Path(os.getenv('TEMP', '.')) / 'aggressive_uninstaller_log.txt'
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    encoding='utf-8')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)


TARGET_SOFTWARE = {
    "3D Viewer": {"type": "Bloatware", "detection": ["Microsoft.Microsoft3DViewer"]},
    "Paint 3D": {"type": "Bloatware", "detection": ["Microsoft.MSPaint"]},
    "Print 3D": {"type": "Bloatware", "detection": ["Microsoft.Print3D"]},
    "Mixed Reality Portal": {"type": "Bloatware", "detection": ["Microsoft.MixedReality.Portal"]},
    "Clipchamp": {"type": "Bloatware", "detection": ["Clipchamp", "Microsoft.Clipchamp"]},
    "Adobe Express": {"type": "Bloatware", "detection": ["Adobe Express", "AdobeSystemsIncorporated.AdobeExpress"]},
    "Candy Crush Saga": {"type": "Adware/Juego", "detection": ["king.com.CandyCrushSaga", "Candy Crush Saga"]},
    "Candy Crush Soda Saga": {"type": "Adware/Juego", "detection": ["king.com.CandyCrushSodaSaga", "Candy Crush Soda Saga"]},
    "Candy Crush Friends Saga": {"type": "Adware/Juego", "detection": ["king.com.CandyCrushFriendsSaga", "Candy Crush Friends Saga"]},
    "FarmVille 2: Country Escape": {"type": "Adware/Juego", "detection": ["ZyngaInc.FarmVille2CountryEscape", "FarmVille 2"]},
    "Hidden City: Hidden Object": {"type": "Adware/Juego", "detection": ["G5EntertainmentAB.HiddenCityHiddenObjectAdventure", "Hidden City"]},
    "Bubble Witch 3 Saga": {"type": "Adware/Juego", "detection": ["king.com.BubbleWitch3Saga", "Bubble Witch 3 Saga"]},
    "Asphalt 8: Airborne": {"type": "Adware/Juego", "detection": ["GAMELOFTSA.Asphalt8Airborne", "Asphalt 8"]},
    "Age of Empires: Castle Siege": {"type": "Bloatware", "detection": ["Microsoft.AgeofEmpiresCastleSiege", "Age of Empires: Castle Siege"]},
    "Minecraft": {"type": "Bloatware", "detection": ["Microsoft.MinecraftUWP", "Minecraft for Windows"]},
    "Microsoft Solitaire Collection": {"type": "Adware/Juego", "detection": ["Microsoft.MicrosoftSolitaireCollection"]},
    "Roblox": {"type": "Adware/Juego", "detection": ["ROBLOXCORPORATION.ROBLOX", "Roblox"]},
    "TikTok": {"type": "Bloatware", "detection": ["ByteDancePte.Ltd.TikTok", "TikTok"]},
    "Instagram": {"type": "Bloatware", "detection": ["Facebook.InstagramBeta", "Instagram"]},
    "Facebook": {"type": "Bloatware", "detection": ["Facebook.Facebook", "Facebook"]},
    "Twitter": {"type": "Bloatware", "detection": ["9E2F88E3.Twitter", "Twitter"]},
    "Netflix": {"type": "Bloatware", "detection": ["Netflix.Netflix", "Netflix"]},
    "Prime Video": {"type": "Bloatware", "detection": ["AmazonVideo.PrimeVideo", "Prime Video"]},
    "Spotify": {"type": "Bloatware", "detection": ["SpotifyAB.SpotifyMusic", "Spotify"]},
    "Farm Heroes Saga": {"type": "Adware/Juego", "detection": ["king.com.FarmHeroesSaga", "Farm Heroes Saga"]},
    "Duolingo": {"type": "Bloatware", "detection": ["Duolingo.Duolingo-LearnLanguagesforFree", "Duolingo"]},
    "World of Tanks Blitz": {"type": "Bloatware", "detection": ["WargamingGroupLimited.WorldofTanksBlitz", "World of Tanks Blitz"]},
    "Disney Magic Kingdoms": {"type": "Adware/Juego", "detection": ["GAMELOFTSA.DisneyMagicKingdoms", "Disney Magic Kingdoms"]},
    "Microsoft News": {"type": "Bloatware", "detection": ["Microsoft.BingNews", "Noticias"]},
    "Tiempo": {"type": "Bloatware", "detection": ["Microsoft.BingWeather"]},
    "Cortana": {"type": "Spyware", "detection": ["Microsoft.549981C3F5F10"]},
    "OneDrive": {"type": "Bloatware", "detection": ["OneDrive", "Microsoft OneDrive"]},
    "Microsoft Teams": {"type": "Bloatware", "detection": ["Microsoft Teams", "Teams Machine-Wide Installer"]},
    "OneNote": {"type": "Bloatware", "detection": ["Microsoft.Office.OneNote"]},
    "Xbox Game Bar": {"type": "Bloatware", "detection": ["Microsoft.XboxGamingOverlay"]},
    "Xbox Console Companion": {"type": "Bloatware", "detection": ["Microsoft.XboxApp"]},
    "Your Phone": {"type": "Bloatware", "detection": ["Microsoft.YourPhone", "Enlace Móvil", "Phone Link"]},
    "Consejos": {"type": "Bloatware", "detection": ["Microsoft.Getstarted", "Microsoft Tips"]},
    "Feedback Hub": {"type": "Bloatware", "detection": ["Microsoft.WindowsFeedbackHub", "Centro de opiniones"]},
    "McAfee": {"type": "Trial AV", "detection": ["McAfee", "McAfee Security Scan Plus"]},
    "Norton": {"type": "Trial AV", "detection": ["Norton", "Symantec"]},
    "Microsoft Office": {"type": "Trialware", "detection": ["Microsoft Office 365", "Microsoft 365"]},
    "WinZip": {"type": "Bloatware", "detection": ["WinZip"]},
    "WPS Office": {"type": "Bloatware", "detection": ["WPS Office"]},
    "Dropbox": {"type": "Bloatware", "detection": ["Dropbox OEM"]},
    "Evernote": {"type": "Bloatware", "detection": ["Evernote OEM"]},
    "WildTangent Games": {"type": "Bloatware", "detection": ["WildTangent"]},
    "CyberLink": {"type": "Bloatware", "detection": ["CyberLink"]},
    "Roxio": {"type": "Bloatware", "detection": ["Roxio"]},
    "Nero": {"type": "Bloatware", "detection": ["Nero"]},
    "HP Support Assistant": {"type": "Bloatware", "detection": ["HP Support Assistant"]},
    "HP JumpStart": {"type": "Bloatware", "detection": ["HP JumpStart"]},
    "HP Audio Switch": {"type": "Bloatware", "detection": ["HP Audio Switch"]},
    "HP Connection Optimizer": {"type": "Bloatware", "detection": ["HP Connection Optimizer"]},
    "HP Command Center": {"type": "Bloatware", "detection": ["HP Command Center", "OMEN Command Center"]},
    "HP Touchpoint Analytics": {"type": "Spyware", "detection": ["HP Touchpoint Analytics Client"]},
    "Dell SupportAssist": {"type": "Bloatware", "detection": ["Dell SupportAssist"]},
    "Dell Update": {"type": "Bloatware", "detection": ["Dell Update", "Dell Digital Delivery"]},
    "Dell Customer Connect": {"type": "Bloatware", "detection": ["Dell Customer Connect"]},
    "Dell Mobile Connect": {"type": "Bloatware", "detection": ["Dell Mobile Connect"]},
    "Lenovo Vantage": {"type": "Utility", "detection": ["Lenovo Vantage"]},
    "Lenovo Solution Center": {"type": "Bloatware", "detection": ["Lenovo Solution Center"]},
    "Lenovo Accelerator": {"type": "Bloatware/Vuln", "detection": ["Lenovo Accelerator Application"]},
    "Lenovo App Explorer": {"type": "Bloatware", "detection": ["Lenovo App Explorer"]},
    "ASUS GiftBox": {"type": "Bloatware", "detection": ["ASUS GiftBox", "ASUS AppDeals"]},
    "ASUS Live Update": {"type": "Bloatware/Vuln", "detection": ["ASUS Live Update"]},
    "MyASUS": {"type": "Bloatware", "detection": ["MyASUS", "ASUS System Control Interface"]},
    "Acer Care Center": {"type": "Bloatware", "detection": ["Acer Care Center"]},
    "Acer Product Registration": {"type": "Bloatware", "detection": ["Acer Product Registration"]},
    "Acer Portal": {"type": "Bloatware", "detection": ["Acer BYOC Apps", "abDocs", "abFiles"]},
    "MSI Dragon Center": {"type": "Bloatware", "detection": ["MSI Dragon Center"]},
    "MSI App Player": {"type": "Bloatware", "detection": ["MSI App Player"]},
    "Samsung Settings": {"type": "Bloatware", "detection": ["Samsung Settings", "Samsung Update"]},
    "VAIO Care": {"type": "Bloatware", "detection": ["VAIO Care", "VAIO Control Center"]},
    "Ask Toolbar": {"type": "Adware/Toolbar", "detection": ["Ask Toolbar", "Updater by Ask", "Ask.com"]},
    "MyWay": {"type": "Adware/Browser Hijacker", "detection": ["MyWay", "MindSpark"]},
    "Conduit": {"type": "Adware/Hijacker", "detection": ["Conduit", "Search Protect"]},
    "SweetIM": {"type": "Adware/Spyware", "detection": ["SweetIM"]},
    "RelevantKnowledge": {"type": "Spyware", "detection": ["RelevantKnowledge"]},
    "DealPly": {"type": "Adware", "detection": ["DealPly"]},
    "Snap.do": {"type": "Browser Hijacker", "detection": ["Snap.do"]},
    "Funmoods": {"type": "Adware/Hijacker", "detection": ["Funmoods"]},
    "Yontoo": {"type": "Adware", "detection": ["Yontoo"]},
    "Crossrider": {"type": "Adware Platform", "detection": ["Crossrider"]},
    "Babylon": {"type": "Adware/Hijacker", "detection": ["Babylon"]},
    "Delta Search": {"type": "Adware/Hijacker", "detection": ["Delta Search"]},
    "Spigot": {"type": "Adware", "detection": ["Spigot"]},
    "Segurazo": {"type": "Rogue AV", "detection": ["Segurazo", "SAntivirus"]},
    "SpyHunter": {"type": "PUP/Rogue", "detection": ["SpyHunter"]},
    "Advanced SystemCare": {"type": "PUP/Optimizador", "detection": ["Advanced SystemCare"]},
    "Driver Booster": {"type": "PUP/Driver Updater", "detection": ["Driver Booster"]},
    "DriverPack Solution": {"type": "Adware/Bundle", "detection": ["DriverPack Solution", "DriverPack Notifier"]},
    "Driver Easy": {"type": "PUP/Driver Updater", "detection": ["Driver Easy"]},
    "SlimDrivers": {"type": "PUP/Driver Updater", "detection": ["SlimDrivers"]},
    "Slimware Utilities": {"type": "PUP/Optimizer", "detection": ["Slimware Utilities", "DriverUpdate"]},
    "WinZip Driver Updater": {"type": "PUP/Driver Updater", "detection": ["WinZip Driver Updater"]},
    "PC Accelerate Pro": {"type": "PUP/Optimizer", "detection": ["PC Accelerate Pro"]},
    "PC Speed Up": {"type": "PUP/Optimizer", "detection": ["PC Speed Up", "PC Optimizer Pro"]},
    "OneSafe PC Cleaner": {"type": "PUP/Optimizer", "detection": ["OneSafe PC Cleaner"]},
    "Advanced System Protector": {"type": "PUP/AntiSpyware", "detection": ["Advanced System Protector"]},
    "RegClean Pro": {"type": "PUP/Registry Cleaner", "detection": ["RegClean Pro"]},
    "Reimage Repair": {"type": "PUP/Scareware", "detection": ["Reimage Repair"]},
    "Restoro": {"type": "PUP/Scareware", "detection": ["Restoro"]},
    "Outbyte PC Repair": {"type": "PUP/Scareware", "detection": ["Outbyte PC Repair"]},
    "TotalAV": {"type": "PUP/Antivirus", "detection": ["TotalAV", "PC Protect"]},
    "Driver Support": {"type": "PUP/Driver Updater", "detection": ["Driver Support", "Asurvio"]},
    "Hola VPN": {"type": "Adware/P2P", "detection": ["Hola VPN"]},
    "KMSPico": {"type": "HackTool/Troyano", "detection": ["KMSPico", "KMSpico Portable"]},
    "CCleaner": {"type": "Useless/Risky", "detection": ["CCleaner", "Piriform", "ccsetup"]},
    "Armoury Crate": {"type": "Bloatware/Persistent", "detection": ["Armoury Crate", "ArmouryCrateInstaller"]},
    "Microsoft Photos": {"type": "Bloatware", "detection": ["Microsoft.Windows.Photos", "Microsoft Photos"]},
    "Mail and Calendar": {"type": "Bloatware", "detection": ["microsoft.windowscommunicationsapps", "Mail and Calendar", "Correo y Calendario"]},
}


def is_admin():
    """ Comprueba si el script se ejecuta con privilegios de administrador """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        logging.error(f"Error al comprobar privilegios de admin: {e}")
        return False

def request_admin_privileges():
    """ Solicita elevación de privilegios UAC """
    if sys.platform == 'win32':
        try:
            logging.info("Solicitando elevación de privilegios UAC...")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            return True
        except Exception as e:
            logging.error(f"Error al solicitar elevación: {e}")
            QMessageBox.critical(None, "Error de Permisos", f"No se pudieron obtener los privilegios de administrador necesarios.\nError: {e}")
            return False
    else:
        logging.warning("La solicitud de elevación solo es compatible con Windows.")
        return False

def safe_str_compare(s1, s2):
    """ Comparación de cadenas insensible a mayúsculas y robusta a None """
    if s1 is None or s2 is None:
        return False
    try:
        return s1.strip().lower() == s2.strip().lower()
    except AttributeError:
        return False

def matches_target(display_name, publisher, detection_terms):
    """ Comprueba si un nombre o publicador coincide con los términos de detección """
    if not display_name and not publisher:
        return False
    name_lower = display_name.lower() if display_name else ""
    pub_lower = publisher.lower() if publisher else ""

    for term in detection_terms:
        term_lower = term.lower()
        if term_lower in name_lower or term_lower in pub_lower:
            return True
        if safe_str_compare(display_name, term) or safe_str_compare(publisher, term):
             return True
    return False

def get_registry_value(key, subkey_name, value_name):
    """ Obtiene un valor específico del registro, manejando errores """
    try:
        with winreg.OpenKey(key, subkey_name) as subkey_handle:
            value, reg_type = winreg.QueryValueEx(subkey_handle, value_name)
            return str(value) if value is not None else None
    except FileNotFoundError:
        return None
    except OSError as e:
        logging.warning(f"Error OS al leer registro {winreg.HKEY_NAMES.get(key.handle, key.handle)}\\{subkey_name}\\{value_name}: {e}")
        return None
    except Exception as e:
        logging.error(f"Error inesperado al leer registro {winreg.HKEY_NAMES.get(key.handle, key.handle)}\\{subkey_name}\\{value_name}: {e}")
        return None

def delete_registry_key_recursive(root_hive, key_path, view=0):
    """ Elimina recursivamente una clave del registro y sus subclaves """
    try:
        key_handle = winreg.OpenKey(root_hive, key_path, 0, winreg.KEY_READ | winreg.KEY_WRITE | view)
    except FileNotFoundError:
        logging.info(f"Clave de registro no encontrada (ya eliminada?): {key_path}")
        return True
    except PermissionError:
        logging.warning(f"Permiso denegado al abrir clave de registro para eliminar: {key_path}")
        return False
    except OSError as e:
        logging.error(f"Error OS al abrir clave de registro {key_path}: {e}")
        return False

    try:
        i = 0
        while True:
            try:
                subkey_name = winreg.EnumKey(key_handle, i)
                subkey_full_path = f"{key_path}\\{subkey_name}"
                if not delete_registry_key_recursive(root_hive, subkey_full_path, view):
                    winreg.CloseKey(key_handle)
                    return False
            except OSError:
                break
    finally:
        winreg.CloseKey(key_handle)

    try:
        winreg.DeleteKeyEx(root_hive, key_path, view, 0)
        logging.info(f"Clave de registro eliminada exitosamente: {key_path}")
        return True
    except FileNotFoundError:
        logging.info(f"Clave de registro no encontrada durante la eliminación final: {key_path}")
        return True
    except PermissionError:
        logging.warning(f"Permiso denegado al eliminar clave de registro: {key_path}")
        return False
    except OSError as e:
        logging.error(f"Error OS al eliminar clave de registro {key_path}: {e}")
        return False

def handle_shutil_error(func, path, excinfo):
    """ Manejador de errores para shutil.rmtree """
    etype, evalue, etb = excinfo
    logging.warning(f"Error al eliminar '{path}' usando {func.__name__}: {evalue}")


class Worker(QThread):
    """ Worker para ejecutar tareas largas (detección, desinstalación) sin bloquear la GUI """
    progress = Signal(int, str)
    finished = Signal(list)
    detection_complete = Signal(list)

    def __init__(self, mode, apps_to_remove=None):
        super().__init__()
        self.mode = mode
        self.apps_to_remove = apps_to_remove if apps_to_remove else []
        self.detected_software = []

    def run(self):
        if self.mode == 'detect':
            self.detect_software()
            self.detection_complete.emit(self.detected_software)
        elif self.mode == 'remove':
            results = self.remove_selected_software()
            self.finished.emit(results)

    def _add_detected_app(self, app_info, checked_display_names):
        """ Helper para añadir app detectada evitando duplicados """
        display_name = app_info.get("name")
        if not display_name:
            return False

        # Comprobar si ya existe una entrada con nombre similar (ignorando versión, etc.)
        for existing_app in self.detected_software:
            if safe_str_compare(existing_app.get("name"), display_name):
                 # Podríamos actualizar info si esta es mejor? Por ahora, evitamos duplicados.
                 # logging.debug(f"Duplicado detectado: {display_name} (Método nuevo: {app_info.get('method')}, Existente: {existing_app.get('method')})")
                 return False # Ya existe

        self.detected_software.append(app_info)
        checked_display_names.add(display_name) # Añadir a lista global de revisados
        logging.info(f"Detectado ({app_info.get('method')}): {display_name} ({app_info.get('type')})")
        return True

    def detect_via_registry(self, checked_display_names):
        """ Búsqueda en el Registro """
        logging.info("Iniciando detección por Registro...")
        detected_count = 0
        registry_keys_to_check = [
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
        ]
        access_flags = [winreg.KEY_READ | winreg.KEY_WOW64_64KEY, winreg.KEY_READ | winreg.KEY_WOW64_32KEY]

        for root_hive, key_path in registry_keys_to_check:
            views = access_flags if root_hive == winreg.HKEY_LOCAL_MACHINE else [winreg.KEY_READ]
            for view in views:
                try:
                    with winreg.OpenKey(root_hive, key_path, 0, view) as key_handle:
                        i = 0
                        while True:
                            try:
                                subkey_name = winreg.EnumKey(key_handle, i)
                                full_subkey_path = f"{key_path}\\{subkey_name}"
                                display_name = get_registry_value(root_hive, full_subkey_path, "DisplayName")
                                publisher = get_registry_value(root_hive, full_subkey_path, "Publisher")
                                version = get_registry_value(root_hive, full_subkey_path, "DisplayVersion")
                                uninstall_string = get_registry_value(root_hive, full_subkey_path, "UninstallString")
                                install_location = get_registry_value(root_hive, full_subkey_path, "InstallLocation")
                                product_code = subkey_name if subkey_name.startswith('{') and subkey_name.endswith('}') else None

                                if display_name:
                                    for target_name, data in TARGET_SOFTWARE.items():
                                        if matches_target(display_name, publisher, data["detection"]):
                                            app_info = {
                                                "name": display_name,
                                                "version": version,
                                                "publisher": publisher,
                                                "type": data["type"],
                                                "method": "Registro",
                                                "uninstall_string": uninstall_string,
                                                "install_location": install_location,
                                                "product_code": product_code,
                                                "registry_path": f"{winreg.HKEY_NAMES.get(root_hive.handle, root_hive.handle)}\\{full_subkey_path}",
                                                "is_uwp": False,
                                                "detection_term": target_name,
                                                "vendor_for_cleanup": publisher,
                                            }
                                            if self._add_detected_app(app_info, checked_display_names):
                                                 detected_count += 1
                                            break
                                i += 1
                            except OSError:
                                break
                            except Exception as e_inner:
                                logging.error(f"Error enumerando subclave en {key_path}: {e_inner}")
                                i += 1
                except FileNotFoundError:
                    logging.info(f"Clave de registro no encontrada: {winreg.HKEY_NAMES.get(root_hive.handle, root_hive.handle)}\\{key_path}")
                except PermissionError:
                     logging.warning(f"Permiso denegado al acceder a clave de registro: {winreg.HKEY_NAMES.get(root_hive.handle, root_hive.handle)}\\{key_path}")
                except Exception as e_outer:
                    logging.error(f"Error al acceder a clave de registro {winreg.HKEY_NAMES.get(root_hive.handle, root_hive.handle)}\\{key_path}: {e_outer}")
        logging.info(f"Detección por Registro finalizada. {detected_count} nuevos elementos encontrados.")

    def detect_via_uwp_powershell(self, checked_display_names):
        """ Búsqueda de Apps UWP (PowerShell) """
        logging.info("Iniciando detección UWP (PowerShell)...")
        detected_count = 0
        try:
            ps_command = "Get-AppxPackage -AllUsers | Select-Object Name, PackageFullName, Publisher, InstallLocation | ConvertTo-Json -Compress"
            result = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_command],
                                    capture_output=True, text=True, check=True, encoding='utf-8', errors='ignore')
            import json
            try:
                uwp_apps = json.loads(result.stdout)
                if isinstance(uwp_apps, dict):
                    uwp_apps = [uwp_apps]

                if isinstance(uwp_apps, list):
                    for app in uwp_apps:
                        display_name = app.get("Name")
                        publisher = app.get("Publisher")
                        package_full_name = app.get("PackageFullName")
                        install_location = app.get("InstallLocation")

                        common_publisher = publisher.split('CN=')[1].split(',')[0] if publisher and 'CN=' in publisher else publisher

                        if display_name and package_full_name:
                             for target_name, data in TARGET_SOFTWARE.items():
                                if matches_target(display_name, common_publisher, data["detection"]) or \
                                   any(term.lower() in package_full_name.lower() for term in data["detection"]):

                                    app_info = {
                                        "name": display_name,
                                        "version": package_full_name.split('_')[1] if '_' in package_full_name else None,
                                        "publisher": common_publisher,
                                        "type": data["type"],
                                        "method": "UWP (PowerShell)",
                                        "package_full_name": package_full_name,
                                        "install_location": install_location,
                                        "is_uwp": True,
                                        "detection_term": target_name,
                                        "vendor_for_cleanup": common_publisher,
                                    }
                                    if self._add_detected_app(app_info, checked_display_names):
                                         detected_count += 1
                                    break
            except json.JSONDecodeError as json_err:
                logging.error(f"Error decodificando salida JSON de PowerShell: {json_err}")
                logging.debug(f"Salida PowerShell (stdout): {result.stdout}")
                logging.debug(f"Salida PowerShell (stderr): {result.stderr}")
            except Exception as parse_err:
                 logging.error(f"Error procesando apps UWP: {parse_err}")

        except subprocess.CalledProcessError as ps_err:
            logging.error(f"Error al ejecutar PowerShell para buscar UWP: {ps_err}")
            logging.error(f"PowerShell stderr: {ps_err.stderr}")
        except FileNotFoundError:
            logging.error("Error: PowerShell no encontrado. No se pueden detectar apps UWP.")
        except Exception as e:
            logging.error(f"Error inesperado buscando apps UWP: {e}")
        logging.info(f"Detección UWP (PowerShell) finalizada. {detected_count} nuevos elementos encontrados.")

    def detect_via_filesystem(self, checked_display_names):
        """ Búsqueda en Sistema de Archivos (Portable/Restos) """
        logging.info("Iniciando detección por Sistema de Archivos...")
        detected_count = 0
        search_dirs = [
            Path(os.environ.get('ProgramFiles', 'C:\\Program Files')),
            Path(os.environ.get('ProgramFiles(x86)', 'C:\\Program Files (x86)')),
            Path(os.environ.get('ProgramData', 'C:\\ProgramData')),
            Path.home() / 'AppData' / 'Local',
            Path.home() / 'AppData' / 'Roaming',
        ]

        for base_dir in search_dirs:
            if not base_dir.exists():
                continue
            logging.debug(f"Escaneando directorio: {base_dir}")
            try:
                for item in base_dir.iterdir():
                     if item.is_dir() or item.is_file():
                         item_name = item.name
                         for target_name, data in TARGET_SOFTWARE.items():
                             if any(term.lower() in item_name.lower() for term in data["detection"]):
                                 app_info = {
                                     "name": item_name,
                                     "version": "N/A",
                                     "publisher": "Desconocido (Archivo)",
                                     "type": data["type"] + " (Portable/Resto?)",
                                     "method": "Sistema de Archivos",
                                     "install_location": str(item.resolve()),
                                     "is_uwp": False,
                                     "is_portable_heuristic": True,
                                     "detection_term": target_name,
                                     "vendor_for_cleanup": None,
                                 }
                                 if self._add_detected_app(app_info, checked_display_names):
                                      detected_count += 1
                                 break
            except PermissionError:
                logging.warning(f"Permiso denegado al escanear: {base_dir}")
            except Exception as fs_err:
                logging.error(f"Error escaneando {base_dir}: {fs_err}")
        logging.info(f"Detección por Sistema de Archivos finalizada. {detected_count} nuevos elementos encontrados.")

    def detect_via_wmi(self, checked_display_names):
        """ Búsqueda usando WMI Win32_Product """
        logging.info("Iniciando detección por WMI (Win32_Product)...")
        detected_count = 0
        try:
            c = wmi.WMI()
            for product in c.Win32_Product():
                display_name = getattr(product, "Name", None)
                publisher = getattr(product, "Vendor", None)
                version = getattr(product, "Version", None)
                install_location = getattr(product, "InstallLocation", None)
                product_code = getattr(product, "IdentifyingNumber", None) # Código MSI

                if display_name:
                    for target_name, data in TARGET_SOFTWARE.items():
                        if matches_target(display_name, publisher, data["detection"]):
                             app_info = {
                                 "name": display_name,
                                 "version": version,
                                 "publisher": publisher,
                                 "type": data["type"],
                                 "method": "WMI",
                                 "uninstall_string": f"msiexec.exe /x {product_code} /qn" if product_code else None,
                                 "install_location": install_location,
                                 "product_code": product_code,
                                 "registry_path": None, # WMI no lo da directamente
                                 "is_uwp": False,
                                 "detection_term": target_name,
                                 "vendor_for_cleanup": publisher,
                             }
                             if self._add_detected_app(app_info, checked_display_names):
                                  detected_count += 1
                             break
        except ImportError:
            logging.error("Módulo WMI no encontrado. Omitiendo detección por WMI.")
        except Exception as wmi_err:
            logging.error(f"Error durante la detección por WMI: {wmi_err}")
        logging.info(f"Detección por WMI finalizada. {detected_count} nuevos elementos encontrados.")

    def detect_via_startmenu(self, checked_display_names):
        """ Búsqueda de carpetas en Menú Inicio """
        logging.info("Iniciando detección por Menú Inicio...")
        detected_count = 0
        start_menu_folders = [
            Path(os.environ.get('ProgramData', 'C:\\ProgramData')) / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs',
            Path.home() / 'AppData' / 'Roaming' / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs'
        ]

        for menu_dir in start_menu_folders:
            if not menu_dir.exists():
                continue
            logging.debug(f"Escaneando Menú Inicio: {menu_dir}")
            try:
                # Iterar sobre carpetas y archivos .lnk directamente en el directorio
                for item in menu_dir.iterdir():
                    item_name = item.stem # Usar stem para quitar extensión .lnk si existe
                    # Heurística simple: buscar carpetas/accesos cuyo nombre coincida
                    for target_name, data in TARGET_SOFTWARE.items():
                        if any(term.lower() in item_name.lower() for term in data["detection"]):
                            # Crear una entrada heurística si no existe ya una más fiable
                            app_info = {
                                "name": item_name, # Nombre de la carpeta/acceso
                                "version": "N/A",
                                "publisher": "Desconocido (Menú Inicio)",
                                "type": data["type"] + " (Menú Inicio)",
                                "method": "Menú Inicio",
                                "install_location": None, # No se sabe desde aquí
                                "is_uwp": False,
                                "is_startmenu_heuristic": True,
                                "detection_term": target_name,
                                "vendor_for_cleanup": None, # Difícil saber
                            }
                            if self._add_detected_app(app_info, checked_display_names):
                                detected_count += 1
                            break # Pasar al siguiente item del menú
            except PermissionError:
                logging.warning(f"Permiso denegado al escanear Menú Inicio: {menu_dir}")
            except Exception as sm_err:
                logging.error(f"Error escaneando Menú Inicio {menu_dir}: {sm_err}")
        logging.info(f"Detección por Menú Inicio finalizada. {detected_count} nuevos elementos encontrados.")


    def detect_software(self):
        """ Realiza la detección multifacética """
        logging.info("Iniciando detección de software no deseado...")
        self.progress.emit(0, "Iniciando detección...")
        self.detected_software = []
        checked_display_names = set()

        self.progress.emit(5, "Buscando en el registro...")
        self.detect_via_registry(checked_display_names)

        self.progress.emit(25, "Buscando aplicaciones UWP (PowerShell)...")
        self.detect_via_uwp_powershell(checked_display_names)

        self.progress.emit(50, "Buscando en sistema de archivos...")
        self.detect_via_filesystem(checked_display_names)

        self.progress.emit(70, "Buscando vía WMI (puede tardar)...")
        self.detect_via_wmi(checked_display_names)

        self.progress.emit(85, "Buscando en Menú Inicio...")
        self.detect_via_startmenu(checked_display_names)

        self.progress.emit(100, "Detección completada.")
        logging.info(f"Detección finalizada. Encontrados {len(self.detected_software)} elementos únicos.")


    def run_command(self, command_list, step_name, app_name, timeout=300, check_return_code=True):
        """ Ejecuta un comando usando subprocess y registra el resultado """
        logging.info(f"[{app_name}] Ejecutando {step_name}: {' '.join(command_list)}")
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE

            result = subprocess.run(command_list,
                                    capture_output=True,
                                    text=True,
                                    check=False,
                                    timeout=timeout,
                                    encoding='utf-8', errors='ignore',
                                    startupinfo=startupinfo)

            log_func = logging.info if result.returncode == 0 else logging.warning
            log_func(f"[{app_name}] Resultado {step_name} (Código: {result.returncode}):")
            if result.stdout:
                log_func(f"  stdout: {result.stdout.strip()}")
            if result.stderr:
                logging.warning(f"  stderr: {result.stderr.strip()}")

            return result.returncode == 0 if check_return_code else True # Éxito si 0 o si no se chequea
        except subprocess.TimeoutExpired:
            logging.error(f"[{app_name}] Timeout ({timeout}s) durante {step_name}.")
            return False
        except FileNotFoundError:
            logging.error(f"[{app_name}] Error: Comando no encontrado para {step_name}: {command_list[0]}")
            return False
        except PermissionError:
             logging.error(f"[{app_name}] Error de permisos ejecutando {step_name}.")
             return False
        except Exception as e:
            logging.error(f"[{app_name}] Error inesperado ejecutando {step_name}: {e}")
            return False

    def terminate_process(self, app_name, install_location):
        """ Intenta terminar procesos asociados a la aplicación """
        logging.info(f"[{app_name}] Método 4: Intentando terminar procesos...")
        terminated_count = 0
        process_name_heuristic = Path(install_location).stem.lower() if install_location and Path(install_location).exists() and Path(install_location).is_file() else app_name.lower()
        install_dir_lower = install_location.lower() if install_location else None

        try:
            for proc in psutil.process_iter(['pid', 'name', 'exe', 'status']):
                try:
                    proc_info = proc.info
                    proc_name = proc_info['name'].lower() if proc_info['name'] else ''
                    proc_exe = proc_info['exe'].lower() if proc_info['exe'] else ''

                    match = False
                    if install_dir_lower and proc_exe.startswith(install_dir_lower):
                         match = True
                    elif proc_name == process_name_heuristic + ".exe":
                         match = True
                    elif app_name.lower() in proc_name: # Coincidencia parcial en nombre proceso
                         match = True
                    elif app_name.lower() in proc_exe: # Coincidencia parcial en ruta ejecutable
                        match = True


                    if match and proc_info['status'] == psutil.STATUS_RUNNING:
                        logging.info(f"[{app_name}] Encontrado proceso coincidente: PID={proc_info['pid']}, Name={proc_info['name']}, Exe={proc_info['exe']}")
                        try:
                            p = psutil.Process(proc_info['pid'])
                            logging.info(f"[{app_name}] Intentando terminar (terminate) PID {p.pid}...")
                            p.terminate()
                            try:
                                p.wait(timeout=2)
                                logging.info(f"[{app_name}] Proceso {p.pid} terminado.")
                                terminated_count += 1
                            except psutil.TimeoutExpired:
                                logging.warning(f"[{app_name}] El proceso {p.pid} no terminó con terminate. Intentando kill...")
                                try:
                                     p.kill()
                                     p.wait(timeout=1)
                                     logging.info(f"[{app_name}] Proceso {p.pid} terminado con kill.")
                                     terminated_count += 1
                                except Exception as kill_err:
                                     logging.error(f"[{app_name}] Fallo al forzar terminación (kill) del proceso {p.pid}: {kill_err}")
                        except psutil.NoSuchProcess:
                            logging.info(f"[{app_name}] El proceso {proc_info['pid']} ya no existe.")
                            terminated_count += 1
                        except psutil.AccessDenied:
                            logging.warning(f"[{app_name}] Acceso denegado al intentar terminar el proceso {proc_info['pid']}.")
                        except Exception as term_err:
                            logging.error(f"[{app_name}] Error inesperado al terminar el proceso {proc_info['pid']}: {term_err}")
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
                except Exception as iter_err:
                     logging.error(f"Error iterando proceso: {iter_err}")

        except Exception as e:
            logging.error(f"[{app_name}] Error durante la búsqueda/terminación de procesos: {e}")

        return terminated_count > 0

    def delete_files_folders(self, app_name, install_location, vendor_name=None, detection_term=None):
        """ Elimina archivos/carpetas de instalación y restos comunes """
        logging.info(f"[{app_name}] Método 5 y Limpieza: Eliminando archivos/carpetas...")
        deleted_something = False

        if install_location and Path(install_location).exists():
            logging.info(f"[{app_name}] Intentando eliminar directorio/archivo principal: {install_location}")
            try:
                resolved_path = Path(install_location).resolve()
                if resolved_path.is_dir():
                    shutil.rmtree(resolved_path, ignore_errors=False, onerror=handle_shutil_error)
                    logging.info(f"[{app_name}] Directorio principal eliminado (o intento iniciado): {resolved_path}")
                    deleted_something = True
                elif resolved_path.is_file():
                     resolved_path.unlink(missing_ok=True)
                     logging.info(f"[{app_name}] Archivo principal eliminado: {resolved_path}")
                     deleted_something = True
            except FileNotFoundError:
                 logging.info(f"[{app_name}] Elemento principal no encontrado (ya eliminado?): {install_location}")
            except PermissionError as pe:
                logging.warning(f"[{app_name}] Permiso denegado al eliminar elemento principal: {install_location} - {pe}")
            except OSError as e:
                logging.warning(f"[{app_name}] Error OS al eliminar elemento principal {install_location}: {e}")
            except Exception as e:
                logging.error(f"[{app_name}] Error inesperado eliminando elemento principal {install_location}: {e}")

        potential_leftovers = []
        search_terms = set(filter(None, [app_name, vendor_name, detection_term]))

        common_locations = [
            Path(os.environ.get('ProgramData', 'C:\\ProgramData')),
            Path.home() / 'AppData' / 'Local',
            Path.home() / 'AppData' / 'Roaming',
            Path(os.environ.get('TEMP', 'C:\\Windows\\Temp')),
            Path(os.environ.get('ProgramFiles', 'C:\\Program Files')),
            Path(os.environ.get('ProgramFiles(x86)', 'C:\\Program Files (x86)')),
            Path(os.environ.get('CommonProgramFiles', 'C:\\Program Files\\Common Files')),
            Path(os.environ.get('CommonProgramFiles(x86)', 'C:\\Program Files (x86)\\Common Files')),
        ]

        for loc in common_locations:
            if loc.exists():
                for term in search_terms:
                    term_lower = term.lower()
                    try:
                        for item in loc.iterdir():
                            # Evitar borrar la carpeta de instalación principal si está en estas rutas
                            resolved_item = item.resolve()
                            resolved_install_loc = Path(install_location).resolve() if install_location else None
                            if resolved_install_loc and resolved_item == resolved_install_loc:
                                continue

                            if term_lower in item.name.lower():
                                if item.is_dir() or item.is_file():
                                    potential_leftovers.append(item)
                    except PermissionError:
                        logging.warning(f"Permiso denegado al buscar restos en {loc}")
                    except Exception as scan_err:
                         logging.error(f"Error buscando restos en {loc}: {scan_err}")

        unique_leftovers = list(set(potential_leftovers))

        for leftover_path in unique_leftovers:
            logging.info(f"[{app_name}] Intentando eliminar resto potencial: {leftover_path}")
            try:
                if leftover_path.is_dir():
                    shutil.rmtree(leftover_path, ignore_errors=False, onerror=handle_shutil_error)
                    logging.info(f"[{app_name}] Resto (directorio) eliminado: {leftover_path}")
                    deleted_something = True
                elif leftover_path.is_file():
                    leftover_path.unlink(missing_ok=True)
                    logging.info(f"[{app_name}] Resto (archivo) eliminado: {leftover_path}")
                    deleted_something = True
            except PermissionError as pe:
                logging.warning(f"[{app_name}] Permiso denegado al eliminar resto: {leftover_path} - {pe}")
            except OSError as e:
                logging.warning(f"[{app_name}] Error OS al eliminar resto {leftover_path}: {e}")
            except Exception as e:
                logging.error(f"[{app_name}] Error inesperado eliminando resto {leftover_path}: {e}")

        return deleted_something


    def cleanup_registry(self, app_name, vendor_name=None, detection_term=None, registry_path=None):
        """ Elimina claves de registro residuales """
        logging.info(f"[{app_name}] Limpieza: Eliminando claves de registro residuales...")
        deleted_something = False

        # Prioridad 1: Eliminar la clave de desinstalación específica si se conoce
        if registry_path:
             try:
                 hive_str, key_part = registry_path.split('\\', 1)
                 hive_map = {
                     "HKEY_LOCAL_MACHINE": winreg.HKEY_LOCAL_MACHINE,
                     "HKEY_CURRENT_USER": winreg.HKEY_CURRENT_USER,
                     # Añadir otros si es necesario
                 }
                 root_hive = hive_map.get(hive_str)
                 if root_hive:
                      # Determinar vista (asumir 64 por defecto, intentar 32 si falla?)
                      # Mejor intentar ambas vistas si es HKLM
                      views_to_try = [winreg.KEY_WOW64_64KEY, winreg.KEY_WOW64_32KEY] if root_hive == winreg.HKEY_LOCAL_MACHINE else [0]
                      deleted_main_key = False
                      for view in views_to_try:
                           if delete_registry_key_recursive(root_hive, key_part, view):
                                deleted_main_key = True
                                deleted_something = True
                                break # Salir si se eliminó con una vista
                      if deleted_main_key:
                           logging.info(f"[{app_name}] Clave de registro de desinstalación principal eliminada: {registry_path}")
                      else:
                            logging.warning(f"[{app_name}] No se pudo eliminar la clave de registro principal: {registry_path}")

             except Exception as e:
                  logging.error(f"[{app_name}] Error al intentar eliminar clave de registro principal {registry_path}: {e}")


        search_terms = set(filter(None, [app_name, vendor_name, detection_term]))
        simplified_terms = set()
        for term in search_terms:
            # Simplificar nombres quitando sufijos comunes, versiones, etc.
            term_simplified = re.sub(r'\(.*\)|v?\d+(\.\d+)*$| Setup$| Suite$| Application$| Driver$| Utility$', '', term, flags=re.IGNORECASE).strip()
            if len(term_simplified) > 3 : # Evitar términos muy cortos
                simplified_terms.add(term_simplified)
            simplified_terms.add(term.replace(" ", "")) # Versión sin espacios

        registry_bases = [
             (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE"),
             (winreg.HKEY_CURRENT_USER, r"SOFTWARE")
             # Podríamos añadir SOFTWARE\Classes para CLSID/ProgID pero es más riesgoso
        ]
        access_views = [winreg.KEY_WOW64_64KEY, winreg.KEY_WOW64_32KEY]

        for root_hive, base_path in registry_bases:
            views_to_check = access_views if root_hive == winreg.HKEY_LOCAL_MACHINE else [0]
            for view in views_to_check:
                try:
                    with winreg.OpenKey(root_hive, base_path, 0, winreg.KEY_READ | view) as base_key:
                        i = 0
                        while True:
                            try:
                                vendor_key_name = winreg.EnumKey(base_key, i)
                                vendor_key_lower = vendor_key_name.lower()
                                vendor_full_path = f"{base_path}\\{vendor_key_name}"

                                # Comprobar si la clave de "vendor" coincide
                                vendor_match = False
                                if vendor_name and vendor_name.lower() in vendor_key_lower:
                                     vendor_match = True
                                if not vendor_match:
                                     for term in simplified_terms:
                                          if term.lower() in vendor_key_lower:
                                               vendor_match = True
                                               break

                                if vendor_match:
                                    # Decidir si borrar toda la clave del vendor o buscar subkeys
                                    delete_entire_vendor_key = False
                                    if safe_str_compare(vendor_key_name, vendor_name) or safe_str_compare(vendor_key_name, detection_term):
                                        delete_entire_vendor_key = True

                                    if delete_entire_vendor_key:
                                         logging.info(f"[{app_name}] Intentando eliminar clave de registro de vendor recursivamente: {vendor_full_path} (Vista: {view})")
                                         if delete_registry_key_recursive(root_hive, vendor_full_path, view):
                                             deleted_something = True
                                             # No incrementar 'i' aquí, ya que la clave fue eliminada
                                             continue # Pasar al siguiente índice de EnumKey

                                    else: # Buscar subkeys de producto que coincidan
                                        try:
                                            with winreg.OpenKey(root_hive, vendor_full_path, 0, winreg.KEY_READ | view) as vendor_key_handle:
                                                j = 0
                                                keys_to_delete = []
                                                while True:
                                                    try:
                                                        product_key_name = winreg.EnumKey(vendor_key_handle, j)
                                                        product_key_lower = product_key_name.lower()
                                                        product_match = False
                                                        for term in simplified_terms:
                                                             if term.lower() in product_key_lower:
                                                                  product_match = True
                                                                  break

                                                        if product_match:
                                                            product_full_path = f"{vendor_full_path}\\{product_key_name}"
                                                            keys_to_delete.append(product_full_path)
                                                        j += 1
                                                    except OSError:
                                                        break

                                                # Eliminar las subkeys marcadas
                                                for key_to_del in set(keys_to_delete):
                                                    logging.info(f"[{app_name}] Intentando eliminar clave de registro de producto recursivamente: {key_to_del} (Vista: {view})")
                                                    if delete_registry_key_recursive(root_hive, key_to_del, view):
                                                        deleted_something = True

                                        except FileNotFoundError:
                                             pass
                                        except PermissionError:
                                             logging.warning(f"Permiso denegado al acceder a subkeys de {vendor_full_path}")
                                        except Exception as subkey_err:
                                             logging.error(f"Error procesando subkeys de {vendor_full_path}: {subkey_err}")
                                i += 1 # Incrementar solo si no se borró la clave vendor entera
                            except OSError:
                                break
                except FileNotFoundError:
                     pass # Es normal si la base no existe en alguna vista
                except PermissionError:
                     logging.warning(f"Permiso denegado al acceder a base de registro: {winreg.HKEY_NAMES.get(root_hive.handle, root_hive.handle)}\\{base_path} (Vista: {view})")
                except Exception as base_err:
                    logging.error(f"Error accediendo a base de registro {winreg.HKEY_NAMES.get(root_hive.handle, root_hive.handle)}\\{base_path} (Vista: {view}): {base_err}")

        return deleted_something

    def delete_services(self, app_name, install_location, vendor_name=None, detection_term=None):
        """ Método Extremo: Intenta detener y eliminar servicios asociados """
        logging.info(f"[{app_name}] Método Extremo: Intentando eliminar servicios asociados...")
        deleted_something = False
        search_terms = set(filter(None, [app_name, vendor_name, detection_term]))
        simplified_terms = set()
        for term in search_terms:
             term_simplified = re.sub(r'\(.*\)|v?\d+(\.\d+)*$| Service$| Update$', '', term, flags=re.IGNORECASE).strip().lower()
             if len(term_simplified) > 3:
                 simplified_terms.add(term_simplified)
                 simplified_terms.add(term.replace(" ", "").lower())

        install_dir_lower = install_location.lower() if install_location else None

        try:
            services = list(psutil.win_service_iter()) # Obtener lista completa primero
            for s in services:
                 service_info = None
                 service_name = None
                 try:
                     service_info = s.as_dict()
                     service_name = service_info.get('name')
                     display_name = service_info.get('display_name', '').lower()
                     binpath = service_info.get('binpath', '').lower()
                     status = service_info.get('status')

                     # Comprobar coincidencia
                     match = False
                     # 1. Por ruta del binario
                     if install_dir_lower and binpath.startswith(install_dir_lower):
                          match = True
                     # 2. Por nombre/display name vs términos simplificados
                     if not match:
                          for term in simplified_terms:
                               if term in service_name.lower() or term in display_name:
                                    match = True
                                    break

                     if match:
                          logging.info(f"[{app_name}] Encontrado servicio coincidente: Name={service_name}, DisplayName={service_info.get('display_name')}, BinPath={service_info.get('binpath')}, Status={status}")

                          # Intentar detener el servicio si está corriendo
                          if status in ['running', 'start_pending', 'stop_pending']:
                               logging.info(f"[{app_name}] Intentando detener servicio '{service_name}'...")
                               if self.run_command(["sc", "stop", service_name], f"Stop Service {service_name}", app_name, timeout=60, check_return_code=False):
                                    logging.info(f"[{app_name}] Comando 'sc stop {service_name}' ejecutado (puede tardar en detenerse).")
                                    time.sleep(3) # Esperar un poco a que se detenga
                               else:
                                    logging.warning(f"[{app_name}] Fallo al ejecutar 'sc stop {service_name}'.")


                          # Intentar eliminar el servicio
                          logging.info(f"[{app_name}] Intentando eliminar servicio '{service_name}'...")
                          if self.run_command(["sc", "delete", service_name], f"Delete Service {service_name}", app_name, timeout=30):
                               logging.info(f"[{app_name}] Servicio '{service_name}' eliminado exitosamente.")
                               deleted_something = True
                          else:
                               logging.warning(f"[{app_name}] Fallo al eliminar servicio '{service_name}'. Podría requerir reinicio o estar bloqueado.")

                 except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                      logging.warning(f"Error accediendo a información del servicio {service_name}: {e}")
                      continue # Saltar al siguiente servicio
                 except Exception as service_err:
                      logging.error(f"Error procesando servicio {service_name}: {service_err}")
                      continue

        except Exception as e:
             logging.error(f"Error general al iterar/eliminar servicios: {e}")

        return deleted_something


    def remove_selected_software(self):
        """ Ejecuta el protocolo de eliminación para las apps seleccionadas """
        results = []
        total_apps = len(self.apps_to_remove)
        start_time = time.time()

        for i, app_info in enumerate(self.apps_to_remove):
            app_name = app_info.get("name", "Desconocido")
            install_loc = app_info.get("install_location")
            uninstall_str = app_info.get("uninstall_string")
            product_code = app_info.get("product_code")
            package_name = app_info.get("package_full_name")
            is_uwp = app_info.get("is_uwp", False)
            vendor = app_info.get("vendor_for_cleanup")
            detect_term = app_info.get("detection_term")
            registry_path = app_info.get("registry_path")

            current_progress = int(((i + 1) / total_apps) * 100)
            self.progress.emit(current_progress, f"Procesando [{i+1}/{total_apps}]: {app_name}")
            logging.info(f"--- Iniciando eliminación de: {app_name} ---")

            status = {"name": app_name, "steps": {}}
            m1_success, m2_success, m3_success, m4_success, m5_deleted_files, m6_deleted_registry, m7_deleted_services = False, False, False, False, False, False, False

            if uninstall_str:
                cmd_parts = []
                try:
                     # Intento de parseo más robusto usando shlex o regex
                     import shlex
                     cmd_parts = shlex.split(uninstall_str)
                except:
                      # Fallback a método simple si shlex falla
                      if '"' in uninstall_str:
                           parts = uninstall_str.split('"')
                           cmd_parts.append(parts[1])
                           remaining_args_str = parts[2].strip() if len(parts) > 2 else ""
                           cmd_parts.extend(remaining_args_str.split())
                      else:
                           cmd_parts = uninstall_str.split()


                remaining_args = " ".join(cmd_parts[1:]) if len(cmd_parts) > 1 else ""
                executable = cmd_parts[0].lower() if cmd_parts else ""

                silent_flags_added = False
                if "msiexec.exe" in executable:
                    if product_code and f"/i{product_code}" in remaining_args.lower():
                        remaining_args = remaining_args.lower().replace(f"/i{product_code}", f"/x{product_code}")
                    elif " /i " in remaining_args.lower():
                         remaining_args = remaining_args.lower().replace(" /i ", " /x ")

                    if "/qn" not in remaining_args.lower() and "/quiet" not in remaining_args.lower():
                         remaining_args += " /qn"
                         silent_flags_added = True
                elif "/silent" not in remaining_args.lower() and "/verysilent" not in remaining_args.lower() and "/s" not in remaining_args.lower():
                     common_flags = [" /S", " /silent", " /verysilent", " -ms", " --silent"]
                     # Intentar añadir un flag común si no hay ninguno
                     # TODO: Podríamos tener una base de datos de flags por instalador
                     remaining_args += " /S" # Añadir el más común por defecto
                     silent_flags_added = True

                final_command = [cmd_parts[0]] + remaining_args.split()
                final_command = [part for part in final_command if part]

                if final_command:
                    if silent_flags_added:
                        logging.info(f"[{app_name}] Añadiendo flags silenciosos heurísticos al comando.")
                    m1_success = self.run_command(final_command, "Método 1 (UninstallString)", app_name)
                    status["steps"]["M1_UninstallString"] = "Éxito" if m1_success else "Fallo/No aplicable"
                else:
                     status["steps"]["M1_UninstallString"] = "Fallo (comando vacío)"
            else:
                status["steps"]["M1_UninstallString"] = "No aplicable (sin UninstallString)"
                logging.info(f"[{app_name}] Método 1 omitido: No hay UninstallString.")

            if product_code: # Intentar siempre MSIEXEC si hay código de producto
                 command = ["msiexec.exe", "/x", product_code, "/qn", "/norestart"]
                 m2_success = self.run_command(command, "Método 2 (MSIEXEC)", app_name)
                 status["steps"]["M2_MSIEXEC"] = "Éxito" if m2_success else "Fallo/No aplicable"
                 # Si M1 tuvo éxito, el fallo de M2 es esperado (ya desinstalado)
                 if m1_success and not m2_success:
                      status["steps"]["M2_MSIEXEC"] = "No aplicable (probablemente ya desinstalado por M1)"

            else:
                 status["steps"]["M2_MSIEXEC"] = "No aplicable (sin ProductCode)"


            if is_uwp and package_name:
                ps_command_all = f'try {{ Get-AppxPackage -Name "{package_name}" -AllUsers | Remove-AppxPackage -AllUsers -ErrorAction Stop }} catch {{ exit 1 }}'
                if not self.run_command(["powershell", "-Command", ps_command_all], "Método 3 (Remove-AppxPackage AllUsers)", app_name):
                     ps_command_user = f'try {{ Get-AppxPackage -Name "{package_name}" | Remove-AppxPackage -ErrorAction Stop }} catch {{ exit 1 }}'
                     m3_success = self.run_command(["powershell", "-Command", ps_command_user], "Método 3 (Remove-AppxPackage User)", app_name)
                else:
                     m3_success = True
                status["steps"]["M3_RemoveAppx"] = "Éxito" if m3_success else "Fallo/No aplicable"
            else:
                status["steps"]["M3_RemoveAppx"] = "No aplicable (no UWP)"


            # Ejecutar terminación de procesos antes de borrar archivos
            m4_success = self.terminate_process(app_name, install_loc)
            status["steps"]["M4_TerminateProc"] = "Éxito (procesos terminados/no encontrados)" if m4_success else "Fallo/No se terminaron procesos"

            # Ejecutar borrado de archivos/carpetas
            m5_deleted_files = self.delete_files_folders(app_name, install_loc, vendor, detect_term)
            status["steps"]["M5_DeleteFiles"] = "Éxito (archivos/carpetas eliminados)" if m5_deleted_files else "No se eliminaron archivos/carpetas"

            # Ejecutar limpieza de registro
            m6_deleted_registry = self.cleanup_registry(app_name, vendor, detect_term, registry_path)
            status["steps"]["M6_RegistryClean"] = "Éxito (claves eliminadas)" if m6_deleted_registry else "No se eliminaron claves de registro"

            # Método Extremo: Eliminar servicios
            m7_deleted_services = self.delete_services(app_name, install_loc, vendor, detect_term)
            status["steps"]["M7_DeleteServices"] = "Éxito (servicios eliminados)" if m7_deleted_services else "No se eliminaron servicios"


            if m1_success or m2_success or m3_success or (m5_deleted_files or m6_deleted_registry or m7_deleted_services):
                 # Considerar éxito si algún método de desinstalación funcionó
                 # O si alguna de las limpiezas agresivas (archivos, registro, servicios) hizo algo.
                 status["final_status"] = "Eliminación/Limpieza Completada (parcial o total)"
                 # Podríamos refinar el estado final basado en qué métodos funcionaron
                 if (m1_success or m2_success or m3_success):
                     status["final_status"] += " - Desinstalador estándar/UWP exitoso."
                 elif (m5_deleted_files or m6_deleted_registry or m7_deleted_services):
                     status["final_status"] += " - Solo limpieza agresiva realizada."

            else:
                 status["final_status"] = "Fallo en todos los métodos intentados"

            logging.info(f"--- Finalizada eliminación de: {app_name} --- Status: {status['final_status']} ---")
            results.append(status)

        end_time = time.time()
        logging.info(f"Proceso de eliminación completado en {end_time - start_time:.2f} segundos.")
        self.progress.emit(100, "Proceso de eliminación completado.")
        return results


class UninstallerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.detected_software = []
        self.worker = None
        self.progress_dialog = None
        self.progress_dialog_remove = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Desinstalador Agresivo de Software')
        
        # --- LÍNEA QUE DEBES AGREGAR ---
        self.setWindowIcon(QIcon('1.ico'))
        # -------------------------------

        self.setGeometry(200, 200, 800, 600)

        layout = QVBoxLayout()

        self.info_label = QLabel("Bienvenido. Haz clic en 'Detectar Software' para comenzar.")
        layout.addWidget(self.info_label)

        self.select_all_checkbox = QCheckBox("Seleccionar/Deseleccionar Todo")
        self.select_all_checkbox.stateChanged.connect(self.toggle_select_all)
        self.select_all_checkbox.setEnabled(False)
        layout.addWidget(self.select_all_checkbox)


        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.detect_button = QPushButton('Detectar Software No Deseado')
        self.detect_button.clicked.connect(self.start_detection)
        layout.addWidget(self.detect_button)

        self.remove_button = QPushButton('Eliminar Software Seleccionado')
        self.remove_button.clicked.connect(self.confirm_and_start_removal)
        self.remove_button.setEnabled(False)
        layout.addWidget(self.remove_button)

        self.setLayout(layout)

    def start_detection(self):
        self.info_label.setText("Detectando software... por favor espera.")
        self.detect_button.setEnabled(False)
        self.remove_button.setEnabled(False)
        self.select_all_checkbox.setEnabled(False)
        self.list_widget.clear()

        if not self.progress_dialog:
             self.progress_dialog = QProgressDialog("Detectando software...", "Cancelar", 0, 100, self)
             self.progress_dialog.setWindowModality(Qt.NonModal)
             self.progress_dialog.setAutoClose(True)
        self.progress_dialog.setValue(0)
        self.progress_dialog.setLabelText("Detectando software...")
        self.progress_dialog.show()


        self.worker = Worker(mode='detect')
        self.worker.progress.connect(self.update_progress)
        self.worker.detection_complete.connect(self.on_detection_complete)
        self.worker.start()

    def update_progress(self, value, message):
         if self.progress_dialog and self.progress_dialog.isVisible():
            self.progress_dialog.setValue(value)
            self.progress_dialog.setLabelText(message)
            QApplication.processEvents()

    def on_detection_complete(self, detected_list):
        self.detected_software = detected_list
        self.detect_button.setEnabled(True)

        if self.progress_dialog:
             self.progress_dialog.close()

        if not self.detected_software:
            self.info_label.setText("No se detectó software conocido no deseado.")
            QMessageBox.information(self, "Detección Completa", "No se encontró software de la lista.")
            self.remove_button.setEnabled(False)
            self.select_all_checkbox.setEnabled(False)
            return

        self.info_label.setText(f"Se detectaron {len(self.detected_software)} elementos. Selecciona cuáles deseas eliminar:")
        self.list_widget.clear()
        self.select_all_checkbox.setEnabled(True)
        self.select_all_checkbox.setChecked(True)

        # Ordenar la lista alfabéticamente por nombre para mejor visualización
        sorted_list = sorted(self.detected_software, key=lambda x: x.get('name', '').lower())

        for app in sorted_list:
            item_text = f"{app.get('name', 'N/A')} ({app.get('type', 'N/A')})"
            if app.get('version'):
                item_text += f" - v{app.get('version')}"
            if app.get('publisher'):
                 item_text += f" ({app.get('publisher')})"
            if app.get('is_portable_heuristic') or app.get('is_startmenu_heuristic'):
                item_text += f" [Detectado por {app.get('method')}]"

            list_item = QListWidgetItem(item_text)
            list_item.setData(Qt.UserRole, app)
            list_item.setFlags(list_item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            list_item.setCheckState(Qt.Checked)
            self.list_widget.addItem(list_item)

        self.remove_button.setEnabled(True)


    def toggle_select_all(self, state):
         check_state = Qt.Checked if state == Qt.Checked else Qt.Unchecked
         for i in range(self.list_widget.count()):
             item = self.list_widget.item(i)
             item.setCheckState(check_state)


    def confirm_and_start_removal(self):
        selected_items = []
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.checkState() == Qt.Checked:
                selected_items.append(item.data(Qt.UserRole))

        if not selected_items:
            QMessageBox.warning(self, "Nada Seleccionado", "Por favor, selecciona al menos una aplicación para eliminar.")
            return

        confirm_dialog = QDialog(self)
        confirm_dialog.setWindowTitle("Confirmar Eliminación Agresiva")
        dialog_layout = QVBoxLayout()

        label = QLabel(f"<b>¡Atención!</b> Estás a punto de intentar eliminar agresivamente <b>{len(selected_items)}</b> elementos seleccionados.")
        label.setWordWrap(True)
        dialog_layout.addWidget(label)

        details_label = QLabel("Esto incluye métodos forzados (terminar procesos, borrar archivos/registro/servicios) que podrían ser irreversibles y, aunque se intenta ser preciso, existe un riesgo inherente si la detección fue incorrecta o si el software es necesario para otro programa. Se recomienda encarecidamente cerrar otras aplicaciones y tener copias de seguridad recientes.")
        details_label.setStyleSheet("QLabel { color : red; }")
        details_label.setWordWrap(True)
        dialog_layout.addWidget(details_label)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.button(QDialogButtonBox.Ok).setText("Sí, Proceder con Eliminación")
        buttons.button(QDialogButtonBox.Cancel).setText("Cancelar")
        buttons.accepted.connect(confirm_dialog.accept)
        buttons.rejected.connect(confirm_dialog.reject)
        dialog_layout.addWidget(buttons)

        confirm_dialog.setLayout(dialog_layout)

        if confirm_dialog.exec():
             self.start_removal(selected_items)
        else:
             logging.info("Eliminación cancelada por el usuario.")


    def start_removal(self, apps_to_remove):
         self.info_label.setText("Eliminando software seleccionado... por favor espera.")
         self.detect_button.setEnabled(False)
         self.remove_button.setEnabled(False)
         self.select_all_checkbox.setEnabled(False)

         if not self.progress_dialog_remove:
             self.progress_dialog_remove = QProgressDialog("Eliminando software...", "Cancelar (No recomendado)", 0, 100, self)
             self.progress_dialog_remove.setWindowModality(Qt.WindowModal)
             self.progress_dialog_remove.setAutoClose(False)
             self.progress_dialog_remove.setAutoReset(False)
         self.progress_dialog_remove.setValue(0)
         self.progress_dialog_remove.setLabelText("Iniciando eliminación...")
         self.progress_dialog_remove.show()

         self.worker = Worker(mode='remove', apps_to_remove=apps_to_remove)
         self.worker.progress.connect(self.update_removal_progress)
         self.worker.finished.connect(self.on_removal_complete)
         self.worker.start()

    def update_removal_progress(self, value, message):
         if self.progress_dialog_remove and self.progress_dialog_remove.isVisible():
             self.progress_dialog_remove.setValue(value)
             self.progress_dialog_remove.setLabelText(message)
             QApplication.processEvents()


    def on_removal_complete(self, results):
        if self.progress_dialog_remove:
             self.progress_dialog_remove.close()

        self.info_label.setText("Proceso de eliminación completado. Revisa los resultados. Se recomienda reiniciar el sistema.")
        self.detect_button.setEnabled(True)
        self.remove_button.setEnabled(False) # Deshabilitar hasta nueva detección
        self.select_all_checkbox.setEnabled(False)


        result_dialog = QDialog(self)
        result_dialog.setWindowTitle("Resultados de la Eliminación")
        result_dialog.setMinimumWidth(600)
        dialog_layout = QVBoxLayout()

        result_text = "Resultados del proceso de eliminación:\n\n"
        successful_removals = 0
        failed_removals = 0
        for result in results:
            result_text += f"- {result['name']}: {result['final_status']}\n"
            # Opcional: Añadir desglose más detallado si es necesario
            # result_text += f"  Pasos: {result['steps']}\n"
            result_text += "\n"
            if "Fallo" not in result['final_status']:
                successful_removals += 1
            else:
                failed_removals += 1

        summary = f"Resumen: {successful_removals} eliminados/limpiados (total o parcialmente), {failed_removals} fallidos.\n\n"

        result_label = QLabel(summary + result_text)
        result_label.setWordWrap(True)
        dialog_layout.addWidget(result_label)

        log_info_label = QLabel(f"Se ha guardado un registro detallado en:\n{log_file}\n\n<b>Se recomienda reiniciar el sistema para completar la limpieza.</b>")
        log_info_label.setWordWrap(True)
        dialog_layout.addWidget(log_info_label)


        buttons = QDialogButtonBox(QDialogButtonBox.Ok)
        buttons.accepted.connect(result_dialog.accept)
        dialog_layout.addWidget(buttons)
        result_dialog.setLayout(dialog_layout)
        result_dialog.exec()

        # Limpiar la lista de la GUI después de mostrar resultados
        self.list_widget.clear()
        self.detected_software = []



if __name__ == '__main__':
    if not is_admin():
        if request_admin_privileges():
            logging.info("Elevación solicitada. Saliendo del proceso no elevado.")
            sys.exit(0)
        else:
            logging.error("No se obtuvieron privilegios de administrador. Saliendo.")
            print("ERROR: Se requieren privilegios de administrador para ejecutar esta aplicación.")
            try: # Intentar mostrar mensaje gráfico si Qt ya estaba importado
                 app_temp = QApplication.instance() or QApplication(sys.argv)
                 QMessageBox.critical(None, "Error de Permisos", "Se requieren privilegios de administrador para ejecutar esta aplicación.")
            except:
                 input("Presiona Enter para salir.") # Fallback a consola
            sys.exit(1)

    logging.info("Ejecutando con privilegios de administrador.")

    app = QApplication(sys.argv)
    ex = UninstallerApp()
    ex.show()
    sys.exit(app.exec())
