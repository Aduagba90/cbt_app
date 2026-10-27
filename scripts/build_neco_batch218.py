"""Batch 218 - NECO Commerce round 8 (NECO top-up, R44).

Grows NECO Commerce from 240 toward ~265 with angles verified absent
from the whole Commerce pool (1,302 items across JAMB, WAEC and NECO):
mail transfer; telegraphic transfer; dishonour for irregular signature;
money market as short-term market; call money; surrender value; group
insurance; share premium; deferred shares; interim dividend; vertical
filing; slogan; speciality shop; tied shop; teleconference; bar code;
nominal partner; trading certificate; dormant account; stock broker;
forward integration; backward integration; cash and carry; order
cheque; travel agency. Checked: crossed-cheque meaning, indent,
charter, FOB/CIF, requisition, authorised capital, average clause,
no-claim bonus, sleeping partner, underwriter, hypermarket, document
of title, retained earnings, money order, post-dated - ALL already in
the bank, avoided.

    python3 scripts/build_neco_batch218.py -> content/batch_218_neco_commerce8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_PAY = "Instruments of Payment"
T_BANK = "Banking Services"
T_BANKA = "Banking Services and Accounts"
T_INS = "Insurance"
T_SE = "The Stock Exchange"
T_OFF = "Office Practice"
T_ADV = "Advertising"
T_RET = "Retailing and Wholesaling"
T_TC = "Transport and Communication"
T_BU = "Business Units"
T_PROD = "Production and Industry"
T_TOUR = "Tourism"

PASSAGES = []
PQ = []

Q = [
    (T_PAY, "Medium", "Alhaji instructs his bank in Kano to send money to a supplier in Dubai. The bank writes out the payment instruction and posts it by ordinary mail to its correspondent bank abroad. This method of payment is",
     "a mail transfer", "a telegraphic transfer",
     "a bill of exchange", "a letter of credit", "A",
     "The instruction travels slowly, by post."),
    (T_PAY, "Easy", "The fastest method of transferring money abroad, in which the paying bank sends the details of the payment by cable or electronic means, is",
     "a telegraphic transfer", "a mail transfer",
     "a postal order", "a promissory note", "A",
     "The message races ahead of any letter."),
    (T_BANK, "Medium", "Which of the following is a valid reason for a bank to dishonour a customer's cheque?",
     "The signature differs from the specimen held at the bank", "The account holds enough money for the payment",
     "The cheque was presented within six months", "The amount in words matches the figures", "A",
     "A strange signature casts doubt on the drawer."),
    (T_BANKA, "Medium", "Short-term financial instruments such as treasury bills and call money are bought and sold in the",
     "money market", "capital market",
     "commodity market", "foreign exchange market", "A",
     "The money market deals in short-term funds."),
    (T_BANKA, "Hard", "Money which banks lend to one another for very short periods and which the lender can recall at any time is called",
     "call money", "fixed deposit",
     "share capital", "legal tender", "A",
     "The borrower must repay as soon as it is called."),
    (T_INS, "Medium", "The sum of money an insurer pays to a life policyholder who gives up his policy before it matures is the",
     "surrender value", "maturity value",
     "face value", "premium rebate", "A",
     "He surrenders the policy and collects what it has earned."),
    (T_INS, "Easy", "A single insurance policy taken out by an employer to cover all the workers in his factory at once is",
     "group insurance", "fire insurance",
     "marine insurance", "motor insurance", "A",
     "One policy covers the whole staff of the firm."),
    (T_SE, "Hard", "A company issues shares at 50 kobo above their nominal value of one naira each. The extra 50 kobo per share is credited to the",
     "share premium account", "sinking fund account",
     "dividend account", "share discount account", "A",
     "The issue price sits above the face value."),
    (T_SE, "Hard", "Shares whose holders receive dividends only after every other class of shareholder has been paid are",
     "deferred shares", "preference shares",
     "ordinary shares", "cumulative shares", "A",
     "Their reward waits until all others are settled."),
    (T_SE, "Medium", "A dividend paid to shareholders part-way through the trading year, before the final accounts have been prepared, is called",
     "an interim dividend", "a final dividend",
     "a stock dividend", "a deferred dividend", "A",
     "It is a part-payment ahead of the year's end."),
    (T_OFF, "Medium", "A filing system in which documents stand upright in a drawer so that any file can be consulted without lifting the others is",
     "vertical filing", "flat filing",
     "box filing", "wire filing", "A",
     "Papers stand on edge like books on a shelf."),
    (T_ADV, "Easy", "A short, striking phrase which advertisers repeat so often that buyers remember the product easily is a",
     "slogan", "poster",
     "leaflet", "caption", "A",
     "A few well-chosen words stick in the memory."),
    (T_RET, "Medium", "A shop that confines itself to one narrow line of goods, such as children's footwear only, is a",
     "speciality shop", "department store",
     "supermarket", "multiple shop", "A",
     "Its whole stock serves one class of buyers."),
    (T_RET, "Medium", "A retail outlet that sells only the products of one manufacturer, such as a brewery's own beer depots, is a",
     "tied shop", "market stall",
     "general store", "mobile shop", "A",
     "Its stock is tied to a single producer."),
    (T_TC, "Easy", "Managers in Lagos, Enugu and Kaduna meet at the same time, seeing and hearing one another through television screens. The meeting is",
     "a teleconference", "a courier service",
     "a telex message", "a telegraph", "A",
     "Distance no longer keeps them apart."),
    (T_RET, "Easy", "The pattern of thick and thin lines printed on a product's packet, which the cashier's scanner reads to bring up the price, is the",
     "bar code", "trade mark",
     "brand name", "price tag", "A",
     "The till reads the lines in a flash."),
    (T_BU, "Hard", "A person who allows his name to be used as a partner although he contributes no capital and shares no profit is a",
     "nominal partner", "sleeping partner",
     "active partner", "general partner", "A",
     "Only his name, not his money, is in the firm."),
    (T_BU, "Medium", "A public limited company may not commence business until it obtains from the Registrar of Companies a",
     "trading certificate", "certificate of origin",
     "memorandum of association", "certificate of insurance", "A",
     "Incorporation births it; this lets it trade."),
    (T_BANK, "Easy", "An account in which the customer has made no deposit or withdrawal for a long period, so that the bank treats it as inactive, is a",
     "dormant account", "current account",
     "savings account", "fixed deposit account", "A",
     "Long silence puts the account to sleep."),
    (T_SE, "Easy", "The dealer who is a member of the stock exchange and buys and sells securities on behalf of investors for a commission is the",
     "stock broker", "jobber",
     "speculator", "registrar", "A",
     "He acts for clients, not for himself."),
    (T_PROD, "Medium", "A flour miller in Kano opens a chain of bakery shops to sell bread directly to consumers. This growth strategy is",
     "forward integration", "backward integration",
     "horizontal integration", "conglomerate integration", "A",
     "He steps nearer to the final consumer."),
    (T_PROD, "Medium", "A baker decides to stop buying flour and establishes his own wheat milling plant. This strategy is",
     "backward integration", "forward integration",
     "horizontal integration", "diversification", "A",
     "He moves a step closer to his raw material."),
    (T_RET, "Medium", "A wholesaling arrangement in which retailers pay cash on the spot and transport the goods away with their own vehicles is",
     "cash and carry", "sale on credit",
     "mail order", "hire purchase", "A",
     "Pay now and pack now; no credit, no delivery."),
    (T_PAY, "Medium", "A cheque whose payee is named as 'Bala Musa or order' can be paid only to Bala or to a person he directs. Such a cheque is",
     "an order cheque", "a bearer cheque",
     "a crossed cheque", "a stale cheque", "A",
     "The words 'or order' restrict the payment."),
    (T_TOUR, "Easy", "A firm that arranges flight tickets, hotel bookings and tours for travellers, earning commission from airlines and hotels, is a",
     "travel agency", "transport company",
     "insurance broker", "shipping line", "A",
     "It plans the journey while others carry it out."),
]

build_batch(
    S,
    "batch_218_neco_commerce8.json",
    "218",
    "NECO Commerce round 8 (R44 top-up): mail transfer; telegraphic "
    "transfer; dishonour for irregular signature; money market as "
    "short-term market; call money; surrender value; group insurance; "
    "share premium; deferred shares; interim dividend; vertical "
    "filing; slogan; speciality shop; tied shop; teleconference; bar "
    "code; nominal partner; trading certificate; dormant account; "
    "stock broker; forward integration; backward integration; cash "
    "and carry; order cheque; travel agency. Scanned against the "
    "whole Commerce pool (JAMB, WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
