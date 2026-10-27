"""Batch 220 - NECO Marketing round 7 (NECO top-up, R44).

Grows NECO Marketing from 249 toward ~274 with angles verified absent
from the whole Marketing pool (503 items across WAEC and NECO):
payment gateway; logistics; lead time; reorder level; safety stock;
missionary selling; sales territory; direct selling; vertical
marketing system; disintermediation; discount store; convenience
store; speciality goods; bonus pack; loyalty card; cooperative
advertising; pioneering advertising; reach; mission statement;
customer retention; business to business; observation method;
experimental method; export agent; embargo. Checked and avoided
(already banked): loss leader, promotional/odd/psychological
pricing, telemarketing, market potential, sales forecast, the four
utilities, brand mark, closing a sale, prospecting, exchange,
warranty, pilot study, comparative and reminder advertising,
sponsorship, internal marketing, price-off coupon.

    python3 scripts/build_neco_batch220.py -> content/batch_220_neco_marketing7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_ECOM = "E-Commerce and Customer Care"
T_PDIST = "Intermediaries and Physical Distribution"
T_SALES = "Salesmanship"
T_CHAN = "Distribution Channels"
T_RETAIL = "Channel Dynamics and Retailing"
T_PROD = "Product and Branding"
T_PROM = "Promotion"
T_PSELL = "Promotion and Selling"
T_ADV = "Advertising and Consumerism"
T_CONC = "Marketing Concepts"
T_REL = "Services and Relationships"
T_RES = "Marketing Research"
T_INTL = "International Marketing"

PASSAGES = []
PQ = []

Q = [
    (T_ECOM, "Medium", "The online service that checks a customer's card details and moves the payment safely from the customer's bank to the seller's account is a",
     "payment gateway", "shopping cart",
     "web browser", "data bundle", "A",
     "It stands guard between the shop and the banks."),
    (T_PDIST, "Medium", "The planning and control of the whole flow of goods, services and information from the producer to the final consumer is called",
     "logistics", "publicity",
     "teleselling", "window dressing", "A",
     "It moves the right goods to the right place on time."),
    (T_PDIST, "Medium", "The length of time between placing an order with a supplier and receiving the goods is called the",
     "lead time", "credit period",
     "grace period", "shelf life", "A",
     "The clock runs from order to delivery."),
    (T_PDIST, "Hard", "A store keeper places a fresh order as soon as stock falls to a chosen level, so that the goods arrive before the shelf empties. That chosen level is the",
     "reorder level", "reorder quantity",
     "safety stock", "stock-out point", "A",
     "Below this line an order must go out at once."),
    (T_PDIST, "Medium", "The extra quantity of goods a dealer keeps in reserve so that an unexpected rush of buyers does not empty his shelves is called",
     "safety stock", "dead stock",
     "pilot stock", "display stock", "A",
     "It is the cushion against a sudden surge in demand."),
    (T_SALES, "Hard", "A salesperson employed to visit doctors and chemists, telling them about a firm's new drug without taking orders directly, is engaged in",
     "missionary selling", "retail selling",
     "street hawking", "teleselling", "A",
     "He builds goodwill; the orders come in later."),
    (T_SALES, "Medium", "The particular area, say the whole of Anambra State, assigned to one sales representative to cover is his",
     "sales territory", "sales quota",
     "sales ledger", "market segment", "A",
     "Every customer in that patch is his to serve."),
    (T_CHAN, "Easy", "Selling products directly to consumers at their homes or offices, without passing through any middleman, is called",
     "direct selling", "indirect exporting",
     "wholesale trade", "bulk breaking", "A",
     "The producer meets the final buyer face to face."),
    (T_CHAN, "Hard", "An arrangement in which a producer, its wholesaler and its retailers operate as one unified system under a single plan is called a",
     "vertical marketing system", "horizontal marketing system",
     "open channel system", "free channel system", "A",
     "All three levels pull together as one team."),
    (T_CHAN, "Hard", "When a manufacturer drops the middlemen and begins to sell to final consumers through its own website, the practice is called",
     "disintermediation", "reintermediation",
     "nationalisation", "wholesaling", "A",
     "The go-betweens are cut out of the chain."),
    (T_RETAIL, "Easy", "A large shop that sells a limited range of goods at prices well below the usual retail prices is a",
     "discount store", "speciality shop",
     "boutique", "luxury arcade", "A",
     "Low margins are made up by high turnover."),
    (T_RETAIL, "Easy", "A small neighbourhood shop that stays open long hours every day and stocks everyday items like bread, milk and airtime is a",
     "convenience store", "warehouse",
     "hypermarket", "department store", "A",
     "Quick, near and always open for small needs."),
    (T_PROD, "Medium", "Goods with special characteristics for which a buyer is willing to make a special effort, such as a particular luxury watch, are",
     "speciality goods", "convenience goods",
     "shopping goods", "unsought goods", "A",
     "The buyer hunts for that one item, not any other."),
    (T_PROM, "Easy", "An offer in which the seller gives the buyer extra quantity free, such as twenty per cent extra free on a pack of detergent, is a",
     "bonus pack", "price-off coupon",
     "trade allowance", "cash discount", "A",
     "The pack itself grows; the price stays put."),
    (T_PROM, "Easy", "A card that records a customer's purchases and rewards continued buying with points or discounts is called a",
     "loyalty card", "credit card",
     "debit card", "gift voucher", "A",
     "It pays the shopper to come back again."),
    (T_PSELL, "Medium", "An arrangement in which a manufacturer pays part of the cost of the adverts that its dealers place in the local newspapers is called",
     "cooperative advertising", "comparative advertising",
     "institutional advertising", "classified advertising", "A",
     "Factory and shopkeeper share the advert bill."),
    (T_ADV, "Medium", "The type of advertising used when a product category is entirely new, aimed at teaching consumers what the product is and what it does, is",
     "pioneering advertising", "reminder advertising",
     "competitive advertising", "classified advertising", "A",
     "It opens the ground before any rival appears."),
    (T_PROM, "Medium", "In advertising, the total number of different people who are exposed to an advertisement at least once during a campaign is called",
     "reach", "frequency",
     "circulation", "impact", "A",
     "Reach counts faces; frequency counts repeats."),
    (T_CONC, "Easy", "A short, clear statement of a firm's basic purpose and general direction, often framed and hung in its offices, is the",
     "mission statement", "marketing plan",
     "sales budget", "annual report", "A",
     "In a few lines it says why the firm exists."),
    (T_REL, "Medium", "All the steps a firm takes to keep its old customers buying from it, instead of spending heavily to win strangers, is known as",
     "customer retention", "customer poaching",
     "market skimming", "product recall", "A",
     "An old customer kept is cheaper than a new one won."),
    (T_ECOM, "Medium", "When one business sells goods or services to another business through an online platform, the trade is described as",
     "business to business (B2B)", "business to consumer (B2C)",
     "consumer to consumer (C2C)", "consumer to business (C2B)", "A",
     "Both the seller and the buyer are firms."),
    (T_RES, "Medium", "A researcher studies shoppers in a Lagos supermarket, recording what they pick up and what they return to the shelf, without asking anyone any questions. He is using the",
     "observation method", "interview method",
     "postal survey method", "focus group method", "A",
     "He watches behaviour; he does not ask about it."),
    (T_RES, "Hard", "A soft-drink firm launches its new flavour in one town while leaving a similar nearby town without it, then compares sales in the two towns. This research technique is the",
     "experimental method", "survey method",
     "desk research method", "panel census method", "A",
     "One town tries it; its twin stands as control."),
    (T_INTL, "Medium", "An agent in a foreign country who sells a Nigerian manufacturer's products there on commission, without ever owning the goods, is an",
     "export agent", "export merchant",
     "shipping agent", "trade commissioner", "A",
     "He sells for the maker but never buys the goods."),
    (T_INTL, "Medium", "A government's total ban on the buying or selling of goods with a particular country is called an",
     "embargo", "tariff",
     "quota", "subsidy", "A",
     "Trade with that country stops completely."),
]

build_batch(
    S,
    "batch_220_neco_marketing7.json",
    "220",
    "NECO Marketing round 7 (R44 top-up): payment gateway; logistics; "
    "lead time; reorder level; safety stock; missionary selling; sales "
    "territory; direct selling; vertical marketing system; "
    "disintermediation; discount store; convenience store; speciality "
    "goods; bonus pack; loyalty card; cooperative advertising; "
    "pioneering advertising; reach; mission statement; customer "
    "retention; B2B; observation method; experimental method; export "
    "agent; embargo. Scanned against the whole Marketing pool (WAEC "
    "and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
