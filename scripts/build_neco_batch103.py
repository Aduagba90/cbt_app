"""Batch 103 - WAEC Commerce round 3 (WAEC top-up, Round 21).

Lifts WAEC Commerce from 101 toward ~145 with angles not yet in the
bank: home vs foreign trade, invisible trade and balance of payments,
trade restrictions and tariffs, bonded warehouses and free ports,
entrepreneurship and business plans, equity vs debt capital, business
risk and insurance types, the stock exchange and its securities,
business combinations, trade associations and chambers, consumer
protection agencies, business communication and e-commerce. Scanned
against WAEC rounds 1-2, NECO Commerce and the JAMB pool.

    python3 scripts/build_neco_batch103.py -> content/batch_103_waec_commerce3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_TRADE = "Trade: Home, Foreign and World"
T_ENT = "Business Units and Entrepreneurship"
T_FIN = "Business Finance and Capital"
T_INS = "Insurance"
T_MKT = "Financial Markets and Combinations"
T_BIZ = "Business Environment and Communication"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- trade
    (T_TRADE, "Easy", "Trade carried on within a country's borders is",
     "home trade", "foreign trade", "entrepot trade", "barter trade", "A",
     "It stays inside the nation."),
    (T_TRADE, "Easy", "Buying goods from abroad for local use is",
     "import trade", "export trade", "entrepot trade", "coastal trade", "A",
     "The goods come in from outside."),
    (T_TRADE, "Medium", "Re-exporting imported goods without altering them is",
     "entrepot trade", "bilateral trade", "counter trade", "visible trade", "A",
     "The warehouse nation resells them."),
    (T_TRADE, "Medium", "Services traded across borders, like banking and tourism, are",
     "invisible trade", "visible trade", "barter trade", "entrepot trade", "A",
     "No goods cross, only services."),
    (T_TRADE, "Hard", "A country's visible trade gap is measured by its",
     "balance of trade", "balance of payments", "budget surplus", "trade cycle", "A",
     "Goods only are counted here."),
    (T_TRADE, "Hard", "The record of all economic dealings between a country and the rest of the world is the",
     "balance of payments", "balance of trade", "national budget", "trade terms", "A",
     "Every transaction is captured."),
    (T_TRADE, "Medium", "A tax charged on imported goods is a",
     "customs duty", "sales tax", "capital levy", "stamp duty", "A",
     "Customs collects it at the port."),
    (T_TRADE, "Hard", "A total ban on importing a particular good is",
     "an embargo", "a tariff", "a quota", "a subsidy", "A",
     "Nothing of that good may enter."),
    (T_TRADE, "Hard", "Restricting imports to a fixed number of units per year is a",
     "quota", "tariff", "embargo", "bounty", "A",
     "The ceiling is fixed in units."),
    (T_TRADE, "Medium", "Goods stored in a bonded warehouse before duty payment are under",
     "customs control", "police control", "bank control", "court control", "A",
     "Customs watches them closely."),
    (T_TRADE, "Medium", "A bonded warehouse's main advantage to an importer is that duty is paid",
     "only when goods are released", "twice on arrival", "in advance always", "never at all", "A",
     "Payment waits until removal."),
    (T_TRADE, "Hard", "An area where goods may enter, be worked on and leave without duties is a",
     "free port or free zone", "bonded warehouse", "public warehouse", "entrepot only", "A",
     "Duties skip the zone entirely."),
    (T_TRADE, "Medium", "The world body that sets rules for trade between nations is the",
     "WTO", "IMF", "OPEC", "ILO", "A",
     "It polices global trade rules."),
    (T_TRADE, "Medium", "UNCTAD, a UN organ, chiefly deals with",
     "trade and development", "refugee camps", "sports festivals", "climate treaties", "A",
     "Development through trade."),

    # ------------------------------------------------------------- entrepreneurship
    (T_ENT, "Medium", "The person who bears the risks of a business in search of profit is the",
     "entrepreneur", "employee", "consumer", "broker", "A",
     "Risk and reward are his lot."),
    (T_ENT, "Medium", "A written document stating a new firm's goals and how to reach them is a",
     "business plan", "trade letter", "invoice", "receipt", "A",
     "It is the firm's road map."),
    (T_ENT, "Hard", "Which factor of production earns profit as its reward?",
     "Entrepreneurship", "Labour", "Land", "Capital", "A",
     "The risk-taker collects profit."),
    (T_ENT, "Hard", "Rent, wages, interest and profit reward, in order, the factors",
     "land, labour, capital and enterprise", "labour, land, capital and enterprise", "capital, land, labour and enterprise", "enterprise, labour, land and capital", "A",
     "Match each factor to its pay."),
    (T_ENT, "Easy", "A business owned and run by one person is a",
     "sole proprietorship", "partnership", "company", "cooperative", "A",
     "One owner carries it all."),
    (T_ENT, "Medium", "A partner who only supplies capital and stays out of daily management is called a",
     "sleeping partner", "active partner", "general partner", "quasi partner", "A",
     "His money sleeps and works."),
    (T_ENT, "Hard", "Ordinary partnership law caps membership at how many partners?",
     "20", "50", "10", "unlimited", "A",
     "Beyond that, form a company.", "20"),
    (T_ENT, "Medium", "In a cooperative society, each member's voice is expressed through",
     "one member, one vote", "share count only", "the chairman alone", "annual rotation", "A",
     "Democracy rules the society."),
    (T_ENT, "Medium", "A business whose shares can be bought by the general public is a",
     "public limited company", "private limited company", "partnership", "sole proprietorship", "A",
     "The public may own pieces."),

    # ------------------------------------------------------------- finance
    (T_FIN, "Medium", "Money invested by owners into a firm in return for shares is",
     "equity capital", "loan capital", "working capital", "seed grant", "A",
     "Owners' money buys ownership."),
    (T_FIN, "Medium", "Money borrowed from a bank that must be repaid with interest is",
     "loan capital", "equity capital", "retained earnings", "capital reserve", "A",
     "The borrower owes interest too."),
    (T_FIN, "Hard", "A debenture holder is best described as a",
     "lender to the company", "owner of the company", "customer of the company", "auditor of the company", "A",
     "He lent money and holds proof."),
    (T_FIN, "Medium", "Trade credit is obtained when a supplier",
     "allows payment later", "demands cash on delivery", "sells only for coins", "gives no invoices", "A",
     "Buy the goods now, settle later."),
    (T_FIN, "Medium", "Short-term finance used to buy stock quickly is often arranged as an",
     "overdraft", "mortgage", "debenture", "leasehold", "A",
     "The account dips below zero."),
    (T_FIN, "Hard", "The stock of a company offered to the public for the first time is its",
     "initial public offer", "rights issue", "bonus issue", "private placement", "A",
     "The first sale to the public."),
    (T_FIN, "Hard", "An issue of extra shares to existing shareholders in proportion to their holding is a",
     "rights issue", "floatation", "takeover bid", "buy-back", "A",
     "Old owners get first option."),

    # ------------------------------------------------------------- insurance
    (T_INS, "Easy", "The principle that returns the insured to his exact loss position is",
     "indemnity", "subrogation", "contribution", "estoppel", "A",
     "The insured gains no profit from a loss."),
    (T_INS, "Hard", "After an insurer pays for a damaged car, the right to collect its scrap value rests with the",
     "insurer, by subrogation", "insured, forever", "repairer", "police", "A",
     "Paying transfers salvage rights."),
    (T_INS, "Medium", "Insuring the same risk with several insurers and sharing the loss among them illustrates",
     "contribution", "indemnity", "insurable interest", "good faith", "A",
     "Each policy pays its share."),
    (T_INS, "Medium", "The document that sets out the terms of cover is the",
     "insurance policy", "proposal form only", "cover note only", "claims form", "A",
     "The policy is the contract."),
    (T_INS, "Medium", "Insurance premium is the name for",
     "the price paid for cover", "the loss claimed", "the agent's fee", "the sum insured", "A",
     "You pay it to stay covered."),
    (T_INS, "Hard", "A policy that pays out a fixed sum either at death or at a set date is",
     "endowment life assurance", "term assurance", "fire insurance", "marine insurance", "A",
     "It matures like a savings plan."),
    (T_INS, "Medium", "Insurance taken to cover goods sent by sea is",
     "marine insurance", "motor insurance", "life assurance", "fidelity insurance", "A",
     "Ships and cargoes are covered."),

    # ------------------------------------------------------------- markets and combinations
    (T_MKT, "Medium", "A market where long-term securities are bought and sold is the",
     "stock exchange", "money market", "foreign exchange", "commodity market", "A",
     "Shares change hands there."),
    (T_MKT, "Hard", "On the trading floor, the dealer who buys and sells securities for his own account is the",
     "jobber", "broker", "stager", "tariff man", "A",
     "He trades with his own book."),
    (T_MKT, "Hard", "The unit into which a company's total share capital is divided is the",
     "share", "debenture", "bond coupon", "premium", "A",
     "Capital is sliced into these."),
    (T_MKT, "Hard", "Two firms that fuse into one new company have undergone an",
     "amalgamation", "agency", "cartel", "sole trade", "A",
     "Both dissolve into the new firm."),
    (T_MKT, "Hard", "Independent firms that agree to fix prices while staying separate form a",
     "cartel", "merger", "cooperative", "trust", "A",
     "They collude without fusing."),
    (T_MKT, "Medium", "An association of traders formed to promote their common interest is a",
     "trade association", "trade union", "political party", "credit union", "A",
     "Traders band together for strength."),

    # ------------------------------------------------------------- environment and communication
    (T_BIZ, "Easy", "Which body certifies the standards of made goods in Nigeria?",
     "SON", "NAFDAC", "FCCPC", "CBN", "A",
     "It stamps quality on goods."),
    (T_BIZ, "Medium", "The agency that regulates food and drug safety in Nigeria is",
     "NAFDAC", "SON", "NNPC", "NPA", "A",
     "It guards what we swallow."),
    (T_BIZ, "Medium", "A formal letter from one firm to another about business is best known as a",
     "business correspondence", "love letter", "obituary", "prose poem", "A",
     "Firms write to each other."),
    (T_BIZ, "Medium", "Buying and selling of goods over the internet is",
     "e-commerce", "barter", "hire purchase", "counter trade", "A",
     "The shop lives on a screen."),
    (T_BIZ, "Hard", "The biggest risk buyers face in online markets is",
     "payment fraud", "power supply", "shop rent", "staff pensions", "A",
     "Dishonest sellers vanish online."),
    (T_BIZ, "Hard", "Tourism earns foreign exchange for a country as part of its",
     "invisible exports", "visible exports", "domestic trade", "budget deficit", "A",
     "Visitors pay for services."),
]

build_batch(
    S,
    "batch_103_waec_commerce3.json",
    "103",
    "WAEC Commerce round 3 (Round 21 top-up): home, foreign and entrepot "
    "trade, invisible trade, balance of trade vs payments, customs "
    "duties, embargo vs quota, bonded warehouses and free ports, WTO and "
    "UNCTAD, entrepreneurs and business plans, factor rewards, sole "
    "proprietorship, sleeping partners, partner limits, cooperative "
    "voting, public companies, equity vs loan capital, debentures as "
    "lending, trade credit, overdrafts, IPO and rights issues, insurance "
    "principles (indemnity, subrogation, contribution), policy documents, "
    "premiums, endowment assurance, marine cover, stock exchange jobbers, "
    "shares, amalgamation vs cartel, trade associations, SON and NAFDAC, "
    "business correspondence, e-commerce risks and tourism earnings. "
    "Scanned against WAEC rounds 1-2, NECO Commerce and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
