"""Batch 149 - NECO Geography round 5 (NECO top-up, R28).

Grows NECO Geography from 173 toward ~209 with angles not yet in the
bank: rocks by mode of formation (granite, limestone, marble);
weathering (exfoliation, carbonation) and mass movement (soil creep,
landslide); earthquake focus vs epicentre and the seismograph;
caldera; ox-bow lakes, levees and river capture; equatorial and
savanna climates, Nigeria's vegetation belt sequence, sahel
characteristics; sheet and gully erosion; the water table and springs;
rural-urban migration and push factors; nucleated and linear
settlements; coal at Enugu, tin at Jos, iron at Itakpe, timber from
the rainforest, rail for bulky goods; Mediterranean orchards; Sudan
savanna grass. Scanned against NECO rounds 1-4, WAEC Geography (all
rounds) and the JAMB pool.

    python3 scripts/build_neco_batch149.py -> content/batch_149_neco_geo5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_ROCK = "Rocks"
T_WEA = "Weathering and Mass Movement"
T_QUA = "Earthquakes and Volcanoes"
T_RIV = "River and Groundwater"
T_CLI = "Climate and Vegetation"
T_SOI = "Soils and Erosion"
T_POP = "Population and Settlement"
T_ECO = "Economic Geography Further"
T_REG = "Regional Geography Further"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- rocks
    (T_ROCK, "Medium", "Granite, formed from cooling magma deep underground, is an example of",
     "an igneous rock", "a sedimentary rock", "a metamorphic rock", "an organic rock", "A",
     "Fire births it below the surface."),
    (T_ROCK, "Medium", "Limestone, built from compressed shells and sediments on old sea floors, is",
     "a sedimentary rock", "an igneous rock", "a metamorphic rock", "a volcanic glass", "A",
     "Layers of ages pressed it together."),
    (T_ROCK, "Hard", "Marble, formed when limestone is changed by heat and pressure, belongs to",
     "metamorphic rocks", "igneous rocks", "sedimentary rocks", "meteoric rocks", "A",
     "Old stone recast by the earth's ovens."),
    (T_ROCK, "Hard", "The family name for rocks changed by heat, pressure or chemical action is",
     "metamorphic", "sedimentary", "igneous", "alluvial", "A",
     "Their very name means transformed."),

    # ------------------------------------------------------------- weathering & mass movement
    (T_WEA, "Hard", "Daily heating and nightly cooling peel a granite dome in onion-like sheets through",
     "exfoliation", "carbonation", "hydration", "oxidation", "A",
     "The sun's daily knead flakes the rock."),
    (T_WEA, "Hard", "Weak carbonic acid in rain gnaws at limestone outcrops, hollowing them into pits and pavements. This weathering process is",
     "carbonation", "exfoliation", "attrition", "corrasion", "A",
     "Weak acid carves the karst."),
    (T_WEA, "Medium", "The slow, almost unseen downhill crawl of soil particles is",
     "soil creep", "landslide", "rockfall", "earthquake", "A",
     "Fences and poles lean with time."),
    (T_WEA, "Medium", "A sudden rapid slide of earth and rock down a steep slope after heavy rain is a",
     "landslide", "soil creep", "spring tide", "dust storm", "A",
     "Whole hillsides shift at once."),

    # ------------------------------------------------------------- earthquakes & volcanoes
    (T_QUA, "Hard", "The point deep underground where an earthquake originates is the",
     "focus", "epicentre", "crater", "rift", "A",
     "The very first shock is born there."),
    (T_QUA, "Medium", "Reporting an earthquake, newscasters name the surface point where shaking was fiercest, lying straight above the buried origin. That point is the",
     "epicentre", "focus", "seismograph station", "anticentre", "A",
     "Shaking is strongest overhead."),
    (T_QUA, "Medium", "The instrument that detects and records earthquake waves is the",
     "seismograph", "barograph", "hygrometer", "theodolite", "A",
     "Its needle writes the trembling."),
    (T_QUA, "Hard", "After a violent eruption empties a volcano's magma chamber, the unsupported summit caves in, leaving a vast depression called a",
     "caldera", "cinder cone", "lava plain", "geyser", "A",
     "The mountain falls into its emptied heart."),

    # ------------------------------------------------------------- rivers & groundwater
    (T_RIV, "Hard", "An ox-bow lake forms when a river's meander neck is cut through and the loop is",
     "abandoned by the main channel", "deepened into a gorge", "raised into a levee", "turned into a delta", "A",
     "The old bend becomes a stranded crescent."),
    (T_RIV, "Medium", "The raised banks along a mature river, built from repeated flood deposits, are",
     "levees", "deltas", "bergs", "eskers", "A",
     "Each flood adds another layer."),
    (T_RIV, "Hard", "When one stream cuts headward and steals the headwaters of a weaker neighbour, the event is",
     "river capture", "river rejuvenation", "aggradation", "flocculation", "A",
     "The robbed stream is left beheaded."),
    (T_RIV, "Medium", "The level below which the ground is saturated with water is the",
     "water table", "spring line", "aquiclude", "artesian well", "A",
     "Wells must dig down to reach it."),
    (T_RIV, "Medium", "Where a hillslope cuts across the water table, groundwater seeps out on its own as a",
     "spring", "geyser", "oasis", "delta", "A",
     "The hillside weeps it out."),

    # ------------------------------------------------------------- climate & vegetation
    (T_CLI, "Hard", "At stations like Calabar, no month passes without generous rain. This is the signature of the",
     "equatorial climate", "mediterranean climate", "sahel climate", "tundra climate", "A",
     "Every month brings its share."),
    (T_CLI, "Medium", "Nigeria's vegetation belts, listed from the coast northwards, begin with",
     "mangrove swamp", "sahel", "guinea savanna", "montane forest", "A",
     "Salt-tolerant trees stand first."),
    (T_CLI, "Hard", "The sahel belt at Nigeria's northern edge is characterised by",
     "short grass and thorny scrub", "tall dense rainforest", "swamp palms", "evergreen bamboo", "A",
     "Rain is brief and grass stays low."),
    (T_CLI, "Medium", "Between the rainforest and the sudan savanna lies the belt known for mixed trees and tall grasses, the",
     "guinea savanna", "mangrove swamp", "sahel", "montane zone", "A",
     "Nigeria's widest belt wears this name."),
    (T_CLI, "Medium", "Trees of the rainforest shed their leaves",
     "a few at a time all year", "entirely in the dry season", "only after fires", "never in their lives", "A",
     "The canopy never stands bare."),

    # ------------------------------------------------------------- soils & erosion
    (T_SOI, "Medium", "The washing away of a thin surface film of soil over a wide area is",
     "sheet erosion", "gully erosion", "wind erosion", "beach erosion", "A",
     "The land is skimmed like milk."),
    (T_SOI, "Hard", "Deep channels cut into farmland by running water after heavy rains are the work of",
     "gully erosion", "sheet erosion", "glaciation", "weathering", "A",
     "The Nanka hills show its scars."),
    (T_SOI, "Medium", "Loss of soil cover in northern Nigeria is hastened most by",
     "overgrazing and tree felling", "terracing and mulching", "cover cropping", "strip farming", "A",
     "Too many goats, too few trees."),

    # ------------------------------------------------------------- population & settlement
    (T_POP, "Hard", "The movement of youths from Ogwashi-Uku to Onitsha in search of factory jobs is",
     "rural-urban migration", "international migration", "seasonal migration", "forced migration", "A",
     "Villages empty into the towns."),
    (T_POP, "Medium", "A factor that drives people away from their home region is called a",
     "push factor", "pull factor", "pivot factor", "constant factor", "A",
     "Poverty and hunger push hardest."),
    (T_POP, "Medium", "Houses clustered tightly around a market square or a water point form a",
     "nucleated settlement", "dispersed settlement", "linear settlement", "isolated farmstead", "A",
     "Homes huddle for company and safety."),
    (T_POP, "Medium", "Homesteads strung out along a road or river valley mark a",
     "linear settlement", "nucleated settlement", "dispersed pattern", "city block", "A",
     "The line of travel strings them."),

    # ------------------------------------------------------------- economic
    (T_ECO, "Medium", "Nigeria's coal, mined since colonial days around Enugu, comes chiefly from the",
     "Enugu coalfields", "Jos Plateau", "Itakpe ridge", "Niger Delta swamps", "A",
     "The railway was built to carry it."),
    (T_ECO, "Medium", "Tin and columbite have been mined for decades on the",
     "Jos Plateau", "Mambilla hills", "Idanre hills", "Obudu mountains", "A",
     "Old granite hills hold the ore."),
    (T_ECO, "Hard", "The iron ore that feeds the Ajaokuta steel complex is mined at",
     "Itakpe", "Enugu", "Jos", "Okaba", "A",
     "The ridge above the Niger holds it."),
    (T_ECO, "Medium", "Hardwood like iroko and mahogany is harvested from Nigeria's",
     "rainforest zone", "sahel zone", "mangrove creeks", "montane grasslands", "A",
     "The high forest shelters the giants."),
    (T_ECO, "Hard", "For hauling coal and cement over long distances at low cost, the best mode of transport is",
     "rail", "air", "motor cycle", "pipeline", "A",
     "Steel rails love heavy loads."),

    # ------------------------------------------------------------- regional
    (T_REG, "Hard", "Viticulture and orchard farming of grapes, olives and citrus typify the",
     "Mediterranean climate", "equatorial climate", "tundra climate", "monsoon climate", "A",
     "Dry summers ripen the vine."),
    (T_REG, "Medium", "The Sudan savanna, unlike the sahel, carries",
     "taller grasses and acacias", "only bare sand", "mangrove thickets", "permanent snow", "A",
     "The wet months last longer there."),
]

build_batch(
    S,
    "batch_149_neco_geo5.json",
    "149",
    "NECO Geography round 5 (R28 top-up): granite igneous, limestone "
    "sedimentary, marble metamorphic, metamorphism defined; exfoliation "
    "onion flakes, carbonation on limestone, soil creep, landslide; "
    "focus vs epicentre, seismograph, caldera collapse; ox-bow lake "
    "from a cut-off meander, levees, river capture, water table, "
    "springs; equatorial all-year rain, mangrove-first belt order, "
    "sahel scrub, guinea savanna, evergreen canopy; sheet vs gully "
    "erosion, overgrazing in the north; rural-urban migration, push "
    "factors, nucleated and linear settlements; Enugu coal, Jos tin, "
    "Itakpe iron ore, rainforest hardwoods, rail for bulky loads; "
    "Mediterranean orchards, Sudan savanna grasses. Scanned against "
    "NECO rounds 1-4, WAEC Geography (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
