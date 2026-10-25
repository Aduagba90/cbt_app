"""Batch 178 - NECO Geography round 6 (NECO top-up, R34).

Grows NECO Geography from 209 toward ~245 with angles not yet in
the bank: the core's iron and nickel; temperature falling with
latitude; the June solstice; the ITCZ where air masses meet; the
tropical maritime air mass from the Atlantic; the anemometer's
speed and the hygrometer's humidity; maximum and minimum
thermometers; dew by radiation cooling; the lagoon behind its sand
spit; the Niger's arcuate delta; tides pulled by moon and sun;
spring tides at full and new moon; communal land tenure; market
gardening; quarrying; dendritic drainage; the south's perennial
streams; runoff when rain beats infiltration; dam displacement;
Obudu's cool ranch; Ikogosi's warm springs; Yankari's game;
the cold current cooling a coast; the Niger-Benue trough;
the Sokoto plains; Cross River rainforest; artesian water under
pressure; traction and saltation; the desert's wide daily range;
cumulonimbus and thunder; the Niger's seasonal regime; Onitsha
the river port. Scanned against NECO rounds 1-5, WAEC Geography
(all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch178.py -> content/batch_178_neco_geo6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_EAR = "The Earth and Its Structure"
T_CLI = "Climate"
T_MAP = "Map Reading and Interpretation"
T_RIV = "River and Groundwater"
T_POP = "Population and Settlement"
T_ECO = "Economic Geography"
T_REG = "Regional Geography of Nigeria"
T_ENV = "Environmental Issues"
T_LAK = "Lakes and Water Bodies"

PASSAGES = []
PQ = []

Q = [
    (T_EAR, "Hard", "The earth's core is believed to consist chiefly of two metals, namely",
     "iron and nickel", "copper and zinc",
     "gold and silver", "aluminium and tin", "A",
     "The dense heart of the planet is a metal pair."),
    (T_EAR, "Medium", "Places at higher latitudes away from the equator are generally cooler because the sun's rays strike them",
     "at a slanting angle", "directly overhead",
     "with greater force", "through thinner air only", "A",
     "Slanting rays spread their heat over more ground."),
    (T_EAR, "Medium", "The day on which the northern hemisphere enjoys its longest daylight is about",
     "June 21", "March 21",
     "September 23", "December 22", "A",
     "The summer solstice gives the north its longest day.", "21"),
    (T_CLI, "Hard", "Rain over West Africa is chiefly triggered along the meeting line of the two great air masses, known as the",
     "Intertropical Convergence Zone", "belt of horse latitudes",
     "polar front", "doldrum calm of the poles", "A",
     "The ITCZ follows the sun and brings the rains."),
    (T_CLI, "Medium", "The moist south-west winds that bring Nigeria's wet season blow in from the",
     "Atlantic Ocean", "Sahara Desert",
     "Mediterranean Sea", "Red Sea hills", "A",
     "The tropical maritime air mass sails in from the ocean."),
    (T_CLI, "Easy", "The instrument whose spinning cups reveal how fast the wind blows is the",
     "anemometer", "wind vane",
     "barometer", "hygrometer", "A",
     "The vane shows direction; the cups measure speed."),
    (T_CLI, "Medium", "The amount of water vapour present in the air is measured with the",
     "hygrometer", "rain gauge",
     "barograph", "thermograph", "A",
     "Humidity is the hygrometer's whole business."),
    (T_CLI, "Medium", "In a weather station, the highest and lowest temperatures of a day are read from the",
     "maximum and minimum thermometers", "wet and dry bulbs",
     "ordinary laboratory thermometers", "thermograph drums only", "A",
     "One holds the day's peak, the other its floor."),
    (T_CLI, "Medium", "Dew forms on grass in the early morning when moist air close to the ground is",
     "chilled by the cooling surface", "warmed by the rising sun",
     "squeezed out by wind", "lifted by convection currents", "A",
     "The cold leaf squeezes the air past its dew point."),
    (T_CLI, "Hard", "Temperatures in the Sahara swing widely between day and night because the desert",
     "lacks the cloud and moisture that hold heat", "lies under permanent snow",
     "is heated from below by volcanoes", "enjoys rainfall every night", "A",
     "Dry, clear air lets the day's heat escape fast."),
    (T_CLI, "Easy", "The towering dark cloud that brings thunderstorms is the",
     "cumulonimbus", "cirrus",
     "stratus", "altocumulus", "A",
     "Its anvil top towers into the high sky."),
    (T_MAP, "Medium", "Lagos and other coastal lagoons are separated from the open sea by",
     "long sand bars built by waves", "walls of coral animals",
     "banks of river mud", "rows of mangrove trees", "A",
     "Waves heap the sand bar across the bay."),
    (T_RIV, "Medium", "The Niger builds its delta at the sea in the shape of a rounded triangle described as",
     "arcuate", "bird's foot",
     "estuarine", "cusped", "A",
     "The great fan spreads its arms round the gulf."),
    (T_RIV, "Easy", "Twice each day the ocean surface rises and falls along the coast. The chief cause is",
     "pull of the moon and sun", "blowing of the trade winds",
     "melting of polar ice", "spinning of the earth alone", "A",
     "The moon's drag lifts the ocean bulge."),
    (T_RIV, "Hard", "Unusually high spring tides occur around the time of the",
     "full and new moon", "first and third quarter",
     "moon's crossing of the equator", "longest night only", "A",
     "Sun and moon pull together then."),
    (T_RIV, "Hard", "The load of a river is dragged along its bed as rolling boulders and sliding gravel by a process called",
     "traction", "saltation",
     "suspension", "solution", "A",
     "The heaviest cargo never leaves the floor."),
    (T_RIV, "Medium", "The bouncing movement in which a river's sand grains hop along the bed is",
     "saltation", "traction",
     "solution", "flocculation", "A",
     "Grain after grain leaps and lands downstream."),
    (T_RIV, "Medium", "Rivers of southern Nigeria flow all year round because the region enjoys",
     "rainfall in every month", "snow melt from the Jos heights",
     "water piped from Lake Chad", "underground streams from the Sahara", "A",
     "Perennial streams are fed the whole year."),
    (T_RIV, "Hard", "Rain that fails to soak into the ground and instead flows away over the surface is",
     "runoff", "infiltration",
     "percolation", "transpiration", "A",
     "Where soaking fails, the water runs off."),
    (T_RIV, "Hard", "Where a water-bearing rock is trapped between impermeable layers and the water rises under its own pressure, an artesian",
     "well can be sunk", "spring never forms",
     "lake dries out", "spring turns saline always", "A",
     "Pressure pushes the water up the bore."),
    (T_RIV, "Medium", "The discharge of the Niger at Lokoja rises and peaks with the seasons each year. This yearly pattern is the river's",
     "regime", "load",
     "gradient", "diversion", "A",
     "Every river keeps its own seasonal rhythm."),
    (T_LAK, "Medium", "A serious social cost of dam construction, seen at Kainji, is the",
     "displacement of whole communities", "loss of the river's source",
     "drying of the Atlantic Ocean", "end of fishing downstream", "A",
     "Old villages sank beneath the lake."),
    (T_POP, "Medium", "The traditional system in which farmland belongs to the family or community rather than to an individual is",
     "communal tenure", "freehold title",
     "leasehold tenure", "state ownership", "A",
     "The community holds the land in trust for all."),
    (T_ECO, "Medium", "Vegetable farmers around Lagos who grow perishable crops close to the city market practise",
     "market gardening", "nomadic herding",
     "plantation agriculture", "shifting cultivation", "A",
     "Fresh vegetables race the short mile to market."),
    (T_ECO, "Medium", "The opening up of rock for granite, limestone and gravel is called",
     "quarrying", "alluvial mining",
     "strip cropping", "offshore drilling", "A",
     "The hillside is cut for its stone."),
    (T_ECO, "Easy", "The Yankari Game Reserve, famous for its hot springs and elephants, is located in",
     "Bauchi state", "Borno state",
     "Kwara state", "Cross River state", "A",
     "The savanna reserve lies in Bauchi."),
    (T_ECO, "Medium", "The warm springs that draw many tourists to Ekiti State bubble up at",
     "Ikogosi", "Olumo",
     "Idanre", "Zuma", "A",
     "Warm and cold springs meet at Ikogosi."),
    (T_ECO, "Medium", "The Obudu Cattle Ranch thrives in the east of Nigeria because its high plateau enjoys",
     "a cool, temperate-like climate", "year-round flooding",
     "salt licks for the herds", "rail links to the coast", "A",
     "The heights are cool enough for exotic cattle."),
    (T_ECO, "Hard", "A cold ocean current flowing along a coast tends to make the adjoining land",
     "cool and dry", "warm and wet",
     "stormy and hot", "fog-free and humid", "A",
     "The Benguela chills Namibia's coast to desert."),
    (T_REG, "Medium", "The broad lowland through which the Niger and Benue flow is underlain mainly by",
     "sedimentary rocks", "ancient granite shields",
     "volcanic ash beds", "metamorphic schists only", "A",
     "Sandstones and shales fill the great trough."),
    (T_REG, "Medium", "The river plains drained by the Rima and Sokoto rivers lie in Nigeria's",
     "north-west", "south-east",
     "coastal belt", "central highlands", "A",
     "Sokoto's plains stretch toward Niger Republic."),
    (T_REG, "Medium", "The rainforest remnants of the Cross River basin lie mainly in",
     "the south-east", "the far north-east",
     "the middle belt", "the FCT", "A",
     "Deep forest survives on the Cameroun border."),
    (T_ECO, "Medium", "Onitsha, Onitsha North's famous commercial town, serves the east as a",
     "river port on the Niger", "deep-sea port for tankers",
     "mountain railway junction", "border customs post", "A",
     "Barges call at its Niger-side wharves."),
    (T_ENV, "Medium", "Removing vegetation for farms and timber exposes the soil chiefly to",
     "erosion by rain and wind", "overnight freezing",
     "volcanic burial", "river deposition", "A",
     "Bare ground washes and blows away."),
    (T_MAP, "Hard", "The drainage pattern in which streams branch again and again like a tree is",
     "dendritic", "radial",
     "centripetal", "trellis", "A",
     "Every tributary twigs from the trunk stream."),
]

build_batch(
    S,
    "batch_178_neco_geo6.json",
    "178",
    "NECO Geography round 6 (R34 top-up): core of iron and nickel; "
    "slanting rays at high latitudes; the June 21 solstice; the "
    "ITCZ where air masses meet; the Atlantic source of the wet-"
    "season winds; anemometer speed, hygrometer humidity, maximum "
    "and minimum thermometers; dew by radiation cooling; the "
    "desert's wide daily range; cumulonimbus thunderheads; the "
    "lagoon behind its sand spit; the Niger's arcuate delta; tides "
    "by moon and sun; spring tides at full and new moon; traction "
    "and saltation along the bed; the south's perennial streams; "
    "runoff beating infiltration; the artesian well; the river's "
    "regime; dam displacement at Kainji; communal tenure; market "
    "gardening; quarrying; Yankari in Bauchi; Ikogosi's warm "
    "springs; Obudu's cool ranch; cold currents cool coasts; the "
    "sedimentary trough; Sokoto's plains; Cross River forest; "
    "Onitsha river port; bared soil and erosion; dendritic "
    "drainage. Scanned against NECO rounds 1-5, WAEC Geography "
    "(all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
