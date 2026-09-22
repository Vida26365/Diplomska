# Linearni tipi

-- Moja diplomska se bo ukvarjala z linearnimi tipi. Da sploh razumemo kaj so linearni tipi, moramo razumeti kaj sploh so tipi.

## Klasična logika
Najprej bi rada predstavila malec drugačen način zapisa standardne logike, ki jo vsi že poznamo iz prvega letnika in prej. Imenuje se naravna dedukcija.

Recimo da velja izjava A in izjava B. Potem velja A in B. Temu pravilu pravimo pravlo upeljave za konjunkcijo. Označi se tukaj desno od te črte.
Obstjata tudi pravili uporabe, ki povesta kako uporabimo konjunkcijo. Če velja A in B, potem velja A

Za vse take izjave imamo pravila vpeljave in pravila uporabe. Ali ima kdo kakšno idejo kako bi zapisali pravili uporabe in izpeljave za implikacijo? Začnimo s pravilom uporabe.
Imamo črto. Želimo uporabiti implikacijo iz A v B, torej imamo implikacijo na črti. Kaj še rabimo? A, torej damo A nad črto. In potem velja da B. To je pravilo uporabe za implikacijo. 
Kaj pa pravilo upeljave?
Pod črto želimo? A v B. Kako pa pridemo do tega? Predpostavimo A in dokažemo B. Rečemo da damo A v kontekst. To se na tak način zapiše takole. A |- B. To bi pomenilo, da če imamo A v kontekstu, imamo B. 
Mamo tudi prailo, ki se imejue hipoteza, ki pravi če je A v kontekstu, potem imamo A.

Kontekst ubistvu pišemo povsod. 

Gremo izpeljati eno pravilo. Želimo izpeljati da iz P sledi P in P. Kako bi se tega lotili. Pod črto želimo dobiti P => P in P. Kaj rabimo nad črto? Pravilo vpeljave implikacije. P |- P in P.
Zdaj imamo konjunkcijo, torej potrebujemo pravilo vpeljave za konjunkcijo. To pa sledi iz pravila hipoteze.

## Linearna logika
Zdaj smo se spomnili standardno logiko, zdaj pa vam lahko predstavim kaj je linearna logika. V linearni logiki želimo vsako predpostavko uporabiti natanko enkrat. Zato imamo malce drugačna pravila. Začnimo s pravilom hipoteze. Izraz gama vejca A predstavlja kontekst gama, ki mu pridružimo izraz A. Prej je veljalo to pravilo, vendar v linearni logiki ne bi bilo validno, saj stvari iz gama ne uporabimo. Zato imamo pravilo A |- A

Poglejmo kako potem izgleda implikacija. Pravilo vpeljave je kar enako. Spremenil se je znak za implikacijo, da se poudari, da to ni ve nadvadna implikacija, ampak je implikacija v linearni logiki. Razlikuje se v pravilu uporabe. Tu, se kontekst gama in delta združi.

Zdaj smo že bližje temu kaj bom delala za diplomski seminar.
Naslednji korak je Curry-Howardov izomorfizem

## Curry-Howardov izomorfizem
Tu je je napisan izomorfizem z navadno logiko. Najbrž se to še spomnite iz programiranja 1. Kako beremo to sintakso. Če imamo spremenljivko x tipa A v kontekstu gama, imamo program, ki vrne to spremenljivko tipa A. 

Program M tipa B imamo, če imamo spremenljivko tipa A in spremenljivke s tipi določenimi s kontekstom gama, potem lahko naredimo program tipa A v B.

Če imamo program tipa A v B in program tipa B, potem lahko dobimo porgram tipa B. Vse je isto kot v navadni logiki.

## Linearni tipi
Zdaj pa želimo da to ni izomorfno navadni logiki, ampak linearni. Pravila se spet rahlo spremenijo
