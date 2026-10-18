"""Batch 093 - WAEC Agricultural Science round 2 (WAEC lift, Round 19).

WAEC Agric Paper 1 draws 50 items; the bank stood at 66. This lift adds
fresh items - land tenure systems, fertiliser application methods,
irrigation methods, storage, weed control, erosion control, animal
reproduction numbers (pig 114 days, hen 21 days, rabbit 31), feeds,
bee-keeping, catfish, Gumboro, IPM, quarantine, mechanisation, surveying,
nursery practice - scanned against WAEC r1, NECO rounds 1-2 and the JAMB
Agric banks.

    python3 scripts/build_neco_batch93.py -> content/batch_093_waec_agric2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Agricultural Science"

T_LAND = "Land Tenure and Land Use"
T_CROP = "Crop Husbandry"
T_SOIL = "Soil Fertility and Conservation"
T_ANIM = "Animal Production"
T_FEED = "Animal Nutrition"
T_HEALTH = "Animal and Crop Health"
T_TOOL = "Mechanisation and Surveying"
T_STORE = "Processing and Storage"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- land tenure
    (T_LAND, "Medium", "The land tenure system in which the community owns land and every member farms a portion is",
     "communal tenure", "individual tenure", "tenancy at will", "freehold tenure", "A",
     "The community holds the land in trust."),
    (T_LAND, "Medium", "A system where land passes from father to son on death is",
     "inheritance tenure", "pledge tenure", "gift tenure", "leasehold tenure", "A",
     "Family land descends the line."),
    (T_LAND, "Medium", "Land acquired by outright purchase and held for life is held on",
     "freehold tenure", "communal tenure", "inheritance tenure", "tenancy tenure", "A",
     "The buyer holds title for life."),
    (T_LAND, "Easy", "A major disadvantage of the communal system for large-scale farming is that land",
     "cannot be used as loan security", "is always too fertile", "sells at very high prices", "needs no clearing work", "A",
     "No individual title, no collateral."),
    # ---------------------------------------------------------------- crop husbandry
    (T_CROP, "Medium", "Seedlings raised in a nursery are hardened off before transplanting by",
     "reducing shade and water gradually", "adding more fertiliser daily", "waterlogging the beds", "covering them fully again", "A",
     "Gradual exposure toughens them."),
    (T_CROP, "Medium", "The fertiliser application method of spreading it all over the field is",
     "broadcasting", "side-dressing", "ring application", "foliar spraying", "A",
     "It covers the whole ground."),
    (T_CROP, "Medium", "Placing fertiliser in a circle some distance round a tree trunk is",
     "ring application", "banding", "drilling", "dipping", "A",
     "The ring feeds the feeding roots."),
    (T_CROP, "Hard", "Drilling as a planting method means placing seeds",
     "in rows below the soil surface", "on top of the flat soil", "inside polythene bags", "broadcast and covered later", "A",
     "Rows and depth define drilling."),
    (T_CROP, "Easy", "Cowpea is valued in rotations mainly because it",
     "adds nitrogen to the soil", "uses up all soil water", "hosts many weeds", "matures very late", "A",
     "Its nodules feed the soil."),
    # ---------------------------------------------------------------- soil
    (T_SOIL, "Medium", "Cutting the slope into level steps to slow runoff is",
     "terracing", "ridging across slopes", "mulching", "ploughing downhill", "A",
     "Steps shorten the slope length."),
    (T_SOIL, "Medium", "Planting crops in strips across the slope so that runoff is checked is",
     "strip cropping", "continuous cropping", "monocropping", "double cropping", "A",
     "Strip barriers brake the water."),
    (T_SOIL, "Medium", "The method that guards the soil surface directly with plant remains is",
     "mulching", "terracetting", "drainage", "flooding", "A",
     "The blanket of remains shields soil."),
    (T_SOIL, "Hard", "Green manure refers to crops ploughed under while still",
     "fresh and green", "dry and brown", "in full flower only", "carrying seed pods", "A",
     "Fresh biomass feeds the soil."),
    # ---------------------------------------------------------------- animal production
    (T_ANIM, "Hard", "For roughly how many days is a sow pregnant before farrowing?",
     "114 days", "150 days", "283 days", "60 days", "A",
     "Three months, three weeks, three days."),
    (T_ANIM, "Hard", "A hen's egg hatches after about",
     "21 days", "28 days", "18 days", "30 days", "A",
     "The chick emerges on day twenty-one."),
    (T_ANIM, "Hard", "Roughly how many days does a doe carry its young before kindling?",
     "31 days", "60 days", "114 days", "90 days", "A",
     "The doe kindles in a month."),
    (T_ANIM, "Easy", "A young female cattle that has not yet calved is a",
     "heifer", "steer", "bull", "cow", "A",
     "Heifers await their first calf."),
    (T_ANIM, "Medium", "The raised wooden or wire home a farmer builds for rabbits is the",
     "hutch", "battery cage", "kennel", "sty", "A",
     "Wire or wooden hutches serve them."),
    (T_ANIM, "Hard", "Clarias, the fish favoured in Nigerian homestead ponds, is the",
     "African catfish", "Nile tilapia", "common carp", "mackerel", "A",
     "Clarias breathes air too."),
    (T_ANIM, "Medium", "Raising different fish species together in one pond is",
     "polyculture", "monoculture", "integrated culture", "seed culture", "A",
     "Catfish and tilapia share the pond."),
    # ---------------------------------------------------------------- nutrition
    (T_FEED, "Easy", "Maize is chiefly valued in livestock rations as a source of",
     "energy", "protein", "vitamins", "minerals", "A",
     "Its carbohydrates fuel growth."),
    (T_FEED, "Easy", "Groundnut cake and fish meal serve mainly as sources of",
     "protein", "energy", "fibre", "water", "A",
     "Cake and meal build the body."),
    (T_FEED, "Medium", "Feeds high in fibre such as hay and fresh grass are classified as",
     "roughages", "concentrates", "supplements", "additives", "A",
     "Roughage fills the belly bulk."),
    (T_FEED, "Medium", "Salt lick is provided to ruminants to supply",
     "minerals", "energy", "protein", "fats", "A",
     "Licks carry needed minerals."),
    # ---------------------------------------------------------------- health
    (T_HEALTH, "Hard", "Gumboro, a viral disease that wastes young chicks, attacks the",
     "bursa of Fabricius", "egg shell gland", "feather roots", "blood of layers", "A",
     "The bursa is its target organ."),
    (T_HEALTH, "Hard", "The strategy that combines chemical, biological, cultural and physical methods against a pest is",
     "integrated pest management", "calendar spraying", "zero grazing", "mixed farming", "A",
     "Many tools, one programme."),
    (T_HEALTH, "Medium", "Keeping newly imported animals separated and watched for a while before joining the flock is",
     "quarantine", "culling", "tagging", "docking", "A",
     "Observation bars hidden disease."),
    (T_HEALTH, "Medium", "Selective herbicides are so called because they",
     "kill weeds but spare the crop", "kill every plant they touch", "act only on insects", "work only in the rain", "A",
     "They choose their victims."),
    (T_HEALTH, "Easy", "The commonest method of weed control on Nigerian smallholdings is",
     "manual hoeing", "aerial spraying", "biological control", "flame weeding", "A",
     "The hoe still rules the farm."),
    # ---------------------------------------------------------------- mechanisation and surveying
    (T_TOOL, "Easy", "One clear advantage of farm mechanisation is that it",
     "saves time on large operations", "needs no repairs ever", "suits every farm size", "removes the need for seed", "A",
     "Machines finish work faster."),
    (T_TOOL, "Medium", "A major limitation of mechanisation on Nigerian smallholdings is",
     "fragmented land holdings", "too many spare parts", "plenty of trained drivers", "cheap fuel everywhere", "A",
     "Small plots defeat big machines."),
    (T_TOOL, "Medium", "Ranging poles and a prismatic compass are instruments of",
     "farm surveying", "weather recording", "soil testing", "animal dipping", "A",
     "They set lines and bearings."),
    (T_TOOL, "Easy", "The surveying instrument used to read vertical heights between points is the",
     "levelling staff with level", "rain gauge", "anemometer", "soil auger", "A",
     "Levels read rise and fall."),
    # ---------------------------------------------------------------- processing and storage
    (T_STORE, "Medium", "Maize cobs stored unshelled in raised ventilated structures are kept in",
     "cribs", "silos", "cold rooms", "drum stores", "A",
     "Crib walls let air pass through."),
    (T_STORE, "Hard", "Airtight bags that keep grain by excluding air and moisture are called",
     "hermetic bags", "jute sacks", "woven baskets", "polythene open sacks", "A",
     "Sealed bags suffocate pests."),
    (T_STORE, "Medium", "Smoking and sun-drying preserve fish mainly by",
     "reducing their water content", "adding vitamins", "killing all the bones", "lowering their weight alone", "A",
     "With less water, decay stalls."),
    (T_STORE, "Easy", "The machine that removes husks from rice after harvest is a",
     "dehusker", "thresher", "mower", "baler", "A",
     "Dehusking strips the paddy."),
    (T_STORE, "Medium", "Processing farm produce soon after harvest mainly improves its",
     "shelf life and market value", "weight and colour only", "seed germination rate", "fertiliser value", "A",
     "Processing keeps quality longer."),
]

build_batch(
    S,
    "batch_093_waec_agric2.json",
    "093",
    "WAEC Agric round 2 (Round 19 lift): land tenure (communal, inheritance, "
    "freehold, collateral weakness), crop husbandry (hardening off, "
    "broadcasting, ring application, drilling, cowpea rotation), soil "
    "conservation (terracing, strip cropping, mulching, green manure), "
    "animal production (sow 114 days, hen 21 days, rabbit 31 days, heifer, "
    "hutches, Clarias catfish, polyculture), nutrition (maize energy, GNC "
    "protein, roughages, salt lick), health (Gumboro bursa, IPM, quarantine, "
    "selective herbicides, hoeing), mechanisation (advantages, fragmented "
    "land limit), surveying (ranging poles, prismatic compass, levelling), "
    "storage (cribs, hermetic bags, fish smoking, dehusker, processing "
    "value). Scanned against WAEC r1, NECO rounds 1-2 and the JAMB banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
