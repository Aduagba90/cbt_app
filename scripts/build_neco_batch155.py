"""Batch 155 - WAEC Agricultural Science round 6 (WAEC top-up, R29).

Grows WAEC Agric from 188 toward ~224 with angles not yet in the
bank: soil profile horizons (A as eluviation), colour as a drainage
clue, sand vs clay vs loam behaviour, humus, green manuring and
composting; crop rotation, cover crops, fallowing, afforestation;
drip and flood irrigation, drainage; photoperiodism; seed dressing,
transplanting, hardening off, roguing, pruning, staking; weeds'
competition; guinea grass, zero grazing, silage vs hay; rabbit
hutches, pond fertilisation and plankton, the seine net, starter
feed, Newcastle vaccination, the queen bee's duty; agro-processing
value addition, commodity boards, demonstration plots, secondary
tillage. Scanned against WAEC rounds 1-5, NECO Agric (all rounds)
and the JAMB pool.

    python3 scripts/build_neco_batch155.py -> content/batch_155_waec_agric6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Agricultural Science"

T_SOI = "Soil Science Further"
T_MAN = "Soil and Water Management"
T_CRO = "Crop Husbandry Practices"
T_PAS = "Pasture and Feed"
T_LIV = "Livestock and Fisheries Detail"
T_EXT = "Institutions, Processing and Mechanisation"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- soil science
    (T_SOI, "Hard", "In a soil profile, the horizon from which nutrients are washed down is the",
     "A horizon", "B horizon", "C horizon", "O horizon", "A",
     "Eluviation empties the top layer."),
    (T_SOI, "Medium", "A bluish-grey subsoil colour usually indicates the soil is",
     "poorly drained", "rich in potash", "sandy and dry", "full of humus", "A",
     "Waterlogged soils wear that hue."),
    (T_SOI, "Medium", "A soil through which water passes almost instantly, holding little for plants, is chiefly",
     "sandy", "clayey", "loamy", "peaty", "A",
     "Its big grains leave wide gaps."),
    (T_SOI, "Medium", "The soil that becomes sticky when wet and cracks when dry is dominated by",
     "clay", "sand", "gravel", "sawdust", "A",
     "Fine particles cling and crack."),
    (T_SOI, "Medium", "The soil most farmers desire, balancing drainage and retention, is",
     "loam", "pure clay", "pure sand", "quartz grit", "A",
     "The middle path holds best."),
    (T_SOI, "Medium", "Decayed plant and animal matter in the soil, dark and spongy, is",
     "humus", "silt", "marl", "laterite", "A",
     "It feeds and loosens the soil."),
    (T_SOI, "Hard", "Ploughing a green crop like centrosema into the soil before it seeds is",
     "green manuring", "composting", "mulching", "fallowing", "A",
     "The living fertiliser is buried."),
    (T_SOI, "Medium", "In compost making, layers of refuse and manure are turned mainly to",
     "admit air and speed decay", "keep away taxes", "dry the heap fully", "deepen the colour", "A",
     "The heap must breathe to cook."),

    # ------------------------------------------------------------- management
    (T_MAN, "Hard", "Of all irrigation methods, the one that delivers water drop by drop to each plant and wastes least is",
     "drip irrigation", "flood irrigation", "sprinkler spraying", "canal banking", "A",
     "Every drop finds its root."),
    (T_MAN, "Medium", "The irrigation method that simply floods the whole field, cheapest but wasteful, is",
     "flood irrigation", "drip irrigation", "sprinkler irrigation", "sub-irrigation", "A",
     "The entire field takes a bath."),
    (T_MAN, "Medium", "Excess water is removed from farm land through",
     "drainage", "mulching", "staking", "winnowing", "A",
     "Open ditches carry it away."),
    (T_MAN, "Hard", "Leaving land uncultivated for seasons so it rebuilds its fertility is",
     "fallowing", "cropping", "grafting", "layering", "A",
     "Rest restores the tired soil."),
    (T_MAN, "Medium", "Planting trees where forests once stood, to check wind and erosion, is",
     "afforestation", "deforestation", "taungya cropping", "land clearing", "A",
     "New trees close old wounds."),

    # ------------------------------------------------------------- crop husbandry
    (T_CRO, "Hard", "The response of plants to the length of day and night, controlling their flowering, is",
     "photoperiodism", "photosynthesis", "photorespiration", "phototropism", "A",
     "The clock lies in the daylight."),
    (T_CRO, "Medium", "Treating seeds with a fungicidal dust before planting guards them against",
     "soil-borne diseases", "birds alone", "stray animals", "frost bite", "A",
     "The coat repels the fungi."),
    (T_CRO, "Medium", "Moving young seedlings from the nursery to the main field is",
     "transplanting", "roguing", "thinning to zero", "pricking out forever", "A",
     "They leave the bed for the field."),
    (T_CRO, "Hard", "Gradually exposing nursery seedlings to sunlight before transplanting, so they do not wilt, is",
     "hardening off", "burning off", "drying off", "topping up", "A",
     "Soft leaves learn the sun slowly."),
    (T_CRO, "Medium", "Uprooting and destroying diseased plants from a standing crop is",
     "roguing", "staking", "mulching", "bird scaring", "A",
     "The sick ones leave the field."),
    (T_CRO, "Medium", "Cutting away unwanted branches from a citrus tree to improve yield is",
     "pruning", "roguing", "thinning", "hilling", "A",
     "Fewer branches, finer fruits."),
    (T_CRO, "Medium", "Giving yam vines or tomato plants support to stand upright is",
     "staking", "mulching", "ridging", "sterilising", "A",
     "The stick bears the climber."),
    (T_CRO, "Medium", "The chief harm weeds do to crops is",
     "competing for nutrients and light", "sweetening the soil", "shading only the paths", "attracting honey bees", "A",
     "Thieves at the same table."),

    # ------------------------------------------------------------- pasture & feed
    (T_PAS, "Medium", "Guinea grass, widely grown for grazing in Nigeria, has the botanical name",
     "Panicum maximum", "Penisetum typhoides", "Zea mays", "Digitaria exilis", "A",
     "The tall tussock of the savanna."),
    (T_PAS, "Medium", "Stall-feeding animals with cut forage instead of grazing them out is",
     "zero grazing", "strip grazing", "herding", "transhumance", "A",
     "The grass walks to the animal."),
    (T_PAS, "Hard", "Green fodder compacted and fermented in an airtight silo is",
     "silage", "hay", "straw", "bran", "A",
     "The sour smell cattle love."),
    (T_PAS, "Medium", "Grass cut and sun-dried for storage as dry season feed is",
     "hay", "silage", "glucose", "chaff", "A",
     "The barn's dry season reserve."),

    # ------------------------------------------------------------- livestock & fisheries
    (T_LIV, "Medium", "A youth corper starting a rabbit project will first build rows of",
     "hutches", "cotes", "slurry pens", "kennels", "A",
     "Wire-front wooden homes on legs."),
    (T_LIV, "Hard", "A fish pond is fertilised before stocking so that it will bloom with",
     "plankton", "bloodworms only", "water hyacinth", "tadpoles", "A",
     "The green soup feeds the fry."),
    (T_LIV, "Medium", "The long net drawn round a pond and hauled ashore to harvest fish is the",
     "seine net", "gill net", "cast net", "trap net", "A",
     "It surrounds and gathers."),
    (T_LIV, "Medium", "Day-old chicks are started on a protein-rich feed called",
     "starter mash", "layer mash", "finisher meal", "bran only", "A",
     "The first food of brooding."),
    (T_LIV, "Medium", "The viral poultry disease Newcastle is guarded against by",
     "vaccination", "dipping", "docking", "candling", "A",
     "The needle comes before the cough."),
    (T_LIV, "Medium", "In the hive, egg-laying is the sole duty of the",
     "queen bee", "worker bee", "drone bee", "guard bee", "A",
     "She alone mothers the colony."),

    # ------------------------------------------------------------- institutions & processing
    (T_EXT, "Medium", "Grinding cassava into flour and garri at a village mill is a form of",
     "agro-processing", "afforestation", "surveying", "rotation", "A",
     "Value is added at the mill."),
    (T_EXT, "Hard", "The bodies once set up to buy and market Nigeria's export crops in bulk were the",
     "commodity boards", "chambers of commerce", "marketing guilds", "cooperative unions", "A",
     "Cocoa and groundnut passed through them."),
    (T_EXT, "Medium", "An extension method where a improved plot of land is farmed to teach by example is the",
     "demonstration plot", "T and V tour", "census survey", "market survey", "A",
     "Seeing once beats hearing twice."),
    (T_EXT, "Hard", "Harrowing and ridging, done after the first ploughing, are collectively called",
     "secondary tillage", "primary tillage", "zero tillage", "minimum tillage", "A",
     "The finishing passes on the soil."),
]

build_batch(
    S,
    "batch_155_waec_agric6.json",
    "155",
    "WAEC Agricultural Science round 6 (R29 top-up): A-horizon "
    "eluviation, grey waterlogged subsoil, sand-clay-loam behaviour, "
    "humus, green manuring, compost turning; drip vs flood irrigation, "
    "drainage, fallowing, afforestation; photoperiodism, seed dressing, "
    "transplanting, hardening off, roguing, pruning, staking, weed "
    "competition; Panicum maximum, zero grazing, silage vs hay; rabbit "
    "hutches, pond plankton bloom, seine net, starter mash, Newcastle "
    "vaccination, queen bee; agro-processing, commodity boards, "
    "demonstration plot, secondary tillage. Scanned against WAEC "
    "rounds 1-5, NECO Agric (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
