# -*- coding: utf-8 -*-

TRANSLATIONS = {
    "es": {
        "app_title": "TANKEKIT - Eliminador Agresivo de Bloatware",
        "welcome_msg": "Bienvenido. Haz clic en 'Detectar Software' para comenzar.",
        "detect_button": "Detectar Software No Deseado",
        "remove_button": "Eliminar Software Seleccionado",
        "select_all": "Seleccionar/Deseleccionar Todo",
        "working": "Trabajando...",
        "detecting": "Detectando software... por favor espera.",
        "removing": "Eliminando software seleccionado... por favor espera.",
        "detection_complete": "Detección Completa",
        "no_software_found": "No se detectó software conocido no deseado.",
        "no_software_in_list": "No se encontró software de la lista.",
        "items_detected": "Se detectaron {count} elementos. Selecciona cuáles deseas eliminar:",
        "nothing_selected": "Nada Seleccionado",
        "select_at_least_one": "Por favor, selecciona al menos una aplicación para eliminar.",
        "confirm_removal_title": "Confirmar Eliminación Agresiva",
        "confirm_removal_text": "<b>¡Atención!</b> Estás a punto de intentar eliminar agresivamente <b>{count}</b> elementos seleccionados.",
        "confirm_removal_details": "Esto incluye métodos forzados (terminar procesos, borrar archivos/registro/servicios) que podrían ser irreversibles y, aunque se intenta ser preciso, existe un riesgo inherente si la detección fue incorrecta o si el software es necesario para otro programa. Se recomienda encarecidamente cerrar otras aplicaciones y tener copias de seguridad recientes.",
        "proceed_button": "Sí, Proceder con Eliminación",
        "cancel_button": "Cancelar",
        "removal_complete": "Proceso de eliminación completado. Revisa los resultados. Se recomienda reiniciar el sistema.",
        "results_title": "Resultados de la Eliminación",
        "summary": "Resumen: {successful} eliminados/limpiados (total o parcialmente), {failed} fallidos.",
        "log_saved": "Se ha guardado un registro detallado en:\n{path}\n\n<b>Se recomienda reiniciar el sistema para completar la limpieza.</b>",
        "ok_button": "Aceptar",
        "permission_error": "Error de Permisos",
        "admin_required": "Se requieren privilegios de administrador para ejecutar esta aplicación.",
        "language": "Idioma",
        "theme": "Tema",
        "spanish": "Español",
        "english": "English"
    },
    "en": {
        "app_title": "TANKEKIT - Aggressive Bloatware Remover",
        "welcome_msg": "Welcome. Click 'Detect Software' to begin.",
        "detect_button": "Detect Unwanted Software",
        "remove_button": "Remove Selected Software",
        "select_all": "Select/Deselect All",
        "working": "Working...",
        "detecting": "Detecting software... please wait.",
        "removing": "Removing selected software... please wait.",
        "detection_complete": "Detection Complete",
        "no_software_found": "No known unwanted software detected.",
        "no_software_in_list": "No software from the list was found.",
        "items_detected": "{count} items detected. Select which ones you want to remove:",
        "nothing_selected": "Nothing Selected",
        "select_at_least_one": "Please select at least one application to remove.",
        "confirm_removal_title": "Confirm Aggressive Removal",
        "confirm_removal_text": "<b>Warning!</b> You are about to aggressively remove <b>{count}</b> selected items.",
        "confirm_removal_details": "This includes forced methods (terminating processes, deleting files/registry/services) that could be irreversible, and although we try to be precise, there is an inherent risk if the detection was incorrect or if the software is needed by another program. It is strongly recommended to close other applications and have recent backups.",
        "proceed_button": "Yes, Proceed with Removal",
        "cancel_button": "Cancel",
        "removal_complete": "Removal process completed. Review the results. System restart is recommended.",
        "results_title": "Removal Results",
        "summary": "Summary: {successful} removed/cleaned (total or partial), {failed} failed.",
        "log_saved": "A detailed log has been saved to:\n{path}\n\n<b>System restart is recommended to complete cleanup.</b>",
        "ok_button": "OK",
        "permission_error": "Permission Error",
        "admin_required": "Administrator privileges are required to run this application.",
        "language": "Language",
        "theme": "Theme",
        "spanish": "Español",
        "english": "English"
    }
}

class I18n:
    def __init__(self, language="es"):
        self.language = language
    
    def set_language(self, language):
        if language in TRANSLATIONS:
            self.language = language
    
    def get(self, key, default=None, **kwargs):
        text = TRANSLATIONS.get(self.language, TRANSLATIONS["es"]).get(key, default or key)
        if kwargs:
            try:
                text = text.format(**kwargs)
            except KeyError:
                pass  # If format kwargs don't match, return text as-is
        return text

i18n = I18n("es")
