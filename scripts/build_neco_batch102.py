"""Batch 102 - WAEC Marketing round 3 (WAEC top-up, Round 21).

Lifts WAEC Marketing from 99 toward ~140 with syllabus angles not yet in
the bank: marketing concept eras, the 4Ps and 7Ps, segmentation bases,
product life cycle, branding and packaging, channel levels and
intermediaries, retail and wholesale types, storage and transport,
sales-promotion tools, advertising media choice, publicity, positioning,
niche vs mass marketing, buying motives, consumer rights, forecasting,
test marketing, marketing audit and control, CRM and sponsorship.
Scanned against WAEC rounds 1-2, NECO Commerce/Marketing items and the
JAMB pool.

    python3 scripts/build_neco_batch102.py -> content/batch_102_waec_marketing3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_CONCEPT = "Marketing Concepts and Strategy"
T_MIX = "The Marketing Mix"
T_SEG = "Segmentation, Targeting and Positioning"
T_PROD = "Product and Branding"
T_DIST = "Channels of Distribution"
T_PROMO = "Promotion and Advertising"
T_BUY = "Consumer Behaviour and Rights"
T_CTRL = "Marketing Research and Control"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------- concepts
    (T_CONCEPT, "Medium", "A firm that starts from the customer's needs and works backwards practises the",
     "marketing concept", "production concept", "selling concept", "product concept", "A",
     "The customer comes first here."),
    (T_CONCEPT, "Medium", "The old idea that a good product will sell itself is the",
     "product concept", "marketing concept", "societal concept", "relationship concept", "A",
     "Quality alone was thought to sell."),
    (T_CONCEPT, "Hard", "The societal marketing concept balances company profit, consumer wants and",
     "society's well-being", "competitors' prices", "staff bonuses", "media ratings", "A",
     "All three interests are weighed."),
    (T_CONCEPT, "Medium", "In the classic mix, the fourth P after product, price and place is",
     "promotion", "people", "process", "planning", "A",
     "The fourth P communicates."),
    (T_CONCEPT, "Hard", "Services marketing widens the mix by adding people, process and",
     "physical evidence", "publicity", "packaging", "planning", "A",
     "That yields the seven Ps."),
    (T_CONCEPT, "Medium", "STP in marketing planning stands for segmentation, targeting and",
     "positioning", "pricing", "promotion", "packaging", "A",
     "The last step plants the brand in the mind."),
    (T_CONCEPT, "Easy", "A marketing objective should be SMART, where M stands for",
     "measurable", "modern", "movable", "moderate", "A",
     "You must be able to count it."),
    (T_CONCEPT, "Hard", "In AIDA, the letter D stands for",
     "desire", "demand", "decision", "delivery", "A",
     "Interest grows into desire."),
    (T_CONCEPT, "Medium", "Selling the same product to the whole market with one offer is",
     "mass marketing", "niche marketing", "segment marketing", "direct marketing", "A",
     "One size fits all buyers."),
    (T_CONCEPT, "Medium", "A firm that serves one small, well-defined corner of the market uses",
     "niche marketing", "mass marketing", "trade marketing", "counter marketing", "A",
     "Small pond, full attention."),

    # ------------------------------------------------------- mix / product
    (T_MIX, "Hard", "Setting a high launch price for a new gadget, then lowering it later, is",
     "price skimming", "penetration pricing", "loss leading", "predatory pricing", "A",
     "You skim the early rich buyers."),
    (T_MIX, "Hard", "Charging a low launch price to grab market share quickly is",
     "penetration pricing", "price skimming", "prestige pricing", "odd pricing", "A",
     "You dive in low and wide."),
    (T_MIX, "Medium", "Pricing a product at N999 instead of N1,000 is called",
     "odd pricing", "cost-plus pricing", "going-rate pricing", "tie-in pricing", "A",
     "The odd figure feels cheaper."),
    (T_MIX, "Medium", "Adding a marked-up percentage to unit cost to set price is",
     "cost-plus pricing", "penetration pricing", "value pricing", "auction pricing", "A",
     "Cost plus a marked-up margin."),
    (T_MIX, "Medium", "Two products bundled together at one attractive price is",
     "product-bundle pricing", "captive pricing", "by-product pricing", "zone pricing", "A",
     "The pair sells as one deal."),
    (T_PROD, "Medium", "The name or symbol that marks one seller's goods apart from rivals' is the",
     "brand", "patent", "coupon", "tender", "A",
     "It marks the goods apart."),
    (T_PROD, "Hard", "The part of the brand that can be SPOKEN is the",
     "brand name", "trade mark", "brand mark", "copyright", "A",
     "Say it out loud to test it."),
    (T_PROD, "Medium", "A legally registered brand or part of it is protected as a",
     "trade mark", "trade name", "trade discount", "trade union", "A",
     "Registration blocks imitators."),
    (T_PROD, "Medium", "Packaging protects the product mainly by",
     "shielding it from damage", "advertising on radio", "cutting its price", "raising its weight", "A",
     "The pack guards the contents from harm."),
    (T_PROD, "Medium", "In the product life cycle, sales rise fast and profits appear in the",
     "growth stage", "introduction stage", "maturity stage", "decline stage", "A",
     "The market warms up to it."),
    (T_PROD, "Hard", "Sales peak and competition is fiercest at the",
     "maturity stage", "growth stage", "introduction stage", "development stage", "A",
     "Everyone fights over a flat pie."),
    (T_PROD, "Hard", "Falling sales and withdrawal of the product mark the",
     "decline stage", "maturity stage", "growth stage", "launch stage", "A",
     "The end of the road nears."),

    # ------------------------------------------------------- segmentation
    (T_SEG, "Medium", "Dividing a market by age groups and income levels is segmentation on",
     "demographic grounds", "geographic grounds", "psychographic grounds", "behavioural grounds", "A",
     "Age and income describe people."),
    (T_SEG, "Medium", "Segmenting buyers by lifestyle and personality is",
     "psychographic segmentation", "demographic segmentation", "geographic segmentation", "bulk segmentation", "A",
     "It reads the buyer's mind."),
    (T_SEG, "Medium", "Grouping customers by how often they use a product is",
     "behavioural segmentation", "geographic segmentation", "demographic segmentation", "industrial segmentation", "A",
     "Usage habits drive the split."),
    (T_SEG, "Hard", "The map that shows how consumers see competing brands is a",
     "perceptual map", "route map", "scale map", "pricing map", "A",
     "Positions cluster on the map."),
    (T_SEG, "Medium", "Planting a brand in the customer's mind as the best value is",
     "positioning", "packing", "branding", "blending", "A",
     "The brand owns a mental slot."),

    # ------------------------------------------------------- distribution
    (T_DIST, "Medium", "A producer selling directly to final consumers uses a",
     "zero-level channel", "one-level channel", "two-level channel", "three-level channel", "A",
     "No middleman stands between."),
    (T_DIST, "Medium", "The channel that runs producer, wholesaler, retailer, consumer has",
     "two middle levels", "one middle level", "three middle levels", "no middle level", "A",
     "Two intermediaries stand in."),
    (T_DIST, "Medium", "An agent who brings buyer and seller together without owning the goods works for",
     "commission", "salary only", "a share of profits", "a flat retainer only", "A",
     "Agents earn a percentage cut."),
    (T_DIST, "Hard", "A large self-service store stocking food and household items is a",
     "supermarket", "departmental store", "kiosk", "mail-order house", "A",
     "Trolleys and shelves, no counters."),
    (T_DIST, "Hard", "A store housing many departments under one roof, each with its own goods, is a",
     "departmental store", "supermarket", "hawker's stand", "tie-in shop", "A",
     "Each floor sells a different line."),
    (T_DIST, "Medium", "Shopping by post or phone with home delivery is",
     "mail-order retailing", "itinerant trading", "hire purchase", "barter", "A",
     "The goods travel to the buyer."),
    (T_DIST, "Hard", "Many identical shops owned by one firm spread across towns form a",
     "chain store", "corner shop", "cooperative kiosk", "duty-free shop", "A",
     "One owner, many branches."),
    (T_DIST, "Medium", "Warehousing creates time utility chiefly by",
     "storing goods until they are needed", "transporting goods faster", "insuring goods", "advertising goods", "A",
     "Goods wait for their season."),
    (T_DIST, "Medium", "For moving crude oil over long distances on land, the cheapest means is",
     "pipeline", "rail", "road tanker", "air freight", "A",
     "The liquid flows day and night."),
    (T_DIST, "Medium", "The fastest but costliest means of transporting goods is",
     "air transport", "sea transport", "rail transport", "pipeline", "A",
     "Speed costs money per kilo."),

    # ------------------------------------------------------- promotion
    (T_PROMO, "Medium", "A price-off coupon is a tool of",
     "sales promotion", "personal selling", "publicity", "market research", "A",
     "It pushes short-term buying."),
    (T_PROMO, "Medium", "A free sample attached to a pack is known as a",
     "premium offer", "trade fair", "tender", "franchise", "A",
     "The gift rides on the pack."),
    (T_PROMO, "Hard", "A customer loyalty programme rewards buyers for",
     "repeated purchases", "first visits only", "watching adverts", "returning defects", "A",
     "Points pile up with each sale."),
    (T_PROMO, "Medium", "Radio advertising's biggest advantage over television is its",
     "lower cost per announcement", "moving pictures", "colour display", "longer copy", "A",
     "Radio airtime costs far less."),
    (T_PROMO, "Hard", "Free news coverage of a firm's activities, not paid for, is",
     "publicity", "advertising", "sales promotion", "sponsoring", "A",
     "The media choose to carry it."),
    (T_PROMO, "Medium", "A billboard by the roadside is best for",
     "reminding many passers-by quickly", "explaining complex details", "targeting one buyer", "sealing contracts", "A",
     "Short and bold does the job."),
    (T_PROMO, "Hard", "Word-of-mouth marketing spreads fastest when customers are",
     "delighted beyond expectation", "overcharged quietly", "kept waiting longer", "ignored after sale", "A",
     "Joy travels mouth to mouth."),

    # ------------------------------------------------------- consumers
    (T_BUY, "Medium", "A buyer moved by a product's durability, not its beauty, acts on",
     "rational motives", "emotional motives", "impulse motives", "habitual motives", "A",
     "The head, not the heart, decides."),
    (T_BUY, "Medium", "Pride or fear that pushes a purchase is an",
     "emotional buying motive", "rational motive", "economy motive", "convenience motive", "A",
     "Feelings drive the wallet."),
    (T_BUY, "Medium", "The right to be told the truth about a product is the consumer's right to",
     "information", "safety", "redress", "choose", "A",
     "Labels and adverts must be honest."),
    (T_BUY, "Hard", "The government agency that protects Nigerian consumers from unfair practices is the",
     "FCCPC", "NAFDAC", "SON", "CBN", "A",
     "The competition and consumer body."),

    # ------------------------------------------------------- control
    (T_CTRL, "Medium", "Checking yearly sales against set targets is part of",
     "annual-plan control", "strategic control", "distribution control", "stock control", "A",
     "Plans need regular scorecards."),
    (T_CTRL, "Hard", "A comprehensive, systematic review of a firm's marketing environment is a",
     "marketing audit", "stock taking", "market survey only", "census", "A",
     "It audits everything at once."),
    (T_CTRL, "Medium", "Sales computed before a budget period, using past records, is",
     "sales forecasting", "sales promotion", "sales quota", "sales territory", "A",
     "Tomorrow's sales, guessed well."),
    (T_CTRL, "Medium", "Introducing a new product to a small town first to test reaction is",
     "test marketing", "mass marketing", "dumping", "franchising", "A",
     "The small town is the lab."),
    (T_CTRL, "Medium", "CRM software mainly helps a firm to",
     "manage customer data", "print annual reports", "hire new staff", "set income tax", "A",
     "Every customer's story is stored in it."),
    (T_CTRL, "Hard", "A firm paying to put its name on a football jersey is using",
     "sponsorship", "personal selling", "franchising", "tendering", "A",
     "Its name rides on the game."),
]

build_batch(
    S,
    "batch_102_waec_marketing3.json",
    "102",
    "WAEC Marketing round 3 (Round 21 top-up): marketing concept eras "
    "(product, selling, marketing, societal), 4Ps and 7Ps, STP, SMART and "
    "AIDA, mass vs niche marketing, skimming vs penetration vs odd vs "
    "cost-plus vs bundle pricing, brand name vs trade mark, packaging "
    "protection, product life cycle stages, segmentation bases "
    "(demographic, psychographic, behavioural), perceptual maps, "
    "positioning, channel levels, agents' commission, supermarket vs "
    "departmental vs chain vs mail-order retail, warehousing and "
    "transport modes, coupons, premiums, loyalty schemes, radio vs "
    "billboard media choice, publicity vs advertising, word-of-mouth, "
    "rational vs emotional motives, consumer rights and the FCCPC, "
    "annual-plan control, marketing audit, forecasting, test marketing, "
    "CRM and sponsorship. Scanned against WAEC rounds 1-2, NECO "
    "Commerce/Marketing and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
