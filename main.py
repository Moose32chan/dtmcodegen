#V1.0 Public Release - Bad but usable
#Next Update Will Fix The Copy Formatting, Add More Page Support (only works with page 1), And Add DTM4U Support
from bs4 import BeautifulSoup
import requests
import re
import pyperclip

r = requests.get("https://www.fcswap.com/game/downtown-mafia/index.php?page=1")
soup = BeautifulSoup(r.text, "html.parser")
inner_text = soup.find("tr", id="").text.strip()
pyperclip.copy(inner_text)
print ("Codes succesfully copied...")
