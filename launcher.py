# -*- coding: utf-8 -*-
import subprocess
import sys

print("""
╔═══════════════════════════════════════════════════════════════╗
║                   TANKEKIT V3.0 - LAUNCHER                    ║
║              5 Temas Profesionales Disponibles                ║
╚═══════════════════════════════════════════════════════════════╝

Elige tu tema favorito / Choose your favorite theme:

1. 🟨 CYBERPUNK 2077    - Futurista neón amarillo/magenta
2. 🔵 PS5               - Minimalista blanco/azul limpio  
3. 🟢 XBOX 360          - Verde clásico gaming
4. 💜 GTA 6             - Vice City neon multi-color
5. 💚 MATRIX            - Terminal hacker verde
6. ⚪ ORIGINAL          - Sin tema (clásico)

0. ❌ Salir / Exit

""")

themes = {
    "1": "tankekit_cyberpunk.py",
    "2": "tankekit_ps5.py",
    "3": "tankekit_xbox360.py",
    "4": "tankekit_gta6.py",
    "5": "tankekit_matrix.py",
    "6": "bloatware_remover.py"
}

while True:
    choice = input("Selecciona una opción (1-6, 0 para salir): ").strip()
    
    if choice == "0":
        print("\n¡Hasta luego! / Goodbye!")
        sys.exit(0)
    
    if choice in themes:
        print(f"\n🚀 Iniciando {themes[choice]}...")
        print("   (Acepta los privilegios de administrador cuando se soliciten)\n")
        try:
            subprocess.run([sys.executable, themes[choice]])
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo {themes[choice]}")
            print("   Asegúrate de estar en el directorio correcto de TANKEKIT\n")
        except KeyboardInterrupt:
            print("\n\n⚠️  Ejecución interrumpida por el usuario\n")
        except Exception as e:
            print(f"❌ Error al ejecutar: {e}\n")
        
        print("\n" + "="*63 + "\n")
        input("Presiona Enter para volver al menú... ")
        print("\n" * 2)
    else:
        print("❌ Opción inválida. Por favor elige 1-6 o 0 para salir.\n")
