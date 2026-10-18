"""Batch 087 - NECO Geography round 2 (NECO lift, Round 18).

NECO Geography objective draws 60 items; the bank stood at 87. This lift
adds fresh items - earth basics (meridians, 15 degrees = 1 hour, equinox),
river landforms (meander, ox-bow, levee, waterfall, youthful stage), map
skills (grid references, area by squares), population (density formula,
brain drain), Nigeria specifics (state capitals, Guinea savanna, Enugu
coal, associated gas), instruments (rain gauge, wind vane, Stevenson
screen) and environment (greenhouse gas, contour ploughing, oil spills).
Scanned against NECO round 1, the WAEC twin and the JAMB Geography banks.

    python3 scripts/build_neco_batch87.py -> content/batch_087_neco_geography2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_EAR = "The Earth and Its Structure"
T_LAN = "Weathering and Landforms"
T_MAP = "Map Reading and Interpretation"
T_POP = "Population and Settlement"
T_ECO = "Economic Geography"
T_REG = "Regional Geography of Nigeria"
T_CLI = "Climate"
T_ENV = "Environmental Issues"
T_TRA = "Transport"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- earth
    (T_EAR, "Easy", "The imaginary lines running from the North Pole to the South Pole are called",
     "meridians of longitude", "parallels of latitude", "the contours", "isobars", "A",
     "Meridians join pole to pole."),
    (T_EAR, "Hard", "Time changes by one hour for every",
     "15 degrees of longitude", "10 degrees of longitude", "30 degrees of latitude", "degree of the equator", "A",
     "The earth turns 360 degrees in 24 hours."),
    (T_EAR, "Medium", "When it is noon in London, clocks in Nigeria read later because Nigeria lies",
     "further east", "further west", "on the equator", "nearer the sea", "A",
     "Eastward places meet the sun earlier."),
    (T_EAR, "Medium", "The yearly seasons are caused by the earth's",
     "revolution round the sun", "rotation on its axis", "distance from the moon", "tilt away from the stars", "A",
     "The tilted journey makes the seasons."),
    (T_EAR, "Hard", "The two days of the year when day and night are equal everywhere are the",
     "equinoxes", "solstices", "zenith days", "eclipses", "A",
     "Equal day and night marks an equinox."),
    # ---------------------------------------------------------------- landforms
    (T_LAN, "Medium", "A river often plunges as a waterfall where it crosses",
     "a band of hard, resistant rock", "a stretch of soft alluvium", "its own delta deposits", "a man-made levee", "A",
     "Soft rock wears away, hard rock stands."),
    (T_LAN, "Easy", "The sweeping bend developed by a river along its middle course is a",
     "meander", "gorge", "rapid", "delta", "A",
     "The river swings in great curves."),
    (T_LAN, "Hard", "The crescent lake left behind when a river short-circuits one of its bends is the",
     "ox-bow lake", "lagoon", "tarn", "moraine lake", "A",
     "The abandoned bend holds water."),
    (T_LAN, "Hard", "The natural embankments of sediment found along a river's lower course are",
     "levees", "eskers", "moraines", "dykes of lava", "A",
     "Flood silt builds up the banks."),
    (T_LAN, "Medium", "A river cuts deep, narrow V-shaped valleys chiefly during its",
     "youthful stage", "mature stage", "old stage", "delta stage", "A",
     "Downcutting rules the young river."),
    (T_LAN, "Medium", "A delta is built up from sediment dropped where a river",
     "enters the sea or a lake", "leaves its source spring", "crosses hard rock", "flows over a plateau", "A",
     "The load settles in still water."),
    # ---------------------------------------------------------------- map reading
    (T_MAP, "Medium", "The eastings and northings printed across a map sheet are used mainly to give",
     "grid references", "magnetic bearings", "relief shading", "scale conversion", "A",
     "Numbers along the grid locate points."),
    (T_MAP, "Hard", "Contour lines can cross one another only where the land forms",
     "an overhanging cliff", "a gentle plain", "a river valley", "a mountain pass", "A",
     "Only an overhang puts one height above another."),
    (T_MAP, "Medium", "To estimate the area of farmland shown on a map, count the",
     "grid squares it covers", "contour lines around it", "rivers crossing it", "settlements inside it", "A",
     "Squares are then converted with the scale."),
    (T_MAP, "Easy", "The direction of one place from another on a map is read as a",
     "bearing measured clockwise from north", "distance measured in kilometres", "height taken from spot heights", "latitude read from the margins", "A",
     "Bearings run clockwise from north."),
    # ---------------------------------------------------------------- population
    (T_POP, "Easy", "A state with 6 million people spread over 60,000 square kilometres has a population density of",
     "100 persons per square km", "10 persons per square km", "1,000 persons per square km", "6,000 persons per square km", "A",
     "Divide 6,000,000 by 60,000 to get 100."),
    (T_POP, "Medium", "The natural increase of a population is the excess of",
     "births over deaths", "immigrants over emigrants", "employed over unemployed", "adults over children", "A",
     "Births minus deaths grow a people."),
    (T_POP, "Easy", "The movement of doctors and engineers from Nigeria to Europe is called",
     "brain drain", "rural-urban drift", "seasonal migration", "pastoral migration", "A",
     "Skilled hands leave the country."),
    (T_POP, "Medium", "A direct social problem of over-crowded Nigerian cities is",
     "high unemployment", "wider farmlands", "falling house rents", "empty classrooms", "A",
     "Jobs cannot match the crowd."),
    (T_POP, "Medium", "The National Population Commission is responsible for",
     "conducting censuses", "issuing passports", "fixing minimum wages", "registering political parties", "A",
     "It counts the nation's people."),
    # ---------------------------------------------------------------- economic
    (T_ECO, "Easy", "Coal was mined for many years around",
     "Enugu", "Warri", "Sokoto", "Maiduguri", "A",
     "The Coal City earned its name there."),
    (T_ECO, "Medium", "Most of Nigeria's natural gas is found",
     "together with crude oil in the ground", "only in the far northern dunes", "only offshore of Lagos", "in coal seams at Enugu", "A",
     "Gas mostly accompanies the oil."),
    (T_ECO, "Medium", "Shiroro and Jebba dams, like Kainji, were built chiefly to generate",
     "hydro-electric power", "irrigation water for rice", "water for Lagos industries", "flood control only", "A",
     "Falling water spins the turbines."),
    (T_ECO, "Medium", "The bulk of Nigeria's hardwood timber comes from the",
     "rainforest belt of the south", "Sahel grassland", "mangrove swamps alone", "high mountain slopes", "A",
     "Dense forests crown the south."),
    (T_ECO, "Medium", "Farmers in the far north depend on irrigation because rainfall there is",
     "low and seasonal", "heavy all year round", "spread through the year", "blocked by mountains", "A",
     "Short wet seasons limit rain-fed farming."),
    # ---------------------------------------------------------------- regional nigeria
    (T_REG, "Easy", "Ibadan, the largest city in West Africa by land area, is the capital of",
     "Oyo State", "Ogun State", "Osun State", "Kwara State", "A",
     "Ibadan serves as Oyo's capital."),
    (T_REG, "Easy", "Port Harcourt is the capital of",
     "Rivers State", "Bayelsa State", "Delta State", "Akwa Ibom", "A",
     "The Garden City leads Rivers."),
    (T_REG, "Medium", "Maiduguri, headquarters of the North-East, is the capital of",
     "Borno State", "Yobe State", "Adamawa State", "Bauchi State", "A",
     "Borno's capital stands at its heart."),
    (T_REG, "Medium", "The widest vegetation belt in Nigeria is the",
     "Guinea savanna", "mangrove swamp", "Sudan savanna", "montane forest", "A",
     "Guinea savanna stretches across the middle."),
    (T_REG, "Medium", "The tree crop that dominates the swampy belts of the South-South is the",
     "oil palm", "cocoa tree", "rubber tree only", "cashew tree", "A",
     "Palms crowd the wet southern lowlands."),
    (T_REG, "Hard", "The temperate-like climate of the Jos Plateau supports the growing of",
     "Irish potatoes", "oil palm", "rubber trees", "mangoes only", "A",
     "Cool heights suit the potato."),
    # ---------------------------------------------------------------- climate
    (T_CLI, "Easy", "After a storm, the weather station reads the depth of water collected in a",
     "rain gauge", "barometer", "anemometer", "thermometer", "A",
     "The gauge collects and measures rain."),
    (T_CLI, "Easy", "The instrument that shows the direction of the wind is the",
     "wind vane", "rain gauge", "barograph", "hygrometer", "A",
     "The vane swings to point the wind."),
    (T_CLI, "Hard", "Weather instruments are shielded from direct sunshine and rain inside the",
     "Stevenson screen", "barograph box", "meteorological mast", "thermal cabinet", "A",
     "The white louvred box protects them."),
    (T_CLI, "Hard", "The red, iron-rich soils commonly found in the Nigerian savanna are",
     "laterites", "alluvium", "regosols", "chernozems", "A",
     "Laterite reddens the savanna earth."),
    # ---------------------------------------------------------------- environment
    (T_ENV, "Easy", "A major greenhouse gas released by burning fuels is",
     "carbon dioxide", "oxygen gas", "nitrogen gas", "hydrogen gas", "A",
     "Burning releases carbon dioxide."),
    (T_ENV, "Medium", "Ploughing across a slope rather than down it helps to reduce",
     "soil erosion by runoff", "the soil's fertility", "the land's gradient", "the amount of rainfall", "A",
     "Contour furrows slow the water."),
    (T_ENV, "Medium", "Fishermen in areas of oil spillage lose their catch because the water is",
     "polluted by crude oil", "too warm for fish", "too saltless for fish", "too deep for nets", "A",
     "Oil poisons fish and gear alike."),
    (T_ENV, "Easy", "The loss of wild animals and plants is a direct consequence of",
     "deforestation", "afforestation", "contour ploughing", "irrigation farming", "A",
     "Habitats vanish with the trees."),
    # ---------------------------------------------------------------- transport
    (T_TRA, "Medium", "Rail transport is best suited for carrying",
     "heavy, bulky goods over land", "fresh vegetables to market", "urgent letters at night", "tourists on short trips", "A",
     "Rails haul weight cheaply."),
]

build_batch(
    S,
    "batch_087_neco_geography2.json",
    "087",
    "NECO Geography round 2 (Round 18 lift): fresh earth items (meridians, "
    "15 degrees = 1 hour, eastward time, revolution-seasons, equinoxes), "
    "river work (waterfall on resistant rock, meander, ox-bow, levees, "
    "youthful V-valleys, delta build-up), map skills (grid references, "
    "crossing contours at cliffs, area by squares), population (density "
    "formula, natural increase, brain drain, overcrowding, NPC), economic "
    "(Enugu coal, associated gas, Shiroro-Jebba, timber belt, northern "
    "irrigation), regional (Ibadan-Oyo, Port Harcourt, Maiduguri, Guinea "
    "savanna, oil palm, Jos potatoes), instruments (rain gauge, wind vane, "
    "Stevenson screen, laterites) and environment (carbon dioxide, contour "
    "ploughing, oil spillage, deforestation). Scanned against NECO round 1, "
    "the WAEC twin and the JAMB Geography banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
