"""Batch 062 - NECO Chemistry top-up (round 2).

Grows the Chemistry bank from 88 to 150 items so students get two full
practice papers without repeats. New angles: sublimation, electron
configuration, valency and radicals, molar mass calculations, brine
electrolysis, flame tests, separation techniques, diamond/graphite,
rusting prevention, alloys, alkenes, esterification. Numeric answers
machine-verified. Near-dup scanned against JAMB, WAEC and the existing
NECO bank.

    python3 scripts/build_neco_batch62.py -> content/batch_062_neco_chemistry2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Chemistry"

T_PART = "Particulate Nature of Matter"
T_ATOM = "Atomic Structure and Periodicity"
T_BOND = "Chemical Bonding"
T_STO = "Stoichiometry and Calculations"
T_ELEC = "Electrolysis"
T_ACID = "Acids, Bases and Salts"
T_WATER = "Water and Air"
T_RATE = "Rates of Reaction and Equilibrium"
T_ENER = "Energy Changes"
T_ORG = "Organic Chemistry"
T_METAL = "Metals and Their Compounds"
T_LAB = "Practical Chemistry"

PASSAGES = []
PQ = []

Q = [
    # --------------------------------------------------------- particulate (5)
    (T_PART, "Easy", "The change of state directly from solid to vapour without melting is called",
     "sublimation", "condensation", "evaporation",
     "freezing", "A",
     "Camphor and iodine sublime on gentle warming."),
    (T_PART, "Medium", "Camphor kept in an open dish slowly disappears because it",
     "sublimes into vapour", "melts into liquid",
     "dissolves in air", "reacts with oxygen", "A",
     "The solid passes straight to gas at room temperature."),
    (T_PART, "Easy", "The state of matter with a fixed shape and volume is the",
     "solid", "liquid", "gas",
     "plasma", "A",
     "Strong forces hold solid particles in place."),
    (T_PART, "Medium", "Boiling differs from evaporation because boiling occurs",
     "throughout the liquid at a fixed temperature", "only at the surface at any temperature",
     "only in closed vessels", "without heat energy", "A",
     "Bubbles form everywhere in the bulk liquid at the boiling point."),
    (T_PART, "Medium", "Gases can be compressed easily because their particles",
     "are far apart", "are tightly packed",
     "have no mass", "are charged", "A",
     "The large empty spaces between gas particles take the pressure."),

    # ------------------------------------------------- atomic structure (6)
    (T_ATOM, "Easy", "The number of protons in an atom is its",
     "atomic number", "mass number", "nucleon number",
     "relative mass", "A",
     "The proton count identifies the element."),
    (T_ATOM, "Medium", "An atom with electron configuration 2, 8, 7 belongs to Group",
     "17 (seven)", "1 (one)", "2 (two)",
     "8 (eight)", "A",
     "Seven outer-shell electrons place it among the halogens."),
    (T_ATOM, "Medium", "An atom has atomic number 11. The arrangement of its electrons is",
     "2, 8, 1", "2, 9", "8, 2, 1",
     "2, 8, 2", "A",
     "Eleven electrons fill the shells as 2, 8, 1."),
    (T_ATOM, "Medium", "The chemical resemblance shown by elements of the same periodic group comes from their equal number of",
     "outer-shell electrons", "neutrons", "shells",
     "nucleons", "A",
     "Outer electrons govern the chemical family behaviour."),
    (T_ATOM, "Hard", "Going down Group 1, the atoms become",
     "larger and more reactive", "smaller and less reactive",
     "larger and less reactive", "smaller and more reactive", "A",
     "The outer electron is farther from the nucleus and lost more easily."),
    (T_ATOM, "Medium", "Argon is unreactive because its outermost shell is",
     "completely filled", "half filled", "empty",
     "odd numbered", "A",
     "A full outer shell leaves no drive to react."),

    # ------------------------------------------------------------ bonding (5)
    (T_BOND, "Medium", "The bond found in solid sodium chloride is",
     "ionic", "covalent", "metallic",
     "hydrogen", "A",
     "Electrons transferred from sodium to chlorine form ions."),
    (T_BOND, "Medium", "The ability of an atom to combine is determined by its",
     "valency", "density", "colour",
     "smell", "A",
     "Valency counts the bonds an atom can form."),
    (T_BOND, "Hard", "The formula of calcium chloride, using the valencies of calcium and chlorine, is",
     "CaCl2", "CaCl", "Ca2Cl",
     "CaCl3", "A",
     "Two chloride ions balance one doubly charged calcium ion."),
    (T_BOND, "Medium", "The bond that holds copper atoms together in a copper wire is",
     "metallic", "ionic", "covalent",
     "dative", "A",
     "A sea of delocalised electrons glues the metal ions."),
    (T_BOND, "Hard", "Diamond fails to conduct electricity because each carbon's outer electrons are",
     "locked in covalent bonds", "free to move about",
     "transferred to ions", "shared with metals", "A",
     "Every outer electron is held between two nuclei."),

    # ------------------------------------------------------ stoichiometry (6)
    (T_STO, "Easy", "The molar mass of water, H₂O, in g/mol is",
     "18", "16", "20",
     "17", "A",
     "Two hydrogens (1 each) plus oxygen 16 gives 18.",
     "2*1+16"),
    (T_STO, "Medium", "The molar mass of calcium carbonate, CaCO₃, in g/mol is",
     "100", "88", "84",
     "116", "A",
     "Calcium 40, carbon 12 and three oxygens 48 total 100.",
     "40+12+3*16"),
    (T_STO, "Medium", "The number of moles present in 36 g of water is",
     "2", "18", "0.5",
     "36", "A",
     "Moles equal mass divided by molar mass: 36/18.",
     "36/18"),
    (T_STO, "Medium", "The mass, in grams, of 0.5 mol of carbon dioxide, CO₂, is",
     "22", "44", "11",
     "88", "A",
     "Half of the molar mass 44 is 22 g.",
     "0.5*44"),
    (T_STO, "Hard", "The percentage of calcium in CaCO₃ is",
     "40", "12", "48",
     "50", "A",
     "Calcium's 40 out of the molar mass 100 is 40 per cent.",
     "40/100*100"),
    (T_STO, "Hard", "A solution contains 0.2 mol of solute in 500 cm³ of solution. Its concentration, in mol/dm³, is",
     "0.4", "0.2", "0.1",
     "100", "A",
     "Concentration = moles × 1000 ÷ volume = 0.2 × 1000/500.",
     "0.2*1000/500"),

    # -------------------------------------------------------- electrolysis (5)
    (T_ELEC, "Easy", "During electrolysis, oxidation of ions takes place at the",
     "anode", "cathode", "neutral electrode",
     "reference electrode", "A",
     "Anode oxidation is the standard memory aid 'an-ox'."),
    (T_ELEC, "Medium", "In the electrolysis of brine (concentrated sodium chloride solution), the gas released at the anode is",
     "chlorine", "hydrogen", "oxygen",
     "nitrogen", "A",
     "Chloride ions discharge in preference to hydroxide."),
    (T_ELEC, "Medium", "Electroplating an object with silver makes the object the",
     "cathode", "anode", "electrolyte",
     "power source", "A",
     "The object to be plated attracts the metal ions as cathode."),
    (T_ELEC, "Medium", "Electrolytic refining of impure copper uses the impure copper as the",
     "anode", "cathode", "salt bridge",
     "voltmeter", "A",
     "Pure copper deposits on the cathode as the anode dissolves."),
    (T_ELEC, "Hard", "A molten ionic compound conducts electricity because on melting its ions become",
     "free to move", "electrically neutral",
     "converted to atoms", "frozen", "A",
     "Mobile charged particles carry the current."),

    # --------------------------------------------------------- acids/bases (6)
    (T_ACID, "Easy", "The colour of litmus paper in an acidic solution is",
     "red", "blue", "green",
     "yellow", "A",
     "Acids turn blue litmus red."),
    (T_ACID, "Medium", "Methyl orange indicator turns yellow in a solution whose pH is greater than",
     "4.4", "7.0", "2.0",
     "9.0", "A",
     "Above its transition range methyl orange shows yellow."),
    (T_ACID, "Medium", "Sulphuric acid is described as dibasic because each molecule can release",
     "two hydrogen ions", "one hydrogen ion", "three hydrogen ions",
     "no hydrogen ion", "A",
     "Both hydrogens can be replaced by metal ions."),
    (T_ACID, "Easy", "The salt formed when hydrochloric acid reacts with sodium hydroxide is",
     "sodium chloride", "sodium sulphate", "sodium nitrate",
     "sodium carbonate", "A",
     "Hydrochloric acid always gives chlorides."),
    (T_ACID, "Medium", "Blue copper(II) sulphate crystals turn white on heating because they lose their",
     "water of crystallisation", "copper ions",
     "sulphur atoms", "blue colour only", "A",
     "Heating drives off the bound water molecules."),
    (T_ACID, "Medium", "An acid that ionises completely in water is described as a",
     "strong acid", "weak acid", "dilute acid",
     "organic acid", "A",
     "Complete ionisation marks strong acids like HCl."),

    # -------------------------------------------------------- water and air (5)
    (T_WATER, "Easy", "The gas mainly responsible for the greenhouse effect in the atmosphere is",
     "carbon dioxide", "nitrogen", "oxygen",
     "argon", "A",
     "CO₂ traps outgoing heat from the earth."),
    (T_WATER, "Medium", "Bulb makers fill lamps with argon rather than air because argon is",
     "chemically inert", "very light", "cheap to make",
     "coloured", "A",
     "The noble gas does not react with the hot filament."),
    (T_WATER, "Medium", "Helium rather than hydrogen is used in party balloons because helium is",
     "non-flammable", "heavier than air", "cheaper",
     "easier to make", "A",
     "Helium cannot burn, unlike hydrogen."),
    (T_WATER, "Easy", "Water that is safe for drinking is described as",
     "potable", "distilled always", "hard water",
     "sea water", "A",
     "Potable water is clean and wholesome."),
    (T_WATER, "Medium", "The chlorine added to municipal water works mainly to",
     "kill germs", "add taste", "soften it",
     "colour it", "A",
     "Chlorination destroys disease-causing organisms."),

    # ------------------------------------------------- rates and equilibrium (6)
    (T_RATE, "Easy", "A substance that alters the rate of a reaction but remains unchanged at the end is a",
     "catalyst", "reactant", "product",
     "solvent", "A",
     "Catalysts speed reactions without being consumed."),
    (T_RATE, "Medium", "Enzymes are best described as biological",
     "catalysts", "acids", "salts",
     "solvents", "A",
     "They speed body reactions at mild temperatures."),
    (T_RATE, "Medium", "Powdering a solid reactant speeds the reaction because it increases the",
     "surface area for collisions", "concentration of the solution",
     "temperature", "pressure", "A",
     "More exposed surface means more fruitful collisions."),
    (T_RATE, "Medium", "Increasing the pressure on a gaseous reaction increases the rate mainly because the",
     "particles collide more often", "particles become heavier",
     "activation energy rises", "catalyst works harder", "A",
     "Crowding the particles raises the collision frequency."),
    (T_RATE, "Hard", "Which catalyst speeds the synthesis of ammonia in the Haber process?",
     "iron", "platinum", "copper",
     "nickel only", "A",
     "Finely divided iron catalyses ammonia synthesis."),
    (T_RATE, "Medium", "When the forward and backward reactions occur at the same rate, the system is at",
     "equilibrium", "completion", "standstill",
     "overflow", "A",
     "Concentrations stay constant though both reactions continue."),

    # -------------------------------------------------------- energy changes (4)
    (T_ENER, "Easy", "Heat is released to the surroundings in a reaction that is",
     "exothermic", "endothermic", "isothermal",
     "adiabatic", "A",
     "Combustion releases heat as it proceeds."),
    (T_ENER, "Medium", "The dissolution of ammonium chloride in water causes the container to feel cold. The process is",
     "endothermic", "exothermic", "neutral",
     "explosive", "A",
     "Heat absorbed from the surroundings cools the vessel."),
    (T_ENER, "Medium", "Burning of petrol in a car engine is an example of an",
     "exothermic reaction", "endothermic reaction", "reversible change",
     "physical change", "A",
     "Energy released as heat and light drives the engine."),
    (T_ENER, "Hard", "The minimum energy that colliding particles must possess for a reaction to occur is the",
     "activation energy", "kinetic energy only",
     "lattice energy", "ionisation energy", "A",
     "Below this threshold collisions bounce off unchanged."),

    # ---------------------------------------------------- organic chemistry (6)
    (T_ORG, "Easy", "The family name of the series with general formula CnH₂n is the",
     "alkenes", "alkanes", "alkynes",
     "alcohols", "A",
     "One double bond leaves two hydrogens per carbon short."),
    (T_ORG, "Medium", "Bromine water is decolourised by ethene because ethene undergoes",
     "an addition reaction", "a substitution reaction",
     "a neutralisation", "combustion", "A",
     "Bromine adds across the double bond."),
    (T_ORG, "Medium", "The two structural isomers of butane differ in the",
     "arrangement of their atoms", "number of carbons",
     "molar mass", "reactivity with water", "A",
     "Same formula, different skeleton."),
    (T_ORG, "Medium", "Ethanol can be produced industrially by the fermentation of",
     "glucose", "proteins", "fats",
     "common salt", "A",
     "Yeast converts sugars to ethanol and carbon dioxide."),
    (T_ORG, "Medium", "Ethanoic acid, the sour component of vinegar, is formed when ethanol is",
     "oxidised", "reduced", "polymerised",
     "dehydrated", "A",
     "Exposure to air oxidises ethanol to the acid."),
    (T_ORG, "Hard", "The sweet-smelling product of the reaction between an organic acid and an alcohol is an",
     "ester", "ether", "alkane",
     "amide", "A",
     "Esterification links acid and alcohol into an ester."),

    # -------------------------------------------------- metals and compounds (7)
    (T_METAL, "Easy", "Gold occurs naturally in the uncombined state because it is",
     "very unreactive", "very heavy", "very cheap",
     "magnetic", "A",
     "Low reactivity keeps gold native in the ground."),
    (T_METAL, "Medium", "The main ore of iron used in the blast furnace is",
     "haematite", "bauxite", "galena",
     "cinnabar", "A",
     "Haematite is iron(III) oxide."),
    (T_METAL, "Medium", "For iron to rust, it must be exposed to both",
     "oxygen and water", "nitrogen and water", "oxygen alone",
     "carbon dioxide alone", "A",
     "Both air and moisture are needed for rust."),
    (T_METAL, "Medium", "Coating iron with zinc to prevent rusting is called",
     "galvanising", "electroplating with gold", "alloying with tin",
     "painting with red lead", "A",
     "The zinc layer shields and sacrifices itself."),
    (T_METAL, "Medium", "Copper mixed with zinc produces the alloy called",
     "brass", "bronze", "solder",
     "steel", "A",
     "Brass mixes copper with zinc for hardness."),
    (T_METAL, "Hard", "In the reactivity series, which metal is the LEAST reactive of those listed?",
     "Silver", "Sodium", "Calcium",
     "Iron", "A",
     "Silver sits far below iron in the series."),
    (T_METAL, "Medium", "Aluminium is a reactive metal, yet cooking foil does not corrode away because its surface",
     "forms an oxide film", "is painted at the factory",
     "contains gold", "is magnetic", "A",
     "The thin, tough oxide layer seals the metal."),

    # --------------------------------------------------------- practical (7)
    (T_LAB, "Easy", "Carbon dioxide gas is confirmed by its turning limewater",
     "milky", "blue", "red",
     "green", "A",
     "A white precipitate of calcium carbonate clouds the water."),
    (T_LAB, "Easy", "A gas that puts out a splint with a 'pop' sound is",
     "hydrogen", "oxygen", "carbon dioxide",
     "ammonia", "A",
     "Burning hydrogen gives the squeaky pop."),
    (T_LAB, "Medium", "A glowing splint relights in a gas jar containing",
     "oxygen", "hydrogen", "nitrogen",
     "carbon dioxide", "A",
     "Oxygen supports combustion strongly."),
    (T_LAB, "Medium", "A salt gives a golden-yellow colour in a flame test. The salt contains the metal",
     "sodium", "potassium", "calcium",
     "copper", "A",
     "Sodium salts colour the flame golden yellow."),
    (T_LAB, "Medium", "The apparatus used to deliver a measured 25.0 cm³ of solution in titration is the",
     "pipette", "burette", "measuring cylinder",
     "beaker", "A",
     "The pipette dispenses one fixed volume accurately."),
    (T_LAB, "Medium", "The best technique for separating pure water from salt solution is",
     "distillation", "filtration", "decantation",
     "evaporation to dryness", "A",
     "Vapour is condensed apart from the salt left behind."),
    (T_LAB, "Hard", "Crude oil is separated into fractions in the refinery by",
     "fractional distillation", "filtration", "crystallisation",
     "sublimation", "A",
     "Different boiling ranges condense at different heights."),
]

build_batch(
    S,
    "batch_062_neco_chemistry2.json",
    "062",
    "NECO Chemistry top-up (round 2): grows the bank to 150 items so "
    "students get two full 60-question papers without repeats. New angles "
    "- sublimation, electron configuration, valency and radicals, molar "
    "mass and concentration calculations (machine-verified), brine "
    "electrolysis, electroplating, indicators, greenhouse gas, Haber iron "
    "catalyst, activation energy, alkenes, isomers, esterification, "
    "haematite, galvanising, brass, flame tests, titration apparatus, "
    "distillation - near-dup scanned against the JAMB, WAEC and existing "
    "NECO banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
