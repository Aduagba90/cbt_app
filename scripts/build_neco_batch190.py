"""Batch 190 - WAEC Geography round 7 (WAEC top-up, R37).

Grows WAEC Geography from 226 toward ~255 with angles not yet in
the bank: attrition; corrasion; levees; the plunge pool; the
alluvial fan; seif dunes; deflation hollows; the U-shaped
glacial valley; fjords; the epicentre; anticlines; horsts; the
East African rift's tension origin; xerophytes; over- and
under-population; tributaries; the watershed; prairie and veld;
wave-cut platforms; spits; oases; Kano groundnuts; Enugu coal;
the Niger-Benue confluence at Lokoja; estuaries; isobars; the
wind vane. Scanned against the whole Geography pool (WAEC, NECO
and JAMB stems, 1,027 items).

    python3 scripts/build_neco_batch190.py -> content/batch_190_waec_geo7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_RIV = "River Processes and Landforms"
T_DES = "Desert and Wind Action"
T_GLA = "Glaciation"
T_INT = "Earth Movements"
T_VEG = "Vegetation"
T_POP = "Population"
T_COA = "Coastal Landforms"
T_NIG = "Geography of Nigeria"
T_MAP = "Map Reading and Weather"

PASSAGES = []
PQ = []

Q = [
    (T_RIV, "Medium", "The process by which the stones a river carries knock against one another and break into smaller pieces is called",
     "attrition", "corrasion",
     "solution", "traction", "A",
     "The load wears itself down on the journey."),
    (T_RIV, "Medium", "A river deepens its valley by the grinding of the sand and stones it drags along its bed. This process is",
     "corrasion", "attrition",
     "deposition", "saltation", "A",
     "The river's own load serves as its chisel."),
    (T_RIV, "Hard", "The raised banks of coarse material which a river builds along its lower course as floods repeatedly overflow are called",
     "levees", "deltas",
     "meander scars", "bluffs", "A",
     "Each flood leaves a fresh rim of coarse sand."),
    (T_RIV, "Medium", "The deep pool hollowed out at the foot of a waterfall by swirling water and its whirling load is a",
     "plunge pool", "gorge",
     "rapid", "kettle lake", "A",
     "Falling water drills its own basin."),
    (T_RIV, "Hard", "Where a swift mountain stream suddenly leaves its gorge and spreads onto flat ground, it drops its load in a fan-shaped heap called",
     "an alluvial fan", "a delta",
     "a flood plain", "an outwash plain", "A",
     "The sudden loss of speed dumps the debris."),
    (T_RIV, "Easy", "A stream that flows into and adds its water to a larger river is called a",
     "tributary", "distributary",
     "confluence", "watershed", "A",
     "Small streams feed the great trunk river."),
    (T_RIV, "Medium", "The highland ridge that separates the waters of one river system from those of another is a",
     "watershed", "water table",
     "divide of labour", "spur", "A",
     "Rain falling on either side runs to different rivers."),
    (T_RIV, "Medium", "The wide mouth of a river, where fresh water meets and mixes with the incoming sea, is called an",
     "estuary", "estuary delta",
     "inlet of the sea", "ria only", "A",
     "The tide pushes in as the river spreads out."),
    (T_DES, "Hard", "A long, knife-edged ridge of sand lying parallel to the prevailing wind across a desert is a",
     "seif dune", "barchan dune",
     "rock pedestal", "sand shadow", "A",
     "The wind combs the sand into long ridges."),
    (T_DES, "Hard", "The shallow hollows blown out of desert floors, where wind has carried away loose sand and dust, are called",
     "deflation hollows", "sinkholes",
     "salt pans only", "blowouts of rock", "A",
     "The wind alone scooped out the basin."),
    (T_DES, "Easy", "A green, watered spot in the desert, often ringed with date palms, is an",
     "oasis", "erg",
     "inselberg", "wadi", "A",
     "A green island set in the sand sea."),
    (T_GLA, "Medium", "A mountain valley whose floor has been widened from a V into a U shape owes its form chiefly to",
     "glacial ice", "river erosion",
     "wind abrasion", "wave attack", "A",
     "The glacier plucked and ground the sides wide."),
    (T_GLA, "Hard", "A long, narrow, steep-sided inlet of the sea formed when a deep glacial valley is flooded by the ocean is a",
     "fjord", "ria",
     "estuary", "creek", "A",
     "The sea crept into the ice-carved trough."),
    (T_INT, "Easy", "The point on the earth's surface lying directly above the place where an earthquake originates is the",
     "epicentre", "focus",
     "fault line", "seismic gap", "A",
     "The focus lies below; the epicentre sits on top."),
    (T_INT, "Medium", "Rocks buckled by earth movements into an upfold or arch form a structure called an",
     "anticline", "syncline",
     "horst", "monocline", "A",
     "The oldest rocks lie at the core of the arch."),
    (T_INT, "Hard", "A block of the earth's crust that has been pushed up between two parallel faults is a",
     "horst", "grabben",
     "anticline", "dome", "A",
     "The land between the cracks stands proud."),
    (T_INT, "Medium", "The great valley that runs through East Africa was formed mainly by",
     "tension pulling the crust apart", "compression squeezing the crust",
     "erosion by a mighty river", "lava burying an old plain", "A",
     "The crust stretched, cracked and dropped."),
    (T_COA, "Hard", "At low tide, the gently sloping rock shelf uncovered beneath a sea cliff is the",
     "wave-cut platform", "beach terrace",
     "spit", "stack", "A",
     "The tide polishes the stump of the cliff."),
    (T_COA, "Hard", "A long, narrow ridge of sand and shingle running out from the coast into the sea is a",
     "spit", "bar",
     "tombolo only", "mudflat", "A",
     "Longshore drift piles the sand into a finger."),
    (T_VEG, "Easy", "Desert plants such as the cactus, with long roots and thick waxy skins, are collectively called",
     "xerophytes", "hydrophytes",
     "halophytes", "epiphytes", "A",
     "They are built to hoard every drop of water."),
    (T_VEG, "Medium", "The temperate grassland of North America, famous for wheat and cattle ranching, is the",
     "prairie", "pampas",
     "veld", "steppe", "A",
     "From Canada to Texas roll the prairie seas."),
    (T_VEG, "Medium", "The open grassland of South Africa on which cattle and sheep are reared is the",
     "veld", "prairie",
     "pampas", "downs", "A",
     "The highveld feeds the flocks of the Cape."),
    (T_POP, "Easy", "A country whose people are too many for its available resources to support is said to have",
     "overpopulation", "underpopulation",
     "optimum population", "a dense market", "A",
     "Mouths have outrun the land's giving."),
    (T_POP, "Medium", "An area with rich land and other resources but too few people to develop them is described as",
     "underpopulated", "overpopulated",
     "congested", "saturated", "A",
     "The land waits for hands that have not come."),
    (T_NIG, "Medium", "Groundnuts were long the chief export crop of the northern belt centred on",
     "Kano", "Enugu",
     "Ibadan", "Port Harcourt", "A",
     "Groundnut pyramids once rose at Kano."),
    (T_NIG, "Medium", "The coal mined at Enugu in Nigeria was formed long ago from",
     "buried swamp vegetation", "molten rock underground",
     "coral reefs of the sea", "wind-blown desert sand", "A",
     "Ancient forests pressed into black stone."),
    (T_NIG, "Easy", "The town of Lokoja is famous as the place where the river Niger is joined by the",
     "Benue", "Ogun",
     "Kaduna", "Cross River", "A",
     "Two great rivers meet beneath the hills."),
    (T_MAP, "Medium", "Lines drawn on a weather map to join places having the same atmospheric pressure are called",
     "isobars", "isohyets",
     "isotherms", "isohels", "A",
     "Forecasters read the pressure rings for wind."),
    (T_MAP, "Easy", "The instrument whose arrow swings to show the direction from which the wind is blowing is the",
     "wind vane", "anemometer",
     "barometer", "hygrometer", "A",
     "The cock on the chapel points the breeze."),
]

build_batch(
    S,
    "batch_190_waec_geo7.json",
    "190",
    "WAEC Geography round 7 (R37 top-up): attrition; corrasion; "
    "levees; plunge pool; alluvial fan; tributary; watershed; "
    "estuary; seif dune; deflation hollow; oasis; U-shaped glacial "
    "valley; fjord; epicentre; anticline; horst; East African rift "
    "by tension; wave-cut platform; spit; xerophytes; prairie; "
    "veld; overpopulation; underpopulation; Kano groundnuts; Enugu "
    "coal; Lokoja confluence; isobars; wind vane. Scanned against "
    "the whole Geography pool (WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
