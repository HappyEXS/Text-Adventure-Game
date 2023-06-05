# Tekstowa gra przygodowa

Jędrzejewski Jan - 15.06.2021r.

## Założenia projektu

Stworzyć oprogramowanie gry tekstowej w terminalu. Gra ma być wczytywana i zapisywana do pliku.
Gracz powinien móc poruszać się, atakować przeciwników, rozmawiać z przyjaciółmi i podnośić przedmioty.
W trakcie gry gracz wykonuje zadania, za które dostaje nagrody. W wyznaczonych momentach gracz mógłby kupować przedmioty ze sklepu.

## Opis gry

W grze wcielamy się w bohatera latającego po układzie słonecznym. Swoim statkiem może przelatywać między planetami, na których czekają go postacie, przedmioty oraz przeciwnicy do pokonania. Gracz ma do wypełnienia szereg misji po których ukończeniu orzywraca pokój w układzie słonecznym.

## Uruchomienie gry

Aby uruchomić grę należy uruchomić plik main.py za pomocą pythona
```bash
python3 main.py
```

## Podstawowe komendy gry

Aby dostać informację o wszystki komendach należy wpisać `help`. Znajdziemy tam wszystkie dostępne komendy wraz ze sposobem
ich użycia oraz wytłumaczeniem ich funkcjonalności.

## Pliki wejściowe gry

W repozytorium zamieszczono dwa przykładowe pliki gry.
`practise.json` - przykładowy plik krótkiej gry aby przetestować wszystkie funkcje gry (ok. 7minut)
`game.json` - pełny plik gry

## Wybór plików

W pliku `utilities.file_data.py` są zapisane ścieżki do plików z którymi pracuje gra.
Żeby zmienić plik nowej gry należy ustawić odpowiednią ścieżkę `DEFAULT_GAME`.
Aby wybrać plik zapisu i załadowania gry należy odpowiednio zmienić `SAVE` oraz `LOAD`.
Domyślnie po zapisaniu gry możemy od razu załadować ją z powrotem.
Należy pamiętać, że gdy zapiszemy grę jeszcze raz poprzedni plik zapisu zostanie nadpisany.
