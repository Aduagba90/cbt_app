"""Batch 140 - NECO Economics round 4 (NECO top-up, Round 26).

Lifts NECO Economics from 160 toward ~197 with angles not yet in any
bank: scale of preference and opportunity cost; production factors
rewards; division of labour limits; movement along vs shift of demand
and supply; PED arithmetic and inelastic staples; perfect competition
vs monopoly; oligopoly interdependence; Malthusian caution and census
uses; barter problems; money qualities; demand-pull vs cost-push
inflation; CBN open-market operations and cash-reserve ratio; budget
purposes and tariff canons; national income uses and per-capita
division; specialisation and comparative cost; balance of payments
structure; devaluation effects; growth vs development; agriculture's
contribution; small-scale enterprises; money and capital markets.
Scanned against NECO rounds 1-3, WAEC Economics (all rounds) and the
JAMB pool.

    python3 scripts/build_neco_batch140.py -> content/batch_140_neco_econ4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Economics"

T_BAS = "Basic Economic Concepts"
T_DEM = "Demand, Supply and Prices"
T_MAR = "Market Structures"
T_POP = "Population and Labour"
T_MON = "Money and Inflation"
T_POL = "Public Finance and Policy"
T_NAT = "National Income"
T_INT = "International Trade and Development"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- basics
    (T_BAS, "Medium", "A family ranks its needs in order of urgency. The list so arranged is its",
     "scale of preference", "budget deficit", "demand schedule", "cash ratio", "A",
     "First things are put first."),
    (T_BAS, "Hard", "A student who spends the night studying economics gives up sleep. The sleep forgone is the",
     "opportunity cost", "money cost", "fixed cost", "social cost", "A",
     "The road not taken is priced."),
    (T_BAS, "Medium", "The reward that flows to capital as a factor of production is",
     "interest", "rent", "wages", "profit", "A",
     "Money lent earns its keep."),
    (T_BAS, "Hard", "A chief weakness of extensive division of labour is that work becomes",
     "monotonous", "more skilled", "slower overall", "unpaid", "A",
     "One man, one screw, all day."),

    # ------------------------------------------------------------- demand & supply
    (T_DEM, "Hard", "A fall in the price of garri, other things equal, causes",
     "a movement down the demand curve", "an inward shift of demand", "an outward shift of demand", "the curve to vanish", "A",
     "Price speaks along the line."),
    (T_DEM, "Hard", "A rise in consumers' incomes, other things equal, causes",
     "an outward shift of the demand curve", "a movement along the curve", "an inward shift of supply", "a price ceiling", "A",
     "The whole line travels right."),
    (T_DEM, "Medium", "When bread rises from N200 to N250 a loaf and daily sales fall from 80 to 60 loaves, the demand for bread is",
     "elastic", "inelastic", "perfectly elastic", "unitary", "A",
     "The drop outweighs the rise in force."),
    (T_DEM, "Hard", "A 10% rise in the price of salt cuts its quantity demanded by barely 2%. Salt demand is",
     "highly inelastic", "highly elastic", "perfectly elastic", "unit elastic", "A",
     "Kitchens cannot do without it."),
    (T_DEM, "Medium", "At the market-clearing price, the quantity buyers willingly take stands",
     "equal to quantity supplied", "far above supply", "at zero", "fixed by decree", "A",
     "The curves shake hands there."),
    (T_DEM, "Medium", "A government-fixed price below equilibrium, holding for rent, is called a",
     "price ceiling", "price floor", "shadow price", "reserve price", "A",
     "The lid presses the market down."),

    # ------------------------------------------------------------- market structures
    (T_MAR, "Hard", "In perfect competition, each firm is a price",
     "taker", "maker", "fixer", "breaker", "A",
     "Its output alone moves no market."),
    (T_MAR, "Medium", "A monopoly exists when there is",
     "a single seller", "perfect knowledge", "free entry", "many small firms", "A",
     "One throat holds the tap."),
    (T_MAR, "Hard", "Oligopolists watch each other's pricing closely because they are",
     "few and interdependent", "many and independent", "price takers by law", "producing different crops", "A",
     "Each move answers another's."),
    (T_MAR, "Medium", "In a market where many sellers dress nearly identical goods in different brand names, the structure is",
     "monopolistic competition", "perfect competition", "duopoly", "communal farming", "A",
     "Brands dress the same goods."),

    # ------------------------------------------------------------- population
    (T_POP, "Medium", "Malthus warned that population grows faster than",
     "food supply", "city traffic", "school fees", "money supply", "A",
     "Geometric hunger meets arithmetic farms."),
    (T_POP, "Medium", "Census figures help government mainly in",
     "planning and revenue sharing", "naming new streets", "printing passports", "fixing match dates", "A",
     "Numbers guide the budget knife."),
    (T_POP, "Hard", "The age structure of Nigeria's population, heavy at the base, implies a high",
     "dependency ratio", "retirement ratio", "savings surplus", "tax per worker", "A",
     "Few shoulders carry many mouths."),

    # ------------------------------------------------------------- money & inflation
    (T_MON, "Medium", "The greatest weakness of barter trade is the",
     "double coincidence of wants", "weight of gold", "cost of banks", "need for receipts", "A",
     "Two wants must meet at once."),
    (T_MON, "Medium", "For money to serve well, it must above all be",
     "generally acceptable", "paper-made", "foreign-printed", "heavy to carry", "A",
     "Trust walks it from hand to hand."),
    (T_MON, "Hard", "Too much money chasing too few goods describes",
     "demand-pull inflation", "cost-push inflation", "deflation", "stagflation", "A",
     "Thick wallets, thin shelves."),
    (T_MON, "Hard", "Inflation born of rising fuel and transport costs is",
     "cost-push", "demand-pull", "imported luxury", "profit-induced", "A",
     "The bill starts at the pump."),

    # ------------------------------------------------------------- public finance
    (T_POL, "Medium", "When the Central Bank sells treasury securities in the open market, it aims to",
     "reduce the money supply", "raise the money supply", "print new notes", "end all banking", "A",
     "Sale soaks cash from banks."),
    (T_POL, "Hard", "Raising the cash-reserve ratio of banks chiefly",
     "shrinks their lending power", "raises their profits", "wipes their deposits", "lowers prices at once", "A",
     "More locked away, less to lend."),
    (T_POL, "Medium", "A government budget exists chiefly to",
     "plan revenue and spending", "record past prices", "set world tariffs", "audit the courts", "A",
     "A money map drawn for the year."),
    (T_POL, "Hard", "By the canon of convenience, a good tax should be",
     "easy to assess and pay", "punitive to the rich", "hidden from payers", "paid only by firms", "A",
     "Paying it should pain nobody."),
    (T_POL, "Medium", "Recurrent expenditure of a government covers",
     "salaries and running costs", "new airport projects", "share purchases", "foreign reserves", "A",
     "The daily bread of government."),

    # ------------------------------------------------------------- national income
    (T_NAT, "Medium", "Per-capita income is found by dividing national income by the",
     "total population", "number of workers", "number of firms", "land area", "A",
     "The national cake per head."),
    (T_NAT, "Hard", "GDP differs from GNP in that GDP counts output",
     "produced within the borders", "owned by citizens abroad", "of foreigners only", "of farms only", "A",
     "Location, not ownership, rules."),
    (T_NAT, "Medium", "National income figures are used chiefly to compare",
     "living standards over time", "football leagues", "weather patterns", "birth names", "A",
     "The tape measure of nations."),

    # ------------------------------------------------------------- trade & development
    (T_INT, "Hard", "A nation specialises most wisely where its sacrifice of other goods is least, obeying the law of",
     "comparative cost", "absolute advantage", "diminishing returns", "increasing cost", "A",
     "Sacrifice least, specialise there."),
    (T_INT, "Medium", "Visible trade together with services flows through the balance-of-payments section called the",
     "current account", "capital account", "official reserves", "errors and omissions", "A",
     "Goods cross with services."),
    (T_INT, "Hard", "Devaluation of the naira makes Nigerian exports",
     "cheaper to foreigners", "costlier to foreigners", "illegal abroad", "heavier at ports", "A",
     "A weaker naira sells more."),
    (T_INT, "Medium", "A country may post rising output figures while welfare stands still. The concept that captures welfare and structural change is",
     "economic development", "economic growth", "gross domestic product", "terms of trade", "A",
     "Growth is size; development is health."),
    (T_INT, "Medium", "To the Nigerian economy, agriculture remains vital mainly for",
     "food and raw materials", "printing currency", "defence contracts", "airline services", "A",
     "The farm feeds factory and family."),
    (T_INT, "Hard", "A leading merit of small-scale enterprises in Nigeria is their",
     "use of local labour", "huge capital base", "foreign ownership", "complete tax freedom", "A",
     "Small shops employ the street."),
    (T_INT, "Medium", "Long-term company shares and bonds are traded in the",
     "capital market", "money market", "commodity market", "labour market", "A",
     "Years-long papers change hands."),
]

build_batch(
    S,
    "batch_140_neco_econ4.json",
    "140",
    "NECO Economics round 4 (Round 26 top-up): scale of preference, "
    "opportunity cost of study, interest as capital's reward, monotony "
    "of division of labour; movement along vs shifts of curves, salt "
    "demand inelastic, equilibrium handshake, rent price ceiling; "
    "price taker, monopoly single seller, oligopoly interdependence, "
    "monopolistic product differentiation; Malthus vs food, census "
    "planning uses, wide-base dependency ratio; double coincidence of "
    "wants, general acceptability, demand-pull and cost-push "
    "inflation; OMO sales soak money, cash-reserve ratio, budget "
    "purpose, canon of convenience, recurrent expenditure; per-capita "
    "division, GDP border rule, living-standard comparisons; "
    "comparative opportunity cost, current account, devaluation "
    "cheapens exports, development beyond growth, agriculture's food "
    "and raw materials, small-scale enterprise merits, capital market. "
    "Scanned against NECO rounds 1-3, WAEC Economics (all rounds) and "
    "the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
