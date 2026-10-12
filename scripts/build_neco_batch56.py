"""Batch 056 - NECO Economics, Paper III Objective round 1.

NECO SSCE Economics Paper III is a 60-item objective paper (1 hr).
This batch covers the SSCE economics syllabus with Nigerian examples
(CBN, naira, OPEC, ECOWAS, cocoa, crude oil) and near-duplicate scans
against the JAMB and WAEC banks.

    python3 scripts/build_neco_batch56.py -> content/batch_056_neco_economics.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Economics"

T_CON = "Basic Economic Concepts"
T_SYS = "Economic Systems"
T_TOOL = "Tools of Economic Analysis"
T_CONS = "Theory of Consumer Behaviour"
T_PROD = "Theory of Production"
T_DS = "Demand and Supply"
T_ELAS = "Elasticity"
T_MKT = "Market Structures"
T_BIZ = "Business Organisations"
T_DIST = "Distributive Trade"
T_POP = "Population and Labour"
T_MON = "Money and Inflation"
T_FIN = "Financial Institutions"
T_PUB = "Public Finance"
T_INT = "International Trade"
T_DEV = "Economic Development and Planning"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------- basic concepts
    (T_CON, "Easy", "The fundamental economic problem of every society is",
     "scarcity", "unemployment", "inflation", "corruption", "A",
     "Human wants are endless while resources to satisfy them are limited."),
    (T_CON, "Easy", "Economics is best defined as the study of how society",
     "allocates its scarce resources", "prints money and coins",
     "elects its leaders", "predicts the weather", "A",
     "Economics studies choice under scarcity."),
    (T_CON, "Medium", "The opportunity cost of a choice is the",
     "next best alternative forgone", "money paid for the choice",
     "total of all alternatives", "cost of all past choices", "A",
     "Choosing one thing means giving up the next best alternative."),
    (T_CON, "Easy", "Land as a factor of production includes",
     "rivers, minerals and forests", "machines and tools",
     "money in the bank", "trained workers", "A",
     "Land means all gifts of nature used in production."),
    (T_CON, "Easy", "For taking the risks of business, the entrepreneur is rewarded with",
     "profit", "rent", "wages", "interest", "A",
     "Entrepreneurs earn profit for risk-taking; land earns rent, labour wages, capital interest."),
    (T_CON, "Medium", "The curve showing the maximum combinations of two goods an economy can produce from its resources is the",
     "production possibility curve", "demand curve",
     "supply curve", "indifference curve", "A",
     "The PPC/PPF marks the frontier of attainable output."),
    (T_CON, "Easy", "Human wants are described as insatiable because they are",
     "without end", "easy to satisfy",
     "identical for everybody", "always material", "A",
     "As one want is satisfied, another arises."),

    # ---------------------------------------------------------- economic systems
    (T_SYS, "Medium", "An economic system in which the means of production are owned and controlled largely by private individuals is",
     "capitalism", "socialism", "communism", "feudalism", "A",
     "Private ownership of resources with market prices defines capitalism."),
    (T_SYS, "Medium", "In a socialist economy, the major economic decisions are taken by the",
     "government or central planning authority", "market forces of demand and supply",
     "traditional elders", "foreign investors", "A",
     "Socialism concentrates production decisions in central hands."),
    (T_SYS, "Easy", "The economic system in which resources are allocated mainly through the price mechanism is the",
     "free market economy", "command economy", "subsistence economy",
     "traditional economy", "A",
     "Prices signal buyers and sellers in a free market."),
    (T_SYS, "Hard", "In a mixed economy, productive resources are held by",
     "both public and private hands", "government alone",
     "private persons alone", "foreigners only", "A",
     "Nigeria's economy mixes public corporations with private firms."),

    # ------------------------------------------------- tools of economic analysis
    (T_TOOL, "Medium", "A table showing the relationship between price and quantity demanded is called a",
     "demand schedule", "supply curve", "production table", "price index", "A",
     "The schedule lists quantities demanded at each price."),
    (T_TOOL, "Easy", "In economics, a graph of the demand schedule is called a",
     "demand curve", "histogram", "pie chart", "pictogram", "A",
     "Plotting the schedule gives the demand curve."),
    (T_TOOL, "Medium", "The mean of the numbers 4, 8, 10, 14 is",
     "9", "8", "10", "36", "A",
     "The mean is the sum 36 divided by the count 4.",
     "(4+8+10+14)/4"),
    (T_TOOL, "Hard", "The median of the values 3, 9, 5, 11, 7 is",
     "7", "5", "9", "3", "A",
     "Ordered 3, 5, 7, 9, 11; the middle value is 7.",
     "7"),
    (T_TOOL, "Medium", "Variables that move in the SAME direction are said to have a",
     "positive correlation", "negative correlation",
     "zero correlation", "scattered correlation", "A",
     "Both rising or both falling together is positive correlation."),

    # ------------------------------------------------- theory of consumer behaviour
    (T_CONS, "Medium", "The satisfaction a consumer derives from consuming a good is called",
     "utility", "profit", "rent", "cost", "A",
     "Utility is the satisfaction from consumption."),
    (T_CONS, "Hard", "The additional satisfaction gained from consuming one more unit of a good is",
     "marginal utility", "total utility", "average utility", "negative utility", "A",
     "Marginal utility is the change in total utility from an extra unit."),
    (T_CONS, "Medium", "As a person consumes more and more units of a good, the satisfaction added by each extra unit",
     "decreases", "increases", "stays constant", "becomes infinite", "A",
     "Successive units give smaller and smaller added satisfaction."),
    (T_CONS, "Easy", "A consumer gets the greatest satisfaction when marginal utility per naira is",
     "equal for all goods bought", "highest for the dearest good",
     "zero for the last good", "negative for all goods", "A",
     "Equilibrium equalises marginal utility per naira across goods."),
    (T_CONS, "Medium", "An indifference curve shows combinations of two goods that give a consumer",
     "equal satisfaction", "equal expenditure", "equal prices",
     "equal weights", "A",
     "Every point on the curve is equally preferred."),

    # ------------------------------------------------------ theory of production
    (T_PROD, "Medium", "The law of diminishing returns applies most clearly in the",
     "short run when one factor is fixed", "long run when all factors vary",
     "money market", "foreign exchange market", "A",
     "With land fixed, adding more labour eventually adds less output."),
    (T_PROD, "Easy", "The cost that does NOT change with the level of output is a",
     "fixed cost", "variable cost", "total cost", "marginal cost", "A",
     "Rent on a shop is fixed regardless of output."),
    (T_PROD, "Medium", "A firm's total cost is the sum of its fixed costs and its",
     "variable costs", "profits", "revenues", "taxes only", "A",
     "Total cost adds together every fixed cost and every variable cost of production."),
    (T_PROD, "Hard", "Whenever marginal cost lies below average cost, average cost must be",
     "falling", "rising", "constant", "negative", "A",
     "A below-average addition pulls the average down."),
    (T_PROD, "Easy", "Output per unit of input is known as",
     "productivity", "consumption", "demand", "supply", "A",
     "Productivity measures efficiency of inputs."),
    (T_PROD, "Medium", "The shortest period in which ALL factors of production can be varied is the",
     "long run", "short run", "market period", "fixed period", "A",
     "Only in the long run can every input be changed."),

    # --------------------------------------------------------- demand and supply
    (T_DS, "Easy", "According to the law of demand, when the price of a good falls, quantity demanded",
     "rises, all else equal", "falls", "stays the same", "disappears", "A",
     "Price and quantity demanded move in opposite directions."),
    (T_DS, "Easy", "The market price of a good is determined where demand",
     "equals supply", "exceeds supply", "is below supply", "is zero", "A",
     "Equilibrium price balances the two sides of the market."),
    (T_DS, "Medium", "Two goods are said to be substitutes when a rise in the price of one causes",
     "the demand for the other to rise", "the demand for the other to fall",
     "both demands to disappear", "supply to rise", "A",
     "Garri and yam: dearer yam pushes buyers toward garri."),
    (T_DS, "Medium", "A fall in the price of a factor of production used in making a good will normally",
     "increase the supply of the good", "decrease the supply of the good",
     "leave supply unchanged", "increase demand for the good", "A",
     "Cheaper inputs make production more profitable at every price."),
    (T_DS, "Hard", "If the government fixes the price of garri BELOW its equilibrium level, the likely result is",
     "excess demand (shortage)", "excess supply (surplus)",
     "a balanced market", "higher farm incomes", "A",
     "A binding price ceiling makes quantity demanded exceed quantity supplied."),
    (T_DS, "Easy", "The quantity of a good producers are willing to sell at a given price over a period is the",
     "supply", "demand", "stock", "surplus", "A",
     "Supply links price to quantity offered for sale."),

    # -------------------------------------------------------------- elasticity
    (T_ELAS, "Medium", "If a 10% rise in price causes a 20% fall in quantity demanded, the price elasticity of demand is",
     "2", "0.5", "10", "30", "A",
     "Elasticity is the percentage response over the percentage change: 20/10.",
     "20/10"),
    (T_ELAS, "Medium", "Demand for a good is described as INELASTIC when a change in its price causes",
     "a smaller percentage change in quantity demanded", "a larger percentage change in quantity demanded",
     "no change in quantity demanded", "an equal change in income", "A",
     "Inelastic demand responds less than proportionately."),
    (T_ELAS, "Easy", "Demand for salt in Nigeria is typically",
     "highly inelastic", "highly elastic", "perfectly elastic", "unitary", "A",
     "Salt is a necessity with few substitutes, so price changes barely affect purchases."),
    (T_ELAS, "Hard", "For a good whose demand is price elastic, raising its price slightly makes total revenue",
     "fall", "rise", "stay constant", "double", "A",
     "With elastic demand, quantity lost outweighs the price gained."),

    # ----------------------------------------------------------- market structures
    (T_MKT, "Medium", "A market with many buyers and sellers of an identical product, such that no single trader can influence price, is",
     "perfect competition", "monopoly", "oligopoly", "duopoly", "A",
     "Perfect competition requires many small traders of a homogeneous good."),
    (T_MKT, "Easy", "A market situation with only ONE seller of a good is called",
     "monopoly", "perfect competition", "oligopoly", "monopsony", "A",
     "Mono means one: a single seller controls the market."),
    (T_MKT, "Medium", "NEPA (now in power sector successor companies) is the closest Nigerian example of a natural monopoly in electricity distribution because",
     "duplicating the national grid would be wasteful", "many firms sell electricity cheaply",
     "consumers generate their own power", "it sells a differentiated product", "A",
     "Huge infrastructure costs make a single provider most efficient."),
    (T_MKT, "Hard", "A market dominated by a few large firms, such as Nigeria's cement industry, is best described as",
     "an oligopoly", "a monopoly", "perfect competition", "a cartel of one", "A",
     "Oligopoly means a handful of interdependent big players."),
    (T_MKT, "Medium", "Product differentiation is a key feature of",
     "monopolistic competition", "perfect competition", "duopoly only",
     "any market with one buyer", "A",
     "Many sellers of slightly different products: monopolistic competition."),

    # ------------------------------------------------------- business organisations
    (T_BIZ, "Easy", "A business owned and managed by one person who bears all its risks is a",
     "sole proprietorship", "partnership", "public limited company", "cooperative", "A",
     "The one-man business is the simplest firm form."),
    (T_BIZ, "Medium", "In a partnership, the maximum number of partners in ordinary business under Nigerian law is conventionally",
     "20", "2", "50", "100", "A",
     "Ordinary partnerships are conventionally capped at twenty members.",
     "20"),
    (T_BIZ, "Easy", "The document that governs the relationship among partners is the",
     "deed of partnership", "prospectus", "memorandum of association",
     "certificate of incorporation", "A",
     "The partnership deed sets out rights and duties."),
    (T_BIZ, "Medium", "Shares in a public limited company are freely",
     "transferred on the stock exchange", "held by one family only",
     "issued by the central bank", "redeemed by the government", "A",
     "The Nigerian Exchange allows free trading of plc shares."),
    (T_BIZ, "Hard", "One main disadvantage of a sole proprietorship is",
     "unlimited liability for the owner", "double taxation of dividends",
     "too much regulation by CAC", "difficulty in dissolving it", "A",
     "The owner's personal property can be claimed for business debts."),

    # ------------------------------------------------------------ distributive trade
    (T_DIST, "Easy", "The channel of distribution that links the producer directly to the final consumer is the",
     "direct sale channel", "wholesaler channel", "retailer channel",
     "broker channel", "A",
     "Farmers selling at the farm gate bypass middlemen."),
    (T_DIST, "Medium", "A wholesaler mainly buys in bulk from producers and sells",
     "in smaller quantities to retailers", "directly to government alone",
     "only abroad", "in bigger quantities to consumers", "A",
     "The wholesaler breaks bulk between producer and retailer."),
    (T_DIST, "Medium", "Middlemen are often criticised in Nigeria for",
     "raising final consumer prices", "producing fake goods",
     "refusing to pay taxes", "building roads", "A",
     "Each middleman margin adds to the final price."),
    (T_DIST, "Easy", "The market where foodstuffs are sold in small quantities directly to households is a",
     "retail market", "wholesale market", "stock exchange", "commodity exchange", "A",
     "Retail means selling to final consumers."),

    # ----------------------------------------------------------- population/labour
    (T_POP, "Easy", "The total number of people living in a country at a particular time is its",
     "population", "labour force", "census sample", "migration rate", "A",
     "Population counts everyone resident at that time."),
    (T_POP, "Medium", "The official count of the people of a country carried out periodically is a",
     "census", "survey of firms", "budget", "poll of voters", "A",
     "A census counts every person, usually every ten years."),
    (T_POP, "Hard", "The dependency ratio measures the proportion of the population that is",
     "outside the working-age bracket", "employed in factories",
     "registered to vote", "living in cities", "A",
     "The young and the old depend on the working group."),
    (T_POP, "Medium", "A rise in the productive working population, other things equal, tends to",
     "increase total output", "reduce total output",
     "leave output constant", "eliminate scarcity", "A",
     "More workers produce more goods and services."),
    (T_POP, "Easy", "The movement of people from one country to another to live is",
     "migration", "circulation", "commuting", "tourism", "A",
     "Migration is the movement of residence."),

    # -------------------------------------------------------------- money/inflation
    (T_MON, "Easy", "Anything generally accepted as payment for goods and services is",
     "money", "wealth", "capital", "a cheque only", "A",
     "General acceptability is money's defining quality."),
    (T_MON, "Easy", "The institution that issues Nigeria's legal tender currency is the",
     "Central Bank of Nigeria", "Ministry of Finance",
     "Nigerian Minting and Printing ns only", "commercial banks", "A",
     "The CBN has the sole right to issue naira notes and coins."),
    (T_MON, "Medium", "A sustained rise in the general price level is called",
     "inflation", "deflation", "recession", "devaluation", "A",
     "Inflation erodes money's purchasing power."),
    (T_MON, "Medium", "When a naira buys fewer goods than before, money is losing its function as a",
     "store of value", "medium of exchange today",
     "unit of account today", "standard of deferred payment today", "A",
     "Inflation attacks money's ability to hold value over time."),
    (T_MON, "Hard", "Cost-push inflation in Nigeria is typically triggered by",
     "rising input costs like fuel", "too much saving by households",
     "falling money wages", "a budget surplus", "A",
     "Higher production costs push prices up."),
    (T_MON, "Easy", "The value of money refers to the quantity of goods and services a unit of money can",
     "buy", "weigh", "print", "tax", "A",
     "Purchasing power defines the value of money."),

    # ------------------------------------------------------- financial institutions
    (T_FIN, "Easy", "The apex bank and banker to the government of Nigeria is the",
     "Central Bank of Nigeria", "Bank of Industry",
     "Nigerian Agricultural Bank", "Stock Exchange", "A",
     "The CBN supervises all banks and manages monetary policy."),
    (T_FIN, "Medium", "The interest rate at which the CBN lends to commercial banks as lender of last resort is influenced by its",
     "monetary policy rate", "import tariff", "excise duty",
     "personal income tax", "A",
     "The MPR anchors the banking system's lending rates."),
    (T_FIN, "Easy", "Accepting deposits and giving loans to customers is the primary business of",
     "commercial banks", "insurance companies", "stock brokers",
     "pension funds", "A",
     "Commercial banks intermediate between savers and borrowers."),
    (T_FIN, "Medium", "A document instructing a bank to pay a stated sum from one's account is a",
     "cheque", "promissory note", "treasury bill", "share certificate", "A",
     "Cheques are drawn orders on bank deposits."),
    (T_FIN, "Hard", "The money market deals mainly in",
     "short-term funds and instruments", "long-term shares and bonds",
     "foreign cars", "agricultural land", "A",
     "Treasury bills and call funds mature within a year."),

    # ------------------------------------------------------------- public finance
    (T_PUB, "Easy", "The main source of government revenue in Nigeria is currently",
     "crude oil earnings", "personal income tax", "motor park levies",
     "school fees", "A",
     "Oil sales and petroleum taxes dominate federally collected revenue."),
    (T_PUB, "Easy", "At the end of the fiscal year a deficit has occurred when planned expenditure",
     "exceeds total revenue", "falls below revenue",
     "equals its revenue", "is taxed away", "A",
     "Deficits are financed by borrowing."),
    (T_PUB, "Medium", "Which of these taxes falls directly on the person who finally bears it?",
     "Personal income tax", "Value added tax",
     "Import duty", "Excise duty", "A",
     "Personal income tax falls directly on the payer."),
    (T_PUB, "Medium", "A tax that takes a HIGHER percentage of income as income rises is",
     "progressive", "regressive", "proportional", "flat", "A",
     "Progression means the rich pay a larger fraction."),
    (T_PUB, "Hard", "The annual statement of a government's expected revenue and expenditure is the",
     "budget", "balance of payments", "census", "gazette", "A",
     "The budget plans the fiscal year."),
    (T_PUB, "Medium", "Public debt owed by a government to its own citizens is described as",
     "internal debt", "external debt", "odious debt", "short-term debt", "A",
     "Domestic borrowing creates internal debt."),

    # ---------------------------------------------------------- international trade
    (T_INT, "Easy", "The difference between a country's visible exports and imports is the",
     "balance of trade", "balance of payments", "terms of trade",
     "exchange rate", "A",
     "Visible goods alone give the balance of trade."),
    (T_INT, "Medium", "Nigeria's membership of OPEC exists mainly to",
     "coordinate crude oil production and prices", "promote cocoa exports",
     "manage the naira exchange rate", "regulate banks", "A",
     "OPEC is the petroleum exporters' cartel."),
    (T_INT, "Medium", "A tariff on imported rice is imposed mainly to",
     "protect local rice producers", "punish consumers",
     "raise transport costs", "ban eating rice", "A",
     "Tariffs make imports dearer, shielding local industry."),
    (T_INT, "Easy", "The policy of completely forbidding the importation of certain goods is",
     "an embargo", "a subsidy", "a quota only", "a tariff", "A",
     "Embargo means total prohibition."),
    (T_INT, "Hard", "The theory that a country should specialise in producing goods in which it has the lower opportunity cost is the theory of",
     "comparative advantage", "absolute advantage only",
     "balance of trade", "terms of trade", "A",
     "Ricardo's comparative advantage rests on opportunity cost."),
    (T_INT, "Medium", "ECOWAS was established in 1975 mainly to promote",
     "West African integration", "military rule",
     "colonial administration", "football in Africa", "A",
     "The treaty of Lagos created ECOWAS for regional cooperation."),

    # ------------------------------------------------- development and planning
    (T_DEV, "Medium", "Economic growth is best measured by a sustained increase in a country's",
     "real gross domestic product", "population",
     "money supply", "foreign aid", "A",
     "Real GDP tracks output of goods and services."),
    (T_DEV, "Easy", "The GDP of a country is the total money value of goods and services produced",
     "within its borders in a year", "by its citizens abroad",
     "by government only", "by farmers only", "A",
     "GDP is territorial; GNP counts citizens everywhere."),
    (T_DEV, "Medium", "Beyond rising output figures, true development also brings",
     "better welfare for the people", "higher money supply",
     "money supply changes", "exchange rates", "A",
     "Growth is more output; development is better lives."),
    (T_DEV, "Hard", "A major reason Nigeria adopted national development plans after independence was to",
     "focus spending on key sectors", "increase the population",
     "deregulate all prices", "leave farming", "A",
     "Plans coordinated public investment in infrastructure and industry."),
    (T_DEV, "Medium", "Rapid population growth can hinder development when it",
     "outpaces the growth of jobs and services", "slows the birth rate",
     "reduces the labour force", "raises school enrolment only", "A",
     "Dependents multiply faster than the economy provides for them."),
]

build_batch(
    S,
    "batch_056_neco_economics.json",
    "056",
    "NECO Economics Paper III round 1: fresh SSCE-standard items with Nigerian "
    "institutions and examples (CBN, naira, OPEC, ECOWAS, crude oil, garri "
    "and yam), near-duplicate scanned against the JAMB and WAEC banks. "
    "Concepts, systems, tools, consumer theory, production, demand and "
    "supply, elasticity, markets, business forms, distribution, population, "
    "money, finance, public finance, trade, development.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
