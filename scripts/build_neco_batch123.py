"""Batch 123 - WAEC Chemistry round 3 (WAEC top-up, Round 23).

Lifts WAEC Chemistry from 166 toward ~205 with angles not yet in any
bank: isotope arithmetic, periodic trends, mole calculations, electrolysis
products, rates and equilibrium, acids/bases and salts, redox, metals
and alloys, organic tests and reactions, water hardness and pollution.
Scanned against WAEC rounds 1-2, NECO Chemistry and the JAMB Chemistry
pool.

    python3 scripts/build_neco_batch123.py -> content/batch_123_waec_chem3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Chemistry"

T_ATOM = "Atoms and the Periodic Table"
T_MOLE = "Moles and Calculations"
T_ELEC = "Electrolysis"
T_RATE = "Rates and Equilibrium"
T_ACID = "Acids, Bases and Salts"
T_RED = "Redox and Reactivity"
T_MET = "Metals and Extraction"
T_ORG = "Organic Chemistry"
T_WATER = "Water and the Environment"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- atoms
    (T_ATOM, "Hard", "Given a chlorine sample with three-quarters Cl-35 and a quarter Cl-37, the relative atomic mass is",
     "35.5", "36.0", "35.0", "37.0", "A",
     "Weight both isotopes by abundance.", "0.75*35+0.25*37"),
    (T_ATOM, "Medium", "What distinguishes two isotopes of the same element?",
     "neutrons", "protons", "electrons", "energy shells", "A",
     "The mass shifts, the chemistry holds."),
    (T_ATOM, "Medium", "Across a period, atomic radii generally",
     "decrease", "increase", "double", "stay fixed", "A",
     "The growing pull tightens the shell."),
    (T_ATOM, "Hard", "Down a group, the outer electron is lost more easily because it is",
     "further from the nucleus", "heavier than lead", "positively charged", "radioactive", "A",
     "Distance weakens the pull."),
    (T_ATOM, "Medium", "Elements in the same group share",
     "similar outer-shell electrons", "the same mass number", "identical colour", "one melting point", "A",
     "Family resemblance in reactions."),

    # ------------------------------------------------------------- moles
    (T_MOLE, "Hard", "The number of moles in 8 g of oxygen gas, O2 (O = 16), is",
     "0.25", "0.5", "2", "8", "A",
     "Divide mass by molar mass.", "8/32"),
    (T_MOLE, "Hard", "The mass of 0.5 mole of sodium carbonate, Na2CO3 (Na=23, C=12, O=16), is",
     "53 g", "106 g", "26.5 g", "159 g", "A",
     "The molar mass works out to 106.", "0.5*106"),
    (T_MOLE, "Medium", "One mole of any substance contains the Avogadro number of particles, about",
     "6.02 times 10 to the 23", "3.02 times 10 to the 20", "6.02 times 10 to the 12", "1.60 times 10 to the 19", "A",
     "A chemist's counting dozen of atoms."),
    (T_MOLE, "Hard", "The concentration of 0.2 mole of solute in 500 cm cubed of solution is",
     "0.4 mol per dm3", "0.1 mol per dm3", "0.2 mol per dm3", "2.0 mol per dm3", "A",
     "Moles over volume in litres.", "0.2/0.5"),

    # ------------------------------------------------------------- electrolysis
    (T_ELEC, "Medium", "In electrolysis, reduction happens at the",
     "cathode", "anode", "battery", "salt bridge", "A",
     "Cations come to collect electrons."),
    (T_ELEC, "Hard", "Electrolysis of concentrated sodium chloride solution releases chlorine gas at the",
     "anode", "cathode", "bottom of the cell", "power pack", "A",
     "Chloride ions surrender charge there."),
    (T_ELEC, "Hard", "Electrolysis of molten aluminium oxide uses cryolite mainly to",
     "lower the melting point", "colour the metal", "make it heavier", "raise resistance", "A",
     "Dissolving the oxide saves power."),
    (T_ELEC, "Medium", "The electrode through which current enters the cell is the",
     "anode", "cathode", "voltmeter", "ammeter only", "A",
     "Positive current flows in."),

    # ------------------------------------------------------------- rates and equilibrium
    (T_RATE, "Medium", "Grinding a solid into powder quickens its reaction by increasing the",
     "increases surface area", "raises the activation energy", "cools the mixture", "adds a catalyst", "A",
     "More faces meet the acid."),
    (T_RATE, "Hard", "A catalyst works by",
     "lowering activation energy", "adding heat permanently", "increasing concentration", "slowing particles", "A",
     "The hill becomes a slope."),
    (T_RATE, "Hard", "In the Haber process, raising pressure shifts the equilibrium towards ammonia because the forward reaction",
     "reduces the number of gas molecules", "produces more gas molecules", "absorbs no heat", "has no gases", "A",
     "Fewer molecules favour high pressure."),
    (T_RATE, "Medium", "Heating a mixture raises the rate of reaction mainly because particles",
     "collide more often and harder", "become heavier", "lose energy", "change element", "A",
     "Kinetic theory in motion."),

    # ------------------------------------------------------------- acids and bases
    (T_ACID, "Medium", "A solution with pH 3 is",
     "acidic", "alkaline", "neutral", "amphoteric", "A",
     "Below seven lies the acid zone."),
    (T_ACID, "Medium", "Neutralising hydrochloric acid with sodium hydroxide produces which salt?",
     "sodium chloride", "sodium sulphate", "sodium nitrate", "sodium carbonate", "A",
     "Common table salt results."),
    (T_ACID, "Hard", "Zinc added to dilute sulphuric acid gives zinc sulphate and",
     "hydrogen gas", "oxygen gas", "chlorine gas", "no gas", "A",
     "The pop test confirms it."),
    (T_ACID, "Hard", "Insoluble salts are best prepared by",
     "precipitation", "evaporation alone", "neutralisation only", "electrolysis", "A",
     "Two solutions trade partners."),
    (T_ACID, "Medium", "An acid is a proton donor, according to the definition given by",
     "Bronsted and Lowry", "Arrhenius alone", "Lavoisier", "Bohr", "A",
     "Protons pass between pairs."),

    # ------------------------------------------------------------- redox and reactivity
    (T_RED, "Medium", "In electron terms, oxidation means the",
     "loss of electrons", "gain of electrons", "loss of protons", "gain of neutrons", "A",
     "The OIL RIG mnemonic recalls it."),
    (T_RED, "Hard", "Assign the oxidation number to sulphur inside sulphuric acid.",
     "+6", "+4", "-2", "+2", "A",
     "Hydrogen is +1, oxygen -2.", "6"),
    (T_RED, "Hard", "Iron displaces copper from copper sulphate solution because iron is",
     "more reactive than copper", "less reactive", "a liquid metal", "a noble metal", "A",
     "The grey nail turns coppery."),
    (T_RED, "Medium", "In the reaction Zn + CuSO4 giving ZnSO4 + Cu, the reducing agent is",
     "zinc", "copper ion", "sulphate", "water", "A",
     "It freely gives electrons away."),

    # ------------------------------------------------------------- metals and extraction
    (T_MET, "Hard", "In the blast furnace, iron ore is reduced mainly by",
     "carbon monoxide", "nitrogen", "oxygen", "argon", "A",
     "The gas strips oxygen away."),
    (T_MET, "Medium", "Inside the blast furnace, limestone takes away",
     "sand impurities as slag", "iron metal", "carbon monoxide", "the heat", "A",
     "The molten slag floats on iron."),
    (T_MET, "Medium", "Stainless steel resists rust because of its",
     "chromium content", "lead content", "wood coating", "plastic paint", "A",
     "The alloying metal shields."),
    (T_MET, "Medium", "Which metal joins copper in the alloy brass?",
     "zinc", "tin", "lead", "silver", "A",
     "The yellow shine gives it away."),

    # ------------------------------------------------------------- organic
    (T_ORG, "Medium", "The test that distinguishes an alkene from an alkane uses",
     "bromine water", "lime water", "litmus paper", "iodine solution", "A",
     "The orange turns colourless."),
    (T_ORG, "Medium", "Ethanol to ethene requires",
     "heating with acid", "cooling with ice", "adding table salt", "passing cold air", "A",
     "Concentrated acid dehydrates it."),
    (T_ORG, "Hard", "Ethanoic acid and ethanol react to form an ester and",
     "water", "hydrogen", "carbon dioxide", "oxygen", "A",
     "The sweet smell of the lab."),
    (T_ORG, "Medium", "Fermentation of glucose yields ethanol and",
     "carbon dioxide", "nitrogen", "methane", "oxygen", "A",
     "Bakers' yeast does the brewing."),
    (T_ORG, "Hard", "The homologous series with the general formula CnH2n+2 is the",
     "alkanes", "alkenes", "alkanols", "alkanoic acids", "A",
     "Saturated and single-bonded."),

    # ------------------------------------------------------------- water and environment
    (T_WATER, "Hard", "The hardness that boiling cannot cure is banished by",
     "washing soda", "boiling", "filtering", "freezing", "A",
     "Boiling only beats the temporary kind."),
    (T_WATER, "Medium", "Scum forms when soap meets hard water because of the dissolved",
     "calcium and magnesium salts", "oxygen gas", "table salt", "sugar", "A",
     "Calcium ions steal the soap."),
    (T_WATER, "Medium", "The gas chiefly responsible for acid rain is",
     "sulphur dioxide", "oxygen", "nitrogen", "helium", "A",
     "Coal-burning chimneys release it."),
    (T_WATER, "Hard", "Biodegradable detergents are preferred because they",
     "are broken down by bacteria", "kill all fish", "never dissolve", "harden water", "A",
     "River bacteria can digest them."),
]

build_batch(
    S,
    "batch_123_waec_chem3.json",
    "123",
    "WAEC Chemistry round 3 (Round 23 top-up): chlorine isotope RAM "
    "35.5, isotope neutrons, periodic trends, electron loss down a "
    "group, group outer shells, 8 g of O2 as 0.25 mol, 0.5 mol of "
    "Na2CO3 weighing 53 g, Avogadro number, 0.4 mol per dm3 "
    "concentration, cathode reduction, brine electrolysis chlorine, "
    "cryolite's role, anode definition, surface area and catalysis, "
    "Haber pressure shift, collision heating, pH 3, hydrochloric acid "
    "plus base salt, zinc plus sulphuric acid, precipitation of "
    "insoluble salts, Bronsted-Lowry, oxidation as electron loss, "
    "sulphur +6 in H2SO4, displacement and reducing agent, blast "
    "furnace carbon monoxide and limestone slag, stainless steel "
    "chromium, brass and zinc, bromine-water alkene test, ethanol "
    "dehydration, esterification and fermentation products, alkane "
    "general formula, permanent hardness removal by washing soda, scum "
    "formation, sulphur dioxide and acid rain, biodegradable "
    "detergents. Scanned against WAEC rounds 1-2, NECO Chemistry and "
    "the JAMB Chemistry pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
