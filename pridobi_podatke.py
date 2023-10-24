import re
import os
import pomozne_funkcije
import csv



vzorec_bloka = re.compile(
    r'<div>.*?'
    r'<div id="specs">.*?'
    r'<header class="heading heading--page l-mb-32">.*?'
    r'</p>.*?'
    r'<div id="location">.*?'
    r'<hr class="divider l-mt-32 l-mb-32">.*?'
    r'</div>',
    flags=re.DOTALL
)

def izlusci_blok(html_koda):
    prebrana = pomozne_funkcije.preberi_datoteko(os.path.join(r"html-ji\oglasi", html_koda))
    blok = re.search(vzorec_bloka, prebrana).group(0)
    return blok



vzorec_glavni = re.compile(
    r'<p class="heading__title-header">.*?'
    r'title=".*?">(?P<tip_barke>.*?)</a>.*?'
    r'<h2 class="heading__title heading__title--icon-right">\s*' 
    r'<span>(?P<ime_barke>.*?)</span>.*?'
    r'<li>\s*<span class="list__value list__value--large">(?P<cena>.*?)</span>.*?'
    r'<ul class="list list--key-value">\s*<li>\s*'
    r'<span class="list__value">(?P<letnik>.*?)</span>.*?'
    r'<ul class="list list--key-value l-mt-16">\s*<li>\s*'
    r'<span class="list__value">(?P<dolzina_sirina>.*?)</span>',   
    flags=re.DOTALL
)

vzorec_st_kabin = re.compile(
    r'<span class="list__value">(?P<st_kabin>.\d*?) Cabin\w*?</span>'
    
)

vzorec_ure = re.compile(
    r'<span class="list__value">(?P<st_ur>.*?) h</span>'
)

vzorec_drzava = re.compile(
    r'<p class="text">\s*(?P<drzava>\w*?) &raquo;'   
)



oglasi_pot = os.path.join("html-ji", "oglasi")

def ustvari_id(oglas):
    niz, _ = oglas.split(".")
    return int(niz[6:])

def izlusci_podatke(mapa=oglasi_pot):
    podatki_bark = []
    for oglas in os.listdir(mapa):
        blok = izlusci_blok(oglas)
        try:
            glavni_podatki = re.search(vzorec_glavni, blok).groupdict()
        except AttributeError:
            continue
        glavni_podatki["id"] = ustvari_id(oglas)
        try:
            glavni_podatki["st_kabin"] = int(re.search(vzorec_st_kabin, blok).groupdict()["st_kabin"])
        except AttributeError:
              glavni_podatki["st_kabin"] = None
        try:
            glavni_podatki["st_ur"] = re.search(vzorec_ure, blok).groupdict()["st_ur"]
        except AttributeError:
             glavni_podatki["st_ur"] = None
        try:
            glavni_podatki["drzava"] = re.search(vzorec_drzava, blok).groupdict()["drzava"]
        except AttributeError:
            glavni_podatki["drzava"] = None
        podatki_bark.append(glavni_podatki)
    return podatki_bark



def pocisti_podatke(sez_bark):
    nov_sez = []
    for slovar in sez_bark:
        if slovar["letnik"].isdigit():
            slovar["letnik"] = int(slovar["letnik"])
        else:
            slovar["letnik"] = None

        try:
            dolzina, sirina = slovar["dolzina_sirina"].rstrip(" m").split(" m x ")
            del slovar["dolzina_sirina"]
            slovar["dolzina"] = float(dolzina)
            slovar["sirina"] = float(sirina)
        except ValueError:
            if slovar["dolzina_sirina"][0].isdigit() and "m" in slovar["dolzina_sirina"]:
                slovar["dolzina"] = float(slovar["dolzina_sirina"].rstrip(" m"))
                del slovar["dolzina_sirina"]
            else:
                del slovar["dolzina_sirina"]
                slovar["dolzina"] = None
                slovar["sirina"] = None

        if slovar["st_ur"] != None and "'" in slovar["st_ur"]:
            nove_ure = slovar["st_ur"].replace("'", "")
            slovar["st_ur"] = int(nove_ure)
        elif slovar["st_ur"] != None:
            slovar["st_ur"] = int(slovar["st_ur"])

        if slovar["cena"] == "Price on Request":
            slovar["cena"] = None
        else:
            try:
                nova_cena = slovar["cena"].lstrip("EUR ").rstrip(",-").replace(".", "")
                slovar["cena"] = int(nova_cena)
            except ValueError:
                slovar["cena"] = None

        nov_sez.append(slovar)
    return nov_sez



podatki = izlusci_podatke()
pocisceni_podatki = pocisti_podatke(podatki)



imena = ["id", "ime_barke", "tip_barke", "cena", "dolzina", "sirina", "letnik", "st_kabin", "st_ur", "drzava"]


def zapisi_csv(csv_dat="podatki_bark.csv", sez=pocisceni_podatki, imena_polj = imena):
    with open(csv_dat, "w", encoding="utf-8") as dat:
        writer = csv.DictWriter(dat, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in sez:
            writer.writerow(slovar)
    print("Končano")



zapisi_csv()







