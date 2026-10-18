"""Batch 088 - NECO Commerce round 2 (NECO lift, Round 18).

NECO Commerce objective draws 60 items; the bank stood at 74. This lift adds
fresh items - retail types (itinerant, supermarket, department store, chain,
mail order), wholesale functions, trade documents new to the bank (invoice,
receipt, proforma, debit note, statement, indent, letter of credit, bill of
entry), banking (overdraft, bank draft, fixed deposit, exchange rate),
insurance types (third-party, premium, reinsurance, actuary), units
(prospectus, consumer cooperative, merger), FOB/CIF and invisible exports.
Scanned against NECO round 1, the WAEC twin and the JAMB Commerce banks.

    python3 scripts/build_neco_batch88.py -> content/batch_088_neco_commerce2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_RET = "Retailing and Wholesaling"
T_DOC = "Trade Documents"
T_BANK = "Banking Services"
T_INS = "Insurance"
T_UNIT = "Business Units"
T_SCOPE = "Meaning and Scope of Commerce"
T_TOUR = "Tourism"
T_ADV = "Advertising"
T_TRADE = "Trade"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- retailing
    (T_RET, "Easy", "Traders who carry their wares from place to place, in buses and along streets, are",
     "itinerant traders", "department stores", "multiple shops", "mail-order houses", "A",
     "They move to meet the buyers."),
    (T_RET, "Easy", "A large self-service store selling food and household goods is a",
     "supermarket", "kiosk", "market stall", "warehouse", "A",
     "Customers serve themselves at shelves."),
    (T_RET, "Medium", "A big shop where many product lines are sold, each in its own section under one roof, is a",
     "department store", "single-line shop", "hawker's cart", "tied shop", "A",
     "Each department handles one line."),
    (T_RET, "Medium", "Several retail shops under one ownership, selling similar goods at uniform prices, are",
     "chain stores", "market associations", "independent retailers", "cooperative farms", "A",
     "One owner, many branches, one price list."),
    (T_RET, "Medium", "Selling through the post, where goods are sent to buyers who ordered from a catalogue, is",
     "mail-order business", "hire purchase", "barter trade", "entrepot trade", "A",
     "The catalogue does the shop's work."),
    (T_RET, "Medium", "By storing large stocks, the wholesaler helps the manufacturer to keep producing",
     "steadily through the year", "only at festival times", "without any profit", "without paying wages", "A",
     "The warehouse absorbs output swings."),
    # ---------------------------------------------------------------- documents
    (T_DOC, "Easy", "The document a seller sends with goods, showing quantities and prices charged, is the",
     "invoice", "receipt", "way bill", "consignment note", "A",
     "It itemises the goods and costs."),
    (T_DOC, "Easy", "The document that proves a payment has actually been made is the",
     "receipt", "invoice", "quotation", "catalogue", "A",
     "It acknowledges money received."),
    (T_DOC, "Hard", "A paper that resembles a bill but only quotes prices before the buyer has decided is a",
     "proforma invoice", "credit note", "debit note", "statement of account", "A",
     "It quotes prices for a would-be sale."),
    (T_DOC, "Hard", "To correct an undercharge on an invoice already sent, the seller issues a",
     "debit note", "credit note", "receipt", "cheque", "A",
     "It debits the balance still owing."),
    (T_DOC, "Medium", "The periodic summary of transactions sent by a trader to a credit customer is the",
     "statement of account", "proforma invoice", "bill of lading", "consignment note", "A",
     "It lists invoices, payments and balance."),
    (T_DOC, "Hard", "An order placed with a foreign supplier through an agent, for goods to be shipped, is called an",
     "indent", "invoice", "estimate", "tender", "A",
     "The agent handles the foreign order."),
    (T_DOC, "Hard", "The bank document promising to pay an exporter once stated conditions are met is a",
     "letter of credit", "bill of exchange", "postal order", "standing order", "A",
     "The bank's promise secures the trade."),
    (T_DOC, "Hard", "Imported goods are released from the port after the importer lodges the",
     "bill of entry", "delivery note", "credit note", "certificate of origin", "A",
     "Customs clears against this bill."),
    # ---------------------------------------------------------------- banking
    (T_BANK, "Medium", "An arrangement allowing a current-account holder to draw more than his balance is an",
     "overdraft", "fixed deposit", "standing order", "savings account", "A",
     "The bank lends the short shortfall."),
    (T_BANK, "Medium", "A cheque drawn by a bank on itself, widely accepted for large payments, is a",
     "bank draft", "post-dated cheque", "stale cheque", "traveller's letter", "A",
     "The bank's own name backs it."),
    (T_BANK, "Medium", "Money placed in a fixed deposit account",
     "stays locked until maturity", "earns no interest at all", "is used for daily payments", "belongs to the cashier", "A",
     "The lock-in earns the higher rate."),
    (T_BANK, "Easy", "The price of one country's money in terms of another's is the",
     "exchange rate", "bank rate", "inflation rate", "interest yield", "A",
     "It prices the naira against the dollar."),
    (T_BANK, "Easy", "During a period of inflation, the same amount of money buys",
     "fewer goods than before", "more goods than before", "exactly the same goods", "only imported goods", "A",
     "Rising prices shrink money's power."),
    # ---------------------------------------------------------------- insurance
    (T_INS, "Medium", "By law, every vehicle owner in Nigeria must hold at least",
     "third-party motor insurance", "comprehensive cover", "life assurance", "fire insurance", "A",
     "Third-party cover protects victims."),
    (T_INS, "Easy", "The regular payment a policyholder makes to keep cover active is the",
     "premium", "claim", "bonus", "dividend", "A",
     "Premiums keep the policy alive."),
    (T_INS, "Hard", "When an insurer passes part of a big risk to another insurer, the arrangement is",
     "reinsurance", "double insurance", "co-insurance of lives", "underwriting", "A",
     "The risk is shared insurer to insurer."),
    (T_INS, "Hard", "The insurance specialist who works out risks and fixes premiums is the",
     "actuary", "assessor", "broker", "loss adjuster", "A",
     "Actuaries price the risk."),
    # ---------------------------------------------------------------- business units
    (T_UNIT, "Hard", "When a company wants the public to buy its new shares, it publishes the",
     "prospectus", "memorandum of association", "articles of association", "share warrant", "A",
     "It advertises the offer for sale."),
    (T_UNIT, "Medium", "A cooperative society formed by customers who buy their goods together is a",
     "consumer cooperative", "producer cooperative", "credit union", "workers' cooperative", "A",
     "Members own the shop they buy from."),
    (T_UNIT, "Hard", "When two firms combine and a completely new firm is formed, the combination is a",
     "merger", "takeover", "partnership", "consortium", "A",
     "Two old names become one new one."),
    # ---------------------------------------------------------------- scope
    (T_SCOPE, "Medium", "Commerce is mainly concerned with the",
     "distribution of goods", "manufacture of goods", "extraction of minerals", "printing of money", "A",
     "Trade and its aids move the goods."),
    (T_SCOPE, "Easy", "Turning raw materials into finished goods is the work of",
     "manufacturing industries", "commercial occupations", "extractive industries", "service trades only", "A",
     "Factories transform the inputs."),
    (T_SCOPE, "Easy", "Mining, fishing and quarrying belong to which group of occupations?",
     "extractive", "constructive", "commercial", "manufacturing", "A",
     "They take wealth from nature."),
    # ---------------------------------------------------------------- tourism
    (T_TOUR, "Easy", "Money spent by foreign tourists is for Nigeria a source of",
     "foreign exchange earnings", "import duties", "income tax refunds", "local levies", "A",
     "Visitors bring hard currency."),
    (T_TOUR, "Easy", "The Obudu Ranch and the Yankari springs are examples of Nigeria's",
     "tourist attractions", "mining sites", "industrial estates", "border posts", "A",
     "Visitors travel to enjoy them."),
    # ---------------------------------------------------------------- advertising
    (T_ADV, "Medium", "An advert placed simply to keep an old brand in buyers' memory is",
     "reminder advertising", "informative advertising", "classified advertising", "corporate advertising", "A",
     "It refreshes a familiar name."),
    (T_ADV, "Medium", "An advert that pushes one firm's product by openly attacking rivals' products is",
     "competitive advertising", "reminder advertising", "public service advertising", "recruitment advertising", "A",
     "It fights for the same buyer."),
    (T_ADV, "Easy", "Firms that plan and run advertising campaigns for client companies are",
     "advertising agencies", "trade unions", "clearing agents", "insurance brokers", "A",
     "They create the campaigns for hire."),
    # ---------------------------------------------------------------- trade
    (T_TRADE, "Hard", "In foreign trade, FOB (free on board) means the seller pays all costs until the goods are",
     "loaded on the ship", "delivered to the buyer's shop", "cleared at customs", "insured to the warehouse", "A",
     "Buyer's costs begin on board."),
    (T_TRADE, "Hard", "A CIF price includes",
     "cost, insurance and freight", "cost only at the factory gate", "customs duty and local delivery", "commission for the buying agent", "A",
     "Three charges ride inside one price."),
    (T_TRADE, "Medium", "Earnings from shipping and insurance services sold to foreigners are Nigeria's",
     "invisible exports", "visible exports", "re-exports", "barter goods", "A",
     "Services exported earn without goods."),
    (T_TRADE, "Medium", "The warehouse owned and used by a single firm for its own goods is a",
     "private warehouse", "public warehouse", "bonded warehouse", "cold store", "A",
     "It serves only its owner."),
    (T_TRADE, "Easy", "Grain silos are built to store",
     "cereals in bulk", "frozen fish", "petroleum products", "motor vehicles", "A",
     "Silos hold dry grain in quantity."),
]

build_batch(
    S,
    "batch_088_neco_commerce2.json",
    "088",
    "NECO Commerce round 2 (Round 18 lift): retail types (itinerant traders, "
    "supermarket, department store, chain stores, mail order), wholesale "
    "steadiness, documents new to the bank (invoice, receipt, proforma, "
    "debit note, statement of account, indent, letter of credit, bill of "
    "entry), banking (overdraft, bank draft, fixed deposit, exchange rate, "
    "inflation), insurance (compulsory third-party, premium, reinsurance, "
    "actuary), units (prospectus, consumer cooperative, merger), scope "
    "(distribution, manufacturing, extractive), tourism, advertising "
    "(reminder, competitive, agencies), trade (FOB, CIF, invisible exports), "
    "private warehouse, grain silos. Scanned against NECO round 1, the WAEC "
    "twin and the large JAMB Commerce banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
