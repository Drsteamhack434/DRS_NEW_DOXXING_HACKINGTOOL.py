#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Código mejorado por @DeepSeekChat (basado en el original de DRS TEAM)
# Herramienta OSINT para rastreo de IP, teléfonos, usuarios y más.

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr
import whois
from datetime import datetime

# Configuración de colores
class Colors:
    BLACK = '\033[30m'
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    RESET = '\033[0m'

# Banner principal
def show_banner():
    banner = f"""
{Colors.CYAN}
██████╗░██████╗░░██████╗  ████████╗███████╗░█████╗░███╗░░░███╗
██╔══██╗██╔══██╗██╔════╝  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║
██║░░██║██████╔╝╚█████╗░  ░░░██║░░░█████╗░░███████║██╔████╔██║
██║░░██║██╔══██╗░╚═══██╗  ░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
██████╔╝██║░░██║██████╔╝  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
{Colors.WHITE}
               HERRAMIENTA OSINT - DRS TEAM (MEJORADA)
{Colors.RESET}
"""
    print(banner)

# Limpiar pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Decorador para mostrar banner antes de cada función
def osint_banner(func):
    def wrapper(*args, **kwargs):
        clear_screen()
        print(f"{Colors.CYAN}\n[+] Ejecutando: {func.__name__.replace('_', ' ').title()}")
        print("-" * 50 + Colors.RESET)
        return func(*args, **kwargs)
    return wrapper

### --- FUNCIONES PRINCIPALES --- ###

@osint_banner
def ip_tracker():
    ip = input(f"{Colors.WHITE}\n[?] Ingrese la IP objetivo: {Colors.GREEN}")
    try:
        response = requests.get(f"http://ipwho.is/{ip}", timeout=10)
        response.raise_for_status()
        data = response.json()
        
        print(f"\n{Colors.WHITE}[i] Información de la IP {Colors.GREEN}{ip}:")
        print(f"{Colors.WHITE}  - País: {Colors.GREEN}{data.get('country', 'N/A')} ({data.get('country_code', 'N/A')})")
        print(f"{Colors.WHITE}  - Ciudad: {Colors.GREEN}{data.get('city', 'N/A')}")
        print(f"{Colors.WHITE}  - Proveedor: {Colors.GREEN}{data.get('connection', {}).get('isp', 'N/A')}")
        print(f"{Colors.WHITE}  - Mapa: {Colors.GREEN}https://www.google.com/maps/@{data.get('latitude')},{data.get('longitude')},8z")
        
    except requests.RequestException as e:
        print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")

@osint_banner
def phone_tracker():
    number = input(f"{Colors.WHITE}\n[?] Ingrese número (Ej: +573123456789): {Colors.GREEN}")
    try:
        parsed = phonenumbers.parse(number)
        print(f"\n{Colors.WHITE}[i] Información del teléfono:")
        print(f"{Colors.WHITE}  - Operador: {Colors.GREEN}{carrier.name_for_number(parsed, 'es')}")
        print(f"{Colors.WHITE}  - Región: {Colors.GREEN}{geocoder.description_for_number(parsed, 'es')}")
        print(f"{Colors.WHITE}  - Zona horaria: {Colors.GREEN}{', '.join(timezone.time_zones_for_number(parsed))}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")

@osint_banner
def username_search():
    username = input(f"{Colors.WHITE}\n[?] Ingrese nombre de usuario: {Colors.GREEN}")
    sites = [
        {"name": "Facebook", "url": "https://facebook.com/{}"},
        {"name": "GitHub", "url": "https://github.com/{}"},
        {"name": "Instagram", "url": "https://instagram.com/{}"},
    ]
    
    print(f"\n{Colors.WHITE}[i] Resultados para {Colors.GREEN}{username}:")
    for site in sites:
        url = site["url"].format(username)
        try:
            response = requests.get(url, timeout=5)
            print(f"{Colors.WHITE}  - {site['name']}: {Colors.GREEN}{'✅ Encontrado' if response.status_code == 200 else '❌ No existe'}")
        except:
            print(f"{Colors.WHITE}  - {site['name']}: {Colors.RED}Error de conexión")

@osint_banner
def domain_info():
    domain = input(f"{Colors.WHITE}\n[?] Ingrese dominio (Ej: google.com): {Colors.GREEN}")
    try:
        info = whois.whois(domain)
        print(f"\n{Colors.WHITE}[i] Información de {Colors.GREEN}{domain}:")
        print(f"{Colors.WHITE}  - Registrante: {Colors.GREEN}{info.registrar}")
        print(f"{Colors.WHITE}  - Fecha creación: {Colors.GREEN}{info.creation_date}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")

### --- MENÚ PRINCIPAL --- ###
def main_menu():
    options = [
        {"num": 1, "text": "Rastrear IP", "func": ip_tracker},
        {"num": 2, "text": "Rastrear Teléfono", "func": phone_tracker},
        {"num": 3, "text": "Buscar Usuario", "func": username_search},
        {"num": 4, "text": "Información de Dominio", "func": domain_info},
        {"num": 0, "text": "Salir", "func": exit}
    ]
    
    while True:
        clear_screen()
        show_banner()
        print(f"{Colors.WHITE}\n[+] Menú Principal:")
        for opt in options:
            print(f"  {Colors.CYAN}[{opt['num']}] {Colors.WHITE}{opt['text']}")
        
        try:
            choice = int(input(f"\n{Colors.GREEN}[?] Seleccione opción: {Colors.WHITE}"))
            selected = next((opt for opt in options if opt["num"] == choice), None)
            if selected:
                selected["func"]()
                input(f"\n{Colors.GREEN}[+] Presione Enter para continuar...")
            else:
                print(f"{Colors.RED}[!] Opción inválida{Colors.RESET}")
                time.sleep(1)
        except ValueError:
            print(f"{Colors.RED}[!] Ingrese un número válido{Colors.RESET}")
            time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}[!] Saliendo...{Colors.RESET}")
            break

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Programa terminado.{Colors.RESET}")
