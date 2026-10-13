"""Batch 082 - WAEC Marketing, Paper 1 Objective round 1.

WASSCE Marketing Paper 1 (Objective) is a 50-item paper (50 min; official
2026 second-series timetable, paper 1121). This batch covers the WASSCE
marketing syllabus with FRESH angles and phrasings - Nigerian brand
scenarios (Indomie sizes, Dangote umbrella brand, gala hawkers, N999
psychological pricing), a new digital-marketing topic (SEO, WhatsApp
business catalogues, cart-abandonment emails, Google Business profiles,
influencer reviews) and question-form stems - because the near-dup scan
checks every item against the JAMB, WAEC and NECO banks, including the
JAMB Commerce marketing items (003, 031) and our 60-item NECO Marketing
bank.

    python3 scripts/build_neco_batch82.py -> content/batch_082_waec_marketing.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Marketing"

T_CON = "Marketing Concepts"
T_MIX = "The Marketing Mix"
T_SEG = "Segmentation and Targeting"
T_PROD = "Product, Branding and Packaging"
T_PRICE = "Pricing"
T_DIST = "Distribution Channels"
T_PROMO = "Promotion and Selling"
T_DIG = "Digital Marketing"
T_RES = "Marketing Research and Consumer Behaviour"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- marketing concepts
    (T_CON, "Medium", "Marketing is wider than selling because marketing",
     "covers research to after-sales care", "stops once the goods are sold", "begins after production ends", "deals only with advertising", "A",
     "Selling is one stage of the journey."),
    (T_CON, "Easy", "The marketing concept places the customer's needs",
     "at the centre of business", "after the production plans", "below the profit targets", "outside company work", "A",
     "The customer steers the firm."),
    (T_CON, "Hard", "Beyond customer satisfaction, societal marketing also guards",
     "the welfare of society", "the factory's overtime pay", "the rivals' market share", "the board's travel budget", "A",
     "It weighs the public good too."),
    (T_CON, "Medium", "No marketing exchange is complete unless",
     "both sides give and receive value", "only the buyer pays money", "the government approves it first", "goods are advertised on radio", "A",
     "Each side gives and receives."),
    (T_CON, "Easy", "Which activity is NOT part of marketing?",
     "compulsory taxation", "product design", "after-sales service", "pricing decisions", "A",
     "Tax is government's business."),
    (T_CON, "Medium", "Relationship marketing aims chiefly at",
     "keeping customers for life", "one-off seasonal sales", "beating rivals' adverts", "reducing staff numbers", "A",
     "Old customers cost less to keep."),
    (T_CON, "Easy", "Product, price and place are three of the Ps; the fourth is",
     "promotion", "people", "packaging", "planning", "A",
     "The classic four Ps close with promotion."),
    # ---------------------------------------------------------------- marketing mix
    (T_MIX, "Medium", "The marketing mix is the set of tools a firm",
     "combines to serve its market", "files with the government", "uses to pay its taxes", "lends to other firms", "A",
     "The blend hits the chosen market."),
    (T_MIX, "Hard", "Adding 'people, process and physical evidence' extends the mix for",
     "services marketing", "goods manufacturing", "raw material mining", "cattle herding", "A",
     "Services need the extra Ps."),
    (T_MIX, "Easy", "Building the right mix starts from knowing the",
     "target market first", "bank manager's mood", "factory capacity alone", "staff holiday roster", "A",
     "The market dictates the blend."),
    (T_MIX, "Hard", "A soft-drink firm redesigns its bottle and launches a city-wide advert. Which Ps are at work?",
     "product and promotion", "price and people", "place and process", "process and physical evidence", "A",
     "The bottle and the campaign speak."),
    (T_MIX, "Medium", "A market where sellers dictate the terms is a",
     "sellers' market", "buyers' market", "stock market", "grey market", "A",
     "Scarcity hands sellers the whip."),
    # ---------------------------------------------------------------- segmentation and targeting
    (T_SEG, "Medium", "Indomie pack sizes for toddlers and for adults segment the market by",
     "age, a demographic factor", "income of the traders", "religion of the buyers", "brand loyalty alone", "A",
     "Age splits the market cleanly."),
    (T_SEG, "Medium", "A designer label targeting young urban professionals segments by",
     "lifestyle and income", "blood group", "shoe size", "nationality of firms", "A",
     "How people live shapes wants."),
    (T_SEG, "Medium", "Concentrated marketing means serving",
     "one narrow segment well", "every segment at once", "only government buyers", "no segment at all", "A",
     "One niche, one sharp focus."),
    (T_SEG, "Easy", "Mass marketing offers",
     "one product to the whole market", "custom goods per person", "only to industrial users", "only in one city ward", "A",
     "One message sweeps everyone."),
    (T_SEG, "Hard", "A niche market is",
     "a small specialised segment", "the entire national market", "the crude oil market", "a government monopoly", "A",
     "Small, but rich for the few."),
    (T_SEG, "Hard", "Segmenting by usage rate separates",
     "heavy users from light users", "men from women only", "rich states from poor ones", "sellers from buyers", "A",
     "Volume of use marks the groups."),
    (T_SEG, "Easy", "Geographic segmentation splits buyers by",
     "where they live", "how old they are", "what they earn", "how they worship", "A",
     "Place of residence draws the line."),
    # ---------------------------------------------------------------- product, branding and packaging
    (T_PROD, "Easy", "A product's life cycle begins with the",
     "introduction stage", "decline stage", "maturity stage", "growth stage", "A",
     "Every launch starts at introduction."),
    (T_PROD, "Medium", "Sales flattening while profits peak signals the",
     "maturity stage", "introduction stage", "decline stage", "development stage", "A",
     "The plateau before the fall."),
    (T_PROD, "Medium", "The moment buyers trust a brand, the brand has become",
     "a mark of assured quality", "a tax on consumers", "a legal monopoly", "a price control", "A",
     "Trust shortens choosing time."),
    (T_PROD, "Hard", "One family name spread across a product line, as Dangote does, is",
     "an umbrella brand", "a private label", "a generic name", "a fighting brand", "A",
     "The name shelters every product."),
    (T_PROD, "Medium", "Good packaging protects the product and also",
     "sells it silently on the shelf", "raises the tax on it", "lengthens its life cycle", "insures it against theft", "A",
     "The pack is a silent salesman."),
    (T_PROD, "Medium", "A free sample pack handed out in a store is part of",
     "sales promotion", "personal selling", "publicity stunt work", "premium pricing", "A",
     "Trial is the shortest road to buy."),
    (T_PROD, "Medium", "Product differentiation aims to make the offer",
     "stand out from rivals", "cheaper than all others", "harder to produce", "heavier to carry", "A",
     "Distinct beats identical."),
    (T_PROD, "Easy", "A product line is a group of",
     "related items under one firm", "unrelated goods in a shop", "staff in one department", "rival firms' brands", "A",
     "One firm, one family of goods."),
    # ---------------------------------------------------------------- pricing
    (T_PRICE, "Medium", "Price skimming launches a new gadget",
     "high before rivals enter", "low to kill all rivals", "at cost price forever", "at auction prices only", "A",
     "Early buyers pay the premium."),
    (T_PRICE, "Medium", "Penetration pricing enters the market",
     "low to win quick share", "high to test the rich", "at double the cost", "only in the dry season", "A",
     "Cheap entry buys the crowd."),
    (T_PRICE, "Easy", "Cost-plus pricing adds to total cost a",
     "markup for profit", "tax for government", "discount for buyers", "commission for agents", "A",
     "Cost first, then the margin."),
    (T_PRICE, "Hard", "Psychological pricing sets N999 instead of N1,000 because",
     "it reads cheaper to buyers", "it cuts tax by one naira", "it eases change-making only", "it blocks all discounts", "A",
     "The eye reads the first digit."),
    (T_PRICE, "Medium", "A discount granted for prompt payment is called",
     "cash discount", "trade discount", "quantity discount", "seasonal discount", "A",
     "Paying early earns a cut."),
    (T_PRICE, "Medium", "When government fixes the pump price of fuel, the pricing is",
     "regulated pricing", "market pricing", "skimming pricing", "penetration pricing", "A",
     "The state, not demand, sets it."),
    (T_PRICE, "Hard", "Loss-leader pricing deliberately",
     "sells one item cheap to draw crowds", "sells every item at a loss", "raises all the prices together", "prices only for the rich", "A",
     "One bargain brings the basket."),
    # ---------------------------------------------------------------- distribution channels
    (T_DIST, "Easy", "Goods that move straight from the maker to the final user skip",
     "all middlemen", "all advertising costs", "all factory gates", "all packing steps", "A",
     "Nothing stands between them."),
    (T_DIST, "Medium", "A wholesaler breaks bulk by",
     "selling in smaller units", "refusing small buyers", "importing raw crude", "printing price lists", "A",
     "Case loads become shop lots."),
    (T_DIST, "Medium", "Perishable vegetables reach city markets fastest through",
     "direct farmer-to-market runs", "long agent chains", "sea freight to Europe", "warehouse storage first", "A",
     "Fewer hands, fresher leaves."),
    (T_DIST, "Hard", "A sole distributor appointed for a whole region enjoys",
     "exclusive distribution", "open distribution", "intensive distribution", "franchise taxation", "A",
     "The maker sells through one hand."),
    (T_DIST, "Hard", "Cement railed to depots across the country illustrates the channel role of",
     "transport and warehousing", "advertising agencies", "market researchers", "brand ambassadors", "A",
     "Place utilities ride on logistics."),
    (T_DIST, "Medium", "Franchising lets a local investor sell under",
     "the franchisor's brand", "his own secret label", "the government's mark", "no brand at all", "A",
     "He buys the right to the name."),
    # ---------------------------------------------------------------- promotion and selling
    (T_PROMO, "Medium", "A door-to-door pitch made to a shop owner is",
     "personal selling", "mass advertising", "public relations work", "sales promotion display", "A",
     "Two people, one persuasion."),
    (T_PROMO, "Medium", "Publicity differs from advertising because publicity",
     "is not paid for directly", "runs only on the radio", "targets only the staff", "always costs far more", "A",
     "The news media carry it free."),
    (T_PROMO, "Medium", "An influencer's honest product review works as",
     "word-of-mouth publicity", "premium pricing", "franchise dealing", "a skimming strategy", "A",
     "Trust travels through voices."),
    (T_PROMO, "Hard", "Above-the-line promotion refers to",
     "paid mass-media advertising", "door-to-door canvassing", "after-sales servicing", "trade fair displays", "A",
     "It rides the bought media."),
    (T_PROMO, "Medium", "A stand at the Lagos trade fair mainly promotes through",
     "display and demonstration", "price reduction only", "bank credit notes", "transport subsidies", "A",
     "The goods speak in person."),
    (T_PROMO, "Medium", "Sales promotion targets quick buyer action with",
     "coupons and free gifts", "long-term brand image", "annual reports", "share dividends", "A",
     "It sparks the purchase now."),
    (T_PROMO, "Hard", "An advert that names the price and phone number seeks",
     "direct sales response", "brand awareness alone", "staff recruitment", "shareholder goodwill", "A",
     "It wants the order today."),
    # ---------------------------------------------------------------- digital marketing
    (T_DIG, "Easy", "Marketing through a WhatsApp business catalogue is",
     "digital marketing", "analogue billboard art", "guerrilla pricing", "bulk breaking", "A",
     "The phone has become a shopfront."),
    (T_DIG, "Medium", "Search engine optimisation aims to make a website",
     "rank higher in searches", "load more offline adverts", "charge visitors fees", "print faster invoices", "A",
     "Free traffic follows the ranking."),
    (T_DIG, "Medium", "A promoted post on Instagram is paid",
     "by reach or clicks", "in cowries at the port", "through bank drafts only", "by the government", "A",
     "Payment follows performance."),
    (T_DIG, "Medium", "Email newsletters nurture customers by",
     "keeping the brand in mind", "spamming them daily", "blocking their orders", "raising their taxes", "A",
     "Small notes keep the thread."),
    (T_DIG, "Hard", "Cart-abandonment emails chase",
     "unfinished online orders", "returned physical goods", "staff leave forms", "bank reconciliation items", "A",
     "The almost-sale is reeled back."),
    (T_DIG, "Hard", "A complete Google Business profile mainly boosts",
     "local search discovery", "factory output speed", "import duty waivers", "staff medical cover", "A",
     "Nearby buyers find the shop."),
    (T_DIG, "Medium", "Viral marketing spreads fastest when the content is",
     "shared by viewers themselves", "bought as airtime slots", "printed on receipts", "read aloud in courts", "A",
     "The audience becomes the media."),
    (T_DIG, "Medium", "Online customer reviews double as",
     "free feedback research", "paid tax returns", "staff appraisals", "loan applications", "A",
     "Every review is field data."),
    # ---------------------------------------------------------------- research and consumer behaviour
    (T_RES, "Easy", "The first step of marketing research is",
     "defining the problem", "printing questionnaires", "hiring many field staff", "buying computer sets", "A",
     "A wrong question wastes the survey."),
    (T_RES, "Hard", "A focus group gathers",
     "consumers for guided discussion", "staff for annual appraisals", "bankers for loan reviews", "dealers for price fixing", "A",
     "A moderator draws out views."),
    (T_RES, "Easy", "Primary data is collected",
     "fresh from the field", "from old annual reports", "from the census archive", "from competitors' files", "A",
     "First-hand data answers first."),
    (T_RES, "Medium", "Quietly noting shoppers' paths through a store is which method?",
     "observation study", "mail questionnaire", "telephone interview", "desk research", "A",
     "The eyes gather what mouths hide."),
    (T_RES, "Medium", "A commuter's quick choice of bread at 7 a.m. is driven mostly by",
     "habit and convenience", "warranty terms", "after-sales service", "installation costs", "A",
     "Routine rides the morning rush."),
    (T_RES, "Hard", "Cognitive dissonance after purchase describes",
     "post-purchase doubt", "pre-sale bargaining", "window shopping urges", "credit refusal shame", "A",
     "The mind second-guesses the buy."),
    (T_RES, "Hard", "Reference groups steer buyers through",
     "peer example and pressure", "court injunctions", "customs tariffs", "bank interest rates", "A",
     "We buy as our circle buys."),
    (T_RES, "Hard", "Stimulus, black box, response is a model of the",
     "consumer buying process", "factory assembly line", "cargo clearing steps", "staff payroll system", "A",
     "Input, mind, then decision."),
]

build_batch(
    S,
    "batch_082_waec_marketing.json",
    "082",
    "WAEC Marketing Paper 1 round 1 (Round 16e): the WASSCE syllabus with "
    "FRESH angles - Nigerian brand scenarios (Indomie pack sizes, Dangote "
    "umbrella brand, N999 psychological pricing, Lagos trade fair, pump "
    "price regulation), a new digital-marketing topic (SEO, WhatsApp "
    "business catalogues, promoted posts, cart-abandonment emails, Google "
    "Business profiles, viral content) and question-form stems - because "
    "the near-dup scan checks every item against the JAMB, WAEC and NECO "
    "banks INCLUDING the JAMB Commerce marketing items (003, 031) and the "
    "60-item NECO Marketing bank. Topics: marketing concepts, the "
    "marketing mix, segmentation, product and branding, pricing, "
    "distribution channels, promotion and selling, digital marketing, "
    "research and consumer behaviour.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
