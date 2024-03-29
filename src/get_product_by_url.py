import requests
import os
import sys
import random
import time
import re

from bs4 import BeautifulSoup
from PIL import Image
from colorama import Fore


def get_willhaben_item_by_url(url):
    name_adding = 0
    product_page = requests.get(url)
    soup_pd = BeautifulSoup(product_page.content, 'html.parser')

    for heading in soup_pd.find_all("title"):
        heading_item = heading.text.strip("- willhaben")

    wh_code = str()
    for char in url[::-1]:
        if char.isnumeric():
            wh_code += char
        elif char == "-":
            break
    wh_code = wh_code[::-1]

    description = soup_pd.find(attrs={"data-testid": "ad-description-Beschreibung"}).text

    if not os.path.exists("Results/" + wh_code):
        os.makedirs("Results/" + wh_code)

    image_regex = r'"referenceImageUrl":".+?(?=")"'
    image_links = [image_link[21:-1] for image_link in re.findall(image_regex, soup_pd.decode())]

    for image_link in image_links:
        response = requests.get(image_link)
        image_name = f"Image{name_adding}" + ".jpg"
        name_adding += 1

        try:
            with open(os.path.join(f'Results/' + f"{wh_code}", image_name), "wb") as file:
                file.write(response.content)
                file.close()
                image_to_change = Image.open(f'Results/' + f"{wh_code}/" + image_name)

                neue_länge = round(int(list(image_to_change.size)[0]) * 0.9)
                neue_breite = round(int(list(image_to_change.size)[1]) * 0.9)

                new_image = image_to_change.resize((neue_länge, neue_breite))
                new_image.save(f'Results/' + f"{wh_code}/" + image_name)
        except:
            os.remove(f'Results/' + f"{wh_code}/{image_name}")

    infos = open("Results/" + wh_code + f"/Infos {wh_code}.txt", "w", encoding='utf-8',
                 errors='replace')
    infos.write("Titel, Price, ZIP and Place:\n")
    infos.write(heading_item)
    infos.write("\n----------------------------------------------\n")
    infos.write("Description:\n")
    infos.write(description)
    infos.write("\n----------------------------------------------\n")
    infos.write("Willhaben Link:\n")
    infos.write(url)
    infos.write("\n----------------------------------------------\n")
    infos.close()

    print(Fore.GREEN + f"-----------------------\nGrabbing completed.\n-----------------------" + Fore.CYAN)
