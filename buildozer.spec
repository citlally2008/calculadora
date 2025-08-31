[app]
# Configuración básica de la app
title = Calculadora Básica
package.name = calculadora
package.domain = org.example
source.dir = .
source.main = main.py
version = 1.0
version.regex = __version__ = ['"]([^'"]*)['"]
version.filename = %(source.dir)s/main.py

# Dependencias requeridas
requirements = python3,kivy

# Configuración de icono y presplash (opcional)
# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

# Configuración Android
[app:android]
# API levels actualizados y compatibles
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.gradle_dependencies = 

# Arquitectura
android.archs = arm64-v8a, armeabi-v7a

# Permisos
android.permissions = 

# Orientación y visualización
orientation = portrait
fullscreen = 0

# Configuración de compilación
[buildozer]
# Nivel de logs
log_level = 2
# Directorio de trabajo
bin_dir = ./bin
