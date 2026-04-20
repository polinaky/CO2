# CO₂ līmeņa analīze
Šī ir Flask tīmekļa lietotne, kas paredzēta ogļskābās gāzes (CO₂) līmeņa monitoringam un analīzei. 
# Uzstādīšana (Instalācija)
Lai uzstādīt programmu, izpildiet šos soļus:
	1.	**Instalējiet Python** (ja tas vēl nav izdarīts) no oficiālās vietnes.
	2.	**Instalējiet Flask bibliotēku**, izmantojot termināli:   pip install flask      
	3.	**Lejupielādējiet projektu** vai klonējiet to no GitHub:   

    git clone https://github.com/polinaky/CO2.git

	4.	**Pārbaudiet failus**: Pārliecinieties, ka projekta mapē atrodas fails data.csv ar mērījumiem.
	5.	**Palaidiet programmu**:
python app.py failā
	6.	**Atveriet pārlūkprogrammu** un ierakstiet adresi: http://127.0.0.1:5000/
# Projekta struktūra un faili
Projekts sastāv no šādām galvenajām daļām:
•	app.py - Galvenais Flask fails. Tas apstrādā datu ielādi, loģiku un maršrutēšanu.
•	data.csv - Datu fails, kurā tiek glabāti CO₂ mērījumi un laiks.
•	templates/index.html - Lietotāja interfeisa veidne, kas attēlo datus un grafiku.
•	static/style.css - Dizaina fails vizuālajam noformējumam.
•	README.md - Projekta dokumentācija (šis fails).
# Failu struktūra ir sekojoša: 
project/
├── app.py # Galvenais Flask fails
├── data.csv # CO₂ dati
├── templates/
│ └── index.html # Lietotāja interfeiss
├── static/
│ └── style.css # Dizains
└── README.md # Dokumentācija

# Lietošanas instrukcija
Programma piedāvā divas galvenās funkcijas:
1.	**Datu apskate**:
o	Izvēlieties datumu kalendārā.
o	Nospiediet pogu "Dati".
o	Sarakstā tiks parādīti visi mērījumi izvēlētajā dienā.
2.	**Grafika skatīšana**:
o	Nospiediet pogu "Grafiks".
o	Tiks parādīta diagramma, kas vizualizē CO₂ līmeņa izmaiņas.
# Gaisa kvalitātes indikācija:
Lietotne automātiski krāso rādījumus atkarībā no CO₂ līmeņa:
•	Zaļš (Labs): < 800 ppm
•	Oranžs (Vidējs): 800 – 1200 ppm
•	Sarkans (Slikts): > 1200 ppm

# Lietošanas piemērs
# Ievade: Lietotājs kalendārā izvēlas datumu 03/21/2026 un nospiež pogu "Rādīt".
# Sagaidāmā izvade:
CO₂: 700 ppm - Labs (Zemāk redzams saraksts ar konkrētās dienas stundām un mērījumiem).
# Licence
Šis projekts ir licencēts saskaņā ar MIT licenci. 
