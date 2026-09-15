"""Builds content/batch_009_maths_round2.json — more JAMB Mathematics: commercial arithmetic,
statistics from a frequency table, calculus, binary operations, bearings, circle theorems and
longitude/latitude, all with worked corrections. Also retires the weakest remaining one-liners.

Run:  python3 scripts/build_content_batch9.py
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_content_batch1 import _balance, _num  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "content", "batch_009_maths_round2.json")

TABLE = ("Frequency table: marks scored by 20 students in a test",
         "Marks scored by 20 students in a test\n"
         "Mark        2    3    4    5    6\n"
         "Frequency   3    5    6    4    2")

TABLE_Q = [
    ("Statistics", "Medium", "From the table above, the mean mark is", "3.85", "4.00", "4.10", "4.25", "A", "Σfx = 2×3 + 3×5 + 4×6 + 5×4 + 6×2 = 6 + 15 + 24 + 20 + 12 = 77; mean = 77/20 = 3.85.", "77/20"),
    ("Statistics", "Easy", "From the table above, the modal mark is", "3", "4", "5", "6", "B", "The mode is the mark with the highest frequency: 4 (frequency 6).", "4"),
    ("Statistics", "Medium", "From the table above, the median mark is", "3", "3.5", "4", "4.5", "C", "Cumulative frequencies: 3, 8, 14, 18, 20. The 10th and 11th values both lie in the mark 4 group, so the median is 4.", "4"),
    ("Probability", "Medium", "From the table above, a student is chosen at random. The probability that the student scored at least 5 marks is", "1/5", "3/10", "1/4", "7/10", "B", "Students with 5 or 6 marks = 4 + 2 = 6; probability = 6/20 = 3/10.", "6/20"),
]

MATHS = [
    ("Number Bases", "Medium", "If 41ₓ = 29₁₀, find the value of x.", "5", "6", "7", "8", "C", "4x + 1 = 29 ⇒ 4x = 28 ⇒ x = 7.", "28/4"),
    ("Number Bases", "Medium", "Evaluate 1101₂ × 11₂, giving the answer in base two.", "100111₂", "101011₂", "110011₂", "111001₂", "A", "1101₂ = 13 and 11₂ = 3; 13 × 3 = 39 = 32 + 4 + 2 + 1 = 100111₂.", None),
    ("Fractions, Decimals and Percentages", "Medium", "A trader bought 50 shirts at ₦1,200 each. He sold 30 of them at ₦1,800 each and the rest at ₦1,000 each. His percentage profit on the whole transaction is", "20%", "23.3%", "25%", "30%", "B", "Cost = 60,000; revenue = 30 × 1,800 + 20 × 1,000 = 54,000 + 20,000 = 74,000; profit = 14,000; 14,000/60,000 × 100 = 23.3%.", "14000/60000*100"),
    ("Fractions, Decimals and Percentages", "Medium", "A television costs ₦120,000 cash. On hire purchase a buyer pays a deposit of ₦30,000 and 12 monthly instalments of ₦9,000. How much more than the cash price does the hire-purchase buyer pay?", "₦8,000", "₦12,000", "₦18,000", "₦30,000", "C", "Hire-purchase total = 30,000 + 12 × 9,000 = 138,000; extra = 138,000 − 120,000 = ₦18,000.", "138000-120000"),
    ("Fractions, Decimals and Percentages", "Medium", "A car bought for ₦4,000,000 depreciates by 10% each year. Its value after 2 years is", "₦3,200,000", "₦3,240,000", "₦3,600,000", "₦3,800,000", "B", "Value = 4,000,000 × 0.9² = 4,000,000 × 0.81 = ₦3,240,000.", "4000000*0.81"),
    ("Fractions, Decimals and Percentages", "Medium", "A shopkeeper adds 7.5% VAT to a bill of ₦24,000. The customer pays", "₦25,800", "₦25,200", "₦26,400", "₦31,500", "A", "VAT = 7.5% of 24,000 = 1,800; total = ₦25,800.", "24000*1.075"),
    ("Fractions, Decimals and Percentages", "Medium", "If 12 men can build a wall in 15 days, how many days will 20 men take working at the same rate?", "8 days", "9 days", "10 days", "12 days", "B", "Inverse proportion: 12 × 15 = 180 man-days; 180/20 = 9 days.", "180/20"),
    ("Fractions, Decimals and Percentages", "Medium", "A man spends ¼ of his salary on rent, ⅓ on food and saves the remaining ₦60,000. His salary is", "₦120,000", "₦144,000", "₦150,000", "₦180,000", "B", "Fraction spent = ¼ + ⅓ = 7/12; savings = 5/12 of salary = 60,000 ⇒ salary = 60,000 × 12/5 = ₦144,000.", "60000*12/5"),
    ("Fractions, Decimals and Percentages", "Hard", "The population of a town increases by 5% every year. If it is now 80,000, its population 2 years ago was approximately", "72,000", "72,562", "76,190", "88,200", "B", "P × 1.05² = 80,000 ⇒ P = 80,000/1.1025 ≈ 72,562.", "80000/1.1025"),
    ("Fractions, Decimals and Percentages", "Medium", "Correct 0.004586 to three significant figures.", "0.004", "0.0045", "0.00459", "0.005", "C", "The first significant figure is 4; the third is 8, and the next digit 6 rounds it up: 0.00459.", None),
    ("Indices", "Medium", "Solve for x: 4ˣ = 8^(x−1).", "1", "2", "3", "4", "C", "2^(2x) = 2^(3x−3) ⇒ 2x = 3x − 3 ⇒ x = 3.", "3"),
    ("Indices", "Medium", "Evaluate (0.0016)^(1/4).", "0.02", "0.04", "0.2", "0.4", "C", "0.0016 = (0.2)⁴, so the fourth root is 0.2.", "0.0016**0.25"),
    ("Logarithms", "Medium", "Solve log₃(x + 2) = 2.", "5", "7", "9", "11", "B", "Rewrite in index form: x + 2 = 3² = 9, so x = 7.", "9-2"),
    ("Logarithms", "Medium", "Simplify log₁₀ 50 + log₁₀ 2 − log₁₀ 10.", "0", "1", "2", "10", "B", "Combine using the log laws: log(50 × 2 ÷ 10) = log₁₀ 10 = 1.", "1"),
    ("Logarithms", "Hard", "If log₂ x + log₂ (x − 2) = 3, the value of x is", "2", "4", "6", "8", "B", "log₂[x(x − 2)] = 3 ⇒ x² − 2x = 8 ⇒ (x − 4)(x + 2) = 0 ⇒ x = 4 (x must be positive and greater than 2).", "4"),
    ("Surds", "Medium", "Simplify (√12 + √27)/√3.", "3", "5", "√5", "5√3", "B", "√12 = 2√3 and √27 = 3√3; (2√3 + 3√3)/√3 = 5√3/√3 = 5.", "5"),
    ("Surds", "Medium", "Express 1/(3 − √2) with a rational denominator.", "(3 + √2)/7", "(3 − √2)/7", "(3 + √2)/11", "3 + √2", "A", "Multiply numerator and denominator by (3 + √2): denominator = 9 − 2 = 7.", None),
    ("Sets", "Hard", "In a class of 60 students, 30 offer Physics, 28 offer Chemistry and 25 offer Biology. Twelve offer Physics and Chemistry, 10 offer Physics and Biology, 8 offer Chemistry and Biology, and 5 offer all three. How many offer none of the three subjects?", "2", "4", "6", "8", "A", "n(P ∪ C ∪ B) = 30 + 28 + 25 − 12 − 10 − 8 + 5 = 58; none = 60 − 58 = 2.", "60-(30+28+25-12-10-8+5)"),
    ("Sets", "Medium", "Given that P = {x : x is a prime number less than 12} and Q = {x : x is an odd number less than 12}, find P ∩ Q.", "{3, 5, 7, 11}", "{1, 3, 5, 7, 11}", "{2, 3, 5, 7, 11}", "{1, 3, 5, 7, 9, 11}", "A", "P = {2, 3, 5, 7, 11}; Q = {1, 3, 5, 7, 9, 11}; common elements: {3, 5, 7, 11}.", None),
    ("Sets", "Medium", "If a set has 5 elements, the number of its subsets is", "10", "25", "31", "32", "D", "A set with n elements has 2ⁿ subsets: 2⁵ = 32 (including the empty set and the set itself).", "2**5"),
    ("Algebraic Expressions", "Medium", "If (3x + 1)/((x − 1)(x + 2)) = A/(x − 1) + B/(x + 2), the value of A is", "4/3", "5/3", "2", "3", "A", "Put x = 1: 3(1) + 1 = A(1 + 2) ⇒ 4 = 3A ⇒ A = 4/3.", "4/3"),
    ("Algebraic Expressions", "Medium", "If (x − 2) is a factor of x³ + kx² − 4x + 8, the value of k is", "−4", "−2", "2", "4", "B", "f(2) = 0: 8 + 4k − 8 + 8 = 0 ⇒ 4k = −8 ⇒ k = −2.", "-2"),
    ("Algebraic Expressions", "Medium", "Simplify 2/(x − 1) − 1/(x + 1).", "(x + 3)/(x² − 1)", "(x + 1)/(x² − 1)", "1/(x² − 1)", "(3x + 1)/(x² − 1)", "A", "LCM is (x − 1)(x + 1): [2(x + 1) − (x − 1)]/(x² − 1) = (x + 3)/(x² − 1).", None),
    ("Algebraic Expressions", "Medium", "Express x² − 6x + 2 in the form (x − a)² − b.", "(x − 3)² − 7", "(x − 3)² + 7", "(x − 6)² − 34", "(x + 3)² − 7", "A", "Complete the square: (x − 3)² = x² − 6x + 9, so x² − 6x + 2 = (x − 3)² − 7.", None),
    ("Equations and Inequalities", "Medium", "The roots of the equation 2x² − 7x + 3 = 0 are", "½ and 3", "−½ and −3", "1 and 3/2", "−1 and 3/2", "A", "(2x − 1)(x − 3) = 0 ⇒ x = ½ or x = 3.", None),
    ("Equations and Inequalities", "Medium", "If α and β are the roots of x² − 5x + 6 = 0, the value of α² + β² is", "11", "13", "25", "37", "B", "α + β = 5, αβ = 6; α² + β² = (α + β)² − 2αβ = 25 − 12 = 13.", "25-12"),
    ("Equations and Inequalities", "Medium", "A rectangular garden has a perimeter of 28 m and an area of 48 m². Its length is", "6 m", "7 m", "8 m", "12 m", "C", "l + b = 14 and lb = 48 ⇒ the numbers are 8 and 6; length = 8 m.", "8"),
    ("Equations and Inequalities", "Medium", "Solve the inequality (x − 1)/2 − (x + 2)/3 ≥ 1.", "x ≥ 13", "x ≤ 13", "x ≥ 7", "x ≥ −13", "A", "Multiply by 6: 3(x − 1) − 2(x + 2) ≥ 6 ⇒ 3x − 3 − 2x − 4 ≥ 6 ⇒ x ≥ 13.", None),
    ("Equations and Inequalities", "Hard", "Find the values of x for which x² − 3x − 10 < 0.", "−2 < x < 5", "x < −2 or x > 5", "−5 < x < 2", "x < −5 or x > 2", "A", "(x − 5)(x + 2) < 0 ⇒ the product is negative between the roots: −2 < x < 5.", None),
    ("Equations and Inequalities", "Medium", "Two numbers differ by 3 and their product is 40. The smaller number, if both are positive, is", "4", "5", "8", "10", "B", "x(x + 3) = 40 ⇒ x² + 3x − 40 = 0 ⇒ (x + 8)(x − 5) = 0 ⇒ x = 5.", "5"),
    ("Binary Operations", "Medium", "A binary operation * is defined on the set of real numbers by a * b = a + b − 2ab. Evaluate 3 * (−2).", "13", "−11", "1", "−1", "A", "3 + (−2) − 2(3)(−2) = 1 + 12 = 13.", "3+(-2)-2*3*(-2)"),
    ("Binary Operations", "Medium", "The operation ⊕ is defined on the set of integers by m ⊕ n = m + n + 1. The identity element is", "−1", "0", "1", "2", "A", "m ⊕ e = m ⇒ m + e + 1 = m ⇒ e = −1.", "-1"),
    ("Binary Operations", "Hard", "If x * y = x² − y² for real numbers x and y, evaluate (3 * 2) * 1.", "24", "25", "5", "4", "A", "3 * 2 = 9 − 4 = 5; then 5 * 1 = 25 − 1 = 24.", "24"),
    ("Variation", "Medium", "The time taken to complete a journey varies inversely as the average speed. A bus travelling at 60 km/h takes 4 hours. At 80 km/h the journey takes", "2 hours", "2½ hours", "3 hours", "5⅓ hours", "C", "Distance = 60 × 4 = 240 km; at 80 km/h, time = 240/80 = 3 hours.", "240/80"),
    ("Variation", "Hard", "The resistance R of a wire varies directly as its length L and inversely as the square of its diameter d. If R = 4 ohms when L = 20 m and d = 2 mm, find R when L = 30 m and d = 4 mm.", "1.5 ohms", "3 ohms", "6 ohms", "12 ohms", "A", "R = kL/d²: 4 = 20k/4 ⇒ k = 0.8; R = 0.8 × 30/16 = 1.5 ohms.", "0.8*30/16"),
    ("Sequences and Series", "Medium", "The sum of the first n terms of an arithmetic progression is given by Sₙ = 2n² + 3n. The 5th term is", "21", "23", "25", "55", "A", "T₅ = S₅ − S₄ = (50 + 15) − (32 + 12) = 65 − 44 = 21.", "65-44"),
    ("Sequences and Series", "Medium", "The second and fourth terms of a geometric progression are 6 and 54 respectively. The common ratio, if positive, is", "2", "3", "6", "9", "B", "ar³/ar = 54/6 = 9 ⇒ r² = 9 ⇒ r = 3.", "3"),
    ("Sequences and Series", "Medium", "How many terms of the arithmetic progression 2, 5, 8, ... add up to 155?", "8", "9", "10", "11", "C", "n/2[4 + 3(n − 1)] = 155 ⇒ n(3n + 1) = 310 ⇒ 3n² + n − 310 = 0 ⇒ (3n + 31)(n − 10) = 0 ⇒ n = 10.", "10"),
    ("Sequences and Series", "Medium", "A ball dropped from a height of 16 m bounces back to half its previous height each time. The total distance it travels before coming to rest is", "32 m", "48 m", "64 m", "infinite", "B", "Downward distances: 16 + 8 + 4 + ... = 32 m; upward: 8 + 4 + 2 + ... = 16 m; total = 48 m.", "48"),
    ("Matrices", "Medium", "If [[2, 1], [3, x]] (rows shown in order) has determinant 5, the value of x is", "1", "2", "4", "8", "C", "2x − 3 = 5 ⇒ 2x = 8 ⇒ x = 4.", "4"),
    ("Matrices", "Medium", "The inverse of the matrix [[3, 1], [5, 2]] (rows shown in order) is", "[[2, −1], [−5, 3]]", "[[2, 1], [5, 3]]", "[[3, −1], [−5, 2]]", "[[−2, 1], [5, −3]]", "A", "Determinant = 6 − 5 = 1; inverse = (1/1)[[2, −1], [−5, 3]].", None),
    ("Matrices", "Medium", "If P = [[1, 2], [0, 1]] (rows shown in order), then P² is", "[[1, 4], [0, 1]]", "[[1, 2], [0, 1]]", "[[2, 4], [0, 2]]", "[[1, 4], [0, 2]]", "A", "Row 1 × column 2: 1×2 + 2×1 = 4; the other entries are 1, 0, 1.", None),
    ("Coordinate Geometry", "Medium", "The point P divides the line joining A(1, 2) and B(7, 11) internally in the ratio 1 : 2. The coordinates of P are", "(3, 5)", "(4, 6.5)", "(5, 8)", "(2, 3)", "A", "P = ((2×1 + 1×7)/3, (2×2 + 1×11)/3) = (9/3, 15/3) = (3, 5).", None),
    ("Coordinate Geometry", "Medium", "The line 3x + 4y = 12 cuts the x-axis at P and the y-axis at Q. The length PQ is", "3 units", "4 units", "5 units", "7 units", "C", "P = (4, 0) and Q = (0, 3); PQ = √(16 + 9) = 5.", "5"),
    ("Coordinate Geometry", "Medium", "The equation of the line through (2, 5) parallel to the line y = 2x − 7 is", "y = 2x + 1", "y = 2x − 1", "y = −½x + 6", "y = 2x + 5", "A", "Parallel lines share gradient 2: y − 5 = 2(x − 2) ⇒ y = 2x + 1.", None),
    ("Coordinate Geometry", "Medium", "The angle which the line y = √3 x + 2 makes with the positive x-axis is", "30°", "45°", "60°", "90°", "C", "Gradient = tan θ = √3 ⇒ θ = 60°.", "60"),
    ("Geometry", "Medium", "The angles of a pentagon are x°, 2x°, 3x°, 4x° and 5x°. The largest angle is", "36°", "120°", "150°", "180°", "D", "Sum = (5 − 2) × 180° = 540°; 15x = 540 ⇒ x = 36; largest = 5 × 36 = 180°.", "540/15*5"),
    ("Geometry", "Medium", "In a circle, a tangent from an external point T touches the circle at A. If the angle between the tangent and a chord AB is 55°, the angle in the alternate segment is", "35°", "55°", "70°", "110°", "B", "Alternate segment theorem: the angle between a tangent and a chord equals the angle in the alternate segment: 55°.", "55"),
    ("Geometry", "Medium", "Two tangents are drawn from an external point P to a circle with centre O, touching it at A and B. If angle APB = 50°, then angle AOB is", "50°", "100°", "130°", "260°", "C", "OA ⊥ PA and OB ⊥ PB, so in quadrilateral OAPB: angle AOB = 360° − 90° − 90° − 50° = 130°.", "360-90-90-50"),
    ("Geometry", "Medium", "The sides of two similar triangles are in the ratio 2 : 5. If the area of the smaller triangle is 12 cm², the area of the larger is", "30 cm²", "48 cm²", "60 cm²", "75 cm²", "D", "Areas are in the ratio of squares of sides: 4 : 25 ⇒ 12 × 25/4 = 75 cm².", "12*25/4"),
    ("Geometry", "Medium", "A man standing 6 m from a wall casts a shadow that just reaches the foot of the wall. If he is 1.8 m tall and the shadow of a 5 m pole standing beside him is 20 m long, how long is his shadow?", "5.4 m", "6 m", "7.2 m", "9 m", "C", "Similar triangles: shadow/height = 20/5 = 4 ⇒ man's shadow = 1.8 × 4 = 7.2 m.", "1.8*4"),
    ("Mensuration", "Medium", "A cylindrical water tank of radius 1.4 m and height 2 m is to be filled by a pipe delivering 88 litres per minute. The time taken to fill it is (take π = 22/7, 1 m³ = 1,000 litres)", "70 minutes", "120 minutes", "140 minutes", "280 minutes", "C", "Volume = 22/7 × 1.4² × 2 = 12.32 m³ = 12,320 litres; time = 12,320/88 = 140 minutes.", "22/7*1.4**2*2*1000/88"),
    ("Mensuration", "Medium", "A sector of a circle of radius 7 cm and angle 90° is folded to form a cone. The base radius of the cone is", "1.75 cm", "3.5 cm", "7 cm", "14 cm", "A", "Arc length = 90/360 × 2π × 7 = 11 cm (π = 22/7) = circumference of the base = 2πr ⇒ r = 11/(2 × 22/7) = 1.75 cm.", "1.75"),
    ("Mensuration", "Medium", "A solid metal sphere of radius 3 cm is melted and recast into a cylinder of radius 3 cm. The height of the cylinder is", "3 cm", "4 cm", "6 cm", "9 cm", "B", "Volume of sphere = 4/3 π(27) = 36π; πr²h = 36π ⇒ 9h = 36 ⇒ h = 4 cm.", "4"),
    ("Mensuration", "Medium", "The total surface area of a closed cylinder of radius 7 cm and height 10 cm is (take π = 22/7)", "440 cm²", "748 cm²", "1,540 cm²", "308 cm²", "B", "TSA = 2πr(r + h) = 2 × 22/7 × 7 × 17 = 748 cm².", "2*22/7*7*17"),
    ("Mensuration", "Hard", "A rectangular tank 2 m long, 1.5 m wide and 1.2 m high is filled with water to a depth of 0.8 m. When a stone is dropped in, the water level rises to 0.9 m. The volume of the stone is", "0.15 m³", "0.3 m³", "2.4 m³", "2.7 m³", "B", "Rise = 0.1 m; volume displaced = 2 × 1.5 × 0.1 = 0.3 m³.", "2*1.5*0.1"),
    ("Trigonometry", "Medium", "A ship sails 12 km due east from a port and then 5 km due north. Its distance from the port is", "7 km", "13 km", "17 km", "√119 km", "B", "√(12² + 5²) = √169 = 13 km.", "13"),
    ("Trigonometry", "Medium", "Town Q is on a bearing of 060° from town P. The bearing of P from Q is", "120°", "240°", "300°", "060°", "B", "Back bearing = 060° + 180° = 240°.", "240"),
    ("Trigonometry", "Medium", "In triangle PQR, angle P = 30°, angle Q = 45° and QR = 10 cm. The length of PR is (sin 45° = √2/2, sin 30° = ½)", "5√2 cm", "10√2 cm", "10 cm", "20 cm", "B", "Sine rule: PR/sin Q = QR/sin P ⇒ PR = 10 × (√2/2)/(½) = 10√2 cm.", "10*2**0.5"),
    ("Trigonometry", "Medium", "If tan θ = 5/12 and θ is acute, the value of sin θ + cos θ is", "7/13", "17/13", "12/13", "5/13", "B", "Hypotenuse = 13; sin θ = 5/13, cos θ = 12/13; sum = 17/13.", "17/13"),
    ("Trigonometry", "Medium", "The value of sin 150° is", "−½", "½", "√3/2", "−√3/2", "B", "150° is in the second quadrant where sine is positive: sin 150° = sin 30° = ½.", "0.5"),
    ("Trigonometry", "Hard", "The angle of elevation of the top of a tower from a point 50 m from its base is 60°. The height of the tower is", "25 m", "25√3 m", "50√3 m", "100 m", "C", "tan 60° = h/50, so h = 50 tan 60° = 50√3 m (about 86.6 m).", "50*3**0.5"),
    ("Longitude and Latitude", "Medium", "Two points on the equator have longitudes 20°E and 40°E. Taking the radius of the earth as 6,400 km and π = 3.142, the distance between them along the equator is approximately", "1,118 km", "2,235 km", "3,353 km", "4,470 km", "B", "Angle difference = 20°; distance = 20/360 × 2 × 3.142 × 6,400 ≈ 2,234 km.", "20/360*2*3.142*6400"),
    ("Longitude and Latitude", "Medium", "The radius of the parallel of latitude 60°N (earth radius R) is", "R", "R/2", "R√3/2", "2R", "B", "The radius of a parallel of latitude θ is R cos θ; cos 60° = ½, so r = R/2.", None),
    ("Statistics", "Medium", "The mean of five numbers is 12. When a sixth number is added the mean becomes 14. The sixth number is", "14", "20", "24", "26", "C", "Sum of five = 60; sum of six = 84; sixth = 24.", "84-60"),
    ("Statistics", "Medium", "The range of the numbers 12, 7, 15, 9, 21, 4 is", "9", "12", "17", "21", "C", "Range = highest − lowest = 21 − 4 = 17.", "21-4"),
    ("Statistics", "Medium", "In a pie chart showing how a student spends 24 hours, the sector for sleep is 120°. The student sleeps for", "6 hours", "8 hours", "10 hours", "12 hours", "B", "The sector is 120° out of 360°, i.e. one third of the day: ⅓ × 24 = 8 hours.", "120/360*24"),
    ("Statistics", "Medium", "The mean deviation of the numbers 2, 4, 6, 8 is", "1", "2", "3", "4", "B", "Mean = 5; deviations 3, 1, 1, 3 sum to 8; mean deviation = 8/4 = 2.", "8/4"),
    ("Statistics", "Hard", "The standard deviation of the numbers 1, 2, 3, 4, 5 is", "√2", "2", "√10", "10", "A", "Mean = 3; squared deviations 4, 1, 0, 1, 4 sum to 10; variance = 10/5 = 2; SD = √2.", "2**0.5"),
    ("Probability", "Medium", "A letter is chosen at random from the word STATISTICS. The probability that it is a T is", "1/5", "3/10", "2/5", "1/2", "B", "STATISTICS has 10 letters, 3 of them T: 3/10.", "3/10"),
    ("Probability", "Medium", "Two fair dice are thrown. The probability that the product of the scores is 12 is", "1/9", "1/12", "1/18", "5/36", "A", "Pairs with product 12: (2,6), (3,4), (4,3), (6,2) = 4 of 36 = 1/9.", "4/36"),
    ("Probability", "Medium", "A bag contains 6 red and 4 white balls. Two balls are drawn one after the other with replacement. The probability that both are white is", "4/25", "2/15", "6/25", "2/5", "A", "P = 4/10 × 4/10 = 16/100 = 4/25.", "16/100"),
    ("Probability", "Hard", "The probability that Ngozi hits a target is 2/3 and that Kola hits it is 3/4. The probability that at least one of them hits the target is", "1/2", "11/12", "5/12", "1/12", "B", "P(neither) = 1/3 × 1/4 = 1/12; P(at least one) = 1 − 1/12 = 11/12.", "11/12"),
    ("Probability", "Medium", "In how many ways can 5 students be seated in a row if two particular students must sit together?", "24", "48", "60", "120", "B", "Treat the pair as one unit: 4! arrangements × 2 (the pair can swap) = 48.", "48"),
    ("Calculus", "Medium", "Differentiate y = 3x⁴ − 2x² + 5x − 7 with respect to x.", "12x³ − 4x + 5", "12x³ − 2x + 5", "3x³ − 4x + 5", "12x³ − 4x − 7", "A", "Differentiate term by term: 12x³ − 4x + 5 (the constant vanishes).", None),
    ("Calculus", "Medium", "The gradient of the curve y = x² − 4x + 3 at the point where x = 3 is", "0", "2", "3", "6", "B", "dy/dx = 2x − 4; at x = 3: 6 − 4 = 2.", "2"),
    ("Calculus", "Medium", "A stone is thrown upward and its height after t seconds is h = 20t − 5t². Its maximum height is", "10 m", "20 m", "40 m", "80 m", "B", "dh/dt = 20 − 10t = 0 ⇒ t = 2; h = 40 − 20 = 20 m.", "20*2-5*4"),
    ("Calculus", "Medium", "Evaluate ∫ (6x² − 4x + 1) dx.", "2x³ − 2x² + x + c", "12x − 4 + c", "2x³ − 4x² + x + c", "6x³ − 2x² + x + c", "A", "Raise each power by one and divide: 6x³/3 − 4x²/2 + x + c = 2x³ − 2x² + x + c.", None),
    ("Calculus", "Medium", "Evaluate ∫₁² 3x² dx.", "3", "7", "8", "9", "B", "Integrate to get x³, then substitute the limits: 2³ − 1³ = 8 − 1 = 7.", "8-1"),
    ("Calculus", "Hard", "The minimum value of y = x² − 6x + 13 is", "3", "4", "9", "13", "B", "dy/dx = 2x − 6 = 0 ⇒ x = 3; y = 9 − 18 + 13 = 4.", "9-18+13"),
    ("Calculus", "Medium", "The area between the curve y = x² and the x-axis from x = 0 to x = 3 is", "3 square units", "6 square units", "9 square units", "27 square units", "C", "∫₀³ x² dx = [x³/3]₀³ = 27/3 = 9.", "27/3"),
    ("Calculus", "Medium", "The rate of change of the area of a circle with respect to its radius when r = 7 cm is (take π = 22/7)", "22 cm²/cm", "44 cm²/cm", "154 cm²/cm", "308 cm²/cm", "B", "A = πr² ⇒ dA/dr = 2πr = 2 × 22/7 × 7 = 44.", "2*22/7*7"),
    ("Vectors", "Medium", "The position vectors of A and B are 2i + 3j and 5i − j respectively. The vector AB is", "3i − 4j", "−3i + 4j", "7i + 2j", "3i + 4j", "A", "AB = OB − OA = (5 − 2)i + (−1 − 3)j = 3i − 4j.", None),
    ("Vectors", "Medium", "If a = 4i + 3j, the unit vector in the direction of a is", "(4i + 3j)/5", "(4i + 3j)/7", "4i + 3j", "(3i + 4j)/5", "A", "|a| = √(16 + 9) = 5; unit vector = a/|a| = (4i + 3j)/5.", None),
    ("Vectors", "Medium", "The scalar (dot) product of p = 2i − 3j and q = 4i + j is", "5", "11", "−5", "8", "A", "p·q = 2(4) + (−3)(1) = 8 − 3 = 5.", "5"),
]

RETIRE = [
    "What is x-coordinate of (3,5)?", "What is y-coordinate of (3,5)?", "Point (0,5) lies on which axis?",
    "A square has how many equal sides?", "Probability of head on fair coin?", "Probability of impossible event?",
    "Probability of rolling a 6 on fair die?", "A chord through the centre is called:", "Matrix with equal rows and columns is:",
    "A matrix with one row is called:", "The sum of angles in a triangle is:", "Perimeter of square side 5 cm?",
    "Area of rectangle 8 cm by 5 cm?", "Perimeter of rectangle 7 cm by 3 cm?", "Find the next term: 2,4,6,8,...",
    "Find the next term: 1,3,5,7,...", "If A={a,b,c}, how many elements does A contain?",
    "A tangent is perpendicular to the radius at contact. Angle?", "For parallel lines, alternate angles are:",
    "If A is identity matrix, A² equals:", "Find the 5th term of 3,6,9,...", "Find the 8th term of 5,10,15,...",
    "A matrix with 2 rows and 3 columns has order:", "If A∩B=∅, which of the following describes A and B?",
    "If p varies directly as q, which is correct?", "Using the information above, how many students offer neither Mathematics nor Physics?",
    "Area of triangle base 12 cm, height 7 cm?", "Distance between (0,0) and (3,4)?", "One complementary angle is 35°. Other?",
    "Two triangle angles are 50° and 60°. Third?", "Find the common difference of 5,9,13,17.",
]


def build():
    questions, bad = [], []
    passages = [{"key": "T2", "title": TABLE[0], "text": TABLE[1]}]

    def add(topic, diff, q, a, b, c, d, ans, exp, verify, passage=None):
        item = {"subject": "Mathematics", "topic": topic, "difficulty": diff, "q": q, "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp}
        if passage:
            item["passage"] = passage
        if verify:
            expected = eval(verify, {"math": math})
            got = _num(item[ans])
            if got is None or abs(got - expected) > max(0.01 * abs(expected), 0.006):
                bad.append((q[:60], ans, item[ans], expected))
        questions.append(item)

    for row in TABLE_Q:
        add(*row, passage="T2")
    for row in MATHS:
        add(*row)
    if bad:
        for b_ in bad:
            print("MISMATCH:", b_)
        sys.exit("Verification failed — file not written.")
    assert not any("simplified:" in q["q"] for q in questions), "unfinished stem left in the list"
    _balance(questions)
    texts = [x["q"] for x in questions]
    assert len(texts) == len(set(texts)), "duplicate question text"
    assert all(x["answer"] in "ABCD" and all(x[k] for k in "ABCD") for x in questions)
    batch = {
        "batch_id": "batch_009_maths_round2",
        "exam_type": "JAMB",
        "note": "Mathematics round 2: commercial arithmetic, frequency-table statistics, calculus, binary operations, bearings, circle theorems, longitude/latitude. Retires the weakest remaining one-line items.",
        "passages": passages,
        "questions": questions,
        "deactivate": [{"subject": "Mathematics", "like": RETIRE, "reason": "one-line recall items far below JAMB level"}],
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=1)
    from collections import Counter
    print(f"wrote {OUT}: {len(questions)} questions, {len(passages)} passages")
    print("answer letters:", dict(Counter(x['answer'] for x in questions)))
    print("per topic:", dict(Counter(x['topic'] for x in questions)))


if __name__ == "__main__":
    build()
