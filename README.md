# **Keylogger Educativo**
Este repositorio tiene como propósito educativo mostrar cómo funciona un keylogger y cómo protegerse de posibles ataques. **El código no debe ser usado de manera malintencionada**. Es esencial realizar este tipo de experimentos solo en entornos controlados y con fines éticos, como pruebas de seguridad en un entorno de laboratorio personal.

## **Índice**
- [Introducción](#introducción)
- [Cómo Funciona el Keylogger](#cómo-funciona-el-keylogger)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación](#instalación)
- [Uso del Código](#uso-del-código)
- [Licencia](#licencia)

## **Introducción**
Un keylogger es un tipo de software que registra las pulsaciones de teclado de un usuario sin su conocimiento. Este código debe ser usado únicamente en un entorno controlado con el objetivo de entender su funcionamiento y aprender a protegerse contra él. **Este proyecto no debe ser utilizado con fines malintencionados ni en sistemas ajenos sin el permiso explícito de los involucrados**.

## **Cómo Funciona el Keylogger**
El keylogger captura las pulsaciones de teclado de un usuario y las guarda en un archivo o las envía a un servidor remoto. En este proyecto, el keylogger puede funcionar de dos maneras:
1. **Localmente**, almacenando las pulsaciones en un archivo de texto.
2. **De manera remota**, enviando las pulsaciones a través de correo electrónico o cargándolas en una nube.

El keylogger se ejecuta en segundo plano sin mostrar ventanas ni advertencias, lo que lo hace más difícil de detectar para el usuario promedio.

### **Flujo básico**:
1. El keylogger comienza a ejecutarse cuando el archivo es descargado.
2. El programa intercepta las teclas presionadas por el usuario.
3. Registra y guarda esas pulsaciones de manera continua.
4. Los datos pueden ser enviados por correo electrónico o subidos a la nube.

## **Requisitos del Sistema**
- **Python 3.x**: Necesario para ejecutar el código.
- **Dependencias**: 
  - `pynput` (Para registrar las pulsaciones del teclado)
  - `smtplib` (Para enviar correos electrónicos)
  - **Otras librerías dependiendo de la configuración** (por ejemplo, `requests` si se utiliza para cargar a la nube).

## **Instalación**

### **Pasos para instalar el proyecto**:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/keylogger_educativo.git
   cd keylogger_educativo

2.Instalar las dependencias: Si no tienes las dependencias necesarias, puedes instalarlas con pip:

```bash
Copia el codi
pip install pynput
```
3. Configuración de correo (si deseas enviar los datos por correo electrónico):
Edita el código para poner tus credenciales de correo electrónico y la dirección del receptor.

### **Uso del Código**
Ejecutar el Keylogger en un entorno controlado:
Para ejecutar el keylogger, simplemente ejecuta el script Python. Recuerda que debes hacerlo en un entorno controlado y con el conocimiento del propietario de la máquina:

```bash
python keylogger.py
```
Una vez ejecutado, el keylogger comenzará a capturar las teclas presionadas y enviará los datos según la configuración (por correo o subiendo a la nube).
