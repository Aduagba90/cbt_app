"""Batch 213 - NECO Geography round 8 (NECO top-up, R42).

Grows NECO Geography from 244 toward ~266 with angles not yet in
the bank: carbonation; landslides; arêtes; hanging valleys;
erratics; pyramidal peaks; ribbon lakes; peneplains; monadnocks;
loess; wadis; brain drain; market gardening; dry-point and
situation of settlements; primate cities; subsistence farming;
aspect; depressions as low pressure; radial drainage; daily mean
temperature; the wind rose. Scanned against the whole Geography
pool (WAEC, NECO and JAMB stems, 1,081 items).

    python3 scripts/build_neco_batch213.py -> content/batch_213_neco_geo8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Geography"

T_GLA = "Glaciation"
T_PRO = "Landforms and Denudation"
T_DES = "Desert and Wind Action"
T_MAP = "Map Reading and Weather"
T_CLI = "Weather and Climate"
T_SET = "Settlements"
T_POP = "Population"
T_AGR = "Agriculture"

PASSAGES = []
PQ = []

Q = [
    (T_PRO, "Medium", "Rain water absorbs carbon(IV) oxide from the air and dissolves limestone. This process of chemical weathering is called",
     "carbonation", "exfoliation",
     "frost shattering", "oxidation", "A",
     "It carves out the karst scenery of limestone regions."),
    (T_PRO, "Hard", "After a week of torrential rain, the whole hillside above a village gave way at once and buried the farms below. This rapid movement is a",
     "landslide", "soil creep",
     "earthflow of dust", "sheet wash", "A",
     "The hillside surrenders in a single moment."),
    (T_GLA, "Hard", "The knife-edged ridge separating two adjacent glacial troughs is an",
     "arête", "esker",
     "arete bench", "arête spur", "A",
     "The ice planed both valleys at once."),
    (T_GLA, "Hard", "A tributary glacial valley whose floor stands high above the main trough after the ice melted is a",
     "hanging valley", "ribbon lake",
     "cirque terrace", "truncated spur", "A",
     "Its stream now leaps as a waterfall."),
    (T_GLA, "Hard", "The large boulder of rock carried far from its home by glacier ice and dumped on stranger ground is an",
     "erratic", "drumlin",
     "esker heap", "moraine ridge", "A",
     "Granite rests on sandstone far from any source."),
    (T_GLA, "Hard", "The sharp, pointed mountain summit carved where several cirques cut back into one another is a",
     "pyramidal peak", "crag and tail",
     "roche moutonnée", "horn ridge only", "A",
     "Snowdon and the Matterhorn wear the shape."),
    (T_GLA, "Hard", "A long, narrow lake occupying a glacial trough deepened below sea level after the ice retreated is a",
     "ribbon lake", "tarn only",
     "kettle hole", "ox-bow lake", "A",
     "Windermere and Loch Ness lie in such troughs."),
    (T_PRO, "Medium", "The almost level surface produced when a landmass is worn down by erosion over immense ages is a",
     "peneplain", "pediment only",
     "coastal shelf", "lava plateau", "A",
     "The land's old age, flat and low."),
    (T_PRO, "Hard", "The lone resistant hill of rock left standing above a worn-down plain around it is a",
     "monadnock", "drumlin",
     "cuesta", "mesa only", "A",
     "The hard core outlasts its softer surroundings."),
    (T_DES, "Hard", "The fine, yellowish, wind-deposited silt that mantles the plains of north-west China is",
     "loess", "laterite",
     "alluvium", "boulder clay", "A",
     "Wind-blown dust settles into fertile soil."),
    (T_DES, "Medium", "The steep-sided desert valley that remains dry except immediately after rare storms is a",
     "wadi", "oasis",
     "erg", "pediment", "A",
     "The flash flood roars through and is gone."),
    (T_POP, "Medium", "The emigration of the best-trained doctors and engineers from a country in search of better pay abroad is called",
     "brain drain", "chain migration",
     "return migration", "labour circulation", "A",
     "The nation's trained minds flow outward."),
    (T_AGR, "Medium", "The small farm close to a city on which vegetables and flowers are grown for the daily urban market practises",
     "market gardening", "dairy farming",
     "shifting cultivation", "ranching", "A",
     "Its fresh produce races to the city each dawn."),
    (T_AGR, "Medium", "Farming in which a family grows food mainly to feed itself, with little or no surplus for sale, is",
     "subsistence farming", "commercial farming",
     "plantation farming", "collective farming", "A",
     "The harvest feeds the household first."),
    (T_SET, "Hard", "A settlement deliberately sited on dry, raised ground above marshes and flood plains is a",
     "dry-point settlement", "wet-point settlement",
     "bridge-point town", "nodal centre", "A",
     "Its founders fled the wet ground below."),
    (T_SET, "Hard", "The position of a settlement in relation to other settlements, routes and surrounding regions is its",
     "situation", "site",
     "sphere of influence", "range of services", "A",
     "It describes the settlement's address in the wider world."),
    (T_SET, "Medium", "A city that is far larger than any other city in its country and dominates its national life, as Lagos once dominated Nigeria, is a",
     "primate city", "capital city",
     "new town", "free port", "A",
     "The head is far bigger than the body."),
    (T_MAP, "Medium", "A slope that faces the warm midday sun will enjoy warmer conditions than one in shadow. This influence of slope direction on climate is called",
     "aspect", "albedo",
     "anemometry", "exposure to frost", "A",
     "Vineyards climb the sunny side of the valley."),
    (T_CLI, "Medium", "An area of low atmospheric pressure, with inward-spiralling winds and unsettled, showery weather, is a",
     "depression", "anticyclone",
     "ridge of high pressure", "col", "A",
     "The weather map's trough of storms."),
    (T_MAP, "Medium", "When streams flow outward in all directions from the top of a dome-shaped highland, the drainage pattern formed is",
     "radial", "dendritic",
     "trellis", "annular only", "A",
     "Like spokes from a hub the rivers run."),
    (T_MAP, "Medium", "The daily mean temperature of a station is obtained by",
     "adding the maximum and minimum and dividing by two", "reading the thermometer at noon only",
     "averaging all hourly readings of sunshine", "subtracting the minimum from the maximum", "A",
     "The day's heat and cold share one figure."),
    (T_MAP, "Hard", "The wind-rose diagram of a weather station shows chiefly",
     "how often the wind blew from each direction", "the speed of the fastest gale",
     "the pressure at every hour", "the temperature of each wind", "A",
     "Longer arms mark the steadier winds."),
]

build_batch(
    S,
    "batch_213_neco_geo8.json",
    "213",
    "NECO Geography round 8 (R42 top-up): carbonation; landslides; "
    "arêtes; hanging valleys; erratics; pyramidal peaks; ribbon "
    "lakes; peneplains; monadnocks; loess; wadis; brain drain; "
    "market gardening; subsistence farming; dry-point and "
    "situation of settlements; primate cities; aspect; "
    "depressions as low pressure; radial drainage; daily mean "
    "temperature; the wind rose. Scanned against the whole "
    "Geography pool (WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
