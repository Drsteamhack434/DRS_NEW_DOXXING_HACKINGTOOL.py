# OSINT Drs - Compatible con Termux y Replit

Este programa es una herramienta de OSINT (Open Source Intelligence) que permite obtener información pública relacionada con IPs, números telefónicos, usuarios en redes sociales y datos WHOIS de dominios. Está diseñada para ser compatible y funcionar correctamente en ambientes como Termux (Android) y Replit (entornos web de desarrollo).

---

## Componentes y Funcionamiento General

### Importaciones y Librerías

- Utiliza librerías estándar (`os`, `time`, `requests`).
- Usa librerías especializadas:  
  - `phonenumbers` para información de números telefónicos.  
  - `whois` para datos de dominios.  
  - `urllib.parse` para codificar URLs.

### Clase `Colors`

Define códigos ANSI para mostrar texto en colores en la consola, haciendo la interfaz más amigable visualmente.

### Funciones Principales

- `clear_screen()`: Limpia la consola para refrescar la interfaz al mostrar el menú o resultados.
- `show_banner()`: Muestra un banner estilizado con colores, presentando el nombre y propósito de la herramienta.
- `decimal_a_dms(lat, lon)`: Convierte coordenadas geográficas de formato decimal a DMS (grados, minutos, segundos), formato común para coordenadas GPS.

---

## Funciones de OSINT

### `rastrear_ip()`
- Solicita una IP.
- Consulta la API pública [ipwho.is](https://ipwho.is) para obtener información geográfica y del proveedor.
- Muestra:
  - País y ciudad asociados a la IP.
  - Proveedor del servicio (ISP).
  - Dos enlaces de mapas en Google Maps: uno con coordenadas decimales y otro en formato DMS, con valores codificados para URL.

### `rastrear_telefono()`
- Solicita un número telefónico con formato internacional (+código de país).
- Con la librería `phonenumbers` obtiene:
  - Operador o carrier del número.
  - Región geográfica del número.
  - Zonas horarias asociadas.

### `buscar_usuario()`
- Solicita un nombre de usuario.
- Consulta más de 100 redes sociales y plataformas para verificar si existe ese usuario.
- Para cada red:
  - Realiza una petición HTTP a la URL construida con el usuario.
  - Informa si el usuario fue encontrado (código HTTP 200) o no.
  - Muestra la URL consultada.
- Maneja errores de conexión para evitar fallos en el programa.

### `info_dominio()`
- Solicita un dominio web (ejemplo: google.com).
- Usa la librería `whois` para obtener:
  - Registrador del dominio.
  - Fecha de creación.
  - Fecha de expiración.
- Normaliza los datos para mostrar correctamente aunque la API regrese listas o valores vacíos.

---

## Menú Principal

El programa corre un loop infinito mostrando un menú con opciones numeradas:

1. Rastrear IP  
2. Rastrear Teléfono  
3. Buscar Usuario  
4. Información de Dominio  
0. Salir  

Según la opción seleccionada, llama a la función correspondiente.  
Al salir (opción 0), muestra enlaces a redes sociales GitHub como despedida.  

Tras cada acción, espera que el usuario presione Enter para continuar, permitiendo revisar la información antes de limpiar la pantalla y mostrar el menú nuevamente.

---

## Librerías usadas

| Librería         | Propósito                                          | Uso Principal                                        |
|------------------|---------------------------------------------------|-----------------------------------------------------|
| `os`             | Ejecutar comandos del sistema operativo           | Limpiar pantalla (`clear_screen()`)                  |
| `time`           | Funciones relacionadas con tiempo y pausas        | (No usado explícitamente en el código actual)        |
| `requests`       | Realizar peticiones HTTP                           | Consultar APIs y URLs para verificar usuarios e IPs |
| `phonenumbers`   | Manipular y validar números telefónicos            | Obtener operador, región y zona horaria de números   |
| `whois`          | Consultar registros WHOIS de dominios               | Obtener datos públicos de un dominio                  |
| `urllib.parse`   | Codificar texto para URLs                           | Codificar coordenadas DMS para enlaces en Google Maps|

---

## APIs externas usadas

| API                     | Qué es                                            | Uso                                                    |
|-------------------------|--------------------------------------------------|--------------------------------------------------------|
| https://ipwho.is/       | API pública gratuita para datos geográficos y de red de IP | Obtener país, ciudad, ISP, latitud y longitud para IP  |

---

## ⚙️ Instalación

```bash
pkg update && pkg upgrade -y

pkg install python git -y

git clone https://github.com/AvastrOficial/DRS_NEW_DOXXING_HACKINGTOOL.git

cd DRS_NEW_DOXXING_HACKINGTOOL

pip install requests phonenumbers python-whois

chmod +x DRS_HackingTools.py

python DRS_HackingTools.py
```
<img width="655" height="482" alt="image" src="https://github.com/user-attachments/assets/ed39617a-3066-4ce5-8c8c-d75ddf1f18d6" />

