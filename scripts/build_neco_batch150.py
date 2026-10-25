"""Batch 150 - NECO Marketing round 5 (NECO top-up, R28).

Grows NECO Marketing from 175 toward ~211 with angles not yet in the
bank: the evolution of marketing concepts (production, selling,
marketing, societal); the marketing mix and goods classification
(convenience, specialty, industrial); services' intangibility and
inseparability; brand equity, brand vs line extension, new-product
development stages; prestige, loss-leader and price-lining strategies;
wholesaler bulk-breaking, brokers and agents, intensive distribution;
sales promotion tools, media selection, publicity, sales quotas and
territories, canvassing; consumer rights, consumerism, caveat emptor;
perishability of services; relationship marketing; social media, email
marketing and SEO; the marketing audit and plan. Scanned against NECO
rounds 1-4, WAEC Marketing (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch150.py -> content/batch_150_neco_marketing5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_CON = "Marketing Concepts"
T_MIX = "Mix and Goods Classification"
T_BR = "Branding and Product Development"
T_PRI = "Pricing Strategies"
T_DIS = "Distribution"
T_PRO = "Promotion and Selling"
T_CONS = "Consumers and Society"
T_SER = "Services and Relationships"
T_DIG = "Digital Marketing"
T_PLA = "Marketing Planning"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- concepts
    (T_CON, "Medium", "A firm that believes customers favour cheap, widely available products follows the",
     "production concept", "selling concept", "societal concept", "product concept", "A",
     "Efficiency and coverage are its gods."),
    (T_CON, "Hard", "A company that pushes its goods through aggressive promotion, caring little for what buyers want, is stuck in the",
     "selling concept", "marketing concept", "societal concept", "holistic concept", "A",
     "It sells what it makes, not what is wanted."),
    (T_CON, "Medium", "Under the marketing concept, every plan in a customer-minded firm begins from",
     "what the buyer needs", "what the factory makes", "what the rivals charge", "what the admen like", "A",
     "The buyer's wish steers the firm."),
    (T_CON, "Hard", "Beyond satisfying the customer, the societal marketing concept also weighs",
     "society's long-run welfare", "the rivals' profits", "the ad agency's fees", "the CEO's comfort", "A",
     "People, planet, then profit."),

    # ------------------------------------------------------------- mix & goods
    (T_MIX, "Medium", "The four Ps together make up the firm's",
     "marketing mix", "profit margin", "mission", "budget line", "A",
     "Product, price, place and promotion."),
    (T_MIX, "Medium", "Items a housewife grabs from the nearest shop with no comparing or hunting are classed as",
     "convenience goods", "specialty goods", "shopping goods", "industrial goods", "A",
     "The nearest shop wins the sale."),
    (T_MIX, "Hard", "A buyer who insists on one particular designer watch and searches far for it is shopping for a",
     "specialty good", "convenience good", "shopping good", "staple good", "A",
     "Worth the long hunt to him."),
    (T_MIX, "Medium", "Machines and raw materials bought for use in further production are",
     "industrial goods", "consumer goods", "durable goods", "specialty goods", "A",
     "Factories, not families, consume them."),
    (T_MIX, "Hard", "A hotel room cannot be seen, tasted or carried home before purchase. This marks the service's",
     "intangibility", "durability", "homogeneity", "divisibility", "A",
     "You buy a promise, not an object."),

    # ------------------------------------------------------------- branding & development
    (T_BR, "Hard", "The extra money buyers pay simply because of a trusted name is the brand's",
     "equity", "premium cost", "tariff", "royalty", "A",
     "Reputation itself holds value."),
    (T_BR, "Hard", "When a famous juice name appears on a new ice cream, the maker is practising",
     "brand extension", "line extension", "brand licensing", "co-branding", "A",
     "The name leaps to a new shelf."),
    (T_BR, "Medium", "Adding a new flavour or pack size within the same product family is",
     "line extension", "brand extension", "diversification", "market entry", "A",
     "The family grows within its row."),
    (T_BR, "Medium", "New product development rightly begins with",
     "idea generation", "test marketing", "pricing", "distribution", "A",
     "Ideas come before everything."),
    (T_BR, "Hard", "Test marketing exists chiefly to",
     "try the product in a real market", "register the trademark", "fix staff salaries", "print the label", "A",
     "A small stage before the full show."),

    # ------------------------------------------------------------- pricing
    (T_PRI, "Hard", "Pricing a wristwatch deliberately high to suggest exclusivity is",
     "prestige pricing", "penetration pricing", "loss-leader pricing", "dumping", "A",
     "The price itself is the ornament."),
    (T_PRI, "Hard", "A supermarket prices bagged rice below cost to pull crowds who buy other items. The rice is a",
     "loss leader", "prestige line", "price liner", "cash cow", "A",
     "It bleeds so the store may gain."),
    (T_PRI, "Medium", "Selling shirts at only N2,000, N3,500 or N5,000, nothing between, uses",
     "price lining", "price skimming", "bundle pricing", "by-product pricing", "A",
     "A few fixed steps, not a slope."),

    # ------------------------------------------------------------- distribution
    (T_DIS, "Hard", "Breaking bulk into smaller quantities for retailers is a key service of the",
     "wholesaler", "broker", "advertising agency", "market researcher", "A",
     "He buys crates and sells dozens."),
    (T_DIS, "Hard", "A broker differs from a merchant wholesaler because the broker",
     "never takes ownership of goods", "finances the buyers", "stores the goods", "brands the goods", "A",
     "He matches, he does not own."),
    (T_DIS, "Medium", "Stocking a product in every kiosk, supermarket and stall available is",
     "intensive distribution", "exclusive distribution", "selective distribution", "direct distribution", "A",
     "Everywhere the eye can turn."),
    (T_DIS, "Medium", "Transport, warehousing, inventory and order processing together form a firm's",
     "physical distribution", "marketing mix", "promotion blend", "pricing policy", "A",
     "Goods must move as well as sell."),

    # ------------------------------------------------------------- promotion & selling
    (T_PRO, "Medium", "Money-off coupons and free samples belong to the promotion family called",
     "sales promotion", "publicity", "personal selling", "trade fairs", "A",
     "Little gifts with short fuses."),
    (T_PRO, "Medium", "The FIRST factor in choosing an advertising medium is the",
     "nature of the target audience", "colour of the product", "mood of the artist", "size of the firm's logo", "A",
     "Speak where your listeners gather."),
    (T_PRO, "Medium", "News coverage that costs the firm nothing is called",
     "publicity", "advertising", "sales promotion", "private selling", "A",
     "Free ink is still ink in the ledger."),
    (T_PRO, "Hard", "The sales target assigned to a salesperson for a period is his",
     "quota", "territory", "commission", "canvass", "A",
     "A number to hunt each month."),
    (T_PRO, "Medium", "The geographic patch a salesperson alone covers is his",
     "territory", "quota", "margin", "portfolio", "A",
     "His map holds all his customers."),
    (T_PRO, "Medium", "Moving from door to door seeking likely buyers is",
     "canvassing", "merchandising", "arbitrating", "consigning", "A",
     "The knuckles do the prospecting."),

    # ------------------------------------------------------------- consumers & society
    (T_CONS, "Medium", "Insisting that producers state true contents and fair prices on every package defends the consumer's right to",
     "information", "safety", "redress", "choice", "A",
     "Labels and honest claims serve it."),
    (T_CONS, "Medium", "The organised effort to protect buyers' interests is known as",
     "consumerism", "capitalism", "commercialism", "communalism", "A",
     "The consumer's own lobby."),
    (T_CONS, "Hard", "The old Latin warning 'caveat emptor' reminds the buyer to",
     "beware", "haggle", "return goods", "pay cash", "A",
     "Let the purchaser watch the scales."),

    # ------------------------------------------------------------- services & relationships
    (T_SER, "Hard", "An empty hotel room last night can never be sold again. This marks a service's",
     "perishability", "tangibility", "separability", "homogeneity", "A",
     "Unsold tonight, gone forever."),
    (T_SER, "Medium", "A barber cuts and the customer receives the haircut at the same moment, showing the service's",
     "inseparability", "intangibility", "durability", "transferability", "A",
     "Making and using are one act."),
    (T_SER, "Medium", "Keeping old customers delighted rather than endlessly hunting new ones is the aim of",
     "relationship marketing", "mass marketing", "counter marketing", "shock marketing", "A",
     "Old friends come back to buy again."),

    # ------------------------------------------------------------- digital
    (T_DIG, "Medium", "Promoting goods through posts, likes and shares on platforms is",
     "social media marketing", "database marketing", "green marketing", "viral pricing", "A",
     "The newsfeed is the new market square."),
    (T_DIG, "Medium", "Sending offers and newsletters to a list of subscribers is",
     "email marketing", "ambient marketing", "guerrilla marketing", "catalogue pricing", "A",
     "The inbox as a shop window."),
    (T_DIG, "Hard", "Improving web pages so they appear higher in unpaid search results is",
     "search engine optimisation", "pay-per-click buying", "banner exchange", "affiliate linking", "A",
     "Climb the list without paying for it."),

    # ------------------------------------------------------------- planning
    (T_PLA, "Hard", "A thorough, periodic review of a firm's marketing environment, objectives and activities is the",
     "marketing audit", "sales quota", "breakeven chart", "stocktaking", "A",
     "The mirror held up to the whole effort."),
    (T_PLA, "Medium", "A marketing plan usually opens with a brief",
     "executive summary", "price list", "staff roster", "list of debtors", "A",
     "The whole story in half a page."),
]

build_batch(
    S,
    "batch_150_neco_marketing5.json",
    "150",
    "NECO Marketing round 5 (R28 top-up): production, selling, "
    "marketing and societal concepts; the 4Ps mix; convenience, "
    "specialty and industrial goods; service intangibility; brand "
    "equity, brand vs line extension; idea generation first, test "
    "marketing's purpose; prestige pricing, loss leader, price lining; "
    "wholesaler bulk-breaking, broker takes no title, intensive "
    "distribution, physical distribution bundle; coupons and samples, "
    "audience-first media choice, publicity, quota, territory, "
    "canvassing; right to information, consumerism, caveat emptor; "
    "perishability and inseparability of services; relationship "
    "marketing; social media, email marketing, SEO; marketing audit "
    "and executive summary. Scanned against NECO rounds 1-4, WAEC "
    "Marketing (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
