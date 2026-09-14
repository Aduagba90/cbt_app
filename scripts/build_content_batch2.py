"""Builds content/batch_002_chemistry_biology.json — applied Chemistry (calculations verified
in Python) and scenario/experiment-based Biology questions.

Run:  python3 scripts/build_content_batch2.py
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_content_batch1 import _balance, _num  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "content", "batch_002_chemistry_biology.json")

# (topic, difficulty, question, A, B, C, D, answer, explanation, verify)
CHEM = [
    ("Mole Concept and Stoichiometry", "Easy", "The number of moles in 11 g of carbon(IV) oxide is (C = 12, O = 16)", "0.25 mol", "0.50 mol", "2.5 mol", "4.0 mol", "A", "Molar mass of CO₂ = 12 + 32 = 44 g/mol; n = 11/44 = 0.25 mol.", "11/44"),
    ("Mole Concept and Stoichiometry", "Easy", "The mass of 0.5 mol of calcium trioxocarbonate(IV), CaCO₃, is (Ca = 40, C = 12, O = 16)", "25 g", "50 g", "100 g", "200 g", "B", "Molar mass = 40 + 12 + 48 = 100 g/mol; mass = 0.5 × 100 = 50 g.", "0.5*100"),
    ("Mole Concept and Stoichiometry", "Medium", "The volume occupied by 8 g of oxygen gas at s.t.p. is (O = 16, molar volume = 22.4 dm³)", "2.8 dm³", "5.6 dm³", "11.2 dm³", "22.4 dm³", "B", "n(O₂) = 8/32 = 0.25 mol; volume = 0.25 × 22.4 = 5.6 dm³.", "8/32*22.4"),
    ("Mole Concept and Stoichiometry", "Medium", "The percentage by mass of nitrogen in ammonium trioxonitrate(V), NH₄NO₃, is (N = 14, H = 1, O = 16)", "17.5%", "35%", "40%", "70%", "B", "Molar mass = 14 + 4 + 14 + 48 = 80; nitrogen = 28; 28/80 × 100 = 35%.", "28/80*100"),
    ("Mole Concept and Stoichiometry", "Medium", "A compound contains 40% calcium, 12% carbon and 48% oxygen by mass. Its empirical formula is (Ca = 40, C = 12, O = 16)", "CaCO₃", "CaC₂O₄", "Ca₂CO₃", "CaCO₂", "A", "Mole ratio: Ca 40/40 = 1, C 12/12 = 1, O 48/16 = 3 ⇒ CaCO₃.", None),
    ("Mole Concept and Stoichiometry", "Easy", "2H₂(g) + O₂(g) → 2H₂O(g). The volume of oxygen required to burn 10 dm³ of hydrogen completely is", "2.5 dm³", "10 dm³", "5 dm³", "20 dm³", "C", "Gas volumes are in the ratio of the coefficients: 2 : 1, so 10 dm³ of H₂ needs 5 dm³ of O₂.", "10/2"),
    ("Mole Concept and Stoichiometry", "Medium", "The number of molecules in 4.4 g of carbon(IV) oxide is (C = 12, O = 16, Avogadro's number = 6.02 × 10²³)", "6.02 × 10²³", "3.01 × 10²³", "1.204 × 10²⁴", "6.02 × 10²²", "D", "n = 4.4/44 = 0.1 mol; molecules = 0.1 × 6.02 × 10²³ = 6.02 × 10²².", None),
    ("Mole Concept and Stoichiometry", "Medium", "4 g of sodium hydroxide is dissolved in water to make 500 cm³ of solution. The concentration of the solution is (Na = 23, O = 16, H = 1)", "0.05 mol/dm³", "0.1 mol/dm³", "0.2 mol/dm³", "0.4 mol/dm³", "C", "n = 4/40 = 0.1 mol; volume = 0.5 dm³; concentration = 0.1/0.5 = 0.2 mol/dm³.", "4/40/0.5"),
    ("Acids Bases and Salts", "Medium", "25.0 cm³ of 0.10 mol/dm³ NaOH was exactly neutralised by 20.0 cm³ of HCl. The concentration of the acid is", "0.080 mol/dm³", "0.125 mol/dm³", "0.200 mol/dm³", "0.250 mol/dm³", "B", "NaOH + HCl → NaCl + H₂O (1 : 1). CₐVₐ = CᵦVᵦ ⇒ Cₐ = (0.10 × 25)/20 = 0.125 mol/dm³.", "0.1*25/20"),
    ("Acids Bases and Salts", "Hard", "25 cm³ of 0.20 mol/dm³ NaOH required 12.5 cm³ of H₂SO₄ for complete neutralisation. The concentration of the acid is", "0.05 mol/dm³", "0.10 mol/dm³", "0.20 mol/dm³", "0.40 mol/dm³", "C", "2NaOH + H₂SO₄ → Na₂SO₄ + 2H₂O. n(NaOH) = 0.005 mol ⇒ n(H₂SO₄) = 0.0025 mol in 0.0125 dm³ ⇒ 0.20 mol/dm³.", "0.2*25/(2*12.5)"),
    ("Chemical Reactions", "Medium", "6.5 g of zinc reacts completely with excess dilute hydrochloric acid. The volume of hydrogen produced at s.t.p. is (Zn = 65, molar volume = 22.4 dm³)", "1.12 dm³", "2.24 dm³", "11.2 dm³", "22.4 dm³", "B", "Zn + 2HCl → ZnCl₂ + H₂. n(Zn) = 6.5/65 = 0.1 mol ⇒ 0.1 mol H₂ = 0.1 × 22.4 = 2.24 dm³.", "6.5/65*22.4"),
    ("Chemical Reactions", "Medium", "When 25 g of calcium trioxocarbonate(IV) is heated strongly until no further change, the mass of solid residue is (CaCO₃ = 100, CaO = 56)", "11 g", "14 g", "25 g", "56 g", "B", "CaCO₃ → CaO + CO₂. 100 g gives 56 g of CaO, so 25 g gives 25 × 56/100 = 14 g.", "25/100*56"),
    ("States of Matter", "Easy", "A gas occupies 300 cm³ at 27 °C. Its volume at 127 °C at the same pressure is", "400 cm³", "1411 cm³", "225 cm³", "200 cm³", "A", "Charles' law with kelvin temperatures: V₂ = 300 × 400/300 = 400 cm³.", "300*400/300"),
    ("States of Matter", "Easy", "200 cm³ of a gas at 760 mmHg is allowed to expand until its pressure falls to 380 mmHg at constant temperature. Its new volume is", "100 cm³", "800 cm³", "200 cm³", "400 cm³", "D", "Boyle's law: P₁V₁ = P₂V₂ ⇒ 760 × 200 = 380 × V₂ ⇒ V₂ = 400 cm³.", "760*200/380"),
    ("States of Matter", "Hard", "500 cm³ of a gas was collected at 27 °C and 700 mmHg. Its volume at s.t.p. is approximately", "596 cm³", "419 cm³", "460 cm³", "350 cm³", "B", "P₁V₁/T₁ = P₂V₂/T₂ ⇒ V₂ = 500 × (700/760) × (273/300) ≈ 419 cm³.", "500*700/760*273/300"),
    ("States of Matter", "Medium", "Under the same conditions, hydrogen (H₂ = 2) diffuses faster than oxygen (O₂ = 32) by a factor of", "2", "4", "16", "0.25", "B", "Graham's law: rate ∝ 1/√M, so rate(H₂)/rate(O₂) = √(32/2) = √16 = 4.", "(32/2)**0.5"),
    ("States of Matter", "Easy", "A vessel contains oxygen at a partial pressure of 300 mmHg and nitrogen at a partial pressure of 450 mmHg. The total pressure in the vessel is", "150 mmHg", "375 mmHg", "750 mmHg", "1350 mmHg", "C", "Dalton's law: total pressure = sum of partial pressures = 300 + 450 = 750 mmHg.", "300+450"),
    ("Acids Bases and Salts", "Easy", "The pH of a 0.01 mol/dm³ solution of hydrochloric acid is", "1", "2", "12", "0.01", "B", "HCl is a strong acid, fully ionised: [H⁺] = 10⁻² ⇒ pH = −log(10⁻²) = 2.", "-math.log10(0.01)"),
    ("Acids Bases and Salts", "Medium", "The pH of a 0.001 mol/dm³ solution of sodium hydroxide is", "3", "1", "11", "13", "C", "[OH⁻] = 10⁻³ ⇒ pOH = 3 ⇒ pH = 14 − 3 = 11.", "14+math.log10(0.001)"),
    ("Acids Bases and Salts", "Medium", "Which of the following salts gives an acidic solution when dissolved in water?", "NH₄Cl", "Na₂CO₃", "NaCl", "CH₃COONa", "A", "NH₄Cl comes from a strong acid and a weak base; the NH₄⁺ ion hydrolyses to release H⁺. Na₂CO₃ and CH₃COONa are alkaline, NaCl is neutral.", None),
    ("Acids Bases and Salts", "Easy", "A student adds a few drops of methyl orange to a beaker of dilute hydrochloric acid. The solution turns", "yellow", "colourless", "blue", "red", "D", "Methyl orange is red in acidic solution (pH below 3.1) and yellow in alkaline solution.", None),
    ("Electrochemistry", "Medium", "The quantity of electricity required to deposit 0.1 mol of copper from a solution of Cu²⁺ ions is (F = 96,500 C/mol)", "9,650 C", "19,300 C", "96,500 C", "193,000 C", "B", "Cu²⁺ + 2e⁻ → Cu: 2 mol of electrons per mole of copper ⇒ 0.1 × 2 × 96,500 = 19,300 C.", "2*0.1*96500"),
    ("Electrochemistry", "Hard", "A current of 0.5 A is passed through silver trioxonitrate(V) solution for 965 s. The mass of silver deposited is (Ag = 108, F = 96,500 C/mol)", "0.54 g", "1.08 g", "5.40 g", "0.27 g", "A", "Q = It = 0.5 × 965 = 482.5 C; mol e⁻ = 482.5/96,500 = 0.005; Ag⁺ + e⁻ → Ag ⇒ 0.005 × 108 = 0.54 g.", "0.5*965/96500*108"),
    ("Electrochemistry", "Hard", "The time required to deposit 6.5 g of zinc from a solution of Zn²⁺ ions using a current of 2 A is (Zn = 65, F = 96,500 C/mol)", "4,825 s", "3,217 s", "9,650 s", "19,300 s", "C", "n(Zn) = 0.1 mol needs 0.2 mol e⁻ = 19,300 C; t = Q/I = 19,300/2 = 9,650 s.", "0.1*2*96500/2"),
    ("Electrochemistry", "Medium", "Given E°(Zn²⁺/Zn) = −0.76 V and E°(Cu²⁺/Cu) = +0.34 V, the e.m.f. of the cell Zn(s)|Zn²⁺(aq)||Cu²⁺(aq)|Cu(s) is", "0.42 V", "1.10 V", "−1.10 V", "−0.42 V", "B", "E°cell = E°(cathode) − E°(anode) = 0.34 − (−0.76) = 1.10 V.", "0.34+0.76"),
    ("Electrochemistry", "Easy", "During the electrolysis of dilute tetraoxosulphate(VI) acid with platinum electrodes, the ratio of the volume of hydrogen to oxygen produced is", "1 : 2", "1 : 1", "2 : 1", "1 : 8", "C", "Water is decomposed: 2H₂O → 2H₂ + O₂, so hydrogen (cathode) : oxygen (anode) = 2 : 1 by volume.", None),
    ("Chemical Reactions", "Easy", "The oxidation number of manganese in KMnO₄ is", "+2", "+4", "+6", "+7", "D", "K = +1, O = −2 × 4 = −8; +1 + x − 8 = 0 ⇒ x = +7.", "8-1"),
    ("Chemical Reactions", "Medium", "The oxidation number of chromium in Cr₂O₇²⁻ is", "+3", "+6", "+7", "+12", "B", "2x + 7(−2) = −2 ⇒ 2x = +12 ⇒ x = +6.", "(14-2)/2"),
    ("Energy and Rates of Reaction", "Easy", "The enthalpy of combustion of methane is −890 kJ/mol. The heat released when 2 mol of methane burn completely is", "445 kJ", "890 kJ", "1,780 kJ", "3,560 kJ", "C", "Heat released = 2 × 890 = 1,780 kJ.", "2*890"),
    ("Energy and Rates of Reaction", "Medium", "The enthalpy of neutralisation of HCl by NaOH is −57 kJ/mol. The heat evolved when 0.5 mol of HCl is completely neutralised is", "14.25 kJ", "28.5 kJ", "57 kJ", "114 kJ", "B", "0.5 mol × 57 kJ/mol = 28.5 kJ.", "0.5*57"),
    ("Energy and Rates of Reaction", "Easy", "0.65 g of zinc granules reacted completely with excess acid in 50 s. The average rate of the reaction is", "0.013 g/s", "0.13 g/s", "1.3 g/s", "32.5 g/s", "A", "Rate = mass reacted/time = 0.65/50 = 0.013 g/s.", "0.65/50"),
    ("Energy and Rates of Reaction", "Easy", "Which change will increase the rate of reaction between marble chips and dilute hydrochloric acid?", "using larger marble chips", "cooling the acid", "diluting the acid with water", "grinding the marble to a powder", "D", "Powdering increases the surface area in contact with the acid, so more collisions occur per second.", None),
    ("Energy and Rates of Reaction", "Medium", "The rate of a certain reaction doubles for every 10 °C rise in temperature. If the reaction takes 40 minutes at 20 °C, at 40 °C it will take about", "10 minutes", "20 minutes", "80 minutes", "160 minutes", "A", "A 20 °C rise = two doublings ⇒ rate × 4 ⇒ time ÷ 4 = 10 minutes.", "40/4"),
    ("Chemical Equilibrium", "Medium", "N₂(g) + 3H₂(g) ⇌ 2NH₃(g), ΔH = −92 kJ. The yield of ammonia is increased by", "high pressure and low temperature", "low pressure and high temperature", "high pressure and high temperature", "low pressure and low temperature", "A", "Le Chatelier: 4 mol of gas become 2, so high pressure favours NH₃; the forward reaction is exothermic, so low temperature favours it.", None),
    ("Chemical Equilibrium", "Hard", "At equilibrium, a mixture contains 0.2 mol/dm³ H₂, 0.2 mol/dm³ I₂ and 0.8 mol/dm³ HI. For H₂(g) + I₂(g) ⇌ 2HI(g), the equilibrium constant Kc is", "2", "4", "16", "0.0625", "C", "Kc = [HI]²/([H₂][I₂]) = 0.8²/(0.2 × 0.2) = 0.64/0.04 = 16.", "0.8**2/(0.2*0.2)"),
    ("Chemical Equilibrium", "Medium", "Adding a catalyst to a reaction that has reached equilibrium will", "increase the yield of products", "shift the equilibrium to the left", "not change the position of equilibrium", "decrease the value of Kc", "C", "A catalyst speeds up the forward and backward reactions equally, so equilibrium is reached faster but its position and Kc are unchanged.", None),
    ("Atomic Structure", "Medium", "Chlorine consists of 75% ³⁵Cl and 25% ³⁷Cl. Its relative atomic mass is", "35.0", "35.5", "36.0", "36.5", "B", "(35 × 0.75) + (37 × 0.25) = 26.25 + 9.25 = 35.5.", "35*0.75+37*0.25"),
    ("Atomic Structure", "Easy", "The number of neutrons in an atom of ²³₁₁Na is", "11", "23", "12", "34", "C", "Neutrons = mass number − atomic number = 23 − 11 = 12.", "23-11"),
    ("Periodic Table", "Medium", "An element X has 17 electrons. Which statement about X is correct?", "It forms X²⁺ ions", "It is a metal", "It has three valence electrons", "It is in Group 7 and Period 3", "D", "Configuration 2, 8, 7: three shells ⇒ Period 3; seven outer electrons ⇒ Group 7 (a halogen that forms X⁻ ions).", None),
    ("Chemical Bonding", "Medium", "Which of the following substances has the highest boiling point?", "hydrogen chloride", "sodium chloride", "methane", "hydrogen", "B", "Sodium chloride is an ionic solid held by strong electrostatic forces; the others are simple molecular substances with weak intermolecular forces.", None),
    ("Organic Chemistry", "Medium", "C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O. The volume of oxygen at s.t.p. needed to burn 1 mol of ethanol completely is (molar volume = 22.4 dm³)", "22.4 dm³", "44.8 dm³", "67.2 dm³", "89.6 dm³", "C", "3 mol of O₂ are needed: 3 × 22.4 = 67.2 dm³.", "3*22.4"),
    ("Organic Chemistry", "Easy", "A student bubbles two gases, ethane and ethene, separately through bromine water. The bromine water is decolourised by", "ethene only", "ethane only", "both gases", "neither gas", "A", "Ethene is unsaturated (C=C) and adds bromine, decolourising it; ethane is saturated and does not react.", None),
    ("Organic Chemistry", "Medium", "The product formed when ethanoic acid is warmed with ethanol in the presence of concentrated tetraoxosulphate(VI) acid is", "ethanal", "ethyl ethanoate", "ethane", "sodium ethanoate", "B", "Acid + alcohol → ester + water (esterification); ethanoic acid and ethanol give ethyl ethanoate.", None),
    ("Organic Chemistry", "Easy", "The molecular formula of the alkane with five carbon atoms is", "C₅H₁₀", "C₅H₈", "C₅H₁₂", "C₅H₅", "C", "Alkanes have the general formula CₙH₂ₙ₊₂; for n = 5, H = 12 ⇒ C₅H₁₂ (pentane).", None),
    ("Water Air and Environmental Chemistry", "Medium", "A sample of water forms a scum with soap. After boiling, the water lathers easily. The hardness was caused by", "calcium tetraoxosulphate(VI)", "calcium hydrogentrioxocarbonate(IV)", "sodium chloride", "magnesium tetraoxosulphate(VI)", "B", "Hardness removed by boiling is temporary hardness, caused by Ca(HCO₃)₂ or Mg(HCO₃)₂, which decompose on heating.", None),
    ("Metals and Non-Metals", "Easy", "Which metal will displace copper from copper(II) tetraoxosulphate(VI) solution?", "silver", "gold", "mercury", "zinc", "D", "Only a metal higher than copper in the activity series can displace it; zinc is more reactive than copper, the others are less reactive.", None),
    ("Industrial Chemistry", "Easy", "The catalyst used in the Contact process for the manufacture of tetraoxosulphate(VI) acid is", "vanadium(V) oxide", "finely divided iron", "nickel", "manganese(IV) oxide", "A", "V₂O₅ catalyses 2SO₂ + O₂ ⇌ 2SO₃ in the Contact process; iron is the Haber-process catalyst.", None),
    ("Chemistry of Biomolecules", "Medium", "A food sample turns blue-black with iodine solution but gives no precipitate with Benedict's solution. The sample contains", "reducing sugar only", "protein only", "starch only", "starch and reducing sugar", "C", "Blue-black with iodine indicates starch; a negative Benedict's test means no reducing sugar.", None),
    ("Chemical Reactions", "Easy", "Zn(s) + CuSO₄(aq) → ZnSO₄(aq) + Cu(s) is an example of a", "neutralisation reaction", "displacement reaction", "decomposition reaction", "double decomposition reaction", "B", "A more reactive metal (zinc) takes the place of a less reactive one (copper) in its compound — a displacement (redox) reaction.", None),
]

BIO = [
    ("Heredity and Variation", "Easy", "In a cross between two heterozygous tall pea plants (Tt × Tt), the expected percentage of short plants in the offspring is", "0%", "25%", "50%", "75%", "B", "Tt × Tt gives TT : Tt : tt in the ratio 1 : 2 : 1; only tt (one quarter) is short."),
    ("Heredity and Variation", "Medium", "A man of blood group AB marries a woman of blood group O. The possible blood groups of their children are", "A and B only", "AB and O only", "A, B, AB and O", "O only", "A", "The father gives either Iᴬ or Iᴮ, the mother always gives i; children are IᴬI (group A) or IᴮI (group B)."),
    ("Heredity and Variation", "Medium", "Colour blindness is a sex-linked recessive trait. A carrier woman marries a man with normal vision. The probability that a son will be colour-blind is", "0%", "25%", "50%", "100%", "C", "Sons get their X chromosome from the mother; she is XᴬXᵃ, so half of her sons receive Xᵃ and are colour-blind."),
    ("Heredity and Variation", "Easy", "Red-flowered and white-flowered four o'clock plants produce offspring with pink flowers. This is an example of", "complete dominance", "codominance", "incomplete dominance", "sex linkage", "C", "Neither allele masks the other; the heterozygote shows a blended (intermediate) phenotype — incomplete dominance."),
    ("Heredity and Variation", "Medium", "A tall plant of unknown genotype was crossed with a short plant (tt). The offspring were 50% tall and 50% short. The genotype of the tall parent is", "TT", "Tt", "tt", "TTt", "B", "This is a test cross; a 1 : 1 ratio means the tall parent gave T half the time and t half the time — it is heterozygous, Tt."),
    ("Nutrition", "Easy", "A food sample gives a brick-red precipitate when boiled with Benedict's solution. The food contains", "starch", "protein", "reducing sugar", "fat", "C", "Benedict's solution changes from blue to brick-red when heated with a reducing sugar such as glucose."),
    ("Nutrition", "Easy", "A food sample rubbed on a piece of paper leaves a translucent spot that does not disappear on drying. The food contains", "protein", "fat or oil", "starch", "vitamin C", "B", "The grease-spot test: fats and oils leave a permanent translucent mark on paper."),
    ("Nutrition", "Medium", "A potted plant was kept in a dark cupboard for 48 hours and a leaf was then tested for starch. The result was negative because", "the leaf had died", "starch cannot be tested in the dark", "the plant used up its stored starch and could not photosynthesise without light", "iodine does not work on old leaves", "C", "Without light there is no photosynthesis; the starch already in the leaf is converted to sugar and used, so the leaf becomes destarched."),
    ("Nutrition", "Medium", "Part of a destarched leaf was covered with black paper and the plant was placed in sunlight for six hours. When tested with iodine, only the uncovered part turned blue-black. This shows that", "chlorophyll is necessary for photosynthesis", "light is necessary for photosynthesis", "carbon(IV) oxide is necessary for photosynthesis", "water is necessary for photosynthesis", "B", "The only difference between the two parts of the leaf was light; starch formed only where light reached."),
    ("Nutrition", "Medium", "A destarched variegated leaf (green and white patches) was exposed to light for several hours and then tested with iodine. Only the green parts turned blue-black. This shows that", "light is necessary for photosynthesis", "oxygen is produced during photosynthesis", "chlorophyll is necessary for photosynthesis", "the white parts have no stomata", "C", "Both parts received light, water and CO₂; only the green parts contain chlorophyll and only they made starch."),
    ("Transport", "Easy", "A red blood cell placed in distilled water swells and bursts because", "water enters the cell by osmosis", "water leaves the cell by osmosis", "salt enters the cell by diffusion", "the cell wall is weak", "A", "Distilled water is hypotonic to the cell contents, so water moves in by osmosis; with no cell wall the cell bursts (haemolysis)."),
    ("Transport", "Easy", "Fresh potato strips placed in a concentrated salt solution for an hour became soft and flabby because", "salt dissolved the cell walls", "the cells gained water and burst", "water moved out of the cells by osmosis", "the starch was converted to sugar", "C", "The salt solution is hypertonic to the cell sap, so water leaves the cells and they become flaccid (plasmolysed)."),
    ("Respiration", "Easy", "Lime water in a sealed flask containing germinating bean seeds turned milky after a few hours. This shows that germinating seeds", "give out oxygen", "give out carbon(IV) oxide", "absorb water", "produce heat", "B", "Lime water turns milky with carbon(IV) oxide, released by the respiring seeds."),
    ("Respiration", "Medium", "During a 100 m sprint an athlete's leg muscles accumulate lactic acid because", "the muscles are respiring aerobically", "oxygen supply cannot meet demand, so anaerobic respiration occurs", "the blood carries too much oxygen", "glucose has run out", "B", "When oxygen cannot be delivered fast enough, muscle cells break down glucose without oxygen, producing lactic acid (oxygen debt)."),
    ("Excretion", "Medium", "On a very hot day a person produces a small volume of concentrated urine because", "the kidneys stop working in heat", "less water is lost through sweat", "more water is reabsorbed in the kidney tubules under the influence of ADH", "the bladder shrinks in heat", "C", "Sweating lowers blood water content; the pituitary releases more ADH, the tubules reabsorb more water and the urine becomes concentrated."),
    ("Coordination and Control", "Easy", "When a person touches a hot pot, the hand is withdrawn before any pain is felt. This is because", "the reflex is coordinated by the spinal cord, not the brain", "pain receptors are slow", "the brain ignores heat", "muscles act without nerves", "A", "A spinal reflex arc (receptor → sensory neurone → spinal cord → motor neurone → muscle) is faster than the message reaching the brain."),
    ("Coordination and Control", "Medium", "A person whose pancreas produces too little insulin is likely to have", "low blood glucose and no glucose in the urine", "high blood glucose and glucose in the urine", "low blood pressure", "excess red blood cells", "B", "Insulin lowers blood glucose; without enough of it, glucose stays high and spills into the urine (diabetes mellitus)."),
    ("Ecology", "Medium", "In the food chain grass → grasshopper → lizard → hawk, if a pesticide kills most of the lizards, the immediate effect will be", "more grasshoppers and fewer hawks", "fewer grasshoppers and more hawks", "more grass and more hawks", "no change in the other populations", "A", "Grasshoppers lose their predator and increase; hawks lose their food and decrease."),
    ("Ecology", "Hard", "A 1 m² quadrat was thrown 10 times at random in a 200 m² field. A total of 50 plants of species X were counted. The estimated population of X in the field is", "50", "500", "1,000", "2,000", "C", "Mean density = 50/10 = 5 plants per m²; population = 5 × 200 = 1,000."),
    ("Ecology", "Medium", "A single mango tree supports thousands of caterpillars, which are eaten by a few dozen birds. The pyramid of numbers for this food chain is", "upright", "inverted at the base", "a straight column", "impossible to draw", "B", "One producer supports many consumers, so the base (the tree) is narrower than the next level — the pyramid is inverted."),
    ("Soil", "Easy", "Water poured onto a soil sample drained through in a few seconds and the soil held very little of it. The soil is most likely", "clay", "loam", "sandy", "humus", "C", "Sandy soil has large particles and large air spaces, so it drains quickly and retains little water."),
    ("Humans and Environment", "Medium", "Untreated sewage was discharged into a river and, a few days later, many fish died. The most likely cause is that", "the sewage poisoned the fish directly", "bacteria decomposing the sewage used up the dissolved oxygen", "the river became too cold", "the fish had no food", "B", "Decomposers multiply on the organic waste and consume dissolved oxygen, so the fish suffocate."),
    ("Evolution", "Medium", "In industrial areas of England, dark-coloured peppered moths became more common than light-coloured ones. The best explanation is that", "soot dyed the moths dark", "dark moths were better camouflaged on soot-covered trees and less often eaten by birds", "light moths migrated away", "dark moths reproduced without mating", "B", "This is natural selection: the better-camouflaged variety survived and reproduced more."),
    ("Reproduction", "Easy", "A flower has small dull petals, no scent, no nectar and long feathery stigmas hanging outside the flower. It is most likely pollinated by", "insects", "birds", "wind", "bats", "C", "Wind-pollinated flowers do not need to attract animals; feathery stigmas catch pollen from the air."),
    ("Growth", "Easy", "A seedling kept in a box with light entering from one side bent towards the light. This response is called", "positive phototropism", "negative geotropism", "hydrotropism", "nastic movement", "A", "Growth of a shoot towards light is positive phototropism, caused by auxin accumulating on the shaded side."),
    ("Support and Movement", "Easy", "When the biceps contracts the triceps relaxes and the arm bends; when the triceps contracts the biceps relaxes and the arm straightens. The two muscles are described as", "voluntary", "antagonistic", "involuntary", "cardiac", "B", "Muscles that produce opposite movements at a joint form an antagonistic pair."),
    ("Cell Structure and Organization", "Easy", "A cell seen under the microscope has a cell wall, chloroplasts and a large central vacuole. It is most likely a", "human cheek cell", "bacterium", "leaf cell", "red blood cell", "C", "Chloroplasts and a cellulose cell wall occur only in plant cells; leaf cells are photosynthetic."),
    ("Variety of Organisms", "Easy", "An animal has moist skin without scales, lays its eggs in water and its young breathe with gills while the adults breathe with lungs. It is", "a reptile", "a fish", "a mammal", "an amphibian", "D", "Amphibians such as frogs and toads have a water-dwelling larval stage (tadpole) and lung-breathing adults."),
]


def build():
    questions, bad = [], []
    for topic, diff, q, a, b, c, d, ans, exp, verify in CHEM:
        item = {"subject": "Chemistry", "topic": topic, "difficulty": diff, "q": q, "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp}
        if verify:
            expected = eval(verify, {"math": math})
            got = _num(item[ans])
            if got is None or abs(got - expected) > max(0.01 * abs(expected), 0.006):
                bad.append((q[:60], ans, item[ans], expected))
        questions.append(item)
    for topic, diff, q, a, b, c, d, ans, exp in BIO:
        questions.append({"subject": "Biology", "topic": topic, "difficulty": diff, "q": q, "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    if bad:
        for b_ in bad:
            print("MISMATCH:", b_)
        sys.exit("Chemistry verification failed — file not written.")
    _balance(questions)
    texts = [x["q"] for x in questions]
    assert len(texts) == len(set(texts)), "duplicate question text"
    assert all(x["answer"] in "ABCD" and all(x[k] for k in "ABCD") for x in questions)
    batch = {
        "batch_id": "batch_002_chemistry_biology",
        "exam_type": "JAMB",
        "note": "Applied Chemistry (calculations verified in Python) and experiment/scenario Biology questions.",
        "passages": [],
        "questions": questions,
        "deactivate": [],
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=1)
    from collections import Counter
    print(f"wrote {OUT}: {len(questions)} questions")
    print("answer letters:", dict(Counter(x['answer'] for x in questions)))
    print("per subject:", dict(Counter(x['subject'] for x in questions)))


if __name__ == "__main__":
    build()
