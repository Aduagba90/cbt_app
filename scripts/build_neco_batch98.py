"""Batch 098 - WAEC Commerce round 2 (WAEC lift, Round 19).

WAEC Commerce Paper 1 draws 50 items; the bank stood at 63. This lift adds
fresh items - barter's limits, money's functions, division of labour,
quotation, tender, delivery note, transport choice and containerisation,
insurance brokerage and marine cover, merchant and microfinance banks,
bulls and bears, market tiers, partnership deed, private vs public
company, CAC, privatisation, consumer rights, chambers, persuasive and
false advertising, BOP, dumping, quotas, auctions, hire purchase - scanned
against WAEC r1, NECO rounds 1-2 and the JAMB Commerce banks.

    python3 scripts/build_neco_batch98.py -> content/batch_098_waec_commerce2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_TRADE = "Trade and Money"
T_DOC = "Trade Documents"
T_AID = "Aids to Trade"
T_BANK = "Banking and Finance"
T_CAP = "Capital Markets"
T_UNIT = "Business Units and Regulation"
T_CONS = "The Consumer"
T_ADV = "Advertising"
T_INT = "International Trade"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- trade and money
    (T_TRADE, "Hard", "The barter system's need for a 'double coincidence of wants' means the trader must",
     "find a wants-matching partner", "exchange goods in pairs of two only", "pay double the price each time", "swear an oath twice before trading", "A",
     "Both sides must match exactly."),
    (T_TRADE, "Easy", "Money serving as a 'medium of exchange' means it",
     "settles payments for goods", "measures prices only", "stores wealth only", "adorned kings' crowns", "A",
     "Goods change hands for money."),
    (T_TRADE, "Medium", "Keeping money for future use without loss of value makes money a",
     "store of value", "measure of value", "medium of exchange", "standard of deferred payment", "A",
     "Value waits inside money."),
    (T_TRADE, "Medium", "The production process where each worker repeats one task is",
     "division of labour", "specialisation of markets", "mechanisation", "rationalisation", "A",
     "One task per worker speeds output."),
    (T_TRADE, "Medium", "A worker who performs only one operation all day tends to",
     "become faster at that operation", "master every trade equally", "produce less each week", "lose interest in wages", "A",
     "Repetition breeds speed and skill."),
    # ---------------------------------------------------------------- documents
    (T_DOC, "Easy", "The statement a seller sends showing prices of goods offered, without a sale yet, is a",
     "quotation", "receipt", "statement of account", "credit note", "A",
     "It quotes before any dealing."),
    (T_DOC, "Hard", "Sealed bids submitted by firms competing to execute a contract are called",
     "tenders", "treaties", "quotations", "proformas", "A",
     "The best tender wins the job."),
    (T_DOC, "Medium", "The paper that accompanies delivered goods and lists what has been handed over is the",
     "delivery note", "bill of lading", "invoice", "way bill", "A",
     "The buyer checks against it."),
    # ---------------------------------------------------------------- aids to trade
    (T_AID, "Medium", "The cheapest means of carrying very heavy, bulky cargo across an ocean is",
     "sea freight", "air freight", "road haulage", "pipeline", "A",
     "Ships swallow weight cheaply."),
    (T_AID, "Medium", "Air transport is chosen for fresh flowers and vaccines mainly because of",
     "speed", "cost", "capacity", "weather", "A",
     "Perishables race the clock."),
    (T_AID, "Hard", "Carrying goods in sealed standard-sized metal boxes that move from ship to truck is",
     "containerisation", "palletisation", "consolidation", "chartering", "A",
     "One box rides every mode."),
    (T_AID, "Medium", "The main factor a farmer considers when choosing how to send his produce to market is",
     "the nature of the goods", "the colour of the truck", "the driver's hometown", "the day of the week", "A",
     "Perishability picks the mode."),
    # ---------------------------------------------------------------- banking and finance
    (T_BANK, "Hard", "Who shops across many insurers to find the best cover for a client?",
     "the insurance broker", "the insurance agent", "the loss adjuster", "the actuary", "A",
     "The broker shops for the buyer."),
    (T_BANK, "Hard", "The oldest branch of insurance, born with sea trade, is",
     "marine insurance", "life assurance", "motor insurance", "fire insurance", "A",
     "Ships and cargo came first."),
    (T_BANK, "Medium", "The reward an insurer gives a careful driver who makes no claim is the",
     "no-claim bonus", "loyalty dividend", "premium refund", "third-party rebate", "A",
     "Carelessness costs the bonus."),
    (T_BANK, "Medium", "Insurance that protects an employer against staff dishonesty is",
     "fidelity guarantee", "employer's liability", "burglary cover", "consequential loss", "A",
     "It backs up trusted hands."),
    (T_BANK, "Medium", "Merchant banks in Nigeria serve mainly",
     "corporate clients and big deals", "market women and artisans", "school children saving coins", "village cooperatives only", "A",
     "Wholesale banking is their trade."),
    (T_BANK, "Easy", "Microfinance banks exist chiefly to give",
     "small loans to low-income earners", "billion-naira syndicated loans", "car loans to banks' directors", "loans to foreign firms", "A",
     "Little loans lift small trades."),
    (T_BANK, "Hard", "The core idea that makes insurance work is the",
     "pooling of many risks", "certainty of every loss", "profit on every claim", "luck of the insurer", "A",
     "Many carry the burden of one."),
    # ---------------------------------------------------------------- capital markets
    (T_CAP, "Hard", "In stock exchange language, a 'bull' is an investor who",
     "expects prices to rise and buys", "expects prices to fall and sells", "has stopped trading", "trades only in gold", "A",
     "The bull tosses prices up."),
    (T_CAP, "Hard", "An investor called a 'bear' expects prices to",
     "fall", "rise", "double", "stay fixed", "A",
     "The bear drags them down."),
    (T_CAP, "Medium", "The market where companies issue brand-new shares to the public is the",
     "primary market", "secondary market", "money market", "commodity market", "A",
     "New money is raised there."),
    (T_CAP, "Medium", "The market where existing shares change hands between investors is the",
     "secondary market", "primary market", "foreign exchange", "bond desk only", "A",
     "Old shares find new owners."),
    # ---------------------------------------------------------------- business units and regulation
    (T_UNIT, "Medium", "The written agreement among partners on profit sharing and duties is the",
     "partnership deed", "prospectus", "memorandum", "articles", "A",
     "The deed governs the house."),
    (T_UNIT, "Medium", "Under Nigerian law, a private limited company may have between 2 and",
     "50 members", "20 members", "100 members", "500 members", "A",
     "Fifty members is the ceiling."),
    (T_UNIT, "Medium", "A public limited company is identified in its name by the letters",
     "PLC", "PVC", "LLC", "PTY", "A",
     "The suffix announces the status."),
    (T_UNIT, "Easy", "Business names and companies are registered in Nigeria by the",
     "Corporate Affairs Commission", "Standards Organisation", "Central Bank", "Stock Exchange", "A",
     "The CAC keeps the register."),
    (T_UNIT, "Hard", "Selling a government-owned company entirely to private owners is",
     "privatisation", "commercialisation", "nationalisation", "liquidation", "A",
     "The state hands over fully."),
    # ---------------------------------------------------------------- the consumer
    (T_CONS, "Medium", "A buyer's right to know the true price, weight and contents of a product is the right to",
     "information", "safety", "redress", "choice", "A",
     "Labels must tell the truth."),
    (T_CONS, "Medium", "The right that lets a shopper pick among competing brands is the right to",
     "choose", "protest", "credit", "silence", "A",
     "Shelves must offer options."),
    (T_CONS, "Medium", "An association of traders formed to promote business interests in a city is the",
     "chamber of commerce", "trade tribunal", "clearing port", "labour congress", "A",
     "The chamber speaks for trade."),
    # ---------------------------------------------------------------- advertising
    (T_ADV, "Medium", "Advertising that appeals to feelings and lifestyle rather than facts is",
     "persuasive advertising", "informative advertising", "classified advertising", "legal advertising", "A",
     "Emotion moves the buyer's hand."),
    (T_ADV, "Hard", "An advert that falsely claims a drug cures all diseases commits",
     "false advertising", "reminder advertising", "prestige advertising", "corporate advertising", "A",
     "The law frowns at the lie."),
    # ---------------------------------------------------------------- international trade
    (T_INT, "Hard", "The complete record of a country's goods, services and capital dealings with the world is the",
     "balance of payments", "balance of trade", "terms of trade", "trade cycle", "A",
     "Everything crosses into it."),
    (T_INT, "Hard", "Selling goods abroad at prices below their home cost to capture a market is",
     "dumping", "re-exporting", "bartering", "arbitraging", "A",
     "The practice floods the target."),
    (T_INT, "Medium", "A government limit on the quantity of a good that may be imported is a",
     "quota", "tariff", "subsidy", "embargo", "A",
     "A number caps the inflow."),
    (T_INT, "Medium", "Goods sold publicly to the highest bidder are disposed of by",
     "auction", "tender", "raffle", "barter", "A",
     "The hammer falls on the bid."),
    (T_INT, "Medium", "Kelechi pays for a fridge in monthly installments under hire purchase. It legally becomes his",
     "after the final installment", "on the first payment", "before any payment", "never at all", "A",
     "Hire first, own at the end."),
]

build_batch(
    S,
    "batch_098_waec_commerce2.json",
    "098",
    "WAEC Commerce round 2 (Round 19 lift): double coincidence, money as "
    "medium and store, division of labour, quotation, tender, delivery "
    "note, sea freight, air speed, containerisation, choice by goods' "
    "nature, broker vs agent, marine insurance oldest, no-claim bonus, "
    "fidelity guarantee, merchant banks, microfinance, risk pooling, bull, "
    "bear, primary and secondary markets, partnership deed, private 2-50, "
    "PLC, CAC, privatisation, consumer rights (information, choice), "
    "chamber of commerce, persuasive and false advertising, balance of "
    "payments, dumping, quota, auction, hire purchase ownership. Scanned "
    "against WAEC r1, NECO rounds 1-2 and the JAMB Commerce banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
