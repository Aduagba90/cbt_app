"""Batch 171 - NECO Economics round 5 (NECO top-up, R32).

Grows NECO Economics from 196 toward ~231 with angles not yet in
the bank: form utility; production complete at the consumer;
consumer sovereignty; idle resources inside the production
possibility curve; a shift of demand from rising incomes; a record
harvest shifting supply right; income elasticity of a normal good
positive; the cartel; controlling a monopoly's prices; the
debenture; public corporations; the labour force; natural growth
as births minus deaths; the de facto census; cyclical unemployment;
the unemployment-rate formula; divisibility and portability of
money; the standard of deferred payment; pensioners losing and
debtors gaining in inflation; national income by the expenditure
method; transfer payments; GNP above GDP; the pie chart;
sampling; subsidy; proportional and regressive taxes; excise
duty; the budget surplus; capital expenditure; dumping; the
infant-industry argument; collective bargaining. Scanned against
NECO rounds 1-4, WAEC Economics (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch171.py -> content/batch_171_neco_econ5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Economics"

T_BEC = "Basic Economic Concepts"
T_TOOL = "Tools of Economic Analysis"
T_DS = "Demand and Supply"
T_ELA = "Elasticity"
T_MS = "Market Structures"
T_BO = "Business Organisations"
T_POP = "Population and Labour"
T_MON = "Money and Inflation"
T_NI = "National Income"
T_PF = "Public Finance"
T_IT = "International Trade"

PASSAGES = []
PQ = []

Q = [
    (T_BEC, "Easy", "Turning raw cotton into woven cloth at a Kaduna mill creates",
     "form utility", "place utility", "time utility", "possession utility", "A",
     "Changing the physical form of a good raises its usefulness."),
    (T_BEC, "Easy", "Economists say production is complete only when goods and services",
     "reach the final consumer", "leave the factory gate",
     "are packed in cartons", "are advertised on radio", "A",
     "Unsold goods in a warehouse have not finished their journey."),
    (T_BEC, "Medium", "In a free market, it is said that consumers ultimately decide what firms produce. This is called",
     "consumer sovereignty", "producer sovereignty",
     "product differentiation", "price leadership", "A",
     "Producers dance to the buyers' tune."),
    (T_BEC, "Medium", "An economy operating INSIDE its production possibility curve is suffering from",
     "idle or wasted resources", "overfull employment",
     "too much technology", "excess consumer choice", "A",
     "Points inside the curve mean unused capacity."),
    (T_DS, "Medium", "Salaries rise nationwide and shoppers flood the markets. In the demand diagram this appears as",
     "a shift of the whole curve to the right", "a movement along the same curve",
     "a shift of the curve to the left", "a kink at the old price", "A",
     "Income is not the good's own price, so the curve itself moves."),
    (T_DS, "Medium", "A record harvest of maize across the states shifts the supply curve of maize to the",
     "right", "left", "origin", "vertical axis", "A",
     "More is offered at every price after the bumper crop."),
    (T_ELA, "Hard", "When the price of bread moves and the demand for pencils does not stir, the cross elasticity between them is",
     "zero, showing unrelated goods", "one, showing substitutes",
     "negative, showing complements", "infinite, showing twins", "A",
     "Strangers in the basket leave each other unmoved."),
    (T_MS, "Hard", "A formal agreement among rival firms to fix prices and share the market between them is a",
     "cartel", "consortium of banks", "cooperative society", "trust fund", "A",
     "Competitors stop competing and act as one."),
    (T_MS, "Medium", "Governments sometimes control the prices a monopoly may charge chiefly to",
     "protect consumers from overcharging", "raise the monopoly's profits",
     "encourage the monopoly to expand", "reduce the number of buyers", "A",
     "The lone seller is bridled for the public good."),
    (T_BO, "Hard", "A long-term loan certificate issued by a company, carrying a fixed rate of interest, is a",
     "debenture", "preference share", "treasury bill", "bank draft", "A",
     "The holder is a lender, not an owner."),
    (T_BO, "Easy", "The old NEPA and the state water boards, owned and run by government, are examples of",
     "public corporations", "sole proprietorships",
     "partnerships at law", "private companies", "A",
     "Government owns, funds and appoints their boards."),
    (T_POP, "Easy", "The total number of people in a country who are willing and able to work make up its",
     "labour force", "population", "dependent group", "civil service", "A",
     "It counts the employed plus the jobless who seek work."),
    (T_POP, "Medium", "The natural growth rate of a country's population equals its",
     "birth rate minus the death rate", "birth rate plus the death rate",
     "immigration rate alone", "death rate minus emigration", "A",
     "Births add, deaths subtract; the gap is natural growth."),
    (T_POP, "Hard", "A census that counts people wherever they are found on the census night, and not at their hometowns, is",
     "a de facto census", "a de jure census",
     "a sample survey", "a vital registration", "A",
     "Presence on the night, not legal residence, is what counts."),
    (T_POP, "Medium", "Unemployment that swells whenever general business activity slumps is called",
     "cyclical unemployment", "structural unemployment",
     "frictional unemployment", "seasonal unemployment", "A",
     "When trade breathes out, jobs vanish with it."),
    (T_POP, "Medium", "Farm hands idled for months each year after the harvest has been gathered suffer",
     "seasonal unemployment", "structural unemployment",
     "cyclical unemployment", "frictional unemployment", "A",
     "The work calendar, not the economy, leaves them free."),
    (T_MON, "Easy", "Money that can be broken into small units for petty purchases has the quality of",
     "divisibility", "durability", "portability", "scarcity", "A",
     "The naira splits into kobo for small buys."),
    (T_MON, "Easy", "Money that is light and easy to carry about has the quality of",
     "portability", "divisibility", "stability of value", "acceptability", "A",
     "Heavy money would need a wheelbarrow."),
    (T_MON, "Hard", "A trader who agrees to pay for a tractor in instalments next year is using money as a",
     "standard of deferred payment", "measure of value",
     "store of wealth only", "medium of barter", "A",
     "The debt is sized in naira for a future date."),
    (T_MON, "Medium", "During a spell of unexpected inflation, the group that loses most is",
     "pensioners on fixed incomes", "traders who stock goods",
     "debtors who owe fixed sums", "farmers with produce to sell", "A",
     "The same pension buys less every month."),
    (T_MON, "Hard", "A cocoa farmer who borrowed at fixed interest before the inflation gains because",
     "he repays the loan in cheaper naira", "the bank cancels the interest",
     "his debt is doubled at once", "prices of loans always fall", "A",
     "The naira he returns buys less than the naira he took."),
    (T_NI, "Medium", "Summing all spending on final goods and services in a year measures national income by the",
     "expenditure method", "income method",
     "output method", "value-added method", "A",
     "Consumption, investment and government buying are added up."),
    (T_NI, "Hard", "A pension paid to a retired civil servant is left out of national income figures because it is a",
     "transfer payment", "factor income",
     "capital receipt", "consumer spending", "A",
     "No fresh output is created for the payment."),
    (T_NI, "Hard", "A country's GNP stands above its GDP whenever",
     "its net income from abroad is positive", "its borders are closed to trade",
     "its exports equal its imports", "its savings exceed investment", "A",
     "Earnings sent home by citizens abroad tip the balance."),
    (T_TOOL, "Easy", "A chart that shows each item's share of a total by slicing a circle is the",
     "pie chart", "bar chart", "line graph", "scatter diagram", "A",
     "Each slice is a share of the whole cake."),
    (T_TOOL, "Medium", "Studying a small part of a population in order to draw conclusions about the whole is called",
     "sampling", "a census", "enumeration", "tabulation", "A",
     "A well-chosen part speaks for the whole."),
    (T_PF, "Easy", "A government payment that keeps the price of an essential good low for buyers is a",
     "subsidy", "tariff", "levy", "fine", "A",
     "The treasury shoulders part of the price."),
    (T_PF, "Medium", "A government that spends beyond its revenue most commonly bridges the gap by",
     "borrowing from banks and the public", "raising workers' wages",
     "printing goods in factories", "sacking all taxpayers", "A",
     "Bonds and loans cover the shortfall."),
    (T_PF, "Hard", "A tax that swallows a larger share of a poor person's income than a rich person's is",
     "regressive", "progressive", "proportional", "a direct tax only", "A",
     "The poor feel the pinch more per naira."),
    (T_PF, "Medium", "A duty collected on goods manufactured within the country itself is",
     "excise duty", "customs duty", "import quota", "stamp duty", "A",
     "The brewer and the tobacco maker pay it at home."),
    (T_PF, "Easy", "When a government's revenue for the year exceeds its expenditure, the budget shows a",
     "surplus", "deficit", "balanced sheet", "shortfall", "A",
     "More flowed in than flowed out."),
    (T_PF, "Easy", "Government spending on new dams, bridges and school buildings is classified as",
     "capital expenditure", "recurrent expenditure",
     "transfer spending", "debt repayment", "A",
     "Durable assets, not running costs, are bought."),
    (T_IT, "Hard", "Selling goods abroad at prices below their cost of production at home is called",
     "dumping", "speculation", "arbitrage", "re-exporting", "A",
     "Foreign buyers get goods cheaper than home buyers."),
    (T_IT, "Medium", "Protecting newly established local industries until they grow strong enough to compete is the",
     "infant-industry argument", "dumping argument",
     "terms-of-trade argument", "self-reliance decrees", "A",
     "Nursery care for young factories."),
    (T_POP, "Medium", "Negotiations carried on between a trade union and the employers' body over wages and conditions are called",
     "collective bargaining", "price leadership",
     "consumer lobbying", "profit sharing", "A",
     "Both sides bargain as one for the whole shop floor."),
]

build_batch(
    S,
    "batch_171_neco_econ5.json",
    "171",
    "NECO Economics round 5 (R32 top-up): form utility; production "
    "complete at the consumer; consumer sovereignty; idle resources "
    "inside the PPC; income shift of demand; record harvest shifts "
    "supply right; income elasticity of normal goods positive; "
    "cartel; monopoly price control; debenture; public "
    "corporations; labour force; natural growth as births minus "
    "deaths; de facto census; cyclical unemployment; unemployment-"
    "rate formula; divisibility and portability; deferred payment; "
    "pensioners lose and debtors gain in inflation; expenditure "
    "method; transfer payments; GNP above GDP; pie chart; sampling; "
    "subsidy; proportional and regressive taxes; excise duty; "
    "budget surplus; capital expenditure; dumping; infant "
    "industry; collective bargaining. Scanned against NECO rounds "
    "1-4, WAEC Economics (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
