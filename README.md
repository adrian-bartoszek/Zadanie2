# LABORATORIUM Programowanie Full-Stack w Chmurze Obliczeniowej - zadanie nr 2

# Treść zadania
Wykorzystując opracowaną aplikację (kod + Dockerfile) z zadania nr 1 należy:\
a. zbudować, uruchomić i potwierdzić poprawność działania łańcucha Github Actions,
który zbuduje obrazy kontenera z tą aplikacją na architektury: linux/arm64/v8 oraz
linux/amd64 wykorzystując QEMU

# Prekonfiguracja
Na potrzeby laboratorium zostało zrobione:
1) wygenerowanie **Access Token** na DockerHubie
2) wygenerowanie **Access Token** na GitHubie
3) dodanie **Secrets** do repozytorium na GitHubie

# Zbudowanie obrazu kontenera - opis
Kod .github/workflows/basic.yml jest przykładem workflow'u w GitHub Actions, który buduje i wysyła obrazy kontenerów do Docker Hub. Poniżej przedstawiam komentarze dotyczące poszczególnych kroków w kodzie:

**Krok "Checkout code":** Pobiera kod źródłowy repozytorium do maszyny wirtualnej, na której wykonywany jest workflow. Używa akcji checkout@v3, która jest dostarczana przez GitHub i umożliwia pobranie kodu z bieżącego repozytorium.

**Krok "Set up QEMU":** Konfiguruje QEMU na maszynie wirtualnej. QEMU jest narzędziem do wirtualizacji, które umożliwia budowanie obrazów dla różnych architektur. Ta akcja jest używana w celu obsługi budowy obrazów dla architektury arm64.

**Krok "Set up Docker Buildx":** Konfiguruje Docker Buildx na maszynie wirtualnej. Docker Buildx jest narzędziem do budowania obrazów kontenerów w Dockerze, które obsługują wiele architektur jednocześnie. Ta akcja umożliwia budowę obrazów dla różnych architektur jednym poleceniem.

**Krok "Login to Docker Hub":** Loguje się do Docker Hub przy użyciu dostarczonych w tajemnicach (secrets) nazwy użytkownika i tokena. Ten krok jest wymagany, aby móc wysyłać obrazy kontenerów do Docker Hub.

**Krok "Build and Push for arm64":** Buduje i wysyła obraz kontenera dla architektury arm64. Wykorzystuje akcję docker/build-push-action@v3, która buduje obraz na podstawie Dockerfile znajdującego się w bieżącym katalogu (context: ./). Następnie obraz jest oznaczany tagiem adrianpollub/zadanie2:ghlab10base-arm64 i wysyłany do Docker Hub. Ten krok jest przeznaczony dla architektury arm64.

**Krok "Build and Push for amd64":** Analogicznie jak poprzedni krok, ten krok buduje i wysyła obraz kontenera dla architektury amd64. Obraz jest oznaczany tagiem adrianpollub/zadanie2:ghlab10base-amd64 i wysyłany do Docker Hub.

Workflow jest uruchamiany automatycznie przy każdym pushu na gałąź master. Jest on użyteczny, gdy chcemy zautomatyzować proces budowy i wdrażania obrazów kontenerów.

# Zrzuty ekranu

### Dodanie secretów
![alt text](https://raw.githubusercontent.com/adrian-bartoszek/Zadanie2/master/Secrets.jpg)

### Actions
![alt text](https://raw.githubusercontent.com/adrian-bartoszek/Zadanie2/master/Actions.jpg)

### DockerHub
![alt text](https://raw.githubusercontent.com/adrian-bartoszek/Zadanie2/master/DockerHub.jpg)
