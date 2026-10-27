"""Batch 229 - NECO Mathematics round 8 (NECO top-up, R46).

Grows NECO Maths from 253 toward ~278 with angles verified absent
from the whole Mathematics pool (1,373 items across JAMB, WAEC and
NECO): depreciation; completing the square; joint variation; sine
rule; cosine rule; rotational symmetry; Pythagoras named; tree
diagram; permutation; combination; fractional index; negative
index; log of 1; area of triangle 1/2 ab sinC; segment; arc length;
volume scale factor; 1000 cm3 = 1 litre; three-figure bearing;
matrix multiplication; difference of two squares; index law
(multiply = add); index law (divide = subtract); factor theorem;
factorising by grouping. Backups if needed: exterior angle of a
triangle (0), travel/speed-time graph (0), vertically opposite
angles (0). Checked and avoided (already banked): recurring decimal
0.4545, equation-of-line family incl. perpendicular-through-point
item, simultaneous families, ladder problems, mean deviation (twice),
perfect square 121, class boundaries 20-29, arc-length-as-option in
circumference item, algebraic fractions, surds, special angles,
bearings family, alternate/co-interior angles, Pythagoras-adjacent
distance-item, hypotenuse.

    python3 scripts/build_neco_batch229.py -> content/batch_229_neco_maths8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Mathematics"

T_NUM = "Number and Numeration"
T_IND = "Indices and Logarithms"
T_ALG = "Algebraic Expressions and Factorisation"
T_EQN = "Equations and Inequalities"
T_VAR = "Variation"
T_GEO = "Geometry: Angles and Polygons"
T_CIR = "Circle Geometry"
T_TRIG = "Trigonometry"
T_MEN = "Mensuration"
T_COORD = "Coordinates and Transformations"
T_MAT = "Algebra Skills"
T_STAT = "Statistics"
T_PROB = "Probability"
T_COM = "Commercial Mathematics"
T_SEQ = "Sequences"

PASSAGES = []
PQ = []

Q = [
    (T_COM, "Medium", "A machine bought for ₦200,000 is worth ₦170,000 after one year, ₦144,500 after two years, and so on, falling by the same percentage each year. This steady yearly fall in value is called",
     "depreciation", "appreciation",
     "compound interest", "simple interest", "A",
     "Each year the machine is worth less than the year before."),
    (T_EQN, "Hard", "To solve x² + 6x + 1 = 0 by completing the square, we rewrite the left side as",
     "(x + 3)² = 8", "(x + 6)² = 8",
     "(x + 3)² = 10", "(x − 3)² = 8", "A",
     "Half of six, squared, moves across the equals sign."),
    (T_VAR, "Hard", "If z varies jointly as x and y, then the relationship between them is written as",
     "z = kxy", "z = kx + y",
     "z = k(x + y)", "z = kx ÷ y", "A",
     "Two variables multiply under the constant's watch."),
    (T_TRIG, "Medium", "In any triangle ABC, the rule which states that a ÷ sin A = b ÷ sin B = c ÷ sin C is known as the",
     "sine rule", "cosine rule",
     "tangent rule", "Pythagorean rule", "A",
     "Each side stands over the sine of its own angle."),
    (T_TRIG, "Hard", "In any triangle ABC, the rule used to find the third side when two sides and the angle between them are known is",
     "the cosine rule, c² = a² + b² − 2ab cos C", "the sine rule, a ÷ sin A = b ÷ sin B",
     "the area rule, ½ab sin C", "the sine rule for angles", "A",
     "The included angle sits between the two known sides."),
    (T_GEO, "Easy", "The number of times a square fits onto itself in one complete turn about its centre is 4. This number is called the order of",
     "rotational symmetry", "reflective symmetry",
     "translation symmetry", "enlargement factor", "A",
     "Turn it four times before it looks new again."),
    (T_GEO, "Medium", "In a right-angled triangle, the square of the hypotenuse equals the sum of the squares of the two shorter sides. This statement is called",
     "Pythagoras' theorem", "the theorem of circles",
     "the intercept theorem", "the factor theorem", "A",
     "The oldest and most famous rule of the right triangle."),
    (T_PROB, "Easy", "A probability diagram in which each outcome of an experiment is shown as a branch, and further outcomes branch out from them, is called a",
     "tree diagram", "bar chart",
     "Venn diagram", "pie chart", "A",
     "Every path through its branches is one possible outcome."),
    (T_STAT, "Medium", "Four different books are to be arranged in a row on a shelf. The number of different arrangements is",
     "24", "16",
     "12", "8", "A",
     "Four choices, then three, then two, then one.", "24"),
    (T_STAT, "Hard", "A committee of 2 students is to be chosen from a group of 5 students. The number of different committees that can be formed is",
     "10", "20",
     "25", "5", "A",
     "Choosing a pair is not arranging a row.", "10"),
    (T_IND, "Medium", "The value of 27 raised to the power one-third is",
     "3", "9",
     "1", "27", "A",
     "Which number, thrice multiplied by itself, makes 27?", "3"),
    (T_IND, "Medium", "The value of 2 raised to the power negative three is",
     "1/8", "−8",
     "8", "−6", "A",
     "A negative power sends the base below the fraction bar.", "0.125"),
    (T_IND, "Easy", "The logarithm of one, to any base whatsoever, is",
     "0", "1",
     "the base itself", "undefined", "A",
     "Every base, raised to nothing, returns one.", "0"),
    (T_TRIG, "Hard", "The area of a triangle in which two sides a and b enclose an angle C is given by the formula",
     "½ab sin C", "½ab cos C",
     "ab sin C", "½(a + b) sin C", "A",
     "Half the product of the sides, times the sine between."),
    (T_CIR, "Easy", "The region enclosed between a chord of a circle and the arc which the chord cuts off is called a",
     "segment", "sector",
     "secant", "sector of a chord", "A",
     "The chord slices the circle like a moon-shaped piece."),
    (T_CIR, "Medium", "The length of an arc that subtends an angle of 90° at the centre of a circle of radius 7 cm, taking π = 22/7, is",
     "11 cm", "22 cm",
     "44 cm", "7 cm", "A",
     "A quarter of the circle's rim.", "11"),
    (T_MEN, "Hard", "If all the lengths of a solid are enlarged by a scale factor of 3, its volume becomes",
     "27 times the original", "9 times the original",
     "3 times the original", "6 times the original", "A",
     "Thrice along, thrice across, thrice upright.", "27"),
    (T_MEN, "Easy", "A tank has a volume of 4,000 cubic centimetres. In litres, this volume is",
     "4 litres", "40 litres",
     "0.4 litres", "400 litres", "A",
     "A thousand little cubes make one litre.", "4"),
    (T_GEO, "Medium", "The bearing of a town measured clockwise from north and written with three figures, as 045°, is called a",
     "three-figure bearing", "reverse bearing",
     "magnetic bearing", "whole-circle dip", "A",
     "Even north itself is written as 000°."),
    (T_MAT, "Hard", "If A = (1 2; 3 4) and B = (5 6; 7 8) are 2×2 matrices, then the entry in the first row and first column of AB is",
     "19", "15",
     "23", "5", "A",
     "Row one of A walks down column one of B.", "19"),
    (T_ALG, "Medium", "The expression x² − 25 is factorised as (x − 5)(x + 5) by using",
     "the difference of two squares", "the factor theorem only",
     "perfect square expansion", "grouping in pairs", "A",
     "Two squares with a minus between them split neatly."),
    (T_GEO, "Medium", "In any triangle, the exterior angle formed by producing one side equals",
     "the sum of the two interior opposite angles", "the right angle of the triangle",
     "the third angle of the triangle alone", "the sum of all three interior angles", "A",
     "The outside angle collects the two far inside angles."),
    (T_IND, "Easy", "When powers with the same base are divided, such as x⁷ ÷ x², the indices are",
     "subtracted, giving x⁵", "added, giving x⁹",
     "multiplied, giving x¹⁴", "swapped, giving x^(7/2)", "A",
     "Cancel two factors from the top of the seven."),
    (T_ALG, "Hard", "If the expression f(x) is exactly divisible by (x − a), leaving no remainder, then f(a) must equal",
     "0", "1",
     "a", "−a", "A",
     "This test of divisibility is the factor theorem.", "0"),
    (T_ALG, "Medium", "The expression ax + bx + ay + by is factorised by grouping the terms in pairs, giving",
     "(a + b)(x + y)", "(a − b)(x − y)",
     "(a + x)(b + y)", "(ab)(xy)", "A",
     "Take out what each pair shares, then what remains."),
]

build_batch(
    S,
    "batch_229_neco_maths8.json",
    "229",
    "NECO Maths round 8 (R46 top-up): depreciation; completing the "
    "square; joint variation; sine rule; cosine rule; rotational "
    "symmetry; Pythagoras named; tree diagram; permutation; "
    "combination; fractional index; negative index; log of 1; area "
    "of triangle half-ab-sinC; segment; arc length 90°/r=7; volume "
    "scale factor 27; 1000 cm3 = 1 litre; three-figure bearing; "
    "matrix multiplication entry; difference of two squares; index "
    "law multiply-add; index law divide-subtract; factor theorem; "
    "factorising by grouping. Scanned against the whole Maths pool "
    "(JAMB, WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
