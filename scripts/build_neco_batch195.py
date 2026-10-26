"""Batch 195 - NECO Mathematics round 7 (NECO top-up, R38).

Grows NECO Mathematics from 226 toward ~252 with angles not yet
in the bank: place value; perfect square; the only even prime;
the next prime after 7; the HCF defined; the divisibility test
for 3; the cube of 5; the square root of 169; the law of indices
for multiplication; BODMAS order; proper fractions; the
reciprocal; reflex angles; supplementary angles; the angle sum of
a triangle; the hypotenuse; pentagon diagonals; rectangle lines
of symmetry; cuboid faces; the circumference; the sector defined;
mode, range and mean defined; impossible and certain events;
simple interest defined. Scanned against the whole Mathematics
pool (WAEC, NECO and JAMB stems, 1,329 items).

    python3 scripts/build_neco_batch195.py -> content/batch_195_neco_maths7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Mathematics"

T_NUM = "Number and Numeration"
T_ALG = "Algebraic Processes"
T_GEO = "Geometry"
T_MEN = "Mensuration"
T_STA = "Statistics"
T_PRO = "Probability"
T_COM = "Everyday Arithmetic"

PASSAGES = []
PQ = []

Q = [
    (T_NUM, "Easy", "In the number 46,329, the digit 3 stands for",
     "300", "30",
     "3", "3,000", "A",
     "The 3 sits in the hundreds column.", "300"),
    (T_NUM, "Easy", "Which of the following numbers is a perfect square?",
     "121", "98",
     "75", "132", "A",
     "Eleven times eleven gives 121.", "121"),
    (T_NUM, "Easy", "The only even number that is also a prime number is",
     "2", "4",
     "6", "9", "A",
     "Two has no factor besides one and itself.", "2"),
    (T_NUM, "Medium", "The next prime number after 7 is",
     "11", "9",
     "10", "13", "A",
     "Nine and ten divide by other numbers.", "11"),
    (T_NUM, "Medium", "The highest common factor of two numbers is the largest number that",
     "divides both of them exactly", "both of them divide exactly",
     "they both multiply to give", "is a multiple of both", "A",
     "The greatest common divisor hides in each."),
    (T_NUM, "Medium", "A whole number is divisible by 3 whenever",
     "the sum of its digits is a multiple of 3", "it ends with the digit 3 or 6",
     "it is always an odd number", "all of its digits are equal", "A",
     "Add the digits and test the total."),
    (T_NUM, "Easy", "The cube of 5 is",
     "125", "15",
     "25", "5", "A",
     "Five taken three times as a factor.", "125"),
    (T_NUM, "Easy", "Which number, when multiplied by itself, gives 169?",
     "13", "14",
     "17", "11", "A",
     "Thirteen squared gives 169.", "13"),
    (T_ALG, "Medium", "When two powers with the same base are multiplied together, their indices are",
     "added", "subtracted",
     "multiplied", "divided", "A",
     "Two squared times two cubed is two to the five."),
    (T_NUM, "Easy", "In evaluating 5 + 2 × 8 by the correct order of operations, which step comes first?",
     "multiplication", "addition",
     "subtraction", "division", "A",
     "BODMAS puts multiplication before addition."),
    (T_NUM, "Easy", "A fraction whose numerator is smaller than its denominator is called",
     "a proper fraction", "an improper fraction",
     "a mixed number", "a decimal fraction", "A",
     "Three-quarters is proper; four-thirds is not."),
    (T_NUM, "Easy", "The reciprocal of 4/5 is",
     "5/4", "4/5",
     "20/5", "1/5", "A",
     "Turn the fraction upside down."),
    (T_GEO, "Medium", "An angle that is greater than 180° but less than 360° is called",
     "a reflex angle", "an obtuse angle",
     "a right angle", "a straight angle", "A",
     "It bends back past the straight line."),
    (T_GEO, "Easy", "Two angles whose measures add up to 180° are said to be",
     "supplementary", "complementary",
     "vertical", "alternate", "A",
     "Angles on a straight line pair this way."),
    (T_GEO, "Easy", "In every triangle, the angles together make a total of",
     "180°", "90°",
     "270°", "360°", "A",
     "Whatever the triangle's shape.", "180"),
    (T_GEO, "Medium", "The longest side of a right-angled triangle, opposite the right angle, is called the",
     "hypotenuse", "perpendicular",
     "base", "adjacent", "A",
     "Pythagoras built his rule upon it."),
    (T_GEO, "Hard", "The number of diagonals that can be drawn in a pentagon is",
     "5", "4",
     "6", "10", "A",
     "Each of the five corners skips to two others.", "5"),
    (T_GEO, "Easy", "The number of lines of symmetry of a rectangle is",
     "2", "1",
     "4", "0", "A",
     "One through each pair of matching sides.", "2"),
    (T_MEN, "Easy", "A cuboid has how many faces?",
     "6", "4",
     "8", "12", "A",
     "Count top, bottom and the four sides.", "6"),
    (T_MEN, "Easy", "The distance round a circle is called its",
     "circumference", "diameter",
     "radius", "arc length", "A",
     "The rim of the wheel measured all round."),
    (T_MEN, "Medium", "The part of a circle enclosed by two radii and an arc is a",
     "sector", "segment",
     "chord", "quadrant only", "A",
     "Cut a pie slice and you have one."),
    (T_STA, "Easy", "The observation that occurs most frequently in a set of data is the",
     "mode", "mean",
     "median", "range", "A",
     "It is the value seen most often."),
    (T_STA, "Easy", "The range of a set of scores is the difference between",
     "the highest and the lowest", "the mean and the mode",
     "the first and the last entered", "two quartiles", "A",
     "Top score minus bottom score."),
    (T_STA, "Easy", "The mean of a set of numbers is found by dividing their sum by",
     "how many numbers there are", "the largest number",
     "the smallest number", "the median", "A",
     "Share the total fairly among them all."),
    (T_PRO, "Easy", "Every probability, correctly stated, lies between",
     "0 and 1", "1 and 2",
     "-1 and 1", "0 and 10", "A",
     "No chance falls outside nought and one."),
    (T_PRO, "Easy", "The probability of an event that is certain to occur is",
     "1", "0",
     "0.5", "2", "A",
     "The whole chance, and nothing less.", "1"),
    (T_COM, "Medium", "Interest calculated only on the original principal throughout the life of a loan is called",
     "simple interest", "compound interest",
     "discount", "commission", "A",
     "The principal never grows on itself."),
]

build_batch(
    S,
    "batch_195_neco_maths7.json",
    "195",
    "NECO Mathematics round 7 (R38 top-up): place value of 3 in "
    "46,329; perfect square 121; the only even prime 2; next prime "
    "after 7; HCF defined; divisibility test for 3; cube of 5; "
    "square root of 169; indices added on multiplication; BODMAS "
    "order; proper fraction; reciprocal of 4/5; reflex angle; "
    "supplementary angles; triangle angle sum 180°; hypotenuse; "
    "pentagon's five diagonals; rectangle's two lines of symmetry; "
    "cuboid's six faces; circumference; sector defined; mode, "
    "range and mean defined; probability 0 and 1; simple interest "
    "defined. Scanned against the whole Mathematics pool (WAEC, "
    "NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
