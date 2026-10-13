"""Batch 073 - NECO Marketing, Paper III Objective round 1.

NECO SSCE Marketing Paper III (Objective) is a 60-item paper (1 hr;
official 2026 External timetable, paper 3033). Covers the marketing
concept, segmentation, the marketing mix, product life cycle, pricing,
channels, promotion, consumer behaviour and market research. Near-dup
scanned against JAMB, WAEC and the existing NECO banks.

    python3 scripts/build_neco_batch73.py -> content/batch_073_neco_marketing.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_CON = "Marketing Concepts"
T_SEG = "Market Segmentation"
T_MIX = "The Marketing Mix"
T_PROD = "Product and Branding"
T_PRICE = "Pricing"
T_PLACE = "Distribution Channels"
T_PROMO = "Promotion"
T_CUST = "Consumer Behaviour"
T_RES = "Marketing Research"
T_ECOM = "E-Commerce and Customer Care"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- concepts
    (T_CON, "Easy", "Marketing is best defined as the business activities that identify customer needs and",
     "satisfy them profitably", "avoid all selling",
     "raise factory output only", "print advertisements only", "A",
     "Meeting needs at a profit is the core idea."),
    (T_CON, "Easy", "The marketing concept says the starting point of business planning should be the",
     "customer's need", "factory capacity", "bank's advice",
     "regulator's rule", "A",
     "The market comes before the machine."),
    (T_CON, "Medium", "A need becomes a want when it is shaped by culture and personality, but it becomes demand only when it is backed by",
     "purchasing power", "advertising alone",
     "government approval", "transport", "A",
     "Willingness plus ability to pay is demand."),
    (T_CON, "Medium", "The exchange at the heart of marketing requires at least",
     "two parties with something of value", "one party only",
     "money alone as medium", "written contracts always", "A",
     "Value must move both ways."),
    (T_CON, "Medium", "The set of actual and potential buyers of a product is called the",
     "market", "warehouse", "factory",
     "board", "A",
     "Where buyers gather, a market exists."),
    (T_CON, "Hard", "The societal marketing concept adds to the marketing concept a concern for society's",
     "long-run welfare", "short-run profit",
     "tax revenue only", "foreign reserves", "A",
     "Consumer satisfaction must not harm society."),

    # --------------------------------------------------------- segmentation
    (T_SEG, "Easy", "Dividing a broad market into smaller groups of similar buyers is called market",
     "segmentation", "saturation", "penetration",
     "concentration", "A",
     "Segments group buyers with common traits."),
    (T_SEG, "Medium", "Dividing a market by age, income and family size is segmentation by",
     "demographics", "geography", "lifestyle",
     "behaviour", "A",
     "Population statistics define the groups."),
    (T_SEG, "Medium", "A soft-drink firm selling sugar-free drinks to diabetics segments by customer knowledge and usage — segmentation by",
     "behaviour", "geography", "age alone",
     "income alone", "A",
     "Usage occasions and benefits drive it."),
    (T_SEG, "Easy", "Segmenting a market into North, East, West and South is by",
     "geography", "gender", "social class",
     "brand loyalty", "A",
     "Location is the dividing rod."),
    (T_SEG, "Hard", "Segmenting buyers by activities, interests and opinions is segmentation by",
     "psychographics", "demographics", "benefits sought",
     "usage rate", "A",
     "Lifestyle profiles the mind of the buyer."),
    (T_SEG, "Medium", "A market segment worth targeting should be measurable, accessible and",
     "large enough to profit", "impossible to serve",
     "identical to all others", "without competitors", "A",
     "Segments must pay for their own service."),

    # ---------------------------------------------------------- marketing mix
    (T_MIX, "Easy", "The four elements of the marketing mix are product, price, place and",
     "promotion", "people", "packaging",
     "planning", "A",
     "The 4Ps complete the mix."),
    (T_MIX, "Medium", "The marketing mix variables are largely controlled by the",
     "marketing manager", "final consumer alone",
     "government alone", "weather", "A",
     "Managers blend the tools the firm controls."),
    (T_MIX, "Medium", "Deciding the outlets through which a product reaches buyers is the part of the mix",
     "called place", "called price", "called product",
     "called promotion", "A",
     "Place is the distribution decision."),
    (T_MIX, "Hard", "In service marketing, the extended mix adds people, process and",
     "physical evidence", "public debt", "production lines",
     "pricing laws", "A",
     "Buyers judge services by visible cues."),

    # -------------------------------------------------------- product/branding
    (T_PROD, "Easy", "Anything offered to a market for attention, use or consumption is a",
     "product", "price", "discount",
     "ledger", "A",
     "Products may be goods or services."),
    (T_PROD, "Easy", "A name, sign or symbol that identifies a seller's goods is a",
     "brand", "coupon", "barcode",
     "waybill", "A",
     "The brand distinguishes the maker."),
    (T_PROD, "Medium", "The stage a product has reached in the market from launch to withdrawal is its",
     "life cycle", "cash cycle", "credit cycle",
     "billing cycle", "A",
     "Introduction, growth, maturity, decline."),
    (T_PROD, "Medium", "Sales rise slowly and promotion costs are highest at which stage of the product life cycle?",
     "Introduction", "Maturity", "Decline",
     "Growth", "A",
     "The market is still being told."),
    (T_PROD, "Medium", "Competitors are strongest and prices begin to fall during the stage of",
     "maturity", "introduction", "growth only",
     "withdrawal", "A",
     "Crowded markets squeeze margins."),
    (T_PROD, "Easy", "The container or wrapper of a product is its",
     "packaging", "patenting", "labelling only",
     "warehousing", "A",
     "Packaging protects and sells."),
    (T_PROD, "Medium", "The information printed on the package, showing contents and usage, is the",
     "label", "brand mark only", "invoice",
     "receipt", "A",
     "Labels inform and warn the buyer."),

    # --------------------------------------------------------------- pricing
    (T_PRICE, "Easy", "Adding a fixed mark-up to the cost of an item gives the price set by",
     "cost-plus pricing", "skimming", "penetration",
     "psychological pricing", "A",
     "Cost plus a margin is the simple method."),
    (T_PRICE, "Medium", "A new phone launched at a very high price to harvest early buyers is using price",
     "skimming", "penetration", "cost-plus",
     "predatory dumping", "A",
     "The cream is taken off the top first."),
    (T_PRICE, "Medium", "Setting a deliberately low launch price to win market share quickly is",
     "penetration pricing", "skimming", "prestige pricing",
     "price lining", "A",
     "Low entry prices court volume."),
    (T_PRICE, "Medium", "Pricing at ₦499 instead of ₦500 exploits the effect called",
     "psychological pricing", "price war", "dumping",
     "cartel pricing", "A",
     "The price feels a shade cheaper."),
    (T_PRICE, "Hard", "A company selling one product very cheap to pull customers who then buy profitable accessories uses a pricing approach called",
     "captive pricing", "cost-plus only", "skimming only",
     "uniform pricing", "A",
     "Razor cheap, blades costly."),
    (T_PRICE, "Medium", "When two sellers repeatedly cut prices against each other, the market suffers a",
     "price war", "price freeze", "price index",
     "price ceiling", "A",
     "Nobody wins a race to the bottom."),

    # ------------------------------------------------------------- place/channels
    (T_PLACE, "Easy", "The path through which goods move from producer to consumer is the channel of",
     "distribution", "production", "communication",
     "promotion", "A",
     "Channels carry title and product."),
    (T_PLACE, "Easy", "The shortest distribution channel runs directly from producer to",
     "consumer", "wholesaler", "retailer",
     "agent", "A",
     "No middleman stands between."),
    (T_PLACE, "Medium", "The middleman who sells in small quantities directly to final consumers is the",
     "retailer", "wholesaler", "broker only",
     "factory agent", "A",
     "Retail faces the shopper."),
    (T_PLACE, "Medium", "A middleman who never owns the goods but brings buyers and sellers together for a commission is an",
     "agent", "wholesaler", "retailer",
     "consumer", "A",
     "Agents broker, they do not buy."),
    (T_PLACE, "Hard", "A producer who allows only one dealer per territory to sell its product uses distribution that is",
     "exclusive", "intensive", "extensive",
     "selective only", "A",
     "One dealer guards the territory."),
    (T_PLACE, "Medium", "Selling through every possible outlet, as with bread and pure water, is distribution of the kind",
     "intensive", "exclusive", "direct",
     "selective", "A",
     "Convenience goods need to be everywhere the buyer looks."),

    # -------------------------------------------------------------- promotion
    (T_PROMO, "Easy", "The marketing tool that is paid, non-personal mass communication is",
     "advertising", "personal selling", "publicity alone",
     "word of mouth", "A",
     "Advertising buys the mass audience."),
    (T_PROMO, "Medium", "Face-to-face presentation of a product to a prospect is",
     "personal selling", "advertising", "sales promotion",
     "public relations", "A",
     "The salesman answers objections directly."),
    (T_PROMO, "Medium", "Short-term incentives like coupons, free samples and contests make up",
     "sales promotion", "personal selling", "publicity",
     "pricing policy", "A",
     "They push immediate purchase."),
    (T_PROMO, "Medium", "Unpaid mention of a firm in the news media is called",
     "publicity", "advertising", "sales promotion",
     "labelling", "A",
     "Publicity is earned, not bought."),
    (T_PROMO, "Hard", "Building good relations with the public to earn a favourable image is the work of",
     "public relations", "personal selling", "warehousing",
     "production planning", "A",
     "Image is managed deliberately."),
    (T_PROMO, "Easy", "A free sachet of a new detergent inside a newspaper is an example of",
     "a sales promotion sample", "personal selling",
     "a press release", "a price war", "A",
     "Sampling lets the product speak."),

    # -------------------------------------------------------- consumer behaviour
    (T_CUST, "Easy", "The person who finally uses a product is the",
     "consumer", "wholesaler", "agent",
     "advertiser", "A",
     "Consumption ends the journey."),
    (T_CUST, "Medium", "The mental process through which a buyer moves from need recognition to purchase decision is the",
     "buying process", "selling cycle", "production line",
     "billing cycle", "A",
     "Problem, search, evaluation, choice."),
    (T_CUST, "Medium", "Reasons that push a customer to buy, like hunger or status, are called buying",
     "motives", "discounts", "budgets",
     "quotas", "A",
     "Motives drive the decision."),
    (T_CUST, "Medium", "A buyer's choice influenced by friends' opinions is shaped by",
     "social influence", "personal income alone", "weather alone",
     "factory location", "A",
     "Reference groups sway choices."),
    (T_CUST, "Hard", "The discomfort a buyer feels after purchase, wondering if the choice was right, is called",
     "cognitive dissonance", "market segmentation",
     "price skimming", "brand equity", "A",
     "Buyers seek reassurance afterwards."),
    (T_CUST, "Medium", "Repeat purchasing of the same brand shows the customer's",
     "brand loyalty", "brand rejection", "price blindness",
     "market exit", "A",
     "Loyal buyers return without prompt."),

    # -------------------------------------------------------- marketing research
    (T_RES, "Easy", "The gathering and study of market information to guide decisions is market",
     "research", "share", "control",
     "audit", "A",
     "Research replaces guessing."),
    (T_RES, "Medium", "A printed list of questions given to respondents is a",
     "questionnaire", "waybill", "receipt",
     "payroll", "A",
     "Questionnaires collect uniform answers."),
    (T_RES, "Medium", "Watching shoppers actually select goods in a store, without asking questions, is research by",
     "observation", "interview", "experiment",
     "postal survey", "A",
     "Behaviour seen beats behaviour claimed."),
    (T_RES, "Medium", "Testing a new product on a small group of buyers first is called a",
     "test market", "price war", "recall",
     "census", "A",
     "The pilot market reveals the future."),
    (T_RES, "Hard", "Data first collected afresh for the problem at hand is called data of the kind",
     "primary", "secondary", "dummy",
     "external only", "A",
     "Primary data answers this question."),
    (T_RES, "Medium", "Studying the strengths and weaknesses of rival products is research into the",
     "competition", "climate", "culture",
     "channel", "A",
     "Know the rival as yourself."),

    # ---------------------------------------------------- e-commerce/customer care
    (T_ECOM, "Easy", "Buying and selling of goods over the internet is",
     "e-commerce", "barter", "smuggling",
     "wharf trade", "A",
     "Jumia and Konga trade online."),
    (T_ECOM, "Medium", "A firm's website showing its goods and prices to the whole world is an example of marketing",
     "without borders", "by force", "by ration",
     "by barter", "A",
     "The internet removes distance."),
    (T_ECOM, "Medium", "Payment on delivery builds trust between online shops and buyers who fear being",
     "defrauded", "praised", "advertised",
     "sampled", "A",
     "Cash-on-delivery calms doubt."),
    (T_ECOM, "Easy", "Help given to a buyer after the sale, like installation and repairs, is",
     "after-sales service", "pre-sale hype", "labelling",
     "warehousing", "A",
     "Care after payment keeps customers."),
    (T_ECOM, "Medium", "Handling customer complaints promptly mainly improves customer",
     "retention and loyalty", "turnover", "losses",
     "taxes", "A",
     "A recovered complainer stays loyal."),
    (T_ECOM, "Hard", "The practice of keeping customers rather than endlessly chasing new ones is strategy for customer",
     "retention", "acquisition only", "discounting",
     "segmentation only", "A",
     "Old customers cost less to keep."),

    (T_CON, "Medium", "The percentage of an industry's total sales captured by one firm is its",
     "market share", "sales mix", "mark-up",
     "market gap", "A",
     "Share tracks the firm's slice of the whole market."),
]

build_batch(
    S,
    "batch_073_neco_marketing.json",
    "073",
    "NECO Marketing Paper III round 1: the SSCE syllabus - marketing "
    "concepts (needs, wants, demand, exchange), segmentation "
    "(demographic, geographic, behavioural, psychographic), the marketing "
    "mix (4Ps + services), product and branding (life cycle, packaging, "
    "labels), pricing (cost-plus, skimming, penetration, psychological, "
    "captive), channels (exclusive/intensive), promotion (advertising, "
    "personal selling, sales promotion, publicity, PR), consumer behaviour "
    "(buying process, motives, dissonance, loyalty), market research "
    "(questionnaire, observation, test market, primary data) and "
    "e-commerce/customer care. Near-dup scanned against the JAMB, WAEC "
    "and existing NECO banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
