"""Batch 185 - WAEC Commerce round 7 (WAEC top-up, R35).

Grows WAEC Commerce from 223 toward ~254 with angles not yet in
the bank: the enquiry that opens a foreign deal; the CIF price
term; the letter of credit; the import licence; the del credere
agent; the actuary and the loss adjuster; what makes a risk
insurable; the comprehensive motor policy; the negotiable cheque;
the certificate of deposit; the clearing system; the fixed deposit
account; the debit card; the stockbroker; the bonus issue;
leasing; factoring; authorised capital; the consumer cooperative;
vertical integration and the conglomerate; the hypermarket; the
private warehouse; the Ro-Ro vessel; the bilateral trade
agreement; exchange control; NEPC; legal tender; collective
bargaining; goodwill. Scanned against WAEC rounds 1-6, NECO
Commerce (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch185.py -> content/batch_185_waec_commerce7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_TPD = "Trade Procedures and Documents"
T_TPW = "Trade: Home, Foreign and World"
T_TPP = "Trade Practice and Payments"
T_BF = "Banking and Finance"
T_BSE = "Banking and the Stock Exchange"
T_FCN = "Business Finance and Capital"
T_INS = "Insurance"
T_BU = "Business Units"
T_BCO = "Business Combinations and Outlets"
T_ATD = "Aids to Trade"
T_TRN = "Transport and Logistics"
T_CPL = "Consumer Protection and Labour"

PASSAGES = []
PQ = []

Q = [
    (T_TPD, "Medium", "Before ordering goods from abroad, the importer first writes to ask about prices and terms. This opening step is the",
     "enquiry", "indent",
     "offer", "protest", "A",
     "The deal begins with a simple question."),
    (T_TPD, "Hard", "Under the price term CIF, the price quoted by the exporter covers the cost of the goods, the insurance and the",
     "ocean freight", "import duty at home",
     "buyer's profit margin", "local delivery charges", "A",
     "One price carries the goods to your own shore."),
    (T_TPD, "Hard", "The method of paying for imports in which the importer's bank guarantees payment once shipping documents are presented is the",
     "letter of credit", "open account",
     "consignment sale", "barter arrangement", "A",
     "The bank's promise travels in place of cash."),
    (T_TPD, "Medium", "Before certain restricted goods can be shipped in, the importer must first obtain from government an",
     "import licence", "insurance certificate",
     "bill of lading", "certificate of origin", "A",
     "Permission in writing precedes the goods."),
    (T_TPP, "Hard", "An agent who, for an extra commission, promises his principal that every buyer he introduces will pay is a",
     "del credere agent", "broker of ships",
     "auctioneer", "factor", "A",
     "He carries the buyer's debts on his own back."),
    (T_INS, "Hard", "The insurance professional who uses tables of statistics to calculate premiums is the",
     "actuary", "loss adjuster",
     "underwriter of shares", "broker", "A",
     "He prices the risk before it happens."),
    (T_INS, "Hard", "After a claim arises, the specialist the insurer sends to assess how much should be paid is the",
     "loss adjuster", "actuary",
     "assessor of taxes", "inspector of factories", "A",
     "He measures the loss in naira and kobo."),
    (T_INS, "Medium", "For an insurance company to accept a risk, the chance and size of the loss must be",
     "calculable from past records", "totally uncertain",
     "certain to happen soon", "impossibly large", "A",
     "No figures, no premium, no cover."),
    (T_INS, "Medium", "The motor policy that repairs the insured's OWN car after an accident, besides paying third parties, is the",
     "comprehensive policy", "third-party-only policy",
     "act-only policy", "green card", "A",
     "It carries the owner as well as the stranger."),
    (T_BF, "Medium", "A cheque is called a negotiable instrument because it",
     "is transferable by endorsement", "must be cashed only by the drawer",
     "cannot cross the counter freely", "always earns interest", "A",
     "Ownership rides along the signature."),
    (T_BF, "Hard", "The receipt a bank issues for a large fixed deposit, which the holder may sell before maturity, is a",
     "certificate of deposit", "treasury bill",
     "promissory note", "share warrant", "A",
     "A time deposit dressed for the market."),
    (T_BF, "Medium", "Cheques drawn on different banks in the same city are settled daily through the",
     "clearing system", "courier service",
     "stock exchange", "mint", "A",
     "Banks meet and cancel out one another's paper."),
    (T_BF, "Easy", "A customer who lodges money he has resolved not to touch for six months opens a",
     "fixed deposit account", "current account",
     "domiciliary account", "loan account", "A",
     "The money sleeps on deposit and earns interest."),
    (T_BF, "Medium", "Unlike a credit card, a debit card pays for goods by",
     "deducting at once from the holder's bank balance", "billing the holder at month's end",
     "borrowing from the card company", "drawing on the shop's account", "A",
     "Your own money leaves your own account."),
    (T_BSE, "Medium", "The licensed dealer's agent who buys and sells shares on the exchange floor on behalf of clients is the",
     "stockbroker", "jobber",
     "registrar", "stamp dealer", "A",
     "For a commission he carries your order to the floor."),
    (T_BSE, "Hard", "Free extra shares a company gives its owners out of built-up reserves constitute a",
     "bonus issue", "rights issue",
     "private placing", "offer for subscription", "A",
     "Reserves turn into shares, no cheque needed."),
    (T_FCN, "Medium", "A transport firm pays monthly to use trucks it will never own. The arrangement is",
     "leasing", "hire purchase",
     "factoring", "mortgaging", "A",
     "Use without ownership, for a rental."),
    (T_FCN, "Hard", "A company hands its customers' unpaid debts to a finance house and receives most of the cash at once. This is",
     "factoring", "discounting of one bill",
     "underwriting", "subordination", "A",
     "The debts are sold, not merely lent on."),
    (T_FCN, "Medium", "The amount of share capital stated in a company's memorandum as the most it may ever issue is its",
     "authorised capital", "called-up capital",
     "paid-up capital", "reserve capital", "A",
     "The ceiling named at birth."),
    (T_BU, "Medium", "A cooperative society formed so members can buy their everyday household goods cheaply together is a",
     "consumer cooperative", "producer cooperative",
     "credit union", "marketing cooperative", "A",
     "Members shop in the store they own."),
    (T_BCO, "Hard", "A flour mill buying up the farms that grow its wheat is practising",
     "vertical integration", "horizontal integration",
     "conglomeration", "cartel formation", "A",
     "Mill and farm join along one chain."),
    (T_BCO, "Medium", "A vast firm whose interests spread across banking, food processing and road transport at once is a",
     "conglomerate", "partnership",
     "cartel", "cooperative", "A",
     "Many trades under one umbrella."),
    (T_BCO, "Medium", "A single vast store sited outside town, combining a full supermarket with department shopping and parking grounds, is a",
     "hypermarket", "multiple shop",
     "kiosk", "mail-order house", "A",
     "Families drive out to shop for everything at once."),
    (T_ATD, "Medium", "A warehouse built and used by one manufacturer alone to store his own finished goods is a",
     "private warehouse", "public warehouse",
     "bonded warehouse", "cold store", "A",
     "It serves no master but its owner."),
    (T_TRN, "Hard", "A ship with ramps at bow and stern, built so loaded trucks can be driven straight aboard, is a",
     "roll-on roll-off vessel", "container ship",
     "tanker", "tug boat", "A",
     "The wheels roll in and roll out."),
    (T_TPW, "Medium", "An arrangement between two countries to exchange goods on agreed favourable terms is a",
     "bilateral trade agreement", "multilateral treaty",
     "trade embargo", "cartel", "A",
     "Two nations shake hands across the counter."),
    (T_TPW, "Hard", "Government's strict control over who may buy or sell foreign currency, and at what rate, is called",
     "exchange control", "credit control",
     "inventory control", "birth control", "A",
     "The gates of the dollar are guarded."),
    (T_TPW, "Hard", "The federal agency chiefly charged with promoting Nigeria's non-oil exports is",
     "NEPC", "NAFDAC",
     "NEPA", "NRC", "A",
     "The Export Promotion Council sells Nigeria abroad."),
    (T_BF, "Easy", "Naira notes must be accepted in settlement of any debt in Nigeria because they are",
     "legal tender", "near money",
     "representative money", "token coins", "A",
     "The law itself stands behind the paper."),
    (T_CPL, "Medium", "When the workers' union and the employers' association sit together to fix wages and conditions, the talks are called",
     "collective bargaining", "collective farming",
     "arbitration by court", "mediation of chiefs", "A",
     "Both sides speak as one for all their people."),
    (T_FCN, "Medium", "The good name and customer loyalty that make a shop sell for more than the value of its counters and stock is its",
     "goodwill", "capital reserve",
     "trade discount", "floating asset", "A",
     "Reputation itself is priced at the sale."),
]

build_batch(
    S,
    "batch_185_waec_commerce7.json",
    "185",
    "WAEC Commerce round 7 (R35 top-up): the enquiry; CIF; letter "
    "of credit; import licence; del credere agent; actuary; loss "
    "adjuster; insurable risk calculable; comprehensive motor; the "
    "negotiable cheque; certificate of deposit; clearing system; "
    "fixed deposit; debit card; stockbroker; bonus issue; leasing; "
    "factoring; authorised capital; consumer cooperative; vertical "
    "integration; conglomerate; hypermarket; private warehouse; "
    "Ro-Ro vessel; bilateral trade agreement; exchange control; "
    "NEPC; legal tender; collective bargaining; goodwill. Scanned "
    "against WAEC rounds 1-6, NECO Commerce (all rounds) and the "
    "JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
