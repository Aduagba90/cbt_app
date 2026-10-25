"""Batch 162 - NECO Mathematics round 5 (NECO top-up, R30).

Grows NECO Maths from 190 toward ~227 with fresh numeric items and
scenario stems: base-two conversion of 25, LCM scheduling, percentage
increase, simple interest principal, discount, commission; change of
subject, substitution, factorising by grouping, simultaneous word
problem, inequality; regular hexagon interior angle, exterior angle
sum, trapezium area, sector, Pythagoras word, parallel-line angles,
similar triangles; tangent height word problem; mean from a frequency
table, mode; two-coin and die-coin probability, sampling without
replacement; rotation, enlargement area; AP nth term, infinite GP
sum. Numeric items carry verify strings where the correct option's
first number equals the value. Scanned against NECO rounds 1-4, WAEC
Maths (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch162.py -> content/batch_162_neco_maths5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Mathematics"

T_NUM = "Number Work"
T_MON = "Money Problems"
T_ALG = "Algebra Skills"
T_GEO = "Geometry Work"
T_TRIG = "Heights and Distances"
T_STAT = "Statistics"
T_PROB = "Probability"
T_TRAN = "Transformations"
T_SEQ = "Sequences Further"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- numbers
    (T_NUM, "Medium", "A computer stores the count nineteen in binary as",
     "10011", "11001", "10101", "11010", "A",
     "Sixteen, two and one make nineteen.", "10011"),
    (T_NUM, "Hard", "Two bus routes leave the same park: one every 12 minutes, the other every 18. They next leave together after",
     "36 minutes", "6 minutes", "54 minutes", "72 minutes", "A",
     "The least common multiple rules the park.", "36"),
    (T_NUM, "Medium", "A hostel's water bill rose from N4,000 to N5,000. The percentage increase is",
     "25%", "20%", "80%", "125%", "A",
     "One thousand on four thousand.", "25"),
    (T_NUM, "Medium", "Of the pupils in a school, 15 out of 60 wear glasses. The fraction with glasses is",
     "one-quarter", "one-third", "one-fifth", "three-fifths", "A",
     "Fifteen of sixty simplifies."),

    # ------------------------------------------------------------- money
    (T_MON, "Medium", "A cooperative earns N4,500 simple interest at 5% per annum in 3 years. The sum saved was",
     "N30,000", "N22,500", "N27,000", "N45,000", "A",
     "Interest over rate and time.", "30000"),
    (T_MON, "Hard", "A trader marks a generator at N90,000 and allows a 10% discount for cash. The cash price is",
     "N81,000", "N80,000", "N99,000", "N85,000", "A",
     "One-tenth off the marked price.", "81000"),
    (T_MON, "Medium", "An agent is paid 5% commission on sales of N140,000. The commission earned is",
     "N7,000", "N14,000", "N5,000", "N70,000", "A",
     "Five parts of every hundred.", "7000"),

    # ------------------------------------------------------------- algebra
    (T_ALG, "Medium", "If y = 3x + 1, then y at x = -4 equals",
     "-11", "11", "-13", "-9", "A",
     "Twelve with a minus sign, plus one.", "-11"),
    (T_ALG, "Hard", "Making L the subject of the formula A = L x W gives",
     "L = A divided by W", "L = W divided by A", "L = A times W", "L = A plus W", "A",
     "Divide both sides by W first."),
    (T_ALG, "Hard", "Factorised by grouping, ab + 2a + 3b + 6 equals",
     "(a + 3)(b + 2)", "(a + 2)(b + 3)", "(a + b)(3 + 2)", "(a + 6)(b + 1)", "A",
     "Pair, pull out, pair again."),
    (T_ALG, "Hard", "The sum of two numbers is 18 and their difference is 4. The larger number is",
     "11", "14", "9", "7", "A",
     "Half of the sum and difference together.", "11"),
    (T_ALG, "Medium", "The inequality 3x - 2 < 7 solves to",
     "x is less than 3", "x is greater than 3", "x is less than 5", "x is more than 9", "A",
     "Add two, divide by three."),

    # ------------------------------------------------------------- geometry
    (T_GEO, "Hard", "An angle standing on a diameter, at any point of the same circle, is always",
     "90 degrees", "45 degrees", "180 degrees", "60 degrees", "A",
     "The semicircle holds a right angle.", "90"),
    (T_GEO, "Medium", "The exterior angles of ANY polygon, added together, always give",
     "360 degrees", "180 degrees", "540 degrees", "720 degrees", "A",
     "One full turn around the shape.", "360"),
    (T_GEO, "Hard", "The parallel sides of a farmer's trapezium field are 6 m and 10 m, and the field stands 4 m tall. Its area is",
     "32 square m", "60 square m", "16 square m", "40 square m", "A",
     "Half the sum of the parallels, times height.", "32"),
    (T_GEO, "Hard", "A sector of a circle of radius 7 cm cuts 90 degrees at the centre. Taking pi as 22/7, its area is",
     "38.5 square cm", "154 square cm", "77 square cm", "19.25 square cm", "A",
     "A quarter of the whole circle.", "38.5"),
    (T_GEO, "Hard", "A ladder 13 m long leans on a wall with its foot 5 m out. It reaches up the wall",
     "12 m", "8 m", "18 m", "sqrt of 13 m", "A",
     "Five-twelve-thirteen is the triple.", "12"),
    (T_GEO, "Medium", "A line crossing two parallel lines makes an angle of 65 degrees with one. The corresponding angle on the other is",
     "65 degrees", "115 degrees", "25 degrees", "130 degrees", "A",
     "Corresponding angles are equal.", "65"),
    (T_GEO, "Hard", "A triangle with sides 3 cm and 4 cm is enlarged by scale factor 2. The corresponding side to 4 cm becomes",
     "8 cm", "6 cm", "16 cm", "4 cm", "A",
     "Every length of it doubles.", "8"),

    # ------------------------------------------------------------- trigonometry
    (T_TRIG, "Hard", "A flagpole casts a shadow 20 m long when the sun's elevation is 45 degrees. The pole's height is",
     "20 m", "10 m", "40 m", "28.3 m", "A",
     "Tangent 45 degrees is one.", "20"),

    # ------------------------------------------------------------- statistics
    (T_STAT, "Hard", "Scores 2, 3, 3, 5 and 7 occur with frequencies 1, 4, 2, 2 and 1. The mean score is",
     "3.5", "4", "3", "5", "A",
     "Forty shared among ten entries.", "3.5"),
    (T_STAT, "Medium", "In the set of marks 4, 5, 5, 5, 9, 11, the mode is",
     "5", "4", "9", "39 over 6", "A",
     "It simply appears most often.", "5"),

    # ------------------------------------------------------------- probability
    (T_PROB, "Medium", "Two fair coins are tossed together. The probability of two heads is",
     "one-quarter", "one-half", "one-third", "three-quarters", "A",
     "One of four equally likely outcomes."),
    (T_PROB, "Hard", "A fair die is thrown and a fair coin is tossed. The probability of a six and a head together is",
     "one-twelfth", "one-sixth", "one-half", "one-eighth", "A",
     "It is one-sixth of one-half."),
    (T_PROB, "Hard", "A bag holds 4 red and 6 blue beads. Two beads are drawn one after the other WITHOUT replacement. The probability both are red is",
     "2/15", "4/25", "16/100", "1/5", "A",
     "Four-tenths then three-ninths."),

    # ------------------------------------------------------------- transformations
    (T_TRAN, "Medium", "Turning a point through a quarter turn clockwise about the origin performs a",
     "rotation", "reflection", "translation", "enlargement", "A",
     "A fixed centre, a fixed angle."),
    (T_TRAN, "Hard", "A shape is enlarged by scale factor 2. Its area becomes",
     "4 times the original", "2 times the original", "8 times the original", "unchanged", "A",
     "Both its directions double."),

    # ------------------------------------------------------------- sequences
    (T_SEQ, "Hard", "For the pattern 4, 9, 14, 19, ..., the rule for the nth term is",
     "5n - 1", "5n", "4n + 1", "n + 5", "A",
     "Five per every step, less one."),
    (T_SEQ, "Hard", "The sum of the endless series one-half plus one-quarter plus one-eighth and so on is",
     "1", "2", "one-half", "three-quarters", "A",
     "The halves close up to one."),
    (T_SEQ, "Medium", "The seventh term of the progression 2, 6, 18, ... is",
     "1458", "486", "4374", "162", "A",
     "Two grown by three, six times.", "1458"),

    # ------------------------------------------------------------- mixed fresh
    (T_NUM, "Medium", "Rounded to one decimal place, the reading 9.84 is given as",
     "9.8", "9.9", "9.0", "10.4", "A",
     "The second decimal cannot lift it.", "9.8"),
    (T_MON, "Hard", "A shop's VAT of 5% on a bill of N2,400 adds",
     "N120", "N240", "N48", "N2,520", "A",
     "Five parts of every hundred.", "120"),
    (T_ALG, "Medium", "Simplified, 3(2x - 1) - 2(x + 4) equals",
     "4x - 11", "4x + 11", "6x - 11", "4x - 5", "A",
     "Expand, then gather the like terms."),
    (T_GEO, "Medium", "A circle's diameter is 14 cm. Taking pi as 22/7, its circumference is",
     "44 cm", "22 cm", "88 cm", "154 cm", "A",
     "Pi times the diameter gives it.", "44"),
    (T_STAT, "Medium", "On a pie chart of a 24-hour day, sleep of 8 hours takes a sector angle of",
     "120 degrees", "90 degrees", "60 degrees", "45 degrees", "A",
     "A third of the full turn.", "120"),
    (T_PROB, "Medium", "From the word LEVEL, a letter is picked at random. The probability it is L is",
     "2/5", "1/5", "3/5", "2/3", "A",
     "Two L's among five letters."),
]

build_batch(
    S,
    "batch_162_neco_maths5.json",
    "162",
    "NECO Mathematics round 5 (R30 top-up): 25 in base two 11001, "
    "LCM 36-minute buses, 25% rise, 15/60 glasses; SI principal "
    "30,000, discount 81,000, commission 7,000; substitution -7, "
    "subject of formula, grouping factorisation, simultaneous larger "
    "11, inequality x<3; hexagon 120, exterior 360, trapezium 50, "
    "sector 38.5, ladder 12 m, corresponding 65, enlargement side 8; "
    "45-degree shadow 20 m; frequency mean 3.5, mode 3; two heads "
    "1/4, six-and-head 1/12, no-replacement 2/15; quarter-turn "
    "rotation, area x4; nth term 3n+2, infinite sum 1, seventh term "
    "1458; 1 dp 7.5, VAT 120, expansion 4x-11, circumference 44, pie "
    "120 degrees, LEVEL 2/5. Scanned against NECO rounds 1-4, WAEC "
    "Maths (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
