"""Batch 177 - WAEC Economics round 6 (WAEC top-up, R33).

Grows WAEC Economics from 220 toward ~254 with angles not yet in
the bank: the histogram's touching bars; the median of four
values; a taste shift leftward; the ceteris paribus discipline;
the elasticity of supply; land's vertical supply; the break-even
point; farming as the biggest occupation; positive net migration;
near money; the incidence of a tax; a fine is not a tax; what per
capita income hides; current against capital account; a stronger
naira cheapening imports; the customs union's common tariff; the
vicious circle of poverty; capital flight; diversification; the
indigenisation decrees; the real wage; movement along the supply
curve; the informal sector; population density; vital
registration; globalisation; the multinational; a trade surplus;
crowding out; the circular flow; leakages; the multiplier; the
business cycle; the recession. Scanned against WAEC rounds 1-5,
NECO Economics (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch177.py -> content/batch_177_waec_econ6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Economics"

T_TOOL = "Tools of Economic Analysis"
T_DS = "Demand and Supply"
T_BEC = "Basic Economic Concepts"
T_TP = "Theory of Production"
T_POP = "Population and Labour"
T_MI = "Money and Inflation"
T_PF = "Public Finance"
T_MNI = "Measuring National Income"
T_IT = "International Trade"
T_DEV = "Economic Development and Planning"
T_MP = "Markets and Prices"
T_FI = "Financial Institutions"
T_PFIRM = "Production and Firms"
T_TD = "Trade and Development"
T_LW = "Labour and Wages"

PASSAGES = []
PQ = []

Q = [
    (T_TOOL, "Medium", "Unlike a bar chart, a histogram draws its bars touching one another because the data it displays are",
     "grouped into continuous class intervals", "always whole numbers",
     "counted in single years", "drawn from two different sources", "A",
     "Classes run into each other along a continuous scale."),
    (T_TOOL, "Medium", "When a distribution of incomes contains a few extremely large values, the average that best represents the typical earner is the",
     "median", "mean",
     "range", "total", "A",
     "Extreme values drag the mean but leave the median unmoved."),
    (T_DS, "Medium", "A radio campaign persuades many smokers to quit. Other things equal, the campaign will",
     "shift the demand for cigarettes to the left", "shift the demand for cigarettes to the right",
     "move sellers along their supply curve only", "raise the equilibrium price of cigarettes", "A",
     "Tastes turned against the product."),
    (T_BEC, "Hard", "The ceteris paribus assumption is useful to economists because it allows them to",
     "study one factor at a time while holding others constant", "prove that prices never change",
     "ignore human behaviour altogether", "predict the future with total certainty", "A",
     "Isolate a single cause in a busy world."),
    (T_DS, "Medium", "The only factor that moves a seller along his existing supply curve is a change in the",
     "good's own price", "cost of its raw materials",
     "number of rival sellers", "sellers' expectations of profit", "A",
     "The curve itself shifts only when other forces act."),
    (T_DS, "Medium", "The elasticity of supply measures how the quantity supplied responds to a change in the",
     "price of the good", "incomes of buyers",
     "taxes on consumers", "population's size", "A",
     "Sensitivity of sellers to price is its whole concern."),
    (T_DS, "Hard", "Because the total quantity of land in a country cannot increase, the supply curve of land is",
     "perfectly inelastic, a vertical line", "perfectly elastic, a horizontal line",
     "upward sloping and gentle", "downward sloping always", "A",
     "No price conjures more land into existence."),
    (T_MP, "Hard", "The level of output at which a firm's total revenue just covers all its costs is its",
     "break-even point", "profit-maximising point",
     "shut-down point", "point of diminishing returns", "A",
     "Below it every extra sale deepens the loss."),
    (T_POP, "Easy", "The largest single occupation of Nigeria's labour force today is",
     "farming", "banking",
     "oil drilling", "telecommunications", "A",
     "Most workers still earn their living from the soil."),
    (T_POP, "Medium", "When the number of immigrants into a country exceeds the number of emigrants leaving it, the country's net migration is",
     "positive", "negative",
     "zero every year", "equal to the birth rate", "A",
     "Arrivals outweigh departures."),
    (T_POP, "Medium", "Dividing a country's population by its land area in square kilometres gives the",
     "population density", "growth rate",
     "dependency ratio", "labour force", "A",
     "It shows how thickly people settle the land."),
    (T_POP, "Hard", "The continuous official recording of births, deaths and marriages in a country is known as",
     "vital registration", "a sample survey",
     "a de facto census", "panel enumeration", "A",
     "Registrars log each event as it occurs."),
    (T_MI, "Hard", "Treasury bills and savings deposits are called near money because they",
     "convert quickly into cash without losing value", "are printed beside the legal naira notes",
     "carry the portraits of past leaders", "cannot be spent at all", "A",
     "One short step stands between them and cash."),
    (T_LW, "Easy", "A worker's real wage is best expressed as the quantity of",
     "goods and services his wage can buy", "naira notes he takes home",
     "hours he works each week", "taxes deducted from his pay", "A",
     "What matters is what the money fetches."),
    (T_PF, "Hard", "A tax legally levied on a seller but finally borne mostly by consumers illustrates the tax's",
     "incidence", "base",
     "rate", "yield", "A",
     "The burden settles where it finally rests."),
    (T_PF, "Medium", "A court fine differs from a tax because a fine is",
     "a penalty for wrongdoing, not a regular levy", "paid only by registered companies",
     "always refunded after one year", "charged only on incomes above a limit", "A",
     "Taxes fund government; fines punish offenders."),
    (T_MNI, "Medium", "Two countries with equal per capita incomes may differ greatly because per capita income hides",
     "how unevenly the income is shared", "the size of their armed forces",
     "their national anthems", "the colour of their currencies", "A",
     "An average can mask a wide gulf between rich and poor."),
    (T_MNI, "Hard", "A nation's balance of payments account is broadly divided into the current account and the",
     "capital account", "fiscal account",
     "consolidated revenue account", "petty cash account", "A",
     "Trade flows in one; investment flows in the other."),
    (T_IT, "Medium", "When the naira strengthens against the dollar, goods imported from America become for Nigerian buyers",
     "cheaper", "dearer",
     "unobtainable", "tax-free", "A",
     "Fewer naira now settle each dollar invoice."),
    (T_IT, "Hard", "A customs union goes beyond a free trade area by adopting",
     "a common external tariff on outsiders", "one parliament for all members",
     "a single currency at once", "uniform school curricula", "A",
     "Members tax the world outside at the same rate."),
    (T_IT, "Medium", "When a country's exports exceed its imports over a trading year, it records a trade",
     "surplus", "deficit",
     "balance of zero always", "quota", "A",
     "Sales abroad outran purchases from abroad."),
    (T_DEV, "Hard", "An economy whose poverty keeps savings low, which keeps investment low, which keeps income low, is trapped in the",
     "vicious circle of poverty", "multiplier process",
     "law of comparative advantage", "circular flow of income", "A",
     "Poverty reproduces itself round the loop."),
    (T_DEV, "Medium", "Wealthy Nigerians moving their money permanently into foreign banks drain the economy through",
     "capital flight", "capital formation",
     "technology transfer", "trade liberalisation", "A",
     "The savings the economy needs sail away."),
    (T_DEV, "Medium", "The surest long-run guard against sudden crashes in the world oil price is",
     "diversifying the export base", "printing more naira notes",
     "raising import duties alone", "reducing school enrolment", "A",
     "Many products steady the national income."),
    (T_DEV, "Hard", "The indigenisation decrees of the 1970s sought chiefly to",
     "transfer ownership of businesses into Nigerian hands", "invite more foreign firms into retail trade",
     "nationalise every foreign oil company", "reduce the number of Nigerian merchants", "A",
     "Nigerians were moved up the ladder of ownership."),
    (T_TD, "Medium", "The growing integration of the world's economies through trade, investment and technology is called",
     "globalisation", "localisation",
     "nationalisation", "collectivisation", "A",
     "Distant markets now meet in one marketplace."),
    (T_TD, "Medium", "A company with its head office in Lagos and factories in Ghana, Kenya and South Africa is a",
     "multinational corporation", "public corporation",
     "co-operative society", "partnership firm", "A",
     "It produces across many national borders."),
    (T_PF, "Hard", "Heavy government borrowing that pushes up interest rates and squeezes out private investment is called",
     "crowding out", "pump priming",
     "open market operation", "discounting", "A",
     "The treasury's appetite starves private borrowers."),
    (T_MNI, "Medium", "The continuous movement of spending and income between households and firms is the",
     "circular flow of income", "balance of payments",
     "propensity to consume", "terms of trade", "A",
     "One man's spending is another man's income."),
    (T_MNI, "Hard", "Within the circular flow, savings, taxes and spending on imports act as",
     "leakages from the flow", "injections into the flow",
     "multipliers of the flow", "subsidies on the flow", "A",
     "They drain money out of the stream."),
    (T_MNI, "Hard", "A small rise in investment that sets off a larger rise in national income works through the",
     "multiplier", "accelerator limit",
     "paradox of thrift", "quantity theory", "A",
     "Each round of spending breeds the next."),
    (T_DEV, "Medium", "The recurring swings of boom and slump in a nation's economic activity are together called the",
     "business cycle", "budget cycle",
     "vital registration", "circular flow", "A",
     "Prosperity and contraction take turns."),
    (T_DEV, "Medium", "A period in which real output falls and unemployment rises for two successive quarters is a",
     "recession", "recovery",
     "peak of the cycle", "inflationary gap", "A",
     "Six months of shrinking output sound its bell."),
    (T_PFIRM, "Medium", "Artisans, hawkers and home workshops that operate without formal registration make up the",
     "informal sector", "public sector",
     "money market", "joint sector", "A",
     "Their bustle never appears on any official licence."),
]

build_batch(
    S,
    "batch_177_waec_econ6.json",
    "177",
    "WAEC Economics round 6 (R33 top-up): histogram bars touching "
    "and the median of four values; taste shifting demand; ceteris "
    "paribus; the good's own price moving along supply; elasticity "
    "of supply; land's vertical supply; the break-even point; "
    "farming as Nigeria's biggest occupation; positive net "
    "migration; population density; vital registration; near "
    "money; real wage; tax incidence; a fine is no tax; per capita "
    "income hiding inequality; current against capital account; a "
    "stronger naira cheapening imports; the customs union's common "
    "tariff; trade surplus; the vicious circle; capital flight; "
    "diversification; the indigenisation decrees; globalisation; "
    "the multinational; crowding out; the circular flow; leakages; "
    "the multiplier; the business cycle; the recession; the "
    "informal sector. Scanned against WAEC rounds 1-5, NECO "
    "Economics (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
