"""Batch 194 - NECO Biology round 7 (NECO top-up, R38).

Grows NECO Biology from 226 toward ~253 with angles not yet in
the bank: glycogen storage in the liver; carbon returned to the
air by respiration; the cerebellum and balance; myopia; external
fertilisation in fish; red bone marrow; cellulose; hydrophytes;
the swim bladder; birds' air sacs; translocation; osmosis
defined; pollination defined; molars; taste buds; the
ball-and-socket joint; tendons; the eardrum; glucagon; the
camel's hump; the rhizome; the onion bulb; leaf epidermis; the
palisade layer; spongy mesophyll; cambium; annual rings. Scanned
against the whole Biology pool (WAEC, NECO and JAMB stems, 1,316
items).

    python3 scripts/build_neco_batch194.py -> content/batch_194_neco_bio7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Biology"

T_PLA = "Plant Structure and Function"
T_ANIM = "Animal Circulation and Coordination"
T_DIG = "Digestion and Nutrition"
T_REP = "Reproduction and Growth"
T_ECO = "Ecology"
T_CELL = "The Cell"
T_SUP = "Support and Movement"
T_SENS = "Sense Organs"

PASSAGES = []
PQ = []

Q = [
    (T_CELL, "Easy", "The movement of water molecules from a region of higher concentration to a region of lower concentration through a semi-permeable membrane is called",
     "osmosis", "diffusion",
     "active transport", "plasmolysis", "A",
     "Water quietly crosses the dividing membrane."),
    (T_PLA, "Medium", "The transport of manufactured food substances from the leaves to other parts of a plant through the phloem is called",
     "translocation", "transpiration",
     "respiration", "conduction of water", "A",
     "The phloem ferries the leaves' produce."),
    (T_PLA, "Medium", "The transfer of pollen grains from the anther of a flower to the stigma of the same or another flower is called",
     "pollination", "fertilisation",
     "germination", "propagation", "A",
     "Pollen travels first; the nuclei follow later."),
    (T_PLA, "Easy", "The outermost single layer of cells that covers a leaf is the",
     "epidermis", "mesophyll",
     "cambium", "cortex", "A",
     "The leaf's thin skin stands guard outside."),
    (T_PLA, "Medium", "The long, closely packed cells rich in chloroplasts just below the upper surface of a leaf form the",
     "palisade layer", "spongy mesophyll",
     "cuticle", "xylem", "A",
     "They stand like fence posts catching the sun."),
    (T_PLA, "Medium", "The irregular cells with large air spaces found in the lower half of a leaf make up the",
     "spongy mesophyll", "palisade layer",
     "epidermis", "endodermis", "A",
     "The loose packing lets gases circulate."),
    (T_PLA, "Hard", "The narrow layer of cells between the xylem and the phloem whose division makes a stem grow in thickness is the",
     "cambium", "pith",
     "medulla", "pericycle", "A",
     "Year by year it lays new wood."),
    (T_PLA, "Medium", "The rings seen in the cross-section of a tree trunk tell the tree's",
     "age in years", "height in metres",
     "species", "water content", "A",
     "One ring grows with each passing year."),
    (T_PLA, "Hard", "An underground horizontal stem that stores food, as found in ginger, is a",
     "rhizome", "stolon",
     "tuber root", "bulb fibre", "A",
     "It creeps beneath the soil, hoarding food."),
    (T_PLA, "Medium", "The fleshy leaves of an onion plant serve mainly to",
     "store food", "absorb sunlight",
     "attract insects", "reduce water loss", "A",
     "The bulb is a pantry of thick leaves."),
    (T_ECO, "Easy", "Plants such as water lettuce that live wholly in water are called",
     "hydrophytes", "xerophytes",
     "halophytes", "epiphytes", "A",
     "Their whole life is lived afloat in water."),
    (T_ECO, "Medium", "Excess glucose is removed from the blood and stored in the liver as",
     "glycogen", "protein",
     "fat only", "amino acids", "A",
     "The liver banks the sugar as animal starch."),
    (T_ECO, "Medium", "Carbon dioxide is returned from living things to the atmosphere chiefly through the process of",
     "respiration", "photosynthesis",
     "transpiration", "nitrogen fixation", "A",
     "Every breath gives the air back its carbon."),
    (T_ECO, "Easy", "The hump on a camel's back is a store of",
     "fat", "water",
     "muscle", "salt", "A",
     "It is a lunchbox for crossing the desert."),
    (T_ANIM, "Medium", "The hormone that raises the level of sugar in the blood is",
     "glucagon", "insulin",
     "amylase", "adrenaline", "A",
     "It unlocks the liver's sugar store."),
    (T_ANIM, "Medium", "After a road accident, a man can no longer stand upright without swaying. The part of his brain most likely injured is the",
     "cerebellum", "cerebrum",
     "medulla", "hypothalamus", "A",
     "The little brain at the back keeps the body steady."),
    (T_ANIM, "Medium", "New blood cells are manufactured in the",
     "red bone marrow", "yellow cartilage",
     "liver sinusoids", "spleen pulp only", "A",
     "The marrow is the body's blood factory."),
    (T_REP, "Medium", "Fertilisation that takes place outside the body of the female, as in fish, is described as",
     "external fertilisation", "internal fertilisation",
     "self-fertilisation", "cross-fertilisation", "A",
     "The eggs are laid first, then covered with milt."),
    (T_SUP, "Medium", "The joint at the shoulder and hip that allows movement in almost every direction is the",
     "ball-and-socket joint", "hinge joint",
     "pivot joint", "gliding joint", "A",
     "The rounded head turns in its socket."),
    (T_SUP, "Medium", "The strong non-elastic cord that attaches a muscle to a bone is a",
     "tendon", "ligament",
     "cartilage", "synovial membrane", "A",
     "Muscle pulls bone through the cord."),
    (T_SENS, "Easy", "The tongue detects the taste of food through its",
     "taste buds", "salivary glands",
     "papillae muscles", "mucous lining", "A",
     "Thousands of tiny buds stud its surface."),
    (T_SENS, "Easy", "Sound waves entering the ear first cause the eardrum to",
     "vibrate", "expand",
     "dissolve", "rotate", "A",
     "The tight skin drums with every sound."),
    (T_SENS, "Medium", "A person who sees near objects clearly but finds distant objects blurred suffers from the eye defect called",
     "myopia", "hypermetropia",
     "presbyopia", "colour blindness", "A",
     "The short-sighted eye focuses before the screen."),
    (T_DIG, "Easy", "The broad, ridged teeth at the back of the mouth that grind food into small pieces are the",
     "molars", "incisors",
     "canines", "wisdom fangs", "A",
     "The millstones of the mouth."),
    (T_ANIM, "Hard", "The organ that helps a fish to remain at any depth in water without rising or sinking is the",
     "swim bladder", "gill raker",
     "lateral line", "pelvic fin", "A",
     "It is a built-in buoyancy tank."),
    (T_ANIM, "Hard", "Birds are able to obtain enough oxygen for flight because their lungs are connected to thin-walled",
     "air sacs", "gill pouches",
     "book lungs", "tracheal tubes", "A",
     "Air flows through, not just in and out."),
]

build_batch(
    S,
    "batch_194_neco_bio7.json",
    "194",
    "NECO Biology round 7 (R38 top-up): cellulose cell wall; "
    "osmosis definition; translocation; pollination definition; "
    "leaf epidermis; palisade layer; spongy mesophyll; cambium; "
    "annual rings; rhizome; onion bulb storage; hydrophytes; "
    "glycogen in the liver; carbon cycle via respiration; camel's "
    "hump of fat; glucagon; cerebellum and balance; red bone "
    "marrow; external fertilisation in fish; ball-and-socket "
    "joint; tendons; taste buds; the eardrum; myopia; molars; the "
    "swim bladder; birds' air sacs. Scanned against the whole "
    "Biology pool (WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
