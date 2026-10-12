"""Batch 061 - NECO Economics top-up (round 2).

Grows the Economics bank from 84 to 150 items so students get two full
practice papers without repeats. New angles: scale of preference, barter,
complements and inferior goods, division of labour, economies of scale,
cooperatives, capital market, credit creation, canons of taxation,
absolute advantage, devaluation, optimum population, per capita income.
Near-dup scanned against JAMB, WAEC and the existing NECO bank.

    python3 scripts/build_neco_batch61.py -> content/batch_061_neco_economics2.json
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
    # ------------------------------------------------------- basic concepts (5)
    (T_CON, "Easy", "A list of a consumer's wants arranged in order of importance is called a",
     "scale of preference", "shopping budget", "price index",
     "balance sheet", "A",
     "The scale ranks wants so the most pressing comes first."),
    (T_CON, "Easy", "The alternative forgone each time a choice is made from the scale of preference is its",
     "opportunity cost", "money cost", "social cost",
     "production cost", "A",
     "The next best want given up is the real cost of the choice."),
    (T_CON, "Medium", "Sunlight and free air are classified as",
     "free goods", "economic goods", "capital goods",
     "luxury goods", "A",
     "Free goods need no effort or payment to obtain."),
    (T_CON, "Medium", "Man-made aids to production such as machinery and buildings are known as",
     "capital", "land", "labour", "entrepreneurship", "A",
     "Capital consists of produced means of further production."),
    (T_CON, "Hard", "The reward that accrues to land as a factor of production is",
     "rent", "wages", "interest", "profit", "A",
     "Land earns rent for its owner."),

    # ---------------------------------------------------------- systems (4)
    (T_SYS, "Medium", "The main motive for production in a capitalist economy is",
     "profit", "social equality", "national pride", "charity", "A",
     "Private firms produce chiefly to earn profit."),
    (T_SYS, "Hard", "A major defect of the market economy is that it can widen",
     "income inequality", "public ownership",
     "government spending", "rural roads", "A",
     "Unfettered markets reward some and leave others behind."),
    (T_SYS, "Medium", "A centrally planned economy relies mainly on",
     "government directives", "market prices",
     "traditional customs", "foreign investors", "A",
     "Planners decide what, how and for whom to produce."),
    (T_SYS, "Easy", "Nigeria's economy, with both government corporations and private firms, is best described as",
     "mixed", "socialist", "capitalist", "feudal", "A",
     "Public and private ownership side by side defines the mixed economy."),

    # ------------------------------------------------------------- tools (4)
    (T_TOOL, "Easy", "The value that occurs most frequently in a set of data is the",
     "mode", "mean", "median", "range", "A",
     "The mode is the observation with the highest frequency."),
    (T_TOOL, "Medium", "The difference between the highest and lowest values in a data set is the",
     "range", "mode", "mean", "median", "A",
     "Range measures the spread from top to bottom."),
    (T_TOOL, "Medium", "A graph in which pairs of values are plotted as scattered points to show a relationship is a",
     "scatter diagram", "pie chart", "histogram", "bar chart", "A",
     "Scatter diagrams reveal correlation between variables."),
    (T_TOOL, "Hard", "The average of the numbers 6, 4, 8, 2, 10 is",
     "6", "4", "8", "30", "A",
     "The mean is the sum 30 divided by 5 observations.",
     "(6+4+8+2+10)/5"),

    # --------------------------------------------------- consumer behaviour (4)
    (T_CONS, "Easy", "The total satisfaction a consumer gets from all the units of a good consumed is",
     "total utility", "marginal utility", "average utility",
     "derived utility", "A",
     "Total utility adds up satisfaction from every unit."),
    (T_CONS, "Hard", "If total utility is rising at a decreasing rate, then marginal utility is",
     "positive but falling", "negative and falling",
     "constant", "zero", "A",
     "Each extra unit still adds satisfaction, but less and less."),
    (T_CONS, "Medium", "A good whose demand FALLS as consumer income rises is called a",
     "an inferior good", "normal good", "luxury good",
     "complementary good", "A",
     "Better-off consumers switch away from garri to rice."),
    (T_CONS, "Medium", "The difference between what a consumer is willing to pay and what he actually pays is",
     "consumer surplus", "producer surplus", "economic rent",
     "profit margin", "A",
     "Satisfied buyers keep the surplus as extra welfare."),

    # ------------------------------------------------------- production (5)
    (T_PROD, "Medium", "The division of labour means breaking production into",
     "separate specialized tasks", "equal money shares",
     "local and imported parts", "big and small firms", "A",
     "Each worker repeats one task and becomes expert at it."),
    (T_PROD, "Medium", "A major advantage of the division of labour is greater",
     "efficiency and output", "worker fatigue",
     "cost of tools", "time wasting", "A",
     "Specialisation speeds work and raises total output."),
    (T_PROD, "Hard", "The reduction in average cost that a firm enjoys as it grows larger is called",
     "economies of scale", "diminishing returns",
     "marginal cost", "fixed cost", "A",
     "Bulk buying and spreading overheads lower unit costs."),
    (T_PROD, "Medium", "Costs that vary directly with the quantity produced, like raw materials, are",
     "variable costs", "fixed costs", "sunk costs",
     "implicit costs", "A",
     "More output means more materials purchased."),
    (T_PROD, "Medium", "The extra cost of producing one additional unit of output is the",
     "marginal cost", "average cost", "total cost",
     "fixed cost", "A",
     "Marginal cost is the addition to total cost from one more unit."),

    # --------------------------------------------------- demand and supply (6)
    (T_DS, "Medium", "Two goods are complements if a rise in the price of one causes the demand for the other to",
     "fall", "rise", "double", "stay fixed", "A",
     "Petrol and cars: dearer petrol reduces demand for big cars."),
    (T_DS, "Medium", "If the price of a good changes, we normally expect a movement ALONG the demand curve rather than",
     "a shift of the curve", "a new equilibrium only",
     "a change in taste", "a supply shift only", "A",
     "Price changes move us along; other factors shift the curve."),
    (T_DS, "Hard", "If the government fixes the price of kerosene ABOVE the market equilibrium, the likely result is",
     "excess supply (surplus)", "excess demand (shortage)",
     "a balanced market", "disappearance of sellers", "A",
     "A price floor discourages buyers and encourages sellers."),
    (T_DS, "Medium", "The demand for labour by a firm is described as a derived demand because it comes from",
     "the demand for its products", "the workers' own needs",
     "trade union rules", "government quota", "A",
     "Nobody hires bakers for their own sake but for bread."),
    (T_DS, "Hard", "Beef and hides produced together from the same cattle are said to be in",
     "joint supply", "composite demand", "competitive supply",
     "excess supply", "A",
     "Joint supply links two products from one source."),
    (T_DS, "Medium", "At a price above the equilibrium price, quantity supplied exceeds quantity demanded, creating a",
     "surplus", "shortage", "shortage floor", "ration", "A",
     "Sellers hold unsold stock when price is too high."),

    # ---------------------------------------------------------- elasticity (4)
    (T_ELAS, "Medium", "When demand is perfectly elastic, the demand curve is drawn",
     "horizontal", "vertical", "upward sloping", "curved inward", "A",
     "Any price rise wipes out all quantity demanded."),
    (T_ELAS, "Hard", "For close substitutes like different brands of milk, the price elasticity of demand is usually",
     "high", "low", "zero", "negative", "A",
     "Buyers switch brands easily when one gets dearer."),
    (T_ELAS, "Medium", "If a 20% rise in price leaves total revenue unchanged, demand is said to be",
     "unit elastic", "perfectly inelastic", "elastic", "inelastic", "A",
     "Equal percentage swings in price and quantity balance out."),
    (T_ELAS, "Hard", "If a rise in the price of tea increases the demand for coffee, their cross elasticity of demand is",
     "positive", "negative", "zero", "infinite", "A",
     "Dearer tea raises demand for coffee."),

    # -------------------------------------------------------- market structures (5)
    (T_MKT, "Easy", "A market with exactly TWO dominant sellers is called a",
     "duopoly", "monopoly", "oligopoly", "monopsony", "A",
     "Duo means two sellers facing all buyers."),
    (T_MKT, "Medium", "A monopolist is often described as a price",
     "maker", "taker", "regulator", "watchdog", "A",
     "It sets price because it faces no rivals."),
    (T_MKT, "Medium", "Price discrimination is possible only when the seller can separate buyers into",
     "different markets", "one single market", "government offices",
     "trade unions", "A",
     "Charging different prices requires separated markets."),
    (T_MKT, "Medium", "Restaurants, hairdressing salons and tailoring shops in a city are typical examples of",
     "monopolistic competition", "perfect competition",
     "pure monopoly", "duopoly", "A",
     "Many sellers with slightly different styles and prices."),
    (T_MKT, "Hard", "The single buyer in a market is called a",
     "monopsonist", "monopolist", "duopolist", "oligarch", "A",
     "Mono plus opsonia: one purchaser facing many sellers."),

    # ---------------------------------------------------- business organisations (5)
    (T_BIZ, "Easy", "The liability of shareholders in a limited company is limited to",
     "the amount they invested", "their personal houses",
     "the company's debt", "nothing at all", "A",
     "Limited liability protects private assets."),
    (T_BIZ, "Medium", "A business owned and run by its members, who share the benefits, such as a farmers' cooperative, is a",
     "cooperative society", "sole proprietorship",
     "public limited company", "partnership", "A",
     "Cooperatives serve members rather than outside shareholders."),
    (T_BIZ, "Medium", "The document that states a company's objects and powers is the",
     "memorandum of association", "deed of partnership",
     "articles only", "share warrant", "A",
     "The memorandum is the company's charter with the public."),
    (T_BIZ, "Hard", "A major source of finance available ONLY to public limited companies is",
     "selling shares to the public", "bank overdrafts",
     "trade credit", "retained profits", "A",
     "Only a plc may advertise shares on the stock exchange."),
    (T_BIZ, "Medium", "The minimum number of persons needed to form a private limited company in Nigeria is normally",
     "2", "1", "7",
     "20", "A",
     "Two members can register a private company.",
     "2"),

    # -------------------------------------------------------- distributive trade (4)
    (T_DIST, "Easy", "The retailer buys mainly from the",
     "wholesaler", "farmer directly", "central bank",
     "stock exchange", "A",
     "Retailers take smaller lots from wholesalers."),
    (T_DIST, "Medium", "Storing goods until they are needed by consumers is a function performed mainly by the",
     "wholesaler", "consumer", "central bank",
     "government printer", "A",
     "Warehousing balances supply across seasons."),
    (T_DIST, "Medium", "Buying and selling of goods over the internet, as done on Jumia and Konga, is called",
     "e-commerce", "barter", "smuggling",
     "counter trade", "A",
     "Electronic commerce moves markets online."),
    (T_DIST, "Easy", "The speedy movement of goods from farm to market is made possible mainly by",
     "transport", "insurance", "banking",
     "advertising", "A",
     "Transport bridges distance between buyer and seller."),

    # ----------------------------------------------------- population/labour (5)
    (T_POP, "Medium", "The number of live births per thousand of population in a year is the",
     "birth rate", "death rate", "growth rate",
     "dependency ratio", "A",
     "Birth rate is expressed per thousand people."),
    (T_POP, "Hard", "The population at which output per head is at its maximum is the",
     "optimum population", "overpopulation", "underpopulation",
     "census figure", "A",
     "Below it labour is short; above it output per head falls."),
    (T_POP, "Medium", "A country whose people are too few to fully use its resources is said to be",
     "underpopulated", "overpopulated", "at optimum",
     "migrating", "A",
     "Idle land and capital signal underpopulation."),
    (T_POP, "Medium", "Unemployment that arises when workers' skills no longer match available jobs is called",
     "structural unemployment", "frictional unemployment",
     "seasonal unemployment", "voluntary unemployment", "A",
     "Technological change makes old skills obsolete."),
    (T_POP, "Medium", "Education, training and good health are the main determinants of the",
     "efficiency of labour", "supply of land",
     "birth rate", "capital formation", "A",
     "Human capital raises what each worker can produce."),

    # --------------------------------------------------------- money/inflation (6)
    (T_MON, "Easy", "The biggest problem of barter exchange is the need for a",
     "double coincidence of wants", "common currency",
     "bank account", "price list", "A",
     "Each trader must want exactly what the other offers."),
    (T_MON, "Medium", "The use of money that allows a farmer to store wealth from harvest until the dry season is its function as a",
     "store of value", "unit of account",
     "medium of exchange", "standard of payment", "A",
     "Money holds purchasing power over time."),
    (T_MON, "Medium", "Inflation caused by too much money chasing too few goods is described as",
     "demand-pull inflation", "cost-push inflation",
     "imported inflation", "creeping inflation", "A",
     "Excess aggregate demand pulls prices upward."),
    (T_MON, "Hard", "A deliberate fall in the official value of a country's currency is called",
     "devaluation", "revaluation", "appreciation",
     "deflation", "A",
     "Devaluation makes exports cheaper and imports dearer."),
    (T_MON, "Medium", "A sustained fall in the general price level is known as",
     "deflation", "reflation", "devaluation",
     "stagflation", "A",
     "Deflation is the opposite of inflation."),
    (T_MON, "Hard", "One danger of very rapid inflation is that it turns people away from holding",
     "money", "land", "houses", "gold", "A",
     "Money loses value daily, so people flee to real goods."),

    # ------------------------------------------------- financial institutions (5)
    (T_FIN, "Medium", "The market for long-term funds, where shares and bonds are traded, is the",
     "capital market", "money market", "foreign exchange market",
     "commodity market", "A",
     "The Nigerian Exchange is the heart of the capital market."),
    (T_FIN, "Medium", "Commercial banks create money mainly by",
     "granting loans to customers", "printing new notes",
     "selling gold bars", "collecting taxes", "A",
     "Lending expands deposits across the banking system."),
    (T_FIN, "Easy", "When a commercial bank runs short of funds, its lender of last resort in Nigeria is the",
     "Central Bank of Nigeria", "Bank of Industry",
     "Nigerian Exchange", "NDIC", "A",
     "The CBN stands behind banks in distress."),
    (T_FIN, "Hard", "Buying and selling of government securities by the central bank to control money supply is called",
     "open market operation", "reserve requirement",
     "moral suasion", "credit rationing", "A",
     "OMO is the classic instrument of monetary policy."),
    (T_FIN, "Medium", "The business of pooling risks and compensating the insured against loss is",
     "insurance", "banking", "stockbroking",
     "auctioneering", "A",
     "Many premiums together cover the few who suffer loss."),

    # ---------------------------------------------------------- public finance (5)
    (T_PUB, "Medium", "The use of taxation and government spending to guide the economy is called",
     "fiscal policy", "monetary policy", "trade policy",
     "wage policy", "A",
     "Fiscal policy works through the budget."),
    (T_PUB, "Hard", "The classic principles of taxation, including equity and convenience, were set out by",
     "Adam Smith", "David Ricardo", "John Keynes",
     "Alfred Marshall", "A",
     "Smith's canons of taxation remain the standard checklist."),
    (T_PUB, "Medium", "A tax on goods and services that is collected at each stage of production in Nigeria is",
     "value added tax", "personal income tax",
     "capital gains tax", "petroleum profit tax", "A",
     "VAT is an indirect tax borne finally by consumers."),
    (T_PUB, "Hard", "The illegal refusal to pay a tax that is due is called tax",
     "evasion", "avoidance", "incidence",
     "capitalisation", "A",
     "Avoidance rearranges affairs lawfully; evasion cheats."),
    (T_PUB, "Medium", "Government spending on roads, schools and hospitals is called",
     "capital expenditure", "recurrent expenditure",
     "transfer payment", "debt interest", "A",
     "Capital spending creates long-lasting assets."),

    # ------------------------------------------------------ international trade (5)
    (T_INT, "Medium", "The theory that a country should produce the goods it makes with fewer resources than others is attributed to",
     "Adam Smith", "David Ricardo", "Jevons",
     "Pigou", "A",
     "Absolute advantage was Smith's case for free trade."),
    (T_INT, "Medium", "Trade in services such as banking, transport and tourism is described as",
     "invisible trade", "visible trade", "entrepot trade",
     "barter trade", "A",
     "Services cannot be stacked on a ship but earn foreign exchange."),
    (T_INT, "Medium", "The rate at which the naira exchanges for the dollar is the",
     "exchange rate", "inflation rate", "interest rate",
     "birth rate", "A",
     "It prices one currency in terms of another."),
    (T_INT, "Hard", "A quantitative limit on the quantity of a good that may be imported is a",
     "quota", "tariff", "subsidy", "embargo", "A",
     "Quotas cap quantity directly rather than price."),
    (T_INT, "Medium", "The deliberate lowering of trade barriers among ECOWAS member states is aimed at",
     "a wider common market", "higher consumer prices",
     "more customs posts", "stronger borders", "A",
     "The trade liberalisation scheme widens regional markets."),

    # ------------------------------------------------------ development (4)
    (T_DEV, "Easy", "Real GDP divided by the total population gives",
     "per capita income", "national income", "disposable income",
     "gross investment", "A",
     "Output per head is the rough guide to living standards."),
    (T_DEV, "Medium", "The index that combines life expectancy, education and income to rank development is the",
     "Human Development Index", "consumer price index",
     "terms of trade", "dow index", "A",
     "The UNDP's HDI measures welfare beyond income."),
    (T_DEV, "Hard", "A common feature of underdeveloped economies is dependence on",
     "primary production", "heavy industry",
     "high technology", "services only", "A",
     "Farm outputs and raw materials dominate their exports."),
    (T_DEV, "Medium", "Raising a country's stock of machinery and infrastructure requires a high level of",
     "savings and investment", "consumption", "imports of luxuries",
     "money printing", "A",
     "Money saved today funds the capital of tomorrow."),
]

build_batch(
    S,
    "batch_061_neco_economics2.json",
    "061",
    "NECO Economics top-up (round 2): grows the bank to 150 items so "
    "students get two full 60-question papers without repeats. New angles "
    "- scale of preference, free goods, barter, complements, inferior "
    "goods, consumer surplus, division of labour, economies of scale, "
    "joint supply, price floor, duopoly, monopsony, cooperatives, "
    "memorandum of association, e-commerce, optimum population, structural "
    "unemployment, devaluation, capital market, open market operation, "
    "canons of taxation, quota, HDI, per capita income - near-duplicate "
    "scanned against the JAMB, WAEC and existing NECO banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
