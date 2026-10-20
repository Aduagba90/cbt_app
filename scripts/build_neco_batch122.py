"""Batch 122 - WAEC Biology round 3 (WAEC top-up, Round 23).

Lifts WAEC Biology from 146 toward ~190 with angles not yet in any
bank: cell organelles and division, transport in plants and animals,
digestion and enzymes, gaseous exchange, excretion and the nephron,
reproduction and menstrual cycle, genetics numerics and sex
determination, ecology (cycles, pyramids, symbiosis), coordination and
homeostasis, and crop/plant biology. Scanned against WAEC rounds 1-2,
NECO Biology and the JAMB Biology pool.

    python3 scripts/build_neco_batch122.py -> content/batch_122_waec_bio3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Biology"

T_CELL = "The Cell and Cell Division"
T_TRAN = "Transport Systems"
T_NUT = "Nutrition and Digestion"
T_GAS = "Gaseous Exchange and Excretion"
T_REP = "Reproduction and Genetics"
T_ECO = "Ecology"
T_CO = "Coordination and Homeostasis"
T_PL = "Plant Biology"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- cell
    (T_CELL, "Medium", "The organelle that releases energy from food in a cell is the",
     "mitochondrion", "ribosome", "nucleus", "vacuole", "A",
     "It is the cell's powerhouse."),
    (T_CELL, "Medium", "Ribosomes are the sites of",
     "protein synthesis", "photosynthesis", "respiration only", "waste storage", "A",
     "Amino acids are joined there."),
    (T_CELL, "Hard", "The cell wall of a plant is made mostly of",
     "cellulose", "chitin", "protein", "fat", "A",
     "Fibres of it stiffen the wall."),
    (T_CELL, "Medium", "As a cell splits by mitosis, the two new cells are",
     "genetically identical", "half the chromosome number", "of different species", "fused gametes", "A",
     "They are copies, not halves."),
    (T_CELL, "Hard", "Meiosis halves the chromosome number, which is essential for",
     "sexual reproduction", "growth of tissues", "wound healing", "asexual budding", "A",
     "Gametes must halve before fusion."),
    (T_CELL, "Hard", "After mitosis of a 20-chromosome cell, each daughter holds",
     "20 chromosomes", "10 chromosomes", "40 chromosomes", "80 chromosomes", "A",
     "Mitosis keeps the count steady.", "20"),

    # ------------------------------------------------------------- transport
    (T_TRAN, "Medium", "The tissue that carries water upward in a stem is the",
     "xylem", "phloem", "cambium", "cortex", "A",
     "Its dead tubes act as pipes."),
    (T_TRAN, "Medium", "Phloem translocates",
     "dissolved food", "pure water only", "mineral salts only", "gases alone", "A",
     "Sugar syrup travels in it."),
    (T_TRAN, "Hard", "The loss of water vapour from leaves is called",
     "transpiration", "respiration", "gutation", "condensation", "A",
     "The stomata guard the exit."),
    (T_TRAN, "Medium", "The pumping organ of the human transport system is the",
     "heart", "liver", "kidney", "spleen", "A",
     "Four chambers share one beat."),
    (T_TRAN, "Hard", "The blood cells that transport oxygen are the",
     "red blood cells", "white blood cells", "platelets", "plasma cells", "A",
     "Haemoglobin binds the gas."),
    (T_TRAN, "Hard", "Blood flowing from the small intestine to the liver travels in the",
     "hepatic portal vein", "aorta", "pulmonary vein", "renal artery", "A",
     "Food-rich blood takes this shortcut."),

    # ------------------------------------------------------------- nutrition
    (T_NUT, "Medium", "Photosynthesis produces glucose and",
     "oxygen", "carbon dioxide", "nitrogen", "hydrogen only", "A",
     "The waste gas is a treasure."),
    (T_NUT, "Hard", "The green pigment that traps light energy is",
     "chlorophyll", "haemoglobin", "melanin", "carotene only", "A",
     "It sits in the chloroplast."),
    (T_NUT, "Medium", "Enzyme activity is fastest at the enzyme's",
     "optimum temperature", "boiling point", "freezing point", "highest pH", "A",
     "Beyond it, activity collapses."),
    (T_NUT, "Medium", "An enzyme acts only on its specific substrate because of the",
     "lock-and-key fit", "random collisions", "size of the cell", "colour of the food", "A",
     "A matching shape meets its shape."),
    (T_NUT, "Hard", "The enzyme in saliva breaks down",
     "starch", "protein", "fat", "vitamins", "A",
     "Sweetness follows its work."),
    (T_NUT, "Medium", "Protein digestion finally yields",
     "amino acids", "fatty acids", "glucose units", "water only", "A",
     "Building blocks for the body."),

    # ------------------------------------------------------------- gas exchange and excretion
    (T_GAS, "Hard", "Gas swaps swiftly in the lungs because the air sacs are",
     "thin-walled and numerous", "thick and few", "lined with mucus only", "filled with blood clots", "A",
     "A huge thin surface speeds diffusion."),
    (T_GAS, "Medium", "During vigorous exercise, muscles produce lactic acid when oxygen runs short; this is the",
     "oxygen debt", "nitrogen debt", "carbon credit", "photosynthetic sink", "A",
     "Panting slowly repays it later."),
    (T_GAS, "Hard", "Each kidney cleans blood through a million working units called the",
     "nephron", "neuron", "alveolus", "villus", "A",
     "A million work in each kidney."),
    (T_GAS, "Medium", "The main nitrogenous waste in human urine is",
     "urea", "ammonia only", "glucose", "salts alone", "A",
     "The liver makes it from proteins."),

    # ------------------------------------------------------------- reproduction and genetics
    (T_REP, "Medium", "The normal human menstrual cycle runs about",
     "28 days", "14 days", "60 days", "7 days", "A",
     "Ovulation sits mid-cycle.", "28"),
    (T_REP, "Hard", "Fertilisation of the human egg normally occurs in the",
     "fallopian tube", "uterus wall", "ovary itself", "cervix", "A",
     "The tube is the meeting place."),
    (T_REP, "Hard", "The placenta serves the foetus by",
     "exchanging food, gas and waste", "pumping blood to the mother", "digesting milk", "breathing air", "A",
     "It is the unborn child's market."),
    (T_REP, "Hard", "Crossing pure tall (TT) with pure short (tt) pea plants gives offspring that are all",
     "tall carriers (Tt)", "short pure (tt)", "medium height", "half tall, half short", "A",
     "The dominant tall gene shows."),
    (T_REP, "Hard", "Two heterozygous tall plants (Tt x Tt) produce tall to short offspring in the ratio",
     "3 to 1", "1 to 1", "all tall", "2 to 1", "A",
     "It is Mendel's classic ratio.", "3"),
    (T_REP, "Medium", "A human baby's sex is determined by the chromosome carried in the",
     "father's sperm", "mother's egg always", "placenta", "first trimester diet", "A",
     "The X or Y sperm tips the scale."),
    (T_REP, "Medium", "Sickle-cell anaemia is inherited when a child receives",
     "the gene from both parents", "the gene from one parent only", "no gene at all", "a malaria infection", "A",
     "Carriers carry only one copy."),

    # ------------------------------------------------------------- ecology
    (T_ECO, "Medium", "Bacteria in root nodules return nitrogen to the soil as part of the",
     "nitrogen cycle", "water cycle", "carbon cycle", "phosphorus cycle", "A",
     "Nitrogen fixation feeds the farm."),
    (T_ECO, "Hard", "Carbon returns to the atmosphere chiefly through",
     "respiration and combustion", "photosynthesis alone", "erosion only", "rainfall", "A",
     "Breathing and burning both release it."),
    (T_ECO, "Hard", "In a food chain, the arrows always point towards the",
     "consumer", "producer always", "sun", "soil", "A",
     "Energy flows to the eater."),
    (T_ECO, "Medium", "The wide base of an energy pyramid represents the",
     "producers", "top carnivores", "decomposers", "parasites", "A",
     "Green plants hold the most energy."),
    (T_ECO, "Hard", "A tick feeding on a cow is an example of",
     "parasitism", "mutualism", "commensalism", "predation", "A",
     "One gains, the other bleeds."),
    (T_ECO, "Medium", "Rhizobium in legume roots, helping both plant and bacteria, illustrates",
     "mutualism", "parasitism", "competition", "saprophytism", "A",
     "Here both partners profit."),

    # ------------------------------------------------------------- coordination
    (T_CO, "Medium", "The gap across which a nerve impulse jumps between two neurons is the",
     "synapse", "synapse gap only named cleft", "dendrite", "myelin", "A",
     "Chemicals ferry the message."),
    (T_CO, "Medium", "Standing upright without toppling is managed by the",
     "cerebellum", "cerebrum", "medulla", "hypothalamus", "A",
     "It sits below the back of the skull."),
    (T_CO, "Hard", "Insulin lowers blood sugar by making cells",
     "take up glucose", "release glucose", "store fat only", "digest protein", "A",
     "The pancreas secretes it."),
    (T_CO, "Medium", "The pulling away of the hand from a hot object is a",
     "reflex action", "learned habit", "conscious choice", "hormonal response", "A",
     "The spinal cord decides fast."),

    # ------------------------------------------------------------- plant biology
    (T_PL, "Hard", "Insect pollinated flowers usually have",
     "scent and nectar", "light dry pollen", "no petals at all", "feathery stigmas", "A",
     "Scent and nectar invite couriers."),
    (T_PL, "Medium", "Wind pollinated flowers produce pollen that is",
     "light and abundant", "heavy and sticky", "scented strongly", "encased in fruit", "A",
     "The breeze spreads the odds."),
    (T_PL, "Hard", "Seeds dispersed by wind, like the mahogany's, have",
     "wing-like outgrowths", "hooks and spines", "sweet juicy coats", "floating air sacs only", "A",
     "Blades catch the moving air."),
    (T_PL, "Medium", "Auxin, the plant growth hormone, chiefly causes",
     "cell elongation", "leaf fall", "fruit ripening only", "seed dormancy", "A",
     "Tips bend towards light with it."),
]

build_batch(
    S,
    "batch_122_waec_bio3.json",
    "122",
    "WAEC Biology round 3 (Round 23 top-up): mitochondrion and ribosome "
    "roles, cellulose walls, mitosis vs meiosis, 20-chromosome "
    "daughters, xylem and phloem loads, transpiration, red cells and "
    "haemoglobin, hepatic portal vein, photosynthesis outputs, "
    "chlorophyll, enzyme optimum and lock-and-key, salivary amylase, "
    "amino acid ends, alveoli efficiency, oxygen debt, the nephron, "
    "urea, 28-day cycle, fallopian fertilisation, placenta exchange, "
    "TT x tt and Tt x Tt ratios, sex determination, sickle inheritance, "
    "nitrogen cycle bacteria, carbon returns, food-chain arrows, energy "
    "pyramid base, tick parasitism, Rhizobium mutualism, the synapse, "
    "cerebellum, insulin, reflex arc, insect vs wind pollination, "
    "winged seeds and auxin. Scanned against WAEC rounds 1-2, NECO "
    "Biology and the JAMB Biology pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
