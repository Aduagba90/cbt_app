"""Batch 239 - NECO Geography round 5 (NECO top-up, R49).

Grows NECO Geography from 266 toward ~291 with angles verified
absent from the whole Geography pool (1,103 items across JAMB, WAEC
and NECO) and cleared of cross-subject twins via db sweep. Fresh
angles: leap year; river regime; anabatic and katabatic winds;
climograph; highland climate; push and pull factors; site and
situation; urban functions; arable farming; industrial inertia;
industrial pollution; Andes; Australia's wool; Great Barrier Reef;
Jos Plateau climate; Trunk A roads; Kimberley diamonds; Copperbelt;
Egyptian cotton; Kenya's tourism; shelterbelts; Fouta Djallon;
bearing on a map; measuring distance on a map; gradient. Avoided as
banked or cross-twins: railway lines, airports, Japan industry
(Geo banked), warehouse functions (Commerce), cottage industry
(Econ), industrial estate (Econ Lekki), Malthus (Econ), climate
change family, postal services, isotherm/isobar/isohyet families,
map legend, dew point, lapse rate calc, aspect, footloose,
agglomeration, Kimberley-adjacent mining families (tin Jos, coal
Enugu, iron Itakpe, limestone Ewekoro all banked), cocoa/groundnut
crops, trans-Siberian, Suez, St Lawrence, Victoria Falls, Ruhr,
river capture, longshore drift, rainforest layers, freshwater
swamp, taungya, Fouta-free greps, mountain/lake/dam families,
Nigeria latitude bounds, census, population pyramid, demographic
transition, vegetation belts, shelterbelt-free windbreak greps.

    python3 scripts/build_neco_batch239.py -> content/batch_239_neco_geo5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_EARTH = "The Earth and Its Structure"
T_RIVER = "River and Groundwater"
T_CLIM = "Climate"
T_POP = "Population and Settlement"
T_AGRI = "Agricultural Systems"
T_ECON = "Economic Geography"
T_ECONF = "Economic Geography Further"
T_ENV = "Environmental Issues"
T_NIG = "Regional Geography of Nigeria"
T_TRAN = "Transport"
T_LAKES = "Lakes and Water Bodies"
T_MAP = "Map Reading and Interpretation"

PASSAGES = []
PQ = []

Q = [
    (T_EARTH, "Easy", "The Earth takes about 365¼ days to complete one journey round the Sun. The extra quarter-day is collected every fourth year as",
     "29 February", "30 February",
     "a second August", "a double December", "A",
     "Four quarters are saved up for one leap day."),
    (T_RIVER, "Medium", "The pattern of a river's flow through the year — high and full in the rainy months, low and thin in the dry months — is called its",
     "regime", "region",
     "load", "gradient", "A",
     "A river has its seasons, like a farmer."),
    (T_CLIM, "Hard", "By day, in mountain country, the sun heats the slopes and air flows gently up the valley side; by night the cooled air slides down again. These local winds are called",
     "anabatic and katabatic winds", "trade and westerly winds",
     "cyclonic and anticyclonic winds", "onshore and offshore winds", "A",
     "The valley breathes in by day and out by night."),
    (T_CLIM, "Medium", "The graph on which the temperature of a place is drawn as a line and the rainfall as bars, month by month, so that both can be read together, is called a",
     "climograph", "hyetograph",
     "thermograph", "barograph", "A",
     "One picture, two stories of the year's weather."),
    (T_CLIM, "Medium", "Cool temperatures throughout the year, heavy relief rainfall on the windward slopes and a rain shadow on the leeward side are features of the",
     "highland climate", "hot desert climate",
     "Mediterranean climate", "equatorial climate", "A",
     "The higher the land, the cooler the year."),
    (T_POP, "Medium", "Unemployment and poor schools that drive young people away from a village are examples of push factors. Better jobs and city lights that attract them to Lagos are examples of",
     "pull factors", "press factors",
     "plan factors", "pilot factors", "A",
     "One set pushes from behind; the other pulls from ahead."),
    (T_POP, "Medium", "The actual piece of ground on which a settlement stands — dry land by a river crossing — is its site, while its position in relation to other places — at the meeting of trade routes — is its",
     "situation", "size",
     "structure", "sector", "A",
     "The site is where it sits; the situation is what surrounds it."),
    (T_POP, "Easy", "A town may serve as a market centre, an administrative headquarters, a rail junction and a centre of education all at once. These are the town's",
     "functions", "formations",
     "foundations", "franchises", "A",
     "Ask what a town does, and you have named it."),
    (T_AGRI, "Easy", "The cultivation of crops in fields and gardens, as distinct from the rearing of animals, is called",
     "arable farming", "pastoral farming",
     "mixed farming", "fish farming", "A",
     "Plough and hoe, not herd and byre."),
    (T_ECON, "Hard", "A factory sometimes remains at its old site long after the original advantages — coal, perhaps — have gone, simply because the buildings, workers and networks are already there. This is called",
     "industrial inertia", "industrial invasion",
     "industrial insertion", "industrial insulation", "A",
     "The old roots hold the factory to its ground."),
    (T_ENV, "Medium", "Wastes from factories — chemicals poured into rivers and smoke sent into the air — that harm water, air and land around industrial areas constitute",
     "industrial pollution", "industrial dissolution",
     "industrial resolution", "industrial recession", "A",
     "The smokestack's unpaid bill falls on the neighbourhood."),
    (T_ECON, "Medium", "The world's longest mountain range, running down the western side of South America, is the",
     "Andes", "Alps",
     "Rockies", "Atlas", "A",
     "Seven thousand kilometres of climbing western America."),
    (T_ECON, "Medium", "Australia is one of the world's chief exporters of wool because huge flocks of sheep graze its",
     "extensive grasslands", "dense rainforests",
     "northern tundra", "mountain glaciers", "A",
     "Merino sheep and open plains built the wool trade."),
    (T_ECONF, "Easy", "The world's largest coral structure, lying off the north-east coast of Australia in the Pacific, is the",
     "Great Barrier Reef", "Great Wall of China",
     "Grand Canyon", "Great African Rift", "A",
     "A living wall of coral two thousand kilometres long."),
    (T_NIG, "Medium", "Because of its height, the Jos Plateau enjoys a climate that is markedly",
     "cooler than the lowlands", "wetter than the coastlands",
     "hotter than the Sahara", "windier than the seashore", "A",
     "Visitors pack sweaters for a Nigerian summer there."),
    (T_TRAN, "Medium", "In Nigeria, the roads built and maintained by the federal government, linking the states and the big cities, are classified as",
     "Trunk A roads", "Trunk F roads",
     "local council roads", "estate roads", "A",
     "The main arteries of the nation belong to Abuja."),
    (T_ECON, "Hard", "The South African town that grew rich on diamonds after the first stones were found there in the nineteenth century, and gave its name to a famous mining process, is",
     "Kimberley", "Johannesburg",
     "Cape Town", "Durban", "A",
     "The hole it dug is visible from the sky."),
    (T_ECON, "Hard", "The mining region along the Zambia–Congo border, one of the world's richest sources of copper, is known as the",
     "Copperbelt", "Gold Coast",
     "Iron Range", "Diamond Field", "A",
     "The metal in the wire of old radios came from there."),
    (T_AGRI, "Hard", "Egypt grows fine, long-staple cotton in large quantities chiefly because of",
     "irrigation water from the Nile", "heavy equatorial rainfall",
     "harmattan winds", "sea breezes from the Red Sea", "A",
     "The desert blooms wherever the river is led."),
    (T_ECON, "Medium", "Kenya earns much foreign exchange from visitors who come to see the lions, elephants and wildebeest of its game parks. This industry is",
     "wildlife tourism", "nomadic herding",
     "plantation farming", "deep-sea fishing", "A",
     "The lion, in his own country, is a wage earner."),
    (T_ENV, "Medium", "Rows of trees planted across the path of the dry north-east winds in northern Nigeria, to shield farmland from desiccating dust and heat, are called",
     "shelterbelts", "shatterbelts",
     "greenhouses", "wind breaks of iron", "A",
     "A living wall that stands in the wind's way."),
    (T_RIVER, "Medium", "The River Niger, West Africa's great waterway, takes its rise in the",
     "the Fouta Djallon highlands", "the hills of Bauchi state",
     "the mountains of Ethiopia", "the Drakensberg mountains", "A",
     "From Guinea's highlands it runs 4,000 km to the sea."),
    (T_MAP, "Medium", "On a topographic map, the direction of one point from another, measured in degrees clockwise from north, is called the",
     "bearing", "gradient",
     "latitude", "relief", "A",
     "North is zero; east is ninety; the compass tells the rest."),
    (T_MAP, "Medium", "To find the real distance between two towns on a map, the student measures the length between them on paper with a ruler and then",
     "multiplies it by the scale of the map", "divides it by the relief",
     "counts the rivers crossed", "multiplies it by the latitude", "A",
     "One centimetre on paper may be one kilometre on land."),
    (T_MAP, "Hard", "On a map, the steepness of a slope — found by dividing the difference in height between two points by the horizontal distance between them — is called the",
     "gradient", "contour interval",
     "vertical exaggeration", "relief displacement", "A",
     "One in ten is a climb; one in two is a mountain path."),
]

build_batch(
    S,
    "batch_239_neco_geo5.json",
    "239",
    "NECO Geography round 5 (R49 top-up): leap year; river regime; "
    "anabatic and katabatic winds; climograph; highland climate; "
    "push and pull factors; site and situation; urban functions; "
    "arable farming; industrial inertia; industrial pollution; "
    "Andes; Australian wool; Great Barrier Reef; Jos Plateau "
    "climate; Trunk A roads; Kimberley diamonds; Copperbelt; "
    "Egyptian cotton; Kenya wildlife tourism; shelterbelts; Fouta "
    "Djallon source of the Niger; bearing; measuring distance; "
    "gradient. Scanned against the whole Geography pool (JAMB, WAEC "
    "and NECO stems) and cleared of cross-subject twins.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
