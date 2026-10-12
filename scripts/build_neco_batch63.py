"""Batch 063 - NECO Biology top-up (round 2).

Grows the Biology bank from 89 to 150 items so students get two full
practice papers without repeats. Fresh scenario angles on all 14 topics.
Near-dup scanned against JAMB, WAEC and the existing NECO bank.

    python3 scripts/build_neco_batch63.py -> content/batch_063_neco_biology2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Biology"

T_CELL = "Cell Structure and Organisation"
T_DIV = "Cell Division"
T_NUT = "Nutrition in Plants and Animals"
T_TRAN = "Transport Systems"
T_RESP = "Respiration and Gaseous Exchange"
T_EXC = "Excretion"
T_REPRO = "Reproduction and Growth"
T_SUP = "Support and Movement"
T_NERV = "Nervous Coordination and Sense Organs"
T_HORM = "Hormones and Chemical Coordination"
T_GEN = "Genetics and Heredity"
T_ECO = "Ecology and Ecosystems"
T_DIS = "Diseases and Immunity"
T_LAB = "Biology Practical Skills"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- cell structure
    (T_CELL, "Medium", "Which organelle would you expect to be most numerous in an actively contracting muscle cell?",
     "Mitochondrion", "Ribosome", "Vacuole", "Nucleus", "A",
     "Active muscles need much energy, released in mitochondria."),
    (T_CELL, "Easy", "The crunch of fresh vegetables comes from the rigid material of their cell walls, which is",
     "cellulose", "chitin", "protein", "fat", "A",
     "Plant cell walls are built of cellulose fibres."),
    (T_CELL, "Medium", "A mature red blood cell differs from every other human cell because it",
     "lacks a nucleus", "has no cell membrane",
     "contains chlorophyll", "divides constantly", "A",
     "Losing the nucleus leaves more room for haemoglobin."),
    (T_CELL, "Hard", "A fresh leaf strip placed in strong salt solution wilts because its cells undergo",
     "plasmolysis", "photosynthesis", "osmotic bursting",
     "active transport", "A",
     "Water leaves the cells until the cytoplasm pulls from the wall."),

    # ------------------------------------------------------------------ cell division
    (T_DIV, "Medium", "Chromosomes line up along the equator of the cell during which stage of mitosis?",
     "Metaphase", "Prophase", "Anaphase", "Telophase", "A",
     "The metaphase plate forms before the chromatids separate."),
    (T_DIV, "Medium", "Human sperm and egg cells carry only half the usual number of chromosomes because they are made by",
     "meiosis", "mitosis", "budding", "binary fission", "A",
     "Meiosis halves the chromosome set for fertilisation."),
    (T_DIV, "Easy", "Mitosis splits one mother cell into two daughter cells that are",
     "genetically identical", "genetically different",
     "half the size", "without nuclei", "A",
     "Mitosis copies and shares the chromosomes exactly."),
    (T_DIV, "Hard", "The copying of DNA happens before a cell divides, during",
     "interphase", "metaphase", "cytokinesis", "anaphase", "A",
     "Replication is completed while the cell is still at interphase."),

    # -------------------------------------------------------------------- nutrition
    (T_NUT, "Easy", "The waxy cuticle of a leaf is waterproof. Stomata open mainly to let in",
     "carbon dioxide", "oxygen", "nitrogen",
     "water vapour", "A",
     "Carbon dioxide is the raw material for photosynthesis."),
    (T_NUT, "Medium", "A growing child whose meals lack vitamin D is likely to develop",
     "rickets", "night blindness", "beri-beri",
     "goitre", "A",
     "Vitamin D is needed for proper bone formation."),
    (T_NUT, "Medium", "Chewed bread soon tastes slightly sweet because saliva converts its starch into",
     "maltose", "glucose only", "amino acids",
     "fatty acids", "A",
     "Salivary amylase breaks starch to maltose sugar."),
    (T_NUT, "Hard", "Proteins must be fully digested into units small enough to enter the blood. These units are",
     "amino acids", "fatty acids", "vitamins",
     "sugars", "A",
     "Amino acids are the building blocks absorbed in the ileum."),
    (T_NUT, "Medium", "The inner wall of the small intestine is folded into millions of finger-like projections that hugely increase the surface area for",
     "absorption", "digestion of fats only",
     "breathing", "excretion", "A",
     "Villi give the ileum an enormous absorbing surface."),

    # --------------------------------------------------------------------- transport
    (T_TRAN, "Hard", "A ring of bark cut round a tree trunk eventually kills the roots because the cut removes the",
     "phloem", "xylem", "cambium",
     "cortex", "A",
     "Food made in the leaves can no longer reach the roots."),
    (T_TRAN, "Medium", "The heart chamber that pumps blood into the lungs is the",
     "right ventricle", "left ventricle", "right atrium",
     "left atrium", "A",
     "Deoxygenated blood leaves the right ventricle for the lungs."),
    (T_TRAN, "Easy", "Valves inside the heart and veins exist to prevent the",
     "backflow of blood", "clotting of blood",
     "loss of heat", "rise in pressure", "A",
     "One-way valves keep blood moving toward the heart."),
    (T_TRAN, "Medium", "Oxygen is carried in blood combined with a red pigment inside the red cells. The pigment is",
     "haemoglobin", "chlorophyll", "melanin",
     "plasma", "A",
     "Haemoglobin picks up oxygen in the lungs and releases it in tissues."),
    (T_TRAN, "Hard", "In an emergency, group O blood may be given to a group A patient because group O red cells",
     "carry neither A nor B antigens", "are smaller than others",
     "contain extra plasma", "carry both antigens", "A",
     "With no A or B antigens, group O is the universal donor."),

    # -------------------------------------------------------------------- respiration
    (T_RESP, "Medium", "Bread dough rises because yeast anaerobically produces",
     "carbon dioxide", "oxygen", "hydrogen",
     "nitrogen", "A",
     "Yeast fermentation releases carbon dioxide bubbles."),
    (T_RESP, "Medium", "After a long race a sprinter's leg muscles ache because of the build-up of",
     "lactic acid", "carbon dioxide", "alcohol",
     "urea", "A",
     "Short oxygen supply forces anaerobic respiration in muscles."),
    (T_RESP, "Easy", "The taking in of air into the lungs is called",
     "inhalation", "exhalation", "respiration",
     "diffusion", "A",
     "Inhalation draws fresh air over the gas surfaces."),
    (T_RESP, "Medium", "Oxygen and carbon dioxide are exchanged across the thin moist walls of tiny air sacs in the lungs called",
     "alveoli", "bronchi", "tracheae",
     "pleura", "A",
     "Alveoli provide a huge surface for gaseous exchange."),

    # ---------------------------------------------------------------------- excretion
    (T_EXC, "Hard", "Urine formation begins inside each kidney's million tiny filtering units, each called a",
     "nephron", "neuron", "alveolus",
     "villus", "A",
     "The nephron filters blood and shapes the urine."),
    (T_EXC, "Medium", "A patient whose kidneys have failed can have waste removed from the blood artificially by",
     "dialysis", "transfusion", "vaccination",
     "surgery", "A",
     "A dialysis machine filters the blood outside the body."),
    (T_EXC, "Medium", "The liver converts excess amino acids into a less poisonous waste that the kidneys remove. The waste is",
     "urea", "uric acid only", "carbon dioxide",
     "ammonia", "A",
     "Deamination in the liver produces urea."),
    (T_EXC, "Easy", "The skin, lungs, liver and kidneys are all organs of",
     "excretion", "digestion", "reproduction",
     "coordination", "A",
     "Each removes a specific waste from the body."),

    # ------------------------------------------------------------- reproduction/growth
    (T_REPRO, "Easy", "The anther and the filament together make up the male part of a flower, called the",
     "stamen", "carpel", "sepal",
     "corolla", "A",
     "Stamens bear the pollen-producing anthers."),
    (T_REPRO, "Medium", "Pollen transferred from the anther to the stigma of the same flower or plant is described as",
     "self-pollination", "cross-pollination", "fertilisation",
     "germination", "A",
     "Self-pollination keeps the pollen within one plant."),
    (T_REPRO, "Medium", "In a bean seed, the food the developing embryo draws on is stored in the",
     "cotyledons", "testa", "micropyle",
     "plumule", "A",
     "The seed leaves hold the starch store."),
    (T_REPRO, "Hard", "A seedling whose cotyledons are carried above the soil surface shows the type of germination called",
     "epigeal", "hypogeal", "viviparous",
     "dormant", "A",
     "Epigeal germination lifts the cotyledons into the light."),
    (T_REPRO, "Hard", "Identical twins are formed when",
     "one fertilised egg splits into two", "two eggs are released together",
     "one egg is fertilised twice", "twins always share a placenta", "A",
     "A single zygote dividing gives two identical embryos."),

    # ------------------------------------------------------------ support and movement
    (T_SUP, "Easy", "The longest and strongest bone in the human body is the",
     "femur", "humerus", "tibia",
     "radius", "A",
     "The thigh bone carries the body's weight."),
    (T_SUP, "Medium", "Tough strands that join bone to bone at a joint are called",
     "ligaments", "tendons", "muscles",
     "cartilages", "A",
     "Ligaments hold bones together at joints."),
    (T_SUP, "Medium", "The smooth fluid inside a freely moving joint serves mainly to",
     "reduce friction", "feed the bones",
     "remove wastes", "store calcium", "A",
     "Synovial fluid lets the joint surfaces glide."),
    (T_SUP, "Hard", "Hollow bones in birds are an adaptation for",
     "flight", "diving", "egg laying",
     "singing", "A",
     "Air spaces lighten the skeleton for flying."),

    # ----------------------------------------------------------------------- nervous
    (T_NERV, "Hard", "A nerve impulse crosses the tiny gap where one neuron meets another. The gap is the",
     "synapse", "dendrite", "axon",
     "node", "A",
     "Chemicals ferry the signal across the synapse."),
    (T_NERV, "Medium", "Snatching a hand away from a hot pot without thinking is coordinated in the",
     "spinal cord", "cerebrum", "cerebellum",
     "medulla", "A",
     "Reflex arcs pass through the spinal cord for speed."),
    (T_NERV, "Medium", "The part of the brain that maintains balance and posture is the",
     "cerebellum", "cerebrum", "medulla",
     "hypothalamus", "A",
     "The cerebellum fine-tunes movement and balance."),
    (T_NERV, "Easy", "In the eye, light is focused onto the retina by the",
     "lens", "cornea only", "iris",
     "optic nerve", "A",
     "The lens bends rays to a sharp image on the retina."),

    # ------------------------------------------------------------------------ hormones
    (T_HORM, "Medium", "A diabetic whose pancreas secretes too little insulin suffers because insulin normally lowers the level of",
     "blood sugar", "blood pressure", "body temperature",
     "blood volume", "A",
     "Insulin moves glucose from blood into cells."),
    (T_HORM, "Easy", "Adrenaline is produced by the",
     "adrenal glands", "thyroid gland", "pancreas",
     "pituitary gland", "A",
     "Adrenal glands sit above the kidneys."),
    (T_HORM, "Medium", "Doctors call the pituitary the master gland because it",
     "controls other glands", "digests hormones",
     "stores all hormones", "lies in the brain", "A",
     "Its messengers direct the other glands."),
    (T_HORM, "Hard", "A child who produces too much growth hormone grows abnormally tall, a condition called",
     "gigantism", "dwarfism", "goitre",
     "diabetes", "A",
     "Excess hormone before maturity over-stretches growth."),

    # ---------------------------------------------------------------------- genetics
    (T_GEN, "Hard", "Two carriers of sickle-cell trait (Ss) marry. The chance that a child inherits full sickle-cell disease (ss) is",
     "1 in 4", "1 in 2", "3 in 4",
     "every child", "A",
     "The Ss × Ss cross gives 1 SS : 2 Ss : 1 ss."),
    (T_GEN, "Medium", "A pea plant carries genes for both tallness and shortness but grows tall. Its visible height is called its",
     "phenotype", "genotype", "allele",
     "dominance", "A",
     "Phenotype is what can be seen or measured."),
    (T_GEN, "Medium", "A pea plant with genotype TT is described as",
     "homozygous dominant", "heterozygous", "homozygous recessive",
     "hybrid", "A",
     "Two identical dominant alleles make TT homozygous."),
    (T_GEN, "Hard", "A sudden change in the structure of a gene or chromosome is called a",
     "mutation", "migration", "selection",
     "segregation", "A",
     "Mutations introduce new heritable variations."),

    # ---------------------------------------------------------------------- ecology
    (T_ECO, "Medium", "In the chain grass → grasshopper → lizard → hawk, the hawk occupies the position of a",
     "tertiary consumer", "producer", "primary consumer",
     "decomposer", "A",
     "Third feeding level above the producer."),
    (T_ECO, "Hard", "A cattle egret pecking insects disturbed by grazing cows, neither helping nor harming them, illustrates",
     "commensalism", "mutualism", "parasitism",
     "predation", "A",
     "One partner gains while the other is unaffected."),
    (T_ECO, "Easy", "Bacteria and fungi that rot dead leaves return nutrients to the soil as",
     "decomposers", "producers", "herbivores",
     "predators", "A",
     "Decomposers recycle nutrients in the ecosystem."),
    (T_ECO, "Medium", "Water vapour cooling into cloud droplets is which stage of the water cycle?",
     "Condensation", "Evaporation", "Transpiration",
     "Precipitation", "A",
     "Cooling vapour condenses into droplets."),
    (T_ECO, "Medium", "The permanent clearing of natural forest cover is known as",
     "deforestation", "afforestation", "conservation",
     "rotation", "A",
     "Deforestation exposes the land and destroys habitats."),

    # ------------------------------------------------------------- diseases/immunity
    (T_DIS, "Easy", "Sleeping under an insecticide-treated net guards against malaria by blocking the bite of the",
     "female Anopheles mosquito", "tsetse fly", "housefly",
     "blackfly", "A",
     "Only the female Anopheles transmits malaria."),
    (T_DIS, "Medium", "Bleeding gums and slow-healing wounds in someone eating no fresh fruit point to a shortage of vitamin",
     "C", "A", "D",
     "K", "A",
     "Vitamin C keeps gums and tissues healthy."),
    (T_DIS, "Medium", "The immunity a person gains after recovering from a measles attack is",
     "natural active immunity", "natural passive immunity",
     "artificial active immunity", "artificial passive immunity", "A",
     "The body made its own antibodies from the infection."),
    (T_DIS, "Hard", "Antibiotics are ineffective against common colds because colds are caused by",
     "viruses", "bacteria", "fungi",
     "protozoa", "A",
     "Antibacterial drugs cannot touch viruses."),

    # ---------------------------------------------------------------------- practical
    (T_LAB, "Medium", "When first focusing a specimen under the microscope, you should begin with the",
     "low-power objective", "high-power objective",
     "mirror only", "fine adjustment only", "A",
     "Low power locates the specimen before magnifying it."),
    (T_LAB, "Hard", "A fruit-juice sample warmed with Benedict's solution gives a brick-red precipitate. The juice contains",
     "reducing sugar", "starch", "protein",
     "fat", "A",
     "Benedict's turns brick-red with reducing sugars."),
    (T_LAB, "Hard", "A food sample shaken with ethanol and poured into water gives a cloudy white emulsion, showing the presence of",
     "fats", "starch", "glucose",
     "protein", "A",
     "The emulsion test is the standard fat test."),
    (T_LAB, "Medium", "When preparing a wet mount, the thin slice of specimen is covered with a",
     "coverslip", "second slide", "drop of oil",
     "sheet of paper", "A",
     "The coverslip protects the lens and flattens the specimen."),
    (T_LAB, "Easy", "To measure the true length of a leaf in the laboratory, the most suitable instrument is a",
     "metre rule", "vernier caliper", "micrometer",
     "balance", "A",
     "A metre rule reads lengths to the nearest millimetre."),
]

build_batch(
    S,
    "batch_063_neco_biology2.json",
    "063",
    "NECO Biology top-up (round 2): grows the bank to 150 items so "
    "students get two full 60-question papers without repeats. Fresh "
    "scenario angles - mitochondria in muscle, cellulose crunch, RBC "
    "anucleate, plasmolysis, meiosis and gametes, villi absorption, "
    "phloem ringing, universal donor, lactic acid, nephron, dialysis, "
    "cotyledons, epigeal germination, identical twins, femur, synapse, "
    "cerebellum, gigantism, sickle-carrier cross, commensalism, treated "
    "nets, Benedict's and emulsion tests - near-dup scanned against the "
    "JAMB, WAEC and existing NECO banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
