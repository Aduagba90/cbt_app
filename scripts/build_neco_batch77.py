"""Batch 077 - WAEC Geography, Paper 1 Objective round 1.

WASSCE Geography Paper 1 (Objective) is a 50-item paper (1 hr; official 2026
second-series timetable, paper 2041). This batch covers the WASSCE geography
syllabus with FRESH angles and phrasings - Nigeria-specific facts (Lokoja
confluence, Chappal Waddi, Chad Basin, Kainji Dam, harmattan), scenario
stems (steep-slope contours, swollen-river floods, Nanka gullies) and
question-form items - because the near-dup scan checks every item against
the JAMB, WAEC and NECO banks, including the large JAMB Geography banks
(batches 037-038) and our 87-item NECO Geography bank.

    python3 scripts/build_neco_batch77.py -> content/batch_077_waec_geography.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_EAR = "The Earth and Its Structure"
T_WEA = "Weathering and Landforms"
T_CLI = "Weather and Climate"
T_MAP = "Map Reading and Settlement"
T_POP = "Population and Migration"
T_NIG = "Regional Geography of Nigeria"
T_ECO = "Economic Geography"
T_ENV = "Environmental Issues"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- earth and structure
    (T_EAR, "Easy", "The layer of the earth on which people live and farm is the",
     "crust", "mantle", "core", "moho", "A",
     "The crust is the earth's outer skin."),
    (T_EAR, "Easy", "Molten rock that reaches the earth's surface through a vent is called",
     "lava", "magma", "lahar", "regolith", "A",
     "Magma becomes lava once it flows out."),
    (T_EAR, "Easy", "The rock family formed when molten material cools and hardens is",
     "igneous rock", "sedimentary rock", "metamorphic rock", "organic rock", "A",
     "Cooling magma and lava form igneous."),
    (T_EAR, "Medium", "Slate and marble, changed by great heat and pressure, belong to the",
     "metamorphic rocks", "igneous rocks", "sedimentary rocks", "volcanic ash beds", "A",
     "Heat and pressure transform old rocks."),
    (T_EAR, "Medium", "The endless movement of water between sea, air and land is the",
     "hydrological cycle", "rock cycle", "carbon cycle", "nitrogen cycle", "A",
     "Water circulates as vapour and rain."),
    (T_EAR, "Easy", "The numbered line that rings the earth at zero degrees latitude is the",
     "equator", "prime meridian", "tropic of Cancer", "date line", "A",
     "Zero latitude is the equator."),
    (T_EAR, "Easy", "Day and night follow each other because of the earth's",
     "rotation on its axis", "revolution round the sun", "tilt away from the sun", "distance from the sun", "A",
     "Spinning brings each side to light."),
    (T_EAR, "Medium", "Nigeria's yearly rainy season is brought by the",
     "south-west monsoon winds", "harmattan winds", "north-east trade winds", "land breezes", "A",
     "The moist monsoon bears the rains."),
    # ---------------------------------------------------------------- weathering and landforms
    (T_WEA, "Easy", "The gradual breaking down of rock where it lies, without removal, is",
     "weathering", "erosion", "deposition", "transportation", "A",
     "Weathering works in situ, no moving."),
    (T_WEA, "Medium", "Rocks split open by plant roots and burrowing animals undergo",
     "biological weathering", "chemical weathering", "physical weathering", "mass wasting", "A",
     "Living things pry the rock apart."),
    (T_WEA, "Medium", "Exfoliation, the peeling of outer rock layers, is caused mainly by",
     "repeated heating and cooling", "carbon dioxide in rain", "freezing of glacial ice", "growth of plant roots", "A",
     "Daily temperature swings flake rock."),
    (T_WEA, "Medium", "A slow-moving river of ice confined to a valley is a",
     "glacier", "delta", "dune", "watershed", "A",
     "Glaciers creep down high valleys."),
    (T_WEA, "Easy", "The Nigerian town famous as the meeting point of the Niger and the Benue is",
     "Lokoja", "Onitsha", "Yola", "Sokoto", "A",
     "The two great rivers meet at Lokoja."),
    (T_WEA, "Medium", "The Jos Plateau stands out on the map as a",
     "highland of volcanic origin", "riverine flood plain", "coastal lagoon belt", "field of sand hills", "A",
     "Old lava and granite raised it."),
    (T_WEA, "Hard", "Broad U-shaped valleys are carved mainly by",
     "glaciers", "rivers", "wind", "sea waves", "A",
     "Ice gouges valleys into U forms."),
    (T_WEA, "Hard", "In the desert, a lone dune shaped like a new moon is called a",
     "barchan", "seif dune", "inselberg", "wadi", "A",
     "Barchans curve like new moons."),
    # ---------------------------------------------------------------- weather and climate
    (T_CLI, "Easy", "A weather station records air pressure every day with a",
     "barometer", "thermometer", "hygrometer", "anemometer", "A",
     "Barometers weigh the air column."),
    (T_CLI, "Medium", "The water vapour air actually holds, compared with what it could hold, is its",
     "relative humidity", "absolute humidity", "saturation point", "dew point", "A",
     "It is a share of full capacity."),
    (T_CLI, "Easy", "The dry, dusty harmattan that reaches Nigeria in December is a",
     "north-east trade wind", "moist south-west monsoon", "cool sea breeze", "warm land breeze", "A",
     "It sweeps down from the Sahara."),
    (T_CLI, "Medium", "The climate of northern Nigeria is best classified as",
     "tropical continental", "equatorial", "mediterranean", "tropical maritime", "A",
     "Hot, with clear wet and dry terms."),
    (T_CLI, "Medium", "Rainfall around the Niger Delta is best described as",
     "heavy and almost all year", "scanty and seasonal", "winter maximum", "convectional snow", "A",
     "Months of rain drench the delta."),
    (T_CLI, "Easy", "Two of the chief elements of weather are",
     "rainfall and temperature", "rocks and relief", "latitude and soil", "population and trade", "A",
     "Weather is read from such elements."),
    (T_CLI, "Hard", "The belt where the tropical continental and tropical maritime air masses meet over West Africa is the",
     "ITCZ", "polar front", "horse latitude", "cyclone belt", "A",
     "The meeting line shifts with the sun."),
    (T_CLI, "Medium", "Insolation is best defined as",
     "solar energy reaching the earth", "heat from the earth's core", "reflection off the moon", "warmth of ocean currents", "A",
     "The sun's rays strike the surface."),
    # ---------------------------------------------------------------- map reading and settlement
    (T_MAP, "Medium", "On a topographic map, very steep slopes are shown by contour lines drawn",
     "close together", "far apart", "perfectly round", "broken and dashed", "A",
     "Height is packed into little space."),
    (T_MAP, "Easy", "The three-figure bearing of north-east is",
     "045 degrees", "090 degrees", "135 degrees", "270 degrees", "A",
     "Bearings run clockwise from north."),
    (T_MAP, "Medium", "A distance of 5 cm on a map with scale 1:50,000 stands for a ground distance of",
     "2.5 km", "25 km", "0.5 km", "5 km", "A",
     "Multiply by the map scale factor."),
    (T_MAP, "Medium", "A statement scale of 1 cm to 1 km is the same as a representative fraction of",
     "1:100,000", "1:1,000", "1:10,000", "1:50,000", "A",
     "Convert kilometres to centimetres."),
    (T_MAP, "Medium", "A spot height printed on a map gives the",
     "exact height of one point", "average height of a ridge", "depth of a river valley", "width of a road", "A",
     "One surveyed point, one figure."),
    (T_MAP, "Easy", "Houses clustered round a village square and church form a",
     "nucleated settlement", "dispersed settlement", "linear settlement", "isolated settlement", "A",
     "Buildings bunch around a centre."),
    (T_MAP, "Easy", "Buildings strung out in a line along one main road form a",
     "linear settlement", "nucleated settlement", "dispersed settlement", "scattered farmstead", "A",
     "The road strings the houses out."),
    (T_MAP, "Medium", "The high ground dividing the streams of two separate river systems is a",
     "watershed", "water table", "flood plain", "delta", "A",
     "Rivers part ways at the crest."),
    # ---------------------------------------------------------------- population and migration
    (T_POP, "Easy", "Nigeria counts her people once every ten years through a",
     "census", "by-election", "sample poll", "budget audit", "A",
     "The census counts heads by law."),
    (T_POP, "Medium", "The 2006 national census placed Nigeria's population at about",
     "140 million", "60 million", "300 million", "40 million", "A",
     "The count neared 140 million."),
    (T_POP, "Easy", "The mass movement of villagers into Nigerian cities is called",
     "rural-urban migration", "international migration", "seasonal migration", "daily commuting", "A",
     "Countryside people flow to towns."),
    (T_POP, "Medium", "The strongest pull factor drawing youths to Lagos is",
     "better urban jobs", "rural land disputes", "village festivals", "farm mechanisation", "A",
     "Work and wages pull them cityward."),
    (T_POP, "Medium", "A population with many children and few old people, like Nigeria's, shows a",
     "wide-based pyramid", "narrow-based pyramid", "rectangular pyramid", "inverted pyramid", "A",
     "Broad base, many young dependants."),
    (T_POP, "Hard", "Natural population growth is births minus deaths plus",
     "net migration", "gross enrolment", "literacy rate", "life expectancy", "A",
     "Migration completes the balance."),
    (T_POP, "Medium", "Over-population in Lagos has led mainly to",
     "sprawl and slum growth", "rising farm sizes", "falling house rents", "empty classrooms", "A",
     "Cities bulge beyond services."),
    (T_POP, "Hard", "A town that grew big at the crossing of two busy roads is best described as",
     "a nodal town", "a market garden", "a ghost town", "a resort town", "A",
     "Routes meet and trade gathers."),
    # ---------------------------------------------------------------- regional geography of nigeria
    (T_NIG, "Hard", "Nigeria's mainland longitudes run roughly from",
     "3 degrees E to 15 degrees E", "1 degree W to 5 degrees E", "10 degrees W to 2 degrees E", "20 degrees E to 30 degrees E", "A",
     "She spans about twelve degrees."),
    (T_NIG, "Medium", "Nigeria's highest peak, Chappal Waddi, stands on the",
     "Mambila Plateau", "Jos Plateau", "Obudu hills", "Idanre hills", "A",
     "The Mambila edge is highest."),
    (T_NIG, "Medium", "The Chad Basin of north-eastern Nigeria is underlain mainly by",
     "sedimentary rocks", "basaltic lava flows", "granite batholiths", "coral reefs", "A",
     "Old lake deposits fill the basin."),
    (T_NIG, "Medium", "The Niger Delta is watered by a dense network of",
     "distributaries", "tributaries", "wadis", "glacier snouts", "A",
     "The river splits seaward again."),
    (T_NIG, "Easy", "The vegetation belt of Nigeria that faces the Sahara directly is the",
     "Sahel savanna", "mangrove swamp", "rainforest", "derived savanna", "A",
     "Thorny scrub marks the far north."),
    (T_NIG, "Easy", "Trees of the southern rainforest are prized chiefly for their",
     "hardwood timber", "grazing pasture", "cotton fibres", "groundnut oil", "A",
     "Iroko and mahogany sell well."),
    (T_NIG, "Medium", "The River Niger flows into Nigeria from",
     "the north-west", "the south-east", "Lake Chad", "the Cameroon hills", "A",
     "It enters through Kebbi state."),
    (T_NIG, "Hard", "The rivers Sokoto and Rima drain their basin into the",
     "River Niger", "Lake Chad", "Benue trough", "Cross River", "A",
     "They join the Niger near Jebba."),
    # ---------------------------------------------------------------- economic geography
    (T_ECO, "Easy", "Which region holds most of Nigeria's oil wells?",
     "the Niger Delta", "the Jos Plateau", "the Chad Basin", "the Mambila hills", "A",
     "Wells crowd the delta creeks."),
    (T_ECO, "Medium", "Water dropping through the wall at Kainji chiefly serves to",
     "turn electricity turbines", "attract foreign tourists", "control desert locusts", "cool refinery plants", "A",
     "Falling water turns turbines."),
    (T_ECO, "Medium", "Nigeria's first railways were laid chiefly to",
     "move farm produce to ports", "carry tourists to game parks", "link Nigeria with Ghana", "haul crude oil pipelines", "A",
     "Groundnut and cocoa needed outlets."),
    (T_ECO, "Medium", "The economic grouping that binds Nigeria to her West African neighbours is",
     "ECOWAS", "OPEC", "OAU", "NAFTA", "A",
     "West African states trade as one."),
    (T_ECO, "Medium", "Cattle rearing rules the northern savanna because of the region's",
     "grass cover and fewer tsetse", "year-round snow cover", "mangrove swamps", "deep rainforests", "A",
     "Open grass and healthy herds."),
    (T_ECO, "Easy", "Visitors to Yankari Game Reserve support Nigeria's",
     "tourism industry", "steel industry", "oil industry", "textile industry", "A",
     "Wildlife and springs draw guests."),
    (T_ECO, "Medium", "The bulk of Nigeria's manufacturing plants are clustered in",
     "Lagos and the south-west", "Borno and Yobe axis", "Sokoto-Katsina axis", "Bayelsa swamps alone", "A",
     "Industry thickens near the ports."),
    (T_ECO, "Hard", "Irrigation schemes around Lake Chad survive on the lake's",
     "seasonal flooding waters", "melting mountain snow", "underground petroleum", "coastal ocean tides", "A",
     "Floods refill the canal systems."),
    # ---------------------------------------------------------------- environmental issues
    (T_ENV, "Hard", "The gullies eating farmland at Nanka and Agulu in Anambra grow worse through",
     "deforestation and poor farming", "excess afforestation", "thick grass cover", "flat table land", "A",
     "Bare slopes wash away fast."),
    (T_ENV, "Medium", "The disastrous floods that hit Lokoja and Loko in 2012 came mainly from",
     "swollen rivers and heavy rain", "burst oil pipelines", "ocean tsunamis", "volcanic eruptions", "A",
     "Rivers overtopped their banks."),
    (T_ENV, "Medium", "Desert encroachment in Nigeria's far north is checked mainly by",
     "planting shelter belts", "burning grass yearly", "felling rain trees", "draining wetlands", "A",
     "Tree lines brake the desert wind."),
    (T_ENV, "Medium", "The ozone layer suffers depletion mainly from",
     "chlorofluorocarbons", "carbon dioxide gas", "nitrogen gas", "water vapour", "A",
     "CFC gases thin the shield."),
    (T_ENV, "Easy", "Global warming is best described as",
     "a rise in world temperatures", "a fall in sea levels", "cooling of the tropics", "widening deserts alone", "A",
     "The earth's heat balance rises."),
    (T_ENV, "Medium", "Yankari and Cross River are preserved from hunters chiefly as",
     "game reserves", "mining camps", "deep seaports", "cattle ranches", "A",
     "Rare animals find refuge there."),
    (T_ENV, "Easy", "The cheapest first step against flooding in Nigerian cities is to",
     "clear blocked drains", "widen the ocean shelf", "build taller dunes", "sink more boreholes", "A",
     "Free drains carry storm water."),
    (T_ENV, "Medium", "Gas flaring in the Delta chiefly damages the",
     "air and farmland quality", "radio signals", "ocean tides", "solar panels", "A",
     "Soot and heat sour the air."),
]

build_batch(
    S,
    "batch_077_waec_geography.json",
    "077",
    "WAEC Geography Paper 1 round 1 (Round 16e): the WASSCE syllabus with "
    "FRESH angles - Nigeria-specific stems (Lokoja confluence, Chappal Waddi, "
    "Chad Basin, Kainji Dam, Sokoto-Rima, 2006 census, Nanka gullies, 2012 "
    "floods), map-work calculations (045 degrees bearing, 5 cm at 1:50,000) "
    "and scenario items - because the near-dup scan checks every item "
    "against the JAMB, WAEC and NECO banks INCLUDING the big JAMB Geography "
    "banks (037-038) and the 87-item NECO Geography bank. Topics: the earth, "
    "weathering and landforms, weather and climate, map reading and "
    "settlement, population, regional geography of Nigeria, economic "
    "geography, environmental issues.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
