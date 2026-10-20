"""Batch 126 - NECO Commerce round 4 (NECO top-up, Round 24).

Lifts NECO Commerce from 148 toward ~185 with angles not yet in any
bank: trade fairs and exhibitions, foreign-trade documents (bill of
lading, certificate of origin, letter of credit, indent), ports and
customs, warehouse types, further insurance covers, stock exchange
functions, statutory corporations and joint ventures, transport
economics, modern communication and globalisation. Scanned against NECO
rounds 1-3, WAEC Commerce (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch126.py -> content/batch_126_neco_commerce4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_FAIR = "Trade Fairs and Tourism"
T_DOC = "Documents in Foreign Trade"
T_PORT = "Ports, Customs and Warehouses"
T_INS = "Further Insurance"
T_EXCH = "The Stock Exchange and Business Units"
T_COM = "Transport, Communication and Globalisation"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- fairs and tourism
    (T_FAIR, "Medium", "A trade fair is best described as a periodic exhibition where firms",
     "display goods to win customers", "sell shares to the public", "pay their taxes", "train sailors", "A",
     "The stalls do the talking."),
    (T_FAIR, "Medium", "An advantage of exhibiting at a trade fair is",
     "direct contact with many buyers", "free legal services", "automatic tax exemption", "lifetime monopoly", "A",
     "Handshakes there close deals."),
    (T_FAIR, "Hard", "The Lagos international trade fair complex at Badagry expressway hosts exhibitors",
     "from many countries", "from Lagos State only", "selling only farm tools", "without paying rent", "A",
     "Many nations meet there to trade."),
    (T_FAIR, "Medium", "Tourism earns a country foreign exchange through visitors' spending on",
     "hotels, food and transport", "import duties", "company income tax only", "pension funds", "A",
     "The guest's wallet opens."),
    (T_FAIR, "Hard", "Obudu cattle ranch and Yankari reserve serve chiefly as",
     "tourist destinations", "sea ports", "mints", "stock exchanges", "A",
     "Visitors ride and watch game."),

    # ------------------------------------------------------------- documents
    (T_DOC, "Hard", "Which shipping paper is at once a receipt, a contract and a title to the goods?",
     "bill of lading", "invoice", "cheque", "way bill only", "A",
     "Three roles in one paper."),
    (T_DOC, "Hard", "A certificate of origin states",
     "where goods were manufactured", "the shipper's profit", "the crew list", "the import tariff only", "A",
     "Customs reads it for preference."),
    (T_DOC, "Medium", "A letter of credit from a bank promises the exporter that payment will be made if documents are presented; it is opened by the",
     "importer's bank", "exporter's bank only", "port authority", "insurance company", "A",
     "The buyer's bank stands between."),
    (T_DOC, "Hard", "An indent is a document in which an agent is",
     "instructed to buy goods abroad", "dismissed from service", "granted a pension", "licensed to insure ships", "A",
     "The order travels with authority."),
    (T_DOC, "Medium", "A consular invoice, stamped by an embassy, chiefly helps the importing country to",
     "verify the value of goods", "entertain its diplomats", "print new currency", "hire sailors", "A",
     "Duties hinge on the value."),
    (T_DOC, "Hard", "The document listing goods in a consignment packed for shipment is the",
     "packing list", "proforma invoice only", "credit note", "debit note", "A",
     "The buyer checks the cartons."),

    # ------------------------------------------------------------- ports and warehouses
    (T_PORT, "Medium", "Grain silos, cold rooms and bonded warehouses are all types of",
     "warehouses", "markets", "banks", "ports", "A",
     "Goods rest under their roofs."),
    (T_PORT, "Medium", "A public warehouse serves",
     "the public for a fee", "one family alone", "only the government", "only ships' crews", "A",
     "Space is rented to all comers."),
    (T_PORT, "Hard", "Berths, quays and cranes belong to the equipment of a",
     "seaport", "silo", "mint", "post office", "A",
     "Ships tie up alongside them."),
    (T_PORT, "Medium", "The Nigerian Ports Authority chiefly oversees",
     "harbour operations", "airport runways", "railway lines", "customs tariffs only", "A",
     "Cargo handling at the quays is its charge."),
    (T_PORT, "Hard", "Duty payable on goods is computed largely on their",
     "value as declared and verified", "colour", "weight of the ship", "captain's age", "A",
     "The customs assessor works it."),
    (T_PORT, "Medium", "A transit warehouse near a border temporarily holds goods",
     "awaiting onward movement", "for sale to tourists", "for ever", "for the navy", "A",
     "The goods simply pass through."),

    # ------------------------------------------------------------- insurance
    (T_INS, "Medium", "Motor vehicle third-party insurance covers injury or damage to",
     "other road users", "the driver's own car", "the driver's family only", "the insurer", "A",
     "The law demands at least this."),
    (T_INS, "Medium", "Fidelity guarantee insurance protects an employer against",
     "staff dishonesty", "fire at home", "motor accidents", "bad weather", "A",
     "The trusted clerk's fall is covered."),
    (T_INS, "Hard", "Burglary insurance typically pays for loss of property following",
     "breaking and entering", "flooding", "war", "wear and tear", "A",
     "Signs of violent entry are required."),
    (T_INS, "Hard", "Employer's liability insurance covers the employer against claims arising from",
     "injuries to workers at work", "customers' bad debts", "product fashion changes", "share price falls", "A",
     "The workshop's risks shift."),
    (T_INS, "Medium", "Reinsurance means the insurer",
     "passes part of the risk on", "cancels the policy at once", "doubles the premium charged", "insures the police force", "A",
     "No insurer carries a giant alone."),

    # ------------------------------------------------------------- exchange and units
    (T_EXCH, "Medium", "Besides raising capital, the stock exchange helps government and companies to",
     "trade existing securities", "print currency notes", "collect sales tax", "run the ports", "A",
     "Second-hand shares find buyers."),
    (T_EXCH, "Hard", "Listing requirements on the exchange chiefly protect the",
     "investing public", "cleaners of the floor", "jobbers only", "importers of paper", "A",
     "Full disclosure is the price of entry."),
    (T_EXCH, "Hard", "A statutory corporation is created by",
     "an Act of parliament", "a private contract", "a court summons", "a trade union resolution", "A",
     "The law births it for public service."),
    (T_EXCH, "Medium", "A joint venture is formed when two or more firms",
     "combine for one project", "merge permanently", "buy up all rivals", "close down together", "A",
     "Partners for a season, not forever."),
    (T_EXCH, "Medium", "Members of a thrift cooperative chiefly use it to",
     "save and obtain loans easily", "import luxury cars", "avoid all taxes", "elect senators", "A",
     "Their savings fund their needs."),

    # ------------------------------------------------------------- transport, communication, globalisation
    (T_COM, "Hard", "Rail transport suits bulky goods like coal and cement because it",
     "hauls bulk cheaply", "is the fastest means", "needs no tracks at all", "delivers to each door", "A",
     "The steel road hauls cheaply."),
    (T_COM, "Medium", "Pipelines are best reserved for",
     "oil and gas", "furniture", "fresh bread", "live cattle", "A",
     "Fluids flow in them, solids jam."),
    (T_COM, "Medium", "Email has largely replaced business letters because it is",
     "fast and cheap", "more fragrant", "legally binding always", "handwritten", "A",
     "The e-inbox never closes."),
    (T_COM, "Medium", "A memorandum within an office usually",
     "records internal instructions", "carries goods to the port", "insures a ship", "pays a dividend", "A",
     "Internal mail, brief and clear."),
    (T_COM, "Hard", "Globalisation refers to the growing integration of world economies through",
     "trade and capital flows", "one world government", "closed borders", " abolishing money", "A",
     "Distance shrinks for world markets."),
    (T_COM, "Hard", "A multinational company's danger to host nations includes",
     "profit repatriation abroad", "excess local employment", "overpaying taxes twice", "building too many schools", "A",
     "The earnings board the plane."),
    (T_COM, "Medium", "Teleconferencing saves business travellers chiefly the cost of",
     "journeys and hotels", "office rent", "printing", "insurance", "A",
     "The screen replaces the flight."),
]

build_batch(
    S,
    "batch_126_neco_commerce4.json",
    "126",
    "NECO Commerce round 4 (Round 24 top-up): trade fairs and their "
    "value, Lagos international trade fair, tourism's foreign exchange, "
    "Obudu and Yankari, bill of lading's three roles, certificate of "
    "origin, letters of credit, indents, consular invoices, packing "
    "lists, warehouse types (public, bonded, transit, silos, cold "
    "rooms), berths and the NPA, duty computation, third-party motor "
    "cover, fidelity guarantee, burglary and employer's liability "
    "insurance, reinsurance, stock exchange listing, statutory "
    "corporations, joint ventures, cooperative thrift societies, rail "
    "and pipeline economics, email and memoranda, globalisation, "
    "multinationals' repatriation risk and teleconferencing. Scanned "
    "against NECO rounds 1-3, WAEC Commerce (all rounds) and the JAMB "
    "pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
