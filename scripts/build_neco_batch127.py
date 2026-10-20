"""Batch 127 - NECO Biology round 4 (NECO top-up, Round 24).

Lifts NECO Biology from 150 toward ~195 with angles not yet in any
bank: the microscope, cell specialisation, aerobic and anaerobic
respiration, blood groups and transfusion, immunity, the skeleton and
joints, skin thermoregulation, eye defects and ear parts, endocrine
glands, tropisms, seed germination, ecological adaptation, pollution,
food tests, and diseases with their vectors. Scanned against NECO
rounds 1-3, WAEC Biology (all rounds) and the JAMB Biology pool.

    python3 scripts/build_neco_batch127.py -> content/batch_127_neco_bio4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Biology"

T_MIC = "Microscope and Tissues"
T_RESP = "Respiration and Immunity"
T_SKEL = "Skeleton, Skin and Senses"
T_HORM = "Hormones and Plants"
T_ECO = "Adaptation, Pollution and Conservation"
T_DIS = "Food Tests and Diseases"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- microscope and tissues
    (T_MIC, "Medium", "The part of the microscope that gathers light from the mirror is the",
     "objective lens", "eyepiece", "stage clip", "arm", "A",
     "It sits closest to the slide."),
    (T_MIC, "Hard", "With an eyepiece of x10 and an objective of x40, the total magnification is",
     "x400", "x50", "x4", "x4000", "A",
     "Multiply the two lens powers.", "10*40"),
    (T_MIC, "Hard", "To see a specimen in sharper focus under high power, first focus it under",
     "low power", "the mirror only", "closed eyes", "no light", "A",
     "Find it small, then zoom."),
    (T_MIC, "Medium", "A group of similar cells doing one job forms a",
     "tissue", "organ system", "community", "species", "A",
     "Muscle and blood are examples."),
    (T_MIC, "Medium", "Xylem and phloem together form a plant",
     "transport tissue", "storage tissue", "reproductive tissue", "covering tissue", "A",
     "Vascular bundles in the stem."),

    # ------------------------------------------------------------- respiration and immunity
    (T_RESP, "Medium", "Aerobic respiration releases energy using",
     "oxygen", "nitrogen", "carbon dioxide", "sunlight", "A",
     "It is air-fed and efficient."),
    (T_RESP, "Hard", "In yeast cells, anaerobic respiration yields ethanol and",
     "carbon dioxide", "oxygen", "lactic acid", "water only", "A",
     "Brewers thank this chemistry."),
    (T_RESP, "Medium", "The energy currency of the cell is",
     "ATP", "DNA", "RNA", "chlorophyll", "A",
     "Its phosphate bonds spend energy."),
    (T_RESP, "Medium", "People with blood group O can safely donate to groups A, B, AB and O, so they are called",
     "universal donors", "universal recipients", "agglutinated", "negative types", "A",
     "Their red cells lack A and B."),
    (T_RESP, "Hard", "A person with blood group AB can receive blood of any group, being a",
     "universal recipient", "universal donor", "carrier only", "rhesis-negative case", "A",
     "Both antigens sit on the cells."),
    (T_RESP, "Medium", "Immunity gained after recovering from measles is",
     "natural active immunity", "artificial passive immunity", "innate only", "borrowed immunity", "A",
     "The body built it itself."),
    (T_RESP, "Hard", "Antibodies passed through breast milk give the baby",
     "natural passive immunity", "artificial active immunity", "permanent immunity", "no immunity", "A",
     "Borrowed protection fades."),
    (T_RESP, "Medium", "Vaccination works by stimulating the body to produce",
     "antibodies", "antigens only", "red blood cells", "platelets alone", "A",
     "Memory cells patrol afterwards."),

    # ------------------------------------------------------------- skeleton, skin, senses
    (T_SKEL, "Medium", "The axial skeleton comprises the skull, vertebral column and",
     "rib cage", "limb bones", "finger bones", "shoulder girdle", "A",
     "The body's central pillar."),
    (T_SKEL, "Medium", "The joint at the shoulder that swings in many directions is a",
     "ball and socket joint", "hinge joint", "pivot joint", "fixed joint", "A",
     "The humerus head rolls in a cup."),
    (T_SKEL, "Hard", "Cartilage at the ends of bones chiefly",
     "reduces friction at joints", "makes blood cells", "digests food", "stores bile", "A",
     "Smooth pads glide together."),
    (T_SKEL, "Medium", "Sweat glands in the skin help to cool the body by",
     "evaporating sweat", "shivering", "growing hair", "making melanin", "A",
     "Each drop carries heat away."),
    (T_SKEL, "Hard", "Shivering warms the body because rapid muscle contractions",
     "release heat", "draw in cold air", "slow the blood", "burn melanin", "A",
     "Muscle work always makes heat."),
    (T_SKEL, "Medium", "Short-sightedness is corrected with a",
     "concave lens", "convex lens", "flat glass", "curved mirror", "A",
     "Distant objects focus too early."),
    (T_SKEL, "Hard", "The part of the ear that collects and directs sound waves is the",
     "pinna", "cochlea", "eardrum only", "stapes", "A",
     "The outer trumpet of the ear."),

    # ------------------------------------------------------------- hormones and plants
    (T_HORM, "Medium", "The thyroid gland needs iodine to make its hormone, which controls the rate of",
     "metabolism", "digestion only", "muscle twitch", "hair colour", "A",
     "Goitre follows its shortage."),
    (T_HORM, "Hard", "Adrenaline prepares the body for action by raising heartbeat and blood",
     "sugar", "pressure only", "flow to the gut", "platelet count", "A",
     "Fight or flight chemistry."),
    (T_HORM, "Medium", "When a shoot bends as it grows towards a lamp, the response is",
     "phototropism", "geotropism", "hydrotropism", "thigmotropism", "A",
     "Auxin piles on the dark side."),
    (T_HORM, "Medium", "Roots growing downward show",
     "positive geotropism", "negative phototropism only", "nastic movement", "tactic motion", "A",
     "Gravity guides the root tip."),
    (T_HORM, "Hard", "A sunflower head turning to track the sun is a",
     "nastic movement", "tropic bending", "reflex arc", "hormonal surge alone", "A",
     "Movement without direction growth."),

    # ------------------------------------------------------------- ecology, pollution, conservation
    (T_ECO, "Medium", "A xerophyte survives dry conditions by possessing",
     "thick cuticles and spines", "broad floating leaves", "air sacs", "shallow roots only", "A",
     "Cactus is the classic case."),
    (T_ECO, "Medium", "Hydrophytes like water lily float using",
     "air spaces in leaves and stems", "deep tap roots", "thick bark", "spines and hairs", "A",
     "They wear built-in life jackets."),
    (T_ECO, "Hard", "Eutrophication of a lake begins when excess nutrients cause",
     "algal blooms", "fish migration", "water boiling", "ice cover", "A",
     "The green carpet blocks light."),
    (T_ECO, "Medium", "Oil spillage in water kills fish chiefly by",
     "blocking gaseous exchange", "sweetening the water", "adding oxygen", "cooling the surface", "A",
     "Gills and air are cut off."),
    (T_ECO, "Medium", "The safest way to dispose of biodegradable household waste is",
     "composting", "open burning", "river dumping", "plastic bagging", "A",
     "The waste returns as manure."),
    (T_ECO, "Medium", "Afforestation helps conserve water mainly by",
     "holding soil and rain", "drying up rivers", "killing wildlife", "raising temperature", "A",
     "Trees are the water's friends."),

    # ------------------------------------------------------------- food tests and diseases
    (T_DIS, "Medium", "Iodine solution turns blue-black in the presence of",
     "starch", "glucose", "protein", "fat", "A",
     "It is the leaf test's colour."),
    (T_DIS, "Medium", "Glucose in a food sample is shown when Benedict's solution turns",
     "orange on warming", "blue on cooling", "violet at once", "milky white", "A",
     "Warm the mixture gently first."),
    (T_DIS, "Medium", "The violet colour in the biuret test indicates",
     "protein", "starch", "fat", "vitamin C", "A",
     "Egg white gives it richly."),
    (T_DIS, "Hard", "The Anopheles mosquito transmits",
     "malaria", "sleeping sickness", "yellow fever only", "river blindness", "A",
     "Only the female bites at night."),
    (T_DIS, "Medium", "The tsetse fly spreads the parasite that causes",
     "sleeping sickness", "malaria", "cholera", "tuberculosis", "A",
     "Cattle and humans both suffer."),
    (T_DIS, "Medium", "Cholera spreads mainly through contaminated",
     "water and food", "air droplets", "mosquito bites", "skin contact only", "A",
     "Clean wells guard the town."),
    (T_DIS, "Medium", "Tuberculosis is caused by a",
     "bacterium", "virus", "fungus", "protozoan", "A",
     "The cough that wastes the body."),
    (T_DIS, "Hard", "Ringworm, an athlete's foot infection, is caused by a",
     "fungus", "bacterium", "virus", "worm", "A",
     "Despite its name, no worm."),
]

build_batch(
    S,
    "batch_127_neco_bio4.json",
    "127",
    "NECO Biology round 4 (Round 24 top-up): objective lens and x400 "
    "magnification, low-power first focusing, tissues, vascular bundles, "
    "aerobic respiration, yeast's ethanol, ATP, universal donors and AB "
    "recipients, natural active and passive immunity, vaccination, axial "
    "skeleton, ball and socket joints, cartilage, sweat cooling, "
    "shivering heat, concave lens for myopia, the pinna, thyroid "
    "metabolism, adrenaline, phototropism and geotropism, nastic "
    "sunflowers, xerophytes and hydrophytes, eutrophication, oil "
    "spillage effects, composting, afforestation, iodine's blue-black, "
    "Benedict's orange, biuret violet, Anopheles, tsetse, cholera's "
    "water route, TB bacteria and fungal ringworm. Scanned against NECO "
    "rounds 1-3, WAEC Biology (all rounds) and the JAMB Biology pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
