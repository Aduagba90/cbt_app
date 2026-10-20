"""Batch 119 - WAEC Economics round 3 (WAEC top-up, Round 23).

Lifts WAEC Economics from 138 toward ~180 with angles not yet in any
bank: scale of preference and opportunity cost (numeric), production
and factor mobility, demand and supply shifters, elasticity numerics,
market structures compared, money and inflation types, CBN monetary
policy tools, public finance (tax canons, budget types), trade
(absolute vs comparative advantage, terms of trade), population
theories, agriculture and industry in development, and labour matters.
Scanned against WAEC rounds 1-2, NECO Economics and the JAMB Economics
pool.

    python3 scripts/build_neco_batch119.py -> content/batch_119_waec_econ3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Economics"

T_BAS = "Basic Concepts"
T_PROD = "Production and Firms"
T_MKT = "Markets and Prices"
T_MON = "Money, Banking and Inflation"
T_PUB = "Public Finance"
T_TRADE = "Trade and Development"
T_POP = "Population and Labour"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- basics
    (T_BAS, "Medium", "Wants ranked from most to least pressing form the",
     "scale of preference", "production chart", "supply curve", "price index", "A",
     "The most urgent want comes first."),
    (T_BAS, "Hard", "A student with N1,000 buys a textbook and forgoes a meal; the meal is the",
     "opportunity cost", "money cost", "social cost", "fixed cost", "A",
     "The forgone alternative is priced."),
    (T_BAS, "Hard", "Economics exists because of",
     "scarcity and choice", "abundance for all", "endless money", "perfect foresight", "A",
     "Human wants outrun resources."),
    (T_BAS, "Medium", "Goods used together, like tea and sugar, are",
     "complements", "substitutes", "inferior goods", "luxuries", "A",
     "One pulls the other along."),
    (T_BAS, "Medium", "Garri and rice at the table are mostly",
     "substitutes", "complements", "capital goods", "public goods", "A",
     "Either one can stand in for the other."),
    (T_BAS, "Hard", "When pay rises and buyers drop a good, that good is",
     "inferior", "normal", "superior", "neutral", "A",
     "The poor man's bread loses the rich."),

    # ------------------------------------------------------------- production and firms
    (T_PROD, "Medium", "Land, labour, capital and entrepreneurship are the",
     "factors of production", "factors of demand", "markets types", "price list", "A",
     "Four pillars carry output."),
    (T_PROD, "Hard", "The ease with labour moves between trades is called its",
     "mobility", "productivity", "wage rate", "supply curve", "A",
     "Some skills travel poorly."),
    (T_PROD, "Medium", "Production that creates direct satisfaction, like a barber's work, is",
     "direct production", "indirect production", "mass production", "batch production", "A",
     "Service straight to the user."),
    (T_PROD, "Medium", "The law of diminishing returns begins to bite when",
     "extra hands add less", "prices start falling", "all land is sold", "machines stand idle", "A",
     "Too many hands crowd the plot."),
    (T_PROD, "Hard", "Costs that stay fixed however much is produced in the short run include",
     "factory rent", "raw materials", "power used", "packaging", "A",
     "The landlord is paid the same."),
    (T_PROD, "Medium", "The money a firm earns from sales is its",
     "revenue", "profit", "wage bill", "subsidy", "A",
     "Price times quantity sold."),

    # ------------------------------------------------------------- markets and prices
    (T_MKT, "Medium", "A rise in consumers' income, for a normal good, shifts demand to the",
     "right", "left", "origin", "ceiling", "A",
     "More income means more buying."),
    (T_MKT, "Medium", "Which single factor slides a buyer up and down his existing demand curve?",
     "the good's own price", "incomes", "tastes", "population", "A",
     "The curve itself stays still."),
    (T_MKT, "Hard", "If quantity demanded falls 10% after a 5% price rise, demand is",
     "elastic", "inelastic", "unit elastic", "perfectly inelastic", "A",
     "The response beats the cause."),
    (T_MKT, "Hard", "Price of bread rises from N100 to N150 and quantity demanded drops from 40 to 20 loaves; demand here is",
     "elastic", "inelastic", "unit elastic", "infinitely elastic", "A",
     "A 50% price rise halved the loaves."),
    (T_MKT, "Hard", "The market with a single seller of a unique product is",
     "monopoly", "perfect competition", "duopoly", "monopsony", "A",
     "One seller rules the market."),
    (T_MKT, "Hard", "Perfect competition requires many sellers of an identical product and",
     "free entry and exit", "secret prices", "one huge buyer", "state quotas", "A",
     "No fence guards the market."),
    (T_MKT, "Medium", "The equilibrium price sits where quantity demanded",
     "equals quantity supplied", "exceeds supply twice", "is zero", "is rationed", "A",
     "The two curves cross there."),
    (T_MKT, "Medium", "A maximum price fixed below equilibrium usually creates",
     "excess demand and queues", "a permanent glut", "perfect balance", "rising supply", "A",
     "Cheap price, empty shelves."),
    (T_MKT, "Medium", "A minimum price fixed above equilibrium, as for some farm produce, creates",
     "excess supply", "excess demand", "a black market only", "zero supply", "A",
     "Unsold farm stock piles up."),

    # ------------------------------------------------------------- money, banking, inflation
    (T_MON, "Medium", "Money's function as a store of value means it",
     "keeps worth for later", "measures all prices", "ends barter delay", "pays tax directly", "A",
     "Today's pay funds next month."),
    (T_MON, "Medium", "Inflation is a sustained",
     "rise in general prices", "fall in all prices", "rise in output only", "drop in money supply", "A",
     "Each naira buys less than before."),
    (T_MON, "Hard", "Inflation pushed up by production costs like fuel and wages is",
     "cost-push inflation", "demand-pull inflation", "imported deflation", "bottled inflation", "A",
     "Costs push the price tag."),
    (T_MON, "Hard", "Prices climbing because money is plentiful while goods are scarce is",
     "demand-pull", "cost-push", "structural only", "suppressed", "A",
     "Heavy demand drags prices up."),
    (T_MON, "Medium", "The central bank's bank rate is the",
     "rate for lending to banks", "public savings rate", "the exchange rate", "tax on deposits", "A",
     "Lender of last resort's price."),
    (T_MON, "Hard", "Selling treasury securities to the public by the CBN aims to",
     "reduce the money supply", "raise the money supply", "print more notes", "raise inflation", "A",
     "Open-market sales soak cash."),
    (T_MON, "Hard", "The cash reserve ratio works on money supply because banks",
     "must keep some deposits idle", "lend every kobo out", "print their own notes", "pay it as dividend", "A",
     "Idle cash cannot multiply."),
    (T_MON, "Medium", "A barter trader's biggest headache is the need for",
     "a double coincidence of wants", "many warehouses", "strong muscles", "government licence", "A",
     "Each must want the other's ware."),

    # ------------------------------------------------------------- public finance
    (T_PUB, "Medium", "Which tax stays squarely on the shoulder of the payer?",
     "direct", "indirect", "progressive only", "regressive only", "A",
     "The payer carries it alone."),
    (T_PUB, "Hard", "A tax that takes a higher percentage from the rich than the poor is",
     "progressive", "regressive", "proportional", "lump-sum", "A",
     "Ability to pay guides it."),
    (T_PUB, "Hard", "VAT in Nigeria is classified as an",
     "indirect tax", "direct tax", "capital levy", "import duty only", "A",
     "The final consumer bears it."),
    (T_PUB, "Medium", "A budget that plans spending above revenue is",
     "a deficit budget", "a surplus budget", "a balanced budget", "a capital budget", "A",
     "Borrowing fills the hole."),
    (T_PUB, "Medium", "Government spending to fight a recession is called",
     "fiscal policy", "monetary policy", "trade policy", "wage policy", "A",
     "The treasury leads the push."),
    (T_PUB, "Medium", "Public debt owed to citizens at home is",
     "internal debt", "external debt", "equity", "a grant", "A",
     "The creditors live inside."),

    # ------------------------------------------------------------- trade and development
    (T_TRADE, "Medium", "A country's terms of trade compare its",
     "export prices with import prices", "exports with population", "budget with GDP", "savings with loans", "A",
     "The ratio tells who gains."),
    (T_TRADE, "Hard", "Nigeria's overreliance on crude oil exports is a case of",
     "a monoculture economy", "a diversified economy", "an industrial economy", "a service economy", "A",
     "One product carries the nation."),
    (T_TRADE, "Hard", "Protecting infant industries argues for",
     "temporary tariffs", "permanent free trade", "banning all exports", "abolishing customs", "A",
     "Nurture before the storm."),
    (T_TRADE, "Medium", "Economic growth measures a rise in output, while development adds",
     "welfare and structural change", "more money printing", "higher party membership", "longer borders", "A",
     "Growth feeds people or fails."),
    (T_TRADE, "Medium", "Subsistence agriculture slows development because it",
     "ties most labour to low output", "earns the most forex", "builds the best roads", "spreads technology fastest", "A",
     "Many hands, little surplus."),

    # ------------------------------------------------------------- population and labour
    (T_POP, "Medium", "The natural growth rate of population is births minus",
     "deaths", "migration", "taxes", "schooling", "A",
     "It is nature's ledger alone."),
    (T_POP, "Hard", "Malthus predicted population growing faster than",
     "food supply", "money supply", "city land", "hospitals", "A",
     "His doom was later eased by technology."),
    (T_POP, "Hard", "When the working-age share of the population rises, a country enjoys a",
     "demographic dividend", "demographic drag", "census boom", "migrant surplus", "A",
     "Workers outnumber dependants."),
    (T_POP, "Medium", "Unemployment among school leavers who seek office work is",
     "structural unemployment", "frictional unemployment", "seasonal unemployment", "cyclical unemployment", "A",
     "Skills mismatch lies beneath."),
    (T_POP, "Medium", "A trade union chiefly bargains for",
     "better wages and conditions", "higher company profit", "lower taxes on firms", "shorter school terms", "A",
     "The workers' voice at the table."),
]

build_batch(
    S,
    "batch_119_waec_econ3.json",
    "119",
    "WAEC Economics round 3 (Round 23 top-up): scale of preference, "
    "opportunity cost, scarcity, complements vs substitutes, inferior "
    "goods, factor mobility, direct production, diminishing returns, "
    "fixed costs, revenue, demand shifters vs movements, elasticity "
    "numerics (2x response, halved loaves), monopoly and perfect "
    "competition features, equilibrium, maximum and minimum price "
    "effects, money's store of value, cost-push vs demand-pull "
    "inflation, bank rate, open-market operations, cash reserve ratio, "
    "barter's double coincidence, direct vs indirect and progressive "
    "taxes, VAT, deficit budget, fiscal policy, internal debt, terms of "
    "trade, monoculture, infant-industry tariffs, growth vs development, "
    "subsistence drag, natural growth rate, Malthus, demographic "
    "dividend, structural unemployment and trade unions. Scanned against "
    "WAEC rounds 1-2, NECO Economics and the JAMB Economics pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
