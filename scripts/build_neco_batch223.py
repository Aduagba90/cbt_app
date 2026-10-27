"""Batch 223 - WAEC Commerce round 9 (WAEC top-up, R45).

Grows WAEC Commerce from 254 toward ~279 with angles verified absent
from the whole Commerce pool (1,327 items across JAMB, WAEC and NECO):
hazard (insurance); beneficiary; arbitrage; blue chip; hedging; lame
duck; dividend warrant; night safe; counterfoil; passbook; consignee;
lighterage; quorum; proxy; casting vote; statutory meeting;
extraordinary general meeting; company secretary; agenda; lateral
filing; indexing; cross reference; shorthand; photocopier; neon sign.
Checked and avoided (already banked): subrogation, proximate cause,
salvage (inside subrogation item), gilt-edged, insider trading,
manifest, freight forwarder, cold storage, teller/pay-in slip, WTO,
passbook-adjacent items, stevedore (option-only - kept as concept
dropped for space), employer's liability, share certificate face
value (= par value), OFN, ADP, marketing board, marketing channel
items, statutory corporation, e-mail contract copy, marine insurance,
remittance letter (circular letter option-only), debenture families,
bonus issue, trade association, trust, merger, takeover, holding
company, subsidiary, del credere, factor, berth, port dues, dividend
yield, final dividend (R44 interim item), groupage (freight
forwarder/consolidator item covers the agent).

    python3 scripts/build_neco_batch223.py -> content/batch_223_waec_commerce9.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_INS = "Insurance"
T_INSP = "Insurance Principles and Cover"
T_BSE = "Banking and the Stock Exchange"
T_CM = "Capital Markets"
T_BF = "Banking and Finance"
T_TD = "Trade Procedures and Documents"
T_TDP = "Trade Documents and Payments"
T_TL = "Transport and Logistics"
T_BU = "Business Units"
T_BEC = "Business Environment and Communication"
T_ADV = "Advertising"

PASSAGES = []
PQ = []

Q = [
    (T_INSP, "Hard", "A tailor keeps tins of petrol in his shop although his insurance policy forbids it. The stored petrol is regarded in insurance as a",
     "hazard", "premium",
     "benefit", "bond", "A",
     "It raises the chance that fire will strike."),
    (T_INS, "Easy", "The person named in a life insurance policy to receive the money when the insured person dies is the",
     "beneficiary", "benefactor",
     "guarantor", "broker", "A",
     "The payout is his when the policy matures in death."),
    (T_BSE, "Hard", "A dealer buys shares in Lagos in the morning and sells the same shares the same day in another market where the price is higher, gaining from the price difference. This practice is",
     "arbitrage", "arson trade",
     "amortisation", "arrestment", "A",
     "Two prices, one quick profit."),
    (T_BSE, "Medium", "Shares of large, old and financially sound companies, known for steady dividends and safety, are nicknamed",
     "blue chips", "white elephants",
     "red herring", "green belts", "A",
     "The safest names on the exchange."),
    (T_CM, "Hard", "A flour miller sells wheat forward at a fixed price while the wheat is still growing, so that a fall in price before harvest cannot ruin him. This protective dealing is",
     "hedging", "hoarding",
     "haggling", "insider trading", "A",
     "The deal today shields him from tomorrow."),
    (T_BSE, "Hard", "A speculator on the stock exchange who has promised to buy shares but cannot raise the money when settlement is due, and so fails, is called a",
     "lame duck", "bull",
     "stag", "bear", "A",
     "He waddles out of the market wounded."),
    (T_CM, "Medium", "The document, like a cheque, which a company sends to a shareholder to pay him his dividend is a",
     "dividend warrant", "treasury bill",
     "share warrant", "credit note", "A",
     "He takes it to the bank and is paid."),
    (T_BF, "Easy", "The steel drawer fitted into a bank's outer wall, into which a trader can drop his money bag after banking hours, is the",
     "night safe", "safe deposit box",
     "strong room", "cash office", "A",
     "The bank is shut, but the slot still receives."),
    (T_TD, "Easy", "The small part of a cheque left in the cheque book after the cheque is torn out, on which the payment is recorded, is the",
     "counterfoil", "cover note",
     "credit slip", "crossed leaf", "A",
     "It stays behind as the drawer's own record."),
    (T_BF, "Medium", "The small book in which a savings-customer's deposits and withdrawals are written and stamped each time he visits the bank is the",
     "passbook", "textbook",
     "cheque book", "passenger book", "A",
     "The bank and the customer each see the story."),
    (T_TDP, "Medium", "Alhaji sends forty bags of cement by road to his customer in Kaduna, and the customer is to pay after receiving them. The person to whom the goods are sent is the",
     "consignee", "consignor",
     "consul", "carrier only", "A",
     "The goods travel to him, not from him."),
    (T_TL, "Hard", "Where big ships cannot berth close to the quay, goods are carried to and from them in small flat-bottomed boats. The service is called",
     "lighterage", "towage",
     "stevedoring", "pilotage", "A",
     "Small boats bridge ship and shore."),
    (T_BU, "Easy", "The smallest number of members that must be present at a meeting before any business done there is valid is the",
     "quorum", "quota",
     "question time", "quarter day", "A",
     "Without that number the meeting cannot decide."),
    (T_BU, "Medium", "A shareholder who cannot attend the company's annual meeting fills a form authorising another member to attend and vote in his place. The authorised person is a",
     "proxy", "promoter",
     "prospector", "proxy of court", "A",
     "He carries the absent member's vote."),
    (T_BU, "Medium", "When votes at a shareholders' meeting are equal for and against a motion, the chairman gives a second and deciding vote. This vote is his",
     "casting vote", "veto of state",
     "open vote", "reserved vote", "A",
     "It breaks the tie at the table."),
    (T_BU, "Medium", "The one-off meeting which a public limited company must hold shortly after it is permitted to commence business is the",
     "statutory meeting", "statistical meeting",
     "annual meeting", "extraordinary meeting", "A",
     "The law itself requires it once."),
    (T_BU, "Medium", "A meeting called between annual meetings because an urgent matter, such as removing a director, cannot wait for the next AGM, is an",
     "extraordinary general meeting", "emergency welfare meeting",
     "ordinary weekly meeting", "executive session of staff", "A",
     "Business too urgent to keep for a year."),
    (T_BU, "Medium", "The officer of a company, appointed by the directors, who keeps the company's records, sends out notices of meetings and files statutory returns is the",
     "company secretary", "company doctor",
     "registrar of trade", "chief accountant", "A",
     "The company's memory and its messenger."),
    (T_BEC, "Easy", "The list of items of business, arranged in the order in which they will be discussed, that members receive before a meeting, is the",
     "agenda", "adjective",
     "appendix", "abstract", "A",
     "It tells the meeting where to begin and end."),
    (T_BEC, "Medium", "A filing system in which folders lie flat in a drawer, one upon another, so that the papers are stored in piles rather than on edge, is",
     "lateral filing", "vertical filing",
     "wire filing", "box filing", "A",
     "The files sleep in stacks inside the drawer."),
    (T_BEC, "Medium", "The guide, alphabetical or numerical, kept so that any needed file in the cabinet can be located quickly, is called",
     "indexing", "indenting",
     "invoicing", "insuring", "A",
     "Follow the guide and the file is found."),
    (T_BEC, "Medium", "A clerk files Mr Okoro's papers under 'Okoro' and places a card under 'Chukwu' saying 'see Okoro'. The card he has placed is a",
     "cross reference", "crossed cheque",
     "carbon copy", "covering letter", "A",
     "It points from one name to another."),
    (T_BEC, "Easy", "The system of rapid writing in special signs and shortened strokes, used by clerks and secretaries to record speech as it is spoken, is",
     "shorthand", "longhand",
     "signboard", "ship manifest", "A",
     "The pen keeps pace with the speaker."),
    (T_BEC, "Easy", "The office machine that makes exact paper copies of an existing document, page by page, at the touch of a button, is the",
     "photocopier", "dictaphone",
     "franking machine", "folding machine", "A",
     "One page in, many identical pages out."),
    (T_ADV, "Easy", "Advertising signs made of glass tubes that glow with coloured light at night, common above shops and bars, are",
     "neon signs", "kiosk marks",
     "rubber stamps", "road bumps", "A",
     "The gas in the tube glows when switched on."),
]

build_batch(
    S,
    "batch_223_waec_commerce9.json",
    "223",
    "WAEC Commerce round 9 (R45 top-up): hazard; beneficiary; "
    "arbitrage; blue chip; hedging; lame duck; dividend warrant; "
    "night safe; counterfoil; passbook; consignee; lighterage; "
    "quorum; proxy; casting vote; statutory meeting; extraordinary "
    "general meeting; company secretary; agenda; lateral filing; "
    "indexing; cross reference; shorthand; photocopier; neon sign. "
    "Scanned against the whole Commerce pool (JAMB, WAEC and NECO "
    "stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
