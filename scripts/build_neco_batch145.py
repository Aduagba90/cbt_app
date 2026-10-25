"""Batch 145 - WAEC Economics round 5 (WAEC top-up, R27).

Grows WAEC Economics from 183 toward ~219 with angles not yet in the
bank: total vs marginal utility and its diminishing law; price,
cross and income elasticity; fixed and variable costs, diminishing
returns and returns to scale; market failure (externalities, public
goods, merit goods); wage determination and labour mobility; money's
functions, CPI and deflation; unemployment types; CBN as lender of
last resort and banker to government, credit creation; national
income measurement methods and pitfalls, real vs nominal GDP;
progressive and regressive taxes, budget deficit and public debt;
absolute advantage, terms of trade, financing a BOP deficit; poverty
and human capital; optimum population. Scanned against WAEC rounds
1-4, NECO Economics (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch145.py -> content/batch_145_waec_econ5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Economics"

T_UT = "Utility and Consumer Choice"
T_EL = "Elasticity Family"
T_PC = "Production and Costs"
T_MF = "Market Failure"
T_LAB = "Labour and Wages"
T_MON = "Money, Prices and Jobs"
T_BK = "Banking and the Central Bank"
T_NI = "Measuring National Income"
T_PF = "Tax Structure and the Budget"
T_TR = "Trade and Payments"
T_DEV = "Development and Population"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- utility
    (T_UT, "Hard", "The extra satisfaction from drinking one more bottle of water is its",
     "marginal utility", "total utility", "average utility", "fixed utility", "A",
     "Marginal means the last bottle's share."),
    (T_UT, "Hard", "A thirsty traveller values his first cup far above his fifth. This illustrates the law of",
     "diminishing marginal utility", "increasing returns", "comparative cost", "equi-marginal returns", "A",
     "Each extra cup quenches less."),
    (T_UT, "Medium", "Consumer equilibrium is reached when marginal utility per naira is equal across all goods, making the consumer",
     "unable to gain by reshuffling", "spend everything on one good", "save nothing at all", "borrow heavily", "A",
     "No swap would improve his lot."),

    # ------------------------------------------------------------- elasticity
    (T_EL, "Medium", "If the price of millet rises and the quantity of maize demanded rises, the two goods are",
     "substitutes", "complements", "inferior", "unrelated", "A",
     "Cross elasticity here is positive."),
    (T_EL, "Hard", "When incomes rise and demand for garri falls, garri is",
     "an inferior good", "a normal good", "a luxury", "a public good", "A",
     "Better pay demotes it to the shelf."),
    (T_EL, "Hard", "Supply of perishable tomatoes in the short market day is",
     "highly inelastic", "highly elastic", "perfectly elastic", "unitary", "A",
     "They must be sold today regardless."),

    # ------------------------------------------------------------- production & costs
    (T_PC, "Medium", "Rent on a shop continues whether or not production happens. It is a",
     "fixed cost", "variable cost", "marginal cost", "sunk profit", "A",
     "The landlord collects all the same."),
    (T_PC, "Medium", "As more labourers work a fixed plot, each extra worker eventually adds less than the last. This is the law of",
     "diminishing returns", "increasing supply", "comparative advantage", "economies of scale", "A",
     "Too many hands crowd one hoe."),
    (T_PC, "Hard", "When a brewery doubles ALL its inputs and output more than doubles, it enjoys",
     "increasing returns to scale", "diminishing returns", "constant returns", "negative returns", "A",
     "Size itself becomes a machine."),
    (T_PC, "Hard", "Average total cost is found by dividing total cost by",
     "units of output", "number of workers", "hours worked", "price charged", "A",
     "Spread the whole bill over output."),

    # ------------------------------------------------------------- market failure
    (T_MF, "Hard", "A factory's smoke harming neighbours' health is a case of",
     "negative externality", "positive externality", "public good", "merit good", "A",
     "The price ignores the coughing."),
    (T_MF, "Hard", "Street lighting is hard to price because it is non-rival and non-excludable, making it a",
     "public good", "private good", "inferior good", "luxury", "A",
     "None can be barred from its beam."),
    (T_MF, "Medium", "Free education supplied because society under-consumes it is an example of a",
     "merit good", "demerit good", "public bad", "capital good", "A",
     "The state nudges the worthy choice."),

    # ------------------------------------------------------------- labour
    (T_LAB, "Medium", "The market wage in a free labour market settles where demand for labour meets",
     "supply of labour", "union decree", "government wage boards", "the pension fund", "A",
     "Two curves together fix the pay."),
    (T_LAB, "Hard", "A welder who moves from Kaduna to Port Harcourt for better pay displays",
     "geographical mobility", "vertical mobility", "occupational rigidity", "seasonal drift", "A",
     "His skill crossed the map."),

    # ------------------------------------------------------------- money, prices, jobs
    (T_MON, "Medium", "A yam farmer sells his crop now and holds the proceeds until planting season. Money makes this possible because it",
     "stores value safely", "melts in the rain", "feeds his family", "grows new tubers", "A",
     "Wealth sleeps safely in it."),
    (T_MON, "Hard", "Inflation in Nigeria is commonly traced month by month through the",
     "consumer price index", "wholesale butcher list", "football index", "school fees list", "A",
     "The CPI tracks the family basket."),
    (T_MON, "Hard", "A general, persistent fall in price levels is",
     "deflation", "reflation", "stagflation", "hyperinflation", "A",
     "Falling prices can starve trade."),
    (T_MON, "Medium", "A tailor jobless between employers for a few weeks suffers",
     "frictional unemployment", "structural unemployment", "seasonal unemployment", "cyclical unemployment", "A",
     "Between jobs, briefly adrift."),
    (T_MON, "Hard", "Bank clerks displaced by ATM machines face",
     "structural unemployment", "frictional unemployment", "seasonal unemployment", "disguised employment", "A",
     "The skill itself is obsolete."),

    # ------------------------------------------------------------- banking
    (T_BK, "Hard", "As lender of last resort, the Central Bank lends to",
     "commercial banks in distress", "market women", "foreign governments", "school bursars", "A",
     "When all doors close, it opens."),
    (T_BK, "Medium", "The Central Bank keeps government accounts because it is",
     "banker to the government", "a profit-seeking bank", "owned by traders", "a savings house", "A",
     "The treasury banks with it."),
    (T_BK, "Hard", "Dapo banks N100,000; the bank lends most of it to Ada, whose account elsewhere receives it, feeding yet another loan. The chain shows banks creating money through",
     "lending from deposits", "printing fresh notes", "mining gold", "selling stamps", "A",
     "Each loan becomes someone's deposit."),

    # ------------------------------------------------------------- national income
    (T_NI, "Medium", "Summing the value added at every production stage measures national income by the",
     "output method", "income method", "expenditure method", "consumption method", "A",
     "Only value added is counted."),
    (T_NI, "Hard", "Counting both the bread and the flour inside it would commit the error of",
     "double counting", "transfer payment", "import leakage", "capital allowance", "A",
     "Flour already lives in the loaf."),
    (T_NI, "Hard", "Housewives' unpaid services are excluded from GDP partly because they are",
     "not marketed", "too useful", "taxed already", "imported", "A",
     "No market price tags the work."),
    (T_NI, "Medium", "GDP adjusted for price changes gives",
     "real GDP", "nominal GDP", "gross happiness", "per-capita debt", "A",
     "Constant prices strip the inflation."),

    # ------------------------------------------------------------- tax & budget
    (T_PF, "Hard", "A tax taking a larger share as income rises is",
     "progressive", "regressive", "proportional", "lump-sum", "A",
     "The rich shoulder a heavier slice."),
    (T_PF, "Hard", "A flat N1,000 levy on every trader regardless of earnings is",
     "regressive", "progressive", "proportional to profit", "a subsidy", "A",
     "It bites the small trader deepest."),
    (T_PF, "Medium", "When planned spending exceeds planned revenue, the budget shows a",
     "deficit", "surplus", "balance", "windfall", "A",
     "The gap must be borrowed shut."),
    (T_PF, "Hard", "Money a government owes to bondholders at home and abroad is its",
     "public debt", "private saving", "capital stock", "foreign reserve", "A",
     "Borrowed bread repays with interest."),

    # ------------------------------------------------------------- trade
    (T_TR, "Hard", "If Ghana produces a tonne of cocoa using fewer resources than every rival, Ghana holds",
     "absolute advantage", "comparative cost", "a monopoly", "a tariff wall", "A",
     "Absolute means outright best."),
    (T_TR, "Hard", "Cocoa prices rise while machinery prices fall, so each tonne of cocoa now buys more machines. This gain is described as favourable",
     "terms of trade", "balance of trade", "trade cycles", "exchange control", "A",
     "How much imports each export buys."),
    (T_TR, "Medium", "A persistent balance of payments deficit can be financed by",
     "drawing down foreign reserves", "printing salary awards", "banning all banks", "raising school fees", "A",
     "Old savings pay new bills."),

    # ------------------------------------------------------------- development
    (T_DEV, "Medium", "Spending on education and health builds a nation's",
     "human capital", "physical capital", "money capital", "circulating stock", "A",
     "Skilled bodies and minds compound."),
    (T_DEV, "Hard", "Absolute poverty is defined as inability to afford",
     "basic needs of life", "foreign holidays", "luxury cars", "private schools", "A",
     "Food, shelter and clothing first."),
    (T_DEV, "Hard", "The population size at which output per head is greatest is the",
     "optimum population", "maximum population", "Malthusian point", "census peak", "A",
     "Below or above it, income per head falls."),
]

build_batch(
    S,
    "batch_145_waec_econ5.json",
    "145",
    "WAEC Economics round 5 (R27 top-up): marginal utility and its "
    "diminishing law, consumer equilibrium; substitutes via cross "
    "elasticity, garri as inferior good, perishable supply inelastic; "
    "fixed costs, diminishing returns, increasing returns to scale, "
    "ATC formula; negative externality, street lighting as public "
    "good, free education as merit good; wage equilibrium, "
    "geographical mobility; store-of-value money, CPI, deflation; "
    "frictional vs structural unemployment; lender of last resort, "
    "banker to government, credit creation; output method, double "
    "counting, unpaid housework exclusion, real GDP; progressive vs "
    "regressive taxes, budget deficit, public debt; absolute "
    "advantage, terms of trade, reserves-financed BOP deficit; human "
    "capital, absolute poverty, optimum population. Scanned against "
    "WAEC rounds 1-4, NECO Economics (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
