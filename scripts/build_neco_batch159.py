"""Batch 159 - WAEC Geography round 6 (WAEC top-up, R29).

Grows WAEC Geography from 196 toward ~232 with angles not yet in the
bank: the equator as a great circle, meridians converging, the
International Date Line, grid references, contour intervals, map
legends; crust, mantle and core; fossils in sedimentary rock;
freeze-thaw weathering, attrition, mushroom rocks; lava plateaus;
convectional and orographic rainfall; desert diurnal range,
xerophytes, pneumatophores; the soil catena, grass waterways; brain
drain, dispersed settlement, urban slums; oil palm, Niger Delta oil,
Kainji, cement's limestone, the Lokoja confluence; Lake Chad's
shrinkage, desertification's spread. Scanned against WAEC rounds
1-5, NECO Geography (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch159.py -> content/batch_159_waec_geo6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_MAP = "Maps and the Globe"
T_EAR = "Earth's Structure and Rocks"
T_PRO = "Weathering and River Work"
T_VUL = "Vulcanicity Further"
T_CLI = "Rainfall Types Further"
T_VEG = "Vegetation Adaptations"
T_SOI = "Soils and Conservation Further"
T_POP = "Population Further"
T_ECO = "Nigeria's Economic Geography"
T_REG = "Regional Change"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- maps & globe
    (T_MAP, "Hard", "The equator is called a great circle because it",
     "bisects the earth equally", "passes through Nigeria", "is the longest river known", "follows the sunset path", "A",
     "Its centre is the earth's own centre."),
    (T_MAP, "Medium", "Lines of longitude are drawn from the North Pole to the South Pole, where they all",
     "meet at a point", "run parallel forever", "cross the equator twice", "turn eastward", "A",
     "The meridians converge like umbrella ribs."),
    (T_MAP, "Hard", "A traveller crossing the International Date Line westward must",
     "add a day to the calendar", "lose a day entirely", "reset only the clock", "change currency", "A",
     "The date jumps at that line."),
    (T_MAP, "Medium", "On a topographic map sheet, the easting and northing quoted together locate a point by",
     "grid reference", "true bearing", "magnetic declination", "relief shading", "A",
     "Two numbers, one meeting point."),
    (T_MAP, "Medium", "The vertical distance between one contour line and the next is the",
     "contour interval", "map scale", "gradient only", "vertical exaggeration", "A",
     "It may be twenty metres a line."),
    (T_MAP, "Medium", "The symbols and signs explaining a map's features are found in its",
     "legend", "title block only", "margin note only", "publisher's page", "A",
     "The key unlocks the sheet."),

    # ------------------------------------------------------------- earth & rocks
    (T_EAR, "Medium", "The innermost and densest shell of the earth is the",
     "core", "crust", "mantle", " Moho layer", "A",
     "Iron and nickel crowd there."),
    (T_EAR, "Medium", "Between the thin crust and the heavy core lies the thick layer called the",
     "mantle", "sima floor", "lithosphere only", "asthenosphere only", "A",
     "Most of the earth's bulk is it."),
    (T_EAR, "Hard", "Imprints of ancient shells found in limestone tell us the rock is",
     "sedimentary", "igneous", "metamorphic", "meteoric", "A",
     "Only laid-down layers entomb fossils."),

    # ------------------------------------------------------------- weathering & rivers
    (T_PRO, "Hard", "Water entering cracks, freezing and splitting rock apart works by",
     "freeze-thaw action", "carbonation", "hydrolysis", "exfoliation", "A",
     "Ice wedges the joints open."),
    (T_PRO, "Hard", "Pebbles carried by a river grind each other smaller and rounder through",
     "attrition", "abrasion", "solution", "saltation", "A",
     "Stone wears stone in the churn."),
    (T_PRO, "Hard", "A rock pillar whose top is wider than its base, carved by wind-blown sand in the desert, is the",
     "mushroom rock", "inselberg dome", "roche moutonnee", "crag and tail", "A",
     "The sandblaster carves the cap."),

    # ------------------------------------------------------------- vulcanicity
    (T_VUL, "Hard", "Vast sheets of fluid lava pouring from fissures rather than a central vent build a",
     "lava plateau", "composite cone", "caldera ring", "cinder cone", "A",
     "The Jos and Deccan plains rose so."),

    # ------------------------------------------------------------- rainfall types
    (T_CLI, "Hard", "The afternoon thunder showers common over Jos highlands in the wet season arise from",
     "convectional rainfall", "orographic rainfall", "frontal rainfall", "cyclonic rain only", "A",
     "Hot ground lifts moist air till it bursts."),
    (T_CLI, "Medium", "Moist winds forced up the windward side of the Obudu highlands yield rain there and leave the far side dry. The leeward dry side is called the",
     "rain shadow", "dew point", "sun belt", "dry adiabat", "A",
     "The mountain drinks the rain first."),

    # ------------------------------------------------------------- vegetation adaptations
    (T_VEG, "Hard", "Desert plants with deep roots, waxy skins and spines instead of leaves are adapted through",
     "xerophytic features", "hydrophytic features", "halophytic features", "mesophytic features", "A",
     "Every part of it hoards water."),
    (T_VEG, "Medium", "The breathing roots that poke out of mangrove mud to draw air are called",
     "pneumatophores", "prop roots", "buttress roots", "tap roots", "A",
     "The mud suffocates without them."),

    # ------------------------------------------------------------- soils & conservation
    (T_SOI, "Hard", "The sequence of soils arranged from a hilltop to the valley bottom along one slope is a",
     "catena", "profile", "polygon", "pedon", "A",
     "The slope tells the soil story."),
    (T_SOI, "Medium", "Grass planted in the natural depressions where run-off gathers, to slow the water and trap soil, forms",
     "grass waterways", "contour banks", "gabion walls", "terrace risers", "A",
     "Green channels guide the flood."),

    # ------------------------------------------------------------- population
    (T_POP, "Hard", "The departure of Nigeria's doctors and engineers to Europe and America is a classic case of",
     "brain drain", "brain gain", "circular migration", "pastoral drift", "A",
     "The nation trains, others harvest."),
    (T_POP, "Medium", "Farmsteads scattered widely across the countryside, each amid its own fields, form a",
     "dispersed settlement", "nucleated settlement", "linear settlement", "suburban estate", "A",
     "Neighbours live a shout apart."),
    (T_POP, "Medium", "Overcrowded, unserviced housing on city fringes produces",
     "slums", "estates", "suburbs", "new towns", "A",
     "The city grows faster than its pipes."),

    # ------------------------------------------------------------- economic geography
    (T_ECO, "Medium", "Oil palm groves thrive in Nigeria chiefly in the",
     "Niger Delta lowlands", "Sahel margins only", "Jos plateau highlands", "Sudan savanna belts", "A",
     "Rain and swamps favour the palm."),
    (T_ECO, "Hard", "Nigeria's crude oil occurs in thick sedimentary rocks beneath the",
     "Niger Delta basin", "Jos granite", "Chad sand sheets only", "Mambilla plateau", "A",
     "Ancient deltas buried the oil."),
    (T_ECO, "Medium", "The Kainji dam, generating hydroelectric power, stands on the river",
     "Niger", "Benue", "Ogun", "Kaduna", "A",
     "Its lake stretched past Kainji town."),
    (T_ECO, "Hard", "Cement factories like Obajana locate near deposits of",
     "limestone", "tin ore", "coal seams", "laterite", "A",
     "The rock is the recipe's base."),
    (T_ECO, "Medium", "Nigeria's famous confluence town, where the Niger meets the Benue, is",
     "Lokoja", "Onitsha", "Yola", "Baro", "A",
     "Two rivers wed at its doorstep."),

    # ------------------------------------------------------------- regional change
    (T_REG, "Hard", "Lake Chad has shrunk drastically since the 1970s chiefly because of",
     "drought and over-abstraction", "one great earthquake", "volcanic activity below", "sand dam construction", "A",
     "Less rain and more irrigation drains it."),
    (T_REG, "Medium", "Year after year, sand advances onto the farms of Nigeria's far north. The process's name is",
     "desertification", "deforestation", "desert pavement", "salinisation", "A",
     "The desert marches on the farms."),
    (T_REG, "Medium", "Winds blowing from the sea towards the coast in the wet season are ultimately caused by",
     "uneven heating of land and sea", "the earth's magnetism alone", "very deep ocean trenches", "mountain barrier heights", "A",
     "Land and sea warm unevenly."),
]

build_batch(
    S,
    "batch_159_waec_geo6.json",
    "159",
    "WAEC Geography round 6 (R29 top-up): equator great circle, "
    "meridian convergence, Date Line day arithmetic, grid reference, "
    "contour interval, legend; core, mantle, fossils in sedimentary; "
    "freeze-thaw, attrition, mushroom rock; lava plateau; "
    "convectional rain on Jos highlands, rain shadow; xerophytes, "
    "pneumatophores; catena, grass waterways; brain drain, dispersed "
    "settlement, slums; oil palm east, Niger Delta oil, Kainji on the "
    "Niger, limestone for cement, Lokoja confluence; Lake Chad's "
    "shrinkage, desertification, monsoon winds' cause. Scanned against "
    "WAEC rounds 1-5, NECO Geography (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
