"""Batch 080 - WAEC Commerce, Paper 1 Objective round 1.

WASSCE Commerce Paper 1 (Objective) is a 50-item paper (50 min; official 2026
second-series timetable, paper 1031). This batch covers the WASSCE commerce
syllabus with FRESH angles and phrasings - Nigerian agencies (CBN, NDIC, SON,
NAFDAC, ARCON, Nigerian Exchange), document and payment scenarios (Kano
wholesaler to Aba, POS at market stalls, dishonoured cheques), insurance
principles restated as stories, and a new e-commerce topic (payment
gateways, OTP security, drop-shipping) - because the near-dup scan checks
every item against the JAMB, WAEC and NECO banks, including the large JAMB
Commerce banks (batches 003, 030-031) and our 74-item NECO Commerce bank.

    python3 scripts/build_neco_batch80.py -> content/batch_080_waec_commerce.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_TRADE = "Home and Foreign Trade"
T_AID = "Aids to Trade"
T_UNIT = "Business Units"
T_DOC = "Trade Documents and Payments"
T_BANK = "Banking and the Stock Exchange"
T_INS = "Insurance"
T_CONS = "Consumer Protection"
T_ECOM = "E-Commerce and Modern Trade"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- trade
    (T_TRADE, "Easy", "A Kano wholesaler sells cloth to a trader in Aba. This transaction is",
     "home trade", "foreign trade", "entrepot trade", "barter trade", "A",
     "Both parties trade within Nigeria."),
    (T_TRADE, "Easy", "The sale of crude oil by Nigeria to India is an example of",
     "export trade", "import trade", "home trade", "entrepot trade", "A",
     "Goods leaving the country are exports."),
    (T_TRADE, "Medium", "A dealer brings in watches from Japan and ships them out to Ghana unchanged. This is",
     "entrepot trade", "bilateral trade", "counter trade", "barter trade", "A",
     "Re-exporting untouched is entrepot."),
    (T_TRADE, "Medium", "Visible trade differs from invisible trade because visible trade involves",
     "physical goods", "services only", "banking and insurance", "tourism earnings", "A",
     "Goods you can see cross the borders."),
    (T_TRADE, "Medium", "The gap between a nation's merchandise exports and imports is its",
     "balance of trade", "balance of payment", "national budget", "trade cycle", "A",
     "It compares goods with goods alone."),
    (T_TRADE, "Easy", "Import duties are taxes charged on",
     "goods entering a country", "goods leaving a country", "services rendered abroad", "shares traded at the exchange", "A",
     "Customs levies them at the ports."),
    (T_TRADE, "Medium", "Under ECOWAS trade rules, goods moving from Nigeria to Ghana enjoy",
     "reduced tariff barriers", "complete tax exemption on oil", "bans on all imports", "fixed exchange rates", "A",
     "The community lowers internal tariffs."),
    (T_TRADE, "Medium", "A complete legal prohibition of trade in a particular good is",
     "an embargo", "a tariff", "a quota", "a subsidy", "A",
     "Embargo stops the trade outright."),
    # ---------------------------------------------------------------- aids to trade
    (T_AID, "Medium", "The aid to trade that bridges the time between production and consumption is",
     "warehousing", "banking", "insurance", "advertising", "A",
     "Stores hold goods until demand comes."),
    (T_AID, "Easy", "Refrigerated warehouses serve mainly to",
     "keep perishables fresh", "raise their market price", "reduce the goods' weight", "insure them against fire", "A",
     "Cold chains slow down spoilage."),
    (T_AID, "Easy", "Bulky liquids like petrol move best by",
     "pipeline", "aircraft", "head porterage", "bicycles", "A",
     "Pipes pump fuels over long miles."),
    (T_AID, "Medium", "The advertising medium with the widest rural reach in Nigeria is",
     "radio", "cinema", "billboards", "brochures", "A",
     "Radio crosses language and distance."),
    (T_AID, "Medium", "Advertising designed to give facts about a new product is",
     "informative advertising", "competitive advertising", "deceptive advertising", "mass advertising", "A",
     "It informs before it persuades."),
    (T_AID, "Hard", "The postal service that carries compensation for loss or damage is",
     "registered mail", "ordinary mail", "post restante", "cash on delivery", "A",
     "Registration makes the post liable."),
    (T_AID, "Easy", "Express courier and EMS services belong to which aid to trade?",
     "communication", "transportation", "insurance", "banking", "A",
     "They speed up messages and parcels."),
    (T_AID, "Medium", "Public bonded warehouses allow importers to",
     "store goods before duty", "sell shares to the public", "insure goods against theft only", "avoid all customs checks", "A",
     "Duty waits until goods leave the bond."),
    # ---------------------------------------------------------------- business units
    (T_UNIT, "Easy", "Ngozi runs her boutique alone, taking all the profit and all the loss. Her business is a",
     "sole proprietorship", "partnership", "private company", "cooperative", "A",
     "One owner carries the whole risk."),
    (T_UNIT, "Medium", "The maximum number of partners allowed in an ordinary trading partnership is",
     "20", "2", "50", "100", "A",
     "Beyond twenty, a company is required."),
    (T_UNIT, "Hard", "Investors wishing to know a company's legal objects and powers will read its",
     "memorandum of association", "articles of association", "prospectus", "director's report", "A",
     "The memorandum states the objects."),
    (T_UNIT, "Hard", "The certificate that legally brings a company into existence is the",
     "certificate of incorporation", "certificate of origin", "certificate of registration", "trading certificate", "A",
     "CAC issues it after the filing."),
    (T_UNIT, "Medium", "The liability of a shareholder in a limited company is limited to",
     "the amount unpaid on shares", "personal houses and cars", "the company's total debt", "directors' personal guarantees", "A",
     "Shares cap what he can lose."),
    (T_UNIT, "Medium", "A cooperative society shares its yearly surplus to members as",
     "patronage dividend", "interest on capital", "directors' fees", "founders' shares", "A",
     "Reward follows how much you bought."),
    (T_UNIT, "Medium", "A public corporation is established mainly to",
     "provide essential services", "maximise the owners' profit", "trade in company shares", "grant loans to farmers", "A",
     "Service, not gain, is its goal."),
    (T_UNIT, "Hard", "A partner who contributes capital but takes no active part in management is",
     "a sleeping partner", "an active partner", "a general partner", "a nominal partner", "A",
     "His money works, not his hands."),
    # ---------------------------------------------------------------- documents and payments
    (T_DOC, "Hard", "An importer must present the sea document of title before collecting his goods. It is the",
     "bill of lading", "invoice", "consular invoice", "way bill", "A",
     "The bill surrenders the cargo."),
    (T_DOC, "Medium", "A transport document that lists goods aboard but is not a document of title is the",
     "way bill", "bill of lading", "promissory note", "bill of exchange", "A",
     "It accompanies, not transfers, goods."),
    (T_DOC, "Hard", "A cheque crossed with two lines and 'not negotiable' may only be paid into",
     "a bank account", "hand cash over the counter", "a bearer's pocket", "a post office box", "A",
     "Crossing forces it into an account."),
    (T_DOC, "Medium", "A postal order is used mainly to",
     "send money through the post", "insure parcels in transit", "book cargo space early", "register a business name", "A",
     "The post office pays the named payee."),
    (T_DOC, "Medium", "The document that orders a bank to pay a stated sum from a customer's account is",
     "a cheque", "a receipt", "an invoice", "a promissory note", "A",
     "The drawer orders, the bank pays."),
    (T_DOC, "Hard", "A promissory note differs from a bill of exchange because it is",
     "a promise, not an order", "an order to a bank", "a receipt for money paid", "a demand for rent owed", "A",
     "The maker promises to pay himself."),
    (T_DOC, "Medium", "A bank returns Kola's cheque marked 'insufficient funds'. The cheque has been",
     "dishonoured", "crossed", "stale-dated", "post-dated", "A",
     "The bank refused to pay it."),
    (T_DOC, "Easy", "The payment terminal now common at Nigerian market stalls is",
     "the POS machine", "the telegraph", "the postal order", "the promissory note", "A",
     "Cards and transfers feed it."),
    # ---------------------------------------------------------------- banking and stock exchange
    (T_BANK, "Easy", "The banker and financial adviser to the Federal Government is",
     "the Central Bank", "First Bank", "Bank of Industry", "NEXIM Bank", "A",
     "The CBN keeps government accounts."),
    (T_BANK, "Medium", "The bank rate is the rate at which the Central Bank",
     "lends to commercial banks", "pays savers' interest", "charges school fee loans", "buys foreign bureaux", "A",
     "It is the lender's own price."),
    (T_BANK, "Medium", "Which account allows payment to third parties by cheque?",
     "current account", "savings account", "fixed deposit", "domiciliary account", "A",
     "Cheques ride on current accounts."),
    (T_BANK, "Medium", "A standing order is a customer's instruction to the bank to",
     "pay a fixed sum regularly", "freeze the account at will", "lend against collateral", "issue a new cheque book", "A",
     "Rent and school fees ride on it."),
    (T_BANK, "Easy", "Credit transfer by phone is possible today through",
     "mobile banking apps", "telegrams", "money orders", "bills of lading", "A",
     "USSD and apps move money fast."),
    (T_BANK, "Medium", "The agency that insures the deposits of bank customers in Nigeria is",
     "NDIC", "NAFDAC", "SON", "SEC", "A",
     "The deposit corporation stands behind savers."),
    (T_BANK, "Medium", "Domiciliary accounts are kept in",
     "foreign currency", "cowries and shells", "gold bars only", "shares and debentures", "A",
     "Dollars, pounds or euros live in them."),
    (T_BANK, "Hard", "Shares of quoted companies are bought and sold on the",
     "Nigerian Exchange", "CBN auction floor", "NDIC counter", "CAC registry", "A",
     "Stockbrokers trade there daily."),
    # ---------------------------------------------------------------- insurance
    (T_INS, "Hard", "After the fire, the insurer paid exactly the loss suffered, not a kobo more. The principle applied is",
     "indemnity", "subrogation", "contribution", "good faith", "A",
     "The insured is restored, not enriched."),
    (T_INS, "Hard", "Insurable interest requires that the insured",
     "stands to lose if the risk occurs", "owns a fast car in Lagos", "pays premiums strictly in cash", "holds a bank account somewhere", "A",
     "No loss, no cover, no claim."),
    (T_INS, "Medium", "Utmost good faith obliges an applicant to",
     "disclose all material facts", "hide his past claims", "exaggerate the value insured", "insure other people's goods", "A",
     "Both sides show full cards."),
    (T_INS, "Hard", "Subrogation allows the insurer, after paying, to",
     "claim the salvage that remains", "cancel the policy at will", "double the next premium", "sue the insured for fraud", "A",
     "He steps into the insured's shoes."),
    (T_INS, "Medium", "Life business is called assurance because death is",
     "certain to occur", "avoidable by care", "rare in Nigeria", "covered by the state", "A",
     "What is certain is assured."),
    (T_INS, "Easy", "When cover is granted, the printed contract the insurer hands over is the",
     "policy", "prospectus", "way bill", "debenture", "A",
     "The policy is the contract itself."),
    (T_INS, "Hard", "Contribution applies where the same risk is",
     "insured by more than one policy", "left completely uncovered", "insured by the state", "caused by an act of war", "A",
     "Insurers share the loss fairly."),
    # ---------------------------------------------------------------- consumer protection
    (T_CONS, "Medium", "The agency that fixes standards for manufactured products in Nigeria is",
     "SON", "NAFDAC", "CAC", "NDIC", "A",
     "The standards organisation stamps quality."),
    (T_CONS, "Easy", "NAFDAC regulates mainly",
     "food and drugs", "airlines and ports", "banks and insurance", "stock broking firms", "A",
     "Its number guards what we swallow."),
    (T_CONS, "Medium", "A buyer who discovers hidden defects in goods may lawfully demand",
     "repair or replacement", "a free gift voucher", "double his money back", "nothing at all", "A",
     "The sale of goods law backs him."),
    (T_CONS, "Medium", "Caveat emptor places the burden of careful buying on",
     "the buyer", "the seller", "the manufacturer", "the government", "A",
     "Let the buyer beware, says the law."),
    (T_CONS, "Medium", "The Consumer Protection Council exists mainly to",
     "defend consumer rights", "print currency notes", "license commercial banks", "set postal rates", "A",
     "It hears the buyer's complaints."),
    (T_CONS, "Hard", "The body that vets and regulates advertisements in Nigeria is",
     "ARCON", "NNPC", "CAC", "NDLEA", "A",
     "No advert runs outside its rules."),
    (T_CONS, "Hard", "Shrinkflation happens when sellers",
     "reduce size while holding price", "raise the price openly each week", "close their shops on Sundays", "give bigger sizes as gifts", "A",
     "The pack shrinks, the price stands."),
    (T_CONS, "Medium", "Weights and measures inspectors protect buyers against",
     "short-weight fraud", "counterfeit currency", "fake driving licences", "smuggled electronics", "A",
     "Their scales keep markets honest."),
    # ---------------------------------------------------------------- e-commerce
    (T_ECOM, "Easy", "Buying goods through a seller's website is called",
     "online shopping", "window shopping", "impulse buying", "bulk buying", "A",
     "The shop now lives on a screen."),
    (T_ECOM, "Easy", "The letter 'e' in e-commerce stands for",
     "electronic", "economic", "export", "essential", "A",
     "Electronics carry the commerce."),
    (T_ECOM, "Medium", "A payment gateway mainly",
     "processes online card payments", "delivers parcels to homes", "prints receipts in shops", "stores goods in bulk", "A",
     "It moves money for the sale."),
    (T_ECOM, "Medium", "Card fraud online is reduced by",
     "one-time passwords", "sharing PINs with friends", "writing PINs on cards", "banking on public Wi-Fi", "A",
     "Each login needs a fresh code."),
    (T_ECOM, "Easy", "E-commerce reaches customers far beyond the shop's street through",
     "the internet", "town criers", "billboard posters", "handbills", "A",
     "The web carries the shop worldwide."),
    (T_ECOM, "Easy", "The POS machine at a market stall mainly",
     "collects card payments", "weighs farm produce", "prints price tags", "stores cold fish", "A",
     "Buyers tap, sellers get value."),
    (T_ECOM, "Medium", "An online store's customer reviews help future buyers by",
     "guiding purchase choices", "increasing shipping costs", "raising product taxes", "blocking new sellers", "A",
     "Others' experience lights the way."),
    (T_ECOM, "Hard", "Drop-shipping means the seller",
     "ships directly from the producer", "keeps huge stocks upstairs", "refunds every buyer twice", "prints money for buyers", "A",
     "He sells first, the maker ships."),
]

build_batch(
    S,
    "batch_080_waec_commerce.json",
    "080",
    "WAEC Commerce Paper 1 round 1 (Round 16e): the WASSCE syllabus with "
    "FRESH angles - Nigerian agencies (CBN, NDIC, SON, NAFDAC, ARCON, "
    "Nigerian Exchange), document and payment scenarios (Kano-to-Aba home "
    "trade, POS stalls, dishonoured cheques, crossed cheques), insurance "
    "principles restated as stories, and a new e-commerce topic (payment "
    "gateways, OTP security, drop-shipping, shrinkflation) - because the "
    "near-dup scan checks every item against the JAMB, WAEC and NECO banks "
    "INCLUDING the large JAMB Commerce banks (003, 030-031) and the 74-item "
    "NECO Commerce bank. Topics: home and foreign trade, aids to trade, "
    "business units, trade documents and payments, banking and the stock "
    "exchange, insurance, consumer protection, e-commerce.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
