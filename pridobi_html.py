import os
import re
import pomozne_funkcije

            

def ime_datoteke_glavna(st_strani):
    return f"stran_{st_strani}.html"


def ime_datoteke_oglas(i):
    return f"oglas_{i}.html"


def ime_pot(mapa_pot, ime_dat):
    return os.path.join(mapa_pot, ime_dat)


pot_glavne_strani = r"C:\Users\naber\Desktop\projektna\Analiza_podatkov\html-ji\glavne_strani"
st_strani = 107
url_1 = "https://www.boat24.com/en/powerboats/?rgo%5B0%5D=51&rgo%5B1%5D=5&sort=datdesc"
url_ostale = "https://www.boat24.com/en/powerboats/?page=20&rgo%5B0%5D=51&rgo%5B1%5D=5&sort=datdesc"
linki_oglasov = ime_pot("html-ji", "linki_oglasov.txt")
html_ji = ime_pot("html-ji", "glavne_strani")
html_oglasi = ime_pot("html-ji", "oglasi")


def nalozi_html_je(mapa=pot_glavne_strani):
    pomozne_funkcije.shrani_html(url_1, ime_pot(mapa, ime_datoteke_glavna(1)))
    for i in range(1, st_strani):
        pomozne_funkcije.shrani_html((
            f"https://www.boat24.com/en/powerboats/?page={20*i}&rgo%5B0%5D=51&rgo%5B1%5D=5&sort=datdesc"
        ), ime_pot(mapa, ime_datoteke_glavna(i+1)))
    print("Končano")


vzorec_link = re.compile(r'<div class="blurb blurb--strip blurb--singleline js-link" data-link="(?P<link>.+?)" ')
    
def poisci_linke(dat=linki_oglasov, mapa=html_ji):
    with open(dat, "w", encoding="utf-8") as dat:
        for html in os.listdir(mapa):
            prebran = pomozne_funkcije.preberi_datoteko(ime_pot(r"html-ji\glavne_strani", html))
            najdeni_linki = [link["link"] for link in re.finditer(vzorec_link, prebran)]
            for link in najdeni_linki:
                print(link, file=dat)
        

def nalozi_html_oglasov(dat=linki_oglasov, mapa=html_oglasi):
    with open(dat, "r", encoding="utf-8") as dat:
        i = 1
        for link in dat:
            pomozne_funkcije.shrani_html(link.strip(), ime_pot(mapa, ime_datoteke_oglas(i)))
            i += 1
           
nalozi_html_je()
poisci_linke()
nalozi_html_oglasov()


    









    

