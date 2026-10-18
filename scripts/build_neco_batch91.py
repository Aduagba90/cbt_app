"""Batch 091 - NECO Marketing round 2 (NECO lift, Round 18).

NECO Marketing objective draws 60 items; the bank stood at 60. This lift
adds fresh items - product topics new to the bank (decline stage,
convenience/specialty/impulse goods, private label, mix depth, test
marketing), pricing (competition-based, price war, bundling, prestige,
quantity discount, inelastic demand), place (zero-level channel, agents vs
merchants, intensive distribution), promotion (prospecting, AIDA, BOGOF,
reminder advertising, sponsorship, media choice), consumer behaviour (need
recognition, loyalty, word-of-mouth, perceived risk, family decisions),
research (secondary data, leading questions, sampling, pilot study,
internal data) and digital (conversion rate, search ads, content
marketing, social care, opt-in email).

    python3 scripts/build_neco_batch91.py -> content/batch_091_neco_marketing2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_PROD = "Product and Branding"
T_PRICE = "Pricing"
T_DIST = "Distribution Channels"
T_PROM = "Promotion"
T_CONS = "Consumer Behaviour"
T_RES = "Marketing Research"
T_DIG = "E-Commerce and Customer Care"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- product
    (T_PROD, "Medium", "Sales and profits both sliding steadily month after month signal a product in the",
     "decline stage", "growth stage", "maturity stage", "introduction stage", "A",
     "The product is dying slowly."),
    (T_PROD, "Easy", "Bread and newspapers, bought often with little thought, are",
     "convenience goods", "specialty goods", "shopping goods", "industrial goods", "A",
     "Customers grab them on the way."),
    (T_PROD, "Medium", "A buyer who insists on one particular luxury watch and will travel to get it is shopping for",
     "specialty goods", "convenience goods", "impulse goods", "staple farm inputs", "A",
     "Only that one brand will satisfy him."),
    (T_PROD, "Easy", "Sweets placed at the checkout till for unplanned buying are",
     "impulse goods", "specialty goods", "durable goods", "capital goods", "A",
     "The till triggers the buying urge."),
    (T_PROD, "Medium", "The brand name a supermarket owns for the products it sells is a",
     "private label brand", "manufacturer's brand", "generic name", "licensed brand", "A",
     "The seller, not the maker, owns it."),
    (T_PROD, "Hard", "The number of sizes and flavours offered within one product line is the line's",
     "depth", "width", "length", "mix", "A",
     "Depth counts the variants."),
    (T_PROD, "Medium", "Selling a new drink in one small town first to gauge buyers' reaction is",
     "test marketing", "penetration pricing", "skimming", "niche targeting", "A",
     "The town becomes the trial lab."),
    # ---------------------------------------------------------------- pricing
    (T_PRICE, "Medium", "Setting your price by watching what rivals charge is called",
     "competition-based pricing", "cost-plus pricing", "penetration pricing", "psychological pricing", "A",
     "Rivals' prices set the pace."),
    (T_PRICE, "Easy", "Two rival filling stations cutting prices against each other again and again are fighting a",
     "price war", "price freeze", "trade embargo", "bargain fair", "A",
     "Everyone's profit bleeds."),
    (T_PRICE, "Medium", "Offering soap and detergent together in one pack at a single price is",
     "bundle pricing", "loss-leader pricing", "skimming", "prestige pricing", "A",
     "Two items, one combined price."),
    (T_PRICE, "Medium", "Keeping the price of a wristwatch deliberately high to signal quality is",
     "prestige pricing", "penetration pricing", "bundle pricing", "cost-plus pricing", "A",
     "The price itself flatters the good."),
    (T_PRICE, "Easy", "A discount given for buying in large quantities is a",
     "quantity discount", "cash discount", "trade discount", "seasonal discount", "A",
     "Bigger orders earn bigger cuts."),
    (T_PRICE, "Hard", "If a small rise in the price of salt barely reduces the quantity bought, demand for salt is",
     "inelastic", "elastic", "unitary", "perfectly elastic", "A",
     "Necessities resist price changes."),
    # ---------------------------------------------------------------- place
    (T_DIST, "Easy", "A marketing channel that contains no middleman at all is described as",
     "a zero-level channel", "a one-level channel", "an indirect channel", "a reverse channel", "A",
     "Producer meets consumer directly."),
    (T_DIST, "Hard", "Unlike a merchant wholesaler, an agent never",
     "owns the goods he sells", "earns any commission", "meets the buyers", "stores any goods at all", "A",
     "Agents arrange sales, never owning stock."),
    (T_DIST, "Medium", "Stocking a soft drink in every kiosk, supermarket and stall in town is",
     "intensive distribution", "exclusive distribution", "selective distribution", "direct distribution", "A",
     "Every shelf in town carries it."),
    # ---------------------------------------------------------------- promotion
    (T_PROM, "Hard", "A salesperson's first task of hunting out likely buyers is called",
     "prospecting", "closing", "follow-up", "handling objections", "A",
     "The list of prospects starts the sale."),
    (T_PROM, "Hard", "In the AIDA model of selling, the letters stand for",
     "Attention, Interest, Desire, Action", "Aim, Interest, Deal, Award", "Adverts, Incentives, Displays, Ads", "Appeal, Inform, Deliver, Assess", "A",
     "The buyer climbs four steps."),
    (T_PROM, "Easy", "A 'buy-one-get-one-free' offer is a tool of",
     "sales promotion", "personal selling", "publicity", "test marketing", "A",
     "The extra one rewards the buyer."),
    (T_PROM, "Medium", "An advert for an old, familiar soft drink that simply keeps the name in memory is",
     "reminder advertising", "informative advertising", "launch advertising", "recruitment advertising", "A",
     "Old friends need reminding."),
    (T_PROM, "Easy", "A brand paying to put its name on a stadium is engaged in",
     "sponsorship", "franchising", "wholesaling", "hire purchase", "A",
     "Its name rides the event."),
    (T_PROM, "Medium", "The first question in choosing an advertising medium is whether",
     "the target audience can be reached there", "the medium is the cheapest", "the owner likes the channel", "the advert looks colourful", "A",
     "Audience first, cost second."),
    # ---------------------------------------------------------------- consumer behaviour
    (T_CONS, "Easy", "The buying decision process begins when the buyer",
     "recognises a need", "pays for the goods", "compares prices", "discards the pack", "A",
     "Wanting comes before shopping."),
    (T_CONS, "Easy", "A customer buying the same milk brand every month shows",
     "brand loyalty", "brand switching", "impulse buying", "dissonance", "A",
     "Habit anchored to one name."),
    (T_CONS, "Medium", "Recommendations from trusted friends carry weight because they are seen as",
     "unbiased", "costly", "official", "legal", "A",
     "No seller pays the friend."),
    (T_CONS, "Medium", "Fearing a faulty product, a buyer prefers a well-known brand to reduce",
     "perceived risk", "cognitive effort", "price search", "shopping time", "A",
     "Familiar names feel safer."),
    (T_CONS, "Medium", "Household buying decisions are commonly",
     "joint among family members", "made by shopkeepers alone", "left to the youngest child", "decided by strangers", "A",
     "The family negotiates the basket."),
    # ---------------------------------------------------------------- research
    (T_RES, "Medium", "To a marketer, population figures already published by the NBS are",
     "secondary data", "primary data", "field data", "experimental data", "A",
     "Another body gathered them first."),
    (T_RES, "Hard", "A questionnaire item like 'Don't you agree our great product is the best?' is flawed because it is",
     "a leading question", "too short", "anonymous", "open-ended", "A",
     "It pushes the respondent to agree."),
    (T_RES, "Easy", "Surveying a small representative part of the population instead of everybody is",
     "sampling", "censoring", "stocking", "sorting", "A",
     "The sample stands for the whole."),
    (T_RES, "Hard", "Trying a questionnaire out on a few respondents first before the full survey is a",
     "pilot study", "market share", "census", "panel audit", "A",
     "The trial run exposes flaws."),
    (T_RES, "Medium", "A firm's own sales records are, to its researchers, which source of data?",
     "internal", "external", "primary field", "foreign", "A",
     "The data already lives in-house."),
    # ---------------------------------------------------------------- digital
    (T_DIG, "Hard", "Out of 1,000 visitors to an online shop, 30 placed orders. The 3% figure is the site's",
     "conversion rate", "bounce rate", "click rate", "growth rate", "A",
     "Visitors turned into buyers."),
    (T_DIG, "Medium", "The adverts that appear beside results the moment users type keywords are",
     "search ads", "billboard ads", "radio jingles", "cinema slides", "A",
     "They ride the search words."),
    (T_DIG, "Medium", "Winning customers by publishing helpful articles and videos rather than adverts is",
     "content marketing", "loss-leader pricing", "skim marketing", "guerrilla pricing", "A",
     "Usefulness draws the crowd."),
    (T_DIG, "Easy", "Answering a customer's complaint quickly on X (Twitter) is good",
     "online customer care", "market segmentation", "product bundling", "price fixing", "A",
     "Public replies show care."),
    (T_DIG, "Medium", "Marketers send email only to people who opted in because unsolicited mail is treated as",
     "spam", "survey", "invoice", "catalogue", "A",
     "Inboxes punish pushy senders."),
]

build_batch(
    S,
    "batch_091_neco_marketing2.json",
    "091",
    "NECO Marketing round 2 (Round 18 lift): product topics new to the bank "
    "(decline stage, convenience/specialty/impulse goods, private label, "
    "line depth, test marketing), pricing (competition-based, price war, "
    "bundling, prestige, quantity discount, inelastic demand), place "
    "(zero-level channel, agents never owning goods, intensive "
    "distribution), promotion (prospecting, AIDA, buy-one-get-one-free, "
    "reminder advertising, sponsorship, media choice by audience), consumer "
    "behaviour (need recognition, loyalty, trusted friends, perceived risk, "
    "joint family decisions), research (NBS secondary data, leading "
    "questions, sampling, pilot study, internal records) and digital "
    "(conversion rate, search ads, content marketing, social-media care, "
    "opt-in email). Scanned against NECO round 1, the WAEC twin and the "
    "JAMB Commerce marketing items.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
