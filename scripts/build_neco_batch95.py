"""Batch 095 - WAEC Geography round 2 (WAEC lift, Round 19).

WAEC Geography Paper 1 draws 50 items; the bank stood at 64. This lift adds
fresh items - Tropic of Cancer, Greenwich, June 21, solar eclipse,
troposphere and stratosphere, limestone, carbonation, soil creep,
abrasion, saltation, springs, mushroom rocks, stalactites, wave-cut
platforms, caldera, earthquake focus and epicentre, seismograph, linear
scale, hill shading, settlement site, plantation farming, Jos tin,
Itakpe iron, gas-fired power, industry location factors, Rift Valley
lakes, desertification, renewable energy - scanned against WAEC r1, NECO
rounds 1-2 and the JAMB banks.

    python3 scripts/build_neco_batch95.py -> content/batch_095_waec_geography2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_EAR = "The Earth and the Atmosphere"
T_ROC = "Rocks and Weathering"
T_RIV = "Rivers and Water"
T_WIND_COAST = "Wind and Coastal Landforms"
T_MAP = "Maps and Surveying"
T_SET = "Settlement and Population"
T_ECO = "Agriculture, Mining and Industry"
T_AFR = "Africa and Nigeria"
T_ENV = "Environmental Management"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- earth and atmosphere
    (T_EAR, "Easy", "The line of latitude at about 23.5 degrees north of the equator is the",
     "Tropic of Cancer", "Tropic of Capricorn", "Arctic Circle", "Equator", "A",
     "The sun is overhead there in June."),
    (T_EAR, "Medium", "The meridian from which longitude is counted is the",
     "Greenwich meridian", "International Date Line", "equinoctial line", "tropic line", "A",
     "Zero degrees passes through London."),
    (T_EAR, "Medium", "In the northern hemisphere, the longest day of the year falls around",
     "21 June", "21 March", "23 September", "21 December", "A",
     "The June solstice brings it."),
    (T_EAR, "Easy", "When the moon passes between the sun and the earth, the result is a",
     "solar eclipse", "lunar eclipse", "spring tide", "neap tide", "A",
     "The moon's shadow falls on us."),
    (T_EAR, "Medium", "Nearly all the world's weather happens in the",
     "troposphere", "stratosphere", "mesosphere", "exosphere", "A",
     "The lowest layer holds the clouds."),
    (T_EAR, "Medium", "The layer of the atmosphere that shields the earth from harmful radiation is the",
     "stratosphere with its ozone", "troposphere with dust", "mesosphere with ice", "thermosphere with heat", "A",
     "Ozone absorbs the ultraviolet."),
    # ---------------------------------------------------------------- rocks and weathering
    (T_ROC, "Easy", "Limestone and sandstone belong to the rock family that is",
     "sedimentary", "igneous", "metamorphic", "volcanic", "A",
     "They settled layer upon layer."),
    (T_ROC, "Hard", "Rain water charged with carbon dioxide dissolves limestone in the process called",
     "carbonation", "hydration", "oxidation", "solution", "A",
     "The weak acid eats the rock."),
    (T_ROC, "Medium", "The slow downhill creep of soil particles, especially on wet slopes, is",
     "soil creep", "landslide", "rockfall", "earthflow", "A",
     "Creep moves inches a year."),
    (T_ROC, "Medium", "A rock mass broken into huge blocks that race downhill is a",
     "landslide", "soil creep", "mud flow", "solifluction", "A",
     "The slide roars down at once."),
    # ---------------------------------------------------------------- rivers
    (T_RIV, "Hard", "The force of water alone wearing away the river bed is",
     "hydraulic action", "abrasion", "attrition", "corrosion", "A",
     "Water pressure prys and plucks."),
    (T_RIV, "Hard", "Sand and pebbles grinding the river channel as they move form the process of",
     "abrasion", "solution", "saltation", "deposition", "A",
     "The load files the channel smooth."),
    (T_RIV, "Hard", "Bounced movement of medium particles along the river bed is",
     "saltation", "solution", "suspension", "traction", "A",
     "The grains hop downstream."),
    (T_RIV, "Medium", "Where the water table meets the ground surface, water flows out as a",
     "spring", "well", "geyser", "oasis", "A",
     "The hillside weeps a spring."),
    (T_RIV, "Hard", "Rain that soaks underground and rests on impermeable rock builds up the",
     "water table", "aquiclude", "perched lake", "artesian basin", "A",
     "The saturated top is the table."),
    # ---------------------------------------------------------------- wind and coasts
    (T_WIND_COAST, "Medium", "A rock that stands on a slender base after wind erosion has worn its middle is the",
     "rock pedestal", "inselberg", "tor", "mesa", "A",
     "The mushroom shape tells the wind."),
    (T_WIND_COAST, "Hard", "The icicle-like limestone formations hanging from a cave roof are",
     "stalactites", "stalagmites", "stalagnates", "sinkholes", "A",
     "Dripping water drops the stone."),
    (T_WIND_COAST, "Medium", "The flat rock surface left where waves have cut back a cliff is the",
     "wave-cut platform", "beach berm", "spit", "stack", "A",
     "Low tide uncovers the shelf."),
    (T_WIND_COAST, "Medium", "A detached pillar of rock standing in the sea away from a cliff is a",
     "stack", "spit", "bar", "cove", "A",
     "The roof fell, the pillar stayed."),
    # ---------------------------------------------------------------- vulcanism and earthquakes
    (T_EAR, "Hard", "A huge basin formed when a volcano's summit collapses after an eruption is a",
     "caldera", "crater", "sill", "dyke", "A",
     "The crown caved into the vent."),
    (T_EAR, "Medium", "The point underground where an earthquake begins is the",
     "focus", "epicentre", "fault line", "seismograph point", "A",
     "The shaking starts at depth."),
    (T_EAR, "Easy", "The point on the surface directly above an earthquake's origin is the",
     "epicentre", "focus", "core", "mantle", "A",
     "Damage is worst around it."),
    (T_EAR, "Easy", "The instrument that records the strength of earthquakes is the",
     "seismograph", "barograph", "thermograph", "hygrograph", "A",
     "Its needle traces the tremors."),
    # ---------------------------------------------------------------- maps and surveying
    (T_MAP, "Medium", "A scale drawn as a line marked in kilometres beside the map is a",
     "linear scale", "statement scale", "representative fraction", "grid scale", "A",
     "You measure with the bar."),
    (T_MAP, "Hard", "Showing relief by shading the slopes as if light falls from the north-west is",
     "hill shading", "layer colouring", "hachuring", "contouring", "A",
     "Shadows suggest the heights."),
    (T_MAP, "Medium", "A vertical slice drawn across a map to show the shape of the land along that line is a",
     "cross-section", "long profile", "watershed line", "transect chart", "A",
     "It exposes the ups and downs."),
    # ---------------------------------------------------------------- settlement and population
    (T_SET, "Medium", "Early settlers commonly chose village sites beside rivers mainly to secure",
     "water supply", "gold deposits", "cool winds", "road metal", "A",
     "Daily life needs the river."),
    (T_SET, "Medium", "A town whose main work is serving a farming region with markets and services is a",
     "market town", "mining town", "garrison town", "resort town", "A",
     "The farms feed its trade."),
    (T_SET, "Medium", "Life expectancy at birth measures the average number of",
     "years a newborn may live", "children a woman bears", "people per doctor", "deaths per thousand", "A",
     "It reads the lifespan clock."),
    # ---------------------------------------------------------------- agriculture, mining, industry
    (T_ECO, "Medium", "A huge farm of one cash crop run by a company is a",
     "plantation", "peasant farm", "cooperative plot", "kitchen garden", "A",
     "One crop, one estate, many workers."),
    (T_ECO, "Medium", "Tin mining on the Jos Plateau is concentrated around",
     "Bukuru and Barkin Ladi", "Itakpe and Ajaokuta", "Ilesha and Iperindo", "Udi and Ngwo", "A",
     "The plateau's cassiterite belt."),
    (T_ECO, "Hard", "Nigeria's main iron ore deposits at Itakpe feed the steel complex at",
     "Ajaokuta", "Aladja", "Katsina", "Sapele", "A",
     "Ore rides the rail to the plant."),
    (T_ECO, "Medium", "Gas-fired power stations burn natural gas chiefly because Nigeria",
     "flares less and uses the gas", "lacks any coal at all", "imports all its fuel", "has no rivers for dams", "A",
     "The switch turns waste to watts."),
    (T_ECO, "Medium", "A cement factory locating beside a limestone quarry is chasing which factor?",
     "raw materials", "market", "labour", "climate", "A",
     "The heavy stone stays close."),
    (T_ECO, "Medium", "Breweries are usually sited in big cities to be near the",
     "market", "raw materials only", "power source", "railhead alone", "A",
     "Beer travels badly; people don't."),
    # ---------------------------------------------------------------- africa and nigeria
    (T_AFR, "Hard", "The deep lakes of East Africa, like Tanganyika and Malawi, fill the",
     "Rift Valley", "Congo basin", "Kalahari basin", "Atlas range", "A",
     "The cracked floor flooded."),
    (T_AFR, "Medium", "The River Benue joins the Niger after draining the eastern side of the",
     "Adamawa highlands", "Jos Plateau", "Mandara hills", "Obudu hills", "A",
     "Its waters gather from there."),
    (T_AFR, "Medium", "Nigeria's highest annual rainfall totals occur around",
     "the Niger Delta coast", "the Jos Plateau", "the Sokoto plains", "the Chad Basin", "A",
     "Coastal belts drink the most."),
    # ---------------------------------------------------------------- environment
    (T_ENV, "Hard", "The steady southward spread of desert conditions into the Sahel is called",
     "desertification", "deforestation", "siltation", "salinisation", "A",
     "The desert creeps into farmland."),
    (T_ENV, "Easy", "Sunlight, wind and flowing water are grouped as",
     "renewable energy sources", "fossil fuels", "nuclear fuels", "exhaustible fuels", "A",
     "Nature refills them always."),
    (T_ENV, "Medium", "Replanting trees on bare hillsides is done mainly to",
     "bind the soil and slow runoff", "raise the land's price", "attract more tourists", "cool the farm houses", "A",
     "Roots hold the slope together."),
]

build_batch(
    S,
    "batch_095_waec_geography2.json",
    "095",
    "WAEC Geography round 2 (Round 19 lift): Tropic of Cancer, Greenwich, "
    "June 21 solstice, solar eclipse, troposphere weather, stratosphere "
    "ozone, limestone, carbonation, soil creep, landslide, hydraulic "
    "action, abrasion, saltation, springs, water table, rock pedestal, "
    "stalactites, wave-cut platform, stack, caldera, focus vs epicentre, "
    "seismograph, linear scale, hill shading, cross-section, settlement "
    "site water, market town, life expectancy, plantation, Jos tin, "
    "Itakpe-Ajaokuta, gas power, raw-material and market location factors, "
    "Rift Valley lakes, Benue headwaters, Delta rainfall, desertification, "
    "renewables, replanting. Scanned against WAEC r1, NECO rounds 1-2 and "
    "the JAMB banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
