"""Batch 216 - WAEC Mathematics round 8 (WAEC top-up, R43).

Grows WAEC Mathematics from 262 toward ~279 with angles not yet
in the bank: percentage error; the zero index; the discriminant;
the remainder theorem; a vector's magnitude; the order rule for
matrix addition; translation; enlargement; the modal class; the
sample space; mutually exclusive events; independent events; an
expected value; a water-acid mixture; parallel gradients;
collinear points; factorial notation. Scanned against the whole
Mathematics pool (WAEC, NECO and JAMB stems, 1,356 items).

    python3 scripts/build_neco_batch216.py -> content/batch_216_waec_maths8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Mathematics"

T_NUM = "Number and Numeration"
T_ALG = "Algebra"
T_GEO = "Geometry and Vectors"
T_TRA = "Transformations"
T_STA = "Statistics"
T_PRO = "Probability"

PASSAGES = []
PQ = []

Q = [
    (T_NUM, "Medium", "A student measures a line as 6.0 cm when the true length is 5.0 cm. His percentage error is",
     "20%", "16.7%",
     "25%", "10%", "A",
     "The error of 1 cm sits on the true 5 cm.", "20"),
    (T_NUM, "Easy", "Any non-zero number raised to the power zero equals",
     "1", "0",
     "the number itself", "its reciprocal", "A",
     "Any number divided by itself leaves one.", "1"),
    (T_NUM, "Easy", "The shorthand 5 × 4 × 3 × 2 × 1 is written in mathematics as",
     "5!", "5²",
     "5 × 5", "₅C₂", "A",
     "The exclamation counts the falling product."),
    (T_ALG, "Medium", "In the quadratic equation ax² + bx + c = 0, the expression b² − 4ac is known as the",
     "discriminant", "determinant",
     "denominator", "difference of squares", "A",
     "Its sign decides the nature of the roots."),
    (T_ALG, "Hard", "By the remainder theorem, the remainder when x − a divides the polynomial f(x) is",
     "f(a)", "f(0)",
     "f(−a)", "a − f(0)", "A",
     "Put the root in and read off the remainder."),
    (T_GEO, "Easy", "The distance of the point (3, 4) from the origin is",
     "5", "7",
     "12", "25", "A",
     "Pythagoras measures the arrow.", "5"),
    (T_GEO, "Medium", "Two straight lines are parallel if their gradients are",
     "equal", "negative reciprocals",
     "both zero", "opposite in sign", "A",
     "Same slope, same direction forever."),
    (T_GEO, "Hard", "Points that all lie on one and the same straight line are said to be",
     "collinear", "coplanar only",
     "congruent", "corresponding", "A",
     "One ruler can join them all."),
    (T_ALG, "Medium", "Two matrices can be added together only when they are of the same",
     "order", "value",
     "determinant", "row count alone", "A",
     "Rows must meet rows, columns columns."),
    (T_TRA, "Medium", "The transformation that slides every point of a figure through the same distance in the same direction is a",
     "translation", "rotation",
     "reflection", "enlargement", "A",
     "The whole shape drifts without turning."),
    (T_TRA, "Medium", "The transformation that multiplies all distances from a fixed centre by the same scale factor is an",
     "enlargement", "translation",
     "rotation", "shear", "A",
     "The picture grows or shrinks in proportion."),
    (T_STA, "Easy", "In a frequency table, the class with the greatest number of observations is called the",
     "modal class", "median class",
     "mean class", "cumulative class", "A",
     "It is where the data crowds thickest."),
    (T_PRO, "Easy", "The set of all possible outcomes of an experiment is called the",
     "sample space", "event space",
     "frequency set", "possibility line", "A",
     "Every result the experiment can ever give."),
    (T_PRO, "Medium", "Two events that cannot happen at the same time, such as throwing a 2 and a 5 with one die, are said to be",
     "mutually exclusive", "independent",
     "complementary", "exhaustive pairs", "A",
     "One shuts the door against the other."),
    (T_PRO, "Medium", "If the outcome of one event has no effect on the probability of another, the two events are",
     "independent", "mutually exclusive",
     "dependent", "certain", "A",
     "Neither event tips the other's scale."),
    (T_PRO, "Medium", "A raffle ticket wins ₦500 with probability 0.1. The expected winning on one ticket is",
     "₦50", "₦500",
     "₦5", "₦45", "A",
     "Multiply the prize by its chance.", "50"),
    (T_NUM, "Hard", "How many litres of pure water must be added to 20 litres of a 30% acid solution to reduce it to a 15% solution?",
     "20 litres", "10 litres",
     "30 litres", "40 litres", "A",
     "The acid stays fixed; the water doubles.", "20"),
]

build_batch(
    S,
    "batch_216_waec_maths8.json",
    "216",
    "WAEC Mathematics round 8 (R43 top-up): percentage error; zero "
    "index; factorial notation; discriminant; remainder theorem; "
    "vector magnitude; parallel gradients; collinear points; "
    "order rule for matrix addition; translation; enlargement; "
    "modal class; sample space; mutually exclusive; independent "
    "events; expected value; acid-dilution mixture. Scanned "
    "against the whole Mathematics pool (WAEC, NECO and JAMB "
    "stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
