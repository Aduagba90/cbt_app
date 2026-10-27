"""Batch 226 - NECO Biology round 7 (NECO top-up, R46).

Grows NECO Biology from 252 toward ~277 with angles verified absent
from the whole Biology pool (1,367 items across JAMB, WAEC and NECO):
haemolysis; serum; emphysema; asthma; abscission; grana; stroma;
limiting factor; compensation point; carotenoids; penicillin;
vasectomy; condom; tubal ligation; apical dominance; cytokinin;
binomial nomenclature; hermaphrodite; leukaemia; thrombosis;
hypertension; sickle-cell carrier malaria resistance; myoglobin;
puberty; dehiscent fruit. Checked and avoided (already banked): all
major organ systems and classic experiments (see R37-R45 entries),
test cross, albinism cross, secondary sexual characters, rhesus,
fibrinogen, universal donor, taxonomy families (classification,
kingdom, phylum, Homo = genus), classification uses, gibberellin
(stem-growth item), tahnik-style singletons, heredity families,
cell organelles, tropism families, kwashiorkor/rickets, goitre,
cholera/typhoid family, retina family, reflex arc, endocrine items.

    python3 scripts/build_neco_batch226.py -> content/batch_226_neco_bio7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Biology"

T_TRAN = "Transport Systems"
T_DIS = "Diseases and Immunity"
T_RESP = "Respiration and Gaseous Exchange"
T_PLANT = "Plant Structure and Function"
T_NUTP = "Nutrition in Plants and Animals"
T_HORM = "Hormones and Plants"
T_VAR = "The Cell" if False else "Cell Structure and Organisation"
T_GEN = "Genetics and Heredity"
T_REPRO = "Reproduction and Growth"
T_EXCR = "Excretion"
T_Supp = "Support and Movement"
T_VAR2 = "Variety of Organisms" if False else "Ecology and Ecosystems"

PASSAGES = []
PQ = []

Q = [
    (T_TRAN, "Medium", "When red blood cells are placed in distilled water, water enters them by osmosis until they swell and burst. The bursting of the red cells is called",
     "haemolysis", "plasmolysis",
     "haemopoiesis", "hydrolysis", "A",
     "Fresh water swells the cell till its membrane gives way."),
    (T_TRAN, "Medium", "After blood has clotted in a test tube, the pale yellow fluid that separates out on top, free of the clotting protein, is called",
     "serum", "plasma",
     "lymph", "glucose solution", "A",
     "It is plasma that has lost its fibrinogen."),
    (T_DIS, "Medium", "A heavy smoker becomes breathless because the walls of his air sacs have broken down and fused into large weak sacs. This lung disease is",
     "emphysema", "asthma",
     "bronchitis", "pneumonia", "A",
     "The fine air sacs lose their elastic walls."),
    (T_DIS, "Medium", "A disease in which the air passages of the lungs become narrow and produce much mucus, making breathing wheezy, is",
     "asthma", "rabies",
     "malaria", "smallpox", "A",
     "The tightened tubes whistle as air squeezes through."),
    (T_DIS, "Hard", "A disease in which the body makes far too many abnormal white blood cells, crowding the marrow and weakening immunity, is",
     "leukaemia", "haemophilia",
     "anaemia", "sickle cell", "A",
     "The white cells multiply beyond all control."),
    (T_TRAN, "Medium", "A traveller sits still in a bus for many hours, and a clot forms inside the deep vein of his leg. A clot forming inside a blood vessel is called",
     "thrombosis", "circulation",
     "transfusion", "osmosis", "A",
     "The clot grows where the blood flows too slowly."),
    (T_TRAN, "Medium", "A condition in which the blood pressure remains persistently higher than normal, straining the heart and the arteries, is",
     "hypertension", "hypotension",
     "hypermetropia", "haematuria", "A",
     "The silent strain that doctors measure with a cuff."),
    (T_DIS, "Medium", "The antibiotic obtained from the mould Penicillium, which kills bacteria by stopping their cell walls from forming, is",
     "penicillin", "quinine",
     "aspirin", "insulin", "A",
     "Fleming's mould gave medicine its first antibiotic."),
    (T_PLANT, "Medium", "In the dry season, a mango tree forms a soft layer of cells at the base of each leaf stalk, and the leaves fall. The shedding that follows this layer is called",
     "abscission", "absorption",
     "adhesion", "aeration", "A",
     "The weak layer lets the leaf break cleanly away."),
    (T_PLANT, "Hard", "Inside a chloroplast, the green pigment sits in stacks of coin-like membranes. These stacks, the sites of the light reactions, are called",
     "grana", "stroma",
     "cristae", "thylakoid discs alone", "A",
     "Each chloroplast holds many of these stacks."),
    (T_PLANT, "Hard", "The fluid matrix of a chloroplast that surrounds the stacks of membranes, in which carbon dioxide is fixed into sugar, is the",
     "stroma", "grana",
     "cytosol", "sap vacuole", "A",
     "The sugar-building reactions run in this fluid."),
    (T_PLANT, "Hard", "In photosynthesis, whichever requirement is in shortest supply — light, carbon dioxide or temperature — holds back the rate of the whole process. This is the law of",
     "limiting factors", "limiting reactants",
     "diminishing returns", "conservation of matter", "A",
     "The weakest link sets the pace of the chain."),
    (T_PLANT, "Hard", "At dawn or dusk, the rate at which a leaf releases carbon dioxide by respiration exactly equals the rate at which it uses it in photosynthesis. This balance point is the",
     "compensation point", "compensation depth",
     "neutral point", "osmotic point", "A",
     "At this moment the gas given out matches the gas taken in."),
    (T_PLANT, "Medium", "Besides chlorophyll, leaves contain yellow and orange pigments that absorb light of other colours and pass the energy on to chlorophyll. These pigments are the",
     "carotenoids", "carbohydrates",
     "carotid bodies", "collagen fibres", "A",
     "Their colours show plainly in yellow maize and carrots."),
    (T_HORM, "Medium", "A plant hormone that promotes cell division in roots and shoots and delays the ageing of leaves is",
     "cytokinin", "thyroxine",
     "insulin", "adrenaline", "A",
     "Its name comes from cytokinesis, the dividing of cells."),
    (T_HORM, "Hard", "The terminal bud of a young pine tree produces auxin that keeps the side buds below it from growing. This suppression of side branches by the growing tip is called",
     "apical dominance", "apical meristem",
     "axillary inhibition", "tropical dominance", "A",
     "Cut the tip and the sides are freed to sprout."),
    (T_NUTP, "Easy", "The system of naming every living thing with two Latin words, the first for its genus and the second for its species, is called",
     "binomial nomenclature", "unified classification",
     "dual taxonomy", "specific naming", "A",
     "Man is Homo sapiens under this two-name rule."),
    (T_VAR2 if False else T_REPRO, "Easy", "An animal such as the earthworm, which carries both male and female reproductive organs in one body, is said to be",
     "hermaphrodite", "heterozygous",
     "viviparous", "hemiparasitic", "A",
     "One worm carries both bride and groom."),
    (T_GEN, "Medium", "People who carry one sickle-cell allele rarely suffer severe malaria, because the parasite finds their slightly altered red cells a poor home. This survival advantage of carriers is known as",
     "heterozygote advantage", "homozygote dominance",
     "gene mutation pressure", "genetic drift", "A",
     "Carrying one allele shields them from the parasite."),
    (T_REPRO, "Medium", "The stage of life, roughly between ten and fourteen years, when a boy's or girl's reproductive organs mature and the secondary sexual characters appear, is called",
     "puberty", "menopause",
     "adolescence only", "childhood", "A",
     "The body's clock first rings at this season."),
    (T_REPRO, "Medium", "A surgical method of family planning in which each sperm duct is cut and tied so that no sperm can leave the body is",
     "vasectomy", "tubal ligation",
     "hysterectomy", "circumcision", "A",
     "The duct that carries sperm is closed."),
    (T_REPRO, "Medium", "A surgical method of family planning for women in which each fallopian tube is cut and tied so that no egg can reach the womb is",
     "tubal ligation", "vasectomy",
     "ovulation", "caesarean section", "A",
     "The tubes that carry the eggs are sealed."),
    (T_REPRO, "Easy", "A thin rubber sheath worn over the male organ during mating, which stops sperm from reaching the egg, is a",
     "condom", "coil",
     "cervical cap", "diaphragm tablet", "A",
     "It is a barrier that the sperm cannot cross."),
    (T_REPRO, "Medium", "A fruit such as the okra pod or the bean pod that splits open along one or more seams when ripe to release its seeds is described as",
     "dehiscent", "indehiscent",
     "succulent", "parthenocarpic", "A",
     "Ripeness throws its doors open for the seeds."),
    (T_Supp, "Hard", "The red pigment found in muscle fibres, which stores a small supply of oxygen for the muscle to use during hard work, is",
     "myoglobin", "haemoglobin",
     "melanin", "chlorophyll", "A",
     "It holds oxygen like a spare tank in the muscle."),
]

build_batch(
    S,
    "batch_226_neco_bio7.json",
    "226",
    "NECO Biology round 7 (R46 top-up): haemolysis; serum; emphysema; "
    "asthma; leukaemia; thrombosis; hypertension; penicillin; "
    "abscission; grana; stroma; law of limiting factors; "
    "compensation point; carotenoids; cytokinin; apical dominance; "
    "binomial nomenclature; hermaphrodite; sickle-carrier malaria "
    "resistance; puberty; vasectomy; tubal ligation; condom; "
    "dehiscent fruit; myoglobin. Scanned against the whole Biology "
    "pool (JAMB, WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
