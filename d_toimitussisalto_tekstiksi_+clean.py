import io
import os
import re
import fitz  # PyMuPDF
import google.generativeai as genai
import tkinter as tk
from tkinter import filedialog
from datetime import datetime



#======================= D E S I G N T A L O ==========================#
#========================================================================================================#
#========================================================================================================#
#========================================================================================================#


# **muuta_tekstiksi muuttaa pdf-tiedoston tekstiksi. Lukee tiedoston ja kirjoittaa sen uudelleen.
def muuta_tekstiksi(pdf_file):
    def pdf_to_text(pdf):
        with fitz.open(stream=pdf.read(), filetype="pdf") as doc:
            return "".join(page.get_text() for page in doc)

    teksti = pdf_to_text(pdf_file)

    # Varmista, että kansio 'data/d/' on olemassa ennen kirjoittamista
    os.makedirs("data/d/", exist_ok=True)
    
    csv_polku = "data/d/toimitussisältö_kokonaisuudessa_tekstina.txt"
    with open(csv_polku, "w", encoding="utf-8") as tiedosto:
        tiedosto.write(teksti)

    kellonaika = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #tulosta_viesti("lohko2 suoritettu", kellonaika)
    return kellonaika


#======================= D E S I G N T A L O ==========================#
#========================================================================================================#
#========================================================================================================#
#========================================================================================================#


#clean_text poistaa turhat erikoismerkit, korjaa numeromuodot ja selkeyttää tekstiä. Lukee tiedoston ja kirjoittaa sen uudelleen.
import re

def clean_text():
 
    tiedostopolku = "data/d/toimitussisältö_kokonaisuudessa_tekstina.txt"
    korjattu_tiedosto = "data/d/puhdistettu_toimitussisalto.txt"

    if os.path.exists(tiedostopolku):
        with open(tiedostopolku, 'r', encoding='utf-8') as tiedosto:
            sisalto = tiedosto.read()

    text = re.sub(r'[^a-zA-Z0-9äöüÄÖÜß\s@._,-:/]', '', sisalto)  # Poistetaan erikoismerkit (paitsi @, ., _ ja ,)
    text = re.sub(r'\s+', ' ', text).strip()  # Poistetaan ylimääräiset välilyönnit
    text = re.sub(r'(\d{1,3})\s(\d{3})', r'\1\2', text)  # Korjataan hajonneet numerot, esim. 173 500 € -> 173500 €
    text = text.replace("•", "-")  # Korvataan listapallot viivoilla
    

    with open(korjattu_tiedosto, "w", encoding="utf-8") as tiedosto:
        tiedosto.write(text)
    


#======================= D E S I G N T A L O ==========================#
#========================================================================================================#
#========================================================================================================#
#========================================================================================================#


# **Poista sanat tekstistä**
'''
def poista_sanat_tekstista():
    tiedostopolku = "data/d/toimitussisältö_kokonaisuudessa_tekstina.txt"
    korjattu_tiedosto = "data/d/toimitussisältö_kokonaisuudessa_tekstina.txt"
    poistettavat_sanat = [
        Lisää tähän poistettavat sanat
    ]

    if os.path.exists(tiedostopolku):
        with open(tiedostopolku, 'r', encoding='utf-8') as tiedosto:
            sisalto = tiedosto.read()

        puhdistettu_sisalto = poista_sanat_tekstista2(sisalto, poistettavat_sanat)

        with open(korjattu_tiedosto, "w", encoding="utf-8") as tiedosto:
            tiedosto.write(puhdistettu_sisalto)

        print(f"Korjattu teksti tallennettu tiedostoon: {korjattu_tiedosto}")
    else:
        print("Tiedostoa ei löytynyt. Tarkista polku.")

    kellonaika = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #tulosta_viesti("lohko3 suoritettu", kellonaika)
    return kellonaika

def poista_sanat_tekstista2(teksti, poistettavat_sanat):
    for sana in poistettavat_sanat:
        teksti = teksti.replace(sana, "")
    teksti = re.sub(r'TOIMITUSTAPASELOSTE\d+\d+', '', teksti)
    teksti = re.sub(r'^\d{1,2}$', '', teksti, flags=re.MULTILINE)
    return teksti
'''



#======================= D E S I G N T A L O ==========================#
#========================================================================================================#
#========================================================================================================#
#========================================================================================================#






from flask import Flask, request
import os
import json
import pandas as pd

from datetime import datetime  # Lisätään kellonaika jokaiselle tapahtumalle

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "pdf" in request.files:
            file = request.files["pdf"]
            if file:
                muuta_tekstiksi(file)
                      
                clean_text()
                
                #poista_sanat_tekstista()

    
    return f'''
    <!DOCTYPE html>
    <html lang="fi">
    <head>
        <meta charset="UTF-8">
        <title>PDF Käsittely</title>
    </head>
    <body>
         <h2>===  D E S I N G T A L O  ===<br></h2><br>
         <h4>Tähän saa syöttää vain Designtalon toimitussisältöjä<br><br>
         Tuloksen skripti tallentaa tähän Designtalon tiedostoon:<br>puhdistettu_toimitussisalto.txt</h4>
        

        <form method="post" enctype="multipart/form-data">
            <input type="file" name="pdf">
            <input type="submit" value="Lähetä">
        </form>
        
    </body>
    </html>
    '''
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway käyttää PORT-muuttujaa
    app.run(host="0.0.0.0", port=port, debug=True)



