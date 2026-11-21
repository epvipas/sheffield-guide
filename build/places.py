from cats import add

# ---------------- SIGHTS ----------------
add("sights","Winter Garden","Surrey Street, S1 2HH",
 "One of the largest temperate glasshouses built in a UK city in the last century, a huge timber-arched hall full of plants from around the world, free to wander. It joins the Millennium Gallery.",
 "Free; a good place to warm up in winter",geo="Winter Garden, Sheffield")
add("sights","Peace Gardens & Town Hall","Pinstone Street, S1 2HH",
 "The city's main square, with fountains and cascades in front of the 1897 Town Hall. On the Town Hall's tower stands a statue of Vulcan, the god of fire and metalwork.",
 "Your base for walking times",ta=True,geo="Peace Gardens, Sheffield")
add("sights","Park Hill","Duke Street, S2 5RQ",
 "The vast 1960s 'streets in the sky' estate on the hill above the station, Europe's largest listed building, now part-restored with flats, studios and the S1 Artspace gallery. The 'I love you will u marry me' graffiti bridge is now a neon sign.",
 "A 10-minute walk up from the station",ta=True,geo="Park Hill, Sheffield",ll=(53.3780,-1.4605))
add("sights","Kelham Island Quarter","Alma Street, S3 8RY",
 "An old industrial island on the River Don, now the city's best area for independent bars, restaurants and real-ale pubs among restored workshops and warehouses.",
 "Go for an afternoon and stay for the evening",ta=True,geo="Kelham Island, Sheffield",ll=(53.3887,-1.4703))
add("sights","Sheffield Cathedral","Church Street, S1 1HA",
 "A medieval parish church that became a cathedral in 1914, with a striking modern lantern tower and the medieval Shrewsbury Chapel.",
 "Free; a quiet stop on Church Street",geo="Sheffield Cathedral")

# ---------------- MUSEUMS ----------------
add("museums","Kelham Island Museum","Alma Street, S3 8RY",
 "Sheffield's industrial museum, home of the River Don Engine, the most powerful working steam engine in Europe, which still runs on set days. Little Mesters' workshops show the city's cutlery trade.",
 "Free entry; check engine run times",web="https://sheffieldmuseums.org.uk",geo="Kelham Island Museum")
add("museums","Weston Park Museum","Western Bank, S10 2TP",
 "Sheffield's free museum of natural history, archaeology and the city's story, with Snowy the polar bear. A new exhibition, Bittersweet: The Story of Sugar in Sheffield, opens on 27 November 2026.",
 "Free · next to Weston Park and the university",web="https://sheffieldmuseums.org.uk",geo="Weston Park Museum")
add("museums","Abbeydale Industrial Hamlet","Abbeydale Road South, S7 2QW",
 "An 18th-century scythe works with water-powered tilt hammers, workers' cottages and a manager's house, preserved as it was.",
 "Seasonal opening; check before you go",far=True,geo="Abbeydale Industrial Hamlet")
add("museums","Portland Works","Randall Street, S2 4SJ",
 "A Victorian cutlery works, where stainless steel cutlery was first made, now saved by a community share offer and full of working makers. Open days and tours.",
 "Check the tour and open-day dates",ta=False,geo="Portland Works, Sheffield")

# ---------------- GALLERIES ----------------
add("galleries","Millennium Gallery","Arundel Gate, S1 2PP",
 "Free galleries of art and design, including Sheffield's metalwork collection and John Ruskin's collection of art, minerals and casts that he gave to the city's workers.",
 "Free · joined to the Winter Garden",web="https://sheffieldmuseums.org.uk",geo="Millennium Gallery, Sheffield")
add("galleries","Graves Gallery","Surrey Street, S1 1XZ",
 "A free gallery on the top floor of the Central Library with paintings from Turner and Cézanne to contemporary artists.",
 "Free; take the lift up through the library",web="https://sheffieldmuseums.org.uk",geo="Graves Gallery, Sheffield",ll=(53.3802,-1.4673))
add("galleries","Site Gallery","1 Brown Street, S1 2BS",
 "Sheffield's contemporary art centre for moving image, new media and performance, in the Cultural Industries Quarter near the station.",
 "Free",geo="Site Gallery, Sheffield")

# ---------------- SHOPS ----------------
add("shops","Division Street & Devonshire Street","Division Street, S1 4GF",
 "The city centre's indie strip: vintage, streetwear, record and design shops, cafés and bars running down to Devonshire Green.",
 "Start at the top by the old fire station",ta=False,geo="Division Street, Sheffield",ll=(53.3793,-1.4783))
add("shops","Sharrow Vale Road","Sharrow Vale Road, S11 8ZA",
 "A village-like street of independent delis, cafés, a fishmonger and boutiques, a short bus ride from the centre.",
 "Pair with Ecclesall Road and the Botanical Gardens",ta=False,far=True,geo="Sharrow Vale Road, Sheffield")

# ---------------- RECORDS ----------------
add("records","Record Collector","233 Fulwood Road, Broomhill, S10 3BA",
 "South Yorkshire's largest independent record shop, with tens of thousands of new and second-hand records and CDs.",
 "Allow time; the second-hand racks are deep",far=True,geo="Record Collector, Fulwood Road, Sheffield")
add("records","Memory Dance","Chapel Walk, S1 2PD",
 "A new record shop on Chapel Walk, opened in 2026, with a small retro cinema room.",
 "Right in the centre",ta=False,geo="Chapel Walk, Sheffield",ll=(53.3823,-1.4682))
add("records","Hub","Sharrow Vale Road, S11 8ZA",
 "A small independent record shop with new and used vinyl.",
 "Pair with Sharrow Vale's cafés",ta=False,far=True,geo="Hub, Sharrow Vale Road, Sheffield",ll=(53.3700,-1.5000))

# ---------------- CAMERAS & GEAR ----------------
add("gear","Harrison Cameras","112–114 London Road, Highfield, S2 4LR",
 "An independent camera shop with a dedicated second-hand department: film and digital cameras and lenses, inspected and sold with a 12-month warranty.",
 "Mon–Sat 10:00–18:00",web="https://www.harrisoncameras.co.uk",geo="Harrison Cameras, London Road, Sheffield")

# ---------------- VINTAGE & ANTIQUES ----------------
add("vintage","Sheffield Antiques Centre","178 Broadfield Road, S8 0XH",
 "Over 40 antiques stalls in a 19th-century building in the Abbeydale Road Antiques Quarter, with architectural salvage and garden furniture in the courtyard.",
 "Wed–Thu by appointment; open other days",far=True,geo="Sheffield Antiques Centre")
add("vintage","Heeley Bank Antiques Centre","635 Queens Road, S2 4DX",
 "A multi-dealer antiques and vintage centre in an old school, packed with furniture, homewares and curios.",
 "Combine with the Antiques Quarter",ta=False,far=True,geo="Heeley Bank, Queens Road, Sheffield")
add("vintage","Abbeydale Road Antiques Quarter","Abbeydale Road, S7 1FD",
 "A long road of antique and vintage shops, bottle shops, bars, makers and record emporiums stretching into Nether Edge.",
 "Best on a Saturday",ta=False,far=True,geo="Abbeydale Road, Sheffield",ll=(53.3640,-1.4830))
add("vintage","Vulgar","Unit 2, The Forum, 127–129 Devonshire Street, S3 7SB",
 "A city-centre vintage clothing shop in The Forum on Devonshire Street.",
 "Pair with Division Street",ta=False,who=["m","w"],geo="Vulgar, Devonshire Street, Sheffield",ll=(53.3797,-1.4787))

# ---------------- CHARITY ----------------
add("charity","St Luke's Vintage Shop","3 Crookes Road, Broomhill, S10 5BA",
 "The local hospice's vintage charity shop in Broomhill, near Record Collector.",
 "Pair with Record Collector",ta=False,far=True,who=["m","w"],geo="St Luke's, Crookes Road, Sheffield",ll=(53.3822,-1.5005))
add("charity","Age UK, Abbeydale Road","Abbeydale Road, S7",
 "A big charity shop in the Antiques Quarter selling pre-loved clothing, toys, bric-a-brac and homeware.",
 "Mon–Fri 9:00–17:00, Sat 9:00–16:00",ta=False,far=True,who=["m","w","k"],geo="Age UK, Abbeydale Road, Sheffield",ll=(53.3625,-1.4855))

# ---------------- FOOD SHOPS & MARKETS ----------------
add("markets","Moor Market","The Moor, S1 4PF",
 "Sheffield's indoor market, with butchers, fishmongers, international grocers, street food and cafés.",
 "Busiest on Saturdays",geo="Moor Market, Sheffield")
add("food","J.H. Mann fishmonger","261 Sharrow Vale Road, S11 8ZE",
 "A traditional fishmonger on Sharrow Vale Road, sister to the Native seafood restaurant.",
 "Bring a cool bag",ta=False,far=True,geo="J H Mann, Sharrow Vale Road, Sheffield",ll=(53.3702,-1.5005))

# ---------------- CAFÉS ----------------
add("cafes","Tamper Sellers Wheel","149 Arundel Street, S1 2NU",
 "The granddaddy of Sheffield's coffee scene, founded in 2011, with a menu inspired by Auckland cafés, in a former cutlery works.",
 "Brunch gets busy at weekends",price=1,geo="Tamper Sellers Wheel, Sheffield")
add("cafes","Steam Yard","Aberdeen Court, 95–97 Division Street, S1 4GE",
 "A popular independent coffee stop in a courtyard off Division Street, known for coffee and doughnuts.",
 "Doughnuts sell out",price=1,geo="Steam Yard, Sheffield")
add("cafes","Cole's Corner","322 Abbeydale Road, S7 1FN",
 "A quirky café-bar, record shop and gift shop in the Antiques Quarter.",
 "A good break on an antiques hunt",price=1,ta=False,far=True,geo="Cole's Corner, Abbeydale Road, Sheffield",ll=(53.3655,-1.4818))

# ---------------- EAT ----------------
add("splurge","Jöro","Krynkl, 294 Shalesmoor, S3 8US",
 "Inventive Nordic-influenced tasting menus in a restaurant built from shipping containers, consistently ranked among the best in the country since opening in 2016.",
 "Book well ahead",price=4,geo="Joro, Shalesmoor, Sheffield",ll=(53.3876,-1.4785))
add("mid","Juke & Loe","Kelham Island, S3",
 "A Michelin-listed modern British restaurant that has moved from Ecclesall Road to Kelham Island.",
 "Book at weekends",price=3,geo="Juke and Loe, Sheffield",ll=(53.3890,-1.4710))
add("mid","Domo","34–36 Cotton Mill Walk, Kelham Island, S3 8DH",
 "Sardinian cooking in Eagle Works, voted best large Italian restaurant at the UK Italian Awards. Fresh pasta and seafood.",
 "Try the culurgiones",price=2,geo="Domo, Sheffield",ll=(53.3893,-1.4720))
add("mid","Native","167–169 Gibraltar Street, S3 8UA",
 "A seafood restaurant from the team behind the J.H. Mann fishmonger, cooking the day's catch simply and well.",
 "Ask what came in today",price=3,geo="Native, Gibraltar Street, Sheffield",ll=(53.3870,-1.4715))
add("cheap","Cutlery Works","73–101 Neepsend Lane, S3 8AT",
 "A big food hall in an old cutlery factory, with independent kitchens, bars and a coffee roaster, and live music and events.",
 "Good for groups who all want something different",price=1,geo="Cutlery Works, Sheffield")

# ---------------- PUBS ----------------
add("pubs","Kelham Island Tavern","62 Russell Street, S3 8RW",
 "CAMRA's 2026 Sheffield & District Pub of the Year: a small backstreet pub with a dozen handpumps and a sun-trap beer garden. The Telegraph called it the best pub in South Yorkshire.",
 "Start your ale trail here",price=1,geo="Kelham Island Tavern")
add("pubs","The Fat Cat","23 Alma Street, S3 8SA",
 "A proper old-fashioned workers' pub by the Kelham Island Museum, the first in Sheffield to sell guest beers, with its brewery next door.",
 "Cheap, hearty pub food",price=1,geo="Fat Cat, Alma Street, Sheffield")
add("pubs","Shakespeare's","146–148 Gibraltar Street, S3 8UB",
 "A rambling Georgian coaching inn with a huge range of cask ales, ciders and whiskies, and a beer garden.",
 "Live music some nights",price=1,geo="Shakespeare's, Gibraltar Street, Sheffield")
add("pubs","Dog & Partridge","56 Trippet Lane, S1 4EL",
 "An unspoilt Irish-run city-centre pub with small rooms, real ale and traditional music sessions. CAMRA's 2026 city-centre winner.",
 "Folk sessions most evenings",price=1,geo="Dog and Partridge, Trippet Lane, Sheffield",ll=(53.3826,-1.4746))
add("pubs","The Sheffield Tap","Sheffield Station, Sheaf Street, S1 2BP",
 "A gloriously restored Edwardian station refreshment room, with tiles and mahogany, a huge beer range and its own brewery behind glass.",
 "Last drink before the train",price=1,geo="Sheffield Tap")
add("pubs","The Bath Hotel","66–68 Victoria Street, S3 7QL",
 "A beautifully preserved 1930s pub with a heritage interior near the university, serving Thornbridge beers.",
 "Pair with Division Street",price=1,geo="Bath Hotel, Victoria Street, Sheffield")
add("pubs","The Rutland Arms","86 Brown Street, S1 2BS",
 "A friendly corner pub with a striking tiled frontage near the station and Site Gallery, with good beer and food.",
 "Handy before the train",price=1,geo="Rutland Arms, Brown Street, Sheffield")
add("pubs","The Sheaf View","25 Gleadless Road, Heeley, S2 3AA",
 "A real-ale pub in Heeley, CAMRA's 2026 Sheffield South Pub of the Year.",
 "Pair with the Antiques Quarter",price=1,far=True,geo="Sheaf View, Sheffield")

# ---------------- MUSIC & THEATRE ----------------
add("music","Crucible & Lyceum Theatres","55 Norfolk Street, Tudor Square, S1 1DA",
 "The Crucible is home to the World Snooker Championship every spring and a famous thrust-stage theatre. The Lyceum next door is a gorgeous Edwardian theatre for touring shows and panto.",
 "Snooker runs late April to early May",web="https://www.sheffieldtheatres.co.uk",geo="Crucible Theatre")
add("music","Sheffield City Hall","Barker's Pool, S1 2JA",
 "A grand 1930s concert hall with a classic ballroom, for big touring bands, comedians and orchestras.",
 "Check the ballroom gigs too",geo="Sheffield City Hall")
add("music","Abbeydale Picture House","387 Abbeydale Road, S7 1FS",
 "A grand 1920s cinema reborn as a music venue, bar and arts space, with a quarterly vintage market and a monthly car boot sale.",
 "Check gigs and markets",far=True,geo="Abbeydale Picture House")
add("music","Electric Sheffield","6–7 Leadmill Road, S1 4SE",
 "The building that was the famous Leadmill until its 2025 eviction now runs as Electric Sheffield. The Leadmill team is crowdfunding a new home elsewhere.",
 "Check listings",geo="Leadmill Road, Sheffield",ll=(53.3772,-1.4648))

# ---------------- PARKS ----------------
add("parks","Sheffield Botanical Gardens","Clarkehouse Road, S10 2LN",
 "Nineteen acres of gardens laid out in 1836 with three restored glass pavilions, free to visit.",
 "Free · pair with Ecclesall Road cafés",far=True,geo="Sheffield Botanical Gardens")
add("parks","Porter Valley & Shepherd Wheel","Whiteley Wood, S11 7GB",
 "A wooded valley walk from Endcliffe Park past old mill ponds to Shepherd Wheel, a water-powered grinding workshop. Sheffield is one of the greenest cities in Europe.",
 "Walk from Endcliffe Park; Shepherd Wheel opens weekends",far=True,geo="Shepherd Wheel, Sheffield")

# ---------------- SPORT ----------------
add("sport","Bramall Lane (Sheffield United)","Bramall Lane, S2 4SU",
 "The oldest major stadium in the world still hosting professional football, first used in 1862 and home of the Blades.",
 "A 15-minute walk south of the centre",far=True,geo="Bramall Lane")
add("sport","Hillsborough (Sheffield Wednesday)","Hillsborough, S6 1SW",
 "The Owls' historic stadium in the north-west of the city, with a memorial to the 97 Liverpool fans who died in 1989.",
 "Tram to Leppings Lane",far=True,geo="Hillsborough Stadium")

# ---------------- DAY TRIPS ----------------
add("trips","Castleton","Castleton, Hope Valley, S33 8WN",
 "A Peak District village under Peveril Castle, with four show caves including Peak Cavern, Speedwell (by boat) and Blue John Cavern, plus Mam Tor's ridge walk.",
 "Book a cave tour; park early at weekends",far=True,drive="40 min",geo="Castleton, Derbyshire")
add("trips","Chatsworth","Bakewell, Derbyshire, DE45 1PP",
 "The Duke of Devonshire's palace, with a vast garden and art collection. Christmas at Chatsworth runs 7 November 2026 to 3 January 2027, with the Christmas market until 13 December.",
 "Booking needed at Christmas",web="https://www.chatsworth.org",far=True,drive="35 min",geo="Chatsworth House")
add("trips","Stanage Edge & Hathersage","Hathersage, S32 1DT",
 "A gritstone escarpment with huge views, famous with climbers and from Pride and Prejudice, above the village where Little John is said to be buried.",
 "Walk up from Hathersage or park at Hollin Bank",far=True,drive="30 min",geo="Stanage Edge")
add("trips","Ladybower Reservoir","Bamford, S33 0AQ",
 "A huge reservoir in the Upper Derwent valley where the Dambusters practised. Woodland walks, cycle hire and the drowned village of Derwent.",
 "Fairholmes car park and café",far=True,drive="30 min",geo="Ladybower Reservoir")
add("trips","Wentworth Woodhouse","Wentworth, Rotherham, S62 7TQ",
 "A colossal Georgian stately home with the longest façade of any country house in England, being restored by a trust. Guided tours.",
 "Book a tour in advance",far=True,drive="25 min",geo="Wentworth Woodhouse")
add("trips","Yorkshire Sculpture Park","West Bretton, WF4 4LG",
 "500 acres of parkland with sculpture by Henry Moore, Barbara Hepworth and many others, plus indoor galleries.",
 "Free to walk; pay for parking",far=True,drive="35 min",geo="Yorkshire Sculpture Park")
