#!/usr/bin/env python3

import os
import requests
import socket
from urllib.parse import urlparse

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    banner = """
 _           ___ _________ _______  _______  _______  _______  _______  _______           _______  ______   _______  _______  _______  _        _        _______  _______ 
( (    /|   /   )\__   __// ___   )/ ___   )(  ___  )(  ____ \(  ____ \(  ____ \|\     /|(  ____ \(  ___ \ (  ____ \(  ____ \(  ___  )( (    /|( (    /|(  ____ \(  ____ )
|  \  ( |  / /) |   ) (   \/   )  |\/   )  || (   ) || (    \/| (    \/| (    \/| )   ( || (    \/| (   ) )| (    \/| (    \/| (   ) ||  \  ( ||  \  ( || (    \/| (    )|
|   \ | | / (_) (_  | |       /   )    /   )| |   | || (__    | (__    | |      | | _ | || (__    | (__/ / | (_____ | |      | (___) ||   \ | ||   \ | || (__    | (____)|
| (\ \) |(____   _) | |      /   /    /   / | |   | ||  __)   |  __)   | |      | |( )| ||  __)   |  __ (  (_____  )| |      |  ___  || (\ \) || (\ \) ||  __)   |     __)
| | \   |     ) (   | |     /   /    /   /  | |   | || (      | (      | |      | || || || (      | (  \ \       ) || |      | (   ) || | \   || | \   || (      | (\ (   
| )  \  |     | |   | |    /   (_/\ /   (_/\| (___) || )      | )      | (____/\| () () || (____/\| )___) )/\____) || (____/\| )   ( || )  \  || )  \  || (____/\| ) \ \__
|/    )_)     (_)   )_(   (_______/(_______/(_______)|/       |/       (_______/(_______)(_______/|/ \___/ \_______)(_______/|/     \||/    )_)|/    )_)(_______/|/   \__/
                                                                                                                                                                          
        Code by N4tzzOfficial
DONT NOT COPYRIGHT ALL WITHOUT PERMISSION
    """
    print(banner)

def get_ip_and_ports(url):
    try:
        domain = urlparse(url).netloc
        ip_address = socket.gethostbyname(domain)
        print(f"IP Address: {ip_address}")
        
        # Check common ports
        common_ports = [80, 443, 21, 22, 25, 53, 110, 143]
        open_ports = []

        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
            sock.close()

        if open_ports:
            print(f"Open Ports: {', '.join(map(str, open_ports))}")
        else:
            print("No common open ports found.")
            
    except socket.gaierror:
        print("Could not resolve the domain.")

def scan_website(url):
    try:
        response = requests.get(url)
        print(f"\nScanning {url}...")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response.elapsed.total_seconds()} seconds")
        
        # Check for accessibility
        if response.status_code == 200:
            print("Scan results: Website is accessible.")

            # Gather additional information
            print("\nHeaders:")
            for header, value in response.headers.items():
                print(f"{header}: {value}")

            # Check for content type
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' in content_type:
                print("Content-Type indicates this is an HTML page.")

            # Get IP and open ports
            get_ip_and_ports(url)

        else:
            print(f"Scan results: Received status code {response.status_code}.")

    except requests.exceptions.RequestException as e:
        print(f"Error scanning {url}: {e}")

def help_text():
    print("\nHelp: This tool allows you to scan websites for vulnerabilities.")
    print("You can enter a URL (e.g., http://example.com) to check its status and response time.")
    print("Make sure to include http:// or https:// in the URL.")

def main():
    while True:
        clear_screen()
        display_banner()
        print("1) Scan Website")
        print("2) Help")
        print("00) Exit")

        choice = input("Select an option: ")

        if choice == '1':
            url = input("Enter URL to scan (including http:// or https://): ")
            scan_website(url)
            input("\nPress Enter to continue...")
        elif choice == '2':
            help_text()
            input("\nPress Enter to return to the menu...")
        elif choice == '00':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
