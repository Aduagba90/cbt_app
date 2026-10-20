"""Batch 116 - NECO Agricultural Science round 3 (NECO top-up, Round 22).

Lifts NECO Agric from 130 toward ~175 with angles not yet in any bank:
soil composition and water, plant nutrients and fertilisers, farm
machinery and implements, irrigation and drainage, crop pests and
diseases with control, weeds and their menace, apiculture, livestock
breeds and feeds, farm structures and the problems of Nigerian
agriculture. Scanned against NECO rounds 1-2, WAEC Agric (all rounds)
and the JAMB pool.

    python3 scripts/build_neco_batch116.py -> content/batch_116_neco_agric3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Agricultural Science"

T_SOIL = "Soil and Water"
T_NUT = "Plant Nutrition"
T_MACH = "Farm Machinery and Implements"
T_WATER = "Irrigation and Drainage"
T_PROT = "Crop Protection"
T_APIC = "Apiculture and Small Stock"
T_STOCK = "Livestock Breeds and Feeds"
T_STR = "Farm Structures and Nigerian Agriculture"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- soil and water
    (T_SOIL, "Medium", "The four main components of a fertile soil are minerals, organic matter, water and",
     "air", "salt", "sand only", "gravel chips", "A",
     "Roots breathe the fourth."),
    (T_SOIL, "Medium", "Soil water held so tightly that roots cannot draw it is called",
     "hygroscopic water", "capillary water", "gravitational water", "rain water", "A",
     "It clings beyond any root's reach."),
    (T_SOIL, "Hard", "Capillary water is the portion that",
     "remains usable by plants", "drains away within hours", "never touches roots", "stays locked in gravel", "A",
     "It feeds the standing crop."),
    (T_SOIL, "Medium", "Spreading lime on sour farmland chiefly",
     "raises its pH", "lowers its pH", "adds nitrogen", "kills all bacteria", "A",
     "Sour soil turns sweet again."),
    (T_SOIL, "Medium", "Soil colour that is dark usually signals plenty of",
     "humus", "iron oxide", "quartz sand", "lime shells", "A",
     "Decayed matter darkens it."),
    (T_SOIL, "Hard", "Which soil class drains yet holds moisture, suiting most crops?",
     "loam", "heavy clay", "coarse sand", "pure silt", "A",
     "Sand, silt and clay balance it."),

    # ------------------------------------------------------------- nutrition
    (T_NUT, "Medium", "The nutrient plants need most for green leafy growth is",
     "nitrogen", "calcium", "boron", "copper", "A",
     "Chlorophyll depends on it."),
    (T_NUT, "Medium", "Phosphorus is most important for",
     "root development and flowering", "leaf greenness alone", "stalk hardness", "fruit sweetness only", "A",
     "Strong starts come from it."),
    (T_NUT, "Hard", "Yellowing of older lower leaves in a young crop most often points to shortage of",
     "nitrogen", "potassium", "molybdenum", "chlorine", "A",
     "The mobile nutrient drains away."),
    (T_NUT, "Medium", "Potassium chiefly improves a plant's",
     "disease resistance", "leaf colour alone", "stem height alone", "seed coat thickness", "A",
     "Sturdy crops carry enough of it."),
    (T_NUT, "Medium", "NPK 15-15-15 fertiliser contains nitrogen, phosphorus and",
     "potassium", "protein", "phosphate rock", "plaster", "A",
     "Three numbers name the trio."),
    (T_NUT, "Hard", "Legume root nodules house bacteria that convert air nitrogen into usable forms; the process is",
     "nitrogen fixation", "nitrification only", "denitrification", "ammonification", "A",
     "The nodules are tiny factories."),

    # ------------------------------------------------------------- machinery
    (T_MACH, "Medium", "Which implement does the first opening and turning of the land?",
     "plough", "harrow", "ridger", "planter", "A",
     "It opens and turns the land first."),
    (T_MACH, "Medium", "After ploughing, the implement used to break clods and level the surface is the",
     "harrow", "mower", "thresher", "sheller", "A",
     "Its iron teeth comb the soil."),
    (T_MACH, "Hard", "The implement that heaps soil into ridges for yam or cassava is the",
     "ridger", "cultivator", "seed drill", "boom sprayer", "A",
     "The ridges rise behind its blade."),
    (T_MACH, "Medium", "A combine harvester does reaping, threshing and",
     "winnowing in one pass", "ploughing by night", "irrigating rows", "baling straw", "A",
     "One machine, three jobs at once."),
    (T_MACH, "Easy", "The simple tool used for weeding and making heaps in Nigeria is the",
     "hoe", "spanner", "jack plane", "gauge", "A",
     "Every farm hand owns one."),

    # ------------------------------------------------------------- water
    (T_WATER, "Medium", "Furrow irrigation delivers water to crops through",
     "small channels between ridges", "overhead sprinklers", "dripping tubes on beds", "flooding whole fields", "A",
     "The furrows drink along the rows."),
    (T_WATER, "Medium", "Drip irrigation saves water by",
     "placing drops at each plant's root zone", "spraying the whole farm", "flooding the furrows deeply", "canal diversion only", "A",
     "Almost nothing is wasted."),
    (T_WATER, "Hard", "The sprinkler system is most suitable for",
     "lawns and spaced crops", "paddy rice fields", "fishponds only", "thick forests", "A",
     "Rain is manufactured overhead."),
    (T_WATER, "Medium", "Farm drainage is installed chiefly to",
     "remove excess water", "speed up erosion", "water the crops", "raise the water table", "A",
     "Soggy roots otherwise suffocate."),
    (T_WATER, "Hard", "Salinity build-up in over-irrigated dry-land soils is fought by",
     "leaching with good drainage", "adding more fertiliser", "planting deeper", "flooding non-stop", "A",
     "The salts must be flushed down."),

    # ------------------------------------------------------------- crop protection
    (T_PROT, "Medium", "Stem borers attack maize by",
     "tunnelling into the stalk", "sucking pod sap", "eating roots only", "biting cobs only", "A",
     "Deadheart is its tell-tale sign."),
    (T_PROT, "Medium", "Weevils damage stored grains mainly by",
     "boring into the kernels", "spinning webs on bags", "wetting the store", "carrying sand in", "A",
     "Fine flour dust betrays them."),
    (T_PROT, "Hard", "Maize rust and smut are spread mostly by",
     "wind-borne spores", "bees only", "irrigation water only", "birds' feathers only", "A",
     "The spores ride the breeze."),
    (T_PROT, "Medium", "Cassava mosaic disease is spread mainly by",
     "whiteflies", "beetles alone", "earthworms", "termites", "A",
     "The winged carrier moves it."),
    (T_PROT, "Hard", "Introducing the insect's natural enemy to curb it is",
     "biological control", "chemical control", "cultural control", "quarantine only", "A",
     "Nature is set against nature."),
    (T_PROT, "Medium", "Early planting and crop rotation as pest measures are forms of",
     "cultural control", "biological control", "chemical control", "legal control", "A",
     "Good husbandry starves pests."),
    (T_PROT, "Hard", "Weeds reduce crop yields chiefly by competing for",
     "light, water and nutrients", "market prices", "farm labourers", "storage space", "A",
     "The thief stands beside the crop."),
    (T_PROT, "Medium", "Weedkillers that spare the growing crop are described as",
     "weeds but spares the crop", "every plant it touches", "only insects", "only stored grain pests", "A",
     "It tells friend from foe."),

    # ------------------------------------------------------------- apiculture and small stock
    (T_APIC, "Medium", "Beekeeping for honey and wax is called",
     "apiculture", "aquaculture", "sericulture", "horticulture", "A",
     "Hives house the business."),
    (T_APIC, "Hard", "Every egg in the hive is laid by the",
     "queen", "worker", "drone", "guard", "A",
     "One mother fills the hive."),
    (T_APIC, "Hard", "Rearing rabbits for meat and skins is",
     "cuniculture", "pisciculture", "oleiculture", "viticulture", "A",
     "The hutches multiply fast."),
    (T_APIC, "Medium", "A smoker is used at the hive to",
     "calm the bees during work", "kill the colony", "warm the honey", "seal the combs", "A",
     "Smoke softens their alarm."),

    # ------------------------------------------------------------- breeds and feeds
    (T_STOCK, "Hard", "A cattle breed resistant to trypanosomiasis in Nigeria is the",
     "Muturu", "White Fulani only", "Holstein", "Hereford", "A",
     "The small humpless breed endures."),
    (T_STOCK, "Medium", "The White Fulani is kept in the north mainly for",
     "milk and meat", "wool", "hides for export only", "draught only", "A",
     "The zebu serves both tables."),
    (T_STOCK, "Hard", "Feeds high in fibre like straw and elephant grass are classified as",
     "roughages", "concentrates", "supplements", "premixes", "A",
     "Ruminants handle them well."),
    (T_STOCK, "Medium", "Maize and groundnut cake in a ration serve as",
     "concentrates", "roughage for fibre", "mineral licks", "water sources", "A",
     "Little bulk carries much power."),
    (T_STOCK, "Medium", "A balanced ration supplies all needed nutrients in the right",
     "proportions", "colours", "flavours", "weights of water", "A",
     "Not too much, not too little."),

    # ------------------------------------------------------------- structures and Nigerian agriculture
    (T_STR, "Medium", "A crush is a farm structure used for",
     "restraining cattle", "storing maize cobs", "brooding chicks", "mixing feed", "A",
     "The animal stands held tight."),
    (T_STR, "Medium", "A dip is built to",
     "control ticks on livestock", "water the crops", "store water", "rear fish", "A",
     "The animals wade through."),
    (T_STR, "Hard", "A gauge that measures rainfall on the farm is the",
     "rain gauge", "hygrometer", "barometer", "anemometer", "A",
     "Millimetres collect inside."),
    (T_STR, "Medium", "The chief duty of extension workers is to",
     "teach farmers", "sell farm inputs", "buy all harvests", "insure the farms", "A",
     "Research reaches farms through them."),
    (T_STR, "Hard", "Fragmented family land under communal tenure chiefly hinders",
     "mechanised commercial farming", "subsistence hoe farming", "nomadic grazing", "market gardening", "A",
     "Small scattered plots bar machines."),
    (T_STR, "Medium", "Poor storage losses in Nigeria are best cut by",
     "improved silos and dry processing", "harvesting earlier each year", "planting more acres", "selling at night", "A",
     "Keep the rat and mould out."),
    (T_STR, "Medium", "Young school leavers are drawn into farming today mainly through",
     "agribusiness openings", "free land grants", "compulsory service", "tax rebates only", "A",
     "Money in the chain attracts them."),
]

build_batch(
    S,
    "batch_116_neco_agric3.json",
    "116",
    "NECO Agricultural Science round 3 (Round 22 top-up): soil "
    "components, hygroscopic vs capillary water, liming, dark humus, "
    "loam, nitrogen, phosphorus and potassium roles, lower-leaf "
    "yellowing, NPK, nitrogen fixation, plough, harrow, ridger, combine "
    "harvester, hoe, furrow and drip irrigation, sprinklers, drainage "
    "and salinity leaching, stem borers, weevils, rust and smut spores, "
    "cassava mosaic whiteflies, biological and cultural control, weed "
    "competition, selective herbicides, apiculture, the queen, "
    "cuniculture, smokers, Muturu and White Fulani cattle, roughages vs "
    "concentrates, balanced rations, crush, dip, rain gauge, extension "
    "work, fragmented tenure, storage losses and youth agribusiness. "
    "Scanned against NECO rounds 1-2, WAEC Agric (all rounds) and the "
    "JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
