"""Batch 207 - WAEC Financial Accounting round 8 (WAEC top-up, R41).

Grows WAEC Accounting from 258 toward ~280 with angles not yet in
the bank: issued capital; called-up capital; the rights issue;
the credit note; internal audit; the historical cost concept; the
accrual concept; the matching concept; the cash book's double
role; the ledger's personal, real and nominal divisions; the
balance sheet as a statement; retained earnings; the provision
increase charged to P&L; fixed capital; fluctuating capital;
partnership salaries in the appropriation account; the sinking
fund; amortisation; the post-dated cheque; the AGM; shareholders'
limited liability; under-subscription. Scanned against the whole
Accounting pool (WAEC, NECO and JAMB stems, 518 items).

    python3 scripts/build_neco_batch207.py -> content/batch_207_waec_acct8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_CMP = "Company Accounts"
T_CON = "Accounting Concepts"
T_BOOK = "Books of Account"
T_BSH = "The Balance Sheet"
T_PAR = "Partnership Accounts"
T_DEP = "Depreciation and Funds"
T_GEN = "General Topics"

PASSAGES = []
PQ = []

Q = [
    (T_CMP, "Medium", "Of a company's authorised share capital, the portion that has actually been offered to the public for sale is the",
     "issued capital", "reserved capital",
     "called-up capital", "paid-up capital", "A",
     "What is offered may be less than what is authorised."),
    (T_CMP, "Hard", "The part of the issued capital on which shareholders have actually been asked to pay is the",
     "called-up capital", "issued capital",
     "nominal capital", "capital reserve", "A",
     "The company calls for payment in instalments."),
    (T_CMP, "Medium", "New shares offered first to existing shareholders in proportion to their holdings, usually below market price, make up a",
     "rights issue", "bonus issue",
     "private placing", "offer for sale", "A",
     "The old owners keep control and buy cheap."),
    (T_GEN, "Easy", "The document a seller sends out to reduce the amount a customer owes him, say for goods returned, is a",
     "credit note", "debit note",
     "invoice", "pro-forma invoice", "A",
     "It credits the customer's account in the seller's books."),
    (T_GEN, "Hard", "The continuous examination of a company's books by its own staff, as an aid to management, is called",
     "internal audit", "external audit",
     "interim audit", "balance sheet audit", "A",
     "The firm's own auditors watch the books all year."),
    (T_CON, "Medium", "The concept which requires assets to be recorded in the books at the amount originally paid for them is",
     "historical cost", "replacement cost",
     "realisable value", "going concern", "A",
     "The ledger keeps the original purchase price."),
    (T_CON, "Hard", "Under this concept, expenses are recognised in the period in which they are incurred, whether or not cash has yet been paid. It is the",
     "accrual concept", "cash basis concept",
     "realisation concept", "prudence concept", "A",
     "The bill belongs to the month it was earned."),
    (T_CON, "Hard", "The matching concept requires the cost of a fixed asset to be spread over",
     "the years it helps to earn revenue", "the year of purchase alone",
     "the year of its sale", "the months of peak output", "A",
     "Each year bears its fair share of the cost."),
    (T_BOOK, "Medium", "The cash book is unusual among the books of a business because it serves as",
     "both a book of prime entry and a ledger", "only a book of prime entry",
     "only a ledger account", "part of the journal proper", "A",
     "Cash is entered first and balanced in the same book."),
    (T_BOOK, "Medium", "Ledger accounts are traditionally divided into personal accounts and",
     "real and nominal accounts", "cash and bank accounts",
     "trading and P&L accounts", "debit and credit accounts", "A",
     "Real accounts hold assets, nominal hold expenses."),
    (T_BSH, "Medium", "Unlike the trading and profit and loss accounts, the balance sheet is properly described as",
     "a statement and not an account", "an account of balances",
     "a book of original entry", "a subsidiary book", "A",
     "It lists balances; it does not collect them."),
    (T_CMP, "Medium", "The profits of a company kept back for the use of the business instead of being paid out as dividends are called",
     "retained earnings", "share premium",
     "redemption reserve", "sinking funds", "A",
     "Undistributed profit ploughed back into the firm."),
    (T_GEN, "Hard", "At year end the provision for doubtful debts is raised from N2,000 to N3,000. The profit and loss account is charged with",
     "N1,000", "N2,000",
     "N3,000", "N5,000", "A",
     "Only the increase is charged, not the whole balance.", "1000"),
    (T_PAR, "Medium", "In partnership accounts, the capital account that stays the same year after year, all changes going to the current account, is the",
     "fixed capital account", "fluctuating capital account",
     "current account", "appropriation account", "A",
     "Capital stands still; the swings hit current."),
    (T_PAR, "Hard", "Where each partner keeps a single capital account into which capital, profits, drawings and interest are all entered, the capital is said to be",
     "fluctuating", "fixed",
     "permanent", "unappropriated", "A",
     "One account swallows every movement."),
    (T_PAR, "Medium", "The salary due to a partner for active service is transferred to his current account from the",
     "appropriation account", "trading account",
     "profit and loss account", "revaluation account", "A",
     "Profit sharing begins after such rewards."),
    (T_DEP, "Hard", "The fund built up by setting aside cash yearly, invested at interest, to replace an asset at the end of its life is a",
     "sinking fund", "reserve fund",
     "provision fund", "renewal reserve", "A",
     "Compound interest helps to buy the new machine."),
    (T_DEP, "Medium", "The writing off of the cost of a lease or a patent over its legal life, in the manner of depreciation, is called",
     "amortisation", "depletion",
     "obsolescence", "appreciation", "A",
     "Leases and patents fade with the years."),
    (T_GEN, "Easy", "A cheque that bears a future date, so that it cannot be cashed until that day, is said to be",
     "post-dated", "anti-dated",
     "crossed", "stale", "A",
     "The bank must wait for the date written on it."),
    (T_CMP, "Easy", "The yearly meeting of a company at which the directors present the accounts and the shareholders vote is the",
     "annual general meeting", "extraordinary general meeting",
     "statutory meeting", "board meeting", "A",
     "Once a year the owners examine the stewards."),
    (T_CMP, "Medium", "If a limited company fails, the shareholder stands to lose only",
     "the amount unpaid on his shares", "his personal house and car",
     "the whole company's debts", "his dividends alone", "A",
     "His liability stops at his investment."),
    (T_CMP, "Medium", "When the public applies for fewer shares than a company has offered, the issue is said to be",
     "under-subscribed", "over-subscribed",
     "fully subscribed", "privately placed", "A",
     "The share list returns partly empty."),
]

build_batch(
    S,
    "batch_207_waec_acct8.json",
    "207",
    "WAEC Financial Accounting round 8 (R41 top-up): issued "
    "capital; called-up capital; rights issue; credit note; "
    "internal audit; historical cost; accrual concept; matching "
    "concept; the cash book's double role; personal, real and "
    "nominal accounts; the balance sheet as a statement; retained "
    "earnings; provision increase charged to P&L; fixed capital "
    "account; fluctuating capital; partner's salary via "
    "appropriation; sinking fund; amortisation of a lease; the "
    "post-dated cheque; the AGM; shareholders' limited liability; "
    "under-subscription. Scanned against the whole Accounting pool "
    "(WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
