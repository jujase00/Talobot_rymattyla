#from pathlib import Path
import sys
import os
from pathlib import Path

#Lisää juurikansio Pythonin moduulihakemistoon
sys.path.append(os.path.abspath("."))
#sys.path.append(os.path.abspath("utils"))
#sys.path.append(os.path.abspath("api_kyselyt"))



# Määritä peruskansio, jossa data sijaitsee
BASE_DIR = Path(__file__).parent  # Tämä varmistaa, että polut ovat suhteellisia skriptiin

# Data-kansio
S_DIR = BASE_DIR / "data" / "s"
K_DIR = BASE_DIR / "data" / "k"
DATA_DIR = BASE_DIR / "data"


# TXT- JA JSON-tiedostojen polut
IKKUNA2_JSON = S_DIR / "ikkuna2.json"
VALIOVITYYPIT_TXT = S_DIR / "valiovityypit.txt"
TOIMITUSSISALTO_KOKONAISUUDESSA_TXT = S_DIR / "toimitussisalto_kokonaisuudessa_tekstina.txt"
ULKO_OVI_TIEDOT_KOKONAISUUDESSA_TXT = S_DIR / "ulko_ovi_tiedot_kokonaisuudessa.txt"
VALIOVI_TIEDOT_KOKONAISUUDESSA_TXT = S_DIR / "valiovi_tiedot_kokonaisuudessa.txt"
IKKUNATIEDOT_KOKONAISUUDESSA_TXT = S_DIR / "ikkunatiedot_kokonaisuudessa.txt"
IKKUNA_JSON = S_DIR / "ikkuna.json"
PUHDISTETTU_TOIMITUSSISALTO_TXT = S_DIR / "puhdistettu_toimitussisalto.txt"
ULKO_OVI_TIEDOT_2_JSON = S_DIR / "ulko_ovi_tiedot_2.json"
#ULKO_OVI_TIEDOT_JSON = S_DIR / "ulko_ovi_tiedot.json"
TEMP_1_TXT = S_DIR / "temp_1.txt"
TOIMITUSSISALTO_TXT = DATA_DIR / "toimitussisalto.txt"
TOIMITUSSISALTO_SIEVITALO_TXT = DATA_DIR / "toimitussisalto_sievitalo.txt"
TOIMITUSSISALTO_KASTELLI_TXT = DATA_DIR / "toimitussisalto_kastelli.txt"



IKKUNATIEDOT_KASTELLI_KOKONAISUUDESSA_TXT = K_DIR / "ikkunatiedot_kastelli_kokonaisuudessa.txt"
IKKUNA_KASTELLI_JSON = K_DIR / "ikkuna_kastelli.json"
IKKUNA_KASTELLI_JSON_2 = K_DIR / "ikkuna_kastelli_json_2.json"
PUHDISTETTU_TOIMITUSSISALTO_KASTELLI_TXT = K_DIR / "puhdistettu_toimitussisalto_kastelli.txt"

GEMINI_API_KEY = "AIzaSyADY6K_HFjgeyjr3IHHoY5UmK6hSoG_RYg"

PROMPT_SIEVITALO_POIMI_IKKUNATIEDOT_TXT = S_DIR / "prompt_sievitalo_poimi_ikkunatiedot.txt"
PROMPT_SIEVITALO_RYHMITELLE_VALITUT_IKKUNATIEDOT_JSON_MUOTOON = S_DIR / "prompt_sievitalo_ryhmittele_valitut_ikkunatiedot_json_muotoon.txt"
PROMPT_SIEVITALO_POIMI_VALIOVITIEDOT_TXT = S_DIR / "prompt_sievitalo_poimi_valiovitiedot.txt"
PROMPT_SIEVITALO_POIMI_ULKO_OVI_TIEDOT_TXT = S_DIR / "prompt_sievitalo_poimi_ulko_ovi_tiedot.txt"
PROMPT_SIEVITALO_ANNA_VALIOVIMALLIT_TXT = S_DIR / "prompt_sievitalo_anna_valiovimallit.txt"
PROMPT_SIEVITALO_ULKO_OVI_TIEDOT_JSON_MUOTOON = S_DIR / "prompt_sievitalo_ulko_ovi_tiedot_json_muotoon.txt"

PROMPT_KASTELLI_POIMI_IKKUNATIEDOT_TXT = K_DIR / "prompt_kastelli_poimi_ikkunatiedot.txt"
PROMPT_KASTELLI_RYHMITELLE_VALITUT_IKKUNATIEDOT_JSON_MUOTOON = K_DIR / "prompt_kastelli_ryhmittele_valitut_ikkunatiedot_json_muotoon.txt"
PROMPT_KASTELLI_POIMI_VALIOVITIEDOT_TXT = K_DIR / "prompt_kastelli_poimi_valiovitiedot.txt"
PROMPT_KASTELLI_POIMI_ULKO_OVI_TIEDOT_TXT = K_DIR / "prompt_kastelli_poimi_ulko_ovi_tiedot.txt"
PROMPT_KASTELLI_ANNA_VALIOVIMALLIT_TXT = K_DIR / "prompt_kastelli_anna_valiovimallit.txt"
PROMPT_KASTELLI_ULKO_OVI_TIEDOT_JSON_MUOTOON = K_DIR / "prompt_kastelli_ulko_ovi_tiedot_json_muotoon.txt"
   
