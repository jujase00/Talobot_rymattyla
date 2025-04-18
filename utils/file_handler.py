import os
import json
from werkzeug.utils import secure_filename
import fitz
from pathlib import Path
from logger_config import configure_logging
import logging





#==================================================================================================#
#==================================================================================================#
#==================================================================================================#

# Loggerin alustus
configure_logging()
logger = logging.getLogger(__name__)


def lue_txt_url_uuidlla(uuid: str, polku: str) -> str | None:
    """
    Lukee UUID:n ja polun perusteella tekstitiedoston sisällön.
    
    Args:
        uuid (str): Tekstitiedoston UUID, esim. 'abc-123-xyz'
        polku (str): Kansion polku, jossa tiedosto sijaitsee
    
    Returns:
        str | None: Tiedoston sisältö merkkijonona, tai None jos ei löydy
    """
    try:
        tiedostopolku = Path(polku) / f"{uuid}.txt"
        print("tiedostopolku", tiedostopolku)
        if not tiedostopolku.exists():
            print(f"❌ Tiedostoa ei löytynyt: {tiedostopolku}")
            return None

        with tiedostopolku.open("r", encoding="utf-8") as tiedosto:
            sisalto = tiedosto.read()
            print(f"✅ Tiedosto luettu: {tiedostopolku}")
            return sisalto

    except Exception as e:
        print(f"❌ Virhe tiedostoa luettaessa: {e}")
        return None

#==================================================================================================#
# Lukee annetun txt-tiedoston ja palauttaa sen sisällön merkkijonona."""
def lue_txt_tiedosto(tiedostopolku: str) -> str:
    try:
        with open(tiedostopolku, "r", encoding="utf-8") as tiedosto:
            return tiedosto.read()
    except FileNotFoundError:
        logging.warning(f"Virhe: Tiedostoa '{tiedostopolku}' ei löytynyt.")
      
        return ""
    except Exception as e:
        logging.warning(f"Virhe tiedostoa luettaessa: {e}")

        return ""
    
#==================================================================================================#


#Kirjoittaa annetun tekstin tiedostoon annettuun polkuun.
#Palauttaa virheen, jos tiedostopolku ei ole kelvollinen.
def kirjoita_txt_tiedosto(sisalto: str, tiedostopolku: str):
    try:
        if not sisalto:
            raise ValueError("Virhe: Sisältö ei voi olla tyhjä.")

        # Muunnetaan tiedostopolku merkkijonoksi tarvittaessa
        tiedostopolku = str(tiedostopolku)

        if not tiedostopolku.endswith(".txt"):
            raise ValueError("Virhe: Tiedostopolun täytyy olla kelvollinen .txt-tiedosto.")

        os.makedirs(os.path.dirname(tiedostopolku), exist_ok=True)  # Luo kansiot tarvittaessa
        
        with open(tiedostopolku, "w", encoding="utf-8") as tiedosto:
            tiedosto.write(sisalto)

        #print(f"✅ Tiedosto kirjoitettu onnistuneesti: {tiedostopolku}")

    except Exception as e:
        print(f"⚠️ Virhe tiedostoa kirjoittaessa: {e}")



#==================================================================================================#


#Kirjoittaa annetun tekstin json-muodossa tiedostoon annettuun polkuun.
#Palauttaa virheen, jos tiedostopolku ei ole kelvollinen.

def kirjoita_vastaus_jsoniin(response, tiedostopolku):
    try:
        import json
        if not response.text:
            raise ValueError("Response-objekti ei sisällä tekstiä.")
        # Poistetaan mahdollinen ```json merkintä vastauksesta
        teksti = response.text.replace("```json", "").replace("```", "").strip()
        vastaus_json = json.loads(teksti)
        with open(tiedostopolku, "w", encoding="utf-8") as tiedosto:
            json.dump(vastaus_json, tiedosto, ensure_ascii=False, indent=4)
        print(f"Vastaus tallennettu JSON-tiedostoon: {tiedostopolku}")
    except Exception as e:
        print(f"Virhe JSON-tiedostoa kirjoittaessa: {e}")

#==================================================================================================#

import json

def kirjoita_json_tiedostoon(data, tiedostopolku):
    """Kirjoittaa annetun JSON-datan tiedostoon.
    
    Args:
        data (dict | list): JSON-muotoinen Python-objekti.
        tiedostopolku (str): Tiedoston polku, johon JSON tallennetaan.
    
    Returns:
        bool: True, jos kirjoitus onnistui, False jos tuli virhe.
    """
    try:
        # Luodaan tarvittavat kansiot, jos niitä ei ole
        os.makedirs(os.path.dirname(tiedostopolku), exist_ok=True)

        # Kirjoitetaan JSON-tiedostoon
        with open(tiedostopolku, "w", encoding="utf-8") as tiedosto:
            json.dump(data, tiedosto, ensure_ascii=False, indent=4)

        print(f"✅ JSON-tiedosto tallennettu: {tiedostopolku}")
        return True

    except Exception as e:
        print(f"⚠️ Virhe JSON-tiedostoa kirjoittaessa: {e}")
        return False




#==================================================================================================#


#Lukee JSON-tiedoston ja palauttaa sen Python-objektina (dict tai list).

def lue_json_tiedosto(tiedostopolku: str):
    """Lukee JSON-tiedoston ja palauttaa sen Python-objektina (dict tai list)."""
    try:
        with open(tiedostopolku, "r", encoding="utf-8") as tiedosto:
            return json.load(tiedosto)  # Muunnetaan JSON Python-objektiksi

    except FileNotFoundError:
        print(f"⚠️ Virhe: Tiedostoa '{tiedostopolku}' ei löytynyt.")
        return None  # Palautetaan None, jos tiedostoa ei ole

    except json.JSONDecodeError:
        print(f"⚠️ Virhe: Tiedosto '{tiedostopolku}' ei ole kelvollinen JSON.")
        return None

    except Exception as e:
        print(f"⚠️ Virhe tiedostoa luettaessa: {e}")
        return None


#==================================================================================================#


def tallenna_pdf_tiedosto(file, tallennuspolku):
    """
    Tallentaa ladatun PDF-tiedoston haluttuun hakemistoon.
    
    :param file: Flaskin request.files["pdf"] -objekti
    :param tallennuspolku: Merkkijono, minne tiedosto tallennetaan
    :return: Tallennetun tiedoston polku tai virheviesti
    """
    try:
        if not file:
            return "Virhe: Tiedostoa ei ladattu."

        # Varmista, että tiedosto on PDF
        if not file.filename.lower().endswith(".pdf"):
            return "Virhe: Vain PDF-tiedostot ovat sallittuja."

        # Turvallinen tiedostonimi
        tiedostonimi = secure_filename(file.filename)

        # Luo kansio, jos sitä ei ole
        os.makedirs(tallennuspolku, exist_ok=True)

        # Määritä tiedoston tallennuspolku
        tallennettu_polku = os.path.join(tallennuspolku, tiedostonimi)

        # Tallenna tiedosto
        file.save(tallennettu_polku)

        return f"Tiedosto tallennettu onnistuneesti: {tallennettu_polku}"

    except Exception as e:
        return f"Virhe tallennettaessa tiedostoa: {e}"
    


#==================================================================================================#
# **Muuta tekstiksi ja palauttaa txt-tidoston**
import fitz  # PyMuPDF

def muuta_pdf_tekstiksi(pdf_file):
    """
    Muuntaa PDF-tiedoston tekstiksi ja palauttaa sen merkkijonona.
    
    :param pdf_file: Ladattu PDF-tiedosto
    :return: PDF:n sisältämä teksti merkkijonona
    """
    try:
        with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
            return "\n".join(page.get_text() for page in doc)  # Yhdistetään sivut rivinvaihdoilla
        
    except Exception as e:
        print(f"❌ Virhe PDF:n muuntamisessa: {e}")
        return ""  # Jos virhe, palautetaan tyhjä merkkijono
    

#==================================================================================================#
# **Muuta tekstiksi ja palauttaa txt-tidoston**


def muuta_pdf_tekstiksi_ilman_tallennusta(pdf_file):
    """
    Muuntaa PDF-tiedoston tekstiksi ja palauttaa sen merkkijonona.
    
    :param pdf_file: BytesIO-tiedosto-objekti
    :return: PDF:n sisältämä teksti merkkijonona
    """
    try:
        with fitz.open(stream=pdf_file, filetype="pdf") as doc:  # Luetaan muistista
            return "\n".join(page.get_text() for page in doc)  # Yhdistetään sivut rivinvaihdoilla
        
    except Exception as e:
        print(f"❌ Virhe PDF:n muuntamisessa: {e}")
        return ""  # Jos virhe, palautetaan tyhjä merkkijono

    

#==================================================================================================#
# **Muuta tekstiksi ja palauttaa txt-tiedoston**

def muuta_pdf_tekstiksi_2(pdf_bytes):
    try:
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            return "\n".join(page.get_text() for page in doc)  # Muunnetaan kaikki sivut tekstiksi
    except Exception as e:
        print(f"❌ Virhe PDF:n muuntamisessa: {e}")
        return ""  # Jos virhe, palautetaan tyhjä merkkijono





#==================================================================================================#
# Muunnetaan ulko-ovet -json listaksi yhdenmukaisella rakenteella
def normalisoi_ulko_ovet(json_ulko_ovet):
    ovet_lista = []
    
    #print("Normalisoidaan ulko-ovet:", json_ulko_ovet)
    
    # Jos json_ulko_ovet on sanakirja, etsitään "ulko_ovet"-avain
    if isinstance(json_ulko_ovet, dict):
        json_ulko_ovet = json_ulko_ovet.get("ulko_ovet", [])
        print("Sanakirja-muodossa, ulko_ovet-avain:", json_ulko_ovet)

    # Jos json_ulko_ovet on lista, käsitellään suoraan
    if isinstance(json_ulko_ovet, list):
        for ovi_item in json_ulko_ovet:
            # Tarkistetaan, onko ovi_item sanakirja, jossa on oven tyyppi avaimena
            if isinstance(ovi_item, dict):
                for ovi_tyyppi, ovi_tiedot in ovi_item.items():
                    # Tarkistetaan, onko ovi_tiedot sanakirja
                    if isinstance(ovi_tiedot, dict):
                        ovet_lista.append({
                            "nimi": ovi_tyyppi,
                            "merkki": ovi_tiedot.get("merkki", "Ei tietoa"),
                            "malli": ovi_tiedot.get("malli", "Ei tietoa"),
                            "määrä": ovi_tiedot.get("määrä", "Ei tietoa"),
                            "lukko": ovi_tiedot.get("lukko", "Ei tietoa")
                        })
                    else:
                        # Jos ovi_tiedot ei ole sanakirja, käsitellään vanha rakenne
                        ovet_lista.append({
                            "nimi": ovi_tyyppi,
                            "määrä": "Ei tietoa",
                            "lukko": "Ei tietoa"
                        })
            # Vanha rakenne, jossa ovi on suoraan sanakirja
            elif isinstance(ovi_item, dict) and "ovi" in ovi_item:
                ovet_lista.append({
                    "nimi": ovi_item.get("ovi", "Tuntematon ovi"),
                    "määrä": ovi_item.get("määrä", "Ei tietoa"),
                    "lukko": ovi_item.get("lukko", "Ei tietoa")
                })
    
    #print("Normalisoitu lista:", ovet_lista)
    return ovet_lista

