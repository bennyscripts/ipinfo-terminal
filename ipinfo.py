from ipaddress import ip_address
from turtle import color
import requests
import colorama
import sys

def get_info(ip_address):
    url = f"https://ipapi.co/{ip_address}/json/"
    resp = requests.get(url)

    return resp.json()

def clean_str(value):
    new_value = value.replace("_", " ")
    new_value = new_value.replace("-", " ")
    new_value = new_value.title()

    if len(new_value) <= 3:
        new_value = new_value.upper()

    return new_value

def main():
    arguments = sys.argv

    if len(arguments) == 1:
        ip_address = input("Enter an IP address: ")
    else:
        ip_address = arguments[1]

    data = get_info(ip_address)
    ip = data["ip"]
    city = clean_str(data["city"])
    region = clean_str(data["region"])
    region_code = data["region_code"]
    country = clean_str(data["country"])
    country_name = clean_str(data["country_name"])
    country_code = clean_str(data["country_code"])
    postal = data["postal"]
    latitude = data["latitude"]
    longitude = data["longitude"]
    timezone = data["timezone"]
    org = data["org"]
    asn = data["asn"]

    message = f"""
     {colorama.Fore.BLUE}{colorama.Style.BRIGHT}{ip} INFO{colorama.Style.NORMAL}{colorama.Fore.WHITE}
  {colorama.Fore.BLUE}{colorama.Style.BRIGHT}>{(len(f"{ip} INFO") + 4) * "─"}<

  {colorama.Fore.RED}{colorama.Style.BRIGHT}>> Location {colorama.Style.NORMAL}{colorama.Fore.WHITE}
    {colorama.Fore.WHITE}{colorama.Style.BRIGHT}Country :{colorama.Style.NORMAL} {country_name} ({country_code})
    {colorama.Fore.WHITE}{colorama.Style.BRIGHT}City :{colorama.Style.NORMAL} {city}
    {colorama.Fore.WHITE}{colorama.Style.BRIGHT}Region :{colorama.Style.NORMAL} {region} ({region_code})
    {colorama.Fore.WHITE}{colorama.Style.BRIGHT}Postal :{colorama.Style.NORMAL} {postal}
    {colorama.Fore.WHITE}{colorama.Style.BRIGHT}Latitude :{colorama.Style.NORMAL} {latitude}
    {colorama.Fore.WHITE}{colorama.Style.BRIGHT}Longitude :{colorama.Style.NORMAL} {longitude}

  {colorama.Fore.RED}{colorama.Style.BRIGHT}>> Other {colorama.Style.NORMAL}{colorama.Fore.WHITE}
    {colorama.Fore.WHITE}{colorama.Style.BRIGHT}Organisation :{colorama.Style.NORMAL} {org}
    {colorama.Fore.WHITE}{colorama.Style.BRIGHT}ASN :{colorama.Style.NORMAL} {asn}
    {colorama.Fore.WHITE}{colorama.Style.BRIGHT}Timezone :{colorama.Style.NORMAL} {timezone}
"""

    print(message)

if __name__ == "__main__":
    main()