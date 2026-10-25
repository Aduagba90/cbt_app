"""Batch 151 - NECO Agricultural Science round 5 (NECO top-up, R28).

Grows NECO Agric from 176 toward ~212 with angles not yet in the
bank: soil texture vs structure; hygroscopic and gravitational water;
liming acidic soils; nitrogen and potassium roles; propagation by
vine, stem cutting and rhizome; the biennial carrot; legume nitrogen
fixation; intercropping, zero tillage, mulching, strip cropping;
biological control with ladybirds; herbicides; fumigating store
weevils; fungal smut and rust; vaccination and quarantine; dipping,
castration, deep litter, bee products; genotype, hybrid vigour,
inbreeding depression; the inventory record; tannery and feed-mill
linkages; deforestation and bush burning harms; variable farm costs.
Scanned against NECO rounds 1-4, WAEC Agric (all rounds) and the JAMB
pool.

    python3 scripts/build_neco_batch151.py -> content/batch_151_neco_agric5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Agricultural Science"

T_SOI = "Soil and Plant Nutrition"
T_CRO = "Crops and Cropping Practices"
T_PES = "Pests and Disease Control"
T_ANI = "Animal Production"
T_GEN = "Genetics and Breeding"
T_REC = "Records and Agro-Allied Industries"
T_ENV = "Agriculture and the Environment"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- soil & nutrition
    (T_SOI, "Hard", "The proportion of sand, silt and clay particles in a soil defines its",
     "texture", "structure", "fertility", "profile", "A",
     "Feel a handful: that is texture."),
    (T_SOI, "Hard", "The way soil particles clump together into aggregates is the soil's",
     "structure", "texture", "colour", "salinity", "A",
     "Crumb, block or plate describes it."),
    (T_SOI, "Hard", "Days after rain, a thin film still hugs every soil particle, beyond any root's power to pull. This film is the",
     "hygroscopic water", "gravitational water", "capillary water", "free water", "A",
     "It clings beyond the root's reach."),
    (T_SOI, "Medium", "Water that drains freely down through the soil soon after rain is",
     "gravitational water", "hygroscopic water", "bound water", "sap water", "A",
     "It visits briefly and leaves."),
    (T_SOI, "Medium", "Ground limestone is spread on a farm chiefly to",
     "reduce soil acidity", "add nitrogen", "kill weeds", "hasten ripening", "A",
     "Sweet soil for sour fields."),
    (T_SOI, "Medium", "General yellowing of lower maize leaves usually signals shortage of",
     "nitrogen", "iron alone", "copper", "boron", "A",
     "Green pigment needs it most."),
    (T_SOI, "Hard", "Potassium dressing helps crops chiefly by",
     "strengthening disease resistance", "deepening flower colour", "speeding germination", "softening fruits", "A",
     "Sturdy stalks resist attack."),

    # ------------------------------------------------------------- crops
    (T_CRO, "Medium", "Sweet potato is commonly propagated by",
     "vine cuttings", "true seeds", "root suckers", "bulbils", "A",
     "Vines planted in heaps of ridges."),
    (T_CRO, "Medium", "Ginger is propagated by planting pieces of its",
     "rhizome", "seed", "leaf", "root cutting", "A",
     "The knobby underground stem."),
    (T_CRO, "Hard", "A crop like the carrot that completes its life cycle in two growing seasons is",
     "biennial", "annual", "perennial", "ephemeral", "A",
     "Root one year, seed the next."),
    (T_CRO, "Medium", "Cowpea and other pulses improve the soil because their root nodules",
     "fix atmospheric nitrogen", "hold rain water", "absorb sunlight", "kill nematodes", "A",
     "Tiny tenants make free fertiliser."),
    (T_CRO, "Hard", "Growing maize and cowpea together on the same ridges in the same season is",
     "intercropping", "crop rotation", "fallowing", "monoculture", "A",
     "Two crops share one bed of soil."),
    (T_CRO, "Hard", "Leaving land untilled and sowing directly into stubble is called",
     "zero tillage", "deep ploughing", "harrowing", "ridging", "A",
     "The soil keeps its own blanket."),
    (T_CRO, "Medium", "Spreading dry grass around young citrus trees chiefly",
     "conserves soil moisture", "adds colours", "attracts birds", "raises pH", "A",
     "The ground stays cool and damp."),
    (T_CRO, "Hard", "Planting bands of different crops across a slope, rather than down it, is",
     "strip cropping", "mixed farming", "land rotation", "taungya", "A",
     "Each strip brakes the run-off."),

    # ------------------------------------------------------------- pests & diseases
    (T_PES, "Hard", "Releasing ladybirds into an aphid-infested vegetable plot is an example of",
     "biological control", "chemical control", "physical control", "prophylaxis", "A",
     "One insect polices another."),
    (T_PES, "Medium", "The chemical used to kill unwanted plants on the farm is a",
     "herbicide", "insecticide", "fungicide", "nematicide", "A",
     "Its chosen targets are the weeds."),
    (T_PES, "Hard", "Grain stores infested with weevils are commonly cleaned up by",
     "fumigation", "irrigation", "mulching", "winnowing", "A",
     "The gas reaches every crack."),
    (T_PES, "Medium", "Smut and rust, which attack maize and other cereals, are caused by",
     "fungi", "viruses", "nematodes", "birds", "A",
     "Spores spread their kind."),
    (T_PES, "Medium", "Vaccinating a healthy animal protects it by building",
     "artificial active immunity", "natural passive immunity", "no immunity", "instant cure", "A",
     "The body rehearses its defence."),
    (T_PES, "Medium", "Keeping newly bought animals apart from the herd for some weeks is",
     "quarantine", "culling", "dipping", "tagging", "A",
     "A waiting room against disease."),

    # ------------------------------------------------------------- animals
    (T_ANI, "Medium", "Dipping or spraying cattle chiefly rids them of",
     "ticks", "tapeworms", "flukes in the liver", "roundworms only", "A",
     "The dip bath drowns the external pests."),
    (T_ANI, "Hard", "Castrating young male animals intended for meat chiefly makes them",
     "docile with better meat", "faster runners", "better breeders", "immune to flies", "A",
     "Calm animals lay down flesh."),
    (T_ANI, "Medium", "In the deep litter system, poultry are kept",
     "on the floor over bedding", "in individual wire cages", "free on open range", "in battery stacks", "A",
     "Scratching birds on shavings."),
    (T_ANI, "Medium", "Besides honey, the other major hive product is",
     "beeswax", "royal jelly alone", "pollen only", "propolis only", "A",
     "Candles and polish come from it."),
    (T_ANI, "Medium", "A farmer judges an animal healthy when it shows",
     "bright eyes and good appetite", "dull coat and isolation", "constant diarrhoea", "drooping wings", "A",
     "Appetite is the first report card."),

    # ------------------------------------------------------------- genetics
    (T_GEN, "Hard", "The genetic make-up of an animal, whether seen or hidden, is its",
     "genotype", "phenotype", "prototype", "karyotype", "A",
     "It hides in the chromosomes."),
    (T_GEN, "Hard", "When the offspring of two different parent lines outgrows both parents, the gain is called",
     "hybrid vigour", "mutation", "segregation", "dominance", "A",
     "Crossbreeding's welcome bonus."),
    (T_GEN, "Medium", "Continued mating of close relatives weakens stock, a problem known as",
     "inbreeding depression", "heterosis", "polyploidy", "linkage", "A",
     "The family circle grows frail."),

    # ------------------------------------------------------------- records & industries
    (T_REC, "Medium", "The farm record listing every asset owned, from hoes to tractors, is the",
     "inventory", "cash book", "daily diary", "payroll", "A",
     "A yearly census of the farm."),
    (T_REC, "Medium", "A tannery depends on livestock farming to supply",
     "hides and skins", "milk", "eggs", "honey", "A",
     "Leather begins in the kraal."),
    (T_REC, "Medium", "A poultry feed mill depends on crop farmers mainly for",
     "maize and groundnut cake", "fish meal alone", "feathers", "sawdust", "A",
     "Grains fill the feed sacks."),

    # ------------------------------------------------------------- environment
    (T_ENV, "Hard", "Clearing forests without replanting finally invites",
     "erosion and loss of wildlife", "heavier snowfall", "richer topsoil", "cooler nights only", "A",
     "The bare hills weep their soil away."),
    (T_ENV, "Medium", "The chief reason repeated bush burning is condemned is that it destroys",
     "organic matter and soil organisms", "only the weeds", "soil texture permanently", "farm tools", "A",
     "The soil's living wealth burns."),
    (T_ENV, "Medium", "In farm accounting, the cost of feeds and day-old chicks is a",
     "variable cost", "fixed cost", "sunk rent", "capital grant", "A",
     "It rises and falls with the flock."),
]

build_batch(
    S,
    "batch_151_neco_agric5.json",
    "151",
    "NECO Agricultural Science round 5 (R28 top-up): texture vs "
    "structure, hygroscopic and gravitational water, liming, nitrogen "
    "yellowing, potassium and resistance; sweet potato vines, ginger "
    "rhizomes, biennial carrot, legume fixation, intercropping, zero "
    "tillage, mulching, strip cropping; ladybirds as biological "
    "control, herbicide, fumigation, fungal smut and rust, vaccination "
    "immunity, quarantine; dipping, castration, deep litter, beeswax, "
    "health signs; genotype, hybrid vigour, inbreeding depression; "
    "inventory record, tannery linkage, feed mill; deforestation and "
    "bush burning harms, variable costs. Scanned against NECO rounds "
    "1-4, WAEC Agric (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
