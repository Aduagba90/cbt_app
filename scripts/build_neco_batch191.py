"""Batch 191 - WAEC Biology round 7 (WAEC top-up, R37).

Grows WAEC Biology from 227 toward ~252 with angles not yet in
the bank: ribosomes; xylem; turgidity; the heart's four
chambers; capillary walls; pepsin; egestion; canine teeth; the
three vitamin-deficiency signs (scurvy, rickets, night
blindness); bilharzia's snail; ringworm's fungus; sex
determination; the food web; the tapeworm parasite; oil on a
pond; phototropism; Rhizopus spores; Spirogyra fragmentation;
the nine-month pregnancy; the motor neurone; the testa; enamel;
the plumule. Scanned against the whole Biology pool (WAEC, NECO
and JAMB stems, 1,291 items).

    python3 scripts/build_neco_batch191.py -> content/batch_191_waec_bio7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Biology"

T_CELL = "The Cell"
T_PLANT = "Plant Structure and Function"
T_ANIM = "Animal Circulation and Coordination"
T_DIG = "Digestion and Nutrition"
T_REP = "Reproduction and Growth"
T_GEN = "Genetics"
T_ECO = "Ecology"
T_HEALTH = "Health and Diseases"

PASSAGES = []
PQ = []

Q = [
    (T_PLANT, "Medium", "Water evaporating from the leaves pulls a continuous column of water up the xylem from the roots. This upward flow is the",
     "transpiration stream", "root pressure only",
     "capillary pond rise", "osmotic feed", "A",
     "The leaves' pull draws the whole column up."),
    (T_PLANT, "Medium", "Water and dissolved mineral salts travel up from the roots to the leaves of a plant through the",
     "xylem vessels", "phloem sieve tubes",
     "cambium cells", "cortex fibres", "A",
     "The woody vessels are the plant's pipes."),
    (T_PLANT, "Medium", "A herbaceous plant stands upright and firm without a woody stem because its cells are",
     "turgid", "flaccid",
     "plasmolysed", "rootless", "A",
     "Water pressure inside each cell props it up."),
    (T_PLANT, "Medium", "The bending of a green shoot towards light coming from one side is called",
     "phototropism", "geotropism",
     "hydrotropism", "thigmotropism", "A",
     "Growth speeds up on the shaded side."),
    (T_PLANT, "Medium", "The tough outer skin of a seed that shields the embryo within is the",
     "testa", "micropyle",
     "hilum", "pericarp", "A",
     "The seed's coat keeps out harm and dryness."),
    (T_PLANT, "Easy", "The part of a seed's embryo that grows upward to form the young shoot is the",
     "plumule", "radicle",
     "cotyledon", "aleurone", "A",
     "The plumule reaches for the sunlight."),
    (T_ANIM, "Easy", "How many chambers does the human heart have?",
     "4", "2",
     "3", "6", "A",
     "Two atria above and two ventricles below.", "4"),
    (T_ANIM, "Medium", "The exchange of oxygen, food and wastes between the blood and the surrounding cells takes place mainly in the",
     "capillaries", "arteries",
     "veins", "heart chambers", "A",
     "Their walls are one cell thick for easy passage."),
    (T_ANIM, "Medium", "The neurone that carries impulses from the brain or spinal cord out to a muscle or gland is a",
     "motor neurone", "sensory neurone",
     "relay neurone", "dendron", "A",
     "It delivers the command to act."),
    (T_DIG, "Medium", "The enzyme of the stomach that begins the digestion of protein is",
     "pepsin", "amylase",
     "trypsin", "lipase", "A",
     "It works in the stomach's acid bath."),
    (T_DIG, "Easy", "The pointed teeth used for piercing and tearing flesh are the",
     "canines", "incisors",
     "molars", "premolars", "A",
     "A dog grips its meat with them."),
    (T_DIG, "Easy", "The hardest substance in the human body, covering the crown of a tooth, is",
     "enamel", "dentine",
     "cement", "pulp", "A",
     "It shields the tooth but cannot regrow."),
    (T_DIG, "Easy", "The passing out of undigested food through the anus is called",
     "egestion", "excretion",
     "ingestion", "secretion", "A",
     "What the body cannot use leaves by the anus."),
    (T_DIG, "Medium", "Bleeding gums and wounds that heal slowly, in a person who eats no fresh fruit, point to a lack of vitamin",
     "C", "A",
     "D", "B1", "A",
     "Scurvy was the old sailors' disease."),
    (T_DIG, "Medium", "Soft, bent bones and bowed legs in a child kept indoors from sunlight point to a shortage of vitamin",
     "D", "A",
     "C", "K", "A",
     "Sunlight on the skin helps the body make it."),
    (T_DIG, "Hard", "A person who struggles to see in dim light after sunset may be lacking vitamin",
     "A", "C",
     "D", "B2", "A",
     "Night blindness follows its shortage."),
    (T_REP, "Medium", "A human pregnancy normally lasts about",
     "nine months", "six months",
     "three months", "twelve months", "A",
     "About 280 days from the last monthly flow."),
    (T_REP, "Medium", "The bread mould Rhizopus reproduces asexually by releasing",
     "spores", "seeds",
     "buds", "cuttings", "A",
     "Each tiny spore sprouts on damp bread."),
    (T_REP, "Hard", "A Spirogyra filament that breaks into pieces, each of which grows into a new plant, is reproducing by",
     "fragmentation", "binary fission",
     "budding", "spore formation", "A",
     "Every piece becomes a whole new weed."),
    (T_GEN, "Medium", "Whether a child is a boy or a girl is decided by the chromosome carried in the",
     "sperm of the father", "egg of the mother",
     "blood of the mother", "diet of the parents", "A",
     "The father's sperm bears either X or Y."),
    (T_ECO, "Easy", "Many interlinked food chains, forming a network of who-eats-whom in a habitat, make up a",
     "food web", "food chain",
     "energy pyramid", "niche", "A",
     "One predator may dine from several chains."),
    (T_ECO, "Medium", "A tapeworm living in the human intestine and absorbing the host's digested food is an example of a",
     "parasite", "saprophyte",
     "commensal", "mutual partner", "A",
     "It gives nothing back but harm."),
    (T_ECO, "Medium", "When an oil film covers the surface of a pond, the fish soon die because the oil",
     "blocks oxygen from the water", "sweetens the water for germs",
     "makes the water too cold", "sands the fishes' gills", "A",
     "Gills need the air the film shuts out."),
    (T_HEALTH, "Hard", "The blood fluke that causes bilharzia spends part of its life inside a",
     "water snail", "tsetse fly",
     "anopheles mosquito", "house fly", "A",
     "Wading in infested water lets it pierce the skin."),
    (T_HEALTH, "Medium", "Ringworm, which raises round itchy patches on the skin, is caused by a",
     "fungus", "virus",
     "bacterium", "roundworm", "A",
     "It feeds on the dead outer layer of skin."),
]

build_batch(
    S,
    "batch_191_waec_bio7.json",
    "191",
    "WAEC Biology round 7 (R37 top-up): ribosomes; xylem; turgid "
    "support; phototropism; testa; plumule; four heart chambers; "
    "capillary exchange; motor neurone; pepsin; canine teeth; "
    "enamel; egestion; vitamins C, D and A deficiency signs; "
    "nine-month pregnancy; Rhizopus spores; Spirogyra "
    "fragmentation; sex determination by the father's sperm; food "
    "web; tapeworm parasite; oil film on a pond; bilharzia water "
    "snail; ringworm fungus. Scanned against the whole Biology "
    "pool (WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
