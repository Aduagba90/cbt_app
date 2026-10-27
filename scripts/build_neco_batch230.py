"""Batch 230 - WAEC Chemistry round 9 (WAEC top-up, R47).

Grows WAEC Chemistry from 265 toward ~290 with angles verified
absent from the whole Chemistry pool (1,487 items across JAMB, WAEC
and NECO): diatomic elements; nitrogen fixation; superphosphate;
bleaching powder; Graham's law; basicity; solubility curve;
radical; water gas; producer gas; uranium; carbon dating; anomalous
expansion of water; compressibility of gases; chlor-alkali brine
products; Gay-Lussac combining volumes; roasting; calcination;
laboratory preparation of ammonia; kinetic theory of matter; red and
white phosphorus; desalination; vulcanisation; volumetric flask;
law of definite proportions. Checked and avoided (already banked):
potable water, ion-exchange softener, electrolytic refining,
allotropes (sulphur/carbon), Contact/Ostwald/Haber, cracking,
saponification, detergents, SO2/acid rain, ozone/CFC, flame tests,
galvanising/sacrificial, alloys (brass/bronze/solder/pig iron),
amphoteric, indicators, alum, deliquescence, drying agents,
anhydrous CuSO4, thermal decomposition, liquid-air fractionation,
isotopes, RAM, empirical formula, electronic configuration,
valency, metallic/dative bonding, electrolytes, strong/weak acids,
rusting, brine-discharge position, preferential discharge,
titration/end point, molarity, concentration, mole ratio,
percentage yield, limiting reagent, activation energy, collision
theory (option), Brownian, partial pressure, dry cell,
electrochemical series (option), hydrogen lightest, dinitrogen 78%,
noble-gas config, freezing/melting, evaporation, sublimation,
diffusion-fact items, oxidising/reducing agents, neutralisation,
salt types, electrode items, Faraday, electroplating, methane,
ethanol/esters/fermentation, functional group, hydrogenation,
reactivity series, ore definition, gangue, gypsum, baking/washing
soda, quicklime, hydrogen peroxide, gas collection methods,
sulphate/chloride tests, litmus colours, Fe/Al extraction,
monomer of rubber, water treatment with alum, hardness family,
Avogadro items, molar volume 22.4, combustion, physical/chemical
change, molten lead bromide, structural/molecular formula, charcoal
surface area, conservation of mass item.

    python3 scripts/build_neco_batch230.py -> content/batch_230_waec_chem9.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Chemistry"

T_NONMET = "Non-metals and Their Compounds"
T_ACID = "Acids, Bases and Solts" if False else "Acids, Bases and Salts"
T_SOL = "Solutions and Solubility"
T_ATOMIC = "Atomic Structure"
T_GAS = "Gas Laws"
T_ELEC = "Electrolysis"
T_MOLE = "Mole Concept and Stoichiometry"
T_METEX = "Metals and Extraction"
T_PART = "Particulate Nature of Matter"
T_WATER = "Water and Water Treatment"
T_ORG = "Organic Chemistry"
T_LAB = "Separation and Laboratory Techniques"

PASSAGES = []
PQ = []

Q = [
    (T_NONMET, "Easy", "Elements whose molecules normally exist as two atoms joined together, such as H₂, O₂, N₂ and Cl₂, are described as",
     "diatomic elements", "dihedral elements",
     "binary compounds", "divalent ions", "A",
     "Two identical atoms walk through chemistry hand in hand."),
    (T_NONMET, "Medium", "The conversion of atmospheric nitrogen into useful nitrogen compounds, whether by bacteria in root nodules or by industry, is called",
     "nitrogen fixation", "nitrogen fusion",
     "denitrification", "nitration of air", "A",
     "The free gas of the air is locked into compounds."),
    (T_NONMET, "Medium", "The fertiliser made by treating ground phosphate rock with sulphuric acid, so that the phosphorus becomes soluble and available to plants, is",
     "superphosphate", "sodium chloride",
     "slaked lime", "soda ash", "A",
     "The acid makes the rock's phosphorus drinkable."),
    (T_WATER, "Medium", "A white powder made by the action of chlorine on slaked lime, used to kill germs in treated water, is",
     "bleaching powder", "baking powder",
     "washing soda", "plaster of Paris", "A",
     "A little of it makes a well of water safe."),
    (T_GAS, "Hard", "The law stating that the rate of diffusion of a gas is inversely proportional to the square root of its density is",
     "Graham's law", "Boyle's law",
     "Charles' law", "Dalton's law", "A",
     "Light gases race where heavy gases crawl."),
    (T_ACID, "Easy", "The number of replaceable hydrogen atoms in one molecule of an acid is called its",
     "basicity", "basity",
     "alkalinity", "acidity value", "A",
     "HCl has one; H₂SO₄ has two."),
    (T_SOL, "Medium", "A graph plotting the mass of a salt dissolved by a saturated solution against temperature, showing how solubility rises or falls with heat, is called a",
     "solubility curve", "titration curve",
     "heating curve", "cooling graph", "A",
     "Each salt draws its own rising line."),
    (T_ATOMIC, "Easy", "An atom or group of atoms that carries an electric charge, such as NH₄⁺ or SO₄²⁻, is called a",
     "radical", "radicle",
     "reactant", "residue", "A",
     "It behaves as one unit through many reactions."),
    (T_NONMET, "Medium", "The gaseous fuel mixture of carbon(II) oxide and hydrogen, made by passing steam over white-hot coke, is",
     "water gas", "producer gas",
     "natural gas", "marsh gas", "A",
     "Steam and coke give a flame that burns hot."),
    (T_NONMET, "Medium", "The fuel gas mixture of carbon(II) oxide and nitrogen, made by passing air over hot coke, is",
     "producer gas", "water gas",
     "hydrogen gas", "butane gas", "A",
     "Air, not steam, feeds the glowing coke."),
    (T_ATOMIC, "Medium", "The radioactive metal whose atoms can be split in a reactor to release enormous energy is",
     "uranium", "aluminium",
     "sodium", "calcium", "A",
     "One kilogram of it holds a city's evening."),
    (T_ATOMIC, "Hard", "The method of finding the age of very old remains by measuring the amount of carbon-14 still left in them is called",
     "carbon dating", "carbon filtering",
     "carbon coating", "carbon printing", "A",
     "The clock of decay ticks inside the bone."),
    (T_PART, "Hard", "Between 0 °C and 4 °C, water behaves strangely: instead of getting denser as it cools, it expands slightly. This behaviour is called",
     "the anomalous expansion of water", "the ordinary contraction of water",
     "the boiling of water", "the freezing of brine", "A",
     "It is why ice floats and ponds keep their fish."),
    (T_PART, "Easy", "The property of gases that allows them to be squeezed into smaller containers, unlike solids and liquids, is their",
     "compressibility", "incompressibility",
     "rigidity", "fixed volume", "A",
     "The wide spaces between the particles give room."),
    (T_ELEC, "Medium", "When a concentrated solution of sodium chloride is electrolysed, the three main products are",
     "chlorine, hydrogen and sodium hydroxide", "oxygen, nitrogen and salt",
     "sodium, chlorine and water only", "hydrogen, oxygen and lime", "A",
     "Two electrodes, three valuable products."),
    (T_MOLE, "Hard", "The law stating that when gases react, the volumes of the reacting gases and the gaseous products bear simple whole-number ratios to one another is",
     "Gay-Lussac's law of combining volumes", "Avogadro's law of equal volumes",
     "Graham's law of diffusion", "the law of definite proportions", "A",
     "One volume plus two volumes gives two volumes of steam."),
    (T_METEX, "Medium", "The process of heating a sulphide ore strongly in excess air so that it is converted to the metal oxide is called",
     "roasting", "calcination",
     "smelting", "leaching", "A",
     "The ore meets the air and loses its sulphur."),
    (T_METEX, "Medium", "The process of heating a carbonate ore strongly in a limited supply of air, or none at all, so that it breaks down to the oxide is called",
     "calcination", "roasting",
     "reduction", "electrolysis", "A",
     "The carbonate lets its carbon dioxide escape."),
    (T_NONMET, "Hard", "In the laboratory, ammonia is prepared by gently heating a mixture of ammonium chloride and calcium hydroxide (slaked lime). The gas is collected by",
     "downward delivery, since it is lighter than air", "upward delivery, since it is heavier than air",
     "over water, like oxygen", "in a sealed jar with a tap at once", "A",
     "The light gas rises and pushes the air out below."),
    (T_PART, "Medium", "The theory which explains the behaviour of matter by picturing it as made of tiny particles in constant motion, with strong forces in solids and almost none in gases, is the",
     "kinetic theory of matter", "contact theory of matter",
     "valency theory of matter", "periodic theory of matter", "A",
     "Everything is particles, and the particles move."),
    (T_NONMET, "Medium", "Phosphorus exists in two common forms: one a yellow, poisonous, waxy solid that bursts into flame in air, and the other a red, safer powder used on match heads. These two forms are",
     "white and red phosphorus", "grey and green phosphorus",
     "blue and brown phosphorus", "soft and hard phosphorus", "A",
     "One must live under water; the other sits on the match."),
    (T_WATER, "Hard", "The process of removing dissolved salts from sea water to obtain fresh water, as done in some coastal desert cities, is called",
     "desalination", "decantation",
     "deliquescence", "decolourisation", "A",
     "The sea is persuaded to give up its salt."),
    (T_ORG, "Medium", "The process of heating raw rubber with sulphur to make it hard, elastic and durable enough for tyres is called",
     "vulcanisation", "polymerisation",
     "hydrogenation", "vulcanology", "A",
     "A little sulphur turns gum into tyre."),
    (T_LAB, "Medium", "The flat-bottomed flask with a long narrow neck, marked with a single line, used to prepare an exact volume of standard solution, is the",
     "volumetric flask", "conical flask",
     "round-bottomed flask", "filtering flask", "A",
     "Fill to the line and the volume is exact."),
    (T_MOLE, "Hard", "The law stating that a pure chemical compound always contains the same elements combined in the same fixed proportion by mass is the",
     "law of definite proportions", "law of multiple proportions",
     "law of conservation of mass", "law of reciprocal proportions", "A",
     "Water is always one to eight, anywhere on earth."),
]

build_batch(
    S,
    "batch_230_waec_chem9.json",
    "230",
    "WAEC Chemistry round 9 (R47 top-up): diatomic elements; "
    "nitrogen fixation; superphosphate; bleaching powder; Graham's "
    "law; basicity; solubility curve; radical; water gas; producer "
    "gas; uranium; carbon dating; anomalous expansion of water; "
    "compressibility; chlor-alkali products; Gay-Lussac's combining "
    "volumes; roasting; calcination; laboratory preparation of "
    "ammonia; kinetic theory; white and red phosphorus; "
    "desalination; vulcanisation; volumetric flask; law of definite "
    "proportions. Scanned against the whole Chemistry pool (JAMB, "
    "WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
