"""Batch 235 - NECO Chemistry round 8 (NECO top-up, R48).

Grows NECO Chemistry from 257 toward ~282 with angles verified
absent from the whole Chemistry pool (1,512 items across JAMB, WAEC
and NECO, including R47's 25). Fresh angles: Frasch process; NPK
fertiliser; nitrogen cycle; carbon cycle; oil spill damage; sewage
treatment; food preservatives; lead poisoning from leaded petrol;
carbon(II) oxide in poorly ventilated rooms; parts per million;
advantages of hard water; normality; buffer solutions; absolute
zero; acidic salt solutions; ionisation of water; cleansing action
of soap; cobalt chloride paper; silica gel; hydrogen as a clean
fuel; silver bromide in photography; gas pressure from molecular
collisions; the flat portion of a heating curve; uses of esters;
solvent extraction. Avoided as banked or cross-subject twins:
Haber/Solvay conditions, water of crystallisation, efflorescence,
hygroscopic, deliquescence, pH family, enthalpy family,
polymerisation, thermosetting (Bakelite), nuclear fission/fusion
uranium, lime water, marble-chips CO2 prep, drying ammonia with
quicklime, parallax, purity sharp-melting, cobalt catalysts,
Kc family, eutrophication ×2, enzymes, octane rating, ideal-gas
calc, bond energy (option-level), NO2 from copper (brown-fumes item
banked R47-era), oxygen prep (H2O2 family), photosynthesis equation
(Biology twin), nitrogen-uses (adjacent to preservatives item),
smog, dibasic, immiscible/separating funnel, magnetic separation,
camphor sublimation, crystallisation, chromatography, evaporation
to dryness, weak alkali family.

    python3 scripts/build_neco_batch235.py -> content/batch_235_neco_chem8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Chemistry"

T_NONMET = "Non-metals and Their Compounds"
T_ENV = "Water and the Environment"
T_WATER = "Water and Water Treatment"
T_SOL = "Solutions and Solubility"
T_ACID = "Acids, Bases and Salts"
T_ORG = "Organic Chemistry"
T_LAB = "Separation and Laboratory Techniques"
T_PART = "Particulate Nature of Matter"
T_GAS = "Gas Laws"
T_QUAL = "Qualitative Analysis"

PASSAGES = []
PQ = []

Q = [
    (T_NONMET, "Hard", "The method of mining underground deposits of sulphur by melting them with superheated water and forcing the molten sulphur to the surface with compressed air is the",
     "Frasch process", "Fritz process",
     "flash process", "fusion process", "A",
     "Hot water melts the yellow treasure underground."),
    (T_NONMET, "Medium", "A compound fertiliser labelled NPK supplies the three major plant nutrients, which are",
     "nitrogen, phosphorus and potassium", "nitrogen, platinum and krypton",
     "sodium, phosphorus and potassium", "nitrogen, phosphorus and calcium", "A",
     "Three letters, three foods for the farm."),
    (T_ENV, "Medium", "The natural circulation in which nitrogen gas is fixed from the air by bacteria and lightning, passes through plants and animals, and returns to the air, is the",
     "nitrogen cycle", "nitrogen fixation only",
     "nitrification stage", "nitrate loop", "A",
     "The air's nitrogen walks through soil and flesh and back."),
    (T_ENV, "Medium", "The circulation in which carbon(IV) oxide is removed from the air by photosynthesis and returned by respiration, combustion and decay is the",
     "carbon cycle", "carbonation cycle",
     "carbon dating process", "carbon print", "A",
     "Every breath and every fire feed the same turnstile."),
    (T_ENV, "Medium", "A major danger when crude oil is spilled on water is that the oil film",
     "cuts off oxygen supply and kills aquatic life", "makes the water too salty to drink",
     "raises the water's boiling point", "turns the water to acid at once", "A",
     "A thin skin of oil can suffocate a whole creek."),
    (T_ENV, "Medium", "In the treatment of sewage, the stage in which bacteria and other micro-organisms break down the organic waste matter is the",
     "biological treatment stage", "screening stage alone",
     "chlorination stage", "aeration of clean water", "A",
     "Tiny workers digest the filth the town has shed."),
    (T_ENV, "Easy", "Sodium benzoate is added to some bottled drinks mainly to",
     "preserve them from spoiling", "sweeten the drink",
     "colour the drink yellow", "fizz the drink", "A",
     "A pinch of chemistry keeps the bottle patient."),
    (T_NONMET, "Medium", "The addition of tetraethyl lead to petrol to make engines run smoothly was stopped mainly because",
     "lead in exhaust fumes poisons people", "it made petrol too cheap",
     "lead made engines rust quickly", "the compound had no effect on engines", "A",
     "The quiet metal in the tank harmed the crowd outside."),
    (T_NONMET, "Easy", "Charcoal fires burning in poorly ventilated rooms are dangerous because the fire produces",
     "carbon(II) oxide, which is poisonous", "nitrogen, which suffocates",
     "helium, which explodes", "argon, which catches fire", "A",
     "The odourless thief of crowded rooms."),
    (T_SOL, "Medium", "The concentration of a very dilute pollutant, expressed as the number of parts of solute in one million parts of solution, is given in",
     "parts per million", "parts per minute",
     "percentage per mille", "pounds per mile", "A",
     "A trace poison still counts at a millionth."),
    (T_NONMET, "Medium", "In hospitals, the gas supplied from cylinders to patients who have difficulty in breathing is",
     "oxygen", "nitrogen",
     "carbon(IV) oxide", "hydrogen", "A",
     "The breath of life comes in a green cylinder."),
    (T_SOL, "Hard", "The number of gram equivalents of solute dissolved in one cubic decimetre of solution is called the",
     "normality of the solution", "molarity of the solution",
     "morality of the solution", "neutrality of the solution", "A",
     "Equivalents per litre, the older cousin of molarity."),
    (T_ACID, "Hard", "A solution whose pH changes only slightly when a small amount of acid or alkali is added to it is called a",
     "buffer solution", "boiling solution",
     "brine", "balanced solution", "A",
     "It stands like a door against the swing of pH."),
    (T_GAS, "Medium", "The temperature at which, in theory, the particles of a gas would have their lowest possible energy and the gas could be compressed no further is",
     "absolute zero", "the boiling point",
     "room temperature", "the critical temperature", "A",
     "Two hundred and seventy-three degrees below zero."),
    (T_NONMET, "Medium", "Food manufacturers flush packets of noodles and milk powder with nitrogen gas mainly because nitrogen is",
     "unreactive, so it crowds out spoiling oxygen", "cheaper than all the other gases",
     "slightly sweet to the human taste", "a good conductor of electricity", "A",
     "The idle gas crowds out the air's mischief."),
    (T_ACID, "Medium", "Pure water conducts electricity only very faintly because it",
     "is only slightly ionised", "contains no ions at all whatever",
     "is a very good conductor of heat", "is completely ionised into ions", "A",
     "Only a whisper of the molecules break apart."),
    (T_ORG, "Hard", "In the cleansing action of soap, the end of the soap molecule that dissolves in grease is the",
     "hydrocarbon (oil-loving) tail", "charged carboxylate head",
     "sodium ion alone", "water molecule itself", "A",
     "One end grips the dirt, the other grips the water."),
    (T_QUAL, "Medium", "A strip of paper that turns from blue to pink in the presence of water is",
     "cobalt chloride paper", "litmus paper",
     "universal indicator paper", "filter paper", "A",
     "The pink blush announces the water."),
    (T_LAB, "Easy", "The small sachets of a hard, glassy substance often packed with new shoes and cameras to keep them dry contain",
     "silica gel", "sodium chloride",
     "washing soda", "baking powder", "A",
     "It drinks the damp and saves the gadget."),
    (T_NONMET, "Medium", "Hydrogen is regarded as a clean fuel because, when it burns in air, the only product formed is",
     "water", "carbon(IV) oxide",
     "sulphur(IV) oxide", "nitrogen(II) oxide", "A",
     "The exhaust pipe of a hydrogen car drips innocence."),
    (T_QUAL, "Medium", "The light-sensitive compound used on photographic film, which darkens on exposure to light, is",
     "silver bromide", "sodium bromide",
     "calcium chloride", "potassium nitrate", "A",
     "Every photograph begins with a silver salt."),
    (T_PART, "Medium", "The pressure exerted by an enclosed gas results from the repeated",
     "collisions of its molecules with the walls of the container", "settling of the molecules to the bottom",
     "melting of the molecules together", "attraction of the molecules for one another", "A",
     "Trillions of tiny knocks add up to a steady push."),
    (T_PART, "Medium", "In the heating curve of ice being turned to steam, the flat portion between the rising parts shows the period during which",
     "the substance changes state at constant temperature", "the temperature rises fastest of all",
     "nothing at all is happening to it", "the water is freezing again", "A",
     "The heat works unseen, breaking the bonds of state."),
    (T_ORG, "Easy", "Esters are widely used in industry as",
     "perfumes and artificial flavourings", "fertilisers for the farm",
     "fuels for jet engines", "bleaching agents for cloth", "A",
     "The smell of pear-drop sweets is a small ester at work."),
    (T_LAB, "Hard", "The separation method in which a solute is removed from a solution by shaking it with another solvent in which the solute dissolves more readily is",
     "solvent extraction", "simple distillation",
     "crystallisation", "centrifugation", "A",
     "The solute jumps ship to the better solvent."),
]

build_batch(
    S,
    "batch_235_neco_chem8.json",
    "235",
    "NECO Chemistry round 8 (R48 top-up): Frasch process; NPK "
    "fertiliser; nitrogen cycle; carbon cycle; oil spill; sewage "
    "treatment; food preservatives; lead poisoning; carbon(II) oxide "
    "danger; ppm; advantages of hard water; normality; buffer "
    "solution; absolute zero; acidic salt solutions; ionisation of "
    "water; cleansing action of soap; cobalt chloride paper; silica "
    "gel; hydrogen as clean fuel; silver bromide; gas pressure from "
    "collisions; heating curve flat portion; uses of esters; solvent "
    "extraction. Scanned against the whole Chemistry pool (JAMB, "
    "WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
