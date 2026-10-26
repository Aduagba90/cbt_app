"""Batch 203 - NECO Economics round 7 (NECO top-up, R40).

Grows NECO Economics from 231 toward ~256 with angles not yet in
the bank: barter; the double coincidence of wants; money defined;
deflation; demand defined; supply defined; the central bank as
lender of last resort; sole issuer of currency; banker to
government; commercial banks accepting deposits; direct and
indirect taxes; public debt; GDP defined; the standard of living;
mobility of labour; the trade union; structural and frictional
unemployment; the balance of payments; the balance of trade;
tariffs; quotas; wages as the reward for labour. Scanned against
the whole Economics pool (WAEC, NECO and JAMB stems, 1,362 items).

    python3 scripts/build_neco_batch203.py -> content/batch_203_neco_econ7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Economics"

T_MON = "Money and Exchange"
T_CEN = "Financial Institutions"
T_PUB = "Public Finance"
T_CON = "Basic Economic Concepts"
T_LAB = "Labour and Factor Rewards"
T_POP = "Population and Labour Force"
T_INT = "International Trade"

PASSAGES = []
PQ = []

Q = [
    (T_MON, "Easy", "The direct exchange of goods for goods without the use of money is called",
     "barter", "haggling",
     "trade by bar", "hoarding", "A",
     "A bag of rice changes hands for a goat."),
    (T_MON, "Hard", "A farmer who wants cloth must find a weaver who wants yams. This difficulty of barter is known as the",
     "double coincidence of wants", "problem of indivisibility",
     "lack of store of value", "difficulty of valuation", "A",
     "Both sides must want exactly what the other holds."),
    (T_MON, "Medium", "Economists define money as anything that",
     "is generally accepted in exchange", "is printed by a government",
     "can be stored in a bank vault", "is made of paper or metal", "A",
     "Cowries once served; naira notes serve today."),
    (T_MON, "Medium", "A sustained fall in the general price level of goods and services is called",
     "deflation", "inflation",
     "stagflation", "reflation", "A",
     "Money slowly buys more and more."),
    (T_CON, "Medium", "The quantity of a good that consumers are willing and able to buy at a given price over a period of time is called",
     "demand", "supply",
     "equilibrium", "consumption", "A",
     "Willing hands must also be able to pay."),
    (T_CON, "Medium", "The quantity of a good that sellers are willing and able to offer for sale at a given price over a period of time is the",
     "supply", "demand schedule",
     "surplus stock", "market size", "A",
     "At higher prices more sellers step forward."),
    (T_CEN, "Medium", "The Central Bank of Nigeria is described as the lender of last resort because it",
     "lends to banks in distress", "gives loans to every citizen",
     "lends money at zero interest", "refuses to lend to government", "A",
     "When all doors close, the banker of banks opens."),
    (T_CEN, "Easy", "In Nigeria, currency notes and coins are issued solely by the",
     "Central Bank", "Ministry of Finance",
     "commercial banks", "Nigerian Security Printing and Minting Company", "A",
     "No other hand may print the naira."),
    (T_CEN, "Medium", "The Central Bank keeps the accounts of the federal government and its ministries as their",
     "banker", "auditor",
     "tax collector", "debtor", "A",
     "Government salaries pass through its books."),
    (T_CEN, "Easy", "The primary function of a commercial bank is to",
     "accept deposits from customers", "print legal tender notes",
     "fix the national budget", "licence stockbrokers", "A",
     "Every other service grows from the vault."),
    (T_PUB, "Medium", "A tax levied directly on the income or property of individuals and firms, such as income tax, is a",
     "direct tax", "indirect tax",
     "value added tax", "customs duty", "A",
     "The payer cannot shift it to another."),
    (T_PUB, "Medium", "A tax charged on goods and services, such as import duty, which the seller passes on to the final consumer is",
     "an indirect tax", "a direct tax",
     "a capital levy", "a poll tax", "A",
     "The buyer pays it inside the price."),
    (T_PUB, "Medium", "The total amount of money that a government owes to lenders within and outside the country is its",
     "public debt", "budget deficit",
     "capital expenditure", "treasury bill", "A",
     "Every unpaid borrowing is added to the pile."),
    (T_CON, "Medium", "The total value of goods and services produced by the citizens of a country both at home and abroad in a year is its",
     "gross national product", "gross domestic product",
     "net domestic income", "per capita income", "A",
     "Citizens count everywhere, borders apart."),
    (T_CON, "Medium", "The level of material comfort and welfare enjoyed by the people of a country is referred to as their",
     "standard of living", "cost of living index",
     "money income", "gross output", "A",
     "It counts health, schooling and comfort, not just cash."),
    (T_LAB, "Medium", "The ease with which a worker can move from one job or place to another is called",
     "mobility of labour", "productivity of labour",
     "division of labour", "specialisation", "A",
     "A mobile worker follows the work."),
    (T_LAB, "Medium", "An organisation of workers formed to protect and promote the interests of its members at work is a",
     "trade union", "chamber of commerce",
     "employers' association", "consumers' cooperative", "A",
     "The workers speak with one voice."),
    (T_LAB, "Medium", "The reward paid to labour for its part in production is",
     "wages and salaries", "rent",
     "interest", "profit", "A",
     "The worker's pay packet is labour's reward."),
    (T_LAB, "Easy", "When computers displaced the typing pool, typists who could not find new work became",
     "structurally unemployed", "frictionally unemployed",
     "seasonally unemployed", "cyclically unemployed", "A",
     "The structure of the economy moved on."),
    (T_LAB, "Easy", "The short-term unemployment of workers who are between jobs, moving from one to another, is called",
     "frictional unemployment", "structural unemployment",
     "residual unemployment", "disguised unemployment", "A",
     "The gap between two jobs is only friction."),
    (T_POP, "Medium", "The estimated proportion of the working population that is available for employment at any time is the",
     "labour force", "dependent population",
     "mobility ratio", "participation rate only", "A",
     "It counts those able and seeking work."),
    (T_INT, "Medium", "A systematic record of all the economic transactions between one country and the rest of the world in a year is its",
     "balance of payments", "balance of trade",
     "national budget", "trade terms", "A",
     "Every payment in and out is entered."),
    (T_INT, "Medium", "In preparing the national accounts, an economist compares goods exported with goods imported and leaves services out. The statement he prepares is the",
     "balance of trade", "balance of payments",
     "terms of trade", "trade surplus account", "A",
     "Goods alone are counted, services apart."),
    (T_INT, "Medium", "A tax placed on imported goods mainly to raise their price and protect local producers is a",
     "tariff", "quota",
     "subsidy", "trade rebate", "A",
     "The customs gate makes imports dearer."),
    (T_INT, "Medium", "A physical limit placed on the quantity of a good that may be imported into a country in a period is a",
     "quota", "tariff",
     "embargo tax", "exchange control", "A",
     "Beyond the number, the port closes."),
]

build_batch(
    S,
    "batch_203_neco_econ7.json",
    "203",
    "NECO Economics round 7 (R40 top-up): barter; double "
    "coincidence of wants; money defined; deflation; demand and "
    "supply defined; the central bank as lender of last resort, "
    "sole issuer and government's banker; commercial banks' "
    "deposit-taking; direct and indirect taxes; public debt; GDP "
    "defined; standard of living; mobility of labour; the trade "
    "union; wages as labour's reward; structural and frictional "
    "unemployment; the labour force; balance of payments; balance "
    "of trade; tariff; quota. Scanned against the whole Economics "
    "pool (WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
