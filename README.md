# Analiza rabljenih bark
V projektni nalogi sem analiziral približno 2000 oglasov rabljenih bark v Sloveniji in Italiji. Podatke sem zajel iz spletne strani [Boat24](https://www.boat24.com/en/). Pri analizi sem se osredotočil na to, kako je cena barke odvisna od njenih lastnosti.

Pri vsakem oglasu sem zajel:
- Ime barke
- Tip barke
- Ceno
- Dolžino
- Širino
- Letnik izdelave
- Število kabin, ki jih ima
- Število ur motorja (koliko ur je motor deloval)
- Državo (ali se nahaja v Italiji ali Sloveniji)

Dodal sem jim še id za lažjo analizo.


Hipoteze:
- Razlika v povprečni ceni rabljene barke ni velika med Italijo in Slovenijo
- "Flybridge" je najdražji tip barke glede na dolžino
- Cena barke bolj vpada z dolžino kot s številom motornih ur
- Nad 10m dolžine cena bark precej naraste

## Zajem podatkov
Najprej sem z datoteko *pridobi_podatke.py* iz spletne strani pobral html kodo posamezne strani z oglasi, pri tem sem si pomagal z datoteko *pomozne_funkcije.py*. Nato sem pobral še kodo za posamezen oglas, ker na "glavni" strani ni bilo vseh podatkov. To je naredila datoteka *pridobi_podatke.py*, ki jih je tudi "počistila" in zapisala v *podatki_bark.csv*. 
