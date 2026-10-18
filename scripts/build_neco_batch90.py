"""Batch 090 - NECO Financial Accounting round 2 (NECO lift, Round 18).

NECO Accounting objective draws 60 items; the bank stood at 62. This lift
adds fresh items - numeric mini-computations (depreciation N11,000, markup
N1,000, margin 40%, profit from capital N14,000, profit share 2:1, imprest
N3,200, net purchases N39,000), books (journal proper, three-column cash
book, discount allowed, petty cash analysis), ledger tech (debit balance,
carriage inwards/outwards, closing revenue accounts, returns outwards),
controls (purchases/sales ledger control, compensating errors, suspense
clearing, transposition), final accounts (bad debts written off, drawings,
snapshot, indirect labour, cost of goods manufactured), non-profit
(accumulated fund, bar account), payroll (PAYE, net pay) and ratios.

    python3 scripts/build_neco_batch90.py -> content/batch_090_neco_accounting2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_LED = "The Ledger and Double Entry"
T_BOOK = "Books of Prime Entry"
T_ADJ = "Adjustments"
T_FIN = "Final Accounts"
T_BANK = "Bank Reconciliation"
T_ERR = "Errors and the Suspense Account"
T_CON = "Control Accounts"
T_NPO = "Accounts of Non-Profit Bodies"
T_MAN = "Manufacturing Accounts"
T_NAT = "Nature and Purpose of Accounting"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- ledger
    (T_LED, "Easy", "If the debit side of an account is greater than the credit side, the account shows a",
     "debit balance", "credit balance", "zero balance", "suspense balance", "A",
     "Debit weight tips the balance left."),
    (T_LED, "Medium", "In the trading account, carriage inwards is added to",
     "purchases", "sales", "gross profit", "closing stock", "A",
     "Carrying goods in is a buying cost."),
    (T_LED, "Medium", "Carriage outwards is charged in the profit and loss account as",
     "an expense", "an income", "an asset", "a liability", "A",
     "Delivering goods out costs the seller."),
    (T_LED, "Medium", "At the year's end, the accounts of expenses are closed by transfer to the",
     "profit and loss account", "balance sheet", "trial balance", "trading account", "A",
     "Expenses end inside the P&L."),
    (T_LED, "Easy", "Goods returned BY the business TO suppliers are first recorded in the",
     "returns outwards day book", "returns inwards day book", "sales day book", "cash book", "A",
     "Returns outwards go back to sellers."),
    # ---------------------------------------------------------------- books of prime entry
    (T_BOOK, "Medium", "Entries that have no other book of prime entry, like corrections, go into the",
     "journal proper", "petty cash book", "purchases journal", "cash book", "A",
     "The general journal catches the rest."),
    (T_BOOK, "Easy", "A cash book with cash, bank and discount columns is called a",
     "three-column cash book", "two-column cash book", "single-column cash book", "petty cash book", "A",
     "Three columns stand side by side."),
    (T_BOOK, "Hard", "Discount allowed to customers appears on the",
     "debit side of the cash book", "credit side of the cash book", "sales day book only", "petty cash book", "A",
     "It sits by the receipts column."),
    (T_BOOK, "Medium", "The analysis columns of the petty cash book exist to group",
     "small expenses by their type", "customers by their towns", "cheques by their numbers", "staff by their grades", "A",
     "Postage, cleaning and the rest separate."),
    # ---------------------------------------------------------------- computations / adjustments
    (T_ADJ, "Hard", "A generator bought for N100,000 should last 5 years and scrap at N10,000. Annual straight-line depreciation is",
     "N18,000", "N20,000", "N16,000", "N22,000", "A",
     "N90,000 spread over 5 years."),
    (T_ADJ, "Medium", "Goods costing N800 are marked up by 25% on cost. The selling price is",
     "N1,000", "N960", "N1,050", "N825", "A",
     "Add a quarter of the cost."),
    (T_ADJ, "Hard", "Sales N1,000,000 and cost of sales N600,000 give a gross profit margin of",
     "40%", "60%", "67%", "34%", "A",
     "Gross profit of N400,000 over sales."),
    (T_ADJ, "Medium", "Opening capital N50,000 and closing capital N64,000, with no drawings, give a profit of",
     "N14,000", "N114,000", "N9,000", "N6,400", "A",
     "The growth in capital is the profit."),
    (T_ADJ, "Medium", "A profit of N90,000 is shared in the ratio 2:1. The partners receive",
     "N60,000 and N30,000", "N45,000 and N45,000", "N50,000 and N40,000", "N70,000 and N20,000", "A",
     "Two shares and one share split it."),
    (T_ADJ, "Medium", "An imprest float of N5,000 has vouchers of N3,200 at month end. The cashier is reimbursed",
     "N3,200", "N5,000", "N1,800", "N8,200", "A",
     "The refund restores the float."),
    (T_ADJ, "Hard", "Purchases N40,000, returns outwards N2,000, carriage inwards N1,000. Net purchases equal",
     "N39,000", "N43,000", "N37,000", "N41,000", "A",
     "Purchases minus returns plus carriage."),
    (T_ADJ, "Easy", "Buying a delivery van is capital expenditure, but petrol for it is",
     "revenue expenditure", "capital expenditure too", "a liability", "drawings", "A",
     "Running costs expense the year."),
    (T_ADJ, "Easy", "A debt finally written off goes to the profit and loss account as",
     "an expense", "an income", "an asset", "a reserve", "A",
     "The loss reduces the profit."),
    # ---------------------------------------------------------------- final accounts
    (T_FIN, "Easy", "In the balance sheet, drawings are deducted from",
     "capital", "fixed assets", "current liabilities", "sales", "A",
     "What the owner takes shrinks his stake."),
    (T_FIN, "Medium", "The balance sheet differs from the final accounts because it is",
     "a statement of position at one date", "a record of a whole year's trading", "an account inside the ledger", "a list of debtors only", "A",
     "It photographs, not narrates."),
    (T_FIN, "Medium", "A cheque dated for a future day and handed to a supplier today is a",
     "post-dated cheque", "stale cheque", "crossed cheque", "dishonoured cheque", "A",
     "Its date lies in the future."),
    # ---------------------------------------------------------------- bank reconciliation
    (T_BANK, "Easy", "Differences between a firm's cash book and the monthly letter from its bank are settled in the",
     "bank reconciliation statement", "trial balance", "petty cash book", "sales ledger", "A",
     "The two records rarely agree at once."),
    (T_BANK, "Hard", "A statement of assets, liabilities and capital drawn at one date, often from incomplete records, is the",
     "statement of affairs", "balance sheet only", "income statement", "cash flow statement", "A",
     "It fixes a net-worth picture."),
    # ---------------------------------------------------------------- errors and suspense
    (T_ERR, "Medium", "Writing N7,000 in an account instead of N700 is an error of",
     "original entry", "commission", "principle", "complete reversal", "A",
     "The first figure itself was wrong."),
    (T_ERR, "Hard", "Two mistakes that happen to cancel each other out are called",
     "compensating errors", "errors of omission", "errors of principle", "single errors", "A",
     "One hides the other's effect."),
    (T_ERR, "Medium", "Once errors are found, the suspense account is cleared by",
     "journal entries", "deleting the account", "opening a new ledger", "carrying it forward forever", "A",
     "Corrections journal through it."),
    # ---------------------------------------------------------------- control accounts
    (T_CON, "Medium", "The total owed to trade suppliers at any date is shown in the",
     "purchases ledger control account", "sales ledger control account", "petty cash book", "general journal", "A",
     "The control sums the suppliers."),
    (T_CON, "Medium", "The total owed by credit customers is summarised in the",
     "sales ledger control account", "purchases ledger control account", "cash book", "suspense account", "A",
     "The control sums the debtors."),
    (T_CON, "Medium", "A main advantage of control accounts is that they help to",
     "locate errors quickly", "increase the year's profit", "avoid paying tax", "remove the trial balance", "A",
     "Totals point to the bad ledger."),
    # ---------------------------------------------------------------- non-profit bodies
    (T_NPO, "Medium", "In the accounts of a social club, the equivalent of capital is the",
     "accumulated fund", "share capital", "loan capital", "suspense fund", "A",
     "Members' buildup stands as fund."),
    (T_NPO, "Medium", "A social club prepares a bar account to show the profit on",
     "drinks sold", "members' subscriptions", "hall rentals", "donations received", "A",
     "The bar's buying and selling nets out."),
    # ---------------------------------------------------------------- manufacturing
    (T_MAN, "Medium", "Wages paid to factory cleaners are treated as",
     "indirect labour", "direct labour", "office salaries", "selling expenses", "A",
     "They serve the whole factory."),
    (T_MAN, "Medium", "The figure transferred from the manufacturing account to the trading account is the",
     "cost of goods manufactured", "prime cost alone", "factory overheads", "work-in-progress balance", "A",
     "Finished goods feed the trading side."),
    # ---------------------------------------------------------------- nature, payroll, ratios
    (T_NAT, "Medium", "The auditor's report states whether the accounts show a",
     "true and fair view", "guaranteed profit", "tax-free position", "perfect arithmetic", "A",
     "The auditor gives an opinion."),
    (T_NAT, "Medium", "Continuous checking of a firm's books by its own staff is called",
     "internal audit", "external audit", "stock taking", "bank reconciliation", "A",
     "The firm audits itself in-house."),
    (T_NAT, "Easy", "The accounting equation is normally written as",
     "assets = capital + liabilities", "capital = sales - purchases", "assets = income - expenses", "liabilities = assets + capital", "A",
     "What the firm owns balances its funding."),
    (T_NAT, "Medium", "Under PAYE, the employer",
     "deducts tax from wages and remits it", "pays tax from his own pocket", "collects tax from customers", "waives staff taxation", "A",
     "Pay-as-you-earn leaves with the wage."),
    (T_NAT, "Easy", "Net pay means gross pay minus",
     "deductions", "overtime", "basic salary", "transport allowance", "A",
     "What remains is the take-home."),
    (T_NAT, "Easy", "The share of profit paid out to shareholders is the",
     "dividend", "interest", "commission", "premium", "A",
     "Shareholders divide the dividend."),
    (T_NAT, "Medium", "The ratio that shows a firm's ability to meet short-term debts is the",
     "current ratio", "markup ratio", "turnover ratio", "capital ratio", "A",
     "Current assets face current debts."),
]

build_batch(
    S,
    "batch_090_neco_accounting2.json",
    "090",
    "NECO Accounting round 2 (Round 18 lift): numeric mini-computations "
    "(straight-line N11,000, markup N1,000, margin 40%, profit-from-capital "
    "N14,000, 2:1 share N60k/N30k, imprest refund N3,200, net purchases "
    "N39,000), books (journal proper, three-column cash book, discount "
    "allowed, petty cash analysis), ledger tech (debit balance, carriage "
    "inwards/outwards, closing revenue accounts, returns outwards), errors "
    "(original entry, compensating, suspense clearing), controls (purchases/"
    "sales ledger control, error location), final accounts (bad debts, "
    "drawings, snapshot nature, post-dated cheque), statement of affairs, "
    "non-profit (accumulated fund, bar account), manufacturing (indirect "
    "labour, cost of goods manufactured), audit, PAYE, net pay, dividend, "
    "current ratio. Scanned against NECO round 1, the WAEC twin and the "
    "JAMB Accounting banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
