"""Batch 113 - NECO Commerce round 3 (NECO top-up, Round 22).

Lifts NECO Commerce from 113 toward ~155 with angles not yet in any
bank: post office services, bank account types and e-banking channels,
payment instruments (cheques, drafts, bills of exchange, promissory
notes, cards), del credere agents and auctions, chambers of commerce,
business social responsibility and ethics, hire purchase vs leasing,
factoring basics and aids-to-trade links. Scanned against NECO rounds
1-2, WAEC Commerce (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch113.py -> content/batch_113_neco_commerce3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_POST = "The Post Office"
T_BANK = "Banking Services and Accounts"
T_PAY = "Instruments of Payment"
T_AIDS = "Aids to Trade: Agents and Auctions"
T_RESP = "Business Responsibility and Ethics"
T_FIN = "Hire Purchase, Leasing and Factoring"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- post office
    (T_POST, "Medium", "A post office box (PO box) serves mainly to",
     "receive mail securely", "send telegrams abroad", "weigh parcels in transit", "stamp first-day covers", "A",
     "The renter collects mail there."),
    (T_POST, "Medium", "Registered post offers the sender",
     "proof of posting and safer delivery", "free insurance for all goods", "faster planes always", "discounted stamps", "A",
     "The item is tracked and signed for."),
    (T_POST, "Hard", "Post restante means mail is held at the office for collection by",
     "a traveller who shows identity", "the postmaster's family", "the sender again", "no one at all", "A",
     "Town guests collect mail this way."),
    (T_POST, "Medium", "Courier services attract customers mainly because they are",
     "fast and offer door-to-door delivery", "cheaper than any letter", "run by the government only", "limited to books", "A",
     "Speed is their selling point."),
    (T_POST, "Hard", "The postal service's money order allows a customer to",
     "send money through the post", "borrow from the post office", "insure a parcel", "rent a box free", "A",
     "The cash travels as paper."),

    # ------------------------------------------------------------- banking
    (T_BANK, "Medium", "A current account holder is issued a cheque book and normally earns",
     "little or no interest", "the highest interest", "dividends yearly", "free loans monthly", "A",
     "Convenience, not yield, is the aim."),
    (T_BANK, "Medium", "A savings account is designed chiefly to encourage",
     "safe saving of money", "bulk trade payments", "company floatation", "foreign deals only", "A",
     "Small savers are welcome."),
    (T_BANK, "Hard", "A fixed deposit account rewards the customer with",
     "higher interest on locked funds", "unlimited cheque books", "free overdrafts always", "monthly cash prizes", "A",
     "The money stays put for the term."),
    (T_BANK, "Medium", "An overdraft differs from a loan because it is",
     "drawn on a current account", "always for ten years", "given without a bank", "repaid only by salary", "A",
     "You dip below zero as needed."),
    (T_BANK, "Hard", "Using a POS terminal, a buyer pays by",
     "card at the shop till", "post office order", "bill of exchange", "barter of goods", "A",
     "The machine reads the card."),
    (T_BANK, "Medium", "The NIBSS instant transfer system moves money between banks",
     "within seconds, all day", "only on weekdays at noon", "by post each month", "through embassies", "A",
     "NIP payments settle at once."),
    (T_BANK, "Medium", "Mobile banking apps let customers chiefly",
     "transact from anywhere", "print currency at home", "set exchange rates", "audit the bank", "A",
     "The branch fits in a pocket."),

    # ------------------------------------------------------------- payment instruments
    (T_PAY, "Medium", "The person named on a cheque as the payee is the one who",
     "receives the money", "writes the cheque", "guarantees payment", "stamps it paid", "A",
     "The drawer orders payment to him."),
    (T_PAY, "Hard", "Crossing a cheque with two parallel lines makes it",
     "payable only through a bank account", "invalid at once", "payable in cash anywhere", "a bank draft", "A",
     "Cash cannot be paid over the counter."),
    (T_PAY, "Hard", "A stale cheque is one presented after the bank's validity period, usually",
     "six months", "six weeks", "two years", "ten days", "A",
     "Banks refuse the aged cheque."),
    (T_PAY, "Medium", "A bank draft is drawn by",
     "the bank on itself", "a customer on a friend", "a shop on a buyer", "a court on a bank", "A",
     "The bank's own promise pays."),
    (T_PAY, "Hard", "A bill of exchange involves three parties: the drawer, the drawee and the",
     "payee", "notary", "auditor", "broker", "A",
     "One orders, one accepts, one collects."),
    (T_PAY, "Hard", "Two parties only take part in a",
     "promissory note", "bill of exchange", "cheque", "bank draft", "A",
     "The maker promises the payee directly."),
    (T_PAY, "Medium", "A credit card allows the holder to",
     "buy now, settle later", "print money at will", "escape all payments", "set government tariffs", "A",
     "Credit rides on the card."),

    # ------------------------------------------------------------- agents and auctions
    (T_AIDS, "Hard", "A del credere agent promises the principal that buyers he introduces will",
     "pay for the goods supplied", "return the goods unused", "buy from rivals", "insure the goods", "A",
     "He bears the bad-debt risk for extra commission."),
    (T_AIDS, "Medium", "In an auction sale, the item goes to the",
     "highest bidder", "first bidder", "seller's cousin", "lowest bidder", "A",
     "The hammer falls on top money."),
    (T_AIDS, "Hard", "The reserve price in an auction is the figure",
     "below which the seller will not sell", "the auctioneer keeps secret forever", "the buyer must pay twice", "the government taxes", "A",
     "No sale happens under it."),
    (T_AIDS, "Medium", "A factor sells goods on behalf of the principal",
     "in his own name", "only by public auction", "without any commission", "only in foreign markets", "A",
     "He trades as if the goods were his own."),
    (T_AIDS, "Medium", "The Chamber of Commerce mainly promotes",
     "the business interests of an area", "a single family firm", "civil service recruitment", "school sports meets", "A",
     "Members' common good guides it."),

    # ------------------------------------------------------------- responsibility and ethics
    (T_RESP, "Medium", "A firm's social responsibility includes providing",
     "fair wages and safe products", "free holidays abroad", "loans to ministers", "hidden charges", "A",
     "Society expects more than profit."),
    (T_RESP, "Medium", "Business ethics means conducting trade with",
     "honesty and fairness", "maximum speed only", "total secrecy", "zero wages", "A",
     "Right conduct rules the market."),
    (T_RESP, "Hard", "A company that dumps waste into a river violates its duty of",
     "environmental care", "staff promotion", "share registration", "brand loyalty", "A",
     "The community drinks that water."),
    (T_RESP, "Hard", "Insider trading is unethical because it",
     "abuses secret information", "pays its tax too early", "advertises falsely", "overpays its workers", "A",
     "The playing field is tilted."),
    (T_RESP, "Medium", "Honest labelling of a product respects the consumer's right to",
     "information", "free goods", "holiday pay", "silence", "A",
     "The label tells the truth."),

    # ------------------------------------------------------------- hire purchase, leasing, factoring
    (T_FIN, "Medium", "In a hire purchase deal, the buyer finally owns the goods after he",
     "makes the final installment", "signs the agreement", "pays the first deposit", "takes delivery", "A",
     "Until then he only hires."),
    (T_FIN, "Hard", "In a finance lease, the lessor is typically",
     "a leasing company", "the user of the asset", "a bank customer", "an auctioneer", "A",
     "The owner rents, the user pays."),
    (T_FIN, "Hard", "Factoring gives a business quick cash by selling its",
     "accounts receivable", "fixed machines", "office building", "company shares", "A",
     "The factor collects the debts."),
    (T_FIN, "Medium", "The main attraction of hire purchase to a small buyer is",
     "spreading payment over time", "paying less total cash", "owning goods at once", "avoiding all charges", "A",
     "The price of patience is interest."),
    (T_FIN, "Medium", "Transport, banking, insurance, warehousing, advertising and communication are together called the",
     "aids to trade", "channels of trade", "barriers to trade", "terms of trade", "A",
     "They grease the wheels of commerce."),
    (T_FIN, "Hard", "Aiding exchange by bearing risk of loss in transit is performed by",
     "insurers", "advertising agents", "chambers of commerce", "money lenders", "A",
     "For a premium, the risk moves."),
]

build_batch(
    S,
    "batch_113_neco_commerce3.json",
    "113",
    "NECO Commerce round 3 (Round 22 top-up): PO boxes, registered and "
    "post restante mail, couriers and money orders, current, savings and "
    "fixed deposit accounts, overdraft vs loan, POS, NIBSS instant "
    "transfers and mobile apps, payee and drawer, cheque crossing, stale "
    "cheques, bank drafts, bills of exchange, promissory notes, credit "
    "cards, del credere agents, auction reserve prices, factors, the "
    "Chamber of Commerce, social responsibility, business ethics, "
    "pollution and insider trading, honest labels, hire purchase "
    "ownership transfer, finance leases, factoring, aids to trade and "
    "risk-bearing. Scanned against NECO rounds 1-2, WAEC Commerce (all "
    "rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
