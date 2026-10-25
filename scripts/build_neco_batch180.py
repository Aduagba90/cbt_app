"""Batch 180 - NECO Marketing round 6 (NECO top-up, R34).

Grows NECO Marketing from 213 toward ~248 with angles not yet in
the bank: latent and negative demand; the rack jobber and the drop
shipper; horizontal channel conflict; the channel captain; family
packaging; co-branding and multi-branding; value-based and
by-product pricing; the cash discount and the trade-in allowance;
the objective-and-task budget; push against pull; the dealer
loader; advertising frequency and prime time; selective demand;
the perceptual map; closing the sale; the warranty; patronage
motives; the mystery shopper; cart abandonment; the chatbot;
customer lifetime value and churn; internal marketing; the market
leader; niche and undifferentiated marketing; the letter of credit
and counter trade; SON guarding standards. Scanned against NECO
rounds 1-5, WAEC Marketing (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch180.py -> content/batch_180_neco_marketing6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_CON = "Marketing Concepts"
T_SEG = "Market Segmentation"
T_BR = "Product and Branding"
T_PRI = "Pricing"
T_PRO = "Promotion"
T_SAL = "Salesmanship"
T_DIS = "Distribution Channels"
T_RES = "Marketing Research"
T_ECO = "E-Commerce and Customer Care"
T_SER = "Services and Relationships"
T_INT = "International Marketing"
T_CSO = "Consumers and Society"

PASSAGES = []
PQ = []

Q = [
    (T_CON, "Hard", "Would-be buyers who strongly crave a product that no firm has yet offered represent",
     "latent demand", "negative demand",
     "full demand", "overfull demand", "A",
     "The want sleeps until a marketer wakes it."),
    (T_CON, "Hard", "When most consumers avoid a product entirely, as many avoid creepy-crawlies as food, the demand state is",
     "negative", "latent",
     "irrational", "declining", "A",
     "The market runs the other way."),
    (T_CON, "Easy", "The firm with the largest market share, whose moves the others watch and copy, is the market",
     "leader", "challenger",
     "follower", "nicher", "A",
     "The pack keeps one eye on its front runner."),
    (T_CON, "Medium", "Concentrating the whole offer on one small, overlooked corner of a big market is",
     "niche marketing", "mass marketing",
     "differentiated marketing", "counter marketing", "A",
     "The small pond yields a big fish."),
    (T_CON, "Medium", "Offering one undivided product and message to the whole market, ignoring segment differences, is",
     "undifferentiated marketing", "concentrated marketing",
     "micro marketing", "customised marketing", "A",
     "One net is cast for every fish."),
    (T_CON, "Hard", "An advert that urges buyers to choose one particular brand, rather than the product class generally, builds",
     "selective demand", "primary demand",
     "latent demand", "derived demand", "A",
     "Choose ours, not merely ours kind."),
    (T_SEG, "Hard", "Plotting how consumers perceive rival brands along two axes, say price against quality, produces a",
     "perceptual map", "pie chart",
     "control chart", "route plan", "A",
     "The map shows the empty corners worth claiming."),
    (T_BR, "Medium", "Giving every item in a firm's line the same look and design style is",
     "family packaging", "blind packaging",
     "bulk packaging", "own-label packaging", "A",
     "One family face on the whole shelf."),
    (T_BR, "Medium", "A phone maker and a famous camera maker joining their names on one handset practice",
     "co-branding", "rebranding",
     "private branding", "brand extension", "A",
     "Two trusted names share one product."),
    (T_BR, "Hard", "One detergent firm selling several rival brands side by side, each a different name, uses",
     "multi-branding", "brand equity",
     "brand licensing", "line filling", "A",
     "Brothers compete on the same shelf."),
    (T_PRI, "Medium", "Setting the price by what the buyer believes the product is worth, not by its cost, is",
     "value-based pricing", "cost-plus pricing",
     "break-even pricing", "going-rate pricing", "A",
     "The buyer's judgment is the price tag."),
    (T_PRI, "Hard", "A flour mill selling its wheat bran to feed makers to offset milling costs practises",
     "by-product pricing", "product-bundle pricing",
     "captive-product pricing", "two-part pricing", "A",
     "The side product shoulders part of the load."),
    (T_PRI, "Easy", "A trader who pays her supplier within seven days to earn two per cent off enjoys a",
     "cash discount", "quantity discount",
     "trade-in allowance", "seasonal discount", "A",
     "Prompt payment pockets a reward."),
    (T_PRI, "Medium", "A dealer who knocks N150,000 off a new car because the buyer surrendered his old one grants a",
     "trade-in allowance", "cash discount",
     "rebate", "promotional allowance", "A",
     "The old car rides down the new price."),
    (T_PRO, "Hard", "Building the promotion budget by costing each planned activity, instead of a percentage of sales, is the",
     "objective-and-task method", "percentage-of-sales method",
     "affordable method", "competitive-parity method", "A",
     "First count the tasks, then count the money."),
    (T_PRO, "Medium", "Persuading wholesalers and retailers to stock and push a product, rather than advertising to the public, is the",
     "push strategy", "pull strategy",
     "blitz strategy", "holding strategy", "A",
     "The trade is won first, then the shelf fights."),
    (T_PRO, "Medium", "Advertising straight to consumers so shops are forced to stock the advertised brand is the",
     "pull strategy", "push strategy",
     "penetration strategy", "skimming strategy", "A",
     "The customer's asking drags the goods through."),
    (T_PRO, "Hard", "A brewery giving a retailer one free case for every ten bought offers a",
     "dealer loader", "consumer premium",
     "slotting rebate only", "loyalty point", "A",
     "The free case loads the dealer's store."),
    (T_PRO, "Easy", "The number of times the average person meets an advert within the campaign period is its",
     "frequency", "reach",
     "circulation", "impact", "A",
     "Repetition stamps the message in."),
    (T_PRO, "Easy", "The evening hours when television audiences are largest are called",
     "prime time", "dead time",
     "off-peak", "night shift", "A",
     "Every station sells those hours dearest."),
    (T_SAL, "Medium", "After demonstrating the product, the salesperson finally asks the prospect outright to place the order. This step is",
     "closing the sale", "prospecting",
     "pre-approach", "follow-up", "A",
     "The ask turns interest into a signature."),
    (T_SAL, "Easy", "A buyer keeps returning to one shop because of its location, credit and cheerful service. These are",
     "patronage motives", "buying motives",
     "emotional motives", "rational motives", "A",
     "The shop's pull keeps her coming."),
    (T_CSO, "Easy", "A written promise to repair or replace a faulty item within a stated period is a",
     "warranty", "coupon",
     "invoice", "receipt", "A",
     "The paper stands behind the product."),
    (T_CSO, "Medium", "The federal agency chiefly responsible for setting standards for manufactured goods in Nigeria is",
     "SON", "NAFDAC",
     "CBN", "NPC", "A",
     "The Standards Organisation of Nigeria."),
    (T_DIS, "Hard", "A middleman who owns no stock but maintains display racks of say, toys, inside supermarkets is a",
     "rack jobber", "cash-and-carry wholesaler",
     "truck jobber always", "mail-order house", "A",
     "He services his own racks in other men's stores."),
    (T_DIS, "Hard", "A seller who takes orders from catalogues and has the producer ship direct to the buyer, never touching the goods, is a",
     "drop shipper", "merchant wholesaler",
     "broker of services", "rack jobber", "A",
     "The goods bypass his warehouse entirely."),
    (T_DIS, "Hard", "Two independent dealers in the same town quarrelling over the same customers illustrates",
     "horizontal conflict", "vertical conflict",
     "channel cooperation", "channel integration", "A",
     "Brothers of one level fight each other."),
    (T_DIS, "Hard", "The channel member, often the big manufacturer, who sets the rules other members follow is the",
     "channel captain", "channel challenger",
     "gate keeper", "freight forwarder", "A",
     "The captain steers the whole chain."),
    (T_RES, "Hard", "A researcher who poses as an ordinary shopper to rate a store's service quality is a",
     "mystery shopper", "panel member",
     "focus group host", "census officer", "A",
     "The store never knows the customer's brief."),
    (T_ECO, "Medium", "Online shoppers who fill their baskets and then vanish before paying exhibit",
     "cart abandonment", "banner blindness",
     "churn", "bouncing only", "A",
     "Full baskets, empty tills."),
    (T_ECO, "Easy", "The software assistant that instantly answers routine customer questions on a website is a",
     "chatbot", "newswire",
     "ledger", "search engine", "A",
     "It chats day and night without pay."),
    (T_SER, "Hard", "The total profit a firm expects from one customer across all their future years together is",
     "customer lifetime value", "market share",
     "average revenue", "retention cost", "A",
     "Today's buyer is tomorrow's annuity."),
    (T_SER, "Medium", "The rate at which subscribers cancel their service each month is called",
     "churn", "turnover of goods",
     "conversion", "click-through", "A",
     "Every cancellation widens the leak."),
    (T_SER, "Hard", "Training and motivating a firm's own staff to serve customers gladly is itself marketing, called",
     "internal marketing", "demarketing",
     "inverse marketing", "ghost marketing", "A",
     "Happy staff make happy customers."),
    (T_INT, "Hard", "The safest way for an exporter to collect payment abroad is through a",
     "letter of credit", "handshake at the port",
     "post-dated personal cheque", "telegram promising payment", "A",
     "The bank's paper guarantees the money."),
    (T_INT, "Hard", "Two nations exchanging goods directly for goods, without money passing between them, engage in",
     "counter trade", "free trade",
     "entrepot trade", "re-export trade", "A",
     "Oil for machinery, naira never counts."),
]

build_batch(
    S,
    "batch_180_neco_marketing6.json",
    "180",
    "NECO Marketing round 6 (R34 top-up): latent and negative "
    "demand; the market leader; niche and undifferentiated "
    "marketing; selective demand; the perceptual map; family "
    "packaging; co-branding and multi-branding; value-based and "
    "by-product pricing; cash discount and trade-in allowance; the "
    "objective-and-task budget; push against pull; the dealer "
    "loader; frequency and prime time; closing the sale; patronage "
    "motives; the warranty; SON guarding standards; the rack "
    "jobber; the drop shipper; horizontal conflict; the channel "
    "captain; the mystery shopper; cart abandonment; the chatbot; "
    "customer lifetime value; churn; internal marketing; the "
    "letter of credit; counter trade. Scanned against NECO rounds "
    "1-5, WAEC Marketing (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
