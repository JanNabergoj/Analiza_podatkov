import os
import requests
import pomozne_funkcije
            
        
def ime_datoteke_glavna(st_strani):
    return f"stran_{st_strani}.html"


def ime_pot(mapa_pot, ime_dat):
    return os.path.join(mapa_pot, ime_dat)


pot_glavne_strani = r"C:\Users\naber\Desktop\projektna\Analiza_podatkov\html-ji\glavne_strani"
st_strani = 107
url_1 = "https://www.boat24.com/en/powerboats/?rgo%5B0%5D=51&rgo%5B1%5D=5&sort=datdesc"
url_ostale = "https://www.boat24.com/en/powerboats/?page=20&rgo%5B0%5D=51&rgo%5B1%5D=5&sort=datdesc"

def nalozi_html_je(mapa=pot_glavne_strani):
    pomozne_funkcije.shrani_html(url_1, ime_pot(mapa, ime_datoteke_glavna(1)))
    for i in range(1, st_strani):
        pomozne_funkcije.shrani_html((
            f"https://www.boat24.com/en/powerboats/?page={20*i}&rgo%5B0%5D=51&rgo%5B1%5D=5&sort=datdesc"
        ), ime_pot(mapa, ime_datoteke_glavna(i+1)))
    print("Končano")

nalozi_html_je()





    

