"""Batch 131 - WAEC Financial Accounting round 5 (WAEC top-up, Round 25).

Lifts WAEC Accounting from 152 toward ~188 with angles not yet in any
bank: business entity, matching, prudence, going concern and money
measurement concepts; suspense account and the error family (commission,
original entry, principle, omission effects); club accounts (statement
of affairs, subscriptions arrears, accumulated fund, bar trading);
manufacturing numerics (prime cost, WIP adjustment) and cost
classification; bills of exchange (discounting, dishonour, retirement);
partnership admission goodwill, realisation account, partner salary
posting, 5% loan interest; company items (debenture interest vs
dividend, distributable profits, share premium, interim dividend);
reducing-balance and straight-line depreciation numerics; provision for
doubtful debts; outstanding wages; returns outward; mark-up vs margin;
closing stock overstatement. Scanned against WAEC rounds 1-4, NECO
Accounting (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch131.py -> content/batch_131_waec_accounting5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_CON = "Accounting Concepts and Conventions"
T_ERR = "Errors and the Suspense Account"
T_NPO = "Non-Profit-Making Organisations"
T_MAN = "Manufacturing Accounts"
T_BILL = "Bills of Exchange Accounting"
T_PART = "Partnership Changes"
T_CO = "Company Accounts"
T_DEP = "Depreciation and Adjustments"
T_FIN = "Final Accounts Practice"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- concepts
    (T_CON, "Medium", "The concept that keeps the owner's private affairs out of the firm's books is",
     "business entity", "money measurement", "going concern", "dual aspect", "A",
     "The firm breathes with its own lungs."),
    (T_CON, "Hard", "Recognising expenses in the same period as the revenue they help to earn is the",
     "matching concept", "prudence concept", "realisation concept", "entity concept", "A",
     "Costs meet their own income."),
    (T_CON, "Hard", "The prudence concept directs that anticipated losses are",
     "provided for at once", "ignored until paid", "recorded when received", "shared with owners", "A",
     "Count losses early, gains late."),
    (T_CON, "Medium", "The going concern concept assumes the business will",
     "continue operating", "close next week", "be sold today", "shrink yearly", "A",
     "Tomorrow is assumed to come."),
    (T_CON, "Hard", "Under money measurement, records are limited to",
     "items with money value", "staff morale alone", "quality of service", "all human effort", "A",
     "What has no price stays out."),

    # ------------------------------------------------------------- errors and suspense
    (T_ERR, "Medium", "When the two sides of the trial balance refuse to agree, the accountant parks the difference in a",
     "suspense account", "cash book", "capital account", "control account", "A",
     "The difference waits there."),
    (T_ERR, "Hard", "Posting N5,000 to Ojo's account instead of Ojo-Bello's, both customers, is an error of",
     "commission", "principle", "omission", "compensation", "A",
     "Right amount, wrong customer."),
    (T_ERR, "Medium", "Entering N4,500 instead of N5,400 in the sales day book is an error of",
     "original entry", "commission", "principle", "complete reversal", "A",
     "The source figure was wrong."),
    (T_ERR, "Hard", "Omitting a credit sale from both the customer's account and the sales account leaves the trial balance totals",
     "not at all different", "higher by the sale price", "lower by the profit", "higher by the cost", "A",
     "Both sides drop by the same amount."),
    (T_ERR, "Medium", "Charging a new motor van to the motor expenses account is an error of",
     "principle", "commission", "omission", "original entry", "A",
     "Asset costs met expense accounts here."),

    # ------------------------------------------------------------- clubs
    (T_NPO, "Medium", "For a club, the statement showing assets and liabilities at the year end is the",
     "statement of affairs", "trial balance", "receipts statement", "income account", "A",
     "It serves as the balance sheet."),
    (T_NPO, "Hard", "Members' subscriptions due but unpaid at the year end are shown as",
     "a current asset", "a current liability", "a capital reserve", "an income surplus", "A",
     "The club is owed that money."),
    (T_NPO, "Medium", "For a social club, the account that plays the role of a company's profit and loss statement is the",
     "income and expenditure account", "receipts and payments account", "statement of affairs", "bar trading account", "A",
     "It measures the year's surplus."),
    (T_NPO, "Medium", "The surplus or deficit from running a members' bar is found in the",
     "bar trading account", "subscriptions account", "general fund", "bank account", "A",
     "Bar takings meet bar costs."),
    (T_NPO, "Hard", "The excess of a club's income over its expenditure for the year is carried to the",
     "accumulated fund", "profit and loss account", "share premium", "suspense account", "A",
     "It swells the club's own fund."),

    # ------------------------------------------------------------- manufacturing
    (T_MAN, "Medium", "Raw materials consumed, plus direct wages and other direct charges, make up",
     "prime cost", "factory cost", "conversion cost", "production cost", "A",
     "Only direct costs belong there."),
    (T_MAN, "Medium", "Direct materials N50,000; direct labour N30,000; factory overheads N20,000. Prime cost is",
     "N80,000", "N100,000", "N50,000", "N150,000", "A",
     "Materials plus labour only.", "80000"),
    (T_MAN, "Hard", "Opening work-in-progress N5,000; closing work-in-progress N8,000. The net adjustment to production cost is",
     "N3,000 deducted", "N3,000 added", "N13,000 added", "N13,000 deducted", "A",
     "Closing stock leaves the cost.", "3000"),
    (T_MAN, "Hard", "Which cost is NOT included in the cost of production?",
     "sales commission", "factory wages", "factory rent", "plant depreciation", "A",
     "Selling costs stay outside."),

    # ------------------------------------------------------------- bills
    (T_BILL, "Medium", "When a bill is discounted at the bank before maturity, the holder receives",
     "face value less discount", "face value plus discount", "proceeds plus interest", "nothing until maturity", "A",
     "The bank takes its cut early."),
    (T_BILL, "Hard", "On the dishonour of a bill, the drawer debits the",
     "acceptor's account", "bank account", "bills payable", "discount account", "A",
     "The debtor owes him again."),
    (T_BILL, "Medium", "Paying off a bill before its maturity date for less than its face value is called",
     "retirement", "renewal", "discounting", "dishonour", "A",
     "An early exit earns a rebate."),

    # ------------------------------------------------------------- partnership
    (T_PART, "Medium", "On admitting a new partner, goodwill written off after adjustment is shared in the",
     "new profit-sharing ratio", "the old ratio", "the capital ratio", "the salary ratio", "A",
     "The fresh team shares it."),
    (T_PART, "Hard", "In a dissolution, the account that gathers the sale of all the firm's assets is the",
     "realisation account", "revaluation account", "capital account", "suspense account", "A",
     "Everything passes through it."),
    (T_PART, "Medium", "In a partnership keeping current accounts, salary due to a partner is credited to his",
     "current account", "capital account", "loan account", "trading account", "A",
     "Appropriations flow through it."),
    (T_PART, "Hard", "Where there is no agreement, a partner's loan to the firm attracts interest of",
     "5% per annum", "10% per annum", "15% per annum", "no interest at all", "A",
     "The Act allows a modest five."),

    # ------------------------------------------------------------- company
    (T_CO, "Medium", "Debenture interest differs from dividend because it is",
     "an expense of the company", "an appropriation of profit", "paid only to founders", "never tax deductible", "A",
     "It is owed come rain or loss."),
    (T_CO, "Hard", "Dividends are properly declared out of",
     "distributable profits", "share premium", "the company's capital", "loan notes", "A",
     "Capital itself stays intact."),
    (T_CO, "Medium", "Share premium arises when shares are issued",
     "above face value", "below face value", "at face value", "free of charge", "A",
     "Buyers paid something over the par value."),
    (T_CO, "Hard", "An interim dividend is one paid",
     "during the financial year", "only when winding up", "before the firm exists", "after the final one", "A",
     "A mid-course taste of profit."),

    # ------------------------------------------------------------- depreciation
    (T_DEP, "Medium", "A machine costs N100,000 and depreciation is 20% on reducing balance. The second year's depreciation is",
     "N16,000", "N20,000", "N40,000", "N4,000", "A",
     "Twenty per cent of N80,000.", "16000"),
    (T_DEP, "Medium", "Furniture cost N60,000, scrap value N10,000, life 5 years. Annual straight-line depreciation is",
     "N10,000", "N12,000", "N50,000", "N2,000", "A",
     "Fifty thousand spread over five.", "10000"),
    (T_DEP, "Medium", "The yearly provision for doubtful debts is normally based on",
     "debtors less bad debts", "gross sales of the year", "cash sales alone", "the creditors balance", "A",
     "Only the net recoverable count."),
    (T_DEP, "Hard", "Outstanding wages at the year end appear in the balance sheet as",
     "a current liability", "a fixed asset", "a current asset", "capital", "A",
     "Owed work must be paid soon."),

    # ------------------------------------------------------------- final accounts
    (T_FIN, "Medium", "In the trading account, returns outward is deducted from",
     "purchases", "sales", "debtors", "stock", "A",
     "Goods sent back cut the cost."),
    (T_FIN, "Hard", "While margin is computed on sales, mark-up is computed on",
     "cost of goods sold", "net profit", "capital employed", "total assets", "A",
     "Cost carries the mark-up."),
    (T_FIN, "Medium", "Depreciation of office equipment in a trading firm is charged to the",
     "profit and loss account", "trading account", "manufacturing account", "balance sheet only", "A",
     "Office wear meets office profit."),
    (T_FIN, "Hard", "If closing stock is overstated, the gross profit will be",
     "overstated", "understated", "unaffected", "doubled", "A",
     "Cheap goods swell the margin."),
]

build_batch(
    S,
    "batch_131_waec_accounting5.json",
    "131",
    "WAEC Financial Accounting round 5 (Round 25 top-up): business "
    "entity, matching, prudence, going concern, money measurement; "
    "suspense account; errors of commission, original entry and "
    "principle; complete omission's nil trial-balance effect; club "
    "statement of affairs, subscriptions in arrears, income and "
    "expenditure account, bar trading account, accumulated fund; prime "
    "cost N80,000; WIP adjustment N3,000 deducted; sales commission "
    "outside production cost; bill discounting proceeds, dishonour "
    "debit, retirement rebate; admission goodwill in new ratio, "
    "realisation account, partner salary to current account, 5% loan "
    "interest; debenture interest as expense, dividends from "
    "distributable profits, share premium above par, interim dividend; "
    "reducing balance N16,000, straight line N10,000, doubtful-debt "
    "provision base, outstanding wages liability; returns outward off "
    "purchases, mark-up on cost, office depreciation in P&L, overstated "
    "closing stock. Scanned against WAEC rounds 1-4, NECO Accounting "
    "(all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
