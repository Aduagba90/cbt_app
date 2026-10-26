"""Batch 208 - WAEC Geography round 8 (WAEC top-up, R41).

Grows WAEC Geography from 255 toward ~280 with angles not yet in
the bank: drumlins; eskers; river capture; cataracts; potholes;
the braided channel; the bird's-foot delta; the beach; longshore
drift; the tombolo; the natural arch; coasts of emergence; the
atoll; the continental slope; artisanal fishing; dew point; fog;
the anticyclone; fire-resistant savanna bark; the baobab; the
pampas; the llanos; the steppes; emigration defined; the total
fertility rate. Scanned against the whole Geography pool (WAEC,
NECO and JAMB stems, 1,056 items).

    python3 scripts/build_neco_batch208.py -> content/batch_208_waec_geo8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_GLA = "Glaciation"
T_RIV = "River Processes and Landforms"
T_COA = "Coastal Landforms"
T_OCE = "Oceans"
T_CLI = "Weather and Climate"
T_VEG = "Vegetation"
T_POP = "Population"
T_ECO = "Economic Geography"

PASSAGES = []
PQ = []

Q = [
    (T_GLA, "Hard", "The smooth, egg-shaped hills of boulder clay, elongated in the direction the ice travelled, are called",
     "drumlins", "eskers",
     "moraines", "kames", "A",
     "The glacier moulded the till like dough."),
    (T_GLA, "Hard", "A long, winding ridge of sand and gravel laid down by a melt-water stream beneath a glacier is an",
     "esker", "drumlin",
     "erratic", "arête", "A",
     "The old stream's bed is left standing as a ridge."),
    (T_RIV, "Hard", "The diversion of the headwaters of one river into the channel of a stronger neighbouring river is called",
     "river capture", "river regime",
     "river erosion", "river deposition", "A",
     "The robber stream steals its neighbour's source."),
    (T_RIV, "Medium", "A series of rapids and small waterfalls that break a river's course over hard rock, as on the Nile, are called",
     "cataracts", "geysers",
     "pot-holes", "meanders", "A",
     "Navigation halts where they begin."),
    (T_RIV, "Medium", "The circular hollows ground into a river's rocky bed by swirling stones are called",
     "pot-holes", "plunge pools",
     "rapids", "spillways", "A",
     "A stone caught in an eddy drills its own well."),
    (T_RIV, "Medium", "A river choked with load that flows in several interlacing channels divided by banks of sand is said to be",
     "braided", "meandering",
     "incised", "misfit", "A",
     "The divided stream splits and rejoins again and again."),
    (T_RIV, "Hard", "A delta with long, finger-like distributaries pushing far into the sea, like that of the Mississippi, is described as",
     "bird's-foot", "arcuate",
     "estuarine", "cusped", "A",
     "The river's toes spread across the water."),
    (T_COA, "Easy", "The band of sand and shingle deposited along the shore between the low- and high-water marks is the",
     "beach", "spit",
     "bar", "stack", "A",
     "Every tide re-combs its sand."),
    (T_COA, "Medium", "The slow drift of sand and shingle along a coast, set moving by waves breaking at an angle to the shore, is called",
     "longshore drift", "coastal fetch",
     "wave refraction", "tidal flush", "A",
     "The beach material inches along the coast."),
    (T_COA, "Hard", "A spit that grows right out from the coast until it ties an offshore island to the mainland forms a",
     "tombolo", "lagoon",
     "barrier beach", "cusp", "A",
     "The island is roped to the shore by sand."),
    (T_COA, "Medium", "Where waves attack a headland from both sides and bore a tunnel through it, the bridge of rock left standing is a natural",
     "arch", "stack",
     "stump", "geo", "A",
     "One day its roof will fall and leave a stack."),
    (T_COA, "Hard", "Old beaches and wave-cut platforms now lying high and dry inland are evidence of a coast of",
     "emergence", "submergence",
     "recession", "erosion", "A",
     "The land rose, leaving the old shore in the air."),
    (T_OCE, "Hard", "The ring-shaped coral reef that encloses a lagoon, formed around a slowly sinking volcanic island, is an",
     "atoll", "fringing reef",
     "barrier reef", "patch reef", "A",
     "The island drowned; its coral crown remained."),
    (T_OCE, "Medium", "The steeply sloping zone that carries the sea floor from the edge of the continental shelf down to the deep abyssal plain is the",
     "continental slope", "continental shelf",
     "abyssal plain", "ocean trench", "A",
     "The shelf's edge plunges steeply from here."),
    (T_ECO, "Medium", "The small-scale family fishing carried on with canoes and simple gear along the Nigerian coast is described as",
     "artisanal fishing", "industrial trawling",
     "offshore fleets", "long-line fishing", "A",
     "The canoe fisherman works his home waters."),
    (T_CLI, "Medium", "The temperature to which air must be cooled for it to become saturated and dew to begin forming is the",
     "dew point", "freezing point",
     "boiling point", "triple point", "A",
     "Cool the evening air below it and the grass grows wet."),
    (T_CLI, "Medium", "A thick cloud of tiny water droplets formed at ground level, cutting visibility below one kilometre, is",
     "fog", "mist",
     "dew", "smog", "A",
     "Mist is its thinner cousin; fog hides the road."),
    (T_CLI, "Hard", "An area of high atmospheric pressure, with light outward-blowing winds and calm, settled weather, is an",
     "anticyclone", "cyclone",
     "depression", "tornado", "A",
     "Its calm days bring clear skies and frosty nights."),
    (T_VEG, "Hard", "Trees of the Guinea savanna survive the yearly sweep of bush fires chiefly because of their",
     "thick, fire-resistant bark", "deep tap roots",
     "waxy, needle leaves", "broad, shiny leaves", "A",
     "The bark shields the living wood beneath."),
    (T_VEG, "Medium", "The massive savanna tree with a swollen trunk that hoards water against the long dry season is the",
     "baobab", "acacia",
     "shea", "iroko", "A",
     "One trunk may hold thousands of litres."),
    (T_VEG, "Medium", "The treeless grassland of Argentina, world-famous for cattle rearing and wheat, is the",
     "pampas", "prairie",
     "veld", "steppe", "A",
     "The gaucho rides its endless plains."),
    (T_VEG, "Hard", "The seasonally flooded grass plains of the Orinoco basin in Venezuela are known as the",
     "llanos", "pampas",
     "campos", "cerrado", "A",
     "Cattle roam them in the dry and flee them in the wet."),
    (T_VEG, "Medium", "The short-grass plains that stretch from Hungary across Asia to China are called the",
     "steppes", "prairies",
     "downs", "velds", "A",
     "The horsemen of history crossed them."),
    (T_POP, "Easy", "The movement of people out of a country to settle permanently in another is called",
     "emigration", "immigration",
     "migration", "circulation", "A",
     "One side departs, the other side receives."),
    (T_POP, "Medium", "The average number of children a woman in a population is expected to bear in her lifetime is the",
     "total fertility rate", "crude birth rate",
     "natural growth rate", "reproduction ratio", "A",
     "It counts births per woman, not per thousand people."),
]

build_batch(
    S,
    "batch_208_waec_geo8.json",
    "208",
    "WAEC Geography round 8 (R41 top-up): drumlins; eskers; river "
    "capture; cataracts; pot-holes; the braided channel; the "
    "bird's-foot delta; the beach; longshore drift; the tombolo; "
    "the natural arch; coasts of emergence; the atoll; the "
    "continental slope; artisanal fishing; dew point; fog; the "
    "anticyclone; fire-resistant savanna bark; the baobab; the "
    "pampas; the llanos; the steppes; emigration defined; the "
    "total fertility rate. Scanned against the whole Geography "
    "pool (WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
