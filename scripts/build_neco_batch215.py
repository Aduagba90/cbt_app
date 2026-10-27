"""Batch 215 - WAEC Economics round 8 (WAEC top-up, R43).

Grows WAEC Economics from 254 toward ~271 with angles not yet in
the bank: producer surplus; quaternary production; the supply
schedule; primary production; wage differentials; the
substitution and income effects; full employment; why the demand
curve slopes downward; economies of scale; fixed cost defined;
absolute poverty; the cost of living; tax evasion vs avoidance;
saving defined; the demand function; excess demand. Scanned
against the whole Economics pool (WAEC, NECO and JAMB stems,
1,387 items).

    python3 scripts/build_neco_batch215.py -> content/batch_215_waec_econ8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Economics"

T_BAS = "Basic Economic Concepts"
T_PROD = "Theory of Production"
T_DIS = "Distribution and Factor Rewards"
T_PUB = "Public Finance"
T_MON = "Money, Banking and Trade"
T_POP = "Population and Labour"

PASSAGES = []
PQ = []

Q = [
    (T_BAS, "Hard", "The difference between what a seller actually receives for a good and the least amount he would have accepted is his",
     "producer surplus", "consumer surplus",
     "marginal revenue", "economic rent of buyers", "A",
     "The seller pockets more than his minimum."),
    (T_PROD, "Hard", "Workers who earn their living by processing and analysing information, such as software engineers and researchers, belong to ___ production.",
     "quaternary", "primary",
     "secondary", "tertiary", "A",
     "Knowledge itself has become an industry."),
    (T_PROD, "Easy", "Farming, fishing, hunting and mining, which draw wealth directly from nature, belong to ___ production.",
     "primary", "secondary",
     "tertiary", "quaternary", "A",
     "The extractive occupations open the chain."),
    (T_BAS, "Medium", "A table showing the various quantities of a good that sellers are willing to offer at different prices at a given time is called a",
     "supply schedule", "demand schedule",
     "price list of buyers", "production chart", "A",
     "The supply curve is its picture."),
    (T_BAS, "Hard", "When the price of beans rises sharply, Mama Nkechi serves more rice and fewer beans. Her response illustrates the",
     "substitution effect", "income effect",
     "demonstration effect", "multiplier effect", "A",
     "The dearer good gives way to its rival."),
    (T_BAS, "Hard", "Because a fall in price makes a consumer's money income go further, he can buy more than before. This part of the response to a price fall is the",
     "income effect", "substitution effect",
     "ratchet effect", "veblen effect", "A",
     "Cheaper prices fatten the real purse."),
    (T_BAS, "Medium", "An economy in which every person who is willing and able to work can find employment is said to enjoy",
     "full employment", "over-employment",
     "labour saturation", "zero population growth", "A",
     "No willing worker is left idle."),
    (T_BAS, "Medium", "One reason the demand curve slopes downward from left to right is that a fall in price",
     "raises the real income of buyers", "raises the cost of production",
     "discourages all consumers", "reduces the good's usefulness", "A",
     "The same naira buys more when prices fall."),
    (T_BAS, "Medium", "The functional relationship showing the quantity of a good demanded at each possible price is the",
     "demand function", "supply function",
     "production function", "consumption curve", "A",
     "It links price to quantity in one formula."),
    (T_BAS, "Medium", "At a price fixed below the equilibrium, the quantity demanded exceeds the quantity supplied. The shortage so created is called",
     "excess demand", "excess supply",
     "market glut", "equilibrium quantity", "A",
     "Empty shelves and long queues follow it."),
    (T_PROD, "Medium", "The fall in a firm's average cost per unit as it grows larger and spreads its overheads is called",
     "economies of scale", "diminishing returns",
     "diseconomies of growth", "marginal costing", "A",
     "Bigness, up to a point, is thrift."),
    (T_PROD, "Medium", "A cost that remains unchanged however many units a firm produces, such as the yearly rent of its factory, is a",
     "fixed cost", "variable cost",
     "marginal cost", "average cost", "A",
     "The landlord is paid whether or not the machines run."),
    (T_DIS, "Medium", "The differences in the wages paid to different workers and occupations, arising from skill, training and risk, are called",
     "wage differentials", "wage discrimination",
     "income inequality gaps", "salary scales of state", "A",
     "Why the surgeon out-earns the cleaner."),
    (T_POP, "Medium", "A situation in which a person or household cannot afford the basic necessities of life such as food, clothing and shelter is",
     "absolute poverty", "relative poverty",
     "income inequality", "subsistence spending", "A",
     "The cupboard is truly bare."),
    (T_BAS, "Medium", "The average amount of money a household needs to buy the usual basket of goods and services is measured by the",
     "cost of living", "standard of living",
     "per capita income", "real wage index only", "A",
     "When it climbs, every budget feels it."),
    (T_PUB, "Medium", "The illegal act of deliberately failing to declare income or pay the tax due on it is",
     "tax evasion", "tax avoidance",
     "tax capitalisation", "tax indexing", "A",
     "The dodger breaks the law outright."),
    (T_MON, "Medium", "That part of income which a person or household does not spend on consumption but keeps aside is",
     "saving", "investment",
     "hoarding of cash", "tax reserve", "A",
     "What the wallet refuses to spend today."),
]

build_batch(
    S,
    "batch_215_waec_econ8.json",
    "215",
    "WAEC Economics round 8 (R43 top-up): producer surplus; "
    "quaternary production; primary production; the supply "
    "schedule; substitution effect; income effect; full "
    "employment; why demand slopes downward; demand function; "
    "excess demand; economies of scale; fixed cost; wage "
    "differentials; absolute poverty; cost of living; tax "
    "evasion; saving defined. Scanned against the whole Economics "
    "pool (WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
