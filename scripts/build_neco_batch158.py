"""Batch 158 - WAEC Marketing round 6 (WAEC top-up, R29).

Grows WAEC Marketing from 190 toward ~226 with angles not yet in the
bank: SWOT analysis; cognitive dissonance after purchase; emotional
vs rational buying motives; reference groups; product mix width vs
depth, line pruning; the adoption process; diffusion's innovators;
brand loyalty; green marketing; price discrimination; channel
length; selective and exclusive distribution; inventory carrying
costs; reach vs frequency; persuasive vs informative advertising;
handling objections; the AIDA model; telemarketing; influencer and
viral marketing; conversion and landing pages; focus groups; quota
sampling; questionnaire design; marketing control; benefit
segmentation; positioning; the unique selling proposition. Scanned
against WAEC rounds 1-5, NECO Marketing (all rounds) and the JAMB
pool.

    python3 scripts/build_neco_batch158.py -> content/batch_158_waec_marketing6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_ENV = "Analysis and Buyer Behaviour"
T_PL = "Product Strategy Further"
T_PRI = "Pricing Further"
T_DIS = "Distribution Further"
T_PRO = "Promotion Further"
T_DIG = "Digital Marketing Further"
T_RES = "Research and Control"
T_SEG = "Segmentation and Positioning"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- analysis & behaviour
    (T_ENV, "Hard", "In SWOT analysis, the firm's own helpful internal factors are its",
     "strengths", "threats", "opportunities", "weaknesses", "A",
     "They lie within its walls."),
    (T_ENV, "Hard", "A buyer who begins to doubt his choice of phone the day after paying for it is experiencing",
     "cognitive dissonance", "brand loyalty", "post-purchase bliss", "market segmentation", "A",
     "The mind argues with the receipt."),
    (T_ENV, "Medium", "A student who buys a particular sneaker because his favourite musician wears them is moved by an",
     "emotional motive", "rational motive", "economic motive", "legal motive", "A",
     "Feeling, not arithmetic, paid."),
    (T_ENV, "Medium", "Friends, clubs and celebrities whose tastes sway a buyer's choices form his",
     "reference groups", "pressure groups", "focus groups", "trade groups", "A",
     "He dresses to please their eyes."),

    # ------------------------------------------------------------- product strategy
    (T_PL, "Hard", "A brewery produces beer, malt drinks and bottled water. The number of such different rows in its portfolio is the mix's",
     "width", "depth", "length", "consistency", "A",
     "Count the rows across the mix."),
    (T_PL, "Hard", "Within its beer row alone, the brewery offers lager, stout and ale, each in two pack sizes. This variety down one row is the line's",
     "depth", "width", "height", "breadth of trade", "A",
     "Count the rungs down one ladder."),
    (T_PL, "Medium", "Dropping weak items from a product line to tighten it is called line",
     "pruning", "stretching", "filling", "branding", "A",
     "The shears remove dead wood."),
    (T_PL, "Hard", "A customer who passes from awareness through trial to finally making a product his regular choice has completed the",
     "adoption process", "diffusion process", "buying cycle", "audit trail", "A",
     "Steps from hearing to habit."),
    (T_PL, "Hard", "In the diffusion of a new gadget, the small daring group that buys first is the",
     "innovators", "laggards", "late majority", "early majority", "A",
     "They queue before the dawn release."),
    (T_PL, "Medium", "A shopper who rejects all rival brands and searches the town for one name shows",
     "brand loyalty", "brand switching", "price hunting", "impulse buying", "A",
     "Her heart has one address."),
    (T_PL, "Medium", "Packaging and products designed to protect the environment belong to",
     "green marketing", "grey marketing", "black marketing", "mass marketing", "A",
     "The planet is also a customer."),

    # ------------------------------------------------------------- pricing
    (T_PRI, "Hard", "Charging students one price at the campus gate and another at the city gate for the same film show is",
     "price discrimination", "price lining", "loss leading", "price fixing", "A",
     "Same reel, different tolls."),
    (T_PRI, "Hard", "Counting the levels between producer and final consumer gives the channel's",
     "length", "width", "depth", "reach", "A",
     "Each middleman adds a storey."),

    # ------------------------------------------------------------- distribution
    (T_DIS, "Medium", "Shopping goods like televisions are usually sold through a few carefully chosen dealers, a policy of",
     "selective distribution", "intensive distribution", "exclusive distribution", "direct distribution", "A",
     "Some doors, not all doors."),
    (T_DIS, "Medium", "A luxury watch maker allowing only one appointed shop per city practises",
     "exclusive distribution", "intensive distribution", "selective distribution", "mass distribution", "A",
     "Scarcity guards the crown."),
    (T_DIS, "Hard", "The costs of storing, insuring and financing goods held in a warehouse are called",
     "inventory carrying costs", "selling costs", "ordering salaries", "promotional costs", "A",
     "Goods sleeping in store eat money."),

    # ------------------------------------------------------------- promotion
    (T_PRO, "Medium", "During the campaign, two million different Lagos residents heard the jingle at least once. That count of unique listeners measures the advert's",
     "reach", "frequency", "circulation only", "impact", "A",
     "How wide the net is cast."),
    (T_PRO, "Medium", "How often, on average, one person meets the advert is its",
     "frequency", "reach", "cost rate", "rating point", "A",
     "How often the drum beats."),
    (T_PRO, "Medium", "An advert that argues a product's merits to change your mind is",
     "persuasive advertising", "informative advertising", "reminder advertising", "classified advertising", "A",
     "It seeks conversion, not news."),
    (T_PRO, "Hard", "Answering a hesitant customer's worries about price and durability is the selling step of",
     "handling objections", "prospecting", "closing", "following up", "A",
     "Doubts are answered, then the sale."),
    (T_PRO, "Hard", "The AIDA model claims a good advert wins attention, interest and desire before winning",
     "action", "agreement", "admission", "advance payment", "A",
     "The last gate is the purchase."),

    # ------------------------------------------------------------- digital
    (T_DIG, "Medium", "Selling to customers by telephone, whether called or calling, is",
     "telemarketing", "ambush marketing", "word-of-mouth", "catalogue selling", "A",
     "The handshake travels by wire."),
    (T_DIG, "Medium", "Paying a popular online personality to show a product to followers is",
     "influencer marketing", "viral marketing", "guerrilla marketing", "drip marketing", "A",
     "Borrowed fame sells the goods."),
    (T_DIG, "Medium", "Content so entertaining that users spread it themselves is the engine of",
     "viral marketing", "direct mail", "teleshopping", "trade fairs", "A",
     "The audience becomes the medium."),
    (T_DIG, "Hard", "The web page a visitor lands on after clicking an advert, built to push one action, is the",
     "landing page", "home page only", "sitemap", "banner", "A",
     "One door leads to one request."),

    # ------------------------------------------------------------- research & control
    (T_RES, "Hard", "A researcher gathers eight housewives to discuss a new seasoning freely. The method is a",
     "focus group", "census count", "store audit", "shelf test", "A",
     "Talk, not tally, carries the day."),
    (T_RES, "Medium", "Sampling in which the researcher simply fills a quota of respondents by judgement is",
     "quota sampling", "random sampling", "systematic sampling", "stratified sampling", "A",
     "No lottery, just his count."),
    (T_RES, "Hard", "A questionnaire item like 'Do you agree this excellent soap is the best?' is rejected because it is",
     "leading", "double-barrelled only", "too short", "open-ended", "A",
     "It plants its own answer."),
    (T_RES, "Medium", "Comparing actual sales with planned sales and probing the gap is the work of",
     "marketing control", "market share", "product mix", "positioning", "A",
     "Plans are judged by their score."),

    # ------------------------------------------------------------- segmentation & positioning
    (T_SEG, "Hard", "Dividing a toothpaste market into buyers seeking whiteness, freshness or cavity protection is",
     "benefit segmentation", "gender segmentation", "age segmentation", "income segmentation", "A",
     "The sought gain draws the line."),
    (T_SEG, "Medium", "Fixing a clear place for a brand in the consumer's mind against rivals is",
     "positioning", "packaging", "pricing", "placarding", "A",
     "A corner of the head, won and held."),
    (T_SEG, "Medium", "The one benefit a brand claims to deliver better than any rival is its",
     "unique selling proposition", "unit sales plan", "universal sales price", "united stock policy", "A",
     "The promise nobody else owns."),
]

build_batch(
    S,
    "batch_158_waec_marketing6.json",
    "158",
    "WAEC Marketing round 6 (R29 top-up): SWOT strengths, cognitive "
    "dissonance, emotional motive via sneakers, reference groups; mix "
    "width vs depth, line pruning, adoption process, innovators first, "
    "brand loyalty, green marketing; price discrimination at the "
    "campus gate, channel length; selective and exclusive "
    "distribution, inventory carrying costs; reach vs frequency, "
    "persuasive advertising, handling objections, AIDA; telemarketing, "
    "influencers, viral spread, landing page; focus group, quota "
    "sampling, leading questions, marketing control; benefit "
    "segmentation, positioning, USP. Scanned against WAEC rounds 1-5, "
    "NECO Marketing (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
