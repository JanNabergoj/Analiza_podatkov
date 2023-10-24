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

Na koncu pri analizi nisem uporabil vseh podatkov. Analiza je bila narejena s pomočjo knjižnic: *pandas*, *matplotlib* in *numpy*.

Hipoteze:
- Razlika v povprečni ceni rabljene barke ni velika med Italijo in Slovenijo
- "Flybridge" je najdražji tip barke glede na dolžino
- Nad 10m dolžine cena bark precej naraste
- Cena bark pada s starostjo barke
- Cena bark pada s številom motornih ur

## Zajem podatkov
Najprej sem z datoteko *pridobi_podatke.py* iz spletne strani pobral html kodo posamezne strani z oglasi, pri tem sem si pomagal z datoteko *pomozne_funkcije.py*. Nato sem pobral še kodo za posamezen oglas, ker na "glavni" strani ni bilo vseh podatkov. To je naredila datoteka *pridobi_podatke.py*, ki jih je tudi "počistila" in zapisala v *podatki_bark.csv*. Pri tem so mi pomagale knjižnice: *os*, *requests*, *random*, *time*, *re* in *csv*.
