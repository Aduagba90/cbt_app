"""Batch 170 - NECO Biology round 5 (NECO top-up, R32).

Grows NECO Biology from 189 toward ~226 with angles not yet in the
bank: the bacterium's missing nucleus; lysosomes; peristalsis;
hydrochloric acid; tooth decay's acid; roughage; platelets and
plasma; the diaphragm in breathing in; mucus in the windpipe; the
blind spot; rods for dim light; accommodation; ADH on the kidney;
progesterone; thyroxine; the ovule's fate and the ovary's fate
after fertilisation; wind-pollinated flowers; binary fission;
budding in yeast; cassava stem cuttings; the test cross; colour
blindness on the X; the phenotype; codominance in group AB; carbon
dioxide removed by photosynthesis; nitrogen fixation; energy
falling along the chain; habitat; kwashiorkor; measles droplets;
haustoria; gill filaments; the potometer; the control experiment.
Scanned against NECO rounds 1-4, WAEC Biology (all rounds) and the
JAMB pool.

    python3 scripts/build_neco_batch170.py -> content/batch_170_neco_bio5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Biology"

T_CEL = "Cell Structure and Organisation"
T_NUT = "Nutrition in Plants and Animals"
T_TRA = "Transport Systems"
T_RES = "Respiration and Gaseous Exchange"
T_NER = "Nervous Coordination and Sense Organs"
T_HOR = "Hormones and Chemical Coordination"
T_REP = "Reproduction and Growth"
T_GEN = "Genetics and Heredity"
T_ECO = "Ecology and Ecosystems"
T_DIS = "Food Tests and Diseases"
T_IMM = "Diseases and Immunity"
T_ADA = "Adaptation, Pollution and Conservation"
T_PRA = "Biology Practical Skills"

PASSAGES = []
PQ = []

Q = [
    (T_CEL, "Medium", "A bacterium differs from a plant cell mainly because it lacks",
     "a true nucleus", "a cell wall", "cytoplasm", "stored food granules", "A",
     "Its DNA lies free in the cytoplasm."),
    (T_CEL, "Easy", "Dissolved sugars, salts and pigments are stored in a plant cell's",
     "vacuole", "nucleus", "chloroplast", "cell wall", "A",
     "The vacuole's sap holds the cell's dissolved reserves."),
    (T_CEL, "Hard", "The organelles that hold powerful enzymes for digesting worn-out cell parts are the",
     "lysosomes", "ribosomes", "mitochondria", "chloroplasts", "A",
     "They serve as the cell's waste-disposal bags."),
    (T_NUT, "Easy", "The wave of muscular contractions that pushes swallowed food down the gullet is",
     "peristalsis", "digestion", "ingestion", "absorption", "A",
     "Ring muscles squeeze the food onward step by step."),
    (T_NUT, "Medium", "Hydrochloric acid in the stomach provides",
     "the acid medium gastric enzymes need", "the fat-digesting bile",
     "a passage for absorbed food", "the sweetness of the chyme", "A",
     "Pepsin works only in acid surroundings."),
    (T_NUT, "Easy", "Tooth decay begins when mouth bacteria feed on sugar and release",
     "acids that dissolve the enamel", "alkalis that coat the teeth",
     "sweet saliva in plenty", "harmless gases only", "A",
     "The acid slowly eats into the hardest coat."),
    (T_NUT, "Easy", "The part of a meal that helps move food along the intestines without being digested is",
     "roughage (fibre)", "protein", "vitamin C", "table salt", "A",
     "Fibre sweeps the canal clean as it passes."),
    (T_TRA, "Easy", "The blood cells that seal a wound by forming a clot are the",
     "platelets", "red blood cells", "white blood cells", "plasma cells", "A",
     "They patch the leak and stop the bleeding."),
    (T_TRA, "Easy", "Digested food, hormones and waste urea travel around the body dissolved in the blood's",
     "plasma", "red cells", "platelets", "haemoglobin", "A",
     "The liquid plasma carries the dissolved load."),
    (T_RES, "Medium", "Air rushes into the lungs during breathing in chiefly because",
     "the diaphragm flattens and the ribs rise", "the diaphragm domes upward",
     "the lungs themselves contract hard", "the nostrils widen at will", "A",
     "The enlarged chest cavity sucks air in."),
    (T_RES, "Easy", "The mucus and tiny hairs lining the windpipe chiefly",
     "trap dust and germs from inhaled air", "digest any swallowed food",
     "add moisture to the blood", "release enzymes for digestion", "A",
     "The sticky lining strains the incoming air."),
    (T_NER, "Medium", "The blind spot of the eye exists at the point where",
     "the optic nerve leaves the retina", "the cones are most tightly packed",
     "light is brought to focus", "the iris joins the cornea", "A",
     "No rods or cones stand at that exit point."),
    (T_NER, "Easy", "Seeing in dim light is done mainly by the",
     "rods", "cones", "optic nerve", "cornea", "A",
     "Rods answer weak light; cones need brightness for colour."),
    (T_NER, "Medium", "To focus on near and then distant objects, the eye changes",
     "the shape of the lens", "the width of the pupil",
     "the length of the eyeball", "the curve of the cornea", "A",
     "Ciliary muscles squeeze or relax the lens."),
    (T_HOR, "Medium", "The hormone that makes the kidney return more water to the blood is",
     "ADH (anti-diuretic hormone)", "adrenaline", "insulin", "thyroxine", "A",
     "More water is reabsorbed and the urine shrinks."),
    (T_HOR, "Medium", "The hormone that keeps the lining of the uterus prepared for a pregnancy is",
     "progesterone", "adrenaline", "insulin", "thyroxine", "A",
     "Progesterone maintains the womb's thick lining."),
    (T_HOR, "Easy", "Thyroxine, made from iodine, chiefly controls",
     "the body's rate of metabolism", "the clotting of blood",
     "the growth of bones only", "the digestion of fats", "A",
     "It sets the speed at which the body burns food."),
    (T_REP, "Easy", "A dormant maize grain sprouts when it is supplied with",
     "water, oxygen and warmth", "sunlight and dry air",
     "cold and darkness", "salt solution alone", "A",
     "Warm moisture and air wake the embryo."),
    (T_REP, "Easy", "After fertilisation, the ovary of a flower swells and becomes the",
     "fruit", "seed coat", "stigma", "receptacle", "A",
     "The ovary grows fleshy or dry around its seeds."),
    (T_REP, "Medium", "Flowers pollinated by wind usually carry",
     "small dull petals and feathery stigmas", "bright petals and sweet nectar",
     "heavy sticky pollen and scent", "large colourful bracts", "A",
     "Wind needs no colour, scent or nectar."),
    (T_REP, "Easy", "The asexual method by which one bacterium simply splits into two is",
     "binary fission", "budding", "conjugation", "spore formation", "A",
     "One cell divides plainly into two equal cells."),
    (T_REP, "Easy", "A yeast cell multiplies by growing a small bulge that later pinches off. This method is",
     "budding", "binary fission", "layering", "grafting", "A",
     "The bud swells, then breaks away as a new cell."),
    (T_REP, "Medium", "New cassava plants are commonly raised from stem cuttings planted in the soil. This is",
     "vegetative propagation", "sexual reproduction",
     "binary fission", "pollination by insects", "A",
     "A stem piece roots and grows into a new plant."),
    (T_GEN, "Hard", "To discover whether a tall pea plant is pure-bred or carries the dwarf allele, it is crossed with a dwarf plant. Such a cross is called a",
     "test cross", "reciprocal cross", "self-cross", "dihybrid cross", "A",
     "The dwarf parent exposes any hidden allele."),
    (T_GEN, "Hard", "Colour blindness appears more often in boys than girls because its gene lies on",
     "the X chromosome", "the Y chromosome",
     "chromosome pair number one", "the mitochondria", "A",
     "A boy's single faulty X has no partner to mask it."),
    (T_GEN, "Easy", "The outward appearance of an organism, such as tallness or red flowers, is its",
     "phenotype", "genotype", "gamete", "genus", "A",
     "What the eye sees is the phenotype."),
    (T_GEN, "Medium", "In blood group AB, both the A and the B antigen appear together on the red cells. This is a case of",
     "codominance", "complete dominance",
     "sex linkage", "independent assortment", "A",
     "Neither allele masks its partner."),
    (T_ECO, "Medium", "Carbon dioxide is removed from the atmosphere mainly through",
     "photosynthesis by green plants", "respiration by animals",
     "the burning of fuels", "the decay of organisms", "A",
     "Green plants lock the carbon into sugar."),
    (T_ECO, "Medium", "The conversion of free atmospheric nitrogen into nitrates that plants can use is called",
     "nitrogen fixation", "denitrification",
     "ammonification", "photosynthesis", "A",
     "Soil bacteria and lightning fix the gas."),
    (T_ECO, "Medium", "Along the members of a food chain, the energy available at each succeeding level",
     "decreases", "increases",
     "remains exactly constant", "doubles", "A",
     "Heat leaks away at every step of the chain."),
    (T_ECO, "Easy", "The natural place where an organism lives and feeds is called its",
     "habitat", "community", "population", "ecosystem", "A",
     "The habitat is the living thing's address."),
    (T_DIS, "Easy", "A child with a swollen belly, thin limbs and dull skin after a long shortage of protein in the diet suffers from",
     "kwashiorkor", "rickets", "goitre", "anaemia", "A",
     "Protein hunger swells the belly and thins the limbs."),
    (T_IMM, "Easy", "Measles passes from a sick child to a healthy playmate mainly through",
     "droplets from coughs and sneezes", "water drunk from a tap",
     "the bite of a mosquito", "eating undercooked meat", "A",
     "The cough sprays the virus into the air."),
    (T_ADA, "Hard", "Mistletoe and other parasitic plants draw food from their hosts through special suckers called",
     "haustoria", "root hairs", "stomata", "lenticels", "A",
     "The sucking organs pierce deep into the host."),
    (T_ADA, "Medium", "The thin-walled gill filaments of a fish are adapted chiefly for",
     "absorbing dissolved oxygen", "filtering food particles",
     "expelling excess salt", "grinding the food eaten", "A",
     "Blood flows close to the water across the thin wall."),
    (T_PRA, "Medium", "The apparatus used to measure the rate at which a leafy shoot loses water is the",
     "potometer", "respirometer", "barometer", "colorimeter", "A",
     "An air bubble races along as water leaves the shoot."),
    (T_PRA, "Easy", "In a well-planned experiment, the setup kept under exactly the same conditions as the test flask, minus the factor being investigated, is the",
     "control experiment", "repeat experiment",
     "field experiment", "blind experiment", "A",
     "Only the tested factor may differ between them."),
]

build_batch(
    S,
    "batch_170_neco_bio5.json",
    "170",
    "NECO Biology round 5 (R32 top-up): bacterial cell without a "
    "nucleus, vacuole's sap, lysosomes; peristalsis, HCl's acid "
    "medium, sugar-to-acid tooth decay, roughage; platelets and "
    "plasma; diaphragm and ribs in inspiration, mucus-lined "
    "windpipe; blind spot, rods for dim light, accommodation by the "
    "lens; ADH on kidney tubules, progesterone and the uterus "
    "lining, thyroxine and metabolism; ovule to seed, ovary to "
    "fruit, wind-pollinated flowers, binary fission, yeast budding, "
    "cassava cuttings; the test cross, colour blindness on the X, "
    "phenotype, codominance in group AB; CO2 removed by "
    "photosynthesis, nitrogen fixation, energy falling along the "
    "chain, habitat; kwashiorkor, measles by droplets; haustoria, "
    "gill filaments; the potometer, the control experiment. Scanned "
    "against NECO rounds 1-4, WAEC Biology (all rounds) and the "
    "JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
