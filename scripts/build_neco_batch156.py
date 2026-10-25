"""Batch 156 - WAEC Biology round 6 (WAEC top-up, R29).

Grows WAEC Biology from 189 toward ~225 with angles not yet in the
bank: cell organelles (mitochondrion, ribosome, chloroplast, cell
wall), plasmolysis and turgidity, osmosis and diffusion scenarios;
transpiration pull, guard cells, translocation, limiting factors,
aerobic and anaerobic word equations, oxygen debt; bile emulsification,
villi absorption, cellulose digestion, incisors; plasma transport,
platelets, arterial and venous structure, capillary walls;
phagocytosis, ultrafiltration, liver duties, sweating; insulin,
retina rods, semicircular canals, antagonistic muscles; epigeal vs
hypogeal, insect pollination, wind dispersal, decomposers, game
reserves. Scanned against WAEC rounds 1-4, NECO Biology (all rounds)
and the JAMB pool.

    python3 scripts/build_neco_batch156.py -> content/batch_156_waec_bio6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Biology"

T_CELL = "The Cell and Transport"
T_PLA = "Plant Physiology"
T_RES = "Respiration"
T_NUT = "Nutrition and Digestion"
T_TRA = "Transport and Blood"
T_DEF = "Defence and Excretion"
T_REG = "Coordination and Movement"
T_REP = "Reproduction, Genetics and Ecology"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- cell & transport
    (T_CELL, "Medium", "The organelle long called the powerhouse of the cell is the",
     "mitochondrion", "ribosome", "nucleolus", "lysosome", "A",
     "Energy currency leaves its folds."),
    (T_CELL, "Medium", "The organelle on which amino acids are assembled into proteins is the",
     "ribosome", "chloroplast", "vacuole", "centrosome", "A",
     "The cell's own bench of building."),
    (T_CELL, "Medium", "Photosynthesis happens inside the green pigment of the",
     "chloroplast", "mitochondrion", "Golgi body", "nuclear sap", "A",
     "Sunlight is trapped in its stacks."),
    (T_CELL, "Medium", "The outer layer found in plant cells but absent in animal cells is the",
     "cell wall", "cell membrane", "nuclear membrane", "plasma lining", "A",
     "Cellulose armour for plants."),
    (T_CELL, "Hard", "When plant cells lose water to a strong sugar solution, their cytoplasm shrinks from the walls. This is",
     "plasmolysis", "turgidity", "osmosis itself", "diffusion alone", "A",
     "The cell faints inward on itself."),
    (T_CELL, "Medium", "A plant cell firm and swollen with water is described as",
     "turgid", "flaccid", "plasmolysed", "crenated", "A",
     "Fullness keeps the stem upright."),
    (T_CELL, "Medium", "Water moves into a plant root hair because the cell sap is",
     "more concentrated than the soil water", "less concentrated than the soil water", "of equal concentration", "entirely absent", "A",
     "The stronger sap draws the water."),
    (T_CELL, "Hard", "The spreading of perfume from a corner of a room until it fills it illustrates",
     "diffusion", "active transport", "osmosis", "transpiration", "A",
     "Particles wander down their own slope."),
    (T_CELL, "Hard", "The surface area to volume ratio sets the limit of cell size because exchange happens at the",
     "across the surface", "inside the nucleus alone", "within mitochondria only", "along the vacuole edge", "A",
     "Big cells starve at their cores."),

    # ------------------------------------------------------------- plant physiology
    (T_PLA, "Hard", "The main force lifting water up tall trees is",
     "transpiration pull", "root pressure alone", "capillarity alone", "air pressure", "A",
     "Evaporation from leaves hauls the column."),
    (T_PLA, "Medium", "Stomata open when their guard cells",
     "become turgid", "lose all water", "divide in two", "turn green", "A",
     "Swollen cells bow the pore open."),
    (T_PLA, "Medium", "Sugars made in leaves travel to roots and fruits through the",
     "phloem", "xylem", "cambium", "cortex", "A",
     "The food lanes of the stem."),
    (T_PLA, "Hard", "In a dim greenhouse, the factor most likely limiting photosynthesis is",
     "light intensity", "chlorophyll amount", "carbon dioxide alone", "soil texture", "A",
     "Brightness sets the day's pace."),

    # ------------------------------------------------------------- respiration
    (T_RES, "Medium", "The complete word equation of aerobic respiration reads: glucose plus oxygen yields carbon dioxide, water and",
     "energy", "protein", "chlorophyll", "nitrogen", "A",
     "Every living cell cashes it."),
    (T_RES, "Hard", "In yeast cells starved of oxygen, glucose ends chiefly as alcohol and",
     "carbon dioxide", "lactic acid", "water", "oxygen debt", "A",
     "Brewers owe their trade to it."),
    (T_RES, "Hard", "The ache in a sprinter's legs after a 400-metre dash comes from accumulated",
     "lactic acid", "alcohol", "glycogen", "carbon monoxide", "A",
     "The oxygen debt collects interest."),

    # ------------------------------------------------------------- nutrition & digestion
    (T_NUT, "Medium", "Bile helps fat digestion by breaking globules into droplets, a process called",
     "emulsification", "hydrolysis", "condensation", "assimilation", "A",
     "More surface for the enzyme's work."),
    (T_NUT, "Hard", "The tiny finger-like projections lining the small intestine, absorbing digested food, are the",
     "villi", "alveoli", "papillae", "cilia", "A",
     "A velvet of absorbing fingers."),
    (T_NUT, "Hard", "Herbivores like the rabbit have a long caecum because they must digest",
     "cellulose", "fats alone", "proteins only", "mineral salts", "A",
     "Plant walls need long, patient ferment."),
    (T_NUT, "Medium", "The teeth shaped for biting and cutting food at the front of the mouth are the",
     "incisors", "canines", "premolars", "molars", "A",
     "Thin edges for the first bite."),

    # ------------------------------------------------------------- transport & blood
    (T_TRA, "Medium", "The liquid part of blood that carries dissolved food and wastes is",
     "plasma", "haemoglobin", "platelets", "lymphocytes", "A",
     "Ninety per cent of it is water."),
    (T_TRA, "Medium", "The blood cells whose duty is clotting are the",
     "platelets", "red cells", "white cells", "plasma cells", "A",
     "They plug the broken vessel."),
    (T_TRA, "Medium", "Arteries are built with thick muscular walls because they",
     "bear blood at high pressure", "carry no blood", "lie outside the body", "hold only air", "A",
     "The pulse pounds hard there."),
    (T_TRA, "Medium", "The valves inside veins chiefly",
     "prevent backflow of blood", "mix the blood", "add oxygen", "filter clots", "A",
     "One-way doors against gravity."),
    (T_TRA, "Hard", "Exchange of gases and food between blood and tissues occurs across walls that are",
     "one cell thick", "muscle thick", "cartilage lined", "valve guarded", "A",
     "Thin walls trade swiftly."),

    # ------------------------------------------------------------- defence & excretion
    (T_DEF, "Hard", "White blood cells that surround and swallow germs perform",
     "phagocytosis", "osmosis", "plasmolysis", "transpiration", "A",
     "The cell simply eats its enemy."),
    (T_DEF, "Hard", "The first stage of urine formation, where blood is filtered in the kidney, is",
     "ultrafiltration", "reabsorption", "assimilation", "excretion", "A",
     "The glomerulus strains the blood."),
    (T_DEF, "Medium", "Besides making bile, the liver also",
     "detoxifies harmful substances", "pumps blood", "stores urine", "makes insulin", "A",
     "The body's chemical factory."),
    (T_DEF, "Medium", "Sweating cools the body because evaporating water",
     "carries away heat", "adds salts", "warms the skin", "blocks the sun", "A",
     "Each drop leaving takes heat."),

    # ------------------------------------------------------------- coordination & movement
    (T_REG, "Medium", "The hormone insulin, which lowers blood sugar, is secreted by the",
     "pancreas", "liver", "pituitary", "adrenal", "A",
     "Islets in that organ make it."),
    (T_REG, "Medium", "Rods in the retina of the eye are most useful in",
     "dim light", "bright light", "complete darkness", "colour vision", "A",
     "They trade colour for sensitivity."),
    (T_REG, "Medium", "The organ of balance in the ear is the",
     "semicircular canals", "cochlea", "ear drum", "eustachian tube", "A",
     "Three loops sense every tilt."),
    (T_REG, "Medium", "Biceps and triceps working as a pair at the elbow are said to be",
     "antagonistic", "synergistic only", "identical", "redundant", "A",
     "One bends as the other straightens."),

    # ------------------------------------------------------------- reproduction, genetics & ecology
    (T_REP, "Medium", "In epigeal germination, the cotyledons are carried",
     "above the soil", "below the soil", "into the fruit", "nowhere at all", "A",
     "The loop hauls them aloft."),
    (T_REP, "Hard", "Flowers pollinated by insects typically have",
     "bright colour and nectar", "small and dull petals", "feathery dry stigmas", "abundant pollen dust", "A",
     "The insect is bribed and guided."),
    (T_REP, "Hard", "Winged seeds of plants like the African tulip are dispersed by",
     "wind", "water", "birds", "explosions", "A",
     "The blade rides the breeze."),
    (T_REP, "Medium", "A fallen mango left on moist ground soon vanishes, its nutrients returning to the soil through",
     "decomposers", "producers", "predators", "parasites", "A",
     "Nature's own recycling crew."),
    (T_REP, "Medium", "Wildlife is protected from hunters and habitat loss inside",
     "game reserves", " ranches", "piggeries", "fish ponds", "A",
     "The ranger guards the boundary."),
]

build_batch(
    S,
    "batch_156_waec_bio6.json",
    "156",
    "WAEC Biology round 6 (R29 top-up): mitochondrion, ribosome, "
    "chloroplast, cell wall; plasmolysis, turgidity, root-hair osmosis, "
    "perfume diffusion, surface-area limit; transpiration pull, guard "
    "cells, phloem, limiting light; aerobic word equation, yeast "
    "alcohol, lactic debt; bile emulsification, villi, caecum "
    "cellulose, incisors; plasma, platelets, arterial walls, venous "
    "valves, capillary thinness; phagocytosis, ultrafiltration, liver "
    "detox, sweating; insulin, rods, semicircular canals, antagonistic "
    "pair; epigeal cotyledons, insect-pollinated flowers, winged seed "
    "dispersal, decomposers, game reserves. Scanned against WAEC "
    "rounds 1-4, NECO Biology (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
