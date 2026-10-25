"""Batch 165 - NECO Chemistry round 5 (NECO top-up, R30).

Grows NECO Chemistry from 194 toward ~230 with angles not yet in the
bank: sublimation and centrifugation; gas diffusion speeds; Charles
law arithmetic; Q = It charge arithmetic; electroplating; Avogadro's
equal volumes; molar gas volume; basicity of acids; pH direction;
indicator colours; hygroscopic vs deliquescent; oxidising agents;
temperature and collision theory; catalysts of Haber and Contact;
halogen and alkali reactivity trends; electron transfer in NaCl;
diamond vs graphite; alkane general formula; addition vs
substitution; ethanol dehydration; hardness of water and its removal;
brass and steel; rusting conditions and galvanising; argon in bulbs;
oxygen from hydrogen peroxide. Numeric items carry verify strings
where the correct option's first number equals the value. Scanned
against NECO rounds 1-4, WAEC Chemistry (all rounds) and the JAMB
pool.

    python3 scripts/build_neco_batch165.py -> content/batch_165_neco_chem5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Chemistry"

T_SEP = "Separation Further"
T_GAS = "Gas Behaviour"
T_ELE = "Electrolysis Further"
T_MOL = "Mole Further"
T_ACI = "Acids, Bases and pH"
T_SALT = "Salts and Moisture"
T_RED = "Redox Further"
T_RATE = "Rates Further"
T_PER = "Periodic Trends Further"
T_BON = "Bonding Further"
T_ORG = "Organic Further"
T_WAT = "Water and Metals Further"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- separation
    (T_SEP, "Medium", "Iodine crystals heated in a closed dish change straight to vapour. The purification method that uses this is",
     "sublimation", "decantation", "centrifugation", "crystallisation", "A",
     "Solid becomes gas, then solid again."),
    (T_SEP, "Hard", "Separating fine clay particles suspended in water is quickest by",
     "centrifugation", "filtration through paper", "use of a magnet", "fractional distillation", "A",
     "The spinning drives them down."),

    # ------------------------------------------------------------- gas behaviour
    (T_GAS, "Hard", "Ammonia gas spreads faster than hydrogen chloride because ammonia",
     "has the lighter molecules", "is heavier than air", "is coloured deeply", "dissolves less in water", "A",
     "Its lighter feet simply run quicker."),
    (T_GAS, "Hard", "A gas occupies 300 cubic cm at 27 degrees Celsius. At constant pressure and 54 degrees Celsius it occupies",
     "327 cubic cm", "300 cubic cm", "600 cubic cm", "273 cubic cm", "A",
     "Charles law: volume follows kelvin.", "327"),
    (T_GAS, "Medium", "At constant temperature, raising the pressure on a fixed mass of gas",
     "reduces its volume", "raises its volume", "doubles its mass", "changes its colour", "A",
     "Crowding shrinks the space."),

    # ------------------------------------------------------------- electrolysis
    (T_ELE, "Hard", "A current of 2 amperes flowing for 30 seconds passes a charge of",
     "60 coulombs", "15 coulombs", "32 coulombs", "0.067 coulombs", "A",
     "Current times time in seconds.", "60"),
    (T_ELE, "Medium", "Electroplating a spoon with silver exists chiefly to",
     "beautify and protect it", "increase its weight for sale", "make it magnetic", "raise its melting point", "A",
     "A thin coat of lasting glory."),

    # ------------------------------------------------------------- mole
    (T_MOL, "Hard", "Equal volumes of different gases at the same temperature and pressure contain equal numbers of",
     "molecules", "atoms always", "ions", "electrons", "A",
     "Avogadro counted them equal."),
    (T_MOL, "Medium", "At standard conditions, one mole of any gas occupies about",
     "22.4 cubic decimetres", "2.24 cubic decimetres", "24,000 cubic decimetres", "1 cubic decimetre", "A",
     "The molar volume's famous figure.", "22.4"),
    (T_MOL, "Hard", "Using S 32, H 1 and O 16, the percentage by mass of sulphur in H2SO4 comes to",
     "32.7%", "16.3%", "65.3%", "32%", "A",
     "Thirty-two of the ninety-eight.", "32.7"),

    # ------------------------------------------------------------- acids & pH
    (T_ACI, "Hard", "Sulphuric acid, with two ionisable hydrogens per molecule, is described as",
     "dibasic", "monobasic", "tribasic", "amphoteric", "A",
     "Two protons wait to leave."),
    (T_ACI, "Medium", "On the pH scale, increasing acidity means the pH value",
     "falls towards zero", "rises towards fourteen", "stays at seven", "doubles always", "A",
     "Sour solutions count low."),
    (T_ACI, "Medium", "Phenolphthalein in an alkaline solution turns",
     "pink", "blue", "green", "colourless", "A",
     "A blush of strong base appears."),
    (T_ACI, "Medium", "Methyl orange in a strong acid shows",
     "red", "yellow", "blue", "purple", "A",
     "Sourness paints the indicator red."),

    # ------------------------------------------------------------- salts & moisture
    (T_SALT, "Hard", "A substance that absorbs moisture from the air without dissolving is",
     "hygroscopic", "deliquescent", "efflorescent", "hydrophobic", "A",
     "It drinks but keeps its shape."),
    (T_SALT, "Hard", "A solid that absorbs so much air moisture that it finally dissolves is",
     "deliquescent", "hygroscopic", "effervescent", "diamagnetic", "A",
     "It drinks itself into a puddle."),

    # ------------------------------------------------------------- redox
    (T_RED, "Hard", "In the laboratory, acidified potassium manganate (VII) is a standard",
     "oxidising agent", "reducing agent", "drying agent", "indicator", "A",
     "Its purple steal electrons."),
    (T_RED, "Medium", "Oxidation may be defined simply as the",
     "loss of electrons", "gain of electrons", "loss of protons", "sharing of electrons", "A",
     "Remember OIL: oxidation is loss."),

    # ------------------------------------------------------------- rates
    (T_RATE, "Hard", "Warming reactants speeds the reaction because the particles",
     "collide more often and harder", "shrink in size", "change colour", "become lighter", "A",
     "Extra heat quickens the particle dance."),
    (T_RATE, "Medium", "In the plant where nitrogen and hydrogen unite into ammonia, the reaction is hurried along by",
     "promoted iron", "vanadium (V) oxide", "platinum alone", "nickel wire", "A",
     "Promoted iron does the work."),
    (T_RATE, "Hard", "Sulphur dioxide waits on a catalyst bed before oxygen will bind it into the trioxide. That catalyst is",
     "vanadium (V) oxide", "iron filings", "copper turnings", "manganese dioxide", "A",
     "V2O5 shuttles the oxygen."),

    # ------------------------------------------------------------- periodic trends
    (T_PER, "Hard", "Down the halogen group, reactivity",
     "decreases", "increases", "remains constant", "first rises then vanishes", "A",
     "Fluorine is fiercest at the top."),
    (T_PER, "Hard", "Down group one, the alkali metals become",
     "more reactive", "less reactive", "unreactive at once", "gaseous", "A",
     "The outer electron leaves more easily."),

    # ------------------------------------------------------------- bonding
    (T_BON, "Hard", "In forming sodium chloride, each sodium atom",
     "donates one electron to chlorine", "accepts one electron from chlorine", "shares two electrons", "loses its nucleus", "A",
     "Cation meets anion, and they wed."),
    (T_BON, "Hard", "Diamond is harder than graphite because its carbon atoms",
     "form a rigid three-dimensional network", "lie in sliding flat layers", "are loosely packed", "carry free electrons", "A",
     "Every bond locks in place."),
    (T_BON, "Medium", "A pencil core closes a circuit that a diamond cannot. The pencil's graphite manages this because it",
     "loses mobile electrons", "is black in colour", "weighs more per atom", "contains trapped hydrogen", "A",
     "One electron per carbon roams."),

    # ------------------------------------------------------------- organic
    (T_ORG, "Medium", "The general formula of the alkane family is",
     "CnH2n+2", "CnH2n", "CnH2n-2", "CnHn", "A",
     "Saturated chains walk by it."),
    (T_ORG, "Hard", "Ethene reacting with bromine water is an example of",
     "addition reaction", "substitution reaction", "neutralisation", "esterification", "A",
     "The double bond opens its arms."),
    (T_ORG, "Hard", "Passing ethanol over hot aluminium oxide produces",
     "ethene", "ethane", "ethanoic acid", "ethanol itself", "A",
     "Water is stripped from the alcohol."),
    (T_ORG, "Medium", "Soaps in hard water form scum because of the dissolved",
     "calcium and magnesium salts", "oxygen and nitrogen", "sodium chloride", "organic acids", "A",
     "The ions choke the lather."),

    # ------------------------------------------------------------- water & metals
    (T_WAT, "Hard", "Temporary hardness of water, caused by hydrogencarbonates, is removed by simple",
     "boiling", "filtering", "freezing", "stirring", "A",
     "Heat breaks the guilty salts."),
    (T_WAT, "Hard", "Permanent hardness survives boiling and yields only to methods like adding",
     "washing soda", "table salt", "vinegar", "ice", "A",
     "The soda precipitates the culprits."),
    (T_WAT, "Medium", "The alloy made of copper and zinc is",
     "brass", "steel", "bronze", "duralumin", "A",
     "Trumpets and door handles wear it."),
    (T_WAT, "Medium", "Iron rusts only when BOTH water and",
     "oxygen", "nitrogen", "carbon dioxide", "argon", "A",
     "are present together on the metal."),
    (T_WAT, "Medium", "Roofing sheets stay rust-free for years because their iron is dipped in molten zinc. The process is",
     "galvanising", "electrolysis of iron", "tempering", "annealing", "A",
     "The zinc sacrifices itself first."),
    (T_WAT, "Medium", "Argon fills electric bulbs because it is",
     "chemically inert", "cheap and colourful", "a good fuel", "heavier than iron", "A",
     "The filament glows unburnt."),
    (T_WAT, "Hard", "In the laboratory, oxygen is conveniently prepared by decomposing hydrogen peroxide over",
     "manganese (IV) oxide", "iron filings", "common salt", "copper wire", "A",
     "The black powder speeds the split."),
]

build_batch(
    S,
    "batch_165_neco_chem5.json",
    "165",
    "NECO Chemistry round 5 (R30 top-up): sublimation of iodine, "
    "centrifuging clay; ammonia outruns HCl; Charles law 327 cubic cm; "
    "pressure-volume crowd; Q = It 60 coulombs; electroplating purpose; "
    "Avogadro equal volumes; 22.4 molar volume; 35% nitrogen in "
    "NH4NO3; dibasic sulphuric; pH falls with acidity; phenolphthalein "
    "pink, methyl orange red; hygroscopic vs deliquescent; KMnO4 "
    "oxidiser; oxidation as electron loss; collision theory warming; "
    "iron in Haber, V2O5 in Contact; halogens down less reactive, "
    "alkalis down more; sodium donates; diamond network vs graphite "
    "layers; CnH2n+2; addition with bromine; ethanol to ethene; scum "
    "from calcium; temporary vs permanent hardness; brass; rust needs "
    "oxygen; galvanising; argon bulbs; H2O2 over MnO2. Scanned against "
    "NECO rounds 1-4, WAEC Chemistry (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
