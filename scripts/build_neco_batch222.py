"""Batch 222 - WAEC Marketing round 8 (WAEC top-up, R45).

Grows WAEC Marketing from 254 toward ~279 with angles verified absent
from the whole Marketing pool (528 items across WAEC and NECO):
generic brand; individual brand; testimonial; infomercial; outdoor
advertising (category angle - poster sites and painted walls, not the
banked billboard-use item); exhibition; showroom; haggling; cash on
delivery; order cycle; supply chain; third-party logistics;
cross-docking; pay per click; e-tailing; value for money; quality
control; seasonal discount; instalment buying; sales contest; sales
analysis; marketing budget; multichannel; shelf space; planogram.
Checked and avoided (already banked): cannibalisation, private label,
umbrella/family brand, celebrity endorsement, conversion rate, churn,
cart abandonment, customer lifetime value, benefit segmentation,
undifferentiated marketing, MIS, word-of-mouth (option hits),
demonstration, trade promotion, marketing control, push/pull
strategy, packaging functions, blue-chip-adjacent loyalty items,
family brand (= umbrella item).

    python3 scripts/build_neco_batch222.py -> content/batch_222_waec_marketing8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_PB = "Product and Branding"
T_PA = "Promotion and Advertising"
T_PP = "Promotion and Publicity"
T_CH = "Channels of Distribution"
T_DF = "Distribution Further"
T_PR = "Pricing"
T_DM = "Digital Marketing"
T_DMF = "Digital Marketing Further"
T_CB = "Consumer Behaviour and Rights"
T_PS = "Personal Selling and Promotion"
T_RC = "Marketing Research and Control"
T_CE = "Channels and E-marketing"

PASSAGES = []
PQ = []

Q = [
    (T_PB, "Medium", "Products that carry no brand name at all and are known only by the name of the product class itself, such as plain sachets labelled simply 'salt', are",
     "generic brands", "speciality brands",
     "fighting brands", "premium brands", "A",
     "No name distinguishes them but their price."),
    (T_PB, "Hard", "A soap maker gives each of its products a separate name — Joy for bathing soap, Spark for washing soap — instead of one family name. This naming policy is",
     "individual branding", "umbrella branding",
     "private labelling", "co-branding", "A",
     "Every product stands or falls on its own name."),
    (T_PB, "Medium", "The checks a firm carries out at every stage of production so that every unit leaving the factory meets the standard set for it are called",
     "quality control", "quantity discounting",
     "quota selling", "quick stocking", "A",
     "Bad units are caught before they ship out."),
    (T_PA, "Easy", "A satisfied customer appears in a television advert saying how a cough mixture cured her cough. Her statement in the advert is a",
     "testimonial", "preview",
     "press release", "trade journal", "A",
     "A real user's own words vouch for the goods."),
    (T_PA, "Medium", "A paid television programme that may last half an hour, demonstrating a blender or a fitness machine and giving a phone number to order from, is called an",
     "infomercial", "interlude",
     "inset", "intro advert", "A",
     "It is half information and half commercial."),
    (T_PA, "Easy", "Advertising done on poster sites, painted walls, bus shelters and street furniture, where people see it as they move about outdoors, is known as",
     "outdoor advertising", "indoor display",
     "direct mail", "point-of-sale audio", "A",
     "The message waits for passers-by on the streets."),
    (T_PP, "Medium", "An event at which many firms gather under one roof, each at its own stand, to display their goods and meet customers face to face, is an",
     "exhibition", "auction",
     "inventory", "inquest", "A",
     "Buyers walk from stand to stand all day."),
    (T_CH, "Easy", "A room in the dealer's premises where products are neatly arranged and lit so that customers can examine them before buying is a",
     "showroom", "stockroom",
     "warehouse", "workshop", "A",
     "The goods are displayed, not hidden in cartons."),
    (T_CH, "Easy", "A shopper pays for his groceries only when the supermarket's rider delivers them to his door. This method of payment is",
     "cash on delivery", "cash before delivery",
     "credit sale", "hire purchase", "A",
     "Money changes hands only as the goods arrive."),
    (T_CH, "Medium", "The period of time between one order a customer places and the next order he places for the same goods is called the",
     "order cycle", "lead time",
     "credit period", "grace period", "A",
     "The clock restarts each time he reorders."),
    (T_CH, "Medium", "A toothpaste maker notices its brand is losing shelf space to rivals in the big stores. The phrase 'shelf space' refers to",
     "the room a product occupies on a shelf", "the size of the factory floor",
     "space inside the delivery van", "the firm's office floor space", "A",
     "More room on the shelf means more chance to sell."),
    (T_CH, "Hard", "The diagram a retailer uses to show exactly where every product should sit on each shelf, so that every branch is laid out the same way, is a",
     "planogram", "planned economy",
     "floor map only", "price list", "A",
     "Even a new shop assistant can stock the shelf right."),
    (T_DF, "Medium", "The whole network of suppliers, producers, warehouses, transporters and sellers through which a product travels from raw material to the final consumer is the",
     "supply chain", "chain letter",
     "supply curve", "retail chain only", "A",
     "Every link must hold for the goods to arrive."),
    (T_DF, "Hard", "A manufacturing firm hands over its storage and delivery work entirely to a specialist company that does nothing but move other firms' goods. This arrangement is",
     "third-party logistics", "trial purchasing",
     "trade pricing", "total selling", "A",
     "Another firm's trucks now carry the burden."),
    (T_DF, "Hard", "At a distribution centre, goods are unloaded from one truck and straight into another for onward delivery, without ever being put into store. This practice is",
     "cross-docking", "double counting",
     "back-ordering", "bulk breaking", "A",
     "The goods barely touch the ground as they pass."),
    (T_PR, "Easy", "At Tejuosho market, a buyer and a seller argue back and forth over the price of a pair of shoes until they agree on one. This negotiation is called",
     "haggling", "hawking",
     "hoarding", "hosting", "A",
     "The final price is settled by argument."),
    (T_PR, "Medium", "At the end of the rainy season a clothing store cuts the price of its raincoats heavily to clear them before the dry season. This price cut is a",
     "seasonal discount", "cash discount",
     "trade discount", "quantity discount", "A",
     "The time of year dictates the reduction."),
    (T_PR, "Medium", "A trader allows a customer to take a refrigerator home at once and pay the price in small monthly amounts until it is complete. This arrangement is",
     "instalment buying", "impulse buying",
     "bulk buying", "barter buying", "A",
     "The payment arrives piece by piece."),
    (T_DM, "Medium", "In online advertising, the arrangement in which the advertiser pays the website a small sum every single time a visitor clicks on the advert is",
     "pay per click", "pay on delivery",
     "flat-rate space buying", "free listing", "A",
     "No click, no charge for that visitor."),
    (T_DMF, "Easy", "The business of selling goods to final consumers directly over the internet, through a shop's own website or app, is called",
     "e-tailing", "retailing by post only",
     "teleselling", "trolley selling", "A",
     "The shop counter is now a screen."),
    (T_CB, "Medium", "A buyer looks at a torch, weighs its price against how long it will last and how well it will serve him, and concludes it is worth buying. His judgement is about the torch's",
     "value for money", "value added tax",
     "vanity appeal", "vendor price", "A",
     "Is the price fair for what the thing does?"),
    (T_PS, "Medium", "A firm offers its salesmen a weekend in Dubai for whoever sells the most units in the month. This incentive device is a",
     "sales contest", "sales quota",
     "sales territory", "salary review", "A",
     "The best seller takes the prize."),
    (T_RC, "Medium", "The marketing staff sit down at month's end to study their sales figures product by product and zone by zone, to see what is moving and what is not. This study is a",
     "sales analysis", "sales forecast",
     "sales promotion", "sales quota", "A",
     "The figures themselves tell the story."),
    (T_RC, "Medium", "The statement of money a firm sets aside and plans to spend on advertising, promotion and research during the coming year is its",
     "marketing budget", "marketing audit",
     "marketing mix", "marketing board", "A",
     "It caps what the department may spend."),
    (T_CE, "Medium", "A bookshop now sells through its physical shop, its website and its phone app all at once. This approach is",
     "multichannel selling", "mono selling",
     "mass customisation", "mega retailing", "A",
     "The customer chooses how to buy."),
]

build_batch(
    S,
    "batch_222_waec_marketing8.json",
    "222",
    "WAEC Marketing round 8 (R45 top-up): generic brand; individual "
    "brand; quality control; testimonial; infomercial; outdoor "
    "advertising; exhibition; showroom; cash on delivery; order "
    "cycle; shelf space; planogram; supply chain; third-party "
    "logistics; cross-docking; haggling; seasonal discount; "
    "instalment buying; pay per click; e-tailing; value for money; "
    "sales contest; sales analysis; marketing budget; multichannel. "
    "Scanned against the whole Marketing pool (WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
