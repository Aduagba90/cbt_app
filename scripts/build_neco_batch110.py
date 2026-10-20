"""Batch 110 - NECO Marketing round 3 (NECO top-up, Round 22).

Lifts NECO Marketing from 97 toward ~145 with fresh angles not yet in
any bank: the marketing information system, buyer decision steps,
organisational buying, market types, intermediary functions, physical
distribution and order processing, merchandising, selling qualities,
advertising ethics, consumerism, relationship and cause-related
marketing, e-marketing, product differentiation, brand loyalty and
diffusion adopter categories. Scanned against NECO rounds 1-2, WAEC
Marketing (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch110.py -> content/batch_110_neco_marketing3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_MIS = "Marketing Information and Research"
T_BUY = "Buying Behaviour"
T_MKTYPES = "Types of Markets"
T_DIST = "Intermediaries and Physical Distribution"
T_SELL = "Salesmanship"
T_ADV = "Advertising and Consumerism"
T_MOD = "Modern Marketing"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- MIS
    (T_MIS, "Medium", "A marketing information system gathers, analyses and",
     "distributes data for decisions", "prints staff payslips", "hires salesmen", "audits accounts only", "A",
     "Data flows to decision makers."),
    (T_MIS, "Medium", "Internal records, marketing intelligence and marketing research are parts of a",
     "marketing information system", "production plan", "personality test", "sales quota", "A",
     "Three streams feed the system."),
    (T_MIS, "Hard", "Data collected fresh for a specific problem is called",
     "primary data", "secondary data", "census data", "dead data", "A",
     "First-hand and purpose-built."),
    (T_MIS, "Medium", "Published NBS reports used in a study are",
     "secondary data", "primary data", "field data", "panel data", "A",
     "Someone else gathered them first."),
    (T_MIS, "Hard", "In research, the group selected to represent the whole market is the",
     "sample", "population", "census", "quota only", "A",
     "A slice stands for the whole."),
    (T_MIS, "Medium", "A hypothesis in marketing research is a",
     "statement to be tested", "final conclusion", "sales target", "budget line", "A",
     "The study confirms or rejects it."),

    # ------------------------------------------------------------- buying behaviour
    (T_BUY, "Hard", "The buyer's decision process runs from need recognition through information search and evaluation to",
     "purchase and post-purchase feeling", "production and packaging", "storage and insurance", "billing and audit", "A",
     "Five steps end with the verdict."),
    (T_BUY, "Medium", "Discomfort after buying a wrong item is called",
     "cognitive dissonance", "brand loyalty", "impulse buying", "habit", "A",
     "The mind second-guesses the wallet."),
    (T_BUY, "Medium", "Goods bought with little thought, like chewing gum at the till, are",
     "impulse purchases", "shopping goods", "speciality goods", "industrial goods", "A",
     "The till placement triggers them."),
    (T_BUY, "Hard", "A car, shopped carefully for features and price, is a",
     "shopping good", "convenience good", "impulse good", "perishable good", "A",
     "Buyers compare before paying."),
    (T_BUY, "Medium", "A buyer who insists on only one brand of watch shows",
     "brand loyalty", "brand switching", "price hunting", "dissonance", "A",
     "The same name wins every time."),
    (T_BUY, "Hard", "In the diffusion of a new product, the group that adopts last is the",
     "laggards", "innovators", "early majority", "early adopters", "A",
     "They wait until everyone owns one."),
    (T_BUY, "Medium", "The industrial market buys goods mainly to",
     "produce other goods", "eat and wear directly", "gift to relatives", "hoard them forever", "A",
     "Business use drives industrial buying."),

    # ------------------------------------------------------------- market types
    (T_MKTYPES, "Medium", "Individuals and households who buy for personal use form the",
     "consumer market", "industrial market", "reseller market", "government market", "A",
     "Personal use defines them."),
    (T_MKTYPES, "Medium", "Traders who buy goods to resell at a profit make up the",
     "reseller market", "consumer market", "factor market", "grey market", "A",
     "Profit on resale is their aim."),
    (T_MKTYPES, "Medium", "A market where raw cotton is traded is a",
     "commodity market", "capital market", "labour market", "money market", "A",
     "Raw produce changes hands there."),
    (T_MKTYPES, "Hard", "Government departments buying drugs for hospitals belong to the",
     "government market", "reseller market", "consumer market", "industrial market", "A",
     "Public spending powers them."),

    # ------------------------------------------------------------- intermediaries and distribution
    (T_DIST, "Medium", "Middlemen reduce the number of contacts between producers and customers by",
     "concentrating transactions", "increasing paperwork", "banning adverts", "closing markets", "A",
     "One middle link replaces many."),
    (T_DIST, "Medium", "Breaking bulk and assembling small lots are functions of",
     "marketing intermediaries", "final consumers", "central banks", "landlords", "A",
     "They reshape goods between ends."),
    (T_DIST, "Hard", "The set of firms that move goods and ownership from producer to consumer is the",
     "channel of distribution", "chain of stores only", "trade union", "cartel", "A",
     "The route the product travels."),
    (T_DIST, "Hard", "When a producer bypasses his wholesaler to serve retailers directly, the change is in his",
     "channel structure", "product mix", "price line", "staff list", "A",
     "The route itself is re-drawn."),
    (T_DIST, "Medium", "Order processing, warehousing, inventory control and transport make up",
     "physical distribution", "physical evidence", "public relations", "product planning", "A",
     "Goods must move and rest."),
    (T_DIST, "Medium", "Selling straight from the factory gate to the final user is the channel that is",
     "consumer", "wholesaler", "retailer", "agent", "A",
     "Direct selling skips the middlemen."),
    (T_DIST, "Hard", "Stock-outs on shelves damage a firm chiefly through",
     "lost sales", "cheaper storage costs", "faster stock turnover", "lower staff wages", "A",
     "Empty shelves send buyers to rivals."),
    (T_DIST, "Medium", "Attractive display of goods at the point of sale is called",
     "merchandising", "benchmarking", "brainstorming", "broking", "A",
     "The shelf sells silently."),

    # ------------------------------------------------------------- salesmanship
    (T_SELL, "Medium", "The first step in the personal selling process is",
     "prospecting", "closing", "handling objections", "follow-up", "A",
     "Find who might buy first."),
    (T_SELL, "Medium", "A good salesperson should above all be",
     "honest and patient", "loud and pushy", "careless with records", "rude to buyers", "A",
     "Trust closes more than noise."),
    (T_SELL, "Hard", "Identifying potential customers who need and can pay for a product is",
     "prospecting", "canvassing prices", "dispatching", "merchandising", "A",
     "The sales funnel starts here."),
    (T_SELL, "Medium", "A salesperson's demonstration of a product at the buyer's counter is",
     "a product demo approach", "blind prospecting", "tele-marketing only", "mail merging", "A",
     "He shows, not just tells."),

    # ------------------------------------------------------------- advertising and consumerism
    (T_ADV, "Medium", "The watchdog bodies that press for consumer protection make up the",
     "consumerism movement", "cartel movement", "labour movement", "green movement", "A",
     "'The consumer is king' is their cry."),
    (T_ADV, "Medium", "An advert is considered unethical when it is",
     "deceptive or exaggerated", "clearly priced", "signed by the firm", "placed in a paper", "A",
     "Lies sell nothing worth buying."),
    (T_ADV, "Hard", "APCON, the body that vets Nigerian advertising practice, stands for",
     "Advertising Practitioners Council of Nigeria", "Allied Producers Council of Nigeria", "Association of Print Content Owners of Nigeria", "Agency for Product Control of Nigeria", "A",
     "It regulates the advert trade."),
    (T_ADV, "Medium", "The advertising budget that matches a rival's spending uses the",
     "competitive-parity method", "percentage-of-sales method", "objective-and-task method", "affordable method", "A",
     "Keep up with the neighbour."),
    (T_ADV, "Hard", "Setting the budget from what the firm can spare is the",
     "affordable method", "objective-and-task method", "percentage method", "parity method", "A",
     "The purse decides the plan."),

    # ------------------------------------------------------------- modern marketing
    (T_MOD, "Medium", "Marketing that seeks long-term bonds instead of one-off sales is",
     "relationship marketing", "transaction marketing", "mass marketing", "counter marketing", "A",
     "Keep the customer for life."),
    (T_MOD, "Hard", "A firm linking its brand to a charity cause practises",
     "cause-related marketing", "greenwashing only", "test marketing", "demographic marketing", "A",
     "Buying supports the cause."),
    (T_MOD, "Medium", "Using websites, email and social platforms to reach buyers is",
     "e-marketing", "bulk marketing", "demarketing", "offline retailing", "A",
     "The market square moved online."),
    (T_MOD, "Hard", "Efforts to REDUCE demand for a harmful product are called",
     "demarketing", "remarketing", "skimming", "branding", "A",
     "Sometimes less demand is the goal."),
    (T_MOD, "Medium", "Making a product stand out from close substitutes is",
     "product differentiation", "product deletion", "price fixing", "mass selling", "A",
     "A visible edge wins attention."),
    (T_MOD, "Medium", "The added value a famous name gives a product is called",
     "brand equity", "brand fatigue", "price elasticity", "product depth", "A",
     "The name itself is worth money."),
    (T_MOD, "Medium", "Online tools help small firms market chiefly because they are",
     "cheap and wide-reaching", "slow but steady", "licensed to banks", "tied to one city", "A",
     "Little budget, big audience."),
]

build_batch(
    S,
    "batch_110_neco_marketing3.json",
    "110",
    "NECO Marketing round 3 (Round 22 top-up): marketing information "
    "system and its parts, primary vs secondary data, samples and "
    "hypotheses, buyer decision steps, cognitive dissonance, impulse vs "
    "shopping goods, brand loyalty, laggards, the industrial market, "
    "consumer, reseller, commodity and government markets, middlemen "
    "contact-reduction, bulk-breaking, channel structure and physical "
    "distribution, stock-out costs, merchandising, prospecting and "
    "salesperson qualities, demo approach, consumerism, advertising "
    "ethics and APCON, competitive-parity and affordable budgets, "
    "relationship and cause-related marketing, e-marketing, "
    "demarketing, differentiation, brand equity and online tools. "
    "Scanned against NECO rounds 1-2, WAEC Marketing (all rounds) and "
    "the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
