"""Batch 154 - WAEC Commerce round 6 (WAEC top-up, R29).

Grows WAEC Commerce from 187 toward ~225 with angles not yet in the
bank: mergers and takeovers, franchising, chain stores, departmental
stores, mail order; itinerant traders and supermarket self-service;
hire purchase, credit cards, documents against acceptance and sight
drafts; charter parties, freight forwarders, clearing and forwarding,
containerisation, pipelines; courier and registered post, postal
orders; unit trusts, bank drafts, overdrafts, collateral; WTO and
ECOWAS protocol, customs unions; life assurance, the average clause,
no-claim bonus, reinsurance, third-party motor; trade associations
and chambers of commerce, social responsibility, retained earnings.
Scanned against WAEC rounds 1-5, NECO Commerce (all rounds) and the
JAMB pool.

    python3 scripts/build_neco_batch154.py -> content/batch_154_waec_commerce6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_UNIT = "Business Combinations and Outlets"
T_TRADE = "Trade Practice and Payments"
T_TRANS = "Transport and Logistics"
T_COM = "Communication and Banking"
T_BLOC = "Trade Blocs and Agreements"
T_INS = "Insurance Further"
T_SOC = "Business in Society"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- units & outlets
    (T_UNIT, "Hard", "When two banks dissolve their separate identities and continue as one new company, the combination is a",
     "merger", "takeover", "cartel", "partnership", "A",
     "Two old names sink into one."),
    (T_UNIT, "Hard", "A company that buys enough shares of another to control its board has effected a",
     "takeover", "merger", "consortium", "trust fund", "A",
     "The smaller firm keeps its name but obeys."),
    (T_UNIT, "Medium", "A businessman who pays royalties to trade under an established trade name operates a",
     "franchise", "cooperative", "partnership", "cartel", "A",
     "He rents the banner, not the business."),
    (T_UNIT, "Medium", "Ten shops in ten towns, one owner, one style, uniform prices: this retail form is",
     "a chain store", "a departmental store", "a mail order house", "a market stall", "A",
     "Same goods, same face, everywhere."),
    (T_UNIT, "Medium", "Under one roof and one management, a store sells groceries, textiles and electronics in separate sections. It is a",
     "departmental store", "chain store", "superette", "hypermarket stall", "A",
     "Many trades share one roof."),
    (T_UNIT, "Hard", "Buying goods from home through a catalogue and receiving them by post is",
     "mail order trading", "hawking", "auctioning", "bartering", "A",
     "The counter travels by post."),
    (T_UNIT, "Medium", "Hawkers and pedlars who move from place to place with their wares are",
     "itinerant traders", "wholesalers", "brokers", "brokers' agents", "A",
     "The shop walks on two legs."),
    (T_UNIT, "Medium", "A supermarket's chief service innovation is",
     "self-service with trolleys", "bargaining at the counter", "home slaughter of beasts", "credit for all buyers", "A",
     "You gather, then you pay."),

    # ------------------------------------------------------------- trade practice
    (T_TRADE, "Hard", "Under hire purchase, ownership of the article passes to the buyer only when",
     "the last instalment is paid", "the first instalment is paid", "goods are delivered", "he signs the form", "A",
     "Use first, own only at the last."),
    (T_TRADE, "Medium", "A credit card holder enjoys goods today by",
     "borrowing against the card", "paying with coupons", "bartering goods", "winning a lottery", "A",
     "The bill waits for month's end."),
    (T_TRADE, "Hard", "Under documents against acceptance, the bank releases shipping documents to the buyer once he",
     "accepts the bill of exchange", "pays in full at sight", "signs the invoice", "rejects the goods", "A",
     "His signature unlocks the papers."),
    (T_TRADE, "Medium", "A sight draft differs from a usance draft because it is payable",
     "on demand", "after ninety days", "only on holidays", "in kind", "A",
     "Present it and count the cash."),

    # ------------------------------------------------------------- transport & logistics
    (T_TRANS, "Hard", "An importer who hires a whole ship for one complete voyage signs a",
     "voyage charter party", "demise charter", "time charter", "bill of sight", "A",
     "One trip, one signed contract."),
    (T_TRANS, "Medium", "The specialist who assembles small consignments from several shippers into one full load is the",
     "freight forwarder", "ship's captain", "harbour master", "bonded clerk", "A",
     "Small parcels ride his one bill."),
    (T_TRANS, "Medium", "At the ports, the agent who completes customs formalities and releases goods for an importer is the",
     "clearing and forwarding agent", "ship chandler", "stevedore", "pilot", "A",
     "His stamp opens the gate."),
    (T_TRANS, "Hard", "Containerisation has cut port costs chiefly by",
     "speeding loading and cutting pilferage", "slowing ship turnaround", "increasing manual handling", "banning insurance", "A",
     "One steel box, many doors saved."),
    (T_TRANS, "Medium", "The mode of transport best suited to moving crude oil overland is",
     "pipeline", "animal haulage", "bicycle courier", "open wagons", "A",
     "The product flows in its own road."),

    # ------------------------------------------------------------- communication & banking
    (T_COM, "Hard", "A trader who must send a signed original document quickly and safely to Kano will likely use a",
     "courier service", "postal order", "billboard", "radio announcement", "A",
     "Door-to-door with a signature."),
    (T_COM, "Medium", "Sending jewellery by post, a sender protects it best through",
     "registered post", "ordinary parcel post", "printed paper rate", "cash on delivery only", "A",
     "The item travels signed for."),
    (T_COM, "Medium", "A person without a bank account can remit money through the post office using a",
     "postal order", "promissory note", "bill of lading", "waybill", "A",
     "Paper money of small value."),
    (T_COM, "Hard", "A fund that pools the savings of many small investors and spreads them across shares is a",
     "unit trust", "treasury bill", "overdraft", "sinking fund", "A",
     "Many little stakes, one basket of many."),
    (T_COM, "Medium", "A trader who wants a payment instrument guaranteed by a bank itself, not by a private drawer, asks for a",
     "bank draft", "post-dated cheque", "promissory note", "IOU", "A",
     "The bank's name stands behind it."),
    (T_COM, "Medium", "A current account allowed to go below its balance up to an agreed limit enjoys an",
     "overdraft", "interest-free grant", "equity injection", "advance dividend", "A",
     "The bank lends into the red."),
    (T_COM, "Hard", "Before granting a large loan, a bank insists on security popularly called",
     "collateral", "commission", "consideration", "consignment", "A",
     "Something valuable stands surety."),

    # ------------------------------------------------------------- trade blocs
    (T_BLOC, "Hard", "The world body charged with promoting free and fair trade among nations is the",
     "WTO", "IMF shipping desk", "OPEC", "INTERPOL", "A",
     "Its rounds lower the walls."),
    (T_BLOC, "Medium", "Under the ECOWAS protocol, a Nigerian trader needs no visa to trade for ninety days in",
     "Ghana", "India", "China", "Brazil", "A",
     "The region is one compound."),
    (T_BLOC, "Hard", "A group of countries imposing one common duty on goods from outsiders forms a",
     "customs union", "free trade area only", "common market only", "monetary zone", "A",
     "One tariff wall, many rooms."),

    # ------------------------------------------------------------- insurance
    (T_INS, "Hard", "Life assurance is NOT a contract of indemnity because human life is",
     "not measurable in money", "insurable twice over", "always rising in value", "covered by the state", "A",
     "No price tag hangs on a person."),
    (T_INS, "Hard", "A warehouse worth N100,000 is insured for only N60,000. If fire causes N40,000 damage, the average clause pays",
     "N24,000", "N40,000", "N60,000", "N100,000", "A",
     "Cover taken bears the loss paid.", "24000"),
    (T_INS, "Medium", "The no-claim bonus rewards a policyholder who",
     "makes no claim in a year", "pays premiums late", "lends the car out", "changes address often", "A",
     "Careful driving earns discount."),
    (T_INS, "Hard", "An insurance company that passes part of a big risk to another insurer has taken out",
     "reinsurance", "double insurance", "self-insurance", "co-insurance fraud", "A",
     "The risk is shared overhead."),
    (T_INS, "Medium", "In Nigeria, the minimum motor insurance a car owner must carry is",
     "third party cover", "comprehensive cover", "fire and theft only", "no cover at all", "A",
     "It guards the other road user."),

    # ------------------------------------------------------------- business in society
    (T_SOC, "Medium", "Market women dealing in tomatoes may band together to guard their common trade interests. Such a body is a",
     "trade association", "trade union", "consumer club", "government parastatal", "A",
     "One loud voice for one trade."),
    (T_SOC, "Medium", "In many Nigerian cities, business owners gather under one umbrella body that speaks for commerce itself. That body is the",
     "chamber of commerce", "trade union", "consumers' club", "workers' parliament", "A",
     "Commerce's own parliament."),
    (T_SOC, "Hard", "A firm's social responsibility requires it to care for",
     "community and environment", "only its directors", "only the tax office", "only foreign buyers", "A",
     "The ledger has a social column."),
    (T_SOC, "Medium", "The cheapest source of business capital, involving neither interest nor new shares, is",
     "retained earnings", "bank overdraft", "debenture issue", "rights issue", "A",
     "Yesterday's unspent profit funds tomorrow."),
]

build_batch(
    S,
    "batch_154_waec_commerce6.json",
    "154",
    "WAEC Commerce round 6 (R29 top-up): merger vs takeover, franchise, "
    "chain and departmental stores, mail order, itinerant traders, "
    "supermarket self-service; hire purchase ownership on last "
    "instalment, credit cards, documents against acceptance, sight "
    "draft; voyage charter, freight forwarder, clearing and forwarding "
    "agent, containerisation, pipeline; courier and registered post, "
    "postal order; unit trust, bank draft, overdraft, collateral; WTO, "
    "ECOWAS free movement, customs union; life assurance beyond "
    "indemnity, average clause N24,000, no-claim bonus, reinsurance, "
    "compulsory third party; trade association, chamber of commerce, "
    "social responsibility, retained earnings. Scanned against WAEC "
    "rounds 1-5, NECO Commerce (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
