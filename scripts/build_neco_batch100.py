"""Batch 100 - WAEC Marketing round 2 (WAEC lift, Round 19).

WAEC Marketing Paper 1 draws 50 items; the bank stood at 63. This lift adds
fresh items - SWOT, external environment, market share, core and augmented
product, mix width, labelling, the four service characteristics, break-even
numeric, dynamic and freemium pricing, wholesaler credit, possession
utility, closing and follow-up in selling, press releases, reach vs
frequency, telephone and online surveys, culture and opinion leaders,
innovators, B2B traits, derived demand, organic vs paid social, A/B
testing, retargeting, user-generated content, adaptation vs
standardisation, green marketing - scanned against WAEC r1, NECO rounds
1-2 and the JAMB Commerce marketing items.

    python3 scripts/build_neco_batch100.py -> content/batch_100_waec_marketing2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_ENV = "The Marketing Environment"
T_PROD = "Product"
T_SERV = "Services Marketing"
T_PRICE = "Pricing"
T_DIST = "Distribution"
T_SELL = "Personal Selling and Promotion"
T_RES = "Marketing Research"
T_BUY = "Consumer and Business Buying"
T_DIG = "Digital and Global Marketing"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- environment
    (T_ENV, "Hard", "A firm auditing its Strengths, Weaknesses, Opportunities and Threats is doing a",
     "SWOT analysis", "PEST audit", "market share review", "product audit", "A",
     "The four words spell the tool."),
    (T_ENV, "Medium", "Government policy, inflation and technology trends belong to the firm's",
     "external environment", "internal environment", "staff welfare file", "production line", "A",
     "They act from outside the gate."),
    (T_ENV, "Easy", "A firm's own share of total industry sales is its",
     "market share", "market value", "market price", "market place", "A",
     "Our slice of the whole pie."),
    # ---------------------------------------------------------------- product
    (T_PROD, "Hard", "The fundamental benefit a customer really buys, such as 'clean clothes', is the",
     "core product", "actual product", "augmented product", "branded product", "A",
     "The core is the heart of it."),
    (T_PROD, "Hard", "Warranties, free installation and after-sales service added to a product form the",
     "augmented product", "core product", "product line", "product mix", "A",
     "Extras surround the actual good."),
    (T_PROD, "Hard", "The number of different product lines a company carries is its mix's",
     "width", "depth", "length", "consistency", "A",
     "Count the lines for width."),
    (T_PROD, "Easy", "The label on a tin of milk chiefly informs the buyer about",
     "contents and usage", "the owner of the shop", "the weather forecast", "competitors' prices", "A",
     "Labels teach before purchase."),
    # ---------------------------------------------------------------- services
    (T_SERV, "Medium", "A haircut cannot be touched, carried home or stored; it shows the service trait of",
     "intangibility", "variability", "perishability", "separability", "A",
     "You cannot hold a haircut."),
    (T_SERV, "Medium", "An empty hotel room tonight can never be sold again tomorrow, showing",
     "perishability", "intangibility", "heterogeneity", "ownership", "A",
     "Service shelves empty daily."),
    (T_SERV, "Medium", "A service is produced and consumed at the same moment, showing",
     "inseparability", "intangibility", "perishability", "durability", "A",
     "Making and using happen together."),
    (T_SERV, "Hard", "Two barbers in the same shop may give different haircuts, showing service",
     "heterogeneity", "homogeneity", "tangibility", "predictability", "A",
     "Quality varies with the giver."),
    # ---------------------------------------------------------------- pricing
    (T_PRICE, "Hard", "Fixed costs are N200,000; each unit sells at N150 with variable cost of N100. The break-even output is",
     "4,000 units", "2,000 units", "1,334 units", "6,000 units", "A",
     "Contribution of N50 covers N200,000."),
    (T_PRICE, "Medium", "Raising or lowering prices moment to moment, as ride apps do, is",
     "dynamic pricing", "penetration pricing", "cost-plus pricing", "barter pricing", "A",
     "The price breathes with demand."),
    (T_PRICE, "Medium", "Offering a basic version free while charging for premium features is the",
     "freemium model", "franchise model", "bundle model", "auction model", "A",
     "Free draws the crowd; premium pays."),
    # ---------------------------------------------------------------- distribution
    (T_DIST, "Medium", "Besides breaking bulk, a wholesaler helps small retailers by granting them",
     "credit facilities", "free holidays", "company shares", "voting rights", "A",
     "Goods today, money later."),
    (T_DIST, "Hard", "The utility created when a buyer finally owns the good he paid for is",
     "possession utility", "place utility", "form utility", "time utility", "A",
     "Ownership transfers value."),
    # ---------------------------------------------------------------- selling and promotion
    (T_SELL, "Hard", "The selling step where the salesperson finally asks for the order is",
     "closing", "prospecting", "approach", "follow-up", "A",
     "Asking for it seals the sale."),
    (T_SELL, "Hard", "Answering a buyer's worries about durability before closing is",
     "handling objections", "prospecting", "canvassing", "merchandising", "A",
     "Objections met, deals live."),
    (T_SELL, "Medium", "Calling the customer after delivery to confirm satisfaction is",
     "follow-up", "prospecting", "cold calling", "skimming", "A",
     "The last step keeps the buyer."),
    (T_SELL, "Medium", "A short news item a company sends to newspapers to announce a new product is a",
     "press release", "catalogue", "tender", "invoice", "A",
     "Newspapers print the news."),
    (T_SELL, "Hard", "The number of DIFFERENT people who see an advert at least once is its",
     "reach", "frequency", "impact", "circulation only", "A",
     "Count the unique pairs of eyes."),
    # ---------------------------------------------------------------- research
    (T_RES, "Medium", "Interviewing respondents over the phone is fastest for collecting data on a",
     "tight budget and timeline", "national census", "physical product test", "medical examination", "A",
     "Calls gather answers quickly."),
    (T_RES, "Easy", "Online survey forms sent by link are cheap and reach respondents",
     "anywhere with internet", "only in one city", "only by post", "only in the office", "A",
     "The link travels worldwide."),
    (T_RES, "Hard", "Studying the same panel of households month after month to track brand switching uses",
     "panel research", "retail audit", "street intercepts", "mystery shopping", "A",
     "The same faces tell trends."),
    # ---------------------------------------------------------------- consumer and business buying
    (T_BUY, "Medium", "A family that prefers pounded yam to rice because of tradition is shaped by its",
     "culture", "income", "age", "occupation", "A",
     "Culture orders the family menu."),
    (T_BUY, "Medium", "The neighbour whose phone everyone asks about before buying is an",
     "opinion leader", "opinion follower", "late adopter", "retailer", "A",
     "The street trusts his word."),
    (T_BUY, "Hard", "In the spread of a new product, the very first group to buy it is the",
     "innovators", "early majority", "laggards", "late majority", "A",
     "They buy before the crowd."),
    (T_BUY, "Medium", "Business buyers differ from household buyers because they purchase in",
     "larger quantities on contract", "tiny retail amounts", "only at festivals", "only with cash", "A",
     "Big orders, long agreements."),
    (T_BUY, "Hard", "A bakery's demand for flour exists only because households demand bread; this is",
     "derived demand", "elastic demand", "latent demand", "joint demand", "A",
     "The oven follows the table."),
    # ---------------------------------------------------------------- digital and global
    (T_DIG, "Medium", "Posts a page earns naturally without paying are",
     "organic results", "paid results", "spam posts", "bots", "A",
     "Quality earns free reach."),
    (T_DIG, "Hard", "Showing an advert to a visitor who left the website without buying is",
     "retargeting", "prospecting", "skimming", "franchising", "A",
     "The advert chases the cart."),
    (T_DIG, "Hard", "Serving two versions of a landing page to see which converts better is",
     "A/B testing", "data mining", "crowdsourcing", "cold calling", "A",
     "Two pages fight; one wins."),
    (T_DIG, "Medium", "Photos and reviews that happy customers post themselves are",
     "user-generated content", "press releases", "branded adverts", "tenders", "A",
     "Happy fans make the marketing."),
    (T_DIG, "Hard", "Changing a product's recipe or pack to suit each foreign market is",
     "adaptation", "standardisation", "consolidation", "segmentation", "A",
     "Each market gets its own."),
    (T_DIG, "Medium", "Marketing that stresses care for the environment, like recyclable packs, is",
     "green marketing", "grey marketing", "red marketing", "bulk marketing", "A",
     "Green sells responsibility."),
    (T_DIG, "Medium", "Replying to every comment and complaint on a brand's page builds",
     "an online community", "a price war", "a monopoly", "a cartel", "A",
     "Conversation keeps customers."),
]

build_batch(
    S,
    "batch_100_waec_marketing2.json",
    "100",
    "WAEC Marketing round 2 (Round 19 lift): SWOT, external environment, "
    "market share, core and augmented product, mix width, labelling, the "
    "four service characteristics (intangibility, perishability, "
    "inseparability, heterogeneity), break-even 4,000 units, dynamic and "
    "freemium pricing, wholesaler credit, possession utility, closing, "
    "objection handling, follow-up, press release, reach, phone and online "
    "surveys, panel research, culture, opinion leaders, innovators, B2B "
    "buying, derived demand, organic results, retargeting, A/B testing, "
    "user-generated content, adaptation, green marketing, community "
    "building. Scanned against WAEC r1, NECO rounds 1-2 and the JAMB "
    "Commerce marketing items.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
