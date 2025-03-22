world = {
    "Wioska Elfów": {
        "desc": "Piękne domy na drzewach migoczą milionami świetlistych kryształów. W powietrzu unosi się delikatna melodia harf i fletów, a śpiew elfickich bardów rozbrzmiewa wśród liści. Powietrze pachnie jaśminem i sosną. To miejsce wydaje się niemal nierealne, jakby stworzone z czystej magii.",
        "options": {"n": "Mglisty Las", "e": "Rzeka Przeznaczenia"},
        "npcs": {
            "Ailith Świetlista": "Elficka bardka, która gra na harfie i opowiada historie o dawnych czasach.",
            "Lorien Zielonooki": "Strażnik wioski, zawsze czujny, ale przyjazny dla podróżnych.",
        },
        "items": {
            "Amulet Leśnego Światła": "Migoczący naszyjnik, który rozświetla ciemność delikatnym zielonym blaskiem.",
            "Liść Szepczącego Dębu": "Po przyłożeniu do ucha słychać porady mądrych duchów lasu.",
        },
    },
    "Mglisty Las": {
        "desc": "Drzewa w tym lesie są wysokie i smukłe, ich korony znikają w gęstej, mlecznej mgle. Każdy krok wydaje się tłumiony, a cisza, zamiast uspokajać, wzmaga niepokój. Coś przemyka między drzewami – czy to cień, czy może tylko złudzenie? W głębi lasu czuć pradawną, pierwotną moc.",
        "options": {"s": "Wioska Elfów", "w": "Stara Wieża"},
        "npcs": {},
        "items": {},
    },
    "Rzeka Przeznaczenia": {
        "desc": "Rzeka o kryształowo czystej wodzie leniwie płynie wśród bujnej roślinności. Mówi się, że każdy, kto spojrzy w jej nurt, ujrzy odbicie swej przyszłości. Woda lśni tajemniczym blaskiem, a jej szmer zdaje się być szeptem pradawnych duchów.",
        "options": {"w": "Wioska Elfów", "e": "Złoty Most", "s": "Bagna Zapomnienia"},
        "npcs": {},
        "items": {},
    },
    "Złoty Most": {
        "desc": "Stary, kamienny most rozciąga się nad rwącą rzeką. Jego balustrady są zdobione wytłoczonymi w złocie runami, które błyszczą nawet w ciemności. Mówi się, że most jest strażnikiem starożytnych tajemnic i przechodzą przez niego tylko ci, którzy są godni.",
        "options": {"w": "Rzeka Przeznaczenia", "e": "Królestwo Krasnoludów"},
        "npcs": {},
        "items": {},
    },
    "Bagna Zapomnienia": {
        "desc": "Rozległe, mgliste bagna rozciągają się po horyzont. Woda jest gęsta i czarna jak atrament. W powietrzu unosi się zapach gnijących liści i dziwne szepty, które wydają się pochodzić znikąd. Każdy, kto tu wejdzie, zaczyna tracić wspomnienia.",
        "options": {"n": "Rzeka Przeznaczenia", "s": "Cmentarzysko Bohaterów"},
        "npcs": {},
        "items": {},
    },
    "Cmentarzysko Bohaterów": {
        "desc": "Starożytne nagrobki porośnięte bluszczem wznoszą się na wzgórzu. Kamienne pomniki przedstawiają postacie w pełnym uzbrojeniu, jakby gotowe do ostatniej bitwy. Wiatr świszcze między płytami, niosąc ciche szepty dawnych wojowników.",
        "options": {"n": "Bagna Zapomnienia", "s": "Ruiny Zamku Cieni"},
        "npcs": {},
        "items": {},
    },
    "Ruiny Zamku Cieni": {
        "desc": "Mroczne, opuszczone ruiny dawnego zamku. Jego wieże są poszarpane, a ściany pokryte pnączami. W ciemnych zakamarkach wciąż czai się pradawna magia. Każdy, kto przekroczy próg ruin, czuje zimny dotyk czegoś nienamacalnego.",
        "options": {"n": "Cmentarzysko Bohaterów", "w": "Zatopione Katakumby"},
        "npcs": {
            "Czarny Mag": {
                "desc": "Upiorna postać w czarnej pelerynie, której oczy jarzą się czerwonym blaskiem.",
                "responses": {
                    "Kim jesteś?": "Jestem cieniem dawnej potęgi... magiem, który zapłacił najwyższą cenę za wiedzę.",
                    "Czy rzucisz czar?": "Każde zaklęcie ma swoją cenę. Czy jesteś gotów ją zapłacić?",
                    "Czy w ruinach jest skarb?": "Nie wszystko, co błyszczy, jest złotem. Czasem to tylko oczy, które patrzą z mroku...",
                },
            },
            "Złowrogi Gargulec": {
                "desc": "Kamienna istota, która wydaje się poruszać, gdy nikt nie patrzy.",
                "responses": {
                    "Czy żyjesz?": "Może... może nie. Może zawsze byłem tu i będę. Może to ty jesteś snem...",
                    "Czy pilnujesz czegoś?": "Pilnuję tego, co zapomniane. A może to ono pilnuje mnie?",
                    "Co się stanie, jeśli dotknę kamieni?": "Spróbuj, jeśli nie boisz się, że kamień dotknie ciebie...",
                },
            },
        },
        "items": {},
    },
    "Zatopione Katakumby": {
        "desc": "Podziemne korytarze, w których woda sięga do kolan. Ściany zdobią wypłowiałe freski przedstawiające sceny dawnych bitew i ofiar składanych bóstwom. Gdzieś w oddali słychać kapanie wody i szuranie niewidzialnych istot.",
        "options": {"e": "Ruiny Zamku Cieni", "w": "Podziemne Miasto"},
        "npcs": {
            "Szepczący Kościec": {
                "desc": "Kościotrup, który nieustannie mruczy do siebie niezrozumiałe słowa.",
                "responses": {
                    "Kim jesteś?": "Byłem kiedyś kimś... ale woda zatarła moje imię...",
                    "Czy w katakumbach jest coś strasznego?": "Jest coś, co nie śpi. Coś, co czeka. Może na ciebie...",
                    "Co szepczesz?": "To dawne zaklęcia. A może prośby? A może ostrzeżenia?",
                },
            },
            "Strażnik Krypty": {
                "desc": "Duch odziany w starożytną zbroję, wpatrujący się w przechodniów pustym wzrokiem.",
                "responses": {
                    "Kim jesteś?": "Byłem strażnikiem, gdy świat był jeszcze młody... i wciąż nim jestem.",
                    "Czy katakumby skrywają skarb?": "Największy skarb to ten, którego się boisz...",
                    "Czy mogę przejść?": "Tylko ci, którzy nie boją się ciemności, znajdą drogę.",
                },
            },
        },
        "items": {},
    },
    "Podziemne Miasto": {
        "desc": "Ukryte w głębi ziemi miasto, gdzie na wpół zapomniane cywilizacje przetrwały w ciemnościach. Kryształowe lampy rzucają migotliwe światło, a mieszkańcy szepczą o dawnej potędze swego ludu. W powietrzu czuć wilgoć i echo przeszłości.",
        "options": {"e": "Zatopione Katakumby", "s": "Komnata Wiecznego Ognia"},
        "npcs": {
            "Kryształowy Wędrowiec": {
                "desc": "Postać utkana ze światła i mgły, której oczy lśnią niczym diamenty.",
                "responses": {
                    "Kim jesteś?": "Jestem echem dawnych dni. Miasto było kiedyś pełne światła...",
                    "Co się stało z mieszkańcami?": "Niektórzy odeszli. Niektórzy zostali. Niektórzy są bliżej, niż myślisz...",
                    "Czy mogę zostać tutaj?": "Jeśli światło cię zaakceptuje. Jeśli mrok cię nie pochłonie.",
                },
            },
            "Starzec w Kapturze": {
                "desc": "Zgarbiona postać, trzymająca starą księgę z runami, które migoczą w ciemności.",
                "responses": {
                    "Co czytasz?": "To księga opowieści o tym, co było. I o tym, co być może dopiero nadejdzie...",
                    "Czy podziemne miasto jest bezpieczne?": "Nic nie jest naprawdę bezpieczne. Ale nie wszystko chce cię skrzywdzić.",
                    "Czy w mieście są ukryte przejścia?": "Jest więcej dróg, niż widać oczami. Ale niektóre lepiej pozostawić zamknięte...",
                },
            },
        },
        "items": {},
    },
    "Komnata Wiecznego Ognia": {
        "desc": "W sercu podziemi znajduje się komnata z wiecznie płonącym płomieniem. Ogień zdaje się tańczyć w rytm niewidzialnej melodii, a jego blask jest jednocześnie hipnotyzujący i przerażający. Niektórzy twierdzą, że to źródło nieśmiertelności.",
        "options": {"n": "Podziemne Miasto", "e": "Smocza Jama"},
        "npcs": {
            "Strażnik Płomienia": {
                "desc": "Postać złożona z czystego ognia, jej oczy płoną niczym dwa słońca.",
                "responses": {
                    "Kim jesteś?": "Jestem strażnikiem ognia, tym, który nigdy nie gaśnie.",
                    "Czy ogień naprawdę jest wieczny?": "Tak długo, jak jest ktoś, kto go pamięta.",
                    "Czy ogień może mówić?": "Ogień śpiewa, szepcze, tańczy... ale słyszą go tylko ci, którzy chcą go zrozumieć.",
                },
            },
            "Płomienisty Wąż": {
                "desc": "Długie, ogniste stworzenie, które pełza wokół płomienia, wijąc się w rytm jego tańca.",
                "responses": {
                    "Czy jesteś smokiem?": "Jestem dzieckiem ognia... może kiedyś dorosnę i wzniosę się ku niebu!",
                    "Czy ogień boli?": "Nie tych, którzy są jego częścią. Może chcesz spróbować?",
                    "Czy ktoś ukrył tu skarb?": "Nie wszystko, co błyszczy, jest złotem. Czasem to płomień skrywa największą tajemnicę.",
                },
            },
        },
        "items": {},
    },
    "Smocza Jama": {
        "desc": "Olbrzymia pieczara, w której powietrze drży od oddechu śpiącego smoka. Jego łuski błyszczą w mroku niczym płynne złoto, a wokół niego leżą stosy skarbów. Legenda głosi, że tylko najodważniejsi mogą obudzić bestię i przetrwać.",
        "options": {"w": "Komnata Wiecznego Ognia", "n": "Królestwo Krasnoludów"},
        "npcs": {
            "Drakthar, Śniący Smok": {
                "desc": "Potężny, złocisty smok, który zdaje się spać, lecz jedno jego oko jest zawsze lekko uchylone.",
                "responses": {
                    "Czy śpisz?": "Moje ciało odpoczywa, ale mój umysł czuwa... Zawsze.",
                    "Czy obudzisz się, jeśli dotknę skarbu?": "Możesz spróbować... ale czy naprawdę chcesz to zrobić?",
                    "Czy smoki mają marzenia?": "O tak, nasze sny tworzą światy, które nigdy nie znikną.",
                },
            },
            "Mały Smok Pyra": {
                "desc": "Młody, nieporadny smok, który podskakuje wokół i uczy się ziać ogniem.",
                "responses": {
                    "Kim jesteś?": "Jestem Pyra! Jeszcze nie umiem dobrze ziać ogniem, ale kiedyś będę wielki!",
                    "Czy boisz się ludzi?": "Nie, ale zawsze mówią, że smoki są straszne... a ja tylko chcę się bawić!",
                    "Czy masz skarb?": "Mam! Kamyk, który lśni w ciemności! Ale nie oddam go tak łatwo!",
                },
            },
        },
        "items": {},
    },
    "Królestwo Krasnoludów": {
        "desc": "Podziemne miasto wykute w skale. Kamienne ulice oświetlone są blaskiem lawy płynącej w głębokich rowach. Echo młotów uderzających o stal niesie się przez hale pełne kowali i rzemieślników. Krasnoludy strzegą swych skarbów z niebywałą gorliwością.",
        "options": {"w": "Złoty Most", "s": "Smocza Jama"},
        "npcs": {
            "Król Hargor": {
                "desc": "Sędziwy krasnoludzki władca, z brodą długą jak historia jego ludu.",
                "responses": {
                    "Czy jesteś królem?": "Tak, od setek lat czuwam nad mym ludem i jego skarbami.",
                    "Czy krasnoludy boją się smoków?": "Prawdziwy krasnolud boi się tylko pustego kufla!",
                    "Czy masz sekretną kuźnię?": "Może tak, może nie. A może tylko wybrani mogą ją zobaczyć?",
                },
            },
            "Thorgar Kowal": {
                "desc": "Potężny krasnolud z ramionami silnymi jak stal, kujący najtwardsze ostrza.",
                "responses": {
                    "Czy robisz najlepsze miecze?": "Oczywiście! Każde moje ostrze to dzieło sztuki.",
                    "Czy mogę dostać broń?": "Tylko jeśli udowodnisz, że jesteś jej godzien!",
                    "Czy istnieje niezniszczalna stal?": "Legenda mówi o metalu tak twardym, że nawet smoczy ogień go nie stopi...",
                },
            },
        },
        "items": {},
    },
    "Stara Wieża": {
        "desc": "Na skraju lasu stoi zapomniana wieża. Jej kamienie pokrywa mech, a schody wiodą ku ciemnemu niebu. Mówi się, że w jej wnętrzu wciąż mieszka duch dawnego maga, który czeka na kogoś, kto dokończy jego dzieło.",
        "options": {"e": "Mglisty Las", "s": "Zapomniana Karczma"},
        "npcs": {
            "Duch Maga Eldriona": {
                "desc": "Przezroczysta postać w długiej szacie, unosząca się nad podłogą wieży.",
                "responses": {
                    "Kim jesteś?": "Jestem Eldrion, ostatni mag tej wieży. Czekam na kogoś, kto dokończy moje dzieło...",
                    "Czy wieża jest magiczna?": "Jeśli wierzysz w magię, zobaczysz ją na każdym kroku.",
                    "Czy mogę nauczyć się czarów?": "Być może. Ale czy jesteś gotów na ich cenę?",
                },
            },
            "Księga Mądrości": {
                "desc": "Stara, pokryta kurzem księga, która potrafi mówić.",
                "responses": {
                    "Czy możesz mi coś powiedzieć?": "Wiedza to skarb. Ale nie każdy skarb jest bezpieczny...",
                    "Co skrywa ta wieża?": "Wiele tajemnic. Ale czy na pewno chcesz je poznać?",
                    "Czy w wieży jest ukryty skarb?": "Największy skarb to ten, którego nie widzisz oczami, a czujesz sercem...",
                },
            },
        },
        "items": {},
    },
    "Zapomniana Karczma": {
        "desc": "Zniszczona karczma, której ściany kryją więcej tajemnic, niż by się wydawało. Drewniane stoły noszą ślady licznych walk, a za barem stoi jedyny ocalały – zakurzony kufel, który zdaje się sam wypełniać trunkiem.",
        "options": {"n": "Stara Wieża", "w": "Pustynia Kości"},
        "npcs": {
            "Karczmarz Widmo": {
                "desc": "Postać ledwo widoczna, jakby unosiła się pomiędzy światami, zawsze za barem.",
                "responses": {
                    "Kim jesteś?": "Nazywali mnie Rudrik. Kiedyś prowadziłem tę karczmę... zanim stała się zapomniana.",
                    "Czy mogę dostać coś do picia?": "Mogę nalać ci to, co sam sobie przypomnisz.",
                    "Czy tu straszy?": "Nie, to tylko stare wspomnienia. Ale niektóre wspomnienia bywają uparte...",
                },
            },
            "Wędrowiec bez Cienia": {
                "desc": "Zagubiona dusza, której cień zniknął w piaskach pustyni.",
                "responses": {
                    "Kim jesteś?": "Byłem podróżnikiem. Ale pustynia zabrała mój cień... i coś więcej.",
                    "Co się stało z twoim cieniem?": "Zgubiłem go, gdy przekroczyłem pewien próg. A może to on zgubił mnie?",
                    "Czy pustynia jest niebezpieczna?": "Dla tych, którzy zapominają, kim są. Bo pustynia pamięta za nich...",
                },
            },
        },
        "items": {},
    },
    "Pustynia Kości": {
        "desc": "Niekończące się wydmy, na których leżą kości upadłych wojowników. Słońce pali niemiłosiernie, a na horyzoncie widać zarys starożytnej świątyni. Wśród piasków przemykają cienie – czy to złudzenie, czy coś czai się pod powierzchnią?",
        "options": {"e": "Zapomniana Karczma", "s": "Świątynia Czasu"},
        "npcs": {},
        "items": {},
    },
    "Świątynia Czasu": {
        "desc": "Starożytna świątynia, której mury pulsują dziwną energią. Posągi bogów zdają się obserwować każdego, kto przekracza próg. W centrum stoi zegar bez wskazówek – podobno wskazuje czas tylko tym, którzy są gotowi poznać swój los.",
        "options": {"n": "Pustynia Kości"},
        "npcs": {
            "Strażnik Zegara": {
                "desc": "Postać w długiej szacie, której twarz skrywa kaptur. W dłoni trzyma starożytną klepsydrę.",
                "responses": {
                    "Kim jesteś?": "Jestem strażnikiem czasu. Pilnuję, by zegar nie wskazał godziny, której nikt nie powinien poznać...",
                    "Czy mogę zobaczyć wskazówki zegara?": "Tylko jeśli czas uzna, że jesteś gotów.",
                    "Czy można cofnąć czas?": "Każdy dzień to nowa szansa. Ale nie każdy powinien mieć drugą próbę...",
                },
            },
            "Echo Przeszłości": {
                "desc": "Duch, który pojawia się i znika, powtarzając słowa wypowiedziane dawno temu.",
                "responses": {
                    "Kim jesteś?": "Jestem głosem tych, którzy byli przed tobą. A może tych, którzy dopiero nadejdą?",
                    "Czy przyszłość jest zapisana?": "Przyszłość to lustro. Czasem widzisz siebie. Czasem coś, co dopiero się stanie...",
                    "Czy świątynia ma tajemnice?": "Każda ściana widziała więcej, niż można sobie wyobrazić. A zegar... on pamięta wszystko.",
                },
            },
        },
        "items": {},
    },
}
