"""Batch 124 - NECO Marketing round 4 (NECO top-up, Round 24).

Lifts NECO Marketing from 138 toward ~180 with angles not yet in any
bank: micro and macro environment, product-mix decisions, new-product
development steps, branding strategies, psychological and seasonal
pricing, channel conflict and cooperation, retailing trends, sales-force
compensation, media scheduling, efficiency and strategic control, and
international entry modes. Scanned against NECO rounds 1-3, WAEC
Marketing (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch124.py -> content/batch_124_neco_marketing4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_ENV = "The Marketing Environment"
T_PROD = "Product Decisions"
T_PRICE = "Pricing Strategies"
T_DIST = "Channel Dynamics and Retailing"
T_CTRL = "Marketing Organisation and Control"
T_INTL = "International Marketing"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- environment
    (T_ENV, "Medium", "Suppliers, competitors, customers and marketing intermediaries make up a firm's",
     "micro-environment", "macro-environment", "task-free environment", "demographic environment", "A",
     "The firm meets them daily."),
    (T_ENV, "Medium", "Political, economic, social and technological forces form the",
     "macro-environment", "micro-environment", "board of directors", "sales department", "A",
     "PEST scans read these forces."),
    (T_ENV, "Hard", "A drop in consumers' purchasing power hits a food firm through the",
     "economic environment", "legal environment", "physical environment", "internal environment", "A",
     "Tight belts trim the basket."),
    (T_ENV, "Medium", "Marketing intermediaries include",
     "agents and distributors", "tax authorities", "courts", "schools", "A",
     "They bridge producer and buyer."),
    (T_ENV, "Hard", "A firm's own finance and production departments belong to its",
     "internal environment", "macro-environment", "publics only", "demography", "A",
     "Management controls these parts."),

    # ------------------------------------------------------------- product decisions
    (T_PROD, "Medium", "The assortment of product lines a firm offers is its",
     "product mix", "product life cycle", "brand equity", "market share", "A",
     "Width and depth describe it."),
    (T_PROD, "Hard", "Adding a new flavour to an existing drink line is",
     "line extension", "brand extension", "new-to-world launch", "rebranding", "A",
     "The family name stretches."),
    (T_PROD, "Medium", "Using one trusted brand name on a completely new category is",
     "brand extension", "line extension", "co-branding only", "unbranding", "A",
     "The name leaps categories."),
    (T_PROD, "Hard", "New-product development usually ends with",
     "commercialisation", "idea screening", "concept testing", "brainstorming", "A",
     "Full launch crowns the work."),
    (T_PROD, "Medium", "The first stage of new-product development is",
     "idea generation", "test marketing", "pricing", "distribution", "A",
     "Ideas pour in before sieves."),
    (T_PROD, "Hard", "Deleting a weak product from the line is a",
     "product elimination decision", "line extension", "harvest strategy only", "test market", "A",
     "The market laggard is retired."),

    # ------------------------------------------------------------- pricing
    (T_PRICE, "Hard", "Charging N199 to suggest a bargain below N200 is",
     "psychological pricing", "cost-plus pricing", "zone pricing", "transfer pricing", "A",
     "The mind reads it as less."),
    (T_PRICE, "Hard", "Selling umbrellas dearer in the rainy season uses",
     "seasonal pricing", "penetration pricing", "bundle pricing", "by-product pricing", "A",
     "Demand's calendar sets the tag."),
    (T_PRICE, "Medium", "Charging different prices in different regions for the same item is",
     "geographical pricing", "odd pricing", "prestige pricing", "loss leading", "A",
     "Distance and zones decide."),
    (T_PRICE, "Medium", "Selling bread below cost to pull shoppers into a store is",
     "loss leading", "skimming", "markup pricing", "parity pricing", "A",
     "The cheap loaf sells the rest."),
    (T_PRICE, "Hard", "Pricing that signals high quality and status, like luxury watches, is",
     "prestige pricing", "penetration pricing", "discount pricing", "auction pricing", "A",
     "The high price is the point."),

    # ------------------------------------------------------------- channels and retailing
    (T_DIST, "Hard", "Disagreement between a producer and his distributor over margins is",
     "channel conflict", "channel cooperation", "vertical integration", "dual branding", "A",
     "Two channel members pull apart."),
    (T_DIST, "Medium", "When channel members work together to serve customers better, there is channel",
     "cooperation", "conflict", "closure", "rationing", "A",
     "Teamwork moves the goods."),
    (T_DIST, "Hard", "A producer owning his own retail outlets has adopted",
     "vertical integration", "horizontal fusion", "loose alliance", "franchise buying", "A",
     "One owner spans the chain."),
    (T_DIST, "Medium", "Small neighbourhood shops selling convenience goods are",
     "kiosks or corner shops", "departmental stores", "hypermarkets", "mail-order houses", "A",
     "They live on daily needs."),
    (T_DIST, "Medium", "A very large store combining supermarket and department lines is a",
     "hypermarket", "kiosk", "hawker's tray", "market stall", "A",
     "Bulk, variety and parking."),
    (T_DIST, "Hard", "Supermarkets keep prices relatively low mainly through",
     "self-service and bulk buying", "high-pressure selling", "credit sales only", "home visits", "A",
     "Fewer clerks, bigger orders."),
    (T_DIST, "Medium", "Automatic vending machines chiefly offer",
     "round-the-clock sales", "bargaining space", "personal advice", "credit terms", "A",
     "Coins buy at midnight too."),

    # ------------------------------------------------------------- organisation and control
    (T_CTRL, "Medium", "Paying salespeople a fixed salary plus a share of sales uses",
     "salary plus commission", "straight commission", "straight salary only", "piece wages only", "A",
     "Security of pay meets hunger for more."),
    (T_CTRL, "Hard", "Paying salespeople only a percentage of their sales is",
     "straight commission", "salary plus bonus only", "time rate", "coefficient pay", "A",
     "Without a sale there is no pay."),
    (T_CTRL, "Medium", "Sales territories are set mainly to give each salesperson",
     "a defined coverage area", "unlimited travel", "equal holidays", "one customer", "A",
     "Boundaries prevent clashes."),
    (T_CTRL, "Hard", "Comparing sales, costs and profits against the plan is",
     "efficiency control", "strategic control", "concept testing", "screening", "A",
     "Numbers audit the effort."),
    (T_CTRL, "Hard", "Checking whether the firm still exploits its opportunities is",
     "strategic control", "efficiency control", "stock control", "budget control", "A",
     "The marketing audit informs it."),
    (T_CTRL, "Medium", "A marketing audit is best described as",
     "a comprehensive review", "a daily cash count", "a staff party", "a product demo", "A",
     "Everything is examined afresh."),

    # ------------------------------------------------------------- international
    (T_INTL, "Medium", "The simplest way into a foreign market is usually",
     "exporting", "joint venturing", "direct investment", "licensing", "A",
     "Goods leave, the firm stays."),
    (T_INTL, "Hard", "Allowing a foreign firm to produce under your brand for a fee is",
     "licensing", "exporting", "acquisition", "consignment", "A",
     "The licence prints royalties."),
    (T_INTL, "Hard", "A firm and a local investor abroad founding a company together forms a",
     "joint venture", "franchise", "cartel", "consortium of banks only", "A",
     "Both parties share ownership."),
    (T_INTL, "Hard", "Building a factory abroad is the riskiest entry mode because it is",
     "direct investment", "exporting", "licensing", "indirect marketing", "A",
     "Big money sits in deep water."),
    (T_INTL, "Medium", "Standardising one advert worldwide saves cost but risks ignoring",
     "local cultures", "exchange rates", "shipping lanes", "factory sites", "A",
     "One joke carries many meanings."),
    (T_INTL, "Medium", "The entry mode that runs restaurants under one formula worldwide is",
     "franchising", "exporting", "consignment", "tendering", "A",
     "Local owners pay to copy it."),
    (T_INTL, "Hard", "Dumping in world trade means selling abroad at prices",
     "below the home price", "above the home price", "equal to cost plus half", "fixed by UN treaty", "A",
     "It usually provokes retaliation tariffs."),
    (T_INTL, "Medium", "A multinational firm operating in many countries chiefly seeks",
     "wider markets", "one national anthem", "shorter holidays", "fewer customers", "A",
     "Scale and cheaper inputs drive it."),
]

build_batch(
    S,
    "batch_124_neco_marketing4.json",
    "124",
    "NECO Marketing round 4 (Round 24 top-up): micro vs macro "
    "environment, PEST forces, purchasing power, intermediaries, internal "
    "environment, product mix, line vs brand extension, commercialisation "
    "and idea generation, product elimination, psychological, seasonal, "
    "geographical, prestige pricing and loss leading, channel conflict "
    "and cooperation, vertical integration, kiosks, hypermarkets, "
    "self-service economics, vending machines, salary plus commission "
    "and straight commission, sales territories, efficiency vs strategic "
    "control, the marketing audit, exporting, licensing, joint ventures, "
    "direct investment, standardisation risks, franchising, dumping and "
    "multinationals. Scanned against NECO rounds 1-3, WAEC Marketing "
    "(all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
