"""Batch 111 - NECO Financial Accounting round 3 (NECO top-up, Round 22).

Lifts NECO Accounting from 102 toward ~150 with angles not yet in any
bank: partnership accounts (appropriation, current accounts, goodwill,
dissolution basics), non-profit organisations (receipts and payments vs
income and expenditure, subscriptions, accumulated fund), incomplete
records (statement of affairs, markup and margin), further ratios
(stock turnover, return on capital, rate of stock turn), public sector
basics (recurrent vs capital, vote, treasury) and single-entry
limitations. Scanned against NECO rounds 1-2, WAEC Accounting (all
rounds) and the JAMB pool.

    python3 scripts/build_neco_batch111.py -> content/batch_111_neco_accounting3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_PART = "Partnership Accounts"
T_NPO = "Non-Profit Organisations"
T_INC = "Incomplete Records"
T_RAT = "Further Ratios"
T_PUB = "Public Sector Accounting"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- partnership
    (T_PART, "Medium", "The part of profit set aside as each partner's share is credited to his",
     "current account", "capital account only", "drawings account", "suspense account", "A",
     "Current accounts carry the flow."),
    (T_PART, "Medium", "Interest on drawings is debited to the partner and credited to the",
     "appropriation account", "sales account", "goodwill account", "bank account only", "A",
     "It claws a reward back into profit."),
    (T_PART, "Hard", "Partners' salaries are dealt with in the profit and loss",
     "appropriation account", "trading account", "balance sheet only", "revaluation account", "A",
     "Sharing profit comes after it."),
    (T_PART, "Hard", "Profits of N240,000 shared in the ratio 3:2:1 give the first partner",
     "N120,000", "N80,000", "N96,000", "N60,000", "A",
     "Half of the profit is his.", "240000*3/6"),
    (T_PART, "Medium", "Interest a partner earns on his capital is",
     "an appropriation of profit", "a trading expense", "a liability of the bank", "a fixed asset", "A",
     "It shares profit, not costs."),
    (T_PART, "Hard", "Excess of a partner's drawings over his share of profit leaves a",
     "debit current-account balance", "credit current-account balance", "credit capital only", "nil balance always", "A",
     "He has drawn more than he earned."),
    (T_PART, "Medium", "Goodwill in partnership is best described as",
     "the firm's good name", "the value of its buildings", "the cash at bank", "the stock on shelves", "A",
     "Good name is worth money."),
    (T_PART, "Hard", "When a new partner pays for a share of goodwill, the amount is credited to the",
     "old partners' capital accounts", "new partner's drawings", "purchases account", "bank only", "A",
     "The sellers keep the payment."),
    (T_PART, "Hard", "On dissolution, amounts realised from selling the firm's assets go first to",
     "paying the creditors", "the partners equally", "the bank charges only", "new investments", "A",
     "Outsiders are settled first."),

    # ------------------------------------------------------------- non-profit
    (T_NPO, "Medium", "A club's statement of receipts and payments is drawn from the",
     "cash book", "income and expenditure account", "balance sheet", "bank statement only", "A",
     "Only cash items can appear in it."),
    (T_NPO, "Medium", "Which business statement does a club's income and expenditure account mirror?",
     "profit and loss account", "trading account", "cash book", "bank reconciliation", "A",
     "Surplus or deficit ends it."),
    (T_NPO, "Hard", "The equivalent of capital in a club's balance sheet is the",
     "accumulated fund", "share premium", "goodwill", "loan stock", "A",
     "Members' build-up over years."),
    (T_NPO, "Hard", "Subscriptions paid in advance by members are shown as a",
     "current liability", "current asset", "fixed asset", "capital reserve", "A",
     "Next year's income already taken."),
    (T_NPO, "Medium", "Subscriptions owing but unpaid at year end belong among the",
     "accrued incomes (assets)", "current liabilities", "reserves", "deferred expenses", "A",
     "The money is still coming."),
    (T_NPO, "Hard", "A club's bar trading account computes the",
     "bar surplus or deficit", "members' total wealth", "bank balance", "entrance fees only", "A",
     "Drink sales meet drink costs."),
    (T_NPO, "Medium", "Entrance fees paid by new members are normally",
     "income for the year", "capital receipts only", "ignored in the books", "a liability forever", "A",
     "They help to fund the year."),

    # ------------------------------------------------------------- incomplete records
    (T_INC, "Medium", "Single entry bookkeeping's biggest weakness is that it",
     "lacks a full double record", "needs no cash book", "cannot record cash", "suits only companies", "A",
     "One side of a record goes missing."),
    (T_INC, "Hard", "Under single entry, the owner's opening capital is found in the",
     "statement of affairs", "sales day book", "petty cash book", "wage sheet", "A",
     "It lists assets and liabilities."),
    (T_INC, "Hard", "A trader's capital rose from N300,000 to N410,000 while he drew out N70,000; his profit was",
     "N180,000", "N110,000", "N70,000", "N240,000", "A",
     "Capital grew by profit less drawings.", "410000-300000+70000"),
    (T_INC, "Medium", "Mark-up is calculated on",
     "cost price", "selling price", "market price", "replacement price", "A",
     "Profit over what it cost."),
    (T_INC, "Medium", "Margin is calculated on",
     "selling price", "cost price", "buying price", "trade price", "A",
     "Profit inside the ticket."),
    (T_INC, "Hard", "Cost N80,000 with a mark-up of 25% gives a selling price of",
     "N100,000", "N105,000", "N96,000", "N120,000", "A",
     "Add a quarter of the cost.", "80000*1.25"),
    (T_INC, "Hard", "If margin is 20%, then mark-up is",
     "25%", "20%", "80%", "15%", "A",
     "One-fifth of sales is a quarter of cost."),

    # ------------------------------------------------------------- ratios
    (T_RAT, "Medium", "Cost of goods sold divided by average stock gives the",
     "rate of stock turnover", "current ratio", "gross margin", "gearing", "A",
     "How often stock is sold out."),
    (T_RAT, "Hard", "Cost of sales N600,000 and average stock N150,000 give stock turnover of",
     "4 times", "2 times", "6 times", "8 times", "A",
     "Divide cost by the average stock.", "600000/150000"),
    (T_RAT, "Hard", "Net profit N150,000 on capital of N750,000 gives a return on capital of",
     "20%", "15%", "25%", "10%", "A",
     "Profit over the capital employed."),
    (T_RAT, "Medium", "A high stock turnover usually signals",
     "fast-moving goods", "overpriced stock", "a large warehouse", "heavy borrowing", "A",
     "Shelves empty and refill quickly."),
    (T_RAT, "Medium", "A current ratio far above 2 may suggest",
     "idle short-term resources", "certain bankruptcy", "no creditors at all", "zero sales", "A",
     "Too much money sits idle."),

    # ------------------------------------------------------------- public sector
    (T_PUB, "Medium", "Government spending on salaries and rent is classified as",
     "recurrent expenditure", "capital expenditure", "capital receipt", "deferred income", "A",
     "Such spending repeats every year."),
    (T_PUB, "Medium", "Spending on new roads and school buildings is",
     "capital expenditure", "recurrent expenditure", "a contingent liability", "a reserve", "A",
     "Long-life assets are built."),
    (T_PUB, "Hard", "The amount approved for a ministry's spending in a year is its",
     "vote", "budget surplus", "warrant only", "subhead zero", "A",
     "No spending beyond the vote."),
    (T_PUB, "Medium", "The government officer who controls the issue of public funds is the",
     "Accountant-General", " Auditor-General", "Statistician-General", "Surveyor-General", "A",
     "The treasury's chief keeper."),
    (T_PUB, "Hard", "The constitutionally independent checker of public accounts is the",
     "Auditor-General", "Accountant-General", "Central Bank", "Minister of Finance", "A",
     "He audits the books without fear."),
    (T_PUB, "Medium", "Public sector accounts are kept mainly to show",
     "stewardship of public funds", "profit maximisation", "dividend targets", "share values", "A",
     "Trustees must give account."),
    (T_PUB, "Hard", "The fund from which state governments share monthly allocations is the",
     "Federation Account", "Consolidated Fund only", "Development Fund", "Petroleum Fund", "A",
     "FAAC shares from it monthly."),
]

build_batch(
    S,
    "batch_111_neco_accounting3.json",
    "111",
    "NECO Financial Accounting round 3 (Round 22 top-up): partnership "
    "current accounts, interest on drawings and capital, salaries in the "
    "appropriation account, ratio sharing (N120,000), goodwill payments "
    "to old partners, dissolution order of payment, club receipts and "
    "payments vs income and expenditure, accumulated fund, subscriptions "
    "prepaid and accrued, bar trading, entrance fees, single-entry "
    "weakness, statement of affairs, profit from capital movement "
    "(N180,000), mark-up vs margin (25% on cost = 20% margin), selling "
    "price N100,000, stock turnover 4x, return on capital 20%, high "
    "turnover and over-high current ratio signals, recurrent vs capital "
    "spending, votes, Accountant-General vs Auditor-General, stewardship "
    "and the Federation Account. Scanned against NECO rounds 1-2, WAEC "
    "Accounting (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
