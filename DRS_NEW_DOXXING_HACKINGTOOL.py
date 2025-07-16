#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# OSINT Compatible con Termux y Replit - BSZ

import os
import time
import requests
import phonenumbers
import whois
from phonenumbers import carrier, geocoder, timezone
from urllib.parse import quote

# === Colores compatibles ===
class Colors:
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    RESET = '\033[0m'

# === Limpiar pantalla ===
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# === Banner ===
def show_banner():
    print(f"""{Colors.CYAN}
██████╗░██████╗░░██████╗  ████████╗███████╗░█████╗░███╗░░░███╗
██╔══██╗██╔══██╗██╔════╝  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║
██║░░██║██████╔╝╚█████╗░  ░░░██║░░░█████╗░░███████║██╔████╔██║
██║░░██║██╔══██╗░╚═══██╗  ░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
██████╔╝██║░░██║██████╔╝  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
{Colors.WHITE}      HERRAMIENTA OSINT | REPLIT Y TERMUX COMPATIBLE
{Colors.RESET}""")

# === Conversor Decimal a DMS ===
def decimal_a_dms(lat, lon):
    def convertir(valor, pos, neg):
        grados = int(abs(valor))
        minutos_dec = (abs(valor) - grados) * 60
        minutos = int(minutos_dec)
        segundos = (minutos_dec - minutos) * 60
        direccion = pos if valor >= 0 else neg
        return f"{grados}°{minutos}'{round(segundos, 1)}\"{direccion}"

    lat_dms = convertir(lat, 'N', 'S')
    lon_dms = convertir(lon, 'E', 'W')
    return lat_dms, lon_dms

# === Rastrear IP ===
def rastrear_ip():
    ip = input(f"{Colors.WHITE}[?] Ingresa la IP: {Colors.GREEN}")
    try:
        res = requests.get(f"https://ipwho.is/{ip}").json()

        lat = res.get('latitude')
        lon = res.get('longitude')

        if lat is None or lon is None:
            raise ValueError("Coordenadas no disponibles.")

        lat_dms, lon_dms = decimal_a_dms(lat, lon)

        # Codificar para URL
        lat_dms_encoded = quote(lat_dms)
        lon_dms_encoded = quote(lon_dms)

        link_dms = f"https://www.google.com/maps/place/{lat_dms_encoded}+{lon_dms_encoded}/"
        link_decimal = f"https://www.google.com/maps/@{lat},{lon},8z"

        print(f"\n{Colors.WHITE}[i] Información para {Colors.GREEN}{ip}:")
        print(f"{Colors.WHITE}- País: {Colors.GREEN}{res.get('country')}")
        print(f"{Colors.WHITE}- Ciudad: {Colors.GREEN}{res.get('city')}")
        print(f"{Colors.WHITE}- Proveedor: {Colors.GREEN}{res.get('connection', {}).get('isp', 'N/A')}")
        print(f"{Colors.WHITE}- Mapa (Decimal): {Colors.GREEN}{link_decimal}")
        print(f"{Colors.WHITE}- Mapa (DMS): {Colors.GREEN}{link_dms}")

    except Exception as e:
        print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")

# === Rastrear Teléfono ===
def rastrear_telefono():
    numero = input(f"{Colors.WHITE}[?] Ingresa número con + (ej: +573001112233): {Colors.GREEN}")
    try:
        num = phonenumbers.parse(numero)
        print(f"\n{Colors.WHITE}[i] Información del número:")
        print(f"{Colors.WHITE}- Operador: {Colors.GREEN}{carrier.name_for_number(num, 'es')}")
        print(f"{Colors.WHITE}- Región: {Colors.GREEN}{geocoder.description_for_number(num, 'es')}")
        print(f"{Colors.WHITE}- Zona horaria: {Colors.GREEN}{', '.join(timezone.time_zones_for_number(num))}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {e}")

def buscar_usuario():
    username = input(f"{Colors.WHITE}[?] Ingresa el nombre de usuario: {Colors.GREEN}")
    redes = {
        "Facebook": f"https://facebook.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Twitter (X)": f"https://twitter.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Telegram": f"https://t.me/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Blogger": f"https://{username}.blogspot.com",
        "Replit": f"https://replit.com/@{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",
        "About.me": f"https://about.me/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
        "Last.fm": f"https://www.last.fm/user/{username}",
        "500px": f"https://500px.com/{username}",
        "ProductHunt": f"https://www.producthunt.com/@{username}",
        "Dev.to": f"https://dev.to/{username}",
        "HackTheBox": f"https://app.hackthebox.com/profile/{username}",
        "CodePen": f"https://codepen.io/{username}",
        "Keybase": f"https://keybase.io/{username}",
        "BuyMeACoffee": f"https://www.buymeacoffee.com/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "Tripadvisor": f"https://www.tripadvisor.com/Profile/{username}",
        "Disqus": f"https://disqus.com/by/{username}/",
        "Imgur": f"https://imgur.com/user/{username}",
        "Wattpad": f"https://www.wattpad.com/user/{username}",
        "Venmo": f"https://venmo.com/{username}",
        "Cash App": f"https://cash.app/${username}",
        "Strava": f"https://www.strava.com/athletes/{username}",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "Letterboxd": f"https://letterboxd.com/{username}",
        "Anilist": f"https://anilist.co/user/{username}",
        "MyAnimeList": f"https://myanimelist.net/profile/{username}",
        "Bandcamp": f"https://{username}.bandcamp.com",
        "IFTTT": f"https://ifttt.com/p/{username}",
        "OKCupid": f"https://www.okcupid.com/profile/{username}",
        "Taringa": f"https://www.taringa.net/{username}",
        "Ello": f"https://ello.co/{username}",
        "OpenSea": f"https://opensea.io/{username}",
        "NameMC": f"https://namemc.com/profile/{username}",
        "Pluralsight": f"https://app.pluralsight.com/profile/{username}",
        "TryHackMe": f"https://tryhackme.com/p/{username}",
        "Furaffinity": f"https://www.furaffinity.net/user/{username}",
        "Pornhub": f"https://www.pornhub.com/users/{username}",
        "XVideos": f"https://www.xvideos.com/profiles/{username}",
        "XHamster": f"https://xhamster.com/users/{username}",
        "Chess.com": f"https://www.chess.com/member/{username}",
        "Lichess": f"https://lichess.org/@/{username}",
        "Gravatar": f"https://en.gravatar.com/{username}",
        "Instructables": f"https://www.instructables.com/member/{username}",
        "Codeforces": f"https://codeforces.com/profile/{username}",
        "TopCoder": f"https://www.topcoder.com/members/{username}",
        "Stack Overflow": f"https://stackoverflow.com/users/story/{username}",
        "SuperUser": f"https://superuser.com/users/{username}",
        "AskUbuntu": f"https://askubuntu.com/users/{username}",
        "Unix.SE": f"https://unix.stackexchange.com/users/{username}",
        "BitcoinTalk": f"https://bitcointalk.org/index.php?action=profile;u={username}",
        "Scratch": f"https://scratch.mit.edu/users/{username}",
        "Houzz": f"https://www.houzz.com/user/{username}",
        "Mix": f"https://mix.com/{username}",
        "WeHeartIt": f"https://weheartit.com/{username}",
        "DailyMotion": f"https://www.dailymotion.com/{username}",
        "AngelList": f"https://angel.co/u/{username}",
        "Shutterstock": f"https://www.shutterstock.com/g/{username}",
        "Tripit": f"https://www.tripit.com/people/{username}",
        "Canva": f"https://www.canva.com/{username}/",
        "Bitbucket": f"https://bitbucket.org/{username}/",
        "Hackaday.io": f"https://hackaday.io/{username}",
        "Badoo": f"https://badoo.com/profile/{username}",
        "Zoho": f"https://zoho.com/{username}",
        "Zoosk": f"https://www.zoosk.com/profile/{username}",
        "Imgflip": f"https://imgflip.com/user/{username}",
        "Giphy": f"https://giphy.com/{username}",
        "MeWe": f"https://mewe.com/i/{username}",
        "Rumble": f"https://rumble.com/{username}",
        "Brighteon": f"https://www.brighteon.com/channels/{username}",
        "PeerTube": f"https://peertube.social/accounts/{username}",
        "Gab": f"https://gab.com/{username}",
        "Mastodon.social": f"https://mastodon.social/@{username}",
        "Pixiv": f"https://www.pixiv.net/en/users/{username}",
        "Myspace": f"https://myspace.com/{username}",
        "Vero": f"https://getvero.com/{username}",
        "Triller": f"https://triller.co/@{username}",
        "Ravelry": f"https://www.ravelry.com/people/{username}",
        "VSCO": f"https://vsco.co/{username}",
        "Zillow": f"https://www.zillow.com/profile/{username}/",
        "Unsplash": f"https://unsplash.com/@{username}",
        "Ellucian": f"https://{username}.elluciancloud.com"
    }

    print(f"\n{Colors.WHITE}[i] Resultados para {Colors.GREEN}{username}:")
    for nombre, url in redes.items():
        try:
            res = requests.get(url, timeout=5)
            estado = '✅ Encontrado' if res.status_code == 200 else '❌ No encontrado'
            print(f"{Colors.WHITE}- {nombre}: {Colors.GREEN}{estado} {Colors.WHITE}→ {Colors.CYAN}{url}")
        except:
            print(f"{Colors.WHITE}- {nombre}: {Colors.RED}Error de conexión {Colors.WHITE}→ {Colors.CYAN}{url}")

def info_dominio():
    dominio = input(f"{Colors.WHITE}[?] Ingresa el dominio (ej: google.com): {Colors.GREEN}")
    try:
        datos = whois.whois(dominio)

        # Algunos campos pueden ser listas, normalizamos para mostrar solo el primero si es lista
        registrar = datos.registrar if datos.registrar else "No disponible"
        creation_date = datos.creation_date
        expiration_date = datos.expiration_date

        # Si es lista, mostrar solo la primera fecha
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        creation_date = creation_date.strftime('%Y-%m-%d') if creation_date else "No disponible"
        expiration_date = expiration_date.strftime('%Y-%m-%d') if expiration_date else "No disponible"

        print(f"\n{Colors.WHITE}[i] Información WHOIS de {Colors.GREEN}{dominio}:")
        print(f"{Colors.WHITE}- Registrador: {Colors.GREEN}{registrar}")
        print(f"{Colors.WHITE}- Fecha de creación: {Colors.GREEN}{creation_date}")
        print(f"{Colors.WHITE}- Vencimiento: {Colors.GREEN}{expiration_date}")

    except Exception as e:
        print(f"{Colors.RED}[!] Error obteniendo datos WHOIS: {e}")

# === Menú principal ===
def main():
    while True:
        clear_screen()
        show_banner()
        print(f"{Colors.WHITE}[+] Menú Principal:")
        print(f"{Colors.CYAN}[1] {Colors.WHITE}Rastrear IP")
        print(f"{Colors.CYAN}[2] {Colors.WHITE}Rastrear Teléfono")
        print(f"{Colors.CYAN}[3] {Colors.WHITE}Buscar Usuario")
        print(f"{Colors.CYAN}[4] {Colors.WHITE}Información de Dominio")
        print(f"{Colors.CYAN}[0] {Colors.WHITE}Salir")

        opc = input(f"\n{Colors.GREEN}[?] Selecciona opción: {Colors.WHITE}")
        if opc == '1':
            rastrear_ip()
        elif opc == '2':
            rastrear_telefono()
        elif opc == '3':
            buscar_usuario()
        elif opc == '4':
            info_dominio()
        elif opc == '0':
            print(f"{Colors.RED}Saliendo...{Colors.RESET}")
            print(f"\n{Colors.CYAN}¡Sígueme en mis redes sociales!{Colors.RESET}")
            print(f"{Colors.WHITE}- GitHub DRS: {Colors.GREEN}https://github.com/Drsteamhack434")
            print(f"{Colors.WHITE}- GitHub BSZ: {Colors.GREEN}https://github.com/AvastrOficial")
            break

        else:
            print(f"{Colors.RED}[!] Opción inválida")

        input(f"\n{Colors.YELLOW}Presiona Enter para continuar...{Colors.RESET}")

# === Ejecutar ===
if __name__ == "__main__":
    main()
