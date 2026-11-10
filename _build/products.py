"""Oferta Sati Heart Space: jedno źródło dla katalogu i stron sprzedażowych.

Ceny i linki muszą zgadzać się z Naffy (https://www.naffy.io/aleksander-dudek).
Po zmianie czegokolwiek tutaj uruchom:  python3 _build/build.py

Pola tekstowe to fragmenty HTML pisane ręcznie (można użyć <strong>, <a>).
`page: "legacy"` = strona sprzedażowa napisana ręcznie w swoim katalogu;
generator jej nie nadpisuje, tylko pokazuje produkt w katalogu.
"""

NAFFY = "https://www.naffy.io/aleksander-dudek/"

DISCLAIMER = (
    "Materiał ma charakter edukacyjny i nie zastępuje porady lekarza, psychologa "
    "ani fizjoterapeuty. Nie służy do diagnozowania ani leczenia chorób."
)

# Kolejność grup = kolejność na stronie głównej.
GROUPS = [
    ("teraz", "Na stres, który jest teraz",
     "Krótkie praktyki wideo: włączasz film i robisz razem z nim. Od 3 do 15 minut."),
    ("praktyka", "Na głębszą praktykę",
     "Kursy, które tłumaczą, jak i dlaczego technika działa, żebyś stosował(a) ją sam(a)."),
    ("skupienie", "Na koncentrację przy biurku",
     "Dla osób, które pracują głową i spędzają dzień przed monitorem."),
    ("indywidualnie", "Indywidualnie",
     "Gdy wolisz porozmawiać o swojej sytuacji."),
    ("wszystko", "Wszystko w jednym dostępie",
     "Subskrypcja z kursami wideo i kontaktem ze mną."),
]

PRODUCTS = [
    # ── Na stres, który jest teraz ──────────────────────────────────────
    {
        "slug": "reset-kortyzolu",
        "group": "teraz",
        "page": "generated",
        "name": "Reset kortyzolu",
        "kind": "Kurs wideo",
        "naffy": NAFFY + "reset-kortyzolu",
        "price": 17, "price_label": "17 zł", "price_note": "jednorazowo",
        "facts": ["7 sesji wideo", "ok. 6 min dziennie", "dostęp 12 miesięcy"],
        "card": "7 dni, 7 metod regulacji stresu. Około 6 minut dziennie, bez suplementów.",
        "image": "reset-kortyzolu.webp", "image_alt": "Okładka kursu Reset kortyzolu",
        "image_pos": "50% 60%",
        "badge": "Premiera",
        "lead": "Spokojniejszy układ nerwowy w 7 dni. Każdego dnia jedna krótka sesja "
                "wideo: włączasz film i oddychasz razem z kulą na ekranie.",
        "sections": [
            {"type": "text", "title": "Kiedy ciało nie schodzi z trybu alarmowego",
             "body": [
                 "Kortyzol to hormon stresu. Kiedy żyjesz w biegu, ciało rzadko dostaje "
                 "sygnał, że może zejść z trybu alarmowego. Napięte barki, płytki oddech, "
                 "głowa, która wieczorem nie chce się wyłączyć – to znajome?",
                 "„Reset kortyzolu” to 7 krótkich sesji, po jednej na każdy dzień. Animacja, "
                 "licznik i dźwięk prowadzą każdy Twój wdech i wydech, więc nie musisz "
                 "niczego pamiętać ani liczyć. Około 6 minut, z czego 5 to praktyka.",
             ]},
            {"type": "list", "title": "Co dostajesz", "items": [
                "7 prowadzonych sesji wideo – każdego dnia inna metoda regulacji stresu",
                "Prowadzenie dźwiękiem: wyższy ton to wdech, niższy to wydech – możesz ćwiczyć z zamkniętymi oczami",
                "Plan 7 dni w PDF z trackerem: zaznaczasz napięcie przed i po sesji i widzisz, co działa u Ciebie",
                "Ściągę „Który reset kiedy”: co zrobić w pracy, przed rozmową, wieczorem",
                "Tapetę na telefon ze ściągą",
                "Dostęp przez 12 miesięcy na telefonie, tablecie i komputerze",
            ]},
            {"type": "steps", "title": "7 dni, 7 metod", "label": "Dzień", "items": [
                ("Oddech przeponowy", "Fundament: wydech dłuższy niż wdech."),
                ("Cykliczne westchnienie", "Najszybszy reset w ciągu dnia."),
                ("Oddech rezonansowy", "Około 6 oddechów na minutę, dla równowagi."),
                ("Mruczenie na wydechu", "Wydłużony wydech i delikatna wibracja."),
                ("Napnij i puść", "Skrócona relaksacja progresywna dla całego ciała."),
                ("Akupresura w rytmie oddechu", "3 punkty na napięcie."),
                ("Wieczorny reset", "Twój zestaw na co dzień."),
            ]},
            {"type": "steps", "title": "Jak to działa", "items": [
                ("Włączasz sesję z danego dnia", "Około 6 minut, w tym 5 minut praktyki."),
                ("Oddychasz razem z kulą", "Rośnie przy wdechu, maleje przy wydechu."),
                ("Zaznaczasz dzień w trackerze", "Po tygodniu wybierasz ulubioną metodę i zostajesz przy niej."),
            ]},
            {"type": "list", "title": "Dla kogo", "items": [
                "Dla osób, które od tygodni żyją na wysokich obrotach",
                "Dla tych, którzy wieczorem nie potrafią się wyłączyć",
                "Dla pracujących przy biurku, którym przyda się szybki reset między zadaniami",
                "Dla początkujących – każda sesja wyjaśnia technikę od zera",
            ]},
            {"type": "text", "title": "Czego tu nie znajdziesz", "body": [
                "Tabletek, diet ani obietnic odchudzania. To prosty trening reakcji stresowej, "
                "który robisz sam(a), kilka minut dziennie. Uspokojenie zwykle czujesz od "
                "pierwszej sesji, a największą różnicę daje regularność.",
            ]},
            {"type": "faq", "title": "Najczęstsze pytania", "items": [
                ("Czy muszę znać techniki oddechowe?",
                 "Nie. Każda sesja tłumaczy technikę od zera i prowadzi Cię krok po kroku."),
                ("Czy w filmach jest lektor?",
                 "Nie – prowadzą Cię napisy, animacja i dźwięk. Po wstępie możesz zamknąć oczy."),
                ("Czym to się różni od „7 Oddechów”?",
                 "„Reset kortyzolu” to 7-dniowy program, w którym poznajesz różne metody: oddech, "
                 "mruczenie, napinanie i akupresurę. <a href=\"/7-oddechow/\">„7 Oddechów”</a> to "
                 "biblioteka sesji samych technik oddechowych do codziennej praktyki – dobry "
                 "kolejny krok po resecie."),
                ("Czy obejrzę to na telefonie?", "Tak. Najlepiej obróć telefon poziomo."),
            ]},
            {"type": "note", "title": "Ważne", "body": [
                DISCLAIMER,
                "W sesjach znajdziesz zasady bezpieczeństwa. Punktu He Gu nie uciska się "
                "w ciąży, a przy chorobach serca lub płuc pomija się zatrzymania oddechu.",
            ]},
        ],
    },
    {
        "slug": "mapa-spokoju",
        "group": "teraz",
        "page": "generated",
        "name": "Mapa spokoju",
        "kind": "Kurs wideo",
        "naffy": NAFFY + "mapa-spokoju-kurs-video-online-u0h",
        "price": 17, "price_label": "17 zł", "price_note": "jednorazowo",
        "facts": ["8 praktyk po 3 min", "3 gotowe zestawy", "dostęp 12 miesięcy"],
        "card": "8 punktów akupresury na 8 sytuacji: gonitwę myśli, nerwy, spięte barki, trudne zasypianie.",
        "image": "mapa-spokoju.webp", "image_alt": "Okładka kursu Mapa spokoju: 8 punktów akupresury",
        "lead": "Kiedy napięcie rośnie, nie zawsze masz czas na medytację. Masz za to dłonie "
                "i 3 minuty. Osiem punktów akupresury na najczęstsze chwile napięcia.",
        "sections": [
            {"type": "text", "title": "Krótki kurs na chwile napięcia", "body": [
                "„Mapa spokoju” to 8 punktów akupresury na gonitwę myśli, nerwy przed ważną "
                "rozmową, spięte barki, płytki oddech, złość czy trudne wyciszenie przed snem. "
                "Każdy punkt ma swoją 3-minutową praktykę.",
                "Najpierw animacja pokazuje, gdzie dokładnie leży punkt, a potem uciskasz go "
                "w spokojnym rytmie oddechu, który prowadzi Cię na ekranie.",
            ]},
            {"type": "list", "title": "Co dostajesz", "items": [
                "8 praktyk wideo po 3 minuty, każda na inną sytuację",
                "3 gotowe zestawy: „Przed snem”, „Dyskretnie w pracy” i „Po trudnym dniu” (4–6 minut)",
                "Ściągę PDF z całą mapą: sytuacja, punkt i jak go znaleźć",
                "Tapetę na telefon, żeby mapa była zawsze pod ręką",
                "Wyzwanie „7 dni spokoju” z dziennikiem, w którym sprawdzisz, co działa u Ciebie najlepiej",
                "Dostęp przez 12 miesięcy na telefonie, tablecie i komputerze",
            ]},
            {"type": "pairs", "title": "8 punktów na 8 sytuacji", "items": [
                ("Gonitwa myśli", "Yin Tang"),
                ("Niepokój i zasypianie", "Shen Men"),
                ("Nerwy i ścisk w żołądku", "Nei Guan"),
                ("Napięcie i ból głowy", "He Gu"),
                ("Spięte barki i kark", "Jian Jing"),
                ("Ścisk w klatce i płytki oddech", "Shan Zhong"),
                ("Złość i irytacja", "Tai Chong"),
                ("Przeciążenie i nadmiar bodźców", "Bai Hui"),
            ]},
            {"type": "figure", "image": "mapa-spokoju-punkty.webp",
             "alt": "Plansza z kursu: 8 punktów akupresury przypisanych do 8 sytuacji",
             "caption": "Cała mapa na jednej planszy – dostajesz ją też w PDF i jako tapetę."},
            {"type": "steps", "title": "Jak to działa", "items": [
                ("Wybierasz sytuację, w której teraz jesteś", ""),
                ("Włączasz 3-minutowy film", "Znajdujesz punkt razem z animacją."),
                ("Uciskasz w rytmie oddechu", "Na wdechu luzujesz nacisk, na wydechu dociskasz."),
            ]},
            {"type": "list", "title": "Dla kogo", "items": [
                "Dla osób, które chcą mieć prosty sposób na chwile napięcia w pracy, w domu i przed snem",
                "Dla zapracowanych: praktyka trwa 3 minuty i nie wymaga żadnego sprzętu",
                "Dla początkujących: nie musisz nic wiedzieć o akupresurze, wszystko widać na animacjach",
            ]},
            {"type": "note", "title": "Ważne", "body": [
                "Akupresura i oddech pomagają w chwilach napięcia, ale nie zastępują leczenia. "
                "W kursie znajdziesz zasady bezpieczeństwa i przeciwwskazania, m.in. punkty, "
                "których nie uciska się w ciąży.",
            ]},
        ],
    },
    {
        "slug": "oddech-zmieniajacy-zycie",
        "group": "teraz",
        "page": "legacy",
        "name": "Oddech, który zmienia życie",
        "kind": "Kurs wideo",
        "naffy": NAFFY + "oddech-ktory-zmienia-zycie-kurs-wideo-VyJ",
        "price": 17, "price_label": "17 zł", "price_note": "jednorazowo",
        "facts": ["5 odcinków, ok. 20 min", "3 nagrania: 5, 10 i 15 min"],
        "card": "Podstawowa technika oddechowa na reset układu nerwowego: krótki kurs i trzy nagrania z prowadzeniem.",
        "image": "oddech-zmieniajacy-zycie.svg", "image_alt": "Okładka kursu Oddech, który zmienia życie",
        "image_pos": "50% 20%",
    },
    {
        "slug": "7-oddechow",
        "group": "teraz",
        "page": "generated",
        "name": "7 Oddechów",
        "kind": "Sesje wideo",
        "naffy": NAFFY + "7-oddechow",
        "price": 55, "price_label": "55 zł", "price_note": "jednorazowo",
        "facts": ["7 sesji wideo", "ok. 8 min każda", "dostęp 12 miesięcy"],
        "card": "Gotowe sesje oddechowe: włączasz film i oddychasz. Siedem technik na różne sytuacje.",
        "image": "7-oddechow.webp", "image_alt": "Okładka: 7 Oddechów, prowadzone sesje oddechowe wideo",
        "badge": "Nowość",
        "lead": "Włączasz film. Oddychasz. Tyle. Animacja, licznik i dźwięk prowadzą każdy "
                "wdech i wydech, więc nie musisz pamiętać, ile sekund wdechu ani jak długo wydychać.",
        "sections": [
            {"type": "text", "title": "Oddychanie zamiast liczenia w głowie", "body": [
                "Wiesz, że oddech potrafi uspokoić. Ale kiedy przychodzi stres, nie pamiętasz, "
                "ile sekund wdechu, czy zatrzymać powietrze i jak długo wydychać. Kończy się na "
                "liczeniu w głowie zamiast na oddychaniu.",
                "„7 Oddechów” rozwiązuje to w najprostszy sposób: film prowadzi Cię od początku "
                "do końca.",
            ]},
            {"type": "list", "title": "Co dostajesz", "items": [
                "7 prowadzonych sesji wideo (ok. 8 min każda, w tym 4–5 min praktyki)",
                "Bezpieczne wprowadzenie i wyciszenie w każdej sesji",
                "Prowadzenie dźwiękiem – możesz ćwiczyć z zamkniętymi oczami",
                "Bonus: ściągę PDF „Który oddech kiedy” i zasady bezpieczeństwa",
                "Dostęp na 12 miesięcy – na komputerze i telefonie",
            ]},
            {"type": "techniques", "title": "7 sprawdzonych technik", "items": [
                ("Oddech przeponowy", "wdech 4 s · wydech 6 s",
                 "Na co dzień, przed snem i w chwilach napięcia. Od tej sesji warto zacząć."),
                ("Oddech pudełkowy", "4 · 4 · 4 · 4 s",
                 "Przed wystąpieniem, egzaminem lub trudną rozmową – gdy potrzebujesz jasnej głowy."),
                ("Oddech 4-7-8", "wdech 4 s · zatrzymanie 7 s · wydech 8 s",
                 "Wieczorem przed snem i gdy trudno Ci się wyciszyć po intensywnym dniu."),
                ("Oddech rezonansowy", "wdech 5,5 s · wydech 5,5 s",
                 "Codziennie po 5 minut – dla równowagi. Po pracy, przed snem lub przed ważnym zadaniem."),
                ("Cykliczne westchnienie", "wdech 2,5 s + 1 s · wydech 6,5 s",
                 "Gdy narasta stres – już 1–3 westchnienia działają szybko."),
                ("Oddychanie naprzemienne", "wdech 4 s · wydech 6 s, na zmianę stron",
                 "Przed medytacją, nauką lub pracą wymagającą skupienia."),
                ("Oddech przez zasznurowane usta", "wdech 3 s · wydech 6 s",
                 "Przy zadyszce i wysiłku, np. na schodach, oraz gdy oddech przyspiesza z nerwów."),
            ]},
            {"type": "figure", "image": "7-oddechow-kula.webp",
             "alt": "Ekran sesji: kula oddechu, odliczanie sekund i licznik cykli",
             "caption": "Kula rośnie przy wdechu i maleje przy wydechu. Na dole licznik cykli i pozostały czas."},
            {"type": "steps", "title": "Jak wygląda każda sesja", "items": [
                ("Wstęp", "Czym jest technika i jak działa – w prostych słowach."),
                ("Bezpieczeństwo", "Kiedy ćwiczyć, kiedy przerwać i kiedy skonsultować się z lekarzem."),
                ("Przygotowanie", "Pozycja, ułożenie dłoni i kilka swobodnych oddechów."),
                ("Praktyka 4–5 min", "Kula, licznik i dźwięk prowadzą każdy wdech i wydech."),
                ("Wyciszenie", "Spokojny powrót do naturalnego oddechu."),
            ]},
            {"type": "list", "title": "Dla kogo", "items": [
                "Masz dość aplikacji, w których trzeba liczyć w głowie – chcesz po prostu włączyć i oddychać",
                "Pracujesz przy biurku i potrzebujesz szybkiego resetu między zadaniami",
                "Wieczorem trudno Ci się wyciszyć albo zasnąć",
                "Znasz techniki oddechowe z teorii, ale brakuje Ci regularnej praktyki",
                "Chcesz zadbać o układ nerwowy w kilka minut dziennie – bez medytacji i wizualizacji",
            ]},
            {"type": "list", "title": "Bezpieczeństwo jest wbudowane",
             "intro": "Techniki są łagodne i dobrze opisane – bez hiperwentylacji i forsownych "
                      "metod. Każda sesja zaczyna się od zasad bezpieczeństwa:",
             "items": [
                "Ćwicz siedząc lub leżąc – nigdy w wodzie, podczas jazdy ani obsługi maszyn",
                "Oddychaj łagodnie. Komfort jest ważniejszy niż liczby",
                "Przerwij, jeśli poczujesz zawroty głowy, mrowienie, duszność, ból w klatce piersiowej lub narastający niepokój",
                "Przy chorobie serca lub płuc, padaczce, nieuregulowanym nadciśnieniu albo w ciąży pomiń zatrzymania oddechu i skonsultuj praktykę z lekarzem",
            ]},
            {"type": "faq", "title": "Najczęstsze pytania", "items": [
                ("Czy muszę znać techniki oddechowe?",
                 "Nie. Każda sesja tłumaczy technikę od zera. Jeśli zaczynasz, włącz najpierw Oddech przeponowy."),
                ("Czy w filmach jest lektor?",
                 "Nie – prowadzą Cię napisy, animacja i dźwięk. Wyższy ton to wdech, niższy to wydech, "
                 "więc po wstępie możesz zamknąć oczy."),
                ("Czy obejrzę to na telefonie?",
                 "Tak. Filmy są poziome (Full HD), a teksty są duże i czytelne także na smartfonie."),
                ("Jak często ćwiczyć?",
                 "Najwięcej daje regularność – wystarczy jedna sesja dziennie. Ściąga PDF podpowie, "
                 "którą technikę wybrać w danej sytuacji."),
                ("Czym to się różni od kursu „Techniki oddechowe na każdą okazję”?",
                 "<a href=\"/techniki-oddechowe/\">Kurs</a> uczy – wyjaśnia mechanizmy i dobór technik. "
                 "„7 Oddechów” to gotowe sesje do codziennej praktyki: włączasz i oddychasz. "
                 "Dobrze się uzupełniają."),
                ("Jak długo mam dostęp?", "Przez 12 miesięcy od zakupu, w Panelu Klienta."),
            ]},
            {"type": "note", "title": "Ważne", "body": [DISCLAIMER]},
        ],
    },
    # ── Na głębszą praktykę ─────────────────────────────────────────────
    {
        "slug": "jak-wlaczyc-luz",
        "group": "praktyka",
        "page": "generated",
        "name": "Jak włączyć luz i wyłączyć napięcie w każdym momencie",
        "short": "Jak włączyć luz i wyłączyć napięcie",
        "kind": "Kurs wideo",
        "naffy": NAFFY + "jak-wlaczyc-luz-i-wylaczyc-napiecie-w-kazdym-momencie-yzT",
        "price": 170, "price_label": "170 zł", "price_note": "jednorazowo",
        "facts": ["nerw błędny od podstaw"],
        "card": "Kurs o pracy z nerwem błędnym – od zera do metod, które stosujesz na co dzień.",
        "image": "jak-wlaczyc-luz.webp", "image_alt": "Okładka kursu Jak włączyć luz i wyłączyć napięcie w każdym momencie",
        "lead": "Kurs o pracy z nerwem błędnym. Prowadzi od zera do wdrożenia różnych metod, "
                "którymi uspokajasz układ nerwowy na co dzień.",
        "sections": [
            {"type": "text", "title": "Dlaczego nerw błędny", "body": [
                "Nerw błędny działa jak fizjologiczny łącznik między ciałem a umysłem. Pomaga "
                "czuć się bezpiecznie, nawiązywać więzi i zarządzać emocjami w kontakcie "
                "z innymi ludźmi.",
                "W kursie poznajesz go od podstaw, a potem krok po kroku wdrażasz metody pracy "
                "z nim, które możesz stosować samodzielnie.",
            ]},
            {"type": "note", "title": "Ważne", "body": [DISCLAIMER]},
        ],
    },
    {
        "slug": "emocjonalna-blogosc",
        "group": "praktyka",
        "page": "legacy",
        "name": "Emocjonalna błogość w 15 minut",
        "kind": "Kurs online",
        "naffy": NAFFY + "emocjonalna-blogosc-w-15-minut-kurs-online-fpY",
        "price": 280, "price_label": "280 zł", "price_note": "jednorazowo",
        "facts": ["świadomy dotyk i akupresura", "dostęp 6 miesięcy"],
        "card": "Świadomy dotyk i akupresura: rozładowujesz napięcie samymi dłońmi, w biurze, w domu, w podróży.",
        "image": "emocjonalna-blogosc.webp", "image_alt": "Okładka kursu Emocjonalna błogość w 15 minut",
        "image_pos": "50% 35%",
    },
    {
        "slug": "techniki-oddechowe",
        "group": "praktyka",
        "page": "generated",
        "name": "Techniki oddechowe na każdą okazję",
        "kind": "Kurs wideo",
        "naffy": NAFFY + "techniki-oddechowe-na-kazda-okazje-kurs-online-D3Z",
        "price": 350, "price_label": "350 zł", "price_note": "jednorazowo",
        "facts": ["16 filmów wyjaśniających", "technika: 5–15 min", "dostęp 6 miesięcy"],
        "card": "Technika oddechowa dobrana do sytuacji: stres przed wydarzeniem, bezsenność, zmęczenie.",
        "image": "techniki-oddechowe.webp", "image_alt": "Okładka kursu Techniki oddechowe na każdą okazję",
        "lead": "Nie możesz zasnąć o 23:00, choć jesteś wykończony(-a)? Serce wali przed "
                "prezentacją? Dostajesz technikę oddechową dobraną do sytuacji – i wiesz, "
                "dlaczego działa.",
        "sections": [
            {"type": "text", "title": "To nie charakter. To oddech", "body": [
                "Przez większość dnia oddychamy płytko i chaotycznie. Dla układu nerwowego to "
                "sygnał: włącz tryb alarmowy i nie wyłączaj go.",
                "Ten kurs uczy, jak to odwrócić. Zero medytacji, zero „wyciszania umysłu”: "
                "oddychasz zgodnie z instrukcją, a ciało reaguje. Techniki bazują na badaniach.",
            ]},
            {"type": "techniques", "title": "Techniki do zastosowania", "items": [
                ("Przed stresującym wydarzeniem", "5–10 min", "Technika używana przez siły specjalne."),
                ("Na bezsenność i gonitwę myśli", "10–15 min", ""),
                ("Mentalny reset", "5–10 min", "Gdy głowa potrzebuje świeżego startu."),
                ("Energia przy zmęczeniu", "5–15 min", "Technika dla zaawansowanych."),
                ("Głęboka oksygenacja i uwolnienie napięcia", "5–10 min", ""),
            ]},
            {"type": "list", "title": "Co dostajesz", "items": [
                "16 filmów wyjaśniających (ok. 30 min): wprowadzenie, pełna sekcja bezpieczeństwa, mechanizm działania i przeciwwskazania",
                "Prowadzone techniki oddechowe do praktyki, każda na inną sytuację",
                "Dokumentację pisemną: scenariusze, bibliografię i linki do badań",
                "Dostęp na 6 miesięcy",
            ]},
            {"type": "text", "title": "A może wolisz same sesje?", "body": [
                "Ten kurs uczy: wyjaśnia mechanizmy i dobór technik. Jeśli chcesz tylko włączyć "
                "film i oddychać, zobacz <a href=\"/7-oddechow/\">„7 Oddechów”</a> – gotowe "
                "sesje do codziennej praktyki. Dobrze się uzupełniają.",
            ]},
            {"type": "note", "title": "Bezpieczeństwo najpierw", "body": [
                "Każda technika ma pełne instrukcje bezpieczeństwa i przeciwwskazania.",
                DISCLAIMER,
            ]},
        ],
    },
    # ── Na koncentrację przy biurku ─────────────────────────────────────
    {
        "slug": "mistrz-koncentracji",
        "group": "skupienie",
        "page": "legacy",
        "name": "Stań się mistrzem koncentracji i stanu flow",
        "kind": "E-book · wydanie 2.1",
        "naffy": NAFFY + "stan-sie-mistrzem-koncentracji-i-stanu-flow-fg7-4MsN",
        "price": 55, "price_label": "55 zł", "price_note": "jednorazowo",
        "facts": ["84 strony PDF", "+ 3 instrukcje wideo"],
        "card": "System budowania koncentracji od fundamentów: sen, oddech, odżywianie, nerw błędny, rozproszenia.",
        "image": "mistrz-koncentracji.webp", "image_alt": "Okładka e-booka Stań się mistrzem koncentracji i stanu flow",
        "badge": "Bestseller",
    },
    {
        "slug": "laserowa-koncentracja",
        "group": "skupienie",
        "page": "generated",
        "name": "Laserowa koncentracja. Spokojna głowa. Lepsze samopoczucie",
        "short": "Laserowa koncentracja",
        "kind": "Kurs wideo · v3",
        "naffy": NAFFY + "laserowa-koncentracja-spokojna-glowa-lepsze-samopoczucie-v3-7D6",
        "price": 280, "price_label": "280 zł", "price_note": "jednorazowo",
        "facts": ["poniżej 99 minut", "wideo, audio i slajdy PDF", "dostęp 6 miesięcy"],
        "card": "Dla pracujących przy biurku: mikronawyki i krótkie ćwiczenia na skupienie, plecy i sen.",
        "image": "laserowa-koncentracja.webp", "image_alt": "Okładka kursu Laserowa koncentracja",
        "image_pos": "30% 50%",
        "lead": "Praca siedząca potrafi osłabić koncentrację, zniechęcać i utrudniać sen. "
                "W mniej niż 99 minut poznajesz mikronawyki i krótkie zestawy ćwiczeń, które "
                "wdrożysz od razu, bez rewolucji w grafiku.",
        "sections": [
            {"type": "text", "title": "Dla kogo jest ten kurs", "body": [
                "Pracujesz przy komputerze? Przy kilku monitorach? Jesteś programistą, "
                "księgową, analitykiem? Długie godziny przy ekranie obniżają skupienie, zwiększają "
                "irytację, a ciało daje o sobie znać, np. bólem pleców. Pojawia się też "
                "trudność z zasypianiem.",
                "Kurs przekazuje tylko najważniejsze wskazówki, oparte na metodach naukowych. "
                "Minimum teorii, maksimum kroków, które od razu włączasz do dnia.",
            ]},
            {"type": "topics", "title": "Co jest w kursie", "items": [
                ("Wyzwania pracy siedzącej",
                 "Nazywasz, co realnie dzieje się w Twoim dniu przy biurku, i widzisz możliwe "
                 "przyczyny. Łatwiej wtedy wybrać działania, które mają sens."),
                ("Mikronawyki",
                 "Niewielkie, powtarzalne działania połączone z codziennymi momentami w pracy. "
                 "Często wystarczy 10–15 świadomych minut, żeby wesprzeć jakość pracy."),
                ("Ćwiczenia na osłabione mięśnie",
                 "Proste zestawy ruchów, które aktywują partie zaniedbywane przy długim "
                 "siedzeniu, m.in. pośladki i plecy. Krótkie sekwencje na przerwy w pracy."),
                ("Koncentracja i sen",
                 "Co sprzyja skupieniu podczas pracy i jakie proste techniki stosować wieczorem, "
                 "żeby łatwiej zasnąć i przygotować się do następnego dnia."),
            ]},
            {"type": "list", "title": "Forma kursu", "items": [
                "Mniej niż 99 minut skondensowanego materiału",
                "Oglądasz na komputerze lub telefonie albo słuchasz jak podcastu",
                "Slajdy w pliku PDF",
                "Inspiracje: fizjoterapia, praca z ciałem (m.in. koncepcje Lowena), joga i publikacje naukowe",
                "Dostęp na 6 miesięcy",
            ]},
            {"type": "note", "title": "Ważne", "body": [DISCLAIMER]},
        ],
    },
    # ── Indywidualnie ───────────────────────────────────────────────────
    {
        "slug": "konsultacja",
        "group": "indywidualnie",
        "page": "generated",
        "name": "Konsultacja online lub na miejscu",
        "kind": "Spotkanie 1:1",
        "naffy": NAFFY + "konsultacja-online-lub-fizycznie-zJj",
        "price": 350, "price_label": "350 zł", "price_note": "za spotkanie",
        "facts": ["55–90 minut", "Google Meet lub na miejscu", "voucher ważny 90 dni"],
        "card": "Rozmowa 1:1 o samopoczuciu, pracy przy biurku, zarobkach w IT albo AI w pracy.",
        "image": "konsultacja.webp", "image_alt": "Aleksander Dudek",
        "image_pos": "50% 30%",
        "after_buy": "Po zakupie ustalamy termin spotkania.",
        "lead": "Rozmowa 1:1 online przez Google Meet albo na miejscu, po wcześniejszym "
                "umówieniu. Od 55 do 90 minut, zależnie od tego, czego potrzebujesz.",
        "sections": [
            {"type": "list", "title": "W czym mogę pomóc", "items": [
                "Samopoczucie, zdrowie i jakość codziennego życia w oparciu o metody naukowe: biohacking, neurohacking, elementy fizjoterapii i treningu",
                "Lepsze funkcjonowanie przy pracy biurowej, przed monitorami, w każdej formie",
                "Wyższe zarobki w IT jako programista lub specjalista techniczny: trzy strategie (ekspert, partner biznesowy, multitasker) dopasowane do Twojej sytuacji, szablony rozmowy o podwyżkę i oceny miejsca pracy, poduszka finansowa, IP Box",
                "Dodatkowe źródło dochodu bez porzucania obecnej pracy – na etacie i na B2B, w każdej branży",
                "Wszechstronne korzystanie z AI w pracy programisty, marketingowca czy analityka",
                "Klasyczny coaching z elementami mentoringu (business i life)",
            ]},
            {"type": "steps", "title": "Jak to wygląda", "items": [
                ("Kupujesz voucher na Naffy", "Jest imienny i ważny 90 dni od złożenia zamówienia."),
                ("Ustalamy termin", ""),
                ("Spotykamy się", "Online przez Google Meet albo na miejscu, które wskażę. 55–90 minut."),
            ]},
            {"type": "list", "title": "Najważniejsze zasady", "items": [
                "Termin możesz przenieść, jeśli odwołasz spotkanie najpóźniej 7 dni wcześniej i w ciągu 90 dni od zamówienia",
                "Późniejsze odwołanie albo nieobecność bez uprzedzenia oznacza, że konsultacja jest zrealizowana",
                "Spóźnienie wlicza się w czas spotkania. Jeśli to ja się spóźnię, przedłużamy spotkanie albo przenosimy termin",
                "Zwrot pieniędzy dostajesz, gdy konsultacja się nie odbyła: zgłoś to mailowo lub telefonicznie najpóźniej 7 dni od ustalonego terminu (i w ciągu 90 dni od zamówienia). Zwrot należy się też, gdy spotkanie nie odbyło się z mojej winy",
             ],
             "outro": "Pełny regulamin konsultacji jest na stronie produktu na Naffy."},
        ],
    },
    # ── Wszystko w jednym ───────────────────────────────────────────────
    {
        "slug": "tylko-luz-nas-uratuje",
        "group": "wszystko",
        "page": "legacy",
        "name": "Tylko Luz Nas Uratuje",
        "kind": "Subskrypcja",
        "naffy": NAFFY + "tylko-luz-nas-uratuje-fYr",
        "price": 44.99, "price_label": "44,99 zł", "price_note": "miesięcznie",
        "facts": ["7 kursów wideo", "pytania do mnie", "anulujesz, kiedy chcesz"],
        "card": "Wszystkie kursy wideo w jednym dostępie miesięcznym, z możliwością zadawania mi pytań.",
        "image": "tylko-luz-nas-uratuje.webp", "image_alt": "Aleksander Dudek – ilustracja subskrypcji Tylko Luz Nas Uratuje",
        # Na Naffy: „Produkt obecnie niedostępny” + lista oczekujących (stan na 2026-11-10).
        "waitlist": True,
    },
]
