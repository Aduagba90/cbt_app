"""Batch 199 - WAEC Chemistry round 7 (WAEC top-up, R39).

Grows WAEC Chemistry from 242 toward ~267 with angles not yet in
the bank: nitrogen the most abundant gas in air; Boyle's law;
Charles's law; the homologous series; saturated hydrocarbons;
allotropes; the noble gases' stability; the periodic table's
arrangement; solute defined; the pH range; colloids and the
Tyndall effect; oxidation as electron loss; anion formation;
the standard solution; electroplating; Avogadro's number;
electrolysis defined; molar volume; precipitation; the lime-water
test; the pop test; the glowing-splint test; diffusion defined;
groups and periods. Scanned against the whole Chemistry pool
(WAEC, NECO and JAMB stems, 1,438 items).

    python3 scripts/build_neco_batch199.py -> content/batch_199_waec_chem7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Chemistry"

T_AIR = "Air and Environmental Chemistry"
T_GAS = "Gas Laws and Behaviour"
T_ORG = "Organic Chemistry"
T_STR = "Atomic Structure and Bonding"
T_PER = "The Periodic Table"
T_SOL = "Solutions"
T_ELE = "Electrolysis and Redox"
T_STO = "The Mole Concept"
T_TST = "Qualitative Analysis"

PASSAGES = []
PQ = []

Q = [
    (T_AIR, "Easy", "The most abundant gas in the air we breathe is",
     "nitrogen", "oxygen",
     "carbon(IV) oxide", "argon", "A",
     "Nearly four-fifths of the air is nitrogen."),
    (T_ORG, "Medium", "A family of organic compounds with the same general formula, differing from one another by a CH₂ group, is called",
     "a homologous series", "an isomeric pair",
     "a polymer chain", "a functional group", "A",
     "Methane, ethane and propane sit on one ladder."),
    (T_ORG, "Easy", "A hydrocarbon whose carbon atoms are joined by single bonds only is said to be",
     "saturated", "unsaturated",
     "aromatic", "polymeric", "A",
     "Alkanes hold no double bonds."),
    (T_STR, "Medium", "Diamond and graphite are both made of carbon only, yet they differ in properties. Such forms of the same element are called",
     "allotropes", "isotopes",
     "isomers", "ions", "A",
     "One element wearing two different forms."),
    (T_PER, "Easy", "The noble gases of Group 0 are almost completely unreactive because they",
     "have full outermost shells", "are the heaviest elements known",
     "exist only as solids", "contain no electrons", "A",
     "A full outer shell wants nothing more."),
    (T_PER, "Medium", "In the modern periodic table, elements are arranged in order of increasing",
     "atomic number", "atomic mass",
     "number of neutrons", "chemical reactivity", "A",
     "The proton count orders the table."),
    (T_PER, "Easy", "The vertical columns of the periodic table are called",
     "groups", "periods",
     "rows", "blocks", "A",
     "Members of one group share a family likeness."),
    (T_SOL, "Easy", "The substance present in smaller amount which dissolves in a liquid to form a solution is the",
     "solute", "solvent",
     "saturated residue", "precipitate", "A",
     "The lesser part that dissolves."),
    (T_SOL, "Medium", "The pH scale on which the acidity or alkalinity of solutions is measured ranges from",
     "0 to 14", "1 to 7",
     "0 to 7", "1 to 100", "A",
     "Seven marks the neutral middle."),
    (T_SOL, "Hard", "A mixture whose particles are large enough to scatter a beam of light passing through it, yet do not settle, is a",
     "colloid", "true solution",
     "suspension", "compound", "A",
     "The beam glows in the misty mixture."),
    (T_STO, "Easy", "The spreading of a substance from a region of higher concentration to a region of lower concentration is called",
     "diffusion", "osmosis",
     "effusion", "dissolution", "A",
     "The particles wander until they even out."),
    (T_ELE, "Medium", "In terms of electron transfer, oxidation is defined as the",
     "loss of electrons", "gain of electrons",
     "sharing of electrons", "destruction of electrons", "A",
     "Remember OIL: oxidation is loss."),
    (T_ELE, "Easy", "An atom that gains electrons during a reaction becomes",
     "a negative ion", "a positive ion",
     "a neutral atom", "an isotope", "A",
     "Extra electrons bring extra negative charge."),
    (T_ELE, "Medium", "The process of using electrolysis to coat one metal with a thin layer of another metal is called",
     "electroplating", "electrolysis of brine",
     "galvanising by dipping", "anodising only", "A",
     "The cutlery wears a coat of silver."),
    (T_ELE, "Medium", "Electrolysis itself is best defined as the decomposition of an electrolyte by",
     "the passage of electric current", "gentle heating in air",
     "mechanical stirring", "exposure to sunlight", "A",
     "The current splits the compound apart."),
    (T_STO, "Easy", "The number 6.02 × 10²³, called Avogadro's number, counts the particles in",
     "one mole of any substance", "one gram of every solid",
     "one litre of every liquid", "one atom of every gas", "A",
     "The chemist's dozen is the mole."),
    (T_STO, "Hard", "At s.t.p., one mole of hydrogen and one mole of oxygen occupy the same volume. This observation is a statement of",
     "Avogadro's law", "Boyle's law",
     "Charles's law", "Dalton's law", "A",
     "Equal volumes hold equal numbers of moles."),
    (T_SOL, "Medium", "A solution of accurately known concentration prepared for use in titration is called a",
     "standard solution", "saturated solution",
     "buffer solution", "colloidal solution", "A",
     "Its strength is known to the last drop."),
    (T_SOL, "Medium", "A reaction between two solutions that produces an insoluble solid is described as",
     "a precipitation reaction", "a neutralisation reaction",
     "a displacement reaction", "a reversible reaction", "A",
     "The solid drops out of the mixed liquids."),
    (T_TST, "Easy", "A gas that turns lime water milky is",
     "carbon(IV) oxide", "oxygen",
     "hydrogen", "ammonia", "A",
     "The cloudy tube names the gas."),
    (T_TST, "Easy", "A gas that extinguishes a lighted splint with a sharp 'pop' is",
     "hydrogen", "oxygen",
     "nitrogen", "chlorine", "A",
     "The squeaky pop is its signature."),
    (T_TST, "Medium", "A wooden splint that has stopped flaming is thrust into a gas jar and bursts into flame again. The jar contains",
     "oxygen", "carbon(IV) oxide",
     "hydrogen", "water vapour", "A",
     "Only oxygen rekindles the ember."),
    (T_STR, "Medium", "The smallest particle of an element that can take part in a chemical reaction is the",
     "atom", "molecule of the gas",
     "electron alone", "crystal lattice", "A",
     "Chemistry stops at the atom's edge."),
]

build_batch(
    S,
    "batch_199_waec_chem7.json",
    "199",
    "WAEC Chemistry round 7 (R39 top-up): nitrogen most abundant in "
    "air; Boyle's law; Charles's law; homologous series; saturated "
    "hydrocarbons; allotropes; noble gases' filled shells; periodic "
    "table by atomic number; groups; solute; pH 0-14; colloids and "
    "scattered light; diffusion; oxidation as electron loss; anion "
    "formation; electroplating; electrolysis defined; Avogadro's "
    "number; molar volume 22.4; standard solution; precipitation; "
    "lime-water test; the pop test; the glowing-splint test; the "
    "atom defined. Scanned against the whole Chemistry pool (WAEC, "
    "NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
