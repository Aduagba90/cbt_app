"""Batch 183 - WAEC Marketing round 7 (WAEC top-up, R35).

Grows WAEC Marketing from 222 toward ~254 with angles not yet in
the bank: the four Ansoff growth strategies; harvesting a tired
dog; cannibalisation; repositioning; irregular demand; market
potential; delighted customers; the right to redress; unsought
goods; installations among industrial goods; the slogan; celebrity
endorsement; comparative advertising; newspaper copy advantage;
the with-pack premium; sweepstakes; the promotional allowance; the
pre-approach step; price fixing against price wars; predatory
pricing; the co-operative store; the cash-and-carry wholesaler;
the franchising royalty; affiliate marketing; the lead magnet;
cost per thousand impressions; buying by tender; the press
conference; lobbying as public relations. Scanned against WAEC
rounds 1-6, NECO Marketing (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch183.py -> content/batch_183_waec_marketing7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_CON = "Marketing Concepts and Strategy"
T_PB = "Product and Branding"
T_PS = "Product Strategy Further"
T_PRI = "Pricing"
T_AD = "Promotion and Advertising"
T_PRF = "Promotion Further"
T_PUB = "Promotion and Publicity"
T_SEL = "Personal Selling Steps"
T_CH = "Channels of Distribution"
T_DIG = "Digital Marketing Further"
T_CBR = "Consumer Behaviour and Rights"
T_RES = "Marketing Research and Control"

PASSAGES = []
PQ = []

Q = [
    (T_CON, "Medium", "A brewery selling more of its present beers to its present customers is pursuing the growth strategy of market",
     "penetration", "development",
     "diversification", "skimming", "A",
     "Same product, same buyers, more of them buying."),
    (T_CON, "Medium", "Taking an existing product into a brand-new region or country is market",
     "development", "penetration",
     "diversification", "saturation", "A",
     "Old goods find new addresses."),
    (T_CON, "Medium", "Launching a fresh product to the customers the firm already serves is product",
     "development", "penetration",
     "diversification", "harvesting", "A",
     "Known buyers meet a new offer."),
    (T_CON, "Hard", "A soft-drink maker opening a noodle factory for entirely new customers is venturing into",
     "diversification", "product development",
     "market development", "market penetration", "A",
     "New product and new market at once."),
    (T_CON, "Hard", "Cutting promotion and investment on a dying brand simply to squeeze its last profits is the strategy of",
     "harvesting", "penetrating",
     "repositioning", "pioneering", "A",
     "The old cow is milked, not fed."),
    (T_PS, "Hard", "When a firm's new biscuit steals the sales of its own older biscuit instead of rivals' sales, the effect is",
     "cannibalisation", "differentiation",
     "integration", "fragmentation", "A",
     "The young product eats its own parent."),
    (T_PB, "Hard", "Changing an ailing brand's image and target group to win fresh buyers is called",
     "repositioning", "rebranding the staff only",
     "line extension", "penetration pricing", "A",
     "The same goods move to a new corner of the mind."),
    (T_CON, "Hard", "Hillside resorts half empty outside public holidays face demand that is",
     "irregular", "latent",
     "negative", "full", "A",
     "The crowds come in tides, not streams."),
    (T_RES, "Hard", "The upper limit of sales every firm in an industry could achieve together, if marketing were perfect, is the",
     "market potential", "sales quota",
     "company forecast", "sales budget", "A",
     "The ceiling no firm alone can reach."),
    (T_CBR, "Medium", "A customer whose expectations are merely met goes away satisfied; one whose expectations are surpassed goes away",
     "delighted", "confused",
     "indifferent", "overcharged", "A",
     "Delight is what loyalty is built on."),
    (T_CBR, "Medium", "Beyond safety, information and choice, consumers also hold the right to",
     "redress when cheated", "the lowest price always",
     "free goods on complaint", "name the shop's manager", "A",
     "A wronged buyer may demand to be made whole."),
    (T_PB, "Medium", "Goods a consumer neither thinks of buying nor wishes to think about, like burial insurance, are",
     "unsought goods", "speciality goods",
     "convenience goods", "shopping goods", "A",
     "No one shops for them until fate forces it."),
    (T_PS, "Medium", "In industrial-goods classification, a factory's new assembly line counts as",
     "an installation", "an accessory",
     "a supply", "raw material", "A",
     "Big, long-lived capital equipment."),
    (T_PB, "Easy", "The short, memorable phrase a brand pins on its promise, like the words under a famous logo, is its",
     "slogan", "label",
     "byline in news", "trademark shape", "A",
     "Six words that carry the whole promise."),
    (T_AD, "Medium", "A Nollywood star appearing on television to praise a particular soap is engaged in",
     "celebrity endorsement", "publicity stunting",
     "corporate advertising", "trade promotion", "A",
     "A trusted face lends the brand its shine."),
    (T_AD, "Hard", "An advert that sets the firm's product beside a named rival's and lists points of difference is",
     "comparative advertising", "institutional advertising",
     "reminder advertising", "classified advertising", "A",
     "Mine against his, head to head."),
    (T_AD, "Medium", "A newspaper's great advantage over radio as an advertising medium is that it carries",
     "long, detailed copy the reader controls", "moving pictures in colour",
     "sound and music together", "the largest evening audience always", "A",
     "The reader may study every line at leisure."),
    (T_PRF, "Medium", "A free mug packed inside every bag of detergent is a sales-promotion tool known as a",
     "premium", "sample",
     "coupon", "rebate", "A",
     "A gift rides along with the purchase."),
    (T_PRF, "Medium", "A soft-drink firm prints winning codes under bottle caps, and lucky drinkers claim free airtime. This promotion is a",
     "sweepstake", "loyalty scheme",
     "trade allowance", "refund offer", "A",
     "Chance decides who pops the prize."),
    (T_PRF, "Hard", "A manufacturer paying a retailer to mount a special window display for its brand grants a",
     "promotional allowance", "quantity discount",
     "dealer loader only in kind", "slotting fee never", "A",
     "The shopkeeper is paid to showcase."),
    (T_SEL, "Medium", "Before calling on a prospect, the salesperson studies his business and needs. This preparing step is the",
     "pre-approach", "approach",
     "presentation", "prospecting", "A",
     "Know the man before you meet him."),
    (T_PRI, "Hard", "Two rival cement firms secretly agreeing to keep their prices high together are guilty of",
     "price fixing", "price leadership",
     "price discrimination", "price skimming", "A",
     "Competition is throttled by agreement."),
    (T_PRI, "Hard", "Selling below cost deliberately, intending to drive a weaker rival out of business, is",
     "predatory pricing", "penetration pricing",
     "loss-leader pricing", "psychological pricing", "A",
     "The deep pocket bleeds the small one out."),
    (T_CH, "Medium", "A retail store owned and run jointly by its member customers, sharing surplus among them, is a",
     "co-operative store", "department store",
     "multiple shop", "hypermarket", "A",
     "The buyers themselves own the till."),
    (T_CH, "Hard", "A wholesaler who sells strictly for cash, offers no credit and makes no delivery trades as a",
     "cash-and-carry wholesaler", "merchant wholesaler",
     "truck jobber", "broker", "A",
     "Bring your money and carry your goods."),
    (T_CH, "Medium", "The regular fee a franchisee keeps paying the franchisor for the continued right to trade under the famous name is the",
     "royalty", "levy",
     "commission", "premium bond", "A",
     "Every month a slice rides upstream."),
    (T_DIG, "Medium", "A blogger who earns a commission whenever his readers buy through his special links practises",
     "affiliate marketing", "viral marketing",
     "guerrilla marketing", "drip marketing", "A",
     "His recommendation, his commission."),
    (T_DIG, "Hard", "A free e-book offered on a website in exchange for a visitor's email address works as a",
     "lead magnet", "banner advert",
     "pop-up survey", "checkout nudge", "A",
     "The gift buys the address."),
    (T_DIG, "Hard", "The price an advertiser pays for every one thousand times an online advert is shown is called",
     "cost per mille", "cost per click",
     "cost per sale", "cost per lead", "A",
     "Mille is Latin for a thousand."),
    (T_CBR, "Hard", "Government departments and big firms inviting sealed bids and awarding the contract to the best offer buy by",
     "tender", "auction",
     "negotiated contract", "hedging", "A",
     "Sealed envelopes compete in silence."),
    (T_PUB, "Medium", "A firm summoning journalists to hear and question its directors announces its news through a",
     "press conference", "press release only",
     "public hearing", "house journal", "A",
     "The questions come with the news."),
    (T_PUB, "Hard", "A company's delegation meeting lawmakers to argue for a friendly bill is performing the public-relations activity of",
     "lobbying", "sponsoring",
     "publicising", "fund-raising", "A",
     "Quiet persuasion walks the corridors."),
]

build_batch(
    S,
    "batch_183_waec_marketing7.json",
    "183",
    "WAEC Marketing round 7 (R35 top-up): the four Ansoff growth "
    "strategies; harvesting; cannibalisation; repositioning; "
    "irregular demand; market potential; delighted customers; the "
    "right to redress; unsought goods; installations; the slogan; "
    "celebrity endorsement; comparative advertising; newspaper "
    "copy advantage; the with-pack premium; sweepstakes; the "
    "promotional allowance; pre-approach; price fixing; predatory "
    "pricing; the co-operative store; the cash-and-carry "
    "wholesaler; the franchising royalty; affiliate marketing; the "
    "lead magnet; cost per mille; buying by tender; the press "
    "conference; lobbying as public relations. Scanned against "
    "WAEC rounds 1-6, NECO Marketing (all rounds) and the JAMB "
    "pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
