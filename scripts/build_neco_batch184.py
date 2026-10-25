"""Batch 184 - WAEC Agricultural Science round 7 (WAEC top-up, R35).

Grows WAEC Agric from 223 toward ~255 with angles not yet in the
bank: silviculture; porosity and field capacity; urea as a pure
nitrogen fertiliser; purple tinges meaning phosphorus hunger and
blossom-end rot meaning calcium hunger; calving; the pullet; the
broody hen; moulting; creep feed for piglets; evening light for
layers; mastitis and brucellosis; damping off in the nursery; the
plough share; GPS in surveying; the farm balance sheet and salvage
value; the extension field day; the evaporimeter; shelterbelts;
hydroponics and the greenhouse; polythene-pot seedlings; organic
farming; fish monoculture, the hatchery and fry; the soft loan;
the fertiliser subsidy; farm insurance. Scanned against WAEC
rounds 1-6, NECO Agric (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch184.py -> content/batch_184_waec_agric7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Agricultural Science"

T_SC = "Meaning and Scope of Agriculture"
T_SSF = "Soil Science Further"
T_SST = "Soil Science and Fertility"
T_AN = "Animal Production"
T_AH = "Animal Health"
T_PD = "Pests and Diseases"
T_TOL = "Farm Tools and Machinery"
T_MS = "Mechanisation and Surveying"
T_FR = "Farm Records and Planning"
T_EXT = "Agricultural Extension"
T_MET = "Agro-meteorology"
T_FOR = "Agro-forestry and Forests"
T_CRO = "Crop Production"
T_CHP = "Crop Husbandry Practices"
T_FIS = "Fish Farming"
T_ECN = "Agricultural Economics"

PASSAGES = []
PQ = []

Q = [
    (T_SC, "Medium", "The branch of agriculture devoted to raising and tending trees for timber and wood is",
     "silviculture", "horticulture",
     "apiculture", "aquaculture", "A",
     "It is farming whose crop is the forest itself."),
    (T_SSF, "Medium", "The tiny spaces between soil particles, which hold air and water, make up the soil's",
     "porosity", "texture",
     "plasticity", "salinity", "A",
     "A well-pored soil breathes and drinks at once."),
    (T_SSF, "Hard", "The amount of water a soil holds after rain has drained away and free water is gone is its",
     "field capacity", "wilting point",
     "saturation point", "permanent drainage", "A",
     "The soil's cup is full but not overflowing."),
    (T_SST, "Medium", "Of these fertilisers, the one that supplies ONLY nitrogen to the soil is",
     "urea", "single superphosphate",
     "muriate of potash", "limestone", "A",
     "Forty-six per cent of its weight is pure nitrogen."),
    (T_SST, "Medium", "A maize crop whose lower leaves show purple tinges is most likely short of",
     "phosphorus", "nitrogen",
     "iron", "boron", "A",
     "Hunger for phosphorus paints the leaves violet."),
    (T_SST, "Hard", "Tomato fruits developing blackened, sunken patches at their blossom end point to a shortage of",
     "calcium", "potassium",
     "magnesium", "sulphur", "A",
     "Weak cell walls rot where the flower once sat."),
    (T_AN, "Easy", "When a cow brings forth her calf, the event is called",
     "calving", "lambing",
     "kidding", "farrowing", "A",
     "The cow drops her calf in the calving pen."),
    (T_AN, "Easy", "A young female chicken that has not yet begun to lay is a",
     "pullet", "cockerel",
     "broiler", "hen", "A",
     "She waits in the growing house for her first egg."),
    (T_AN, "Medium", "A hen that stops laying, plucks her breast feathers and sits stubbornly on eggs is said to be",
     "broody", "moulting",
     "culling", "molting feathers for show", "A",
     "Her body has turned to hatching duty."),
    (T_AN, "Medium", "The yearly shedding and renewal of a chicken's feathers, when laying pauses, is called",
     "moulting", "brooding",
     "debeaking", "candling", "A",
     "Old feathers drop; new ones dress the bird again."),
    (T_AN, "Hard", "The special feed given to young piglets in a corner their mother cannot reach is called",
     "creep feed", "starter mash for chicks",
     "roughage for sows", "silage", "A",
     "The low gap admits only the little ones."),
    (T_AN, "Medium", "Farmers burn extra lights in the layer house into the evening chiefly to",
     "extend the birds' feeding and laying hours", "keep the house warm through harmattan",
     "discourage rats from entering", "improve the eggs' shell colour", "A",
     "Longer days persuade the hen to lay."),
    (T_AH, "Medium", "A cow with a hot, swollen udder giving blood-streaked milk is suffering from",
     "mastitis", "foot and mouth disease",
     "brucellosis always", "rinderpest", "A",
     "The udder itself has caught fire."),
    (T_AH, "Hard", "The bacterial disease notorious for causing abortion in pregnant cows is",
     "brucellosis", "Newcastle disease",
     "coccidiosis", "anthrax only", "A",
     "Undulant fever rides its raw milk too."),
    (T_PD, "Medium", "In the nursery, seedlings suddenly toppling over with pinched stems at soil level signal the disease called",
     "damping off", "mosaic virus",
     "rust", "smut", "A",
     "The young stems rot where they meet the earth."),
    (T_TOL, "Hard", "The part of the mouldboard plough that first slices the soil at the bottom of the furrow is the",
     "share", "beam",
     "landside", "hitch", "A",
     "The sharp edge leads the plough's work."),
    (T_MS, "Hard", "The hand-held device that fixes a farm's position accurately by listening to satellites is the",
     "GPS receiver", "abney level",
     "dumpy level", "planimeter", "A",
     "A constellation above guides the hand below."),
    (T_FR, "Medium", "The statement showing a farm's assets, liabilities and net worth on a given date is the",
     "balance sheet", "income statement",
     "cash flow plan", "farm diary", "A",
     "On that date the whole farm stands on one page."),
    (T_FR, "Medium", "The amount an old tractor is expected to fetch at the end of its working life is its",
     "salvage value", "purchase cost",
     "book value always", "insurance premium", "A",
     "The junk man's price closes its story."),
    (T_EXT, "Medium", "An occasion when many farmers gather on a model plot to see a new practice demonstrated is a",
     "field day", "market day",
     "census day", "debt day", "A",
     "Seeing once outweighs hearing twice."),
    (T_MET, "Hard", "The instrument that measures the rate at which water evaporates into the air is the",
     "evaporimeter", "hygrometer",
     "barometer", "anemometer", "A",
     "Its pan of water shrinks day by day."),
    (T_FOR, "Medium", "The wide belt of trees planted across the path of desert winds in Nigeria's far north is a",
     "shelterbelt", "windbreak of one row only",
     "hedgerow", "riparian buffer", "A",
     "Many rows of trees stand in the sand's way."),
    (T_CRO, "Hard", "Growing crops with their roots in nutrient-rich water instead of soil is called",
     "hydroponics", "hydrology",
     "hydropower farming", "hydrothermal culture", "A",
     "The roots drink a mixed diet of dissolved salts."),
    (T_CRO, "Medium", "A transparent enclosure where temperature and humidity are controlled for raising tender crops is a",
     "greenhouse", "granary",
     "silo", "crib", "A",
     "Under its glass the weather obeys the farmer."),
    (T_CRO, "Medium", "Seedlings raised in small polythene bags in the nursery are transplanted mainly because the bags",
     "keep the root ball intact at transplanting", "make the seedlings taste sweeter",
     "stop the seedlings from ever growing tall", "remove the need for watering", "A",
     "Roots ride to the field in their own ball of earth."),
    (T_CHP, "Medium", "The farming system that avoids synthetic fertilisers and pesticides, relying on compost and natural enemies, is",
     "organic farming", "shifting cultivation",
     "plantation farming", "mechanised farming", "A",
     "The land is fed the way nature feeds it."),
    (T_FIS, "Medium", "Stocking a pond with only one species of fish throughout is called",
     "monoculture", "polyculture",
     "integrated culture", "mixed farming", "A",
     "One fish alone owns the water."),
    (T_FIS, "Hard", "The facility where fish eggs are hatched and the young ones raised through their first fragile days is a",
     "hatchery", "nursery for pigs",
     "grow-out pond for adults", "fish shop", "A",
     "Life begins for the fry under its care."),
    (T_FIS, "Easy", "Very young fish that have just hatched are known as",
     "fry", "fingerlings",
     "broodstock", "table fish", "A",
     "Fry grow to fingerlings before stocking."),
    (T_ECN, "Medium", "A loan granted to farmers at little or no interest, often by government or donors, is a",
     "soft loan", "commercial loan",
     "hire purchase", "overdraft", "A",
     "The repayment terms are gentler than the bank's."),
    (T_ECN, "Medium", "When government pays part of the cost of fertiliser so farmers buy it cheaper, the payment is a",
     "subsidy", "tariff",
     "levy", "premium", "A",
     "The treasury carries part of the bag's price."),
    (T_ECN, "Medium", "A poultry farmer who insures his flock against disease outbreaks is chiefly guarding against",
     "risk", "taxation",
     "depreciation of feeds", "price crashes only", "A",
     "A small premium stands between him and ruin."),
]

build_batch(
    S,
    "batch_184_waec_agric7.json",
    "184",
    "WAEC Agric round 7 (R35 top-up): silviculture; porosity; field "
    "capacity; urea as pure nitrogen; purple tinges of phosphorus "
    "hunger; blossom-end rot and calcium; calving; the pullet; the "
    "broody hen; moulting; creep feed; evening light for layers; "
    "mastitis; brucellosis; damping off; the plough share; GPS; "
    "the balance sheet; salvage value; the field day; the "
    "evaporimeter; shelterbelts; hydroponics; the greenhouse; "
    "polythene-pot seedlings; organic farming; fish monoculture; "
    "the hatchery; fry; the soft loan; the fertiliser subsidy; "
    "farm insurance. Scanned against WAEC rounds 1-6, NECO Agric "
    "(all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
