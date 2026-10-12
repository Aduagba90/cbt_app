"""Batch 054 - NECO Chemistry, Paper III Objective round 1.

NECO SSCE Chemistry Paper III is a 60-item objective paper (1 hr 15 min).
This batch covers the SSCE chemistry syllabus; numeric answers are
machine-verified by the builder and stems are near-duplicate scanned
against the JAMB and WAEC banks.

    python3 scripts/build_neco_batch54.py -> content/batch_054_neco_chemistry.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Chemistry"

T_PART = "Particulate Nature of Matter"
T_ATOM = "Atomic Structure"
T_PER = "Periodic Table and Periodicity"
T_BOND = "Chemical Bonding and Structure"
T_MOLE = "Mole Concept and Stoichiometry"
T_SOL = "Solutions and Solubility"
T_ACID = "Acids, Bases and Salts"
T_ELEC = "Electrolysis"
T_REDOX = "Redox Reactions and Cells"
T_RATE = "Energy Changes and Rates of Reaction"
T_EQ = "Chemical Equilibrium"
T_MET = "Metals and Their Compounds"
T_NON = "Non-metals and Their Compounds"
T_ORG = "Organic Chemistry"
T_WATER = "Water and Water Treatment"
T_GAS = "Gas Laws"
T_SEP = "Separation and Laboratory Techniques"

PASSAGES = []
PQ = []

Q = [
    # -------------------------------------------------- particulate nature
    (T_PART, "Medium", "The direct change of state from solid to gas is called",
     "sublimation", "evaporation", "condensation", "freezing", "A",
     "A solid that sublimes, like iodine, passes straight to vapour."),
    (T_PART, "Easy", "Diffusion happens fastest in",
     "gases", "liquids", "solids", "vacuum only", "A",
     "Gas particles move freely and quickly, so gases mix fastest."),
    (T_PART, "Easy", "Which state of matter has both fixed shape and fixed volume?",
     "Solid", "Liquid", "Gas", "Plasma", "A",
     "Solid particles are held tightly in a fixed arrangement."),
    (T_PART, "Medium", "The random motion of tiny particles, seen when smoke is viewed under a microscope, is evidence that",
     "matter is particulate", "smoke is a compound",
     "air has mass", "gases are coloured", "A",
     "Smoke specks are jostled by unseen air molecules in random motion."),
    (T_PART, "Easy", "The proton number of an element is also called its",
     "atomic number", "mass number", "nucleon number", "relative mass", "A",
     "The count of protons defines the atomic number."),

    # ------------------------------------------------------- atomic structure
    (T_ATOM, "Easy", "Isotopes of the same element differ in their number of",
     "neutrons", "protons", "electrons", "shells", "A",
     "Isotopes share proton number but differ in neutron number."),
    (T_ATOM, "Easy", "The mass number of an atom is the sum of its protons and",
     "neutrons", "electrons", "shells", "valence electrons", "A",
     "Protons plus neutrons give the nucleon (mass) number."),
    (T_ATOM, "Medium", "The electron configuration of sodium (atomic number 11) is",
     "2, 8, 1", "2, 8, 8", "2, 9", "8, 2, 1", "A",
     "Eleven electrons fill the shells as 2 then 8 then 1."),
    (T_ATOM, "Easy", "Which subatomic particle carries a negative charge?",
     "Electron", "Proton", "Neutron", "Nucleon", "A",
     "Electrons are negative; protons positive; neutrons neutral."),
    (T_ATOM, "Easy", "An atom containing equal numbers of protons and electrons is",
     "electrically neutral", "positively charged", "negatively charged", "an ion", "A",
     "Equal positive and negative charges cancel out."),

    # ---------------------------------------------------------- periodic table
    (T_PER, "Medium", "Elements in the same group of the periodic table have the same",
     "number of outermost electrons", "number of shells", "atomic mass",
     "physical state", "A",
     "Group membership is fixed by the outer-shell electron count."),
    (T_PER, "Easy", "Group VII elements are collectively called the",
     "halogens", "alkali metals", "noble gases", "alkaline earth metals", "A",
     "Fluorine, chlorine, bromine and iodine are halogens."),
    (T_PER, "Medium", "Magnesium, atomic number 12, is placed in Group",
     "II", "I", "III", "VIII", "A",
     "Magnesium (2,8,2) has two outer electrons: Group II."),
    (T_PER, "Hard", "Across a period from left to right, the atomic radius of elements",
     "decreases", "increases", "stays constant", "doubles", "A",
     "Rising nuclear charge pulls the same-shell electrons closer."),
    (T_PER, "Easy", "Noble gases are chemically unreactive because they",
     "have complete outer shells", "are monoatomic gases",
     "are rare in nature", "have low densities", "A",
     "A full outer shell means no drive to gain or lose electrons."),

    # ---------------------------------------------------------- chemical bonding
    (T_BOND, "Easy", "The bond formed in sodium chloride is",
     "ionic (electrovalent)", "covalent", "metallic", "hydrogen bonding", "A",
     "Sodium transfers an electron to chlorine: oppositely charged ions attract."),
    (T_BOND, "Easy", "The bond between the two atoms in a hydrogen molecule is",
     "covalent", "ionic", "metallic", "dative", "A",
     "The two atoms share their single electrons equally."),
    (T_BOND, "Medium", "Which substance conducts electricity when molten but not when solid?",
     "Sodium chloride", "Copper", "Graphite", "Sugar", "A",
     "Solid ionic compounds lock their ions; melting frees them to carry charge."),
    (T_BOND, "Easy", "How many covalent bonds can one carbon atom form?",
     "4", "2", "3", "1", "A",
     "Carbon has four outer electrons to share.",
     "4"),
    (T_BOND, "Hard", "A covalent bond in which both shared electrons are donated by one atom is called",
     "a dative (coordinate) bond", "a metallic bond", "an ionic bond",
     "a hydrogen bond", "A",
     "In the ammonium ion, nitrogen donates both electrons of one bond."),

    # ------------------------------------------------------------- mole concept
    (T_MOLE, "Medium", "The relative molecular mass of calcium trioxocarbonate(IV), CaCO3, is",
     "100", "84", "116", "90", "A",
     "Ca=40, C=12 and three oxygens=48, giving 100.",
     "40+12+3*16"),
    (T_MOLE, "Medium", "Calculate the number of moles of O2 molecules in an 8 g sample of the gas. (O = 16)",
     "0.25", "0.5", "1", "2", "A",
     "O2 has molar mass 32; 8 divided by 32 gives 0.25 mole.",
     "8/32"),
    (T_MOLE, "Easy", "One mole of any gas at standard temperature and pressure occupies a volume of",
     "22.4 dm3", "24 dm3 only", "11.2 dm3", "44.8 dm3", "A",
     "The molar volume of a gas at STP is 22.4 cubic decimetres.",
     "22.4"),
    (T_MOLE, "Hard", "How many molecules are there in 0.5 mole of carbon dioxide? (Avogadro number = 6.02 × 10²³)",
     "3.01 × 10²³", "6.02 × 10²³", "1.204 × 10²⁴", "6.02 × 10²²", "A",
     "Half a mole holds half of Avogadro's number of molecules.",
     "0.5*6.02"),
    (T_MOLE, "Hard", "Find the mass percentage of nitrogen in NH4NO3. (N = 14, H = 1, O = 16)",
     "35%", "28%", "17.5%", "46.7%", "A",
     "Two nitrogens (28) out of the molar mass 80 gives 35 per cent.",
     "28/80*100"),
    (T_MOLE, "Hard", "How many moles of hydrochloric acid are in 250 cm³ of a 0.2 mol/dm³ solution?",
     "0.05", "0.5", "0.02", "50", "A",
     "Moles = concentration times volume in litres: 0.2 × 0.25.",
     "0.2*0.25"),
    (T_MOLE, "Medium", "One mole of zinc reacting completely with excess dilute hydrochloric acid produces",
     "1 mole of hydrogen gas", "2 moles of hydrogen gas", "0.5 mole of hydrogen gas",
     "1 mole of chlorine", "A",
     "Zn + 2HCl gives ZnCl2 + H2 in a one-to-one mole ratio.",
     "1"),

    # ------------------------------------------------------------- solutions
    (T_SOL, "Easy", "A solution that can hold no more dissolved solute at a given temperature is said to be",
     "saturated", "dilute", "concentrated", "supersaturated always", "A",
     "At saturation, dissolving balances crystallising."),
    (T_SOL, "Easy", "Solubility of a solid in water is usually expressed in grams per",
     "100 g of water", "litre of solution only", "kilogram of solute", "mole of solvent", "A",
     "Standard solubility units are grams per hundred grams of water.",
     "100"),
    (T_SOL, "Medium", "Sugar dissolves faster in warm water when the mixture is stirred. Stirring increases the rate of dissolution by",
     "moving dissolved sugar away from the crystal", "warming the whole solution at once",
     "breaking the sugar into ions", "changing sugar into another substance", "A",
     "Stirring moves saturated solution away so fresh solvent reaches the solid."),
    (T_SOL, "Hard", "What volume of water must be added to 25 cm³ of 2.0 mol/dm³ acid to dilute it to 0.5 mol/dm³, in cm³?",
     "75", "50", "100", "25", "A",
     "Final volume = 25 × 2 ÷ 0.5 = 100 cm³, so add 75 cm³ of water.",
     "25*2/0.5-25"),
    (T_SOL, "Easy", "A dilute solution is one that contains",
     "little solute in much solvent", "no solute at all",
     "the maximum possible solute", "two immiscible liquids", "A",
     "Dilute describes low solute relative to solvent."),

    # ------------------------------------------------------- acids and bases
    (T_ACID, "Easy", "Pure water at 25 °C has a pH of",
     "7", "0", "1", "14", "A",
     "Neutral solutions have equal H+ and OH- ions: pH 7.",
     "7"),
    (T_ACID, "Medium", "Which of these salts is soluble in water?",
     "Potassium nitrate", "Barium sulfate", "Silver chloride", "Lead carbonate", "A",
     "All common potassium and nitrate salts dissolve."),
    (T_ACID, "Easy", "When hydrochloric acid is mixed with sodium hydroxide, salt and water are the only products. This type of reaction is",
     "neutralisation", "esterification", "hydrolysis", "sublimation", "A",
     "Acid plus base yields salt and water: neutralisation."),
    (T_ACID, "Medium", "Which of the following is a BASIC oxide?",
     "Copper(II) oxide", "Carbon dioxide", "Sulphur(IV) oxide", "Phosphorus(V) oxide", "A",
     "Metal oxides like CuO are basic; non-metal oxides are acidic."),
    (T_ACID, "Medium", "Dilute hydrochloric acid is added to a rock fragment and effervescence occurs. The rock most likely contains a",
     "carbonate", "chloride", "sulfate", "nitrate", "A",
     "Acids liberate carbon dioxide gas from carbonates."),
    (T_ACID, "Medium", "Which indicator is colourless in acidic solution but pink in alkaline solution?",
     "Phenolphthalein", "Methyl orange", "Litmus", "Universal indicator", "A",
     "Phenolphthalein switches from colourless to pink across neutral."),

    # ----------------------------------------------------------- electrolysis
    (T_ELEC, "Medium", "During the electrolysis of molten lead(II) bromide, the product at the cathode is",
     "molten lead", "bromine gas", "hydrogen", "lead(IV) oxide", "A",
     "Positively charged lead ions gain electrons at the cathode."),
    (T_ELEC, "Easy", "The electrode at which oxidation occurs during electrolysis is the",
     "anode", "cathode", "negative electrode always", "salt bridge", "A",
     "By convention, oxidation happens at the anode."),
    (T_ELEC, "Medium", "Which of these is a strong electrolyte?",
     "Aqueous sodium chloride", "Sugar solution", "Ethanol in water", "Distilled water", "A",
     "Sodium chloride solution ionises completely and conducts well."),
    (T_ELEC, "Hard", "In the electrolysis of acidified water, the volumes of hydrogen and oxygen collected are in the ratio",
     "2 : 1", "1 : 2", "1 : 1", "1 : 8", "A",
     "Water gives twice as many hydrogen molecules as oxygen molecules.",
     "2"),
    (T_ELEC, "Hard", "In the electrolysis of CONCENTRATED sodium chloride solution, the gas discharged at the anode is",
     "chlorine", "oxygen", "hydrogen", "nitrogen", "A",
     "High chloride concentration favours discharge of chlorine over oxygen."),

    # ----------------------------------------------------------- redox and cells
    (T_REDOX, "Easy", "In terms of electrons, oxidation is defined as the",
     "loss of electrons", "gain of electrons", "sharing of electrons", "removal of oxygen", "A",
     "OIL RIG: oxidation is loss, reduction is gain of electrons."),
    (T_REDOX, "Medium", "In the reaction Zn + CuSO4 → ZnSO4 + Cu, the zinc has been",
     "oxidised", "reduced", "neutralised", "displaced", "A",
     "Zinc loses two electrons to copper: it is oxidised."),
    (T_REDOX, "Medium", "A reducing agent is a substance that",
     "donates electrons to another substance", "accepts electrons from another substance",
     "increases its own oxidation number", "releases oxygen gas", "A",
     "The reducer gives electrons and is itself oxidised."),
    (T_REDOX, "Medium", "Iron rusting requires the presence of",
     "oxygen and water", "nitrogen and water", "carbon dioxide only", "hydrogen gas", "A",
     "Rust is hydrated iron(III) oxide formed from air and moisture."),
    (T_REDOX, "Hard", "In a simple cell with zinc and copper electrodes dipped in dilute acid, the negative electrode is",
     "zinc", "copper", "both electrodes", "the electrolyte", "A",
     "Zinc, being more reactive, releases electrons and forms the negative pole."),

    # ------------------------------------------------- energy changes and rates
    (T_RATE, "Easy", "A reaction that releases heat to its surroundings is called",
     "exothermic", "endothermic", "reversible", "neutral", "A",
     "Exothermic reactions warm their container."),
    (T_RATE, "Medium", "Raising the temperature speeds up a reaction because the particles",
     "collide harder and more often", "become heavier",
     "increase in number", "lose their charges", "A",
     "Faster, more energetic particles pass the activation barrier more often."),
    (T_RATE, "Easy", "A catalyst is a substance that",
     "speeds up a reaction without being used up", "slows down a reaction permanently",
     "is always used up completely", "changes the products formed", "A",
     "Catalysts offer an easier pathway and survive the reaction."),
    (T_RATE, "Medium", "Which of these processes is endothermic?",
     "Thermal decomposition of limestone", "Burning of firewood",
     "Neutralisation of acid by alkali", "Respiration", "A",
     "Heating limestone to quicklime absorbs heat from the surroundings."),
    (T_RATE, "Easy", "The heat energy change of a reaction is measured in the laboratory using a",
     "calorimeter", "voltameter", "barometer", "manometer", "A",
     "A calorimeter tracks the temperature change of a known mass of water."),

    # -------------------------------------------------------------- equilibrium
    (T_EQ, "Easy", "When a reversible reaction reaches dynamic equilibrium, the forward rate exactly equals the",
     "backward rate", "decomposition", "combustion", "precipitation", "A",
     "Forward and backward changes balance in a closed system."),
    (T_EQ, "Hard", "For the Haber process, N2(g) + 3H2(g) ⇌ 2NH3(g), increasing the pressure shifts the equilibrium to the",
     "right, because fewer gas moles are on that side", "left, because more gas moles are on that side",
     "left, because ammonia is lighter", "neither side; pressure has no effect", "A",
     "Pressure favours the side with fewer gas molecules: the ammonia side."),
    (T_EQ, "Medium", "A reversible reaction can only reach equilibrium in a",
     "closed system", "beaker open to the air", "blast furnace", "flowing river", "A",
     "Equilibrium needs a closed system so no substance escapes."),
    (T_EQ, "Hard", "Raising the temperature of a system at equilibrium shifts the position of equilibrium in the direction that is",
     "endothermic", "exothermic", "unchanged", "precipitating", "A",
     "Extra heat is absorbed by favouring the endothermic direction."),

    # ------------------------------------------------------------------ metals
    (T_MET, "Easy", "Which of these metals is the most reactive?",
     "Sodium", "Calcium", "Magnesium", "Zinc", "A",
     "Sodium reacts violently with cold water; the others react mildly or not at all."),
    (T_MET, "Easy", "Iron is extracted from its ore in the",
     "blast furnace", "electrolytic cell", "beaker by displacement", "fractionating column", "A",
     "Haematite is reduced by carbon monoxide in the blast furnace."),
    (T_MET, "Medium", "Which metal is extracted from its molten ore by electrolysis?",
     "Aluminium", "Iron", "Copper", "Zinc", "A",
     "Aluminium's oxide is too stable for carbon reduction."),
    (T_MET, "Easy", "Bronze is an alloy of copper and",
     "tin", "zinc", "lead", "carbon", "A",
     "Bronze is copper with tin; brass pairs copper with zinc."),
    (T_MET, "Medium", "Galvanisation protects iron from rusting by coating it with",
     "zinc", "tin", "copper", "silver", "A",
     "The zinc layer shields the iron and corrodes first."),
    (T_MET, "Medium", "Which metal does NOT react with dilute hydrochloric acid?",
     "Copper", "Zinc", "Magnesium", "Iron", "A",
     "Copper sits below hydrogen in the reactivity series."),

    # -------------------------------------------------------------- non-metals
    (T_NON, "Easy", "Which gas turns limewater milky?",
     "Carbon dioxide", "Oxygen", "Hydrogen", "Nitrogen", "A",
     "Carbon dioxide forms insoluble calcium carbonate with limewater."),
    (T_NON, "Easy", "A gas that burns with a 'pop' sound when a lighted splint is applied is",
     "hydrogen", "oxygen", "carbon dioxide", "ammonia", "A",
     "Hydrogen ignites explosively with a characteristic pop."),
    (T_NON, "Easy", "Which gas relights a glowing splint?",
     "Oxygen", "Carbon dioxide", "Nitrogen", "Chlorine", "A",
     "Oxygen rekindles combustion in the glowing splint."),
    (T_NON, "Medium", "Sulphur(IV) oxide released from factories contributes mainly to",
     "acid rain", "global warming only", "ozone depletion", "photochemical smog only", "A",
     "Dissolved in rain clouds, SO2 forms sulphurous and sulphuric acids."),
    (T_NON, "Medium", "The industrial process that combines nitrogen and hydrogen to make ammonia is the",
     "Haber process", "Contact process", "Ostwald process", "Solvay process", "A",
     "Nitrogen and hydrogen combine under pressure in the Haber process."),

    # ---------------------------------------------------------------- organic
    (T_ORG, "Easy", "Which series has the general formula shown as CnH2n+2?",
     "the alkanes", "CnH2n", "CnH2n-2", "CnHn", "A",
     "Methane CH4 fits CnH2n+2 with n = 1."),
    (T_ORG, "Medium", "When ethanol is oxidised, the organic product is",
     "ethanoic acid", "ethanal only", "ethene", "ethyl ethanoate", "A",
     "Strong oxidation of a primary alcohol gives the acid."),
    (T_ORG, "Easy", "Which of these hydrocarbons is saturated?",
     "Ethane", "Ethene", "Ethyne", "Benzene", "A",
     "Ethane has only single bonds; the others are unsaturated."),
    (T_ORG, "Easy", "The functional group of the alcohols is",
     "-OH", "-COOH", "-CHO", "-NH2", "A",
     "Alcohols carry the hydroxyl group attached to carbon."),
    (T_ORG, "Medium", "Crude oil is separated into useful fractions by",
     "fractional distillation", "filtration", "chromatography", "crystallisation", "A",
     "Fractions boil at different temperatures and condense at different levels."),
    (T_ORG, "Medium", "Compounds with the same molecular formula but different structural arrangements are called",
     "isomers", "allotropes", "isotopes", "polymers", "A",
     "Isomerism means same formula, different structure."),

    # ------------------------------------------------------------------ water
    (T_WATER, "Hard", "Which dissolved substance is chiefly responsible for temporary hardness in water?",
     "Calcium hydrogencarbonate", "calcium sulfate", "sodium chloride",
     "magnesium chloride only", "A",
     "Rain dissolves carbon dioxide, then limestone, forming the hydrogencarbonate."),
    (T_WATER, "Medium", "Hardness in water caused by calcium hydrogencarbonate can be removed by",
     "boiling", "adding soap", "filtering", "freezing", "A",
     "Boiling decomposes the hydrogencarbonate; the carbonate precipitates."),
    (T_WATER, "Easy", "Which substance is added to municipal water to kill disease-causing germs?",
     "Chlorine", "Sodium hydroxide", "Sulfuric acid", "Common salt", "A",
     "Chlorination disinfects drinking water."),
    (T_WATER, "Medium", "Why does soap produce scum in hard water? The calcium and magnesium ions",
     "form insoluble salts with the soap", "make the soap more soluble",
     "evaporate with the water", "coat the soap with oil", "A",
     "Insoluble calcium and magnesium stearates are the scum."),

    # ---------------------------------------------------------------- gas laws
    (T_GAS, "Easy", "Boyle's law states that at constant temperature, the volume of a fixed mass of gas is",
     "inversely proportional to its pressure", "directly proportional to its pressure",
     "proportional to the square of its pressure", "independent of pressure", "A",
     "Squeeze a gas and its volume shrinks in exact inverse proportion."),
    (T_GAS, "Medium", "Charles' law relates the volume of a gas to its temperature measured in",
     "kelvin", "degrees Celsius", "degrees Fahrenheit", "joules", "A",
     "Only absolute temperature gives the straight-line relationship."),
    (T_GAS, "Easy", "Convert 27 °C to the kelvin scale.",
     "300 K", "246 K", "27 K", "306 K", "A",
     "Add 273 to the Celsius reading.",
     "27+273"),
    (T_GAS, "Hard", "At constant pressure, a gas occupies 300 cm³ at 300 K. What volume will it occupy at 600 K, in cm³?",
     "600", "150", "300", "900", "A",
     "Charles' law: volume scales with kelvin temperature, doubling it.",
     "300*600/300"),

    # -------------------------------------------------------- separation methods
    (T_SEP, "Medium", "Fractional distillation is used to separate",
     "miscible liquids with close boiling points", "immiscible liquids",
     "insoluble solids from liquids", "coloured pigments only", "A",
     "The fractionating column separates liquids whose boilings points differ slightly."),
    (T_SEP, "Medium", "Chromatography separates the pigments in a dye because each pigment",
     "travels at a different speed", "evaporates completely",
     "is magnetic", "reacts with the solvent", "A",
     "Differing adsorption gives different travel distances."),
    (T_SEP, "Medium", "Pure crystals of copper(II) sulfate are obtained from its aqueous solution by",
     "crystallisation", "decantation", "filtration", "distillation", "A",
     "Slow evaporation then cooling grows pure crystals."),
    (T_SEP, "Easy", "Filtration separates",
     "an insoluble solid from a liquid", "two miscible liquids", "a dissolved solid from its solution",
     "gases from each other", "A",
     "Filter paper traps the insoluble residue."),
    (T_SEP, "Easy", "To obtain pure water from salt solution, the best technique is",
     "distillation", "filtration", "evaporation to dryness", "chromatography", "A",
     "Distillation collects the vaporised, pure solvent."),
    (T_SEP, "Easy", "Which laboratory apparatus delivers a FIXED volume of liquid accurately?",
     "Pipette", "Beaker", "Measuring cylinder", "Burette", "A",
     "A pipette is calibrated to deliver one exact volume."),
]

build_batch(
    S,
    "batch_054_neco_chemistry.json",
    "054",
    "NECO Chemistry Paper III round 1: fresh SSCE-standard items across the "
    "full syllabus (particles, atomic structure, periodicity, bonding, mole "
    "concept, solutions, acids and bases, electrolysis, redox, rates, "
    "equilibrium, metals, non-metals, organic, water, gas laws, separation "
    "techniques). Numeric answers machine-verified; near-duplicate scanned "
    "against the JAMB and WAEC banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
