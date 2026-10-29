"""Batch 238 - NECO Commerce round 4 (NECO top-up, R49).

Grows NECO Commerce from 265 toward ~290 with angles verified absent
from the whole Commerce pool (1,352 items across JAMB, WAEC and
NECO) and cleared of cross-subject twins via db sweep. Fresh angles:
purchase requisition; purchase order; goods received note; back
order; bin card; shredder; office memo; grapevine; upward and
downward communication; physical distribution; stock control;
reorder level; lead time; buffer stock; economic order quantity;
just-in-time; labour turnover; fringe benefits; invoice
discounting; compulsory third-party insurance; offer and
acceptance; poste restante; dry port (inland container depot);
transit trade; functions of packaging. Avoided as banked: all the
classic trade documents (invoice, credit/debit notes, consignment
note, advice note, delivery note, bill of lading, airway bill,
charter party, mate's receipt as option, packing list, indent,
certificate of origin, consular invoice, statement of account,
quotation, remittance letter), insurance families (principles,
actuary, surrender value, subrogation, fidelity, NEPC), retail
institutions (supermarket, multiples, mail order, vending, tied
shops, cash-and-carry, hypermarket, discount store), transport
modes incl. pipeline items, warehouse types incl. bonded ×many,
personal selling, test marketing, after-sales, caveat emptor,
amalgamation, delegation, span of control, NEPC, social
responsibility, Maslow (kept out — syllabus fit), order processing
(Marketing cross-twin), functions of warehousing (JAMB NOT-item
banked), wholesaler/retailer functions.

    python3 scripts/build_neco_batch238.py -> content/batch_238_neco_comm4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_DOC = "Trade Documents"
T_OFF = "Office Practice"
T_TRAN = "Transport"
T_WARE = "Warehousing"
T_OCC = "Occupations and Production"
T_FIN = "Hire Purchase, Leasing and Factoring"
T_INS = "Insurance"
T_TRADE = "Trade"
T_POST = "The Post Office"
T_PORT = "Ports, Customs and Warehouses"
T_HOME = "Home and Foreign Trade"
T_CONS = "The Consumer"

PASSAGES = []
PQ = []

Q = [
    (T_DOC, "Medium", "In a well-run store, the internal document filled by a department to formally request the purchase office to buy goods for it is the",
     "purchase requisition", "purchase order",
     "goods received note", "sales invoice", "A",
     "It says: we need this — please go and buy."),
    (T_DOC, "Medium", "The document that the buying firm sends to the supplier, stating the goods, quantities, prices and delivery terms agreed, is the",
     "purchase order", "purchase requisition",
     "debit note", "waybill", "A",
     "Once the supplier accepts it, a binding deal exists."),
    (T_DOC, "Easy", "When goods ordered finally arrive, the store keeper checks them against the order and signs the document that confirms the right goods were received in good condition. That document is the",
     "goods received note", "credit note",
     "proforma invoice", "consignment note", "A",
     "No note, no entry into the stores ledger."),
    (T_DOC, "Hard", "A customer orders ten cartons of soap but the supplier is able to send only six, promising to send the remaining four later. The four outstanding cartons form a",
     "back order", "bad order",
     "counter order", "closed order", "A",
     "The unfinished part of the order waits in the book."),
    (T_OFF, "Medium", "The card kept in the store for each item of stock, on which the store keeper records every quantity received and issued and the balance remaining, is the",
     "bin card", "index card",
     "credit card", "score card", "A",
     "One card, one item, always showing what is left."),
    (T_OFF, "Easy", "The office machine used to destroy confidential waste papers so that strangers cannot read them is the",
     "shredder", "photocopier",
     "guillotine", "stapler", "A",
     "Old secrets leave the office as strips."),
    (T_OFF, "Medium", "A short written message used for communication within one organisation, from one office to another, is the",
     "office memo", "circular letter",
     "waybill", "telex message", "A",
     "No stamp is needed; it never leaves the house."),
    (T_OFF, "Hard", "In office communication, the informal network through which rumours and unofficial news travel among workers is popularly called the",
     "grapevine", "grapesheet",
     "green line", "grey channel", "A",
     "News that grows along it ripens faster than the notice board."),
    (T_OFF, "Medium", "Communication that flows from superior to subordinate is called downward communication, while communication that flows from subordinate to superior is called",
     "upward communication", "outward communication",
     "sideward communication", "inward communication", "A",
     "Orders travel down; reports travel up."),
    (T_TRAN, "Medium", "All the activities involved in moving goods from the end of the production line into the hands of the final consumer — transport, warehousing, stock control and order handling — are together called",
     "physical distribution", "physical inspection",
     "wholesale trading", "counter trade", "A",
     "The product's last journey has its own name."),
    (T_WARE, "Medium", "The whole system of checking, recording and regulating the quantities of goods a firm holds, so that it neither runs short nor overstocks, is called",
     "stock control", "stock exchange",
     "stocktaking only", "stockbroking", "A",
     "Too little stops sales; too much blocks money."),
    (T_WARE, "Hard", "The stock level at which a new order must be placed so that fresh supplies arrive just before the old stock finishes is the",
     "reorder level", "retail level",
     "resale level", "recording level", "A",
     "Below this line, the pen writes to the supplier."),
    (T_WARE, "Medium", "The number of days between placing an order for goods and their arrival at the store is called the",
     "lead time", "lease time",
     "loss time", "log time", "A",
     "The gap between ordering and opening the cartons."),
    (T_WARE, "Hard", "Extra stock deliberately held above the normal level to guard against sudden rises in demand or delay in delivery is called",
     "buffer stock", "bad stock",
     "bonded stock", "barter stock", "A",
     "The pillow that softens an unexpected blow."),
    (T_WARE, "Hard", "The quantity of an item that a firm should order each time, so that the combined costs of ordering and of holding stock are as low as possible, is the",
     "economic order quantity", "easiest order quantity",
     "estimated order quality", "emergency order quota", "A",
     "Order too rarely or too often and costs climb."),
    (T_WARE, "Hard", "A purchasing system in which a firm arranges for goods to arrive only shortly before they are needed, so that it holds almost no stock, is known as",
     "just-in-time purchasing", "just-in-case purchasing",
     "cash-and-carry purchasing", "hire-and-return purchasing", "A",
     "The part reaches the line the hour it is wanted."),
    (T_OCC, "Medium", "The rate at which workers leave a firm and have to be replaced within a given period is called",
     "labour turnover", "labour exchange",
     "staff rotation", "shift turnover", "A",
     "When many hands go, the door revolves quickly."),
    (T_OCC, "Easy", "Extra benefits given to workers apart from their basic salary — such as housing allowance, medical care and transport — are collectively called",
     "fringe benefits", "fringe salaries",
     "outer wages", "side commissions", "A",
     "The basket of extras that keeps the worker glad."),
    (T_FIN, "Hard", "A firm raises immediate cash by selling its unpaid customer invoices to a finance house at a discount, but without the safety of the debts being guaranteed. This arrangement is",
     "invoice discounting", "factoring",
     "forfeiting", "floor financing", "A",
     "The debts are advanced upon, not collected for you."),
    (T_INS, "Medium", "The insurance that every vehicle owner in Nigeria must by law have before driving on public roads is",
     "third-party motor insurance", "comprehensive cover only",
     "life assurance", "fidelity guarantee", "A",
     "It protects the other road user, not your own car."),
    (T_TRADE, "Medium", "When a buyer's offer to buy is accepted by the seller, the essential first requirement of a simple contract of sale has been created. This requirement is",
     "offer and acceptance", "seal and stamp",
     "witness and oath", "registry and licence", "A",
     "One hand stretches out; the other closes on it."),
    (T_POST, "Medium", "The postal service by which letters are addressed to a post office and kept there until the addressee, who is travelling and has no fixed address, calls to collect them, is",
     "poste restante", "recorded delivery",
     "post office box", "cash on delivery", "A",
     "The letter waits at the counter for its owner."),
    (T_PORT, "Hard", "An inland facility, linked to the seaports by rail or road, where containers can be cleared and customs formalities completed far from the coast, is called a",
     "dry port", "free port",
     "ocean port", "fishing port", "A",
     "The sea is brought, by rail, to Kano's doorstep."),
    (T_HOME, "Medium", "Goods that pass through Nigeria from one foreign country to another, without being consumed in Nigeria, are said to be in",
     "transit trade", "entrepôt trade only",
     "coastal trade", "bilateral trade", "A",
     "They enter at one border and leave by another."),
    (T_CONS, "Medium", "Besides protecting the goods inside, a good package identifies the product, carries instructions, and helps to advertise it. These are together described as the",
     "functions of packaging", "facts of branding",
     "rules of labelling", "forms of wrapping", "A",
     "The wrapper works as guard, clerk and salesman."),
]

build_batch(
    S,
    "batch_238_neco_comm4.json",
    "238",
    "NECO Commerce round 4 (R49 top-up): purchase requisition; "
    "purchase order; goods received note; back order; bin card; "
    "shredder; office memo; grapevine; upward and downward "
    "communication; physical distribution; stock control; reorder "
    "level; lead time; buffer stock; EOQ; just-in-time; labour "
    "turnover; fringe benefits; invoice discounting; compulsory "
    "third-party insurance; offer and acceptance; poste restante; "
    "dry port; transit trade; functions of packaging. Scanned "
    "against the whole Commerce pool (JAMB, WAEC and NECO stems) "
    "and cleared of cross-subject twins.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
