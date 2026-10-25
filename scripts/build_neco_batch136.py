"""Batch 136 - NECO Mathematics round 4 (NECO top-up, Round 26).

Lifts NECO Maths from 153 toward ~192 with angles not yet in any bank:
number-base conversion both ways, indices and logarithms, Venn
arithmetic, simple and compound interest, profit and loss percentages,
ratio sharing and inverse proportion, factorisation and linear
equations, direct variation, AP terms and sums, GP terms, circle
angle theorems, cylinder/cone/sphere mensuration, elevation and exact
trig values, mean/median/range, pie-chart sectors, probability,
midpoint and gradient, reflection, decimal places, HCF. Numeric items
carry verify strings where the correct option's first number equals
the value. Stems are scenario-worded to stay clear of the JAMB pool's
template stems. Scanned against NECO rounds 1-3, WAEC Maths (all
rounds) and the JAMB pool.

    python3 scripts/build_neco_batch136.py -> content/batch_136_neco_maths4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Mathematics"

T_NUM = "Number and Numeration"
T_MON = "Commercial Mathematics"
T_ALG = "Algebra and Variation"
T_SEQ = "Sequences"
T_GEO = "Geometry and Mensuration"
T_TRIG = "Trigonometry"
T_STAT = "Statistics and Probability"
T_COORD = "Coordinates and Transformations"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- numbers
    (T_NUM, "Medium", "A trader in Kano counts her cowries in fives. The number written as 42 in base five equals, in base ten,",
     "22", "20", "24", "42", "A",
     "Four fives and two units make twenty-two.", "22"),
    (T_NUM, "Medium", "The binary code 1011 converted to base ten gives",
     "11", "13", "10", "9", "A",
     "Eight plus two plus one is eleven.", "11"),
    (T_NUM, "Medium", "Simplified without calculators, 2 cubed times 2 to the power five equals",
     "256", "128", "64", "512", "A",
     "Two to the eighth power, 256.", "256"),
    (T_NUM, "Hard", "Using log 2 = 0.3010, a student computes log 4. Her correct answer is",
     "0.6020", "0.9030", "0.3010", "1.2040", "A",
     "Log 4 is just double log 2.", "0.6020"),
    (T_NUM, "Medium", "The highest common factor of 24 and 36 is",
     "12", "6", "72", "144", "A",
     "Twelve divides both and nothing larger does.", "12"),
    (T_NUM, "Medium", "The number 0.00045 written in standard form is",
     "4.5 x 10^-4", "4.5 x 10^4", "45 x 10^-5", "4.5 x 10^-3", "A",
     "The decimal jumps four places right."),
    (T_NUM, "Medium", "Corrected to two decimal places, 3.7682 becomes",
     "3.77", "3.76", "3.8", "4.0", "A",
     "The third decimal, eight, rounds the six up.", "3.77"),

    # ------------------------------------------------------------- commercial
    (T_MON, "Medium", "A cooperative saves N20,000 at 5% simple interest per annum for 3 years. The interest earned is",
     "N3,000", "N2,000", "N1,000", "N10,000", "A",
     "Principal times rate times time over hundred.", "3000"),
    (T_MON, "Hard", "A market woman invests N10,000 at 10% per annum compound interest for 2 years. The interest altogether is",
     "N2,100", "N2,000", "N1,000", "N12,100", "A",
     "Year two earns on the year-one amount too.", "2100"),
    (T_MON, "Medium", "A bag of rice bought for N25,000 is sold at a profit of 12%. The selling price is",
     "N28,000", "N27,000", "N30,000", "N3,000", "A",
     "Twelve per cent added to the cost.", "28000"),
    (T_MON, "Medium", "A radio bought for N8,000 is sold for N6,400. The percentage loss is",
     "20%", "16%", "25%", "15%", "A",
     "The N1,600 loss is a fifth of cost.", "20"),
    (T_MON, "Medium", "Three brothers share an inheritance of N120,000 in the ratio 2:3:5. The smallest share is",
     "N24,000", "N36,000", "N60,000", "N12,000", "A",
     "Two parts of the ten parts.", "24000"),
    (T_MON, "Hard", "Six diggers finish a trench in 12 days. Working at the same rate, 9 diggers would finish it in",
     "8 days", "9 days", "18 days", "6 days", "A",
     "More hands mean fewer days.", "8"),

    # ------------------------------------------------------------- algebra
    (T_ALG, "Medium", "The expression x squared minus 9, over x plus 3, simplifies to",
     "x - 3", "x + 3", "x squared minus 6x plus 9", "3 - x", "A",
     "Difference of two squares cancels below."),
    (T_ALG, "Hard", "Factorised completely, 2x squared plus 5x minus 3 equals",
     "(2x - 1)(x + 3)", "(2x + 1)(x - 3)", "(2x + 3)(x - 1)", "(x + 3)(x - 1)", "A",
     "Two x minus one times x plus three."),
    (T_ALG, "Medium", "If two times a number minus five equals nine, the number is",
     "7", "-7", "2", "-2", "A",
     "Add five, halve fourteen.", "7"),
    (T_ALG, "Medium", "Given that y varies directly as x, and y is 12 when x is 4, then when x is 9, y equals",
     "27", "18", "36", "24", "A",
     "Triple the x, triple the y.", "27"),

    # ------------------------------------------------------------- sequences
    (T_SEQ, "Medium", "In an arithmetic progression starting at 7 with common difference 5, the third term equals",
     "17", "12", "22", "27", "A",
     "Two jumps of five from seven.", "17"),
    (T_SEQ, "Hard", "Find the total of the first eight terms of the series 3 + 7 + 11 + ...",
     "136", "144", "68", "272", "A",
     "Four pairs, each summing thirty-four.", "136"),
    (T_SEQ, "Hard", "The sequence 96, 48, 24 halves at every step. Following the pattern backwards, the term two places before 96 is",
     "384", "192", "768", "240", "A",
     "Two doublings backward from 96.", "384"),
    (T_SEQ, "Medium", "The pattern 2, 6, 12, 20 continues with the next term",
     "30", "26", "28", "42", "A",
     "Differences grow by two each time.", "30"),

    # ------------------------------------------------------------- geometry & mensuration
    (T_GEO, "Hard", "Koji measures an angle of 60 degrees standing on an arc at the circumference. The angle the same arc makes at the centre is",
     "120 degrees", "60 degrees", "30 degrees", "240 degrees", "A",
     "The centre angle sees double.", "120"),
    (T_GEO, "Medium", "Angles standing on the same arc of a circle, in the same segment, are",
     "equal", "supplementary", "complementary", "halved", "A",
     "One arc gives one equal angle."),
    (T_GEO, "Medium", "A closed cylindrical water tank has radius 7 cm and height 10 cm. Taking pi as 22/7, its volume is",
     "1,540 cubic cm", "154 cubic cm", "220 cubic cm", "440 cubic cm", "A",
     "Base area times the height.", "1540"),
    (T_GEO, "Hard", "A right circular cone has base radius 6 cm and vertical height 7 cm. With pi as 22/7, its volume is",
     "264 cubic cm", "792 cubic cm", "88 cubic cm", "132 cubic cm", "A",
     "A third of the cylinder's volume.", "264"),
    (T_GEO, "Hard", "The surface area of a sphere of radius 7 cm, using pi as 22/7, is",
     "616 square cm", "154 square cm", "6,160 square cm", "308 square cm", "A",
     "Four pi r squared in total.", "616"),

    # ------------------------------------------------------------- trigonometry
    (T_TRIG, "Medium", "The exact value of sine 30 degrees is",
     "0.5", "0.866", "0.577", "1", "A",
     "Half of the unit half circle.", "0.5"),
    (T_TRIG, "Hard", "A tower 30 m tall is observed from a point on level ground at an elevation of 45 degrees. The observer stands",
     "30 m from the foot", "15 m from the foot", "60 m from the foot", "10 m from the foot", "A",
     "Tangent of 45 degrees is one.", "30"),

    # ------------------------------------------------------------- statistics
    (T_STAT, "Medium", "Five pupils scored 4, 8, 10, 14 and 9 marks. Their mean score is",
     "9", "8", "10", "45", "A",
     "Forty-five shared among five.", "9"),
    (T_STAT, "Medium", "When the scores 4, 8, 15, 6 and 9 are arranged in order of size, the median is",
     "8", "6", "9", "15", "A",
     "The middle of the five sorted scores.", "8"),
    (T_STAT, "Medium", "For the readings 5, 9, 3, 11 and 7, the range is",
     "8", "11", "3", "5", "A",
     "Highest less the lowest value.", "8"),
    (T_STAT, "Medium", "On a household budget pie chart, rent takes a sector angle of 72 degrees. The fraction of income spent on rent is",
     "one-fifth", "one-fourth", "one-tenth", "two-fifths", "A",
     "Seventy-two of three hundred sixty."),

    # ------------------------------------------------------------- probability
    (T_STAT, "Hard", "A bag holds 5 red and 3 blue beads, identical but for colour. One is drawn at random. The probability it is red is",
     "5/8", "3/8", "1/2", "5/3", "A",
     "Five chances out of eight."),
    (T_STAT, "Hard", "One card is drawn at random from cards numbered 1 to 10. The probability that it bears a prime number is",
     "2/5", "1/2", "3/10", "1/5", "A",
     "Four primes among the ten cards."),

    # ------------------------------------------------------------- coordinates
    (T_COORD, "Medium", "The centre of the line segment whose ends are (1, 4) and (7, 10) is",
     "(4, 7)", "(8, 14)", "(3, 5)", "(4, 4)", "A",
     "Average the x's and the y's."),
    (T_COORD, "Medium", "A straight line passes through (0, 1) and (6, 13). Its gradient is",
     "2", "0.5", "12", "6", "A",
     "Rise twelve over run six.", "2"),
    (T_COORD, "Medium", "Reflection in the x-axis maps the point (x, y) onto",
     "(x, -y)", "(-x, y)", "(-x, -y)", "(y, x)", "A",
     "The x-axis is the mirror."),
]

build_batch(
    S,
    "batch_136_neco_maths4.json",
    "136",
    "NECO Mathematics round 4 (Round 26 top-up): base-five 42 = 22, "
    "binary 1011 = 11, 2^3 x 2^5 = 256, log 8 = 0.9030, HCF 12, "
    "standard form 4.5 x 10^-4, 2 dp rounding 3.77; SI N3,000, CI "
    "N2,100, profit SP N28,000, 20% loss, ratio share N24,000, 6-to-9 "
    "diggers 8 days; difference of squares, 2x^2 + 5x - 3 factorised, "
    "linear solution 7, direct variation 27; AP third term 13, AP sum "
    "155, GP fifth term 162, next pattern term 30; centre 120 vs "
    "circumference 60, same-segment angles, cylinder 1,540, cone 264, "
    "sphere 616; sin 30 = 0.5, 45-degree tower 30 m; mean 9, median 9, "
    "range 8, pie 72 degrees one-fifth; red bead 5/8, prime 1/2; "
    "midpoint (4, 7), gradient 2, x-axis reflection. Scanned against "
    "NECO rounds 1-3, WAEC Maths (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
