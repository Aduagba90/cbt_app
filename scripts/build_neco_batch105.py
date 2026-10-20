"""Batch 105 - WAEC Agricultural Science round 3 (WAEC top-up, Round 21).

Lifts WAEC Agric from 104 toward ~150 with fresh angles: cropping
systems, propagation methods, nurseries, pasture and forage, silage,
fish farming and pond management, poultry production, livestock
management and health, farm records and planning, agro-processing,
storage structures, agricultural institutions and land tenure. Scanned
against WAEC rounds 1-2, NECO Agric and the JAMB pool.

    python3 scripts/build_neco_batch105.py -> content/batch_105_waec_agric3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Agricultural Science"

T_CROP = "Crop Production"
T_PROP = "Propagation and Nurseries"
T_PAST = "Pastures and Forage Crops"
T_FISH = "Fish Farming"
T_LIVE = "Livestock and Poultry"
T_HEALTH = "Animal Health"
T_FARM = "Farm Records and Planning"
T_PROC = "Agro-processing and Storage"
T_INST = "Institutions and Land Tenure"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- crops
    (T_CROP, "Medium", "Growing maize and beans together on the same plot in one season is",
     "mixed cropping", "crop rotation", "relay cropping", "fallowing", "A",
     "Two crops share one plot."),
    (T_CROP, "Medium", "Sowing the next crop into a standing one is",
     "relay cropping", "mixed cropping", "monocropping", "strip cropping", "A",
     "The next crop starts early."),
    (T_CROP, "Hard", "Growing different crops on the same plot in a fixed order season after season is",
     "crop rotation", "mixed farming", "shifting cultivation", "taungya", "A",
     "The order repeats itself."),
    (T_CROP, "Medium", "Crop rotation chiefly helps the soil by",
     "varying nutrient demands", "drying the soil out", "removing all humus", "raising its acidity", "A",
     "Crops swap needs and break pest cycles."),
    (T_CROP, "Hard", "The taungya system combines forestry with",
     "food crops in young plantations", "cattle rearing in sheds", "fish ponds in rivers", "poultry cages", "A",
     "Farmers tend trees and crops together."),
    (T_CROP, "Medium", "Cassava is commonly propagated through",
     "stem cuttings", "seeds only", "leaf buds", "root suckers", "A",
     "Sticks sprout into new plants."),
    (T_CROP, "Medium", "Tomato seedlings are first raised in a",
     "nursery bed", "silo", "fish pond", " paddock", "A",
     "They start life in the nursery."),
    (T_CROP, "Hard", "Which cropping system keeps soil covered against erosion by planting across a slope in bands?",
     "strip cropping", "monocropping", "flood cropping", "aerial cropping", "A",
     "Grass bands check the runoff."),

    # ------------------------------------------------------------- propagation
    (T_PROP, "Medium", "Grafting joins two plants so that the upper part is the",
     "scion", "stock", "root", "seed", "A",
     "The scion sits on top of the stock."),
    (T_PROP, "Medium", "In budding, the bud inserted into the stock is usually taken from a",
     "mature desired variety", "random seedling", "root piece", "dry leaf", "A",
     "The bud carries the wanted traits."),
    (T_PROP, "Hard", "The main reason for grafting citrus is to",
     "combine good fruit with strong roots", "make the tree grow taller", "slow fruiting by years", "kill the stock", "A",
     "Both partners bring a strength."),
    (T_PROP, "Medium", "Layering produces new plants by",
     "rooting a stem still attached", "sowing seeds in trays", "cutting roots off", "grafting buds only", "A",
     "The branch roots before cutting."),

    # ------------------------------------------------------------- pastures
    (T_PAST, "Medium", "Elephant grass is valued in livestock feeding mainly as a",
     "fodder grass", "cover crop for cocoa", "medicinal herb", "cash flower", "A",
     "Animals browse its bulky leaves."),
    (T_PAST, "Hard", "Storing green forage in an airtight silo to ferment is making",
     "silage", "hay", "compost", "straw", "A",
     "Fermentation keeps it succulent."),
    (T_PAST, "Medium", "Hay is forage that has been",
     "dried in the sun for storage", "fermented in a pit", "grazed in the wet season", "rolled into bales of silage", "A",
     "Drying in the sun preserves it."),
    (T_PAST, "Hard", "A legume like stylo is often added to pastures because it",
     "fixes nitrogen into the soil", "drains the soil dry", "kills all grasses", "adds sand to the soil", "A",
     "Root nodules feed the soil."),
    (T_PAST, "Medium", "Overstocking a pasture leads chiefly to",
     "overgrazing and erosion", "richer grass each year", "deeper topsoil", "fewer weeds", "A",
     "Too many mouths ruin the field."),

    # ------------------------------------------------------------- fish
    (T_FISH, "Medium", "The commonest fish raised in Nigerian ponds is",
     "tilapia", "shark", "catshark", "mackerel", "A",
     "It grows and breeds fast in ponds."),
    (T_FISH, "Medium", "Before stocking, a new pond is fertilised mainly to",
     "grow natural fish food", "clean the water", "warm the pond", "kill all plankton", "A",
     "Plankton bloom feeds the fry."),
    (T_FISH, "Hard", "The screen at a pond's inlet and outlet chiefly prevents",
     "escape of fish and entry of predators", "water from flowing in", "sunlight warming the pond", "feed from sinking", "A",
     "Mesh keeps the pond secure."),
    (T_FISH, "Hard", "Harvesting a pond by draining all water at once is called",
     "total drainage harvesting", "partial harvesting", "seine cropping", "hook fishing", "A",
     "Every last fish is taken out."),
    (T_FISH, "Medium", "Feeding fish with formulated pellets mainly aims to",
     "speed growth and cut waste", "colour the water green", "raise pond acidity", "reduce oxygen", "A",
     "Balanced diet, faster weight."),

    # ------------------------------------------------------------- livestock
    (T_LIVE, "Medium", "Broilers are chickens kept mainly for",
     "meat", "eggs", "feathers", "cockfighting", "A",
     "They bulk up for the pot."),
    (T_LIVE, "Medium", "Chicks kept warm artificially in their first weeks are under",
     "brooding", "candling", "culling", "dubbing", "A",
     "Heat lamps stand in for mother hen."),
    (T_LIVE, "Hard", "Debeaking in poultry management is done chiefly to",
     "stop pecking and cannibalism", "make the birds sing", "hasten egg laying", "improve the comb", "A",
     "Blunt beaks stop feather pecking."),
    (T_LIVE, "Medium", "A battery cage system is a form of",
     "intensive poultry housing", "extensive grazing", "semi-intensive ranching", "free-range rearing", "A",
     "Birds live in tight rows."),
    (T_LIVE, "Hard", "The gestation period of a ewe is roughly",
     "150 days", "283 days", "114 days", "60 days", "A",
     "Five months carry the lamb.", "150"),
    (T_LIVE, "Medium", "Ruminants like cattle digest tough grass in the",
     "rumen", "gizzard", "crop", "caecum only", "A",
     "The first stomach ferments it."),

    # ------------------------------------------------------------- health
    (T_HEALTH, "Medium", "Isolating a sick animal from the herd is called",
     "quarantine", "vaccination", "culling", "drenching", "A",
     "Separation halts the spread."),
    (T_HEALTH, "Medium", "Vaccinating a healthy animal aims to",
     "build immunity before infection", "cure an existing disease", "colour the hide", "boost fertility only", "A",
     "Prevention always beats cure."),
    (T_HEALTH, "Hard", "A viral disease that sweeps through flocks is Newcastle, which attacks",
     "poultry", "cattle", "goats", "fish", "A",
     "It sweeps through flocks fast."),
    (T_HEALTH, "Hard", "Ticks and lice are examples of parasites living",
     "externally on the body", "inside the intestines", "in the blood stream only", "within muscle tissue", "A",
     "They cling to skin and feathers."),
    (T_HEALTH, "Medium", "Liver flukes, living inside the animal, are",
     "internal parasites", "external parasites", "bacteria", "viruses", "A",
     "They lodge inside the liver."),
    (T_HEALTH, "Medium", "Deworming an animal rids it of",
     "internal worms", "ticks on the skin", "ringworm patches", "foot rot", "A",
     "The drench cleans out the gut."),

    # ------------------------------------------------------------- records and planning
    (T_FARM, "Medium", "The record showing all animals on the farm with their details is the",
     "livestock inventory", "sales receipt", "feed slip", "wage sheet", "A",
     "Every beast is listed there."),
    (T_FARM, "Hard", "A farm record used to compute profit at the end of a season is the",
     "income and expense account", "rainfall chart", "breeding chart", "visitors' book", "A",
     "Ins and outs decide profit."),
    (T_FARM, "Medium", "A farm budget prepared before the season mainly helps the farmer to",
     "plan spending and returns", "predict the weather", "hire labourers only", "delay all sales", "A",
     "He plans spending against returns."),
    (T_FARM, "Hard", "Gross margin on a farm enterprise equals output value minus",
     "variable costs", "fixed costs only", "all family labour", "land rent", "A",
     "Only the varying costs count."),

    # ------------------------------------------------------------- processing and storage
    (T_PROC, "Medium", "Turning cassava tubers into garri is an example of",
     "agro-processing", "crop propagation", "pasture management", "fish pond culture", "A",
     "The raw tuber becomes food."),
    (T_PROC, "Medium", "A crib is a farm structure used mainly to",
     "store maize cobs with airflow", "rear rabbits", "mix feeds", "trap birds", "A",
     "Air moves through the slats."),
    (T_PROC, "Hard", "A hermetically sealed silo preserves grain chiefly by",
     "excluding air and moisture", "heating the grain", "spreading it in the sun", "spraying weekly", "A",
     "The sealed air stops pests."),
    (T_PROC, "Medium", "Sun-drying maize before storage mainly reduces",
     "moisture and mould risk", "protein content", "germination forever", "the grain's weight value", "A",
     "Well-dried grain keeps long."),
    (T_PROC, "Hard", "Cold storage delays spoilage of tomatoes chiefly by",
     "slowing down microorganisms", "killing all bacteria instantly", "adding preservatives", "removing the skin", "A",
     "The chill slows rot and mould."),

    # ------------------------------------------------------------- institutions and land
    (T_INST, "Medium", "The research institute for root and tuber crops, based in Ibadan, is the",
     "IITA", "NIHORT", "NIFOR", "FRIN", "A",
     "Its campus breeds cassava."),
    (T_INST, "Hard", "NIFOR, the institute for oil crops, is headquartered in",
     "Benin City", "Ibadan", "Zaria", "Maiduguri", "A",
     "Benin, the palm city, hosts it."),
    (T_INST, "Medium", "ADPs, which brought extension services to rural farmers, stand for",
     "Agricultural Development Projects", "Agricultural Data Programmes", "Area Development Plans", "Animal Disease Posts", "A",
     "The projects reached villages."),
    (T_INST, "Hard", "The land tenure system in which a family holds land as a unit is",
     "communal tenure", "individual tenure", "leasehold tenure", "freehold tenure", "A",
     "The community owns it together."),
    (T_INST, "Medium", "The practice of leaving land uncultivated to recover fertility is",
     "fallowing", "strip cropping", "relay cropping", "monocropping", "A",
     "The tired land takes a rest."),
]

build_batch(
    S,
    "batch_105_waec_agric3.json",
    "105",
    "WAEC Agricultural Science round 3 (Round 21 top-up): mixed, relay, "
    "strip and rotation cropping, taungya, cassava stem cuttings, nursery "
    "beds, grafting scion and stock, budding, layering, elephant grass "
    "fodder, silage vs hay, legume nitrogen fixation, overgrazing, "
    "tilapia ponds, pond fertilisation and screens, total drainage "
    "harvest, pellet feeding, broilers, brooding, debeaking, battery "
    "cages, ewe gestation 150 days, the rumen, quarantine, vaccination, "
    "Newcastle disease, ticks vs liver flukes, deworming, livestock "
    "inventory, income and expense records, farm budgets, gross margin, "
    "garri processing, cribs and silos, sun-drying, cold storage, IITA, "
    "NIFOR, ADPs, communal tenure and fallowing. Scanned against WAEC "
    "rounds 1-2, NECO Agric and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
