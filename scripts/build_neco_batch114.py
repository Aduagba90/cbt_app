"""Batch 114 - NECO Geography round 3 (NECO top-up, Round 22).

Lifts NECO Geography from 127 toward ~175 with angles not yet in any
bank: map work (contours, gradient, scale, relief representation),
rainfall types, plate tectonics, earthquakes and volcanoes, karst and
arid landforms, lake types, agricultural systems, energy sources and
renewables, and Niger Delta environmental problems. Scanned against
NECO rounds 1-2, WAEC Geography (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch114.py -> content/batch_114_neco_geo3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_MAP = "Maps and Map Work"
T_RAIN = "Types of Rainfall"
T_TECT = "Plate Tectonics and Hazards"
T_LAND = "Karst and Arid Landforms"
T_LAKE = "Lakes and Water Bodies"
T_AGRI = "Agricultural Systems"
T_ENER = "Energy and Resources"
T_DEL = "Niger Delta and Environment"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- map work
    (T_MAP, "Medium", "What name is given to map lines that connect points of the same altitude?",
     "contours", "isobars", "isohyets", "isotherms", "A",
     "Each line holds one altitude."),
    (T_MAP, "Medium", "Lines joining places of equal rainfall on a map are",
     "isohyets", "contours", "isobars", "isonephs", "A",
     "Rainfall maps are drawn with them."),
    (T_MAP, "Medium", "Lines joining places of equal pressure are",
     "isobars", "isohyets", "contours", "isohelses", "A",
     "Weather charts lean on them."),
    (T_MAP, "Hard", "On a topographic map, contours very close together indicate a",
     "steep slope", "gentle slope", "flat plain", "deep valley floor", "A",
     "Height climbs in a short run."),
    (T_MAP, "Hard", "A gradient is expressed as a ratio of",
     "vertical rise to horizontal run", "distance travelled to time taken", "map area to ground area", "speed of flow to cost of travel", "A",
     "One in so many measures it."),
    (T_MAP, "Medium", "A scale of 1:50,000 means one centimetre on the map stands for",
     "50,000 cm on the ground", "50,000 kilometres", "50 centimetres only", "500 kilometres", "A",
     "Multiply the map length by the ratio.", "50000"),
    (T_MAP, "Medium", "Hachures and layer colouring are methods of showing",
     "relief", "rainfall", "population", "soil", "A",
     "The land's shape gets drawn."),
    (T_MAP, "Hard", "The conventional map sign for a marsh is usually",
     "short horizontal blue tufts", "a solid red dot", "a black cross", "a brown triangle", "A",
     "Reeds drawn in blue mark it."),

    # ------------------------------------------------------------- rainfall
    (T_RAIN, "Medium", "Rainfall caused by sun-heated air rising from the ground is",
     "convectional rainfall", "orographic rainfall", "frontal rainfall", "cyclonic rainfall", "A",
     "Afternoon towers build it."),
    (T_RAIN, "Medium", "Rainfall formed where moist air climbs a mountain barrier is",
     "orographic rainfall", "convectional rainfall", "frontal rainfall", "relief-free rainfall", "A",
     "The windward slope is soaked."),
    (T_RAIN, "Hard", "The dry zone on the leeward side of a mountain is the",
     "rain shadow", "dew point", "convergence belt", "triple point", "A",
     "Sinking air keeps it dry."),
    (T_RAIN, "Hard", "Frontal rainfall develops where warm and cold air masses",
     "meet and the warm air rises", "stand perfectly still", "move in the same direction", "cancel each other out", "A",
     "The front forces the lift."),
    (T_RAIN, "Medium", "Convectional rainfall in Nigeria is commonest in",
     "the afternoon of the wet season", "the dry season mornings", "the harmattan nights", "the winter weeks", "A",
     "Day heat builds the storm."),

    # ------------------------------------------------------------- tectonics and hazards
    (T_TECT, "Medium", "The theory explaining earth's crust as moving slabs is",
     "plate tectonics", "continental drift only", "isostasy", "planation", "A",
     "Plates ride the mantle slowly."),
    (T_TECT, "Hard", "The boundary where two plates collide and one dives beneath is",
     "a subduction zone", "a rift valley", "a transform fault", "a mid-ocean trench vent", "A",
     "One slab sinks below another."),
    (T_TECT, "Medium", "A long crack valley formed where plates pull apart is a",
     "rift valley", "caldera", "geosyncline", "corrie", "A",
     "East Africa displays a giant one."),
    (T_TECT, "Hard", "The scale used to express earthquake strength is the",
     "Richter scale", "Beaufort scale", "Mohs scale", "pH scale", "A",
     "Each step multiplies the power."),
    (T_TECT, "Medium", "An opening in the crust from which lava erupts is a",
     "volcano", "geyser", "hot spring only", "fumarole", "A",
     "Molten rock reaches the air."),
    (T_TECT, "Hard", "Quakes begin at a point beneath the surface called the",
     "focus", "epicentre", "isoseimal line", "seismograph", "A",
     "The surface point above differs."),

    # ------------------------------------------------------------- karst and arid
    (T_LAND, "Medium", "Stalactites and stalagmites decorate",
     "limestone caves", "granite domes", "sand dunes", "mud volcanoes", "A",
     "Dripping calcite builds them."),
    (T_LAND, "Hard", "A limestone surface carved into grooves and ridges by rainwater is called a",
     "clint-and-grike pavement", "barchan dune field", "pediment plain surface", "dry salt pan", "A",
     "Rain solution etches the limestone."),
    (T_LAND, "Hard", "A sinkhole or doline forms when limestone",
     "collapses into a cave below", "is pushed up by lava", "dries into loose sand", "freezes and cracks open", "A",
     "The old cave roof gives way."),
    (T_LAND, "Medium", "Which dune looks like a new moon with horns trailing downwind?",
     "barchan", "seif", "star dune", "dome", "A",
     "It marches across the desert floor."),
    (T_LAND, "Hard", "A mushroom rock in the desert owes its shape to",
     "wind erosion at the base", "river deposition", "glacial plucking", "coastal wave attack", "A",
     "Sand-laden wind cuts the stem."),
    (T_LAND, "Medium", "Rock pedestals, yardangs and zeugen are worked by",
     "wind abrasion", "soil creep", "wave sorting", "frost shattering", "A",
     "The desert's chisel is the wind."),

    # ------------------------------------------------------------- lakes
    (T_LAKE, "Medium", "Lake Kainji on the Niger was formed by",
     "damming the river", "volcanic eruption", "glacial scouring", "meteor impact", "A",
     "Man's wall holds the water."),
    (T_LAKE, "Hard", "A lake in a volcano's collapsed crater is a",
     "caldera lake", "oxbow lake", "tarn", "lagoon", "A",
     "The crater rim cups the water."),
    (T_LAKE, "Medium", "A crescent lake left by an abandoned river bend is an",
     "oxbow lake", "caldera lake", "tarn", "paternoster", "A",
     "The old river loop is cut off."),
    (T_LAKE, "Hard", "A lake held behind moraine in a mountain cirque is a",
     "tarn", "lagoon", "bayou", "sebkha", "A",
     "Ice left the basin behind."),
    (T_LAKE, "Medium", "Lake Chad is shrinking chiefly because of",
     "drought and water abstraction", "rising ocean tides", "earthquakes", "volcanic ash", "A",
     "Less inflow, more pumping."),

    # ------------------------------------------------------------- agriculture
    (T_AGRI, "Medium", "Farming that feeds mainly the farmer's family is",
     "subsistence farming", "plantation farming", "commercial grain farming", "truck farming", "A",
     "The harvest feeds the house."),
    (T_AGRI, "Medium", "A plantation is a large estate growing",
     "one cash crop for export", "mixed food crops only", "forest trees only", "fish in ponds", "A",
     "Cocoa, rubber or oil palm fills it."),
    (T_AGRI, "Hard", "Taungya farming combines food crops with",
     "young forest trees", "fish ponds", "poultry cages", "irrigated rice only", "A",
     "Farmers tend both at once."),
    (T_AGRI, "Medium", "Shifting cultivation degrades land when the fallow period becomes",
     "too short", "too long", "perfectly balanced", "fully planted", "A",
     "Soil never gets time to heal."),
    (T_AGRI, "Medium", "Irrigation farming in Nigeria's north depends heavily on",
     "river water and boreholes", "sea water", "glacier melt", "desalination plants", "A",
     "Kano's schemes draw rivers."),
    (T_AGRI, "Hard", "Nomadic herding moves herds chiefly in response to",
     "rainfall and pasture", "market days alone", "road construction", "political rallies", "A",
     "The grass leads the cattle."),

    # ------------------------------------------------------------- energy
    (T_ENER, "Medium", "Coal, crude oil and natural gas are together called",
     "fossil fuels", "renewable sources", "green energies", "primary foods", "A",
     "Buried ancient life made them."),
    (T_ENER, "Medium", "From this list, the source nature refills daily is",
     "solar power", "coal", "crude oil", "natural gas", "A",
     "The sun refills it daily."),
    (T_ENER, "Hard", "Gas flaring in the oil fields wastes a resource that could be used for",
     "cooking gas and power", "road building", "fertiliser sacks", "cement mixing", "A",
     "The flare burns usable money."),
    (T_ENER, "Medium", "Firewood and charcoal dominate rural cooking energy, causing",
     "deforestation", "flood control", "soil enrichment", "cloud seeding", "A",
     "Every felled tree burns once."),
    (T_ENER, "Hard", "The share of electricity in a national grid supplied at any moment is called",
     "generating capacity", "tariff band", "load shedding", "wheeling license", "A",
     "Installed plants set the limit."),

    # ------------------------------------------------------------- niger delta
    (T_DEL, "Hard", "Oil spillage damages farmland mainly by",
     "killing crops and poisoning soil", "adding free fertiliser", "improving drainage", "cooling the surface", "A",
     "The black film starves roots."),
    (T_DEL, "Medium", "Canalization and dredging in the delta have sped up",
     "erosion and salt intrusion", "tree planting drives", "fish breeding schemes", "rainfall totals rising", "A",
     "Salt rides up the new channels."),
    (T_DEL, "Medium", "Mangrove clearance in the delta removes nature's",
     "storm buffer and fish nursery", "oil refinery", "grain store", "rail terminal", "A",
     "The swamp guards the coast."),
    (T_DEL, "Hard", "Host-community agitations in the delta stem mostly from",
     "pollution and few benefits", "excess rainfall", "too many schools", "cold weather", "A",
     "Poverty sits beside the pipelines."),
    (T_DEL, "Medium", "Ogoni cleanup efforts target mainly",
     "remediating polluted land", "building new seaports", "drilling deeper wells", "importing crude oil", "A",
     "HYPREP leads the cleanup work."),
]

build_batch(
    S,
    "batch_114_neco_geo3.json",
    "114",
    "NECO Geography round 3 (Round 22 top-up): contours, isohyets and "
    "isobars, steep-slope contour spacing, gradient as rise over "
    "distance, 1:50,000 scale, relief representation, marsh symbols, "
    "convectional, orographic and frontal rainfall, rain shadows, plate "
    "tectonics, subduction, rift valleys, Richter scale, volcanoes, "
    "focus vs epicentre, stalactites, clints and grikes, dolines, "
    "barchans, mushroom rocks, wind abrasion, Kainji, caldera and oxbow "
    "lakes, tarns, Lake Chad's shrinkage, subsistence and plantation "
    "farming, taungya, fallow shortfalls, irrigation, nomadic herding, "
    "fossil vs renewable energy, gas flaring, firewood deforestation, "
    "generating capacity, oil spills, canalization, mangrove loss, "
    "host-community grievances and the Ogoni cleanup. Scanned against "
    "NECO rounds 1-2, WAEC Geography (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
