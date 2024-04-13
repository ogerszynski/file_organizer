Przewodnik po aplikacji

Opis aplikacji:
SProsty organizator plików pozwala na automatyczne sortowanie plików w określonym katalogu według rozszerzenia pliku. Umożliwia to szybkie i efektywne przenoszenie plików do wskazanych folderów.

Jak uruchomić skrypt:

    Otwórz wiersz poleceń (Command Prompt) lub PowerShell.
    Przejdź do folderu, w którym znajduje się skrypt.
    Uruchom skrypt, wpisując python file_organizer.py.

Dostępne Komendy:

    help - Wyświetla opisy poszczególnych rozszerzeń plików.
    enter directory - Pozwala użytkownikowi na określenie katalogu i rodzaju plików, które mają być zorganizowane.
    move - Przenosi pliki do wybranego folderu na podstawie wcześniej określonych danych.
    exit - Zamyka program.

Szczegółowy Opis Komend:

    help:
        Po wpisaniu komendy help skrypt wyświetli listę rozszerzeń plików wraz z ich opisami. Przykładowo, .doc - dokument tekstowy Microsoft Word, .jpg - obraz w formacie JPEG.

    enter directory:
        Komenda enter directory pozwala użytkownikowi na wprowadzenie ścieżki do katalogu, w którym znajdują się pliki do zorganizowania oraz na podanie rozszerzenia plików, które mają być przeniesione. Skrypt sprawdzi i wyświetli listę plików pasujących do podanego rozszerzenia. Jeśli użytkownik nie wprowadzi kropki przed rozszerzeniem, skrypt automatycznie ją doda.

    move:
        Po wybraniu plików za pomocą komendy enter directory, można użyć komendy move, aby przenieść te pliki do nowego folderu. Skrypt zapyta o ścieżkę do folderu docelowego. Jeśli nie zostaną spełnione wcześniejsze warunki (określenie katalogu i typu pliku), skrypt poinformuje o konieczności wykonania komendy enter directory.

    exit:
        Komenda exit zakończy działanie programu.

Jak używać:

    Uruchom skrypt.
    Wpisz help aby zobaczyć, które rozszerzenia plików możesz zorganizować.
    Wpisz enter directory, a następnie podaj ścieżkę i rozszerzenie plików, które chcesz zorganizować.
    Wpisz move, aby przenieść pliki do nowego folderu.
    Wpisz exit, aby zakończyć działanie skryptu.
