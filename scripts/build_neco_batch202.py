"""Batch 202 - NECO Chemistry round 7 (NECO top-up, R40).

Grows NECO Chemistry from 231 toward ~256 with angles not yet in
the bank: the three states of matter; physical change; the
element and the molecule defined; the ion; the covalent bond; the
ionic bond; acids and bases defined; pH as a measure; valency;
molarity; the saturated solution; water of crystallisation;
efflorescence; caustic soda; hydrogen the lightest gas; neon
signs; helium balloons; soft water; monobasic acids; the alkali;
chromatography; sublimation; magnetic separation. Scanned against
the whole Chemistry pool (WAEC, NECO and JAMB stems, 1,461 items).

    python3 scripts/build_neco_batch202.py -> content/batch_202_neco_chem7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Chemistry"

T_MAT = "Matter and Its Properties"
T_STR = "Atoms, Elements and Compounds"
T_ACI = "Acids, Bases and Salts"
T_SOL = "Solutions and Separation"
T_APP = "Chemistry in Everyday Life"

PASSAGES = []
PQ = []

Q = [
    (T_MAT, "Easy", "The three states of matter are",
     "solid, liquid and gas", "solid, water and air",
     "element, compound and mixture", "metal, nonmetal and salt", "A",
     "Everything around us takes one of these forms."),
    (T_MAT, "Medium", "A change in which no new substance is formed, such as melting ice, is called",
     "a physical change", "a chemical change",
     "a nuclear reaction", "an irreversible change", "A",
     "The water remains water, only its shape changes."),
    (T_STR, "Easy", "A substance that cannot be split into simpler substances by chemical means is",
     "an element", "a compound",
     "a mixture", "a solution", "A",
     "Gold, oxygen and iron all stand alone."),
    (T_STR, "Medium", "The smallest particle of an element that can exist alone and still retain the element's properties is",
     "an atom", "an ion",
     "an electron", "a crystal", "A",
     "The building brick stops at the atom."),
    (T_STR, "Medium", "An atom that has lost or gained electrons and therefore carries a charge is",
     "an ion", "an isotope",
     "a molecule", "a neutron", "A",
     "Lost electrons leave a positive behind."),
    (T_STR, "Medium", "A covalent bond is formed between two atoms by",
     "the sharing of electrons", "the transfer of electrons",
     "the attraction of opposite charges only", "the release of neutrons", "A",
     "Each atom lends a share to the partnership."),
    (T_STR, "Medium", "An ionic bond is produced when one atom",
     "transfers electrons to another", "shares electrons equally",
     "attracts a neutron", "loses its nucleus", "A",
     "The metal gives; the nonmetal receives."),
    (T_STR, "Medium", "The combining power of an element, which decides how it bonds with others, is its",
     "valency", "atomic mass",
     "density", "reactivity series position", "A",
     "Sodium's single outer electron gives it one."),
    (T_ACI, "Easy", "A substance that turns blue litmus red and has a sour taste is",
     "an acid", "a base",
     "a salt", "an alkali", "A",
     "Vinegar and lemon juice answer the test."),
    (T_ACI, "Easy", "A substance that neutralises an acid to form salt and water is",
     "a base", "an acid",
     "an indicator", "a catalyst", "A",
     "Bases soothe the acid's sting."),
    (T_ACI, "Medium", "A base that dissolves in water to form an alkaline solution is called",
     "an alkali", "an acid salt",
     "an anhydride", "an amphoteric oxide", "A",
     "Caustic soda in water makes an alkali."),
    (T_ACI, "Medium", "An acid such as hydrochloric acid that can donate only one proton per molecule is described as",
     "monobasic", "dibasic",
     "tribasic", "polybasic", "A",
     "One hydrogen ion is all it has to give."),
    (T_ACI, "Medium", "The pH of a solution is a measure of the concentration of",
     "hydrogen ions in it", "oxygen dissolved in it",
     "salt dissolved in it", "its own weight", "A",
     "More hydrogen ions push the pH down."),
    (T_SOL, "Medium", "A solution that can dissolve no more solute at a particular temperature is said to be",
     "saturated", "concentrated",
     "dilute", "colloidal", "A",
     "The solvent has taken all it can hold."),
    (T_SOL, "Medium", "The concentration of a solution expressed in moles of solute per cubic decimetre of solution is its",
     "molarity", "molar mass",
     "density", "molality in grams", "A",
     "The chemist counts moles in every litre."),
    (T_SOL, "Medium", "A solid that separates out when a hot saturated solution is cooled is formed by",
     "crystallisation", "condensation",
     "sublimation", "evaporation only", "A",
     "Cooling forces the extra solute out as crystals."),
    (T_STR, "Hard", "The water molecules loosely attached to the crystals of some salts, as in washing soda, are called",
     "water of crystallisation", "water of hydration of gases",
     "moisture of deliquescence", "solution water", "A",
     "Gentle heating sets them free."),
    (T_STR, "Hard", "Crystals that lose their water of crystallisation to the dry air and become powder are said to be",
     "efflorescent", "deliquescent",
     "hygroscopic", "effervescent", "A",
     "The crystals bloom away into dust."),
    (T_SOL, "Hard", "The technique of separating the coloured substances in a dye using a solvent that carries them different distances is",
     "chromatography", "distillation",
     "decantation", "filtration", "A",
     "The colours race at different speeds."),
    (T_SOL, "Medium", "Mothballs left in a wardrobe slowly vanish without ever wetting the shelf. The change they undergo is",
     "sublimation", "condensation",
     "evaporation", "dissolution", "A",
     "The solid skips the liquid stage entirely."),
    (T_SOL, "Medium", "Iron filings mixed with sulphur powder are best separated by",
     "using a magnet", "filtering with paper",
     "boiling in water", "burning the mixture", "A",
     "The magnet picks its own out."),
    (T_APP, "Easy", "The common name of sodium hydroxide, used in making soap, is",
     "caustic soda", "washing soda",
     "baking soda", "table salt", "A",
     "Its burning touch earns the name caustic."),
    (T_APP, "Easy", "The lightest of all gases, once used to fill party balloons, is",
     "hydrogen", "oxygen",
     "nitrogen", "carbon(IV) oxide", "A",
     "Its tiny atom makes it featherlight."),
    (T_APP, "Easy", "The noble gas used to fill advertising signs, glowing red-orange when electrified, is",
     "neon", "argon",
     "helium", "krypton", "A",
     "The city's bright signs owe their glow to it."),
    (T_APP, "Medium", "The noble gas used to fill weather balloons and airships because it does not burn is",
     "helium", "neon",
     "argon", "radon", "A",
     "A safe lifter of balloons."),
    (T_APP, "Medium", "Water that easily forms lather with soap because it contains little dissolved calcium and magnesium is",
     "soft water", "hard water",
     "distilled brine", "heavy water", "A",
     "The soap bubbles freely in it."),
]

build_batch(
    S,
    "batch_202_neco_chem7.json",
    "202",
    "NECO Chemistry round 7 (R40 top-up): three states of matter; "
    "physical change; element, atom, ion and molecule defined; "
    "covalent and ionic bonds; valency; acid and base defined; "
    "alkali; monobasic; pH as hydrogen-ion measure; saturated "
    "solution; molarity; crystallisation; water of crystallisation; "
    "efflorescence; chromatography; sublimation; magnetic "
    "separation; caustic soda; hydrogen lightest; neon signs; "
    "helium balloons; soft water. Scanned against the whole "
    "Chemistry pool (WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
