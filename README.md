# Home-eBook-Library
This is Django based project for home usage only. It allows family members to save their eBooks on local server and make its own eBook database.

# CZ manual k instalaci a spuštění Djanga
1. Otevři si příkazovou řádku klávesovou zkratkou Win+R a vepiš příkaz
```cmd```
Pomocí příkazů 
```cd název-složky``` se dostaň na úroveň Django projektu.
Výpis šložky, abys viděla, co je v ní, se dělá příkazem
```dir```. O úroveň výš se dostaneš příkazem ```cd ..```
3. Vytvoř virtuální prostředí příkazem. Já ho mám o úroveň výš než je soubor manage.py.
```python -m venv env```. Aktivaci virtuálního prostředí provedeš příkazem ```env\Scripts\activate```.
4. Pokud nejsi na stejné úrovni jako soubor manage.py, tak se tam přesuň. Naistaluješ si potřebné knihovny pro Python příkazem ```pip install -r requirements.txt```.
5. No a teď by měl jít spustit web. V příkazové řádce prověď příkaz ```python manage.py runserver```.
6. Ve webovém prohlížeči napiš adresu ```127.0.0.1:8000``` a nebo ```localhost:8000```.


```python.exe -m pip install --upgrade pip``` upgrade pythonu

```cd /d V:\``` změna disku

```ctr + c```  vypnout server a pak shift + šipka hore

# Práce s gitem
## Poslat úpravy na github:
```git add .```
```git commit -m "komentář"```
```git push origin master```

## Stáhnout z githubu:
```git pull origin master```



# Clonování - VS a GitHub

1. Nainstalujeme si GIT a VS code pokud ještě nemáme. Taky budeme potřebovat účet na GitHubu.
2. Vybereme si složku, kam chceme vložit nový repozitář, na klávesnici stikneme SHIFT a na myši stikneme pravé tlačítko. Rozbalí se nám menu a vybereme ```Open Git Bash here``` a otevře se příkazový řádek GITu.
3. Najdeme si na GitHubu repozitář, který chceme naklonovat, klikneme na zelený tlačítko CODE a v local skopírujeme odkaz na repozitář.
4. Přejdeme zpátky na příkazový řádek Gitu, napíšeme ```git clone``` a složíme pomocí ```SHIFT + INSERT``` odkaz.
5. Vytvořila se složka tam, kde jsme ji chtěli. 
6. Vrátíme se zpátky na příkazový řádek Gitu, napíšeme ```cd MojeSložka``` a stiskneme enter.
7. Dále napíšeme ```code .``` a zase enter.
8. Otevře se VS s aktuální složkou, na které chceme pracovat.

- musíte být přihlášeni na VS studiu do GitHubu, aby se vám propisoval repozitář, což uděláte vlevo dole pod ikonou postavičky<br>
![Obrázek postavičky](https://i.ibb.co/kHPcsM7/02.png)
- aby jste mohli změněné soubory posílat na GitHub, přejdete na levém panelu na ikonu 
![Obrázek ikony](https://i.ibb.co/MMz6gnQ/01.png)
