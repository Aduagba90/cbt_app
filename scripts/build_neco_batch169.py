"""Batch 169 - WAEC Chemistry round 6 (WAEC top-up, R31).

Grows WAEC Chemistry from 205 toward ~242 with angles not yet in the
bank: titration volume from acid-base ratios; percentage yield; the
limiting reagent with hydrogen in excess; concentration from mass
and volume; one faraday as 96,500 coulombs; the white silver
chloride test, lilac flame of potassium, blue copper(II) precipitate
with NaOH, ammonia on damp red litmus; ionisation energy across a
period; fog and mist as colloids; lime raising soil pH; 78%
nitrogen and argon in air; methane from livestock; oxygen from
liquid air; the ion-exchange softener; bond breaking versus bond
making; the refrigerator and spoilage; concentration and collision
frequency; the catalyst chemically unchanged; exothermic delta H
negative; removing product shifts equilibrium right; aluminium as
most abundant metal; pig iron; tin cans; solder; bronze;
hydrogenation of vegetable oils; ethene as polythene's monomer;
sour wine oxidising to ethanoic acid; the alkanols' general
formula; blue copper(II) sulphate losing its water of
crystallisation; parallax error; the sharp melting point of a pure
solid; hard water's calcium advantage. Scanned against WAEC rounds
1-5, NECO Chemistry (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch169.py -> content/batch_169_waec_chem6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Chemistry"

T_MOL = "Mole Concept and Stoichiometry"
T_EL = "Electrolysis"
T_ABS = "Acids, Bases and Salts"
T_MTC = "Metals and Their Compounds"
T_NMC = "Non-metals and Their Compounds"
T_PER = "Periodic Table and Periodicity"
T_PNM = "Particulate Nature of Matter"
T_ENV = "Water and the Environment"
T_SEP = "Separation and Laboratory Techniques"
T_WWT = "Water and Water Treatment"
T_ENR = "Energy Changes and Rates of Reaction"
T_EQ = "Chemical Equilibrium"
T_MET = "Metals and Extraction"
T_ORG = "Organic Chemistry"

PASSAGES = []
PQ = []

Q = [
    (T_MOL, "Hard", "What volume of 0.5 mol/dm3 sulphuric acid exactly neutralises 25 cm3 of 1.0 mol/dm3 sodium hydroxide solution?",
     "25 cm3", "12.5 cm3", "50 cm3", "100 cm3", "A",
     "Two moles of the base match one mole of the acid.", "25"),
    (T_MOL, "Medium", "A reaction is expected to give 20 g of product but only 15 g is obtained. The percentage yield is",
     "75%", "25%", "60%", "133%", "A",
     "Fifteen of the twenty expected parts arrived.", "75"),
    (T_MOL, "Hard", "In the reaction 2H2 + O2 -> 2H2O, 8 g of hydrogen is mixed with 32 g of oxygen. The reagent in excess is",
     "hydrogen", "oxygen", "water", "neither reagent", "A",
     "Four moles of hydrogen need only two of oxygen."),
    (T_MOL, "Medium", "A solution contains 8 g of sodium hydroxide in 2 dm3 of solution. Its concentration in mol/dm3 is (NaOH = 40)",
     "0.1", "0.2", "0.4", "4.0", "A",
     "Eight grams is a fifth of a mole in two litres.", "0.1"),
    (T_EL, "Medium", "One faraday of electricity is approximately",
     "96,500 coulombs", "9,650 coulombs", "6,020 coulombs", "100,000 volts", "A",
     "That charge deposits one mole of silver.", "96500"),
    (T_ABS, "Medium", "Adding silver nitrate solution to a solution of sodium chloride gives",
     "a white precipitate of silver chloride", "a blue precipitate of copper(II)",
     "a colourless solution only", "a yellow precipitate of silver iodide", "A",
     "The curdy white solid proves chloride present."),
    (T_MTC, "Medium", "When a potassium compound is held in a Bunsen flame, the colour that appears is",
     "lilac", "golden-yellow", "brick-red", "apple-green", "A",
     "Viewed through blue glass, the lilac shines."),
    (T_MTC, "Medium", "Adding sodium hydroxide solution drop by drop to a copper(II) salt solution gives",
     "a pale blue precipitate", "a reddish-brown precipitate",
     "a green precipitate", "a white precipitate", "A",
     "The blue jelly of copper hydroxide appears."),
    (T_NMC, "Easy", "A gas is identified in the laboratory when it turns damp red litmus paper blue. The gas is",
     "ammonia", "hydrogen chloride", "sulphur dioxide", "nitrogen", "A",
     "Only the alkaline gas blues the litmus."),
    (T_PER, "Hard", "Across a period of the periodic table from left to right, the energy needed to remove the first electron from an atom",
     "generally increases", "generally decreases",
     "remains exactly constant", "falls to zero at the far end", "A",
     "The tightening nuclear pull holds each electron more firmly."),
    (T_PNM, "Easy", "Fog and mist, in which tiny droplets are scattered through air, are examples of",
     "colloids", "true solutions", "suspensions that settle", "compounds of water", "A",
     "The droplets stay scattered and never settle."),
    (T_PNM, "Easy", "The approximate percentage of nitrogen in dry air is",
     "78%", "21%", "1%", "0.03%", "A",
     "More than three-quarters of every breath.", "78"),
    (T_PNM, "Medium", "After nitrogen and oxygen, the next most abundant gas in dry air is",
     "argon", "carbon dioxide", "hydrogen", "methane", "A",
     "The noble gas quietly fills almost one percent."),
    (T_ENV, "Medium", "Besides carbon dioxide, a greenhouse gas released by cattle and rice paddies is",
     "methane", "argon", "oxygen", "nitrogen", "A",
     "Herd and paddy both breathe out methane."),
    (T_SEP, "Medium", "Tons of oxygen for hospitals are obtained from ordinary air by",
     "fractional distillation of liquid air", "simple distillation of ordinary air",
     "evaporation of sea water", "the Contact process", "A",
     "Chilled to liquid, the gases boil apart."),
    (T_ABS, "Medium", "A farmer spreads lime on his acidic soil in order to",
     "raise the soil pH", "lower the soil pH further",
     "colour the field green", "kill every soil organism", "A",
     "Lime sweetens sour ground for the crops."),
    (T_WWT, "Medium", "A kitchen softener swaps calcium ions in hard water for sodium ions as the water flows through it. This method is called",
     "ion exchange", "reverse osmosis",
     "simple distillation", "precipitation softening", "A",
     "Unwanted ions are traded away in the resin bed."),
    (T_WWT, "Easy", "One advantage hard water enjoys over soft water is that it",
     "supplies calcium for bones and teeth", "lathers more easily with soap",
     "boils away much faster", "never leaves scale in kettles", "A",
     "Its dissolved calcium strengthens growing bones."),
    (T_ENR, "Hard", "In every chemical change, bond breaking",
     "absorbs energy, while bond making releases it", "releases energy, while bond making absorbs it",
     "absorbs energy in both directions", "releases energy in both directions", "A",
     "Paying in to break, collecting to make."),
    (T_ENR, "Easy", "Food kept in a refrigerator spoils more slowly because the lower temperature",
     "slows down spoilage reactions", "kills all bacteria at once",
     "freezes the water inside", "dries the food out", "A",
     "Cold particles collide too slowly to react."),
    (T_ENR, "Medium", "Doubling the concentration of acid in the reaction with magnesium increases the rate mainly because",
     "collisions become more frequent", "the acid particles grow heavier",
     "the magnesium ribbon softens", "the reaction absorbs energy", "A",
     "Crowded particles meet each other more often."),
    (T_ENR, "Medium", "At the end of a catalysed reaction, the catalyst itself is",
     "chemically unchanged", "completely used up",
     "converted into product", "always a gas", "A",
     "It helps without being spent."),
    (T_ENR, "Medium", "In an exothermic reaction, the enthalpy change, delta H, is",
     "negative", "positive", "zero", "infinite", "A",
     "Heat leaves, so the store goes down."),
    (T_EQ, "Medium", "In the Haber process, continuously removing the ammonia as it forms shifts the equilibrium",
     "to the right, making more ammonia", "to the left, destroying ammonia",
     "nowhere; it remains exactly where it was before", "nowhere; everything stops altogether", "A",
     "Le Chatelier replaces what is taken."),
    (T_MET, "Easy", "The most abundant metal in the earth's crust is",
     "aluminium", "iron", "calcium", "copper", "A",
     "Clays and bauxite are built around it."),
    (T_MET, "Medium", "The iron that runs directly from the blast furnace is called",
     "pig iron", "wrought iron", "steel", "pure iron", "A",
     "It carries carbon and impurities from the furnace."),
    (T_MET, "Easy", "Food cans are made from sheets of steel plated with a thin layer of",
     "tin", "silver", "gold", "copper", "A",
     "The tin coat keeps the steel from rusting."),
    (T_MET, "Medium", "Solder, used by electricians to join wires, is an alloy of lead and",
     "tin", "zinc", "mercury", "carbon", "A",
     "The soft alloy melts at a gentle heat."),
    (T_MET, "Easy", "The alloy made by mixing copper with tin is",
     "bronze", "brass", "steel", "solder", "A",
     "Tin in the copper gives bronze its hardness."),
    (T_ORG, "Medium", "Vegetable oil is hardened into margarine by reacting it with",
     "hydrogen gas over a nickel catalyst", "oxygen gas over a platinum gauze",
     "chlorine gas in the dark", "steam over red-hot iron filings", "A",
     "Hydrogen firms the oil into spreading fat."),
    (T_ORG, "Easy", "The monomer from which polythene is made is",
     "ethene", "ethane", "ethanol", "ethanoic acid", "A",
     "Ethene units join hand in hand."),
    (T_ORG, "Easy", "Wine left open to the air turns sour because its ethanol is slowly oxidised to",
     "ethanoic acid", "methanoic acid", "ethanal", "ethene", "A",
     "Air changes the wine to weak vinegar."),
    (T_ORG, "Medium", "All members of the alkanol family share the general molecular formula",
     "CnH2n+1OH", "CnH2n+2", "CnH2n", "CnH2n-1COOH", "A",
     "One hydrogen of the alkane gives way to OH."),
    (T_ABS, "Medium", "A salt is warmed with dilute sodium hydroxide solution and a pungent gas rises. The salt contains",
     "the ammonium ion", "the copper(II) ion",
     "the iron(III) ion", "the carbonate ion", "A",
     "Alkali frees ammonia from ammonium salts."),
    (T_SEP, "Medium", "A student reads a burette with his eye above the meniscus. The reading error he commits is called",
     "parallax error", "zero error",
     "titration error", "indicator error", "A",
     "The eye must sit level with the liquid line."),
    (T_SEP, "Medium", "A student checks a solid's purity by its melting point. A pure substance shows",
     "a sharp melting point", "a wide, wandering range",
     "no melting point at all", "melting only above 100 degrees Celsius", "A",
     "Purity melts at one exact temperature."),
    (T_PNM, "Easy", "Steam touching a cold mirror turns back into water. The change of state is",
     "condensation", "sublimation", "evaporation", "decomposition", "A",
     "Gas cools and gathers into liquid drops."),
]

build_batch(
    S,
    "batch_169_waec_chem6.json",
    "169",
    "WAEC Chemistry round 6 (R31 top-up): titration volume by ratio; "
    "percentage yield 75; hydrogen in excess; 8 g NaOH in 2 dm3 as "
    "0.1 mol/dm3; one faraday 96,500 C; silver chloride white, lilac "
    "potassium flame, blue Cu(II) precipitate, ammonia blues damp "
    "litmus; ionisation energy rises across a period; fog as colloid; "
    "air 78% nitrogen and next argon; methane from herds and paddies; "
    "oxygen from liquid air; lime sweetens soil; ion-exchange "
    "softener; breaking absorbs, making releases; fridge slows "
    "spoilage; concentration crowds collisions; catalyst unchanged; "
    "exothermic delta H negative; removing product shifts right; "
    "aluminium most abundant; pig iron; tin cans; solder; bronze; "
    "hydrogenated oils; ethene into polythene; sour wine to ethanoic "
    "acid; alkanols CnH2n+1OH; blue vitriol loses its water; "
    "parallax; sharp melting point of purity; steam to condensation. "
    "Scanned against WAEC rounds 1-5, NECO Chemistry (all rounds) "
    "and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
