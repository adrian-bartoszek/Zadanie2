# LABORATORIUM Programowanie Full-Stack w Chmurze Obliczeniowej - zadanie nr 1

# Zrzut ekranu przedstawiający działanie aplikacji
![alt text](https://github.com/adrian-bartoszek/Zadanie1/blob/main/screenshot.jpg?raw=true)

# Zbudowanie obrazu kontenera
```docker build -t moj-kontener:1.0 .```

# Uruchomienie kontenera na podstawie zbudowanego obrazu
```docker run -p 5000:5000 -e PORT=5000 -e HOST_PORT=5000 moj-kontener:1 python server.py```

# Sposób uzyskania informacji wygenerowanych przez serwer podczas uruchamiania kontenera
Kod źródłowy używa funkcji os.environ.get() do pobrania wartości zmiennych środowiskowych PORT i HOST_PORT.
Kontener jest zbudowany i uruchomiony, przekazując zmienne środowiskowe PORT i HOST_PORT:\
```docker run -p 5000:5000 -e PORT=5000 -e HOST_PORT=5000 moj-kontener:1 .```

# Sprawdzenie ilości warstw zbudowanego obrazu
```docker image inspect <nazwa_obrazu>```

# Dodatkowe informacje
Funkcja get_user_ip():
Ta funkcja wykonuje żądanie GET do witryny "https://ipapi.co/ip/" w celu uzyskania adresu IP użytkownika.
Zwraca tekstową odpowiedź z żądania, pozbawioną białych znaków.

Funkcja get_user_timezone(ip_address): 
Ta funkcja przyjmuje jako argument ip_address, który jest adresem IP użytkownika.    
Tworzy URL na podstawie podanego ip_address, używając go do zapytania o strefę czasową użytkownika.
WWykonuje żądanie GET do utworzonego URL.
Zwraca tekstową odpowiedź z żądania, pozbawioną białych znaków.

Obie funkcje wykorzystują moduł requests, aby wykonywać żądania HTTP. Pierwsza funkcja pobiera adres IP użytkownika, a druga funkcja na podstawie tego adresu IP pobiera strefę czasową użytkownika.

# Healthcheck
Aplikacja posiada funkcjonalność health check. Pierwsza część kodu instaluje zależność curl przy użyciu polecenia systemowego apt-get. Curl jest narzędziem, które umożliwia wykonywanie żądań HTTP wewnątrz kontenera.\
```docker inspect --format='{{json .State.Health}}' <id>```

Używając polecenia curl, kontener regularnie sprawdza dostępność serwera pod adresem http://localhost:5000/health. Jeśli żądanie nie zwróci sukcesu (kod HTTP różny od 2xx), to health check zwróci wartość 1, co oznacza, że kontener jest w złym stanie. Jest to przydatne narzędzie do monitorowania stanu kontenera i zapewnienia jego niezawodności.




