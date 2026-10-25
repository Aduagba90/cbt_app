"""Batch 133 - WAEC Marketing round 5 (WAEC top-up, Round 25).

Lifts WAEC Marketing from 153 toward ~190 with angles not yet in any
bank: micro vs macro environment forces (demographic, economic,
legal-political); psychographic and behavioural segmentation, mass vs
niche targeting; product life cycle stages and strategies; trademark,
packaging functions, product modification; cost-plus, skimming,
penetration and psychological pricing; primary vs secondary data,
research steps, probability sampling; publicity, PR vs advertising,
trade fairs, personal selling for industrial goods; zero-level
channels, channel conflict, online direct channels, search ads,
click-through rate; standardisation vs adaptation, dumping;
prospecting, closing and follow-up. Scanned against WAEC rounds 1-4,
NECO Marketing (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch133.py -> content/batch_133_waec_marketing5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_ENV = "The Marketing Environment"
T_SEG = "Segmentation and Targeting"
T_PL = "Product and Branding"
T_PRICE = "Pricing"
T_RES = "Marketing Research"
T_PROMO = "Promotion and Publicity"
T_CH = "Channels and E-marketing"
T_INTL = "International Marketing"
T_SELL = "Personal Selling Steps"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- environment
    (T_ENV, "Medium", "The near-at-hand actors that a marketing firm deals with daily make up its",
     "micro-environment", "macro-environment", "task-free zone", "external audit", "A",
     "The actors nearest the firm."),
    (T_ENV, "Medium", "Inflation, interest and exchange rates belong to the",
     "economic environment", "political environment", "social environment", "legal environment", "A",
     "Prices and credit live here."),
    (T_ENV, "Hard", "A new consumer-protection law forcing label changes is a",
     "legal-political force", "demographic force", "technological force", "cultural force", "A",
     "Legislatures move markets."),
    (T_ENV, "Medium", "A rising share of older persons in the population is a change in the",
     "demographic environment", "technological environment", "economic environment", "physical environment", "A",
     "People's ages reshape demand."),

    # ------------------------------------------------------------- segmentation
    (T_SEG, "Medium", "Grouping buyers by lifestyle, personality and social class is",
     "psychographic segmentation", "geographic segmentation", "demographic segmentation", "behavioural segmentation", "A",
     "It reads how people live and feel."),
    (T_SEG, "Medium", "Splitting a market by usage rate, readiness and loyalty is",
     "behavioural segmentation", "geographic segmentation", "psychographic segmentation", "demographic segmentation", "A",
     "Actions, not ages, decide it."),
    (T_SEG, "Hard", "Offering one product to the whole market without division is",
     "mass marketing", "niche marketing", "direct marketing", "micro marketing", "A",
     "One net is cast for all fish."),
    (T_SEG, "Hard", "Focusing all effort on one small but profitable corner of a market is",
     "niche marketing", "mass marketing", "differentiated marketing", "counter marketing", "A",
     "A small pond, fully owned."),

    # ------------------------------------------------------------- product
    (T_PL, "Medium", "The course of a product's sales and profits from launch to decline is its",
     "product life cycle", "the trade cycle", "the stock cycle", "the cash cycle", "A",
     "Every product walks this road."),
    (T_PL, "Hard", "In which product life cycle stage do sales rise fastest?",
     "growth", "introduction", "maturity", "decline", "A",
     "The steep climb of the curve."),
    (T_PL, "Hard", "Promotional spending is heaviest relative to sales at the",
     "introduction stage", "growth stage", "maturity stage", "decline stage", "A",
     "Awareness must be bought first."),
    (T_PL, "Medium", "A brand name, symbol or design given legal protection is a",
     "trademark", "patent", "copyright", "franchise", "A",
     "The law stands guard over it."),
    (T_PL, "Medium", "Which of these is NOT a function of packaging?",
     "fixing the selling price", "protecting the product", "aiding product use", "promoting the brand", "A",
     "Price lives outside the pack."),
    (T_PL, "Hard", "Improving a mature product's features, styling or quality to lift flagging sales is called",
     "product modification", "market penetration", "line stretching", "brand stretching", "A",
     "Old goods get new clothes."),

    # ------------------------------------------------------------- pricing
    (T_PRICE, "Medium", "Cost-plus pricing works by",
     "adding a mark-up to cost", "matching the rival's price", "testing buyer feelings", "bidding below cost", "A",
     "Cost first, margin on top."),
    (T_PRICE, "Hard", "Launching a new gadget at a high price and cutting it later is",
     "market skimming", "penetration pricing", "predatory pricing", "psychological pricing", "A",
     "Cream is taken before milk."),
    (T_PRICE, "Hard", "A low introductory price chosen to capture share quickly is",
     "penetration pricing", "market skimming", "prestige pricing", "loss-leader pricing", "A",
     "Enter cheap, conquer, then earn."),
    (T_PRICE, "Medium", "Tagging an item at N999 instead of N1,000 uses",
     "psychological pricing", "geographical pricing", "promotional pricing", "differential pricing", "A",
     "The eye reads nine as much less."),

    # ------------------------------------------------------------- research
    (T_RES, "Medium", "Information gathered afresh for the problem at hand is called",
     "primary data", "secondary data", "internal data", "census data", "A",
     "First-hand and purpose-built."),
    (T_RES, "Medium", "Census tables and trade journals already published provide",
     "secondary data", "primary data", "field data", "observational data", "A",
     "Others gathered it first."),
    (T_RES, "Hard", "Sound marketing research always begins by",
     "defining the problem", "drafting questionnaires", "collecting field data", "sampling the population", "A",
     "A blurred question wastes all."),
    (T_RES, "Hard", "A sample in which every population member has a known chance of selection is",
     "probability sampling", "quota sampling", "judgement sampling", "convenience sampling", "A",
     "Chance, not choice, picks them."),

    # ------------------------------------------------------------- promotion
    (T_PROMO, "Medium", "Free news mention of a firm's new product is",
     "publicity", "advertising", "sales promotion", "personal selling", "A",
     "No invoice rides with the news."),
    (T_PROMO, "Medium", "Public relations differs from advertising chiefly in that it",
     "aims at goodwill, not sales", "sells space in papers", "targets only dealers", "avoids the public eye", "A",
     "Goodwill is its quiet product."),
    (T_PROMO, "Medium", "For an industrial-goods firm, trade fairs chiefly serve to",
     "display goods to many buyers", "replace the sales force", "fix market prices", "store finished goods", "A",
     "Many buyers meet one stand."),
    (T_PROMO, "Hard", "Selling costly industrial machinery relies most heavily on",
     "personal selling", "radio jingles", "billboard adverts", "consumer coupons", "A",
     "Machines need explaining hands."),

    # ------------------------------------------------------------- channels
    (T_CH, "Medium", "A channel of distribution with no middlemen at all is described as",
     "a zero-level channel", "a one-level channel", "a two-level channel", "a reverse channel", "A",
     "Producer meets consumer directly."),
    (T_CH, "Hard", "A serious quarrel over margins between a producer and his retailer is",
     "channel conflict", "channel leadership", "channel cooperation", "channel partnering", "A",
     "Partners in one pipe quarrel."),
    (T_CH, "Medium", "A company selling directly through its own website operates",
     "an online direct channel", "a wholesale channel", "a vending channel", "an agency channel", "A",
     "The shop window never closes."),
    (T_CH, "Hard", "Sponsored links that appear beside search-engine results are called",
     "search ads", "pop-up ads", "banner ads", "outdoor ads", "A",
     "They answer typed questions."),
    (T_CH, "Medium", "The proportion of email recipients who click a campaign link is the",
     "click-through rate", "bounce rate", "market share", "penetration rate", "A",
     "Clicks measure real interest."),

    # ------------------------------------------------------------- international
    (T_INTL, "Medium", "Offering an identical product and message worldwide is called",
     "standardisation", "adaptation", "localisation", "nationalisation", "A",
     "One recipe for every table."),
    (T_INTL, "Hard", "Adjusting a product's formula or package to suit a foreign market is",
     "adaptation", "standardisation", "counterfeiting", "dumping", "A",
     "The product bends to the buyer."),
    (T_INTL, "Hard", "Exporting goods at prices below the home market to clear surplus is",
     "dumping", "skimming", "hoarding", "hedging", "A",
     "Cheap floods can drown local mills."),

    # ------------------------------------------------------------- selling steps
    (T_SELL, "Medium", "The personal selling step of hunting out likely buyers is",
     "prospecting", "closing", "handling", "following up", "A",
     "Names are gathered before calls."),
    (T_SELL, "Hard", "Asking for the order outright is known in selling as",
     "closing", "prospecting", "presentation", "pre-approach", "A",
     "The question that wins the sale."),
    (T_SELL, "Medium", "A salesperson's follow-up after a sale chiefly aims at",
     "repeat business", "higher taxes", "longer meetings", "cheaper travel", "A",
     "The second sale starts today."),
]

build_batch(
    S,
    "batch_133_waec_marketing5.json",
    "133",
    "WAEC Marketing round 5 (Round 25 top-up): micro-environment, "
    "economic environment, legal-political force, demographic change; "
    "psychographic and behavioural segmentation, mass vs niche "
    "marketing; product life cycle and its stages, trademark, packaging "
    "non-functions, product modification; cost-plus, skimming, "
    "penetration and N999 psychological pricing; primary vs secondary "
    "data, problem definition first, probability sampling; publicity, "
    "PR vs advertising, trade fairs, personal selling for machinery; "
    "zero-level channel, channel conflict, online direct channel, "
    "search ads, click-through rate; standardisation, adaptation, "
    "dumping; prospecting, closing, follow-up. Scanned against WAEC "
    "rounds 1-4, NECO Marketing (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
