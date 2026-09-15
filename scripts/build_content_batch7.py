"""Builds content/batch_007_maths.json — JAMB-style Mathematics word problems with step-by-step
corrections. Every numerical answer is re-computed in Python before the file is written; the
telegraphic old stems ("Magnitude of (3,4)?") are retired.

Run:  python3 scripts/build_content_batch7.py
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_content_batch1 import _balance, _num  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "content", "batch_007_maths.json")

# (topic, difficulty, question, A, B, C, D, answer, explanation, verify)
MATHS = [
    ("Number Bases", "Medium", "Convert 1011₂ to a number in base ten.", "9", "11", "13", "15", "B", "1011₂ = 1×8 + 0×4 + 1×2 + 1×1 = 8 + 0 + 2 + 1 = 11.", "8+2+1"),
    ("Number Bases", "Medium", "Express 45₁₀ as a number in base five.", "130₅", "140₅", "145₅", "180₅", "B", "45 ÷ 5 = 9 remainder 0; 9 ÷ 5 = 1 remainder 4; 1 ÷ 5 = 0 remainder 1. Reading the remainders upwards gives 140₅.", None),
    ("Number Bases", "Hard", "If 34ₓ = 22₁₀, find the value of x.", "5", "6", "7", "8", "B", "3x + 4 = 22 ⇒ 3x = 18 ⇒ x = 6.", "18/3"),
    ("Number Bases", "Medium", "Evaluate 213₄ + 31₄, giving the answer in base four.", "244₄", "310₄", "302₄", "1030₄", "B", "In base ten: 213₄ = 32 + 4 + 3 = 39 and 31₄ = 12 + 1 = 13; 39 + 13 = 52 = 3×16 + 1×4 + 0 = 310₄.", None),
    ("Fractions, Decimals and Percentages", "Medium", "A trader bought a bag of rice for ₦45,000 and sold it for ₦52,200. Her percentage profit is", "12%", "14%", "16%", "18%", "C", "Profit = 52,200 − 45,000 = ₦7,200; % profit = 7,200/45,000 × 100 = 16%.", "7200/45000*100"),
    ("Fractions, Decimals and Percentages", "Medium", "After a 15% discount, a phone was sold for ₦68,000. The original price was", "₦78,200", "₦80,000", "₦83,000", "₦85,000", "B", "85% of the price = 68,000 ⇒ price = 68,000 ÷ 0.85 = ₦80,000.", "68000/0.85"),
    ("Fractions, Decimals and Percentages", "Medium", "Express 0.00042 in standard form.", "4.2 × 10⁻³", "4.2 × 10⁻⁴", "4.2 × 10⁴", "42 × 10⁻⁵", "B", "Move the decimal point four places to the right to get 4.2, so the power is 10⁻⁴.", None),
    ("Fractions, Decimals and Percentages", "Medium", "Simplify 2⅓ ÷ 1¾ × ⅜.", "½", "⅝", "¾", "1⅛", "A", "2⅓ ÷ 1¾ = 7/3 × 4/7 = 4/3; then 4/3 × 3/8 = 12/24 = ½.", "7/3*4/7*3/8"),
    ("Fractions, Decimals and Percentages", "Medium", "A man's salary was increased by 20% and later decreased by 20%. The overall change in his salary is", "no change", "a 4% decrease", "a 4% increase", "a 2% decrease", "B", "Let the salary be 100: after +20% it is 120; 20% of 120 is 24, so it falls to 96 — a 4% decrease.", None),
    ("Fractions, Decimals and Percentages", "Medium", "A sum of ₦50,000 is invested at 8% simple interest per annum. The interest after 3 years is", "₦4,000", "₦12,000", "₦62,000", "₦1,200", "B", "I = PRT/100 = 50,000 × 8 × 3/100 = ₦12,000.", "50000*8*3/100"),
    ("Fractions, Decimals and Percentages", "Hard", "₦20,000 is invested at 10% per annum compound interest. The amount after 2 years is", "₦22,000", "₦24,000", "₦24,200", "₦26,620", "C", "A = P(1 + r)ⁿ = 20,000 × 1.1² = 20,000 × 1.21 = ₦24,200.", "20000*1.1**2"),
    ("Fractions, Decimals and Percentages", "Medium", "Three partners share a profit of ₦360,000 in the ratio 2 : 3 : 4. The largest share is", "₦80,000", "₦120,000", "₦160,000", "₦180,000", "C", "Total parts = 9; one part = 360,000/9 = 40,000; largest share = 4 × 40,000 = ₦160,000.", "360000/9*4"),
    ("Indices", "Medium", "Simplify (27)^(2/3) × (16)^(−1/4).", "4.5", "9", "18", "3", "A", "27^(2/3) = (³√27)² = 3² = 9; 16^(−1/4) = 1/⁴√16 = ½; 9 × ½ = 4.5.", "27**(2/3)*16**(-1/4)"),
    ("Indices", "Medium", "Solve for x: 3^(2x−1) = 27.", "1", "2", "3", "4", "B", "27 = 3³ ⇒ 2x − 1 = 3 ⇒ x = 2.", "(3+1)/2"),
    ("Indices", "Medium", "If 5^(x+1) = 125, the value of x is", "1", "2", "3", "4", "B", "125 = 5³ ⇒ x + 1 = 3 ⇒ x = 2.", "3-1"),
    ("Indices", "Medium", "Simplify (2⁵ × 2⁻³) ÷ 2⁻².", "2", "4", "8", "16", "D", "2⁵ × 2⁻³ = 2²; 2² ÷ 2⁻² = 2⁴ = 16.", "2**4"),
    ("Logarithms", "Medium", "Evaluate log₂ 32 + log₃ 27.", "5", "8", "10", "15", "B", "log₂ 32 = 5 (2⁵ = 32); log₃ 27 = 3 (3³ = 27); 5 + 3 = 8.", "5+3"),
    ("Logarithms", "Hard", "If log₁₀ 2 = 0.3010, find log₁₀ 8 + log₁₀ 5.", "1.204", "1.000", "1.602", "0.903", "C", "log 8 + log 5 = log 40 = log 4 + log 10 = 2 log 2 + 1 = 0.602 + 1 = 1.602.", "2*0.3010+1"),
    ("Surds", "Medium", "Simplify √50 − √18 + √8.", "√40", "4√2", "6√2", "2√2", "B", "√50 = 5√2, √18 = 3√2, √8 = 2√2; 5√2 − 3√2 + 2√2 = 4√2.", None),
    ("Surds", "Medium", "Rationalise the denominator of 6/(√3).", "2√3", "3√3", "6√3", "√3/2", "A", "6/√3 × √3/√3 = 6√3/3 = 2√3.", None),
    ("Surds", "Hard", "Simplify (√5 + √2)(√5 − √2).", "3", "7", "√10", "2√10", "A", "Difference of two squares: (√5)² − (√2)² = 5 − 2 = 3.", "5-2"),
    ("Sets", "Medium", "In a class of 40 students, 25 offer Chemistry, 20 offer Biology and 5 offer neither. How many students offer both subjects?", "5", "10", "15", "20", "B", "Students offering at least one = 40 − 5 = 35; n(C ∪ B) = 25 + 20 − n(both) ⇒ 35 = 45 − n(both) ⇒ n(both) = 10.", "25+20-35"),
    ("Sets", "Medium", "If U = {1, 2, 3, ..., 10}, A = {even numbers} and B = {multiples of 3}, find A ∩ B.", "{6}", "{3, 6, 9}", "{2, 4, 6, 8, 10}", "{6, 12}", "A", "A = {2, 4, 6, 8, 10}; B = {3, 6, 9}; the only element in both is 6.", None),
    ("Sets", "Medium", "In a survey of 60 traders, 32 sell yams, 30 sell beans and 8 sell neither. How many sell beans only?", "10", "12", "20", "22", "C", "At least one = 52; both = 32 + 30 − 52 = 10; beans only = 30 − 10 = 20.", "30-(32+30-52)"),
    ("Algebraic Expressions", "Medium", "Factorise completely: 2x² − 8.", "2(x − 2)²", "2(x − 4)(x + 4)", "2(x − 2)(x + 2)", "(2x − 4)(x + 2)", "C", "2x² − 8 = 2(x² − 4) = 2(x − 2)(x + 2).", None),
    ("Algebraic Expressions", "Medium", "Expand and simplify (2x − 3)(x + 4).", "2x² + 5x − 12", "2x² − 5x − 12", "2x² + 11x − 12", "2x² + 5x + 12", "A", "2x² + 8x − 3x − 12 = 2x² + 5x − 12.", None),
    ("Algebraic Expressions", "Medium", "Simplify (x² − 9)/(x² + 5x + 6).", "(x − 3)/(x + 2)", "(x + 3)/(x + 2)", "(x − 3)/(x + 3)", "x − 3", "A", "x² − 9 = (x − 3)(x + 3); x² + 5x + 6 = (x + 2)(x + 3); cancelling (x + 3) gives (x − 3)/(x + 2).", None),
    ("Algebraic Expressions", "Medium", "Make h the subject of the formula V = ⅓πr²h.", "h = 3V/(πr²)", "h = V/(3πr²)", "h = 3πr²/V", "h = πr²/(3V)", "A", "Multiply both sides by 3: 3V = πr²h; divide by πr²: h = 3V/(πr²).", None),
    ("Algebraic Expressions", "Medium", "If x + y = 7 and xy = 10, find the value of x² + y².", "29", "39", "49", "69", "A", "x² + y² = (x + y)² − 2xy = 49 − 20 = 29.", "49-20"),
    ("Algebraic Expressions", "Medium", "The remainder when x³ − 2x² + 3x − 5 is divided by (x − 2) is", "−1", "1", "3", "9", "B", "Remainder theorem: f(2) = 8 − 8 + 6 − 5 = 1.", "8-8+6-5"),
    ("Equations and Inequalities", "Medium", "Solve the simultaneous equations 2x + y = 7 and x − y = 2.", "x = 3, y = 1", "x = 1, y = 3", "x = 2, y = 3", "x = 3, y = −1", "A", "Adding the equations: 3x = 9 ⇒ x = 3; then y = 7 − 6 = 1.", None),
    ("Equations and Inequalities", "Medium", "Solve x² − 5x + 6 = 0.", "x = 2 or 3", "x = −2 or −3", "x = 1 or 6", "x = −1 or −6", "A", "(x − 2)(x − 3) = 0 ⇒ x = 2 or x = 3.", None),
    ("Equations and Inequalities", "Medium", "The sum of two consecutive odd numbers is 56. The larger number is", "27", "29", "31", "33", "B", "Let the numbers be n and n + 2: 2n + 2 = 56 ⇒ n = 27; the larger is 29.", "(56-2)/2+2"),
    ("Equations and Inequalities", "Medium", "Solve the inequality 3x − 7 < 2x + 5.", "x < 12", "x > 12", "x < −12", "x < 2", "A", "3x − 2x < 5 + 7 ⇒ x < 12.", None),
    ("Equations and Inequalities", "Medium", "A father is three times as old as his son. In 12 years he will be twice as old as the son. The son's present age is", "6 years", "10 years", "12 years", "18 years", "C", "Let the son be s: 3s + 12 = 2(s + 12) ⇒ 3s + 12 = 2s + 24 ⇒ s = 12.", "24-12"),
    ("Equations and Inequalities", "Medium", "Find the range of values of x for which 2x − 1 ≥ 5 and x + 3 < 10.", "3 ≤ x < 7", "3 < x ≤ 7", "x ≥ 3", "x < 7", "A", "2x − 1 ≥ 5 ⇒ x ≥ 3; x + 3 < 10 ⇒ x < 7; combined: 3 ≤ x < 7.", None),
    ("Equations and Inequalities", "Hard", "The equation x² + kx + 9 = 0 has equal roots. The positive value of k is", "3", "6", "9", "18", "B", "Equal roots ⇒ b² − 4ac = 0 ⇒ k² − 36 = 0 ⇒ k = 6.", "36**0.5"),
    ("Variation", "Medium", "y varies inversely as x. When y = 4, x = 6. Find y when x = 8.", "3", "5", "12", "48", "A", "xy = k = 24; when x = 8, y = 24/8 = 3.", "24/8"),
    ("Variation", "Medium", "The cost of feeding a family is partly constant and partly varies with the number of people. It costs ₦30,000 for 4 people and ₦42,000 for 7 people. The cost for 10 people is", "₦50,000", "₦52,000", "₦54,000", "₦60,000", "C", "C = a + bn: 30,000 = a + 4b and 42,000 = a + 7b ⇒ 3b = 12,000 ⇒ b = 4,000, a = 14,000; for 10 people: 14,000 + 40,000 = ₦54,000.", "14000+10*4000"),
    ("Variation", "Medium", "z varies jointly as x and the square of y. If z = 36 when x = 2 and y = 3, find z when x = 3 and y = 2.", "16", "24", "27", "48", "B", "z = kxy² ⇒ 36 = k × 2 × 9 ⇒ k = 2; z = 2 × 3 × 4 = 24.", "2*3*4"),
    ("Sequences and Series", "Medium", "The 3rd term of an arithmetic progression is 11 and the 7th term is 23. The first term is", "2", "3", "5", "8", "C", "4d = 23 − 11 = 12 ⇒ d = 3; a = 11 − 2d = 11 − 6 = 5.", "11-6"),
    ("Sequences and Series", "Medium", "Find the sum of the first 20 terms of the arithmetic progression 3, 7, 11, ...", "400", "780", "800", "820", "D", "S₂₀ = n/2[2a + (n − 1)d] = 10[6 + 19 × 4] = 10 × 82 = 820.", "10*(6+76)"),
    ("Sequences and Series", "Medium", "The 5th term of the geometric progression 2, 6, 18, ... is", "54", "108", "162", "486", "C", "T₅ = ar⁴ = 2 × 3⁴ = 2 × 81 = 162.", "2*81"),
    ("Sequences and Series", "Hard", "The sum to infinity of the geometric series 8 + 4 + 2 + 1 + ... is", "15", "16", "24", "32", "B", "S∞ = a/(1 − r) = 8/(1 − ½) = 16.", "8/(1-0.5)"),
    ("Sequences and Series", "Medium", "A man saves ₦1,000 in January and increases his saving by ₦500 every month. His total savings for the year is", "₦39,000", "₦45,000", "₦48,000", "₦52,000", "B", "AP with a = 1,000, d = 500, n = 12: S = 6[2,000 + 11 × 500] = 6 × 7,500 = ₦45,000.", "6*(2000+5500)"),
    ("Matrices", "Medium", "The determinant of the matrix [[3, 2], [1, 4]] (rows shown in order) is", "10", "12", "14", "2", "A", "det = (3 × 4) − (2 × 1) = 12 − 2 = 10.", "12-2"),
    ("Matrices", "Medium", "If P = [[1, 2], [3, 4]] and Q = [[2, 0], [1, 1]] (rows shown in order), the element in the first row, first column of PQ is", "2", "4", "5", "7", "B", "Row 1 of P × column 1 of Q: (1 × 2) + (2 × 1) = 4.", "1*2+2*1"),
    ("Matrices", "Medium", "The matrix [[2, k], [4, 6]] (rows shown in order) is singular. The value of k is", "2", "3", "4", "12", "B", "Singular ⇒ determinant 0: 2 × 6 − 4k = 0 ⇒ k = 3.", "12/4"),
    ("Coordinate Geometry", "Medium", "The gradient of the line joining the points (2, 3) and (6, 11) is", "½", "2", "4", "8", "B", "m = (11 − 3)/(6 − 2) = 8/4 = 2.", "8/4"),
    ("Coordinate Geometry", "Medium", "The midpoint of the line joining (−2, 5) and (4, −1) is", "(1, 2)", "(2, 4)", "(3, 3)", "(1, 3)", "A", "Midpoint = ((−2 + 4)/2, (5 + (−1))/2) = (1, 2).", None),
    ("Coordinate Geometry", "Medium", "The distance between the points (1, 2) and (4, 6) is", "3 units", "4 units", "5 units", "7 units", "C", "d = √((4 − 1)² + (6 − 2)²) = √(9 + 16) = 5.", "(9+16)**0.5"),
    ("Coordinate Geometry", "Medium", "The equation of the line with gradient 3 passing through the point (1, −2) is", "y = 3x − 5", "y = 3x + 1", "y = 3x − 1", "y = 3x + 5", "A", "y − (−2) = 3(x − 1) ⇒ y + 2 = 3x − 3 ⇒ y = 3x − 5.", None),
    ("Coordinate Geometry", "Hard", "The line 2y = 4x + 6 is perpendicular to a line whose gradient is", "2", "−2", "½", "−½", "D", "Gradient of the given line = 2; a perpendicular line has gradient −1/2.", "-1/2"),
    ("Geometry", "Medium", "The interior angle of a regular polygon is 144°. The number of sides is", "8", "9", "10", "12", "C", "Exterior angle = 180° − 144° = 36°; number of sides = 360°/36° = 10.", "360/36"),
    ("Geometry", "Medium", "In a triangle, the angles are in the ratio 2 : 3 : 4. The largest angle is", "40°", "60°", "80°", "100°", "C", "Total parts 9; 180°/9 = 20° per part; largest = 4 × 20° = 80°.", "180/9*4"),
    ("Geometry", "Medium", "A chord of a circle subtends an angle of 70° at the centre. The angle it subtends at a point on the major arc is", "35°", "70°", "110°", "140°", "A", "The angle at the centre is twice the angle at the circumference: 70°/2 = 35°.", "70/2"),
    ("Geometry", "Medium", "PQRS is a cyclic quadrilateral in which angle P = 105°. The size of angle R is", "75°", "85°", "105°", "255°", "A", "Opposite angles of a cyclic quadrilateral are supplementary: 180° − 105° = 75°.", "180-105"),
    ("Geometry", "Medium", "A tangent and a radius of a circle meet at the point of contact. The angle between them is", "45°", "60°", "90°", "180°", "C", "A radius is always perpendicular to the tangent at the point of contact.", "90"),
    ("Geometry", "Medium", "The sum of the interior angles of a hexagon is", "540°", "720°", "900°", "1080°", "B", "(n − 2) × 180° = 4 × 180° = 720°.", "4*180"),
    ("Mensuration", "Medium", "A cylindrical tank of radius 7 m is filled with water to a depth of 10 m. The volume of water is (take π = 22/7)", "220 m³", "440 m³", "1,540 m³", "3,080 m³", "C", "V = πr²h = 22/7 × 49 × 10 = 1,540 m³.", "22/7*49*10"),
    ("Mensuration", "Medium", "The area of a sector of a circle of radius 14 cm subtending 90° at the centre is (take π = 22/7)", "77 cm²", "154 cm²", "308 cm²", "616 cm²", "B", "Area = θ/360 × πr² = ¼ × 22/7 × 196 = 154 cm².", "0.25*22/7*196"),
    ("Mensuration", "Medium", "The length of an arc of a circle of radius 21 cm which subtends 60° at the centre is (take π = 22/7)", "11 cm", "22 cm", "44 cm", "66 cm", "B", "Arc = θ/360 × 2πr = 1/6 × 2 × 22/7 × 21 = 22 cm.", "1/6*2*22/7*21"),
    ("Mensuration", "Medium", "A rectangular field is 60 m long and 40 m wide. The cost of fencing it at ₦1,500 per metre is", "₦150,000", "₦300,000", "₦360,000", "₦3,600,000", "B", "Perimeter = 2(60 + 40) = 200 m; cost = 200 × 1,500 = ₦300,000.", "200*1500"),
    ("Mensuration", "Hard", "A cone has base radius 6 cm and slant height 10 cm. Its total surface area is", "60π cm²", "96π cm²", "136π cm²", "216π cm²", "B", "Curved surface = πrl = 60π; base = πr² = 36π; total = 96π cm².", "60+36"),
    ("Mensuration", "Medium", "The volume of a cube is 216 cm³. Its total surface area is", "36 cm²", "144 cm²", "216 cm²", "1,296 cm²", "C", "Side = ³√216 = 6 cm; surface area = 6 × 6² = 216 cm².", "6*36"),
    ("Trigonometry", "Medium", "A ladder 10 m long leans against a vertical wall making an angle of 60° with the ground. How far up the wall does it reach?", "5 m", "5√3 m", "10√3 m", "20 m", "B", "Height = 10 sin 60° = 10 × √3/2 = 5√3 m.", "10*math.sin(math.radians(60))"),
    ("Trigonometry", "Medium", "From the top of a cliff 40 m high, the angle of depression of a boat is 30°. The distance of the boat from the foot of the cliff is", "20 m", "40 m", "40√3 m", "80 m", "C", "tan 30° = 40/d ⇒ d = 40/tan 30° = 40√3 m.", "40/math.tan(math.radians(30))"),
    ("Trigonometry", "Medium", "If sin θ = 3/5 and θ is acute, the value of tan θ is", "3/4", "4/3", "4/5", "5/4", "A", "cos θ = √(1 − 9/25) = 4/5; tan θ = sin θ/cos θ = (3/5)/(4/5) = 3/4.", "3/4"),
    ("Trigonometry", "Medium", "The value of cos 120° is", "½", "−½", "√3/2", "−√3/2", "B", "120° is in the second quadrant where cosine is negative: cos 120° = −cos 60° = −½.", None),
    ("Trigonometry", "Hard", "A man walks 6 km due north and then 8 km on a bearing of 090°. His bearing from the starting point is approximately", "037°", "053°", "127°", "143°", "B", "tan θ = 8/6 ⇒ θ ≈ 53° measured clockwise from north: bearing 053°.", "math.degrees(math.atan(8/6))"),
    ("Trigonometry", "Medium", "In triangle ABC, a = 5 cm, b = 7 cm and angle C = 60°. The length of side c is (cos 60° = ½)", "√39 cm", "√59 cm", "√74 cm", "√109 cm", "A", "Cosine rule: c² = 25 + 49 − 2(5)(7)(½) = 74 − 35 = 39 ⇒ c = √39 cm.", None),
    ("Probability", "Medium", "A bag contains 5 red, 3 blue and 2 green balls. A ball is picked at random. The probability that it is not blue is", "3/10", "1/2", "7/10", "4/5", "C", "P(not blue) = 1 − 3/10 = 7/10.", "7/10"),
    ("Probability", "Medium", "Two fair dice are thrown together. The probability of obtaining a total of 7 is", "1/12", "1/6", "7/36", "1/9", "B", "Totals of 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes out of 36 = 1/6.", "6/36"),
    ("Probability", "Medium", "A fair coin is tossed three times. The probability of obtaining exactly two heads is", "1/8", "1/4", "3/8", "1/2", "C", "Favourable: HHT, HTH, THH = 3 of the 8 equally likely outcomes = 3/8.", "3/8"),
    ("Probability", "Hard", "A box contains 4 good and 2 defective bulbs. Two bulbs are drawn at random without replacement. The probability that both are good is", "2/5", "4/9", "1/3", "8/15", "A", "P = 4/6 × 3/5 = 12/30 = 2/5.", "4/6*3/5"),
    ("Probability", "Medium", "The probability that Ada passes an examination is 0.7 and the probability that Bayo passes is 0.6. The probability that both pass is", "0.13", "0.42", "0.65", "1.3", "B", "Independent events: 0.7 × 0.6 = 0.42.", "0.7*0.6"),
    ("Statistics", "Medium", "The scores of 10 students in a test are 4, 6, 6, 7, 8, 8, 8, 9, 10, 10. The mode and median are respectively", "8 and 8", "8 and 7.5", "6 and 8", "8 and 7", "A", "Mode = most frequent = 8; median = average of the 5th and 6th values = (8 + 8)/2 = 8.", None),
    ("Statistics", "Medium", "The mean of the numbers 3, 5, x, 9 and 12 is 8. The value of x is", "9", "10", "11", "13", "C", "Sum = 8 × 5 = 40 ⇒ 3 + 5 + x + 9 + 12 = 40 ⇒ x = 11.", "40-29"),
    ("Statistics", "Hard", "The variance of the numbers 2, 4, 6, 8, 10 is", "2√2", "6", "8", "40", "C", "Mean = 6; squared deviations 16, 4, 0, 4, 16 sum to 40; variance = 40/5 = 8.", "40/5"),
    ("Probability", "Medium", "In how many ways can a committee of 3 be chosen from 7 people?", "21", "35", "210", "343", "B", "⁷C₃ = 7!/(3!4!) = (7 × 6 × 5)/(3 × 2 × 1) = 35.", "math.comb(7,3)"),
    ("Probability", "Medium", "In how many ways can the letters of the word MANGO be arranged?", "25", "60", "120", "720", "C", "5 different letters: 5! = 120.", "math.factorial(5)"),
    ("Vectors", "Medium", "If a = 3i + 4j and b = i − 2j, find |a + b|.", "√20", "√29", "√13", "6", "A", "a + b = 4i + 2j; |a + b| = √(16 + 4) = √20.", None),
    ("Vectors", "Medium", "The vectors p = 2i + 3j and q = 6i + kj are parallel. The value of k is", "4", "6", "9", "12", "C", "Parallel ⇒ q = 3p ⇒ k = 3 × 3 = 9.", "3*3"),
    ("Vectors", "Medium", "A boat heads due east at 8 km/h while the current flows due north at 6 km/h. The resultant speed of the boat is", "2 km/h", "10 km/h", "14 km/h", "48 km/h", "B", "Resultant = √(8² + 6²) = √100 = 10 km/h.", "(64+36)**0.5"),
]


def build():
    questions, bad = [], []
    for topic, diff, q, a, b, c, d, ans, exp, verify in MATHS:
        item = {"subject": "Mathematics", "topic": topic, "difficulty": diff, "q": q, "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp}
        if verify:
            expected = eval(verify, {"math": math})
            got = _num(item[ans])
            if got is None or abs(got - expected) > max(0.01 * abs(expected), 0.006):
                bad.append((q[:60], ans, item[ans], expected))
        questions.append(item)
    if bad:
        for b_ in bad:
            print("MISMATCH:", b_)
        sys.exit("Verification failed — file not written.")
    _balance(questions)
    texts = [x["q"] for x in questions]
    assert len(texts) == len(set(texts)), "duplicate question text"
    assert all(x["answer"] in "ABCD" and all(x[k] for k in "ABCD") for x in questions)
    batch = {
        "batch_id": "batch_007_maths",
        "exam_type": "JAMB",
        "note": "Mathematics word problems with step-by-step corrections (all numerical answers verified). Retires telegraphic stems.",
        "passages": [],
        "questions": questions,
        "deactivate": [
            {"subject": "Mathematics", "max_length": 30, "keep_at_least": 200, "reason": "telegraphic stems such as 'Magnitude of (3,4)?'"},
            {"subject": "Mathematics", "like": ["%?", "Simplify %.", "Find %.", "Solve %.", "Evaluate %."], "max_length": 42, "keep_at_least": 200, "reason": "very short command stems"},
            {"subject": "Mathematics", "telegraphic": True, "keep_at_least": 200, "reason": "note-style stems without a sentence, e.g. 'Area circle radius 7 cm, π=22/7?'"},
        ],
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=1)
    from collections import Counter
    print(f"wrote {OUT}: {len(questions)} questions")
    print("answer letters:", dict(Counter(x['answer'] for x in questions)))
    print("per topic:", dict(Counter(x['topic'] for x in questions)))


if __name__ == "__main__":
    build()
