# WasteWaven julkaiseminen GitHubiin

## 1. Pohjan avaaminen

Pura ZIP ja avaa pääte `WasteWave`-kansiossa. ZIP ei sisällä Git-historiaa.
Luo paikallinen repositorio:

```sh
git init -b main
git status
```

Voit julkaista pelkän pohjan, kun READMEssä säilyy tieto puuttuvasta datasta.
Älä nimeä sitä valmiiksi dataset-julkaisuksi ennen kuin tiedostot ovat ladattavissa.

## 2. Datan lisääminen

Kopioi alkuperäiset tiedostot kansioon `data/raw/`. Täydennä DATA_FORMAT.md,
metadata/dataset.json sekä data/metadata/manifest.csv todellisten tietojen perusteella.
Aluksi .gitignore estää mittaustiedostojen tahattoman lisäämisen. Poista tarvittava
`/data/raw/*`-sääntö (ja tarvittaessa processed/splits-säännöt) vasta kun olet
valmis lisäämään tiedostot. Älä käytä sokkona `git add -f`.

## 3. Suuret tiedostot ja Git LFS

Tiedostokokoja ei ole tiedossa, joten LFS-seuranta ei ole oletuksena käytössä.
GitHub estää tavallisessa Gitissä yli 100 MiB:n tiedostot ja varoittaa yli 50 MiB:n
tiedostoista. Tarkista nykyiset rajat ja LFS-tilisi tallennus- ja siirtokiintiöt.
Suurille tai usein muuttuville binääritiedostoille ota LFS käyttöön **ennen ensimmäistä
niitä sisältävää commitia**. Esimerkki, jos todelliset tiedostot ovat NPZ-muotoisia:

```sh
git lfs install
git lfs track "data/raw/**/*.npz"
git add .gitattributes
git check-attr filter -- data/raw/example.npz
```

Vaihda seurattava tiedostopääte todellista aineistoa vastaavaksi; esimerkkitiedostoa
ei ole pohjassa. `git lfs track` päivittää .gitattributes-tiedoston.
Lisää tämän jälkeen datatiedostot ja tarkista `git lfs ls-files` ennen pushia.
Jo commitoitu suuri tiedosto ei muutu LFS-tiedostoksi pelkällä track-komennolla.

Laajalle tutkimusaineistolle vaihtoehtona on erillinen data-arkisto (esim. Zenodo)
ja GitHubissa metadata, koodi sekä varmennettu latauslinkki. GitHubin automaattinen
lähdekoodi-ZIP ei välttämättä sisällä LFS-tiedostojen sisältöä: tarkista arkistoasetukset
ja testaa lataus. LFS-käyttäjä lataa datan kloonauksen jälkeen näin:

```sh
git lfs install
git lfs pull
```

## 4. Ensimmäinen commit

Valitse lisenssit LICENSE_SELECTION.md-ohjeella ennen varsinaista datajulkaisua.
Täydennä README ja tarkista lisättävät tiedostot:

```sh
python3 scripts/checksums.py
git add .
git status
git diff --cached --stat
git commit -m "Prepare WasteWave dataset repository"
```

Komento tarkistussummille tulostaa CSV:n; siirrä tiedot manifestiin ja lisää
rooli, formaatti sekä mittaus- ja kappalemäärät. Tyhjällä pohjalla tulostuu vain otsikko.

## 5. GitHub-julkaisu selaimella ja Gitillä

Kirjaudu GitHubiin ja luo uusi repositorio nimeltä `WasteWave`. Valitse haluamasi
näkyvyys. Älä luo palvelussa ylimääräistä READMEä, .gitignorea tai lisenssiä,
koska paikallinen pohja sisältää jo vastaavat ohjeet ja tiedostot.
Kopioi GitHubin näyttämä repositorion HTTPS-osoite. Korvaa alla OMA-TUNNUS
omalla käyttäjätunnuksellasi tai organisaatiollasi:

```sh
git remote add origin https://github.com/OMA-TUNNUS/WasteWave.git
git push -u origin main
```

GitHub-kirjautuminen pitää olla määritetty Gitille. Älä kirjoita salasanoja tai
käyttöoikeustunnuksia repositorion tiedostoihin.

Vaihtoehto GitHub CLI:llä, jos `gh` on asennettu:

```sh
gh auth login
gh repo create WasteWave --private --source=. --remote=origin --push
```

Valitse vain yksi julkaisumenetelmä. CLI-esimerkki luo yksityisen repositorion;
voit muuttaa sen julkiseksi GitHubissa, kun julkaisu on valmis.

## 6. Ennen varsinaista dataset-versiota

- Varmista 1 112 yksilöllistä mittausta, 97 fyysistä kappaletta ja luokkajakauma
  373/375/364, tai dokumentoi ero paperiin.
- Varmista taajuusvektori, komponenttien järjestys, yksiköt ja puuttuvat arvot.
- Tarkista lisenssitekstit, tekijät, metadata, manifesti ja latauslinkit.
- Dokumentoi muunnokset ja varmista, etteivät saman kappaleen mittaukset vuoda
  item-based-jaon osajoukosta toiseen.
- Tee puhdas kloonaus ja kokeile datan lataamista myös LFS:n kanssa.
- Lisää oikea viittaustieto ja DOI vasta kun ne on saatu. Päivitä paperin
  [repository URL], [link] ja [license] oikeilla arvoilla.
- Tee vasta tämän jälkeen datasetin versiotunniste ja GitHub Release.

## Viralliset ohjeet

Tarkistettu 5.11.2026:
- [Paikallisen repositorion julkaisu](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
- [Suurten tiedostojen rajat](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)
- [Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage)
