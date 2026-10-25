"""Batch 137 - NECO Chemistry round 4 (NECO top-up, Round 26).

Lifts NECO Chemistry from 156 toward ~193 with angles not yet in any
bank: separation technique selection (immiscible liquids, boiling-point
close fractions, solute colours); kinetic-theory evidence; Boyle-law
arithmetic; Faraday-style electrolysis products by discharge order;
moles from mass (CaCO3); preparation routes for salts (insoluble by
precipitation, soluble by titration); oxidation-number bookkeeping;
rate-curve reading; Le Chatelier on the Haber process; group and
period trends; hydrogen bonding and malleability; esterification and
polymerisation word equations; water treatment stages; blast-furnace
and aluminium extraction; air composition percentages; acid-rain
gases; gas identification tests. Numeric items carry verify strings
where the correct option's first number equals the value. Scanned
against NECO rounds 1-3, WAEC Chemistry (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch137.py -> content/batch_137_neco_chem4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Chemistry"

T_SEP = "Separation and Purity"
T_KIN = "States of Matter and Gas Laws"
T_ELE = "Electrolysis"
T_MOL = "The Mole Concept"
T_SALT = "Acids, Bases and Salts"
T_RED = "Redox Reactions"
T_RATE = "Rates and Equilibrium"
T_PER = "Periodic Table and Bonding"
T_ORG = "Organic Chemistry"
T_ENV = "Water, Air and Metals"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- separation
    (T_SEP, "Medium", "To separate a mixture of kerosene and water, the best apparatus is the",
     "separating funnel", "fractionating column", "filter paper", "liebig condenser", "A",
     "The two liquids refuse to mix."),
    (T_SEP, "Hard", "Crude oil splits into petrol and diesel fractions because the fractions differ in",
     "boiling points", "melting colours", "electrical charge", "magnetic pull", "A",
     "Heat sorts them by volatility."),
    (T_SEP, "Medium", "Different coloured pigments in a leaf extract are best separated by",
     "chromatography", "filtration", "decantation", "evaporation", "A",
     "Solvent races them up the paper."),
    (T_SEP, "Medium", "A hot, saturated copper (II) sulphate solution left to cool slowly yields blue crystals through",
     "crystallisation", "simple distillation", "sublimation", "magnetic separation", "A",
     "Slow cooling grows the crystals."),

    # ------------------------------------------------------------- states & gases
    (T_KIN, "Medium", "Brownian motion in smoke cells is evidence that gas particles",
     "move randomly and constantly", "rest most of the time", "travel in straight lines only", "attract each other", "A",
     "Specks dance on unseen feet."),
    (T_KIN, "Hard", "A gas occupies 200 cubic cm at 1 atmosphere. Kept at constant temperature, at 2 atmospheres its volume becomes",
     "100 cubic cm", "400 cubic cm", "200 cubic cm", "50 cubic cm", "A",
     "Squeeze twice, halve the space.", "100"),
    (T_KIN, "Medium", "Melting is the change of state from",
     "solid to liquid", "liquid to solid", "gas to liquid", "liquid to gas", "A",
     "Heat loosens the lattice."),

    # ------------------------------------------------------------- electrolysis
    (T_ELE, "Medium", "During the electrolysis of molten lead (II) bromide, reduction takes place at the",
     "cathode", "anode", "electrolyte surface", "battery terminal", "A",
     "The negative electrode feeds electrons."),
    (T_ELE, "Hard", "During the electrolysis of dilute sulphuric acid, the gas given off at the anode is",
     "oxygen", "hydrogen", "sulphur dioxide", "chlorine", "A",
     "Hydroxide ions surrender there."),
    (T_ELE, "Medium", "Copper is purified by electrolysis using",
     "impure copper as anode", "impure copper as cathode", "pure copper as anode", "a carbon cathode", "A",
     "The dirty anode slowly dissolves."),
    (T_ELE, "Hard", "When concentrated sodium chloride solution is electrolysed, chlorine forms at the anode because chloride ions are",
     "concentrated enough to discharge first", "lighter than hydroxide ions", "positively charged", "gases already", "A",
     "Crowding beats the ease order."),

    # ------------------------------------------------------------- mole
    (T_MOL, "Hard", "The number of moles in 10 grams of calcium carbonate, CaCO3 (Ca 40, C 12, O 16), is",
     "0.1", "1.0", "0.2", "0.01", "A",
     "Ten grams over the molar hundred.", "0.1"),
    (T_MOL, "Medium", "The molar mass of CaCO3 from Ca 40, C 12, O 16 is",
     "100 g per mole", "88 g per mole", "72 g per mole", "112 g per mole", "A",
     "Forty, twelve and three sixteens.", "100"),

    # ------------------------------------------------------------- acids & salts
    (T_SALT, "Medium", "An insoluble salt such as lead (II) iodide is best prepared by",
     "precipitation", "titration", "neutralisation by boiling", "direct combination", "A",
     "Two clear solutions wed at once."),
    (T_SALT, "Medium", "The standard volumetric preparation of sodium chloride solution uses",
     "titration of acid with alkali", "heating sodium metal", "evaporating brine rocks", "double decomposition", "A",
     "Burette meets flask drop by drop."),
    (T_SALT, "Hard", "A salt that is neither an acid salt nor a normal salt is the",
     "basic salt", "double salt", "complex salt", "mixed salt", "A",
     "It still carries metal hydroxide."),
    (T_SALT, "Medium", "The two acids whose salts are ALL soluble in water are",
     "nitric acid and ethanoic acid", "sulphuric acid and hydrochloric acid", "carbonic acid and nitric acid", "hydrochloric acid and carbonic acid", "A",
     "Even their lead and barium salts dissolve."),

    # ------------------------------------------------------------- redox
    (T_RED, "Medium", "Working from hydrogen +1 and oxygen -2, the oxidation number of nitrogen in HNO3 comes to",
     "+5", "+3", "+7", "-3", "A",
     "One hydrogen balances three oxygens partly.", "+5"),
    (T_RED, "Hard", "When magnesium burns in carbon dioxide to give magnesium oxide and carbon, the substance oxidised is the",
     "magnesium", "carbon", "carbon dioxide", "magnesium oxide", "A",
     "It surrenders electrons to the dioxide."),
    (T_RED, "Medium", "Loss of hydrogen by a substance during a reaction is",
     "oxidation", "reduction", "neutralisation", "hydrolysis", "A",
     "Losing hydrogen is losing hold."),

    # ------------------------------------------------------------- rates & equilibrium
    (T_RATE, "Hard", "Powdering a solid reactant quickens the reaction chiefly by",
     "increasing surface area", "raising the temperature", "thinning the solution", "adding a catalyst", "A",
     "More faces meet the acid."),
    (T_RATE, "Medium", "A catalyst changes a reaction's rate by changing the",
     "activation energy path", "final products formed", "overall heat given out", "concentrations", "A",
     "It builds a lower bridge."),
    (T_RATE, "Medium", "On a rate graph, a steeper initial slope means the reaction",
     "started faster", "lasted longer", "ended with more gas", "was colder", "A",
     "Steepness is early speed."),
    (T_RATE, "Hard", "Running the Haber process at a lower temperature raises the ammonia yield because the forward reaction is",
     "exothermic", "endothermic", "athermal", "photochemical", "A",
     "Heat is a product; cold favours it."),

    # ------------------------------------------------------------- periodic & bonding
    (T_PER, "Hard", "Down any group of the periodic table, the general trend is that atomic radius",
     "increases", "decreases", "stays constant", "first rises then falls", "A",
     "Each row adds a new shell."),
    (T_PER, "Medium", "The family likeness of the group one metals stems from each atom having",
     "one outer electron", "the same mass number", "equal total shells", "eight outer electrons", "A",
     "Family resemblance sits outside."),
    (T_PER, "Hard", "The unusually high boiling point of water, compared with its neighbours, is due to",
     "hydrogen bonding", "ionic bonding", "metallic bonding", "van der Waals only", "A",
     "Strong handshakes between molecules."),
    (T_PER, "Medium", "Metals can be hammered into sheets because their atoms are held by a",
     "sea of mobile electrons", "fixed covalent network", "giant ionic lattice", "hydrogen-bond chain", "A",
     "Layers slide without breaking."),

    # ------------------------------------------------------------- organic
    (T_ORG, "Medium", "The reaction between ethanoic acid and ethanol produces",
     "an ester and water", "a soap and glycerol", "an alkene and water", "a polymer", "A",
     "Fruity smells are born so."),
    (T_ORG, "Hard", "The repeated linking of many small molecules into long chains is called",
     "polymerisation", "esterification", "saponification", "fermentation", "A",
     "Beads string into necklaces."),
    (T_ORG, "Medium", "Both butane and methylpropane share the formula C4H10. They are",
     "isomers", "allotropes", "isotopes", "homologues", "A",
     "Same atoms, different houses."),
    (T_ORG, "Medium", "The conversion of starch to ethanol by yeast proceeds through",
     "fermentation", "sublimation", "cracking", "hydrogenation", "A",
     "Yeast eats sugar, breathes wine."),

    # ------------------------------------------------------------- environment & metals
    (T_ENV, "Medium", "The correct order of stages in municipal water treatment is",
     "coagulation, sedimentation, filtration, disinfection", "filtration, boiling, freezing, salting", "sedimentation, salting, distillation, drying", "disinfection, coagulation, boiling, filtering", "A",
     "Floc settles, sand polishes, chlorine guards."),
    (T_ENV, "Medium", "The main gases responsible for acid rain are oxides of",
     "sulphur and nitrogen", "carbon and hydrogen", "oxygen and helium", "nitrogen and argon", "A",
     "Chimneys brew the sour rain."),
    (T_ENV, "Hard", "Inside the blast furnace, iron (III) oxide meets a gas that robs it of its oxygen. That gas is chiefly",
     "carbon monoxide", "carbon dioxide", "nitrogen", "sulphur dioxide", "A",
     "It strips oxygen and leaves iron."),
    (T_ENV, "Hard", "Aluminium is extracted from purified bauxite by",
     "electrolysis of molten alumina", "reduction with carbon monoxide", "heating the ore alone", "the blast furnace", "A",
     "Electric current does the digging."),
    (T_ENV, "Medium", "When a lighted splint is applied to a gas and a 'pop' is heard, the gas is",
     "hydrogen", "oxygen", "carbon dioxide", "ammonia", "A",
     "The sharp squeal names it."),
    (T_ENV, "Medium", "Damp red litmus turning blue identifies",
     "ammonia", "hydrogen chloride", "sulphur dioxide", "carbon monoxide", "A",
     "The alkaline breath shows."),
]

build_batch(
    S,
    "batch_137_neco_chem4.json",
    "137",
    "NECO Chemistry round 4 (Round 26 top-up): separating funnel for "
    "immiscibles, crude-oil fractions by boiling point, chromatography, "
    "crystallisation; Brownian motion, Boyle-law 200 to 100 cubic cm, "
    "melting; lead at cathode, oxygen at anode of dilute H2SO4, copper "
    "refining anode, brine chlorine by concentration; CaCO3 moles 0.1 "
    "and molar mass 100; precipitation vs titration routes, basic "
    "salt, all-soluble acids (HNO3 and CH3COOH); Mn +7 in KMnO4, zinc "
    "reducing agent, hydrogen loss as oxidation; surface area, catalyst "
    "paths, steep rate curves, Haber pressure; radius down-group, "
    "outer electrons, hydrogen bonding, malleability; esterification, "
    "polymerisation, C4H10 isomers, fermentation; water-treatment "
    "order, acid-rain gases, CO as blast-furnace reducer, aluminium by "
    "electrolysis, pop-test hydrogen, ammonia litmus. Scanned against "
    "NECO rounds 1-3, WAEC Chemistry (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
