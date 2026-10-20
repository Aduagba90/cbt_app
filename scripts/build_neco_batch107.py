"""Batch 107 - WAEC Geography round 3 (WAEC top-up, Round 21).

Lifts WAEC Geography from 105 toward ~150 with fresh angles: the grid
and local time, earth's structure, rocks and weathering, rivers and
drainage, coastal and ocean features, climate elements, soils,
population and settlement, resources and industries, and environmental
hazards. Scanned against WAEC rounds 1-2, NECO Geography and the JAMB
pool.

    python3 scripts/build_neco_batch107.py -> content/batch_107_waec_geo3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_PHYS = "Physical Geography: Earth and Rocks"
T_RIV = "Rivers and Drainage"
T_COAST = "Coasts and Oceans"
T_CLIM = "Climate and Vegetation"
T_SOIL = "Soils"
T_POP = "Population and Settlement"
T_RES = "Resources and Industries"
T_HAZ = "Environmental Hazards"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- earth and rocks
    (T_PHYS, "Medium", "The line of latitude at zero degrees is the",
     "equator", "Tropic of Cancer", "prime meridian", "International Date Line", "A",
     "It splits the globe into two halves."),
    (T_PHYS, "Medium", "The prime meridian passes through",
     "Greenwich", "the Equator town", "Paris", "Rome", "A",
     "London's observatory marks it."),
    (T_PHYS, "Hard", "Places 15 degrees of longitude apart differ in local time by",
     "one hour", "two hours", "30 minutes", "four hours", "A",
     "The globe turns 15 degrees each hour."),
    (T_PHYS, "Medium", "Human beings and all surface life stand on which earth layer?",
     "crust", "mantle", "core", "asthenosphere", "A",
     "Its thin shell carries all life."),
    (T_PHYS, "Hard", "The earth's innermost zone, mostly iron and nickel, is the",
     "core", "mantle", "crust", "moho", "A",
     "It sits at the very centre."),
    (T_PHYS, "Medium", "Granite and basalt are examples of",
     "igneous rocks", "sedimentary rocks", "metamorphic rocks", "organic rocks", "A",
     "They cooled from molten magma."),
    (T_PHYS, "Medium", "Sandstone and limestone belong to the",
     "sedimentary rocks", "igneous rocks", "metamorphic rocks", "volcanic glass", "A",
     "They settled down in layers."),
    (T_PHYS, "Hard", "Limestone transformed by heat and pressure becomes the rock called",
     "metamorphic", "igneous", "sedimentary", "meteoric", "A",
     "Change of form gives the name."),
    (T_PHYS, "Medium", "The breakdown of rocks in place is",
     "weathering", "erosion", "deposition", "transportation", "A",
     "The rock rots where it stands."),
    (T_PHYS, "Hard", "Rocks shattered by alternate freezing and thawing of water in cracks undergo",
     "frost weathering", "carbonation", "exfoliation", "hydration", "A",
     "Ice wedges force cracks wide."),

    # ------------------------------------------------------------- rivers
    (T_RIV, "Medium", "The journey of a river is divided into upper, middle and",
     "lower courses", "coastal plains only", "deltas", "tributaries", "A",
     "Three stages make the journey."),
    (T_RIV, "Medium", "The chief work of a river in its upper course is",
     "vertical erosion", "deposition", "lateral erosion", "braiding", "A",
     "It cuts steeply downward."),
    (T_RIV, "Hard", "A waterfall forming where soft rock overlies hard rock recedes upstream leaving a",
     "gorge", "delta", "flood plain", "meander scar", "A",
     "The retreat carves a steep valley."),
    (T_RIV, "Medium", "Wide bends developed by a mature river on flat land are",
     "meanders", "rapids", "geysers", "braids", "A",
     "The river swings side to side."),
    (T_RIV, "Medium", "The finger-like channels spreading where a river meets the sea form a",
     "delta", "estuary only", "stack", "wave-cut platform", "A",
     "The Nile and Niger both show one."),
    (T_RIV, "Hard", "A dendritic drainage pattern resembles the branches of a",
     "tree", "ladder", "star", "grid", "A",
     "Tributaries twig off randomly."),
    (T_RIV, "Hard", "Streams flowing outwards from a central peak produce a drainage pattern that is",
     "radial", "dendritic", "trellis", "centripetal", "A",
     "Flow radiates like wheel spokes."),

    # ------------------------------------------------------------- coasts and oceans
    (T_COAST, "Medium", "Waves erode the coast mainly by hydraulic action, corrosion and",
     "attrition", "accretion", "adsorption", "assimilation", "A",
     "Stones grind each other down."),
    (T_COAST, "Hard", "A steep rock face cut back by wave attack is a",
     "wave-cut cliff", "spit", "tombolo", "bar", "A",
     "Undercutting leaves it standing."),
    (T_COAST, "Hard", "The sand ridge tying an offshore isle to the shore is a",
     "tombolo", "spit", "stack", "bay-bar", "A",
     "It ties the isle to the shore."),
    (T_COAST, "Medium", "The rise and fall of sea level twice daily is caused chiefly by",
     "the moon's pull", "ocean currents", "coastal winds", "earthquakes", "A",
     "Gravity does the lifting."),
    (T_COAST, "Medium", "Warm ocean currents flowing along coasts tend to",
     "warm the coast and bring rain", "freeze the coast dry", "lower all humidity", "stop all winds", "A",
     "Warm water warms and moistens air."),
    (T_COAST, "Hard", "The cold current that flows southward along the west coast of Africa is the",
     "Benguela Current", "Gulf Stream", "Kuroshio", "Agulhas", "A",
     "Cold waters chill the Namib."),

    # ------------------------------------------------------------- climate
    (T_CLIM, "Medium", "The two elements of weather most commonly measured daily are",
     "temperature and rainfall", "soil and rock", "population and births", "imports and exports", "A",
     "Every weather report leads with them."),
    (T_CLIM, "Medium", "The instrument that measures atmospheric pressure is the",
     "barometer", "thermometer", "anemometer", "hygrometer", "A",
     "Rising mercury fair, falling foul."),
    (T_CLIM, "Medium", "Wind speed is recorded with an",
     "anemometer", "barograph", "rain gauge", "wind vane", "A",
     "Cups spinning measure the gusts."),
    (T_CLIM, "Hard", "Subtracting a day's lowest temperature from its highest yields the",
     "daily range", "annual range", "mean temperature", "diurnal mean", "A",
     "The gap between high and low is the range."),
    (T_CLIM, "Medium", "The equatorial climate is marked by",
     "constant heavy rain and heat", "one dry season only", "winter snowfall", "cool nights always", "A",
     "No real dry month ever exists."),
    (T_CLIM, "Hard", "Sudan savanna vegetation is dominated by",
     "tall grass and scattered trees", "dense evergreen forest", "mangrove swamp", "alpine meadow", "A",
     "Grassland dotted with trees."),
    (T_CLIM, "Medium", "The Sahel lies between the savanna and the",
     "Sahara desert", "rainforest", "coastal lagoon", "mountain parks", "A",
     "Dry grass fringes the great sand."),

    # ------------------------------------------------------------- soils
    (T_SOIL, "Medium", "The individual soil layers seen in a profile are called",
     "horizons", "plates", "folds", "gullies", "A",
     "Each layer has its own look."),
    (T_SOIL, "Hard", "The layer of a soil profile where leached materials accumulate is the",
     "B horizon", "O horizon", "A horizon", "parent rock", "A",
     "It gathers what the top loses."),
    (T_SOIL, "Medium", "The proportions of sand, silt and clay describe a soil's",
     "texture", "structure", "colour", "acidity only", "A",
     "Feel a handful to judge it."),
    (T_SOIL, "Medium", "Soil acidity and alkalinity are measured on the",
     "pH scale", "Beaufort scale", "Richter scale", "Mohs scale", "A",
     "Seven marks neutral on it."),
    (T_SOIL, "Hard", "The red tropical soil rich in iron and aluminium is",
     "laterite", "chernozem", "podzol", "alluvium", "A",
     "It hardens on exposure to sun."),

    # ------------------------------------------------------------- population
    (T_POP, "Medium", "An official count of a country's people is a",
     "census", "survey", "sample", "quota", "A",
     "Every household is counted."),
    (T_POP, "Medium", "The number of people per square kilometre is",
     "population density", "population growth", "birth rate", "vital rate", "A",
     "Divide people by the land area."),
    (T_POP, "Hard", "A population with a high proportion of children shows a",
     "broad-based pyramid", "narrow-based pyramid", "rectangular pyramid", "inverted pyramid", "A",
     "The base bulges with the young."),
    (T_POP, "Medium", "Moving from one place to another to live is",
     "migration", "commuting", "tourism", "nomadic grazing only", "A",
     "It changes both ends of the move."),
    (T_POP, "Medium", "Villages clustered around a well or market show a settlement pattern that is",
     "nucleated", "dispersed", "linear", "isolated", "A",
     "The homes huddle together."),
    (T_POP, "Hard", "Houses strung out along a road or river follow a settlement pattern that is",
     "linear", "nucleated", "circular", "square", "A",
     "The line of travel decides."),
    (T_POP, "Medium", "The rapid growth of cities is called",
     "urbanisation", "ruralisation", "desertification", "globalisation", "A",
     "People pour into the towns."),

    # ------------------------------------------------------------- resources
    (T_RES, "Medium", "Coal mined in Nigeria comes chiefly from",
     "Enugu", "Jos", "Kaduna", "Calabar", "A",
     "The coal city sits on the seam."),
    (T_RES, "Medium", "Tin and columbite are mined around",
     "Jos Plateau", "Niger Delta", "Sokoto plains", "Obudu hills", "A",
     "The plateau's old granites carry them."),
    (T_RES, "Hard", "The oil wells of Nigeria cluster thickly in the",
     "Niger Delta region", "Chad Basin only", "Sahel belt", "Mambilla plateau", "A",
     "Wells crowd the delta swamps."),
    (T_RES, "Medium", "Iron ore deposits at Itakpe are located in",
     "Kogi State", "Anambra State", "Ogun State", "Bauchi State", "A",
     "The steel plant feeds on them."),
    (T_RES, "Medium", "Industries that process farm produce near the source are drawn by",
     "raw materials", "sea breeze", "tourist sites", "cheap power only", "A",
     "The farm gate pulls them close."),
    (T_RES, "Hard", "The Kainji Dam is primarily a source of",
     "hydroelectric power", "natural gas", "wind power", "nuclear energy", "A",
     "Its turbines light the grid."),

    # ------------------------------------------------------------- hazards
    (T_HAZ, "Medium", "The sudden overflow of a river onto adjoining land is a",
     "flood", "drought", "harmattan", "landslide", "A",
     "Channels burst their banks."),
    (T_HAZ, "Hard", "A prolonged period of far below-average rainfall is a",
     "drought", "flood", "hailstorm", "monsoon", "A",
     "The land dries and crops fail."),
    (T_HAZ, "Medium", "The southward spread of desert conditions into savanna land is",
     "desertification", "afforestation", "irrigation", "reclamation", "A",
     "The sands creep towards the coast."),
    (T_HAZ, "Medium", "Planting trees to check erosion and restore land is",
     "afforestation", "deforestation", "mining", "damming", "A",
     "New forests hold the soil."),
    (T_HAZ, "Hard", "Gully erosion, common in the south-east, is best checked by",
     "planting cover crops and building checks", "burning the slopes", "straight-ploughing downhill", "clearing all grass", "A",
     "Vegetation and barriers slow runoff."),
]

build_batch(
    S,
    "batch_107_waec_geo3.json",
    "107",
    "WAEC Geography round 3 (Round 21 top-up): equator and Greenwich, "
    "15-degrees-per-hour local time, earth's layers, igneous, "
    "sedimentary and metamorphic rocks, frost weathering, river courses "
    "and meanders, waterfalls and gorges, deltas, dendritic and radial "
    "drainage, wave erosion, cliffs, tombolos, tides, warm and cold "
    "currents (Benguela), weather instruments (barometer, anemometer), "
    "daily temperature range, equatorial climate, Sudan savanna, Sahel, "
    "soil horizons, texture, pH and laterite, census, density, "
    "population pyramids, migration, nucleated and linear settlement, "
    "urbanisation, Enugu coal, Jos tin, Niger Delta oil, Itakpe iron "
    "ore, industrial location, Kainji Dam, floods, drought, "
    "desertification, afforestation and gully-erosion control. Scanned "
    "against WAEC rounds 1-2, NECO Geography and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
