"""Batch 188 - NECO Commerce round 7 (NECO top-up, R36).

Grows NECO Commerce from 215 toward ~240 with angles not yet in
the bank: banking, insurance, transport, advertising and
warehousing as the aids to trade; demurrage; insurance
underwriting; the NIS quality mark; credit sale versus hire
purchase; the auctioneer's reserve price; nationalisation; the
articles of association; the prospectus; devaluation; ad valorem
duty; the certificate of origin; mining and lumbering as
industrial occupations; the face value of a share; the right to
safety; grading and standardisation; FOB; the factor who holds
goods; the cover note; USSD banking; the ATM; the gilt-edged
security; email. Scanned against NECO rounds 1-6, WAEC Commerce
(all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch188.py -> content/batch_188_neco_commerce7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_TRA = "Home and Foreign Trade"
T_DOC = "Trade Documents"
T_BAN = "Banking and Finance"
T_INS = "Insurance"
T_BUS = "Business Units"
T_STK = "The Stock Exchange"
T_TRA2 = "Transport"
T_CON = "The Consumer"
T_OCC = "Occupations and Production"
T_WAR = "Warehousing"

PASSAGES = []
PQ = []

Q = [
    (T_TRA, "Easy", "The two great branches of commerce are trade itself and the",
     "aids to trade", "arms of government",
     "factors of production", "types of market", "A",
     "One branch sells; the other smooths the selling."),
    (T_OCC, "Medium", "Mining, quarrying and lumbering, which draw wealth from nature, belong to ___ occupations.",
     "industrial", "commercial",
     "professional", "services", "A",
     "Extractive work opens the production chain."),
    (T_DOC, "Medium", "The customs document that states the country in which imported goods were produced is the",
     "certificate of origin", "bill of lading",
     "consular card", "dock warrant", "A",
     "Origin decides the duty the goods pay."),
    (T_DOC, "Hard", "Under the price term FOB, the buyer begins to bear the cost of the goods once they pass over the ship's",
     "rail at the loading port", "hatch at the destination port",
     "bow on the open sea", "deck at anchorage", "A",
     "Free on board ends the seller's risk at the rail."),
    (T_DOC, "Hard", "A duty calculated as a percentage of the value of the goods, rather than a flat sum, is said to be",
     "ad valorem", "specific",
     "compound", "prohibitive", "A",
     "The value of the goods sets the tax."),
    (T_TRA, "Medium", "The deliberate official lowering of a country's currency against other currencies is called",
     "devaluation", "appreciation",
     "revaluation", "stabilisation", "A",
     "The naira is priced cheaper to the world."),
    (T_TRA2, "Hard", "The charge a shipowner demands when a charterer keeps the vessel waiting beyond the agreed free days is",
     "demurrage", "freight",
     "insurance premium", "port dues", "A",
     "Every idle day beyond the free days costs money."),
    (T_WAR, "Medium", "Sorting cocoa into recognised standard qualities before it is exported is called",
     "grading", "blending",
     "branding", "bulking", "A",
     "Grade one commands grade one prices."),
    (T_WAR, "Medium", "Making goods conform to one fixed specification of size and quality is",
     "standardisation", "specialisation",
     "diversification", "integration", "A",
     "Every unit matches the stated standard."),
    (T_INS, "Hard", "The work of examining a proposed risk and deciding whether and at what price to accept it is",
     "underwriting", "broking",
     "adjusting of losses", "actuarial science only", "A",
     "The underwriter signs his name under the risk."),
    (T_INS, "Medium", "The brief note an insurer issues to cover the insured while the full policy document is being prepared is a",
     "cover note", "renewal notice",
     "claim form", "binder of title", "A",
     "Temporary paper, full protection."),
    (T_INS, "Medium", "The greatest amount the insurer has agreed to pay under a policy is its",
     "sum insured", "premium",
     "excess", " rebate", "A",
     "The ceiling of the promise is written down."),
    (T_BAN, "Easy", "Money can be sent with a mobile phone using a short code even without internet access through",
     "USSD transfer", "SWIFT cable",
     "telex message", "postal order", "A",
     "The star-and-hash code carries the naira."),
    (T_BAN, "Easy", "The machine outside a bank hall from which a customer draws cash at any hour is the",
     "ATM", "POS",
     "GPS", "ticker", "A",
     "The card and PIN open the cash drawer."),
    (T_BAN, "Medium", "Government loans regarded as the safest securities in the market are nicknamed",
     "gilt-edged", "blue chips of oil",
     "junk bonds", "preference paper", "A",
     "The treasury's paper gleams safest."),
    (T_BAN, "Medium", "The electronic means of sending written messages across the world almost at once is",
     "email", "telegram by wire",
     "the telex machine", "registered post", "A",
     "One click and the letter has landed."),
    (T_BUS, "Medium", "The rules that govern a company's internal management, meetings and directors' powers are set out in its",
     "articles of association", "memorandum of association",
     "prospectus", "certificate of incorporation", "A",
     "The internal rulebook of the company."),
    (T_BUS, "Hard", "The printed invitation by which a public company asks the general public to subscribe for its shares is the",
     "prospectus", "debenture",
     "share warrant", "broker's note", "A",
     "It tells the public what it is buying into."),
    (T_BUS, "Medium", "Government taking over ownership and control of a private business is called",
     "nationalisation", "privatisation",
     "commercialisation", "liquidation", "A",
     "The state swallows the company whole."),
    (T_STK, "Easy", "The amount printed on a share certificate as the value of one share is its",
     "face value", "market value",
     "premium", "yield", "A",
     "The naira figure the paper carries."),
    (T_CON, "Medium", "In a credit sale, unlike hire purchase, ownership of the goods passes to the buyer",
     "immediately the sale is made", "only after the final instalment",
     "after six months by law", "never at all", "A",
     "The goods are his from day one, debt and all."),
    (T_CON, "Easy", "The consumer right that demands goods should not harm life or property is the right to",
     "safety", "redress",
     "information", "choose", "A",
     "No kettle should scald its owner."),
    (T_CON, "Medium", "The mark of quality, such as NIS, displayed on goods certified to meet Nigerian standards, shows",
     "compliance with standards", "ownership by government",
     "cheapness of the product", "foreign origin", "A",
     "The stamp vouches for the maker."),
    (T_DOC, "Hard", "An auctioneer is instructed not to sell a rare carving below a certain amount known as the",
     "reserve price", "asking price",
     "spot price", "minimum tender", "A",
     "Below the reserve the hammer stays silent."),
    (T_DOC, "Hard", "The agent who takes physical possession of the goods and sells them in his own name for a commission is a",
     "factor", "broker",
     "del credere agent", "auctioneer", "A",
     "The goods pass through his own hands."),
]

build_batch(
    S,
    "batch_188_neco_commerce7.json",
    "188",
    "NECO Commerce round 7 (R36 top-up): aids to trade umbrella; "
    "mining and lumbering as industrial occupations; certificate of "
    "origin; FOB at the ship's rail; ad valorem duty; devaluation; "
    "demurrage; grading and standardisation; underwriting; the "
    "cover note; sum insured; USSD transfers; the ATM; gilt-edged "
    "securities; email; articles of association; the prospectus; "
    "nationalisation; face value; credit sale versus hire purchase; "
    "right to safety; the NIS mark; the reserve price; the factor "
    "who holds goods. Scanned against NECO rounds 1-6, WAEC "
    "Commerce (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
