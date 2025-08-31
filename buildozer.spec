
[app]
# Configuración básica de la app
title = Calculadora Básica
package.name = calculadora
package.domain = org.example
source.dir = .
source.main = main.py
version = 1.0

# Dependencias requeridas
requirements = python3,kivy

# Configuración Android
android.permissions =
android.api = 28
android.minapi = 21
android.sdk = 28
android.ndk = 21e

# Orientación y visualización
orientation = portrait
fullscreen = 0
window.fullscreen = 0

# Logs y debugging
log_level = 2
android.arch = arm64-v8a
