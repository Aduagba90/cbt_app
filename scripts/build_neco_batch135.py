"""Batch 135 - WAEC Geography round 5 (WAEC top-up, Round 25).

Lifts WAEC Geography from 158 toward ~196 with angles not yet in any
bank: scale arithmetic (2 km), contour V-shapes and spacing, latitude
origin, Greenwich time at 30 degrees E (2:00 pm); equinoxes, 21 June
solstice, cause of seasons; dyke, sill and batholith; middle-course
lateral erosion, waterfall gorges, deltas, radial and trellis
drainage; inselbergs, barchans, deflation hollows; harmattan,
south-west monsoon, temperature range arithmetic, swamp belt order;
B horizon accumulation, laterisation, contour ploughing, shelter
belts; density arithmetic (2,000), density pull factors, site vs
situation, the CBD; cocoa and groundnut belts, footloose industry,
Kilimanjaro, Lake Victoria, Victoria Falls. Scanned against WAEC
rounds 1-4, NECO Geography (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch135.py -> content/batch_135_waec_geo5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_MAP = "Map Work and Scale"
T_ROT = "Earth's Movement"
T_VUL = "Intrusive Vulcanicity"
T_RIV = "River Action"
T_ARID = "Arid Landforms"
T_CLIM = "Climate Further"
T_SOIL = "Soils Further"
T_POP = "Population and Settlement"
T_ECO = "Economic and Regional Geography"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- map work
    (T_MAP, "Medium", "On a map whose scale is 1:50,000, a distance of 4 cm represents",
     "2 km", "4 km", "1 km", "8 km", "A",
     "Four centimetres times fifty thousand.", "2"),
    (T_MAP, "Hard", "On a topographic map, contour lines forming a V that points towards higher ground indicate a",
     "river valley", "hill crest", "ridge line", "plateau edge", "A",
     "The V climbs to meet the source."),
    (T_MAP, "Medium", "Where contour lines on a topographic sheet crowd together, the ground is",
     "steep", "gentle", "level", "marshy", "A",
     "Heights crowd where land climbs."),
    (T_MAP, "Medium", "Latitude is measured in degrees from the",
     "equator", "prime meridian", "poles", "tropics", "A",
     "The zero line girdles the middle."),
    (T_MAP, "Hard", "A place lying 30 degrees east of Greenwich enjoys, at Greenwich noon, a local time of",
     "2:00 pm", "10:00 am", "1:00 pm", "6:00 pm", "A",
     "Every fifteen degrees adds an hour.", "2"),

    # ------------------------------------------------------------- earth's movement
    (T_ROT, "Medium", "Around 21 March and 23 September, day and night stand equal across the globe; such days are the",
     "equinoxes", "solstices", "aphelions", "perihelia", "A",
     "March and September share them."),
    (T_ROT, "Hard", "The sun stands directly over the Tropic of Cancer around",
     "21 June", "21 March", "23 September", "22 December", "A",
     "Northern summer starts that day.", "21"),
    (T_ROT, "Medium", "The chief cause of the seasons is the earth's",
     "tilted axis and revolution", "distance from the sun", "round shape alone", "daily rotation", "A",
     "The lean meets the year-long path."),

    # ------------------------------------------------------------- vulcanicity
    (T_VUL, "Hard", "A vertical sheet of magma cutting across rock layers is a",
     "dyke", "sill", "laccolith", "batholith", "A",
     "It stands like a wall across strata."),
    (T_VUL, "Medium", "Magma forced between rock layers to lie flat forms a",
     "sill", "dyke", "laccolith", "batholith", "A",
     "It lies like a table between beds."),
    (T_VUL, "Hard", "The largest intrusive magma mass, forming a dome deep in the crust, is a",
     "batholith", "dyke", "sill", "maar", "A",
     "Whole mountain roots are made of it."),

    # ------------------------------------------------------------- rivers
    (T_RIV, "Medium", "A river's middle course is marked by widening of the valley mainly through",
     "lateral erosion", "vertical erosion", "deposition of silt", "solution only", "A",
     "The river now swings side to side."),
    (T_RIV, "Hard", "As a waterfall retreats upstream over hard rock, it leaves behind a",
     "gorge", "delta", "meander", "levee", "A",
     "The retreat carves a deep trench."),
    (T_RIV, "Medium", "The fan of channels and silt at a river's mouth forms a",
     "delta", "gorge", "levee", "v-shaped valley", "A",
     "Silt builds new land at the gate."),
    (T_RIV, "Hard", "Streams radiating from a tall central peak form a",
     "radial pattern", "dendritic pattern", "trellis pattern", "centripetal pattern", "A",
     "All streams flee the summit."),
    (T_RIV, "Medium", "A trellis drainage pattern develops where rock resistance",
     "alternates hard and soft", "is uniform throughout", "is all hard rock", "is volcanic only", "A",
     "Side streams wait for soft bands."),

    # ------------------------------------------------------------- arid landforms
    (T_ARID, "Hard", "A lone steep-sided hill rising abruptly from an arid plain is an",
     "inselberg", "mesa", "butte", "pediment", "A",
     "An island of rock in a sand sea."),
    (T_ARID, "Medium", "The crescent dune of the open desert, its arms trailing with the wind, is the",
     "barchan", "seif dune", "star dune", "erg", "A",
     "Its curved arms point with the wind."),
    (T_ARID, "Hard", "Saucer-shaped hollows blown out of desert floors by wind removal are",
     "deflation hollows", "sink holes", "salt pans", "dry wadi beds", "A",
     "Wind lifts the fines and lowers land."),

    # ------------------------------------------------------------- climate
    (T_CLIM, "Medium", "The dry, dusty wind that blows over West Africa from December to February is the",
     "harmattan", "monsoon", "sirocco", "chinook", "A",
     "It dusts every roof in the dry season."),
    (T_CLIM, "Medium", "West Africa's rainy season is brought by the moist",
     "south-west monsoon", "north-east trade", "harmattan winds", "föhn wind", "A",
     "Atlantic moisture rides it inland."),
    (T_CLIM, "Hard", "If July averages 28 degrees C and January averages 22 degrees C, the annual range of temperature is",
     "6 degrees C", "50 degrees C", "25 degrees C", "10 degrees C", "A",
     "Highest mean less lowest mean.", "6"),
    (T_CLIM, "Medium", "Moving inland from Nigeria's coast, freshwater swamp follows the",
     "mangrove swamp", "derived savanna", "montane forest", "sudan savanna", "A",
     "Salt water yields to fresh inland."),

    # ------------------------------------------------------------- soils
    (T_SOIL, "Medium", "In a soil profile, the B horizon is the zone of",
     "accumulation", "eluviation", "topsoil litter", "parent rock", "A",
     "Washed-down minerals gather there."),
    (T_SOIL, "Hard", "The hardening of tropical soils into iron-rich crusts is called",
     "laterisation", "podzolisation", "salinisation", "gleization", "A",
     "Iron pans seal the tired soil."),
    (T_SOIL, "Medium", "Farmers who plough along the contour of a slope rather than straight down it aim to",
     "slow surface run-off", "speed up drainage", "raise soil pH", "dry the land faster", "A",
     "Furrows stair-step the slope."),
    (T_SOIL, "Medium", "Rows of trees planted as shelter belts chiefly guard against",
     "wind erosion", "river floods", "soil salinity", "crop diseases", "A",
     "Green walls brake the dust-laden wind."),

    # ------------------------------------------------------------- population and settlement
    (T_POP, "Medium", "A town of 40,000 people living on 20 square kilometres has a population density of",
     "2,000 per sq km", "800 per sq km", "20,000 per sq km", "200 per sq km", "A",
     "People divided by land area.", "2000"),
    (T_POP, "Hard", "Which factor ENCOURAGES high population density?",
     "fertile alluvial soil", "swampy marshland", "dense rainforest", "high mountain ridges", "A",
     "Rich soils feed crowded farms."),
    (T_POP, "Medium", "The actual ground on which a settlement stands is its",
     "site", "situation", "function", "sphere", "A",
     "It is the soil beneath the houses."),
    (T_POP, "Hard", "A village described as '10 km upstream of the river crossing' is being defined by its",
     "situation", "site", "status", "specialisation", "A",
     "Location relative to other places."),
    (T_POP, "Medium", "The core of a West African city holding banks, offices and the main market is the",
     "central business district", "the suburban estate", "an industrial park", "the commuter belt", "A",
     "Land value peaks at this core."),

    # ------------------------------------------------------------- economic and regional
    (T_ECO, "Medium", "Nigeria's cocoa belt lies chiefly in the",
     "south-west", "north-east", "north-west", "middle belt", "A",
     "Ibadan's forests nurse the pods."),
    (T_ECO, "Medium", "Groundnuts are traditionally the leading cash crop of Nigeria's",
     "far north", "coastal swamps", "eastern highlands", "oil-producing delta", "A",
     "Sudan savanna soils bore the pyramids."),
    (T_ECO, "Hard", "An industry that can set up almost anywhere without being tied to raw materials is called",
     "footloose industry", "heavy industry", "basic industry", "key industry", "A",
     "Neither mine nor port binds it."),
    (T_ECO, "Hard", "The highest mountain in Africa is",
     "Kilimanjaro", "Mount Kenya", "the Atlas range", "the Drakensberg", "A",
     "Its snows stand near the equator."),
    (T_ECO, "Medium", "The great lake that feeds the White Nile is",
     "Lake Victoria", "Lake Chad", "Lake Tanganyika", "Lake Nyasa", "A",
     "The Nile leaves it at Jinja."),
    (T_ECO, "Hard", "The Zambezi River plunges over the world's widest curtain of water at",
     "Victoria Falls", "Kainji Falls", "Augrabies Falls", "Livingstone Falls", "A",
     "Mosi-oa-Tunya, the smoke that thunders."),
]

build_batch(
    S,
    "batch_135_waec_geo5.json",
    "135",
    "WAEC Geography round 5 (Round 25 top-up): 1:50,000 scale giving "
    "2 km, contour Vs pointing uphill, close contours, latitude from "
    "the equator, 30 degrees East at 2:00 pm; equinoxes, 21 June "
    "solstice, tilted-axis seasons; dyke, sill, batholith; lateral "
    "erosion, waterfall gorge, delta, radial and trellis drainage; "
    "inselberg, barchan, deflation hollows; harmattan, south-west "
    "monsoon, 6-degree annual range, mangrove-to-freshwater order; B "
    "horizon accumulation, laterisation, contour ploughing, shelter "
    "belts; density 2,000 per sq km, alluvial pull, site vs situation, "
    "CBD; cocoa south-west, groundnut far north, footloose industry, "
    "Kilimanjaro, Lake Victoria, Victoria Falls. Scanned against WAEC "
    "rounds 1-4, NECO Geography (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
