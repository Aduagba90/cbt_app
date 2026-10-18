"""Batch 085 - NECO Agricultural Science round 2 (NECO lift, Round 18).

NECO Agric objective draws 60 items; the bank stood at 90. This lift adds
fresh items - crop and soil specifics (yam mounds, cowpea nodules, staking,
alley cropping, hygroscopic water, alluvial soils), animal husbandry
(brooding, battery cage, breeds, doe/sow), pest control (ladybird, nagana,
coccidiosis), tools (knapsack sprayer, cultivator, mower), farm economics
(gross margin, farm diary, demonstration plots) and forestry/fisheries -
scanned against NECO round 1, the WAEC twin and the JAMB Agric banks.

    python3 scripts/build_neco_batch85.py -> content/batch_085_neco_agric2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Agricultural Science"

T_CROP = "Crop Production"
T_SOIL = "Soil Science"
T_ANIM = "Animal Production"
T_PEST = "Pests and Diseases"
T_TOOL = "Farm Tools and Machinery"
T_ECON = "Agricultural Economics and Extension"
T_FISH = "Fisheries and Forestry"
T_PROP = "Crop Propagation"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- crop production
    (T_CROP, "Medium", "Before planting yam setts, a farmer heaps the soil into mounds so that the",
     "tubers can swell in loose earth", "field drains completely dry", "insects are trapped inside", "vines stop climbing stakes", "A",
     "Loose earth lets tubers swell freely."),
    (T_CROP, "Medium", "Cowpea and other legumes improve the soil because their roots carry",
     "nitrogen-fixing nodules", "oil-storing tubers", "water-proof hairs", "starch-rich taproots", "A",
     "Bacteria in the nodules fix nitrogen."),
    (T_CROP, "Easy", "Tomato plants are staked in order to",
     "keep the fruits off the wet ground", "make the leaves greener", "shorten the maturity period", "sweeten the fruits", "A",
     "Staking keeps fruits clean and rot-free."),
    (T_CROP, "Easy", "Elephant grass and spear grass are examples of",
     "weeds", "cover crops", "green manures", "cash crops", "A",
     "They grow where they are not wanted."),
    (T_CROP, "Hard", "Growing food crops in the spaces between rows of planted trees is called",
     "alley cropping", "crop rotation", "mixed farming", "land rotation", "A",
     "Crops occupy the alleys between trees."),
    (T_CROP, "Easy", "Mulching the soil chiefly helps to",
     "conserve soil moisture", "increase soil acidity", "kill all soil bacteria", "harden the soil surface", "A",
     "The mulch blanket checks evaporation."),
    # ---------------------------------------------------------------- soil science
    (T_SOIL, "Easy", "The horizon of the soil profile richest in humus is the",
     "topsoil", "subsoil", "parent rock", "bedrock", "A",
     "Decaying matter gathers at the top."),
    (T_SOIL, "Medium", "Alluvial soils are usually fertile because they are",
     "formed from river deposits", "rich in farmyard manure", "free of all soil organisms", "always covered by mulch", "A",
     "Rivers drop rich silt as they flood."),
    (T_SOIL, "Hard", "The water held so tightly round soil particles that plants cannot absorb it is",
     "hygroscopic water", "capillary water", "gravitational water", "available water", "A",
     "Hygroscopic water clings beyond use."),
    (T_SOIL, "Medium", "The best soil structure for most crop growth is",
     "crumb structure", "blocky structure", "prismatic structure", "massive structure", "A",
     "Crumbs hold both air and water well."),
    (T_SOIL, "Easy", "Adding compost to the farm mainly improves the soil's",
     "structure and water holding", "colour and weight", "acidity and salt", "texture into pure sand", "A",
     "Organic matter builds better soil."),
    # ---------------------------------------------------------------- animal production
    (T_ANIM, "Easy", "Layers' feed must be rich in calcium so that the hens can form",
     "strong egg shells", "long feathers", "extra body fat", "bright combs", "A",
     "Shells are mostly calcium."),
    (T_ANIM, "Easy", "Day-old chicks are given extra heat during brooding because",
     "they cannot control body heat yet", "heat makes them grow wings", "cold kills their feathers", "heat sweetens their feed", "A",
     "Chicks need warmth to survive."),
    (T_ANIM, "Medium", "Keeping layers in wire compartments with feed and water piped to each cage is the",
     "battery cage system", "deep litter system", "free range system", "fold unit system", "A",
     "Cages confine each bird singly."),
    (T_ANIM, "Easy", "A female rabbit is called a",
     "doe", "ewe", "sow", "nanny", "A",
     "The doe kindles the young."),
    (T_ANIM, "Easy", "Rhode Island Red and Leghorn are well-known breeds of",
     "poultry", "cattle", "goats", "pigs", "A",
     "Both are famous chicken breeds."),
    (T_ANIM, "Hard", "The N'dama cattle is prized in West Africa because it is",
     "tolerant of trypanosomiasis", "the fastest draught animal", "immune to all foot diseases", "the heaviest beef breed", "A",
     "It survives in tsetse country."),
    (T_ANIM, "Easy", "A female pig is called a",
     "sow", "doe", "ewe", "hen", "A",
     "The sow farrows the piglets."),
    # ---------------------------------------------------------------- pests and diseases
    (T_PEST, "Hard", "Ladybird beetles are welcomed on the farm because they",
     "feed on aphids", "pollinate maize", "eat weed seeds", "kill soil fungi", "A",
     "Their larvae devour aphids."),
    (T_PEST, "Medium", "The tsetse fly spreads which disease among cattle?",
     "trypanosomiasis", "anthrax", "foot rot", "coccidiosis", "A",
     "Its bite passes the blood parasite."),
    (T_PEST, "Medium", "Foot and mouth disease, which blisters the mouths of cattle, is caused by",
     "a virus", "a bacterium", "a fungus", "a protozoan", "A",
     "It is a highly viral disease."),
    (T_PEST, "Hard", "Coccidiosis, which causes bloody droppings in chicks, is caused by",
     "a protozoan", "a virus", "a bacterium", "a fluke", "A",
     "Protozoa attack the gut lining."),
    (T_PEST, "Easy", "Besides insects, the commonest pests of stored grain are",
     "rodents", "cattle", "hawks", "snails", "A",
     "Rats eat and soil the grain."),
    (T_PEST, "Medium", "Rotating crops season by season helps to control pests because it",
     "breaks the pests' life cycle", "kills the pests with shade", "drowns all pest eggs", "attracts more pests away", "A",
     "Pests starve without their host crop."),
    # ---------------------------------------------------------------- farm tools
    (T_TOOL, "Medium", "A farmer walking the rows with a tank on his back to spray weeds is using a",
     "knapsack sprayer", "hand duster", "watering can", "slurry pump", "A",
     "The tank rides on his back."),
    (T_TOOL, "Medium", "The tractor implement used to stir the soil between crop rows and cut down weeds is the",
     "cultivator", "planter", "thresher", "ridger", "A",
     "Cultivators weed between the rows."),
    (T_TOOL, "Medium", "The implement used to cut standing grass when making hay is the",
     "mower", "plough", "harrow", "roller", "A",
     "Mowers level the grass fields."),
    (T_TOOL, "Easy", "The part of a sprayer that breaks the liquid into fine droplets is the",
     "nozzle", "tank", "hose", "handle", "A",
     "The nozzle atomises the spray."),
    # ---------------------------------------------------------------- economics and extension
    (T_ECON, "Hard", "A farmer's income minus his running costs for the season gives the",
     "gross margin", "net worth", "turnover", "fixed cost", "A",
     "Gross margin nets off variable costs."),
    (T_ECON, "Easy", "The farm record that notes daily happenings on the farm is the",
     "farm diary", "cash book", "balance sheet", "yield register", "A",
     "Events enter the diary day by day."),
    (T_ECON, "Medium", "A small plot where a new method is shown to farmers under extension guidance is a",
     "demonstration plot", "control plot", "fallow plot", "market garden", "A",
     "Farmers see the method, then adopt it."),
    (T_ECON, "Medium", "Farmers form cooperative societies mainly to",
     "buy inputs and sell produce jointly", "avoid paying all taxes", "escape extension advice", "share family land equally", "A",
     "Strength comes from numbers."),
    (T_ECON, "Easy", "Which of these is a fixed asset on a farm?",
     "farm tractor", "feed concentrate", "fertiliser bags", "day-old chicks", "A",
     "The tractor serves for years."),
    # ---------------------------------------------------------------- fisheries and forestry
    (T_FISH, "Medium", "Growing trees, crops and animals together on the same land is called",
     "agroforestry", "monocropping", "taungya farming", "bush fallowing", "A",
     "Trees share the land with crops and beasts."),
    (T_FISH, "Medium", "Planting trees to create a forest where none stood before is",
     "afforestation", "deforestation", "reforestation", "selective felling", "A",
     "New forests are planted from scratch."),
    (T_FISH, "Easy", "One-man fishing in rivers and ponds commonly uses",
     "hook and line", "trawlers", "purse seines", "giant drag nets", "A",
     "The lone angler hooks his catch."),
    # ---------------------------------------------------------------- propagation
    (T_PROP, "Easy", "Irish potato is propagated by means of",
     "stem tubers", "true seeds", "stem cuttings", "suckers", "A",
     "Planted tubers sprout new stems."),
    (T_PROP, "Hard", "In grafting, the shoot that is fixed onto another plant is the",
     "scion", "stock", "taproot", "slip", "A",
     "The scion grows on the stock."),
    (T_PROP, "Easy", "Sugarcane is commonly propagated by",
     "stem cuttings", "seeds", "bulbils", "runners", "A",
     "Cane stems with buds are planted."),
    (T_PROP, "Medium", "In layering, a branch forms roots",
     "while still attached to the parent", "after being cut off first", "only inside water jars", "only in the dry season", "A",
     "Roots form before separation."),
]

build_batch(
    S,
    "batch_085_neco_agric2.json",
    "085",
    "NECO Agric round 2 (Round 18 lift): fresh crop and soil items (yam "
    "mounds, cowpea nodules, staking, alley cropping, mulching, humus "
    "horizon, alluvial soils, hygroscopic water, crumb structure), animal "
    "husbandry (calcium for shells, brooding heat, battery cage, doe/sow, "
    "Rhode Island Red and Leghorn, N'dama trypanotolerance), pests (ladybird "
    "vs aphids, tsetse-nagana, foot-and-mouth virus, coccidiosis protozoan, "
    "rodents, rotation breaking cycles), tools (knapsack sprayer, cultivator, "
    "mower, nozzle), economics and extension (gross margin, farm diary, "
    "demonstration plot, cooperatives, fixed assets), agroforestry and "
    "afforestation, hook-and-line fishing, propagation (Irish potato tubers, "
    "scion, sugarcane cuttings, layering). Scanned against NECO round 1, the "
    "WAEC twin and the JAMB Agric banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
