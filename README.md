# TANKEKIT - Aggressive Bloatware Removal Tool

Una herramienta potente y agresiva para eliminar software no deseado, bloatware, adware, y programas potencialmente peligrosos de sistemas Windows.

## ⚠️ ADVERTENCIA IMPORTANTE

**ESTA HERRAMIENTA ES EXTREMADAMENTE AGRESIVA Y REALIZA ELIMINACIONES IRREVERSIBLES**

- Siempre crea un punto de restauración del sistema antes de usar
- Revisa cuidadosamente qué software se eliminará
- Cierra todas las aplicaciones antes de ejecutar
- Ejecuta bajo tu propio riesgo
- Recomendado solo para usuarios avanzados

## 🆕 Novedades en Esta Versión

### Refactorización Completa V2.0
- ✅ **Código optimizado a 2 archivos**: `bloatware_database.py` (datos) y `bloatware_remover.py` (GUI + lógica)
- ✅ **Base de datos DUPLICADA**: 41 → 112 → 226 entradas (+450% más software detectado)
- ✅ **Métodos de eliminación mejorados**: 7 → 9 métodos diferentes
- ✅ **Sistema de verificación**: Comprobación completa post-eliminación
- ✅ **Diálogos de progreso mejorados**: Título personalizado "TANKEKIT", animación de rueda giratoria, texto "Trabajando"
- ✅ **Análisis de código**: 10 métodos de análisis aplicados y errores corregidos
- ✅ **Seguridad mejorada**: Vulnerabilidades corregidas, validación de entrada

### Base de Datos DUPLICADA (226 Entradas)

Cada entrada incluye:
- **Nombre del software**
- **Tipo** (Bloatware, Adware, Spyware, PUP, etc.)
- **Patrones de detección** (nombres, publicadores, paquetes)
- **Razón detallada** explicando por qué es problemático

#### Categorías Incluidas (226 entradas totales):
- **Bloatware de Windows**: Apps preinstaladas innecesarias (3D Viewer, Paint 3D, etc.)
- **Juegos y Adware**: Candy Crush, Farm Heroes, Roblox, Disney Magic Kingdoms, etc.
- **Redes Sociales**: TikTok, Facebook, Instagram, Twitter, etc.
- **Streaming**: Netflix, Prime Video, Spotify, etc.
- **Antivirus Agresivo**: McAfee, Norton, Avast, AVG, Avira, Bitdefender, etc.
- **Antivirus Falso/Rogue**: Segurazo, SpyHunter, Windows Malware Defender, Antimalware Doctor, etc.
- **Optimizadores Falsos**: CCleaner, Advanced SystemCare, PC Speed Up, MyCleanPC, iolo, etc.
- **Limpiadores de Registro**: RegClean Pro, WinThruster, Wise Registry Cleaner, etc.
- **Actualizadores de Drivers**: Driver Booster, DriverPack Solution, Driver Easy, SlimDrivers, etc.
- **Toolbars y Hijackers**: Ask Toolbar, MyWay, Conduit, Babylon, Search Baron, Trovi, etc.
- **Adware de Compras**: SaveSense, PriceMeter, Shopper Pro, CouponBar, etc.
- **Software Chino**: 360 Total Security, Baidu Antivirus, Tencent PC Manager, etc.
- **OEM Bloatware**: HP, Dell, Lenovo, ASUS, Acer, MSI, Samsung, Toshiba, Sony, Fujitsu, etc.
- **Bundleware**: OpenCandy, Installcore, Amonetize, DVDVideoSoft, etc.
- **Servicios de Terceros**: Bonjour, Adobe Update, Google Update, Java Auto Updater, etc.
- **Software Peligroso**: KMSPico, Hola VPN, Chromium Malware, RelevantKnowledge, etc.

## 🚀 Características

### Detección Multifacética (5 Métodos)
1. **Registro de Windows** - Claves de desinstalación
2. **Aplicaciones UWP** - PowerShell Get-AppxPackage
3. **WMI** - Win32_Product
4. **Sistema de archivos** - Búsqueda heurística
5. **Menú Inicio** - Accesos directos

### Métodos de Eliminación (9 Métodos)
1. **UninstallString** - Cadena de desinstalación del registro
2. **MSIEXEC** - Desinstalador MSI con ProductCode
3. **Remove-AppxPackage** - Eliminación de apps UWP
4. **Terminación de procesos** - Kill de procesos en ejecución
5. **Eliminación de archivos/carpetas** - Borrado recursivo
6. **Limpieza de registro** - Eliminación de claves residuales
7. **Eliminación de servicios** - Stop y delete de servicios
8. **🆕 Force Delete con Takeown** - Toma de propiedad + permisos forzados
9. **🆕 Eliminación en arranque** - Script batch para próximo reinicio

### Sistema de Verificación (5 Puntos)
- ✓ Registro limpio
- ✓ Archivos eliminados
- ✓ Procesos terminados
- ✓ Servicios eliminados
- ✓ Paquetes UWP desinstalados

Si la verificación falla, se aplican métodos adicionales automáticamente.

## 📋 Requisitos

- **Sistema Operativo**: Windows 10/11 (64-bit recomendado)
- **Python**: 3.7 o superior
- **Privilegios**: Administrador (solicitados automáticamente)
- **Dependencias** (se instalan automáticamente):
  - `psutil` - Gestión de procesos
  - `wmi` - Acceso a WMI de Windows
  - `PySide6` - Interfaz gráfica Qt

## 🔧 Instalación

### Opción 1: Clonar Repositorio
```bash
git clone https://github.com/moltenisoy/TANKEKIT.git
cd TANKEKIT
python bloatware_remover.py
```

### Opción 2: Descarga Directa
1. Descarga `bloatware_database.py`
2. Descarga `bloatware_remover.py`
3. Coloca ambos archivos en la misma carpeta
4. Ejecuta `python bloatware_remover.py`

## 💻 Uso

### Ejecución
```bash
python bloatware_remover.py
```

La aplicación solicitará automáticamente privilegios de administrador.

### Interfaz Gráfica
1. **Click "Detectar Software No Deseado"**: Escanea el sistema
2. **Revisa la lista**: Examina el software detectado
3. **Selecciona items**: Marca los que deseas eliminar
4. **Click "Eliminar Software Seleccionado"**: Confirma y elimina
5. **Espera**: El proceso puede tardar varios minutos
6. **Revisa resultados**: Lee el resumen y log detallado
7. **Reinicia**: Recomendado para completar la eliminación

### Logs
Los logs detallados se guardan en:
```
%TEMP%\aggressive_uninstaller_log.txt
```

## 📊 Ejemplos de Software Detectado

### Bloatware Típico
- **Candy Crush Saga**: "Mobile game con monetización agresiva y ads"
- **OneDrive**: "Cloud storage forzado. Debería ser opcional"
- **McAfee**: "Trial AV con popups agresivos. Considerado bloatware por expertos"

### Software Peligroso
- **Segurazo**: "FAKE antivirus. Muestra falsos positivos. Clasificado como malware"
- **DriverPack Solution**: "Conocido por incluir malware. Instala software no deseado"
- **KMSPico**: "Herramienta ILEGAL. Frecuentemente contiene troyanos"

## 🏗️ Arquitectura del Proyecto

```
TANKEKIT/
├── bloatware_database.py     # Base de datos (112 entradas)
│   ├── TARGET_SOFTWARE dict
│   ├── get_software_info()
│   ├── get_software_count()
│   └── get_software_by_type()
│
├── bloatware_remover.py       # Aplicación principal
│   ├── Worker class (detección/eliminación)
│   ├── UninstallerApp class (GUI)
│   ├── 9 métodos de eliminación
│   └── Sistema de verificación
│
├── 2eliminabloatware2.py      # Original (referencia)
├── CAMBIOS.md                 # Documentación detallada de cambios
├── README.md                  # Este archivo
└── .gitignore                 # Archivos ignorados
```

## 🛡️ Seguridad

### Análisis de Código Realizado
- ✅ **Pylint**: Análisis estático
- ✅ **Flake8**: Estilo PEP8
- ✅ **Bandit**: Seguridad
- ✅ **CodeQL**: Vulnerabilidades (0 encontradas)
- ✅ **Revisión manual**: Lógica y patrones

### Mitigaciones Implementadas
- ✓ Sanitización de entrada para prevenir command injection
- ✓ Validación de rutas de archivo
- ✓ Manejo seguro de privilegios
- ✓ Logging detallado para auditoría
- ✓ Confirmación explícita antes de eliminación

## 📈 Estadísticas

| Métrica | Valor Original | Valor Actual | Mejora |
|---------|----------------|--------------|--------|
| Entradas en BD | 41 | 226 | +451% |
| Métodos eliminación | 7 | 9 | +28% |
| Métodos detección | 4 | 5 | +25% |
| Verificación | No | Sí (5 puntos) | ∞ |
| Archivos | 3 | 2 (optimizado) | -33% |
| Líneas de código | ~1375 | ~2300 | +67% |
| Descripciones detalladas | No | Sí (todas 226) | ∞ |
| Diálogo de progreso | Estándar | Personalizado con animación | ∞ |

## 🐛 Problemas Conocidos

- **Armoury Crate (ASUS)**: Extremadamente difícil de eliminar, se reinstala
- **OneDrive**: Puede requerir reinicio para eliminación completa
- **Microsoft Teams**: Puede reinstalarse con actualizaciones de Windows
- **OEM Software**: Fabricantes pueden reinstalar con actualizaciones de BIOS/drivers

## 🤝 Contribuir

Las contribuciones son bienvenidas, especialmente:
- Nuevas entradas para la base de datos
- Mejoras en los métodos de detección
- Correcciones de bugs
- Traducciones

## 📝 Licencia

Este proyecto es de código abierto. Ver [LICENSE](LICENSE) para más detalles.

## ⚖️ Disclaimer

Este software se proporciona "tal cual" sin garantías de ningún tipo. Los autores no son responsables por:
- Pérdida de datos
- Daños al sistema
- Eliminación accidental de software necesario
- Problemas de estabilidad del sistema
- Cualquier otro daño directo o indirecto

**SIEMPRE** haz una copia de seguridad completa antes de usar esta herramienta.

## 📞 Soporte

- **Issues**: [GitHub Issues](https://github.com/moltenisoy/TANKEKIT/issues)
- **Documentación**: Ver `CAMBIOS.md` para detalles técnicos

## 🙏 Agradecimientos

- Comunidad de código abierto
- Testers y reportadores de bugs
- Contribuidores de la base de datos

---

**Desarrollado con ❤️ para limpiar Windows de bloatware**

**Versión**: 2.1 (Base de Datos Duplicada + UI Mejorada)  
**Última actualización**: Enero 2025
