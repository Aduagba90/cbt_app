"""Batch 209 - WAEC Biology round 8 (WAEC top-up, R41).

Grows WAEC Biology from 252 toward ~277 with angles not yet in
the bank: emulsification by bile; the lacteal; pancreatic juice;
enzymes as proteins; denaturing; homeostasis; vasodilation for
cooling; double circulation; phagocytes; oestrogen;
progesterone; testosterone; fertilisation in the fallopian tube;
propagation by cuttings; double fertilisation; the gene defined;
mimicry; mutualism defined; the ecosystem defined; the pyramid of
numbers; predation; the antiseptic difference; metamorphosis; the
insect thorax; the housefly as a disease vector. Scanned against
the whole Biology pool (WAEC, NECO and JAMB stems, 1,342 items).

    python3 scripts/build_neco_batch209.py -> content/batch_209_waec_bio8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Biology"

T_DIG = "Digestion and Nutrition"
T_BLD = "Blood and Circulation"
T_COO = "Coordination and Homeostasis"
T_REP = "Reproduction and Growth"
T_GEN = "Genetics and Evolution"
T_ECO = "Ecology"
T_CLA = "Classification of Organisms"

PASSAGES = []
PQ = []

Q = [
    (T_DIG, "Medium", "Bile from the liver assists the digestion of fats mainly by",
     "breaking fat globules into droplets", "chemically splitting the fats",
     "transporting fats to the cells", "storing fats as glycogen", "A",
     "Finer droplets give the lipase more surface to work on."),
    (T_DIG, "Hard", "The tiny lymph vessel found inside each villus of the small intestine, which absorbs digested fats, is the",
     "lacteal", "capillary",
     "venule", "arteriole", "A",
     "Fatty food rides the lymph before it meets the blood."),
    (T_DIG, "Medium", "The gland that pours its juice, rich in amylase, trypsin and lipase, into the duodenum is the",
     "pancreas", "liver",
     "gastric gland", "salivary gland", "A",
     "Its juice completes the work the others began."),
    (T_DIG, "Easy", "Enzymes, whatever their work in the body, belong chemically to the class of substances called",
     "proteins", "fats",
     "carbohydrates", "vitamins", "A",
     "Every enzyme is first of all a protein."),
    (T_DIG, "Hard", "An enzyme that has been boiled loses its working power for good because its protein has been",
     "denatured", "dehydrated",
     "ionised", "reduced", "A",
     "Heat wrecks the very shape that does the work."),
    (T_COO, "Medium", "The maintenance of a steady internal environment in the body, despite changes outside, is called",
     "homeostasis", "haemostasis",
     "osmosis", "hibernation", "A",
     "The body keeps its own conditions constant."),
    (T_COO, "Easy", "On a hot afternoon the skin sheds excess heat because its small blood vessels",
     "dilate to lose heat", "constrict to save heat",
     "shut down entirely", "absorb the sunlight", "A",
     "More blood at the surface means more warmth escaping."),
    (T_BLD, "Medium", "In humans, blood passes through the heart twice in one complete circuit of the body. This pattern is called",
     "double circulation", "single circulation",
     "pulmonary shunting", "systemic looping", "A",
     "Once for the lungs, once for the body."),
    (T_ECO, "Medium", "Besides pulling water up the stem, transpiration is useful to a plant because it",
     "cools the leaves", "makes its food",
     "breathes in air", "stores up water", "A",
     "The evaporating water carries heat away from the leaf."),
    (T_REP, "Medium", "The hormone secreted by the ovary which repairs and thickens the lining of the womb each month is",
     "oestrogen", "testosterone",
     "insulin", "thyroxine", "A",
     "It prepares the nursery before the egg arrives."),
    (T_REP, "Medium", "The hormone whose chief work is to maintain pregnancy and keep the womb quiet after fertilisation is",
     "progesterone", "oestrogen",
     "prolactin", "oxytocin", "A",
     "It holds the cradle steady till term."),
    (T_REP, "Easy", "The male hormone, made in the testes, that brings about the deep voice and beard of a man is",
     "testosterone", "oestrogen",
     "adrenaline", "progesterone", "A",
     "Masculinity rides on this single hormone."),
    (T_REP, "Medium", "The tube along which the egg travels from the ovary towards the womb is the",
     "fallopian tube", "ureter of the kidney",
     "birth canal itself", "ovarian ligament", "A",
     "It is there that the sperm usually meets the egg."),
    (T_REP, "Medium", "A new orange tree exactly like its parent can be raised quickly by planting a cut leafy branch. This method is",
     "propagation by cuttings", "germination of seeds",
     "grafting of scions", "spore formation", "A",
     "The branch roots and repeats its parent wholly."),
    (T_REP, "Hard", "In flowering plants, the fusion of one male nucleus with the egg and of a second with the polar nuclei is called",
     "double fertilisation", "self-pollination",
     "cross-fertilisation", "triple fusion", "A",
     "Two unions, one moment, a seed is begun."),
    (T_GEN, "Easy", "The unit of heredity that sits at a fixed point on a chromosome and controls one character is the",
     "gene", "allele",
     "cell", "gamete", "A",
     "Thousands of them line every chromosome."),
    (T_GEN, "Hard", "A harmless hoverfly that wears the yellow and black stripes of a stinging wasp gains protection through",
     "mimicry", "camouflage",
     "warning coloration", "hibernation", "A",
     "It copies a dangerous model and fools its enemies."),
    (T_ECO, "Medium", "The close association between two organisms of different kinds in which both partners benefit is called",
     "mutualism", "commensalism",
     "parasitism", "saprophytism", "A",
     "Both parties profit from the partnership."),
    (T_ECO, "Medium", "A community of living organisms together with its physical surroundings, working as one natural unit, is an",
     "ecosystem", "biome",
     "habitat", "biosphere", "A",
     "Pond, forest and grassland are each one."),
    (T_ECO, "Medium", "The diagram that shows the ever-decreasing numbers of organisms from green plants up to the top carnivores is the",
     "pyramid of numbers", "food web",
     "cycle of matter", "energy chart", "A",
     "Fewer mouths sit at every higher step."),
    (T_ECO, "Easy", "The relationship in which one animal hunts, kills and feeds on another animal is called",
     "predation", "competition",
     "parasitism", "symbiosis", "A",
     "The hunter dines; the hunted dies."),
    (T_ECO, "Medium", "The large-scale felling of trees without planting new ones is called",
     "deforestation", "afforestation",
     "reforestation", "taungya farming", "A",
     "The bare hills weep away their soil."),
    (T_CLA, "Medium", "The series of marked changes in body form through which a young insect passes on its way to the adult stage is called",
     "metamorphosis", "moulting",
     "regeneration", "budding", "A",
     "Egg, larva, pupa, adult, in the butterfly's story."),
    (T_CLA, "Easy", "The middle region of an insect's body, which carries the legs and the wings, is the",
     "thorax", "abdomen",
     "head", "cephalothorax", "A",
     "Six legs and four wings all hang from it."),
    (T_CLA, "Easy", "The common insect that spreads dysentery and cholera germs by vomiting and treading on exposed food is the",
     "housefly", "mosquito",
     "tsetse fly", "blackfly", "A",
     "It feasts on filth and then on the family's food."),
]

build_batch(
    S,
    "batch_209_waec_bio8.json",
    "209",
    "WAEC Biology round 8 (R41 top-up): bile's emulsification; the "
    "lacteal; pancreatic juice; enzymes as proteins; denaturing; "
    "homeostasis; vasodilation; double circulation; phagocytes; "
    "oestrogen; progesterone; testosterone; fertilisation in the "
    "fallopian tube; propagation by cuttings; double "
    "fertilisation; the gene defined; mimicry; mutualism defined; "
    "the ecosystem defined; the pyramid of numbers; predation; "
    "deforestation; metamorphosis; the insect thorax; the "
    "housefly as vector. Scanned against the whole Biology pool "
    "(WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
