"""Batch 234 - NECO Economics round 5 (NECO top-up, R48).

Grows NECO Economics from 256 toward ~281 with angles verified
absent from the whole Economics pool (1,404 items across JAMB, WAEC
and NECO) and cleared against other subjects' pools (Commerce, Gov,
Geo, CA) for cross-subject twins. Dropped as cross-twins: merchant
bank, development bank, unit trust, primary/secondary market,
privatisation/commercialisation (all banked in Commerce/Gov), WTO
(banked in Geo and CA), corporation tax angle (econ company income
tax family). Fresh angles: tax incidence; Ricardian rent; piece vs
time rate; BoP deficit correction; inflation effects on creditors
and debtors; deficit financing; merit goods; free rider; fiat
money; Engel's law; repatriation of profits; petroleum profit tax;
trade diversion; counter trade; SDR; gilt-edged securities;
deregulation; strike; velocity of circulation; Gresham's law;
automatic stabiliser; motives for holding money; determinants of
savings; determinants of investment; capital gains tax.

    python3 scripts/build_neco_batch234.py -> content/batch_234_neco_econ5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Economics"

T_TAX = "Tax Structure and the Budget"
T_PUB = "Public Finance"
T_PROD = "Theory of Production"
T_LAB = "Labour and Wages"
T_TRADE = "International Trade"
T_PAY = "Trade and Payments"
T_FIN = "Financial Institutions"
T_MON = "Money and Inflation"
T_CONS = "Theory of Consumer Behaviour"
T_MKT = "Markets and Prices"
T_FAIL = "Market Failure"
T_NAT = "Measuring National Income"
T_DEV = "Money, Prices and Jobs"
T_FIRM = "Production and Firms"

PASSAGES = []
PQ = []

Q = [
    (T_TAX, "Medium", "The final resting place of a tax — who really bears its burden after it has been passed on through higher prices or lower wages — is called",
     "the incidence of the tax", "the licence of the tax",
     "the tariff code", "the yield of the tax", "A",
     "The law may levy it on one man; the market can shift it."),
    (T_PROD, "Hard", "David Ricardo explained that rent on land arises mainly because",
     "land differs in fertility and superior land is scarce", "farmers are too poor to buy land",
     "governments force tenants to pay rent", "all land is exactly equally fertile", "A",
     "The best plots are limited, so their surplus becomes rent."),
    (T_LAB, "Medium", "A worker who is paid a fixed sum for each unit he produces, rather than a fixed sum for each day worked, is paid by",
     "piece rate", "time rate",
     "share rate", "scale rate", "A",
     "The tally of finished goods settles the pay."),
    (T_PAY, "Hard", "A country that persistently spends more on imports than it earns from exports may correct the deficit by",
     "devaluing the currency and cutting imports", "raising all import quotas to record levels",
     "banning exports of all its cash crops", "printing much more domestic currency", "A",
     "Cheaper exports and dearer imports begin to right the scales."),
    (T_LAB, "Hard", "At very high wage levels, some workers choose to enjoy more leisure and offer fewer hours of work. Their supply curve of labour therefore",
     "bends backwards", "slopes downward forever",
     "becomes vertical only", "disappears entirely", "A",
     "Beyond a point, richer workers buy rest, not more work."),
    (T_PUB, "Hard", "A situation in which government deliberately spends more than its revenue and bridges the gap by borrowing is called",
     "deficit financing", "deficit budgeting only",
     "surplus financing", "zero-based budgeting", "A",
     "The gap is filled with borrowed money, not taxation."),
    (T_FAIL, "Hard", "Goods such as education and vaccination, which bring benefits to the whole society and are therefore provided or supported by government, are called",
     "merit goods", "mixed goods",
     "composite goods", "counter goods", "A",
     "Left alone, people would buy too little of them."),
    (T_FAIL, "Medium", "A herdsman who grazes his cattle on a village common field free of charge, leaving the field overgrazed for everyone, illustrates the problem of the",
     "free rider", "free market",
     "foreign exchange", "fixed cost", "A",
     "He enjoys the gain; the village bears the cost."),
    (T_MON, "Easy", "Money that has little or no intrinsic value of its own but is accepted as money because the government declares it legal tender is called",
     "fiat money", "commodity money",
     "token barter", "near money", "A",
     "Its worth rests on the law, not on the paper."),
    (T_CONS, "Hard", "Engel's law states that as a household's income rises,",
     "the proportion spent on food falls", "the proportion spent on food rises",
     "all spending falls", "savings disappear", "A",
     "Richer families still eat — but food takes a smaller slice."),
    (T_TRADE, "Medium", "The profits of a foreign-owned oil company that are sent out of Nigeria to its shareholders abroad represent",
     "repatriation of profits", "reinvested earnings",
     "inward remittances", "invisible imports", "A",
     "The earnings earned here travel home abroad."),
    (T_TAX, "Medium", "The special tax levied on the profits of companies engaged in petroleum operations in Nigeria is",
     "petroleum profit tax", "value added tax",
     "personal income tax", "capital gains tax", "A",
     "The oil wells pay a tax of their own name."),
    (T_TRADE, "Hard", "When a customs union diverts a member's purchases from a cheaper outside producer to a dearer partner inside the union, the loss suffered is called",
     "trade diversion", "trade creation",
     "trade liberalisation", "trade balancing", "A",
     "The tariff wall turns trade to a costlier door."),
    (T_TRADE, "Medium", "A direct exchange of Nigeria's crude oil for another country's machinery, without any currency passing between them, is an example of",
     "counter trade", "invisible trade",
     "entrepôt trade", "free trade", "A",
     "Goods swap for goods across the border."),
    (T_FIN, "Medium", "Special Drawing Rights, the international reserve asset created by the International Monetary Fund to supplement members' reserves, are commonly known as",
     "SDRs", "SWIFTs",
     "SDRs bonds", "SEGAs", "A",
     "The Fund's basket lends strength to reserves."),
    (T_FIN, "Medium", "Government securities, such as treasury bonds, are regarded as very safe investments because the government cannot easily fail to pay; they are therefore described as",
     "gilt-edged securities", "blue-water stocks",
     "red-tape shares", "grey-market bonds", "A",
     "As safe as the state's own promise to pay."),
    (T_MKT, "Medium", "The removal of government controls over the prices and operations of an industry, such as the downstream petrol sector, is called",
     "deregulation", "devaluation",
     "denationalisation", "delimitation", "A",
     "The controls are lifted; the market takes the wheel."),
    (T_LAB, "Easy", "A concerted refusal by workers to do their work until their demands are met is called",
     "a strike", "a sit-in allowance",
     "a lockout", "a retrenchment", "A",
     "The tools lie quiet until the grievance is heard."),
    (T_MON, "Hard", "The average number of times a unit of money changes hands in paying for goods and services within a period is the",
     "velocity of circulation", "volume of trade",
     "value of money", "velocity of inflation", "A",
     "One naira may pay five bills in one market day."),
    (T_MON, "Hard", "Gresham's law states that when two forms of money circulate together,",
     "bad money drives good money out of circulation", "good money drives bad money out",
     "both forms circulate equally for ever", "paper always replaces metal", "A",
     "People hoard the better coins and spend the worse."),
    (T_TAX, "Medium", "A feature of the tax system that automatically softens a boom and cushions a recession without any new law — as progressive tax receipts rise and fall with incomes — is called",
     "an automatic stabiliser", "a fiscal drag rule",
     "a tariff lever", "a monetary anchor", "A",
     "The tax code steadies the economy by itself."),
    (T_MON, "Hard", "Keynes grouped the reasons why people hold money into the transactions motive, the precautionary motive and the",
     "speculative motive", "sacrificial motive",
     "subsistence motive", "seigniorage motive", "A",
     "Some cash is kept waiting for a chance to buy cheap."),
    (T_DEV, "Medium", "The level of savings in an economy is chiefly determined by",
     "the level of income and the rate of interest", "the colour of the printed currency notes",
     "the number of commercial bank branches alone", "the size of the country's civil service", "A",
     "People save from what is left after spending."),
    (T_FIRM, "Medium", "The main determinants of investment in an economy are",
     "the expected profit and the rate of interest", "the price of garri and yam",
     "the number of commercial banks alone", "the size of the civil service", "A",
     "Money moves where the return beats the interest."),
    (T_TAX, "Medium", "The tax charged on the profit a person makes when he sells an asset such as land or shares is",
     "capital gains tax", "capital transfer levy",
     "company income tax", "customs excise", "A",
     "The gain on the sale itself is what is taxed."),
]

build_batch(
    S,
    "batch_234_neco_econ5.json",
    "234",
    "NECO Economics round 5 (R48 top-up): tax incidence; Ricardian "
    "rent; piece rate; BoP deficit correction; inflation and "
    "creditors; deficit financing; merit goods; free rider; fiat "
    "money; Engel's law; repatriation of profits; petroleum profit "
    "tax; trade diversion; counter trade; SDR; gilt-edged; "
    "deregulation; strike; velocity of circulation; Gresham's law; "
    "automatic stabiliser; motives for holding money; determinants "
    "of savings; determinants of investment; capital gains tax. "
    "Scanned against the whole Economics pool (JAMB, WAEC and NECO "
    "stems) and cleared of cross-subject twins (Commerce/Gov/Geo/CA).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
