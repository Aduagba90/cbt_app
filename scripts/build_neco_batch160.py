"""Batch 160 - NECO Commerce round 6 (NECO top-up, R30).

Grows NECO Commerce from 182 toward ~220 with angles not yet in the
bank: office practice (filing methods, mail registers, remittance
letters, franking, open-plan vs closed offices, the personnel
department, requisitions, indexing); itinerant traders (hawker,
pedlar, cheap jack, stallholder); the five Cs of credit; transport
mode comparisons (air for urgent perishables, water for heavy
international cargo, road door-to-door, rail for bulk); and
telecommunication services (telephone, telex, fax, telegram, email vs
post). Scanned against NECO rounds 1-4, WAEC Commerce (all rounds)
and the JAMB pool.

    python3 scripts/build_neco_batch160.py -> content/batch_160_neco_commerce6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_OFF = "Office Practice"
T_ITIN = "Itinerant Traders"
T_CRED = "Consumer Credit"
T_TRANS = "Choosing Transport Modes"
T_TEL = "Telecommunication Services"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- office practice
    (T_OFF, "Medium", "Files arranged in a cabinet following customers' surnames from A to Z use the",
     "alphabetical method", "numerical method", "geographical method", "subject method", "A",
     "Adewale sits before Bello."),
    (T_OFF, "Hard", "The filing method that uses an index to link numbers with names is the",
     "numerical method", "alphabetical method", "chronological method", "alpha-numerical-free method", "A",
     "The number hides behind the index card."),
    (T_OFF, "Medium", "Invoices filed strictly by the dates they were received follow the",
     "chronological method", "subject method", "numerical method", "place method", "A",
     "Time itself orders the row."),
    (T_OFF, "Hard", "A clinic filing all documents on malaria together, whoever the patient, uses the",
     "subject method", "alphabetical method", "numerical method", "chronological method", "A",
     "The topic rules the folder."),
    (T_OFF, "Medium", "The book recording every letter the office receives, with dates and senders, is the",
     "inward mail register", "outward mail register", "cash book", "minute book", "A",
     "Incoming post signs its name there."),
    (T_OFF, "Medium", "Before dispatching goods, a mail clerk stamps the envelope with the postage meter. This is called",
     "franking", "folding", "collating", "laminating", "A",
     "The machine prints the postage."),
    (T_OFF, "Hard", "The letter sent along with a payment, telling the seller what the money is for, is a",
     "remittance letter", "covering licence", "pro-forma invoice", "circular letter", "A",
     "It names the debt being settled."),
    (T_OFF, "Medium", "A big room where all clerks sit together without partitioning walls is",
     "an open-plan office", "a closed office", "a private study", "a board room", "A",
     "One floor, many desks, easy watching."),
    (T_OFF, "Hard", "A closed office arrangement's chief merit is",
     "privacy and quiet", "cheap furniture always", "no supervision ever", "faster filing guaranteed", "A",
     "Walls keep secrets and silence."),
    (T_OFF, "Medium", "The department that keeps staff records and handles recruitment is",
     "personnel department", "accounts department", "marketing department", "legal department", "A",
     "People are that ledger every day."),
    (T_OFF, "Medium", "The internal document a department sends to the store keeper asking for stationery is a",
     "requisition", "receipt voucher", "credit note", "waybill", "A",
     "It asks the store to issue goods."),
    (T_OFF, "Hard", "The card that guides a clerk straight to a file's number without searching is the",
     "index card", "salary sheet", "bin card only", "delivery note", "A",
     "A small signpost made of card."),
    (T_OFF, "Medium", "Before a new file is opened, the clerk first checks the",
     "cross-reference sheet", "cash analysis book", "petty cash float", "staff roster", "A",
     "Old papers may already live elsewhere."),

    # ------------------------------------------------------------- itinerant traders
    (T_ITIN, "Medium", "A trader who carries his wares on his head through the streets, calling out to buyers, is a",
     "hawker", "pedlar", "cheap jack", "stallholder", "A",
     "His shop walks and shouts."),
    (T_ITIN, "Hard", "The itinerant trader who moves from town to town carrying his goods on a bicycle or animal is the",
     "pedlar", "hawker", "cheap jack", "barrow boy", "A",
     "The distance is his market place."),
    (T_ITIN, "Hard", "An itinerant who sets up a temporary stand at market days and auctions cheap assorted goods is the",
     "cheap jack", "pedlar", "hawker", "wholesaler", "A",
     "Today here, tomorrow gone."),
    (T_ITIN, "Medium", "A trader who rents a fixed spot by the roadside with a small permanent table operates as a",
     "stallholder", "hawker", "pedlar", "mail order house", "A",
     "The table stays; the market visits."),
    (T_ITIN, "Medium", "The chief common feature of all itinerant traders is that they",
     "move about to meet buyers", "own large shops", "sell only to governments", "grant long credits", "A",
     "Their stock travels with them."),

    # ------------------------------------------------------------- credit
    (T_CRED, "Hard", "A credit applicant's steady income and ability to repay constitute his",
     "capacity", "capital", "character", "collateral", "A",
     "Can he truly repay the loan?"),
    (T_CRED, "Hard", "The asset a borrower pledges, which the lender may seize on default, is his",
     "collateral", "capacity", "condition", "capital", "A",
     "The security stands behind the loan."),
    (T_CRED, "Medium", "A customer's honest reputation for paying debts, gathered from referees, is his",
     "character", "capacity", "collateral", "connection", "A",
     "Past honesty predicts future payment."),
    (T_CRED, "Medium", "The money a trader has invested in his own business is, in credit analysis, his",
     "capital", "character", "condition", "collateral", "A",
     "His own stake in the game."),
    (T_CRED, "Hard", "The general state of trade and the economy at the time of lending is the",
     "condition", "capacity", "collateral", "capital", "A",
     "Even honest men drown in floods."),

    # ------------------------------------------------------------- transport modes
    (T_TRANS, "Medium", "Fresh flowers and live perishables for export travel best by",
     "air", "rail", "sea", "pipeline", "A",
     "Speed alone keeps them alive."),
    (T_TRANS, "Medium", "Heavy machinery imported from Europe to Lagos moves cheapest by",
     "sea", "air", "road", "post", "A",
     "Ships carry tonnes for kobo."),
    (T_TRANS, "Medium", "The transport mode that alone delivers goods from the factory to the buyer's doorstep is",
     "road", "rail", "air", "pipeline", "A",
     "The lorry owns the last mile."),
    (T_TRANS, "Hard", "Bags of cement moving in one long train from Obajana to Kaduna travel best by",
     "rail", "air", "motor cycle", "pipeline", "A",
     "Steel wheels love steady bulk."),
    (T_TRANS, "Hard", "A product that can be moved ONLY by pipeline among all the modes is",
     "cooking gas in bulk", "bagged rice", "frozen fish", "motor cars", "A",
     "It flows where nothing rolls."),

    # ------------------------------------------------------------- telecom
    (T_TEL, "Medium", "The telecommunication service that transmits written messages over telephone lines to printed terminals is",
     "telex", "telegram", "registered mail", "radio phone-in", "A",
     "The office machine that talks on paper."),
    (T_TEL, "Hard", "A document transmitted as an electronic picture of its original, signature included, is sent by",
     "fax", "telex", "telegram", " mail order", "A",
     "The page arrives looking itself."),
    (T_TEL, "Medium", "The service by which a message is dictated to a post office and delivered as a written note is the",
     "telegram", "telephone", "fax", "telex", "A",
     "Wire-borne words on paper."),
    (T_TEL, "Medium", "Compared with the postal service, the chief advantage of email is",
     "speed and low cost", "better handwriting", "heavier parcels", "stamps collected", "A",
     "It crosses oceans in seconds."),
    (T_TEL, "Hard", "The telephone's greatest limitation in business communication is that it leaves",
     "no written record unless noted", "no sound at all", "no bills ever", "no distance covered", "A",
     "Words vanish when the call ends."),
]

build_batch(
    S,
    "batch_160_neco_commerce6.json",
    "160",
    "NECO Commerce round 6 (R30 top-up): alphabetical, numerical, "
    "chronological and subject filing; inward mail register, franking, "
    "remittance letter; open-plan vs closed office; personnel "
    "department; requisition; index card; cross-reference; hawker, "
    "pedlar, cheap jack, stallholder and their common feature; five Cs "
    "of credit (capacity, collateral, character, capital, condition); "
    "air for perishables, sea for heavy cargo, road door-to-door, rail "
    "for cement, pipeline for gas; telex, fax, telegram, email vs "
    "post, telephone's no-record limit. Scanned against NECO rounds "
    "1-4, WAEC Commerce (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
