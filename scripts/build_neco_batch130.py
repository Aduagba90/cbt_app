"""Batch 130 - WAEC Commerce round 5 (WAEC top-up, Round 25).

Lifts WAEC Commerce from 150 toward ~187 with angles not yet in any
bank: partnership deed and unlimited liability, incorporation and
company types, cooperative surplus, fixed-term dissolution, pro-forma
invoice / credit and debit notes, indents, protective tariffs, bonded
goods, entrepot and invisible trade, balance of trade arithmetic,
working capital, debentures vs shares, preference shares, the stock
exchange and underwriting, treasury bills, money vs capital market,
insurance principles (insurable interest, indemnity, contribution,
subrogation, proximate cause) and covers (fidelity guarantee,
consequential loss), SON / NAFDAC / FCCPC, trade unions, industrial
arbitration and employers' associations. Scanned against WAEC rounds
1-4, NECO Commerce (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch130.py -> content/batch_130_waec_commerce5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Commerce"

T_UNITS = "Business Units and Ownership"
T_DOCS = "Trade Procedures and Documents"
T_FIN = "Business Finance and the Exchange"
T_INS = "Insurance Principles and Cover"
T_CONS = "Consumer Protection and Labour"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- business units
    (T_UNITS, "Medium", "The document stating partners' capital, rights and profit-sharing is the",
     "partnership deed", "memorandum", "prospectus", "articles", "A",
     "The deed governs the partnership."),
    (T_UNITS, "Hard", "Under unlimited liability, if a firm's assets cannot pay its debts, a partner's",
     "personal assets may be sold", "liability stops at his capital", "only the firm's stock is touched", "debts die with the firm", "A",
     "Homes and cars follow debts."),
    (T_UNITS, "Medium", "The strongest reason small investors buy shares in a limited company is",
     "limited liability", "unlimited profits", "zero taxation for life", "exempt directors", "A",
     "Losses stop at one's shares."),
    (T_UNITS, "Hard", "Unlike a private company, a public company may",
     "sell shares to the public", "sell shares only to staff", "borrow from banks alone", "elect a life president", "A",
     "The exchange opens to it."),
    (T_UNITS, "Medium", "In a well-run cooperative, the annual surplus is shared mainly as",
     "dividend on members' patronage", "equal cash for all adults", "salaries fixed by government", "interest on bank loans", "A",
     "Patronage decides the dividend."),
    (T_UNITS, "Hard", "Public corporations in Nigeria are financed chiefly through",
     "government subventions", "members' monthly dues", "foreign aid only", "lottery funds", "A",
     "The treasury props them up."),
    (T_UNITS, "Medium", "A partnership formed for a fixed term dissolves at",
     "the end of that term", "the first partner's death", "any court ruling", "the auditor's order", "A",
     "The term itself closes it."),

    # ------------------------------------------------------------- trade documents
    (T_DOCS, "Medium", "A pro-forma invoice differs from a final invoice because it",
     "asks for no payment yet", "lists no prices at all", "demands cash on delivery", "is never signed", "A",
     "A polite price list, first."),
    (T_DOCS, "Medium", "A seller sends a credit note to",
     "reduce the amount a buyer owes", "increase the debt owed", "cancel the whole trade", "order fresh goods", "A",
     "An apology written in figures."),
    (T_DOCS, "Hard", "A seller issues a debit note when the buyer has been",
     "undercharged", "overcharged", "double billed", "fully refunded", "A",
     "The bill grows to match goods."),
    (T_DOCS, "Hard", "The buying instruction a merchant hands to his import agent abroad is known as",
     "an indent", "a bill of lading", "a waybill", "a consular form", "A",
     "Agents route indents abroad."),
    (T_DOCS, "Medium", "Duties charged mainly to shield local producers from foreign competition are",
     "protective tariffs", "revenue duties", "excise duties", "subsidies", "A",
     "Tariffs guard the home mills."),
    (T_DOCS, "Hard", "Goods stored in a bonded warehouse with duty unpaid are held",
     "under bond", "free of duty", "on consignment", "duty pre-paid", "A",
     "Duty pauses at the custom gate."),
    (T_DOCS, "Medium", "Entrepot trade consists of",
     "re-exporting imports", "banning all imports", "smuggling goods", "barter trade", "A",
     "Goods land, then sail again."),
    (T_DOCS, "Hard", "Invisible trade covers",
     "services rather than goods", "crude oil cargoes", "bagged farm produce", "container goods", "A",
     "No crates carry it, yet it earns."),
    (T_DOCS, "Medium", "Nigeria's visible exports total N400bn and visible imports N250bn. Her balance of trade is",
     "N150 billion favourable", "N650 billion favourable", "N150 billion unfavourable", "N650 billion unfavourable", "A",
     "Exports minus imports, in the black.", "150"),

    # ------------------------------------------------------------- finance
    (T_FIN, "Medium", "A trader's current assets are N90,000 and current liabilities N30,000. His working capital is",
     "N60,000", "N120,000", "N3,000", "N30,000", "A",
     "Current assets minus liabilities.", "60000"),
    (T_FIN, "Medium", "Capital tied down in machines that serve for years is",
     "fixed capital", "working capital", "circulating capital", "nominal capital", "A",
     "It turns slowly, serving long."),
    (T_FIN, "Hard", "Unlike shares, debentures",
     "earn fixed interest", "earn fluctuating dividends", "carry voting rights", "are never redeemed", "A",
     "Lenders stand before owners."),
    (T_FIN, "Hard", "Preference shareholders are 'preferred' because they",
     "are paid dividends first", "receive double dividends", "never receive dividends", "manage the company", "A",
     "First seats at the table."),
    (T_FIN, "Medium", "The stock exchange chiefly helps companies to",
     "raise long-term capital", "print paper money", "keep daily cash", "fix exchange rates", "A",
     "Long money changes hands there."),
    (T_FIN, "Hard", "An underwriter in a new share issue agrees to",
     "buy unsold shares", "advertise the shares", "audit the accounts", "fix share prices", "A",
     "He sweeps up the leftovers."),
    (T_FIN, "Medium", "Treasury bills are short-term instruments issued by the",
     "central government", "commercial banks", "stock exchanges", "insurance firms", "A",
     "Ninety-one-day government paper."),
    (T_FIN, "Hard", "The essential difference between the money and capital markets is the",
     "length of funds traded", "countries involved", "currencies used", "brokers allowed in", "A",
     "Days are traded against decades."),

    # ------------------------------------------------------------- insurance
    (T_INS, "Medium", "The principle requiring a genuine financial stake in the subject insured is",
     "insurable interest", "utmost good faith", "contribution", "subrogation", "A",
     "No stake, no valid policy."),
    (T_INS, "Hard", "Indemnity means the insured is",
     "restored to his loss position", "enriched beyond his loss", "paid twice over", "left to bear it alone", "A",
     "Compensation, never profit."),
    (T_INS, "Hard", "When two policies cover the same risk, each pays its share under the principle of",
     "contribution", "indemnity", "subrogation", "proximate cause", "A",
     "Twin policies split the bill."),
    (T_INS, "Medium", "After an insurer pays for goods a careless driver destroyed, it may sue the driver in the insured's name. This right of pursuit is",
     "subrogation", "contribution", "indemnity", "insurable interest", "A",
     "Paying buys the right to pursue."),
    (T_INS, "Hard", "The most direct cause that must be covered for a claim to stand is the",
     "proximate cause", "remote cause", "original cause", "final cost", "A",
     "The nearest spark counts."),
    (T_INS, "Medium", "The cover a bank buys so that losses from a thieving cashier are repaid is",
     "fidelity guarantee", "consequential loss", "motor third party", "marine hull", "A",
     "It guards the till from within."),
    (T_INS, "Hard", "Consequential loss insurance is taken to cover",
     "profits lost after a fire", "damage done by floods", "goods stolen in transit", "injuries at work", "A",
     "It pays the silence after flames."),

    # ------------------------------------------------------------- consumer & labour
    (T_CONS, "Medium", "In Nigeria, the body that sets standards for manufactured goods is",
     "SON", "NAFDAC", "FCCPC", "CBN", "A",
     "Its stamp approves quality."),
    (T_CONS, "Medium", "NAFDAC's chief concern is the regulation of",
     "food and drugs", "houses and land", "roads and bridges", "ships and ports", "A",
     "Pills and tins answer to it."),
    (T_CONS, "Hard", "The FCCPC's mandate combines consumer protection with",
     "promoting fair competition", "printing the currency", "building power plants", "running the ports", "A",
     "Markets stay open and clean."),
    (T_CONS, "Medium", "A main function of trade unions is to",
     "negotiate members' wages", "set national budgets", "fix fuel prices", "run the civil service", "A",
     "One voice speaks for many."),
    (T_CONS, "Hard", "A dispute that unions and employers cannot settle themselves is referred to",
     "industrial arbitration", "the stock exchange", "a ward tribunal", "the police council", "A",
     "A neutral gives the verdict."),
    (T_CONS, "Medium", "Employers' associations chiefly exist to",
     "promote members' interests", "settle workers' strikes alone", "print trade journals", "collect income taxes", "A",
     "The other side of the table."),
]

build_batch(
    S,
    "batch_130_waec_commerce5.json",
    "130",
    "WAEC Commerce round 5 (Round 25 top-up): partnership deed, "
    "unlimited liability, incorporation, public vs private companies, "
    "cooperative surplus, public corporation finance, fixed-term "
    "dissolution, pro-forma invoice, credit and debit notes, indents, "
    "protective tariffs, bonded goods, entrepot and invisible trade, "
    "balance of trade arithmetic (N150bn), working capital (N60,000), "
    "fixed capital, debentures vs shares, preference shares, stock "
    "exchange and underwriting, treasury bills, money vs capital market, "
    "insurable interest, indemnity, contribution, subrogation, proximate "
    "cause, fidelity guarantee, consequential loss, SON, NAFDAC, FCCPC, "
    "trade unions, industrial arbitration, employers' associations. "
    "Scanned against WAEC rounds 1-4, NECO Commerce (all rounds) and the "
    "JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
